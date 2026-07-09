from __future__ import annotations
import ast
import base64
import html
import importlib.util
import io
import os
import re
import runpy
import shlex
import signal
import sys
import threading
import traceback
from contextlib import redirect_stderr, redirect_stdout
from dataclasses import dataclass, field
from pathlib import Path
from types import ModuleType

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
IGNORE_DIRS = {".venv", "__pycache__", ".git", ".gemini"}
IGNORE_FILES = {"streamlit_app.py", "graph_script_template.py", "__init__.py"}
DATA_EXTENSIONS = {".txt", ".json", ".csv"}

st.write("To C or not to C that is the question")


# input_type controls what the "Run with custom graph" section renders:
#   "graph"           – adjacency matrix + pos dict  (most experiments)
#   "degree_sequence" – only a degree sequence list   (exp 5)
#   None              – no custom-input section yet


EXP_CONFIG: dict[str, dict] = {
    "1":  {"input_type": "graph", "graph_count": 1, "weighted": False},
    "2":  {"input_type": "graph", "graph_count": 3, "weighted": False},
    "3":  {"input_type": "graph", "graph_count": 1, "weighted": False},
    "4":  {"input_type": "degree_sequence"},
    "5":  {"input_type": "graph", "graph_count": 1, "weighted": False},
    "6":  {"input_type": "graph", "graph_count": 1, "weighted": True},   # -1 sentinel
    "7":  {"input_type": "graph", "graph_count": 1, "weighted": True},   # inf sentinel
    "8":  {"input_type": "graph", "graph_count": 1, "weighted": False},
    "9":  {"input_type": "graph", "graph_count": 1, "weighted": False},
    "10": {"input_type": "graph", "graph_count": 1, "weighted": False},
    "11": {"input_type": "graph", "graph_count": 1, "weighted": False},
}

@dataclass
class RunResult:
    mode: str           # "demo" | "custom"
    stdout: str
    stderr: str
    exit_code: int | None
    timed_out: bool = False
    error: str | None = None
    figures: list[object] = field(default_factory=list)


@dataclass
class GraphSummary:
    label: str
    nodes: list[str]
    edges: list[tuple[str, ...]]
    directed: bool
    multigraph: bool


def iter_files(base_dir: Path, extensions: set[str]) -> list[Path]:
    files: list[Path] = []
    for root, dirs, filenames in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for name in filenames:
            path = Path(root) / name
            if path.suffix.lower() not in extensions:
                continue
            files.append(path)
    return files


def find_projects(base_dir: Path) -> dict[str, Path]:
    projects: dict[str, Path] = {}
    for entry in sorted(base_dir.iterdir(), key=lambda e: (not e.name.isdigit(), int(e.name) if e.name.isdigit() else float("inf"), e.name)):
        if not entry.is_dir():
            continue
        if entry.name in IGNORE_DIRS:
            continue
        main_file = entry / "main.py"
        if main_file.exists():
            projects[entry.name] = main_file
    return projects


def find_data_files(base_dir: Path) -> list[Path]:
    files = iter_files(base_dir, DATA_EXTENSIONS)
    files.sort(key=lambda p: p.relative_to(base_dir).as_posix().lower())
    return files


def read_source(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        return f"# Unable to read file: {exc}"


@st.cache_data(show_spinner=False)
def load_logo_base64(path: Path) -> str | None:
    try:
        return base64.b64encode(path.read_bytes()).decode("ascii")
    except OSError:
        return None


@st.cache_data(show_spinner=False)
def load_theory_markdown(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _setup_mpl() -> None:
    """Force Agg backend and suppress plt.show() before any script runs."""
    try:
        import matplotlib
        matplotlib.use("Agg", force=True)
        import matplotlib.pyplot as plt
        plt.close("all")
        plt.show = lambda *a, **k: None
    except Exception:
        pass


def _env_context(path: Path):
    """Return a dict of saved originals and set up the execution environment."""
    saved = {
        "cwd": os.getcwd(),
        "argv": sys.argv[:],
        "stdin": sys.stdin,
        "path": sys.path[:],
        "mplbackend": os.environ.get("MPLBACKEND"),
    }
    os.environ["MPLBACKEND"] = "Agg"
    os.chdir(path.parent)
    sys.argv = [str(path)]
    sys.stdin = io.StringIO("")
    sys.path.insert(0, str(path.parent))
    return saved


def _restore_env(saved: dict) -> None:
    os.chdir(saved["cwd"])
    sys.argv = saved["argv"]
    sys.stdin = saved["stdin"]
    sys.path = saved["path"]
    if saved["mplbackend"] is None:
        os.environ.pop("MPLBACKEND", None)
    else:
        os.environ["MPLBACKEND"] = saved["mplbackend"]


def load_experiment_module(path: Path) -> tuple[ModuleType | None, str | None]:
    """
    Import the experiment's main.py as a module and return it.
    Returns (module, error_string). The module's top-level code is NOT run;
    only its function definitions are loaded.
    """
    spec = importlib.util.spec_from_file_location("_exp_module", str(path))
    if spec is None or spec.loader is None:
        return None, "Could not create module spec."
    mod = importlib.util.module_from_spec(spec)
    saved = _env_context(path)
    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    try:
        _setup_mpl()
        with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
            spec.loader.exec_module(mod)  # type: ignore[attr-defined]
        return mod, None
    except Exception:
        return None, traceback.format_exc()
    finally:
        _restore_env(saved)
        
        
def _collect_figures() -> list[object]:
    try:
        import matplotlib.pyplot as plt
        return [plt.figure(num) for num in plt.get_fignums()]
    except Exception:
        return []


def call_function(
    path: Path,
    func_name: str,        # "main" or "run"
    func_args: tuple = (),
    func_kwargs: dict | None = None,
    timeout: int = 60,
) -> RunResult:
    """
    Load the experiment module and call func_name(*func_args, **func_kwargs).
    Captures stdout, stderr, and matplotlib figures.
    """
    if func_kwargs is None:
        func_kwargs = {}

    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    result = RunResult(mode="demo" if func_name == "main" else "custom",
                       stdout="", stderr="", exit_code=None)

    supports_alarm = (
        hasattr(signal, "SIGALRM")
        and threading.current_thread() is threading.main_thread()
    )
    original_alarm = signal.getsignal(signal.SIGALRM) if supports_alarm else None

    def _handle_timeout(_signum: int, _frame) -> None:
        raise TimeoutError(f"Timed out after {timeout} seconds.")

    saved = _env_context(path)
    try:
        _setup_mpl()

        if supports_alarm:
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(timeout)

        mod, load_err = load_experiment_module(path)
        if load_err:
            result.exit_code = 1
            result.error = load_err
            return result

        func = getattr(mod, func_name, None)
        if func is None:
            result.exit_code = 1
            result.error = f"Function '{func_name}()' not found in {path.name}."
            return result

        with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
            try:
                func(*func_args, **func_kwargs)
                result.exit_code = 0
            except SystemExit as exc:
                result.exit_code = 0 if exc.code in (None, 0) else 1
            except TimeoutError as exc:
                result.timed_out = True
                result.error = str(exc)
            except Exception:
                result.exit_code = 1
                result.error = traceback.format_exc()
    finally:
        if supports_alarm and original_alarm is not None:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, original_alarm)
        _restore_env(saved)

    result.stdout = stdout_buf.getvalue()
    result.stderr = stderr_buf.getvalue()
    result.figures = _collect_figures()
    return result


def _safe_sorted(values: list[object]) -> list[object]:
    try:
        return sorted(values)
    except TypeError:
        return sorted(values, key=str)


def _format_nodes(nodes: list[object]) -> list[str]:
    return [str(n) for n in _safe_sorted(nodes)]


def _format_edges(edges: list[tuple[object, ...]]) -> list[tuple[str, ...]]:
    formatted = [tuple(str(p) for p in e) for e in edges]
    return sorted(formatted, key=str)


def _format_edge_lines(edges: list[tuple[str, ...]], directed: bool) -> list[str]:
    connector = " -> " if directed else " -- "
    lines: list[str] = []
    for edge in edges:
        if len(edge) >= 2:
            line = f"{edge[0]}{connector}{edge[1]}"
            if len(edge) > 2:
                line = f"{line} ({', '.join(edge[2:])})"
        else:
            line = ", ".join(edge)
        lines.append(line)
    return lines


def extract_graph_summaries(path: Path) -> tuple[list[GraphSummary], str | None]:
    """
    Monkey-patches nx graph classes to capture any graphs constructed during
    main(). Falls back to running the whole module if main() is absent.
    """
    stdout_buf = io.StringIO()
    stderr_buf = io.StringIO()
    summaries: list[GraphSummary] = []
    error: str | None = None

    supports_alarm = (
        hasattr(signal, "SIGALRM")
        and threading.current_thread() is threading.main_thread()
    )
    original_alarm = signal.getsignal(signal.SIGALRM) if supports_alarm else None

    def _handle_timeout(_signum, _frame):
        raise TimeoutError("Timed out after 20 seconds.")

    saved = _env_context(path)
    try:
        try:
            import networkx as nx
        except Exception as exc:
            return [], f"NetworkX unavailable ({exc})"

        registry: list[object] = []
        capture_state = {"enabled": True}

        def _no_capture(func):
            capture_state["enabled"] = False
            try:
                return func()
            finally:
                capture_state["enabled"] = True

        orig_G   = nx.Graph
        orig_DG  = nx.DiGraph
        orig_MG  = nx.MultiGraph
        orig_MDG = nx.MultiDiGraph

        class _CG(orig_G):
            def __init__(self, *a, **k):
                super().__init__(*a, **k)
                if capture_state["enabled"]: registry.append(self)
            def copy(self, as_view=False): return _no_capture(lambda: super().copy(as_view=as_view))
            def subgraph(self, n): return _no_capture(lambda: super().subgraph(n))

        class _CDG(orig_DG):
            def __init__(self, *a, **k):
                super().__init__(*a, **k)
                if capture_state["enabled"]: registry.append(self)
            def copy(self, as_view=False): return _no_capture(lambda: super().copy(as_view=as_view))
            def subgraph(self, n): return _no_capture(lambda: super().subgraph(n))

        class _CMG(orig_MG):
            def __init__(self, *a, **k):
                super().__init__(*a, **k)
                if capture_state["enabled"]: registry.append(self)
            def copy(self, as_view=False): return _no_capture(lambda: super().copy(as_view=as_view))
            def subgraph(self, n): return _no_capture(lambda: super().subgraph(n))

        class _CMDG(orig_MDG):
            def __init__(self, *a, **k):
                super().__init__(*a, **k)
                if capture_state["enabled"]: registry.append(self)
            def copy(self, as_view=False): return _no_capture(lambda: super().copy(as_view=as_view))
            def subgraph(self, n): return _no_capture(lambda: super().subgraph(n))

        nx.Graph = _CG
        nx.DiGraph = _CDG
        nx.MultiGraph = _CMG
        nx.MultiDiGraph = _CMDG

        try:
            _setup_mpl()
            if supports_alarm:
                signal.signal(signal.SIGALRM, _handle_timeout)
                signal.alarm(20)

            with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
                try:
                    globs = runpy.run_path(str(path), run_name="__main__")
                    main_fn = globs.get("main")
                    if main_fn is not None:
                        main_fn()
                except SystemExit:
                    pass
        except TimeoutError as exc:
            error = str(exc)
        except Exception as exc:
            error = f"{type(exc).__name__}: {exc}"
        finally:
            nx.Graph = orig_G
            nx.DiGraph = orig_DG
            nx.MultiGraph = orig_MG
            nx.MultiDiGraph = orig_MDG
        seen: set = set()
        for graph in registry:
            nodes = _format_nodes(list(graph.nodes()))
            edges_raw = list(graph.edges(keys=True)) if graph.is_multigraph() else list(graph.edges())
            edges = _format_edges(edges_raw)
            sig = (tuple(nodes), tuple(edges))
            if sig in seen:
                continue
            seen.add(sig)
            label = graph.graph.get("name") if isinstance(getattr(graph, "graph", None), dict) else None
            summaries.append(GraphSummary(
                label=label or f"Graph {len(summaries) + 1}",
                nodes=nodes,
                edges=edges,
                directed=graph.is_directed(),
                multigraph=graph.is_multigraph(),
            ))
    finally:
        if supports_alarm and original_alarm is not None:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, original_alarm)
        _restore_env(saved)

    return summaries, error


def get_graph_summaries(path_str: str, modified_at: float) -> tuple[list[GraphSummary], str | None]:
    cache_key = f"graph_summary_{path_str}_{modified_at}"
    if cache_key not in st.session_state:
        st.session_state[cache_key] = extract_graph_summaries(Path(path_str))
    return st.session_state[cache_key]


def terminal_block(text: str) -> str:
    escaped = html.escape(text)
    return f"<div class='terminal'><pre>{escaped}</pre></div>"


def clean_stderr(stderr: str) -> str:
    if not stderr:
        return ""
    ignored = ("FigureCanvasAgg is non-interactive",)
    lines = [l for l in stderr.splitlines() if not any(t in l for t in ignored)]
    return "\n".join(lines).strip()


def render_result(result: RunResult) -> None:
    """Render a RunResult (stdout, errors, figures) into the current column."""
    label = "Demo" if result.mode == "demo" else "Custom run"
    if result.timed_out:
        st.error(result.error or "Process timed out.")
    elif result.exit_code not in (0, None):
        st.error(f"{label} — exit code: {result.exit_code}")
    else:
        st.success(f"{label} completed.")

    if result.error and not result.timed_out:
        st.code(result.error, language="text")

    combined = result.stdout.strip()
    cleaned_stderr = clean_stderr(result.stderr)
    if cleaned_stderr:
        combined = f"{combined}\n\n[stderr]\n{cleaned_stderr}".strip()
    if combined:
        st.markdown(terminal_block(combined), unsafe_allow_html=True)

    if result.figures:
        st.markdown("#### Visualization")
        for fig in result.figures:
            st.pyplot(fig, use_container_width=True)


def render_custom_input(exp_number: str) -> tuple[bool, dict]:
    """
    Render the input widgets for the given experiment.
    Returns (ready, params) where params will be unpacked into run(**params).

    Each experiment that needs special handling has its own branch.
    The generic branches cover graph-input and degree-sequence-input.
    """
    cfg = EXP_CONFIG.get(exp_number, {})
    input_type = cfg.get("input_type")

    if input_type is None:
        st.info("No custom input defined for this experiment yet.")
        return False, {}
    if exp_number == "1":        
        pass  # generic graph input below
    elif exp_number == "2":
        pass  # generic graph input below

    elif exp_number == "3":
        pass  # generic graph input below

    elif exp_number == "4":
        pass  # generic graph input below

    elif exp_number == "5":
        pass  # degree sequence input below

    elif exp_number == "6":
        pass  # generic graph input below

    elif exp_number == "7":
        pass  # generic graph input below

    elif exp_number == "8":
        pass  # generic graph input below

    elif exp_number == "9":
        pass  # generic graph input below

    elif exp_number == "10":
        pass  # generic graph input below

    elif exp_number == "11":
        pass  # generic graph input below

    # ------------------------------------------------------------------
    # Generic input rendering based on input_type
    # ------------------------------------------------------------------
    if input_type == "graph":
        graph_count = cfg.get("graph_count", 1)
        weighted = cfg.get("weighted", False)
        return _render_graph_input(graph_count, weighted)
    if input_type == "degree_sequence":
        return _render_degree_sequence_input()

    return False, {}


def _render_graph_input(graph_count: int = 1, weighted: bool = False) -> tuple[bool, dict]:
    if graph_count == 1:
        return _render_visjs_canvas(canvas_key="single", weighted=weighted)

    tabs = st.tabs([f"Graph {i+1}" for i in range(graph_count)])
    matrices, positions = [], []
    for i, tab in enumerate(tabs):
        with tab:
            ready, data = _render_visjs_canvas(
                canvas_key=f"multi_{i}", weighted=weighted
            )
            if not ready:
                return False, {}
            matrices.append(data["g"])
            positions.append(data["pos"])

    return True, {"graphs": matrices, "positions": positions}
    
def _render_degree_sequence_input() -> tuple[bool, dict]:
    """
    Degree-sequence input for Exp 5.
    Returns (ready, {"degree_sequence": list[int]}).
    """
    st.markdown("**Degree sequence** — space-separated integers, e.g. `3 3 2 2 2`")
    seq_text = st.text_input("degree_sequence", value="3 3 2 2 2", label_visibility="collapsed")
    try:
        seq = [int(x) for x in seq_text.split()]
    except Exception:
        st.warning("Enter space-separated integers.")
        return False, {}

    if sum(seq) % 2 != 0:
        st.warning("Sum of degrees must be even (Erdős–Gallai condition).")
        return False, {}

    return True, {"degree_sequence": seq}
    
    
def _render_visjs_canvas(canvas_key: str, weighted: bool = False) -> tuple[bool, dict]:
    import json
    import numpy as np

    json_input_key = f"visjs_json_{canvas_key}"
    html_path = BASE_DIR / "static" / "graph_builder.html"
    html = html_path.read_text(encoding="utf-8")
    html = html.replace(
    "var WEIGHTED = false;",
    f"var WEIGHTED = {str(weighted).lower()};"
    )
    st.components.v1.html(
    html,
    height=460,
    scrolling=False,
    )
    st.caption("After clicking Confirm above, copy the JSON and paste it here:")
    json_text = st.text_area(
        label="graph_json",
        value=st.session_state.get(json_input_key, ""),
        height=80,
        placeholder='{"matrix": [[0,1],[1,0]], "pos": {"0":[0,1],"1":[1,0]}}',
        label_visibility="collapsed",
        key=json_input_key,
    )

    if not json_text.strip():
        return False, {}

    try:
        parsed = json.loads(json_text)
        mat = np.array(parsed["matrix"], dtype=float)
        pos = {int(k): tuple(float(x) for x in v) for k, v in parsed["pos"].items()}
        n_nodes = mat.shape[0]
        n_edges = int(np.sum(mat != 0) // 2)
        st.caption(f"Parsed: {n_nodes} nodes · {n_edges} edges")
        return True, {"g": mat, "pos": pos}
    except Exception as exc:
        st.warning(f"Could not parse graph JSON: {exc}")
        return False, {}
st.set_page_config(page_title="Graph Theory Dashboard", layout="wide")

st.markdown("""
<style>
:root {
    --bg: #ffffff;
    --panel: #f5f7fb;
    --panel-2: #ffffff;
    --text: #111827;
    --muted: #6b7280;
    --accent: #2563eb;
    --accent-2: #1d4ed8;
    --border: #d1d5db;
    --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}
.stApp { background: var(--bg); color: var(--text); }
.block-container { padding-top: 1.6rem; padding-bottom: 2.5rem; }
.app-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 0.6rem 0 0.85rem; border-bottom: 1px solid var(--border);
    margin-bottom: 0.75rem; margin-top: 0.5rem;
}
.app-header .header-left { display: flex; flex-direction: column; gap: 0.2rem; }
.app-header .header-title { font-size: 1.15rem; font-weight: 600; }
.app-header .header-subtitle { font-size: 0.9rem; color: var(--muted); }
.app-header .header-logo {
    width: 58px; height: 58px; border-radius: 999px;
    border: 2px solid var(--border); object-fit: cover;
    background: #ffffff; padding: 4px;
}
.header-banner {
    width: 100%; height: 180px; object-fit: cover;
    border-radius: 12px; border: 1px solid var(--border); margin-bottom: 1rem;
}
.header-content { display: flex; align-items: center; justify-content: space-between; }
section[data-testid="stSidebar"] { background: var(--panel); border-right: 1px solid var(--border); }
.stButton > button {
    background: var(--accent); color: #0a0b0f;
    border: 1px solid var(--accent); border-radius: 8px; font-weight: 600;
}
.stButton > button:hover { background: var(--accent-2); border-color: var(--accent-2); color: #0a0b0f; }
.terminal {
    background: var(--panel-2); border: 1px solid var(--border);
    border-radius: 8px; padding: 14px; font-family: var(--mono);
    font-size: 0.92rem; color: var(--text);
    white-space: pre-wrap; max-height: 420px; overflow: auto;
}
code, pre, textarea { font-family: var(--mono) !important; }
.muted { color: var(--muted); }
.app-footer {
    display: flex; align-items: center; justify-content: space-between;
    gap: 1rem; border-top: 1px solid var(--border);
    background: var(--panel-2); position: sticky; bottom: 0;
    padding: 0.75rem 0; margin-top: 1.5rem; z-index: 50;
    color: var(--text); font-size: 0.95rem; font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

projects = find_projects(BASE_DIR)

if not projects:
    st.warning("No projects found.")
    st.stop()
with st.sidebar:
    st.markdown("### Experiments")

    if "selected_project" not in st.session_state:
        st.session_state.selected_project = list(projects.keys())[0]

    for project_name in projects:
        is_selected = project_name == st.session_state.selected_project
        label = f"▶ Experiment {project_name}" if is_selected else f"Experiment {project_name}"
        if st.button(label, key=f"project-{project_name}", use_container_width=True):
            # Clear results when switching experiments
            st.session_state.selected_project = project_name
            st.session_state.demo_result = None
            st.session_state.custom_result = None

selected_project = st.session_state.selected_project
selected_path = projects[selected_project]
project_dir = selected_path.parent
exp_number = selected_project

theory_path = BASE_DIR / "theory" / f"exp{exp_number}.md"
theory_markdown = load_theory_markdown(theory_path)

logo_data   = load_logo_base64(BASE_DIR / "logo.png")
banner_data = load_logo_base64(BASE_DIR / "banner.png")

logo_html = (
    f"<img class='header-logo' src='data:image/png;base64,{logo_data}' alt='logo' />"
    if logo_data else ""
)

selected_label = f"Experiment {selected_project}"

st.markdown(
    "<div class='app-header'>"
    f"<img class='header-banner' src='data:image/png;base64,{banner_data}' alt='banner' />"
    "<div class='header-content'>"
    "<div class='header-left'>"
    "<div class='header-title'>Subject Name: CMP-226 Graph Theory and Combinatorics Lab</div>"
    f"<div class='header-subtitle'>Selected: {selected_label}</div>"
    "</div>"
    f"{logo_html}"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

if "show_source_panel" not in st.session_state:
    st.session_state.show_source_panel = False
if "show_graph_panel" not in st.session_state:
    st.session_state.show_graph_panel = False

st.toggle("Show source code", key="show_source_panel")
if not st.session_state.show_source_panel:
    st.toggle("Show graph structure", key="show_graph_panel")
else:
    st.session_state.show_graph_panel = False

if "demo_result" not in st.session_state:
    st.session_state.demo_result = None
if "custom_result" not in st.session_state:
    st.session_state.custom_result = None
if "last_demo_project" not in st.session_state:
    st.session_state.last_demo_project = None

if st.session_state.last_demo_project != selected_project:
    with st.spinner(f"Running demo for Experiment {selected_project}…"):
        st.session_state.demo_result = call_function(selected_path, "main")
    st.session_state.last_demo_project = selected_project
    st.session_state.custom_result = None   # clear stale custom result

column_weights = [3, 2] if st.session_state.show_source_panel else [1, 1]
left_col, right_col = st.columns(column_weights, gap="large")

with left_col:
    if st.session_state.show_source_panel:
        st.markdown("### Source code")
        st.code(read_source(selected_path), language="python")

    elif st.session_state.show_graph_panel:
        st.markdown("### Graph Structure")
        try:
            modified_at = selected_path.stat().st_mtime
        except OSError as exc:
            st.warning(f"Unable to inspect graph data: {exc}")
        else:
            graph_summaries, graph_error = get_graph_summaries(str(selected_path), modified_at)
            if graph_error:
                st.warning(graph_error)
            elif not graph_summaries:
                st.info("No graphs detected in this script.")
            else:
                for index, summary in enumerate(graph_summaries, start=1):
                    st.markdown(f"**{summary.label}**")
                    meta_parts = [
                        "Directed" if summary.directed else "Undirected",
                        f"Nodes: {len(summary.nodes)}",
                        f"Edges: {len(summary.edges)}",
                    ]
                    if summary.multigraph:
                        meta_parts.insert(1, "Multigraph")
                    st.markdown(
                        f"<div class='muted'>{' · '.join(meta_parts)}</div>",
                        unsafe_allow_html=True,
                    )
                    nodes_block = "\n".join(summary.nodes) if summary.nodes else "None"
                    edge_lines  = _format_edge_lines(summary.edges, summary.directed)
                    edges_block = "\n".join(edge_lines) if edge_lines else "None"
                    nodes_col, edges_col = st.columns(2, gap="large")
                    with nodes_col:
                        st.markdown("**Nodes**")
                        st.markdown(terminal_block(nodes_block), unsafe_allow_html=True)
                    with edges_col:
                        st.markdown("**Edges**")
                        st.markdown(terminal_block(edges_block), unsafe_allow_html=True)
                    if index < len(graph_summaries):
                        st.divider()

    else:
        if theory_markdown:
            st.markdown(theory_markdown)
        else:
            missing_label = f"exp{exp_number}.md"
            st.info(f"No theory file found for this experiment ({missing_label}).")

    st.divider()

with right_col:

    st.markdown("### Demo")
    demo_result: RunResult | None = st.session_state.demo_result

    if demo_result is None:
        st.info("Demo will run automatically when an experiment is selected.")
    else:
        render_result(demo_result)

    st.divider()
    st.markdown("### Run with custom input")

    with st.expander("Input", expanded=True):
        params_ready, params = render_custom_input(exp_number)

    run_clicked = st.button("Run Algorithm", type="primary", use_container_width=True,
                             disabled=not params_ready)

    if run_clicked and params_ready:
        with st.spinner("Running…"):
            st.session_state.custom_result = call_function(
                selected_path, "run", func_kwargs=params
            )

    custom_result: RunResult | None = st.session_state.custom_result
    if custom_result:
        render_result(custom_result)

st.markdown(
    "<div class='app-footer'>"
    "<div>Abdullah Mukadam</div>"
    "<div>[REDACTED]</div>"
    "<div>Sem IV</div>"
    "</div>",
    unsafe_allow_html=True,
)
