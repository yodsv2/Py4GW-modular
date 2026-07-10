"""Run a single Python modular recipe through BottingTree."""

from __future__ import annotations

import ast
import json
import os
import time
from dataclasses import dataclass
from pathlib import Path
from time import monotonic
from time import sleep
from typing import Any

import PyImGui

from Py4GWCoreLib import Console
from Py4GWCoreLib import ConsoleLog
from Py4GWCoreLib.botting_tree_src.ui import BottingTreeUIMovePathMixin
from Py4GWCoreLib.BottingTree import BottingTree
from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.modular_recipes.catalog import RecipeSpec
from Sources.modular_recipes.catalog import all_specs
from Sources.modular_recipes.catalog import get_recipe_factory
from Sources.modular_recipes.catalog import get_recipe_module
from Widgets.Automation.modular.widget_guard import guarded_widget_main

MODULE_NAME = "Modular Tester"
MODULE_ICON = "Textures/Module_Icons/Route Planner.png"
MODULE_TAGS = ["Automation", "modular_bot"]
STATE_PATH = Path(__file__).with_suffix(".run_state.json")
STATE_LOCK_PATH = Path(f"{STATE_PATH}.lock")

ACCENT = (0.30, 0.78, 0.86, 1.0)
GOOD = (0.42, 0.88, 0.55, 1.0)
WARN = (1.00, 0.78, 0.32, 1.0)
BAD = (1.00, 0.38, 0.38, 1.0)
MUTED = (0.62, 0.66, 0.70, 1.0)
TEXT = (0.92, 0.94, 0.96, 1.0)
RUN_PENDING = "pending"
RUN_SUCCESS = "success"
RUN_FAILED = "failed"
RUN_RUNNING = "running"
RUN_FILTER_ALL = "all"
RUN_FILTER_PENDING = "pending"
RUN_FILTER_SUCCESS = "done"
RUN_FILTER_FAILED = "failed"
WINDOW_BG = (0.055, 0.070, 0.085, 0.985)
PANEL_BG = (0.080, 0.100, 0.120, 0.965)
PANEL_ALT_BG = (0.105, 0.125, 0.145, 0.965)
BORDER = (0.18, 0.27, 0.31, 0.78)
HEADER_BG = (0.10, 0.34, 0.40, 0.82)
HEADER_HOVER = (0.12, 0.43, 0.50, 0.92)
HEADER_ACTIVE = (0.08, 0.28, 0.34, 0.94)


@dataclass(frozen=True)
class RecipeSummary:
    title: str
    kind: str
    steps: int
    module: str
    factory: str


@dataclass(frozen=True)
class SourceStep:
    index: int
    file: str
    line: int
    end_line: int
    call: str
    source: str
    points: tuple[tuple[float, float], ...] = ()


_recipe_files: list[str] = []
_recipe_tree: dict[str, object] = {"dirs": {}, "files": []}
_recipe_titles: dict[str, str] = {}
_recipe_summaries: dict[str, RecipeSummary] = {}
_recipe_specs: dict[str, RecipeSpec] = {}
_selected_recipe = ""
_browser_path: list[str] = []
_filter_text = ""
_runner: BottingTree | None = None
_planner_step_total = 0
_last_active_step_name = ""
_status = ""
_last_recipe = ""
_recipe_run_states: dict[str, str] = {}
_run_states_loaded = False
_run_state_filter = RUN_FILTER_ALL
_loop = False
_debug_logging = False
_draw_move_path = True
_draw_move_path_labels = False
_draw_move_path_thickness = 4.0
_draw_move_waypoint_radius = 15.0
_draw_move_current_waypoint_radius = 20.0


class _TesterMovePathDrawer(BottingTreeUIMovePathMixin):
    def __init__(self) -> None:
        self.blackboard: dict = {}
        self.draw_move_path_enabled = True
        self.draw_move_path_labels = False
        self.draw_move_path_thickness = 4.0
        self.draw_move_waypoint_radius = 15.0
        self.draw_move_current_waypoint_radius = 20.0
        self.tree = self

    def draw(self) -> None:
        return


_path_drawer = _TesterMovePathDrawer()
_source_steps_by_recipe: dict[str, tuple[SourceStep, ...]] = {}


def _valid_run_state(value: object) -> str:
    text = str(value or "").strip()
    if text in {RUN_SUCCESS, RUN_FAILED, RUN_RUNNING}:
        return text
    return RUN_PENDING


def _read_run_state_recipes() -> dict[str, str]:
    if not STATE_PATH.exists():
        return {}
    raw = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    recipes = raw.get("recipes", {}) if isinstance(raw, dict) else {}
    if not isinstance(recipes, dict):
        return {}
    return {
        str(recipe): state
        for recipe, raw_state in recipes.items()
        if (state := _valid_run_state(raw_state)) in {RUN_SUCCESS, RUN_FAILED}
    }


def _atomic_write_run_state_recipes(recipes: dict[str, str]) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = STATE_PATH.with_name(f"{STATE_PATH.name}.{os.getpid()}.tmp")
    payload = {
        "version": 1,
        "recipes": {
            recipe: state
            for recipe, state in sorted(recipes.items())
            if state in {RUN_SUCCESS, RUN_FAILED}
        },
    }
    tmp_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    os.replace(str(tmp_path), str(STATE_PATH))


def _acquire_run_state_lock(timeout_s: float = 1.5) -> int:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    deadline = monotonic() + max(0.1, float(timeout_s))
    while True:
        try:
            return os.open(str(STATE_LOCK_PATH), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            try:
                if time.time() - STATE_LOCK_PATH.stat().st_mtime > 10.0:
                    STATE_LOCK_PATH.unlink()
                    continue
            except FileNotFoundError:
                continue
            except Exception:
                pass
            if monotonic() >= deadline:
                raise TimeoutError(f"Timed out waiting for {STATE_LOCK_PATH.name}.")
            sleep(0.05)


def _release_run_state_lock(lock_fd: int) -> None:
    try:
        os.close(lock_fd)
    finally:
        try:
            STATE_LOCK_PATH.unlink()
        except FileNotFoundError:
            pass


def _load_run_states(force: bool = False) -> None:
    global _run_states_loaded, _recipe_run_states
    if _run_states_loaded and not force:
        return
    _run_states_loaded = True
    try:
        final_states = _read_run_state_recipes()
    except Exception as exc:
        ConsoleLog(MODULE_NAME, f"Run state load failed: {exc}", Console.MessageType.Warning)
        return
    running_states = {
        recipe: state
        for recipe, state in _recipe_run_states.items()
        if state == RUN_RUNNING
    }
    _recipe_run_states = {**final_states, **running_states}


def _save_run_states(
    updates: dict[str, str] | None = None,
    removals: set[str] | None = None,
    replace: bool = False,
) -> None:
    global _recipe_run_states
    updates = updates or {}
    removals = removals or set()
    lock_fd = -1
    try:
        lock_fd = _acquire_run_state_lock()
        recipes = {} if replace else _read_run_state_recipes()
        for recipe in removals:
            recipes.pop(str(recipe), None)
        for recipe, state in updates.items():
            state = _valid_run_state(state)
            if state in {RUN_SUCCESS, RUN_FAILED}:
                recipes[str(recipe)] = state
        if replace:
            for recipe, state in _recipe_run_states.items():
                if state in {RUN_SUCCESS, RUN_FAILED}:
                    recipes[str(recipe)] = state
        _atomic_write_run_state_recipes(recipes)
        running_states = {
            recipe: state
            for recipe, state in _recipe_run_states.items()
            if state == RUN_RUNNING
        }
        _recipe_run_states = {**recipes, **running_states}
    except Exception as exc:
        ConsoleLog(MODULE_NAME, f"Run state save failed: {exc}", Console.MessageType.Warning)
    finally:
        if lock_fd >= 0:
            _release_run_state_lock(lock_fd)


def _debug(message: str) -> None:
    if _debug_logging:
        ConsoleLog(MODULE_NAME, message, Console.MessageType.Info)


def _refresh_recipe_files(reload_run_states: bool = False) -> None:
    global _recipe_files, _recipe_tree, _recipe_titles, _recipe_summaries, _recipe_specs
    global _selected_recipe
    _load_run_states(force=reload_run_states)
    recipes: list[str] = []
    titles: dict[str, str] = {}
    summaries: dict[str, RecipeSummary] = {}
    specs: dict[str, RecipeSpec] = {}
    for spec in all_specs():
        rel = _spec_display_path(spec)
        recipes.append(rel)
        specs[rel] = spec
        summary = _summary_from_spec(spec, rel)
        titles[rel] = summary.title
        summaries[rel] = summary
    _recipe_files = sorted(recipes)
    _recipe_titles = titles
    _recipe_summaries = summaries
    _recipe_specs = specs
    _recipe_tree = _build_recipe_tree(_recipe_files)
    if _selected_recipe not in _recipe_files:
        _selected_recipe = ""


def _build_recipe_tree(paths: list[str]) -> dict[str, object]:
    root: dict[str, object] = {"dirs": {}, "files": []}
    for relative_path in paths:
        parts = relative_path.split("/")
        node = root
        for folder in parts[:-1]:
            dirs = node.setdefault("dirs", {})
            if not isinstance(dirs, dict):
                dirs = {}
                node["dirs"] = dirs
            node = dirs.setdefault(folder, {"dirs": {}, "files": []})
        files = node.setdefault("files", [])
        if isinstance(files, list):
            files.append(relative_path)
    return root


def _matches_run_state_filter(relative_path: str) -> bool:
    state = _recipe_run_state(relative_path)
    if _run_state_filter == RUN_FILTER_ALL:
        return True
    if _run_state_filter == RUN_FILTER_SUCCESS:
        return state == RUN_SUCCESS
    if _run_state_filter == RUN_FILTER_FAILED:
        return state == RUN_FAILED
    if _run_state_filter == RUN_FILTER_PENDING:
        return state not in {RUN_SUCCESS, RUN_FAILED}
    return True


def _status_filtered_recipe_files() -> list[str]:
    return [path for path in _recipe_files if _matches_run_state_filter(path)]


def _visible_recipe_files() -> list[str]:
    needle = _filter_text.strip().lower()
    candidates = _status_filtered_recipe_files()
    if not needle:
        return candidates
    return [
        path for path in candidates if needle in path.lower() or needle in (_recipe_titles.get(path) or "").lower()
    ]


def _selected_recipe_path() -> str:
    if _selected_recipe in _recipe_files:
        return _selected_recipe
    return ""


def _browser_node() -> dict[str, object]:
    node = _build_recipe_tree(_status_filtered_recipe_files())
    for folder in _browser_path:
        dirs = node.get("dirs", {})
        if not isinstance(dirs, dict):
            return {"dirs": {}, "files": []}
        child = dirs.get(folder)
        if not isinstance(child, dict):
            return {"dirs": {}, "files": []}
        node = child
    return node


def _browser_label() -> str:
    return "/".join(_browser_path) if _browser_path else "modular_recipes"


def _spec_display_path(spec: RecipeSpec) -> str:
    return f"{spec.kind}/{spec.key}"


def _selected_spec(relative_path: str) -> RecipeSpec | None:
    return _recipe_specs.get(relative_path)


def _summary_from_spec(spec: RecipeSpec, relative_path: str) -> RecipeSummary:
    title = str(spec.title).strip() or Path(relative_path).name.replace("_", " ").title()
    return RecipeSummary(
        title=title,
        kind=str(spec.kind),
        steps=int(spec.steps),
        module=str(spec.module),
        factory=str(spec.factory),
    )


def _recipe_module(relative_path: str):
    spec = _selected_spec(relative_path)
    if spec is None:
        return None
    try:
        return get_recipe_module(spec)
    except Exception:
        return None


def _recipe_summary(relative_path: str) -> RecipeSummary:
    spec = _selected_spec(relative_path)
    if spec is None:
        title = Path(relative_path).name.replace("_", " ").title()
        kind = Path(relative_path).parts[0] if Path(relative_path).parts else "recipes"
        return RecipeSummary(title=title, kind=kind, steps=0, module="", factory="")
    return _summary_from_spec(spec, relative_path)


def _literal_point(node: ast.AST) -> tuple[float, float] | None:
    try:
        value = ast.literal_eval(node)
    except Exception:
        return None
    if not isinstance(value, tuple) or len(value) != 2:
        return None
    try:
        return float(value[0]), float(value[1])
    except Exception:
        return None


def _points_from_call(node: ast.Call) -> tuple[tuple[float, float], ...]:
    for keyword in node.keywords:
        if keyword.arg != "pos":
            continue
        point = _literal_point(keyword.value)
        if point is not None:
            return (point,)
        if isinstance(keyword.value, ast.List):
            points = [_literal_point(element) for element in keyword.value.elts]
            return tuple(point for point in points if point is not None)
    return ()


def _bt_call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
        if isinstance(node.func.value, ast.Name) and node.func.value.id == "BT":
            return f"BT.{node.func.attr}"
    return "BT step"


def _module_relative_file(module: Any) -> str:
    path = Path(str(getattr(module, "__file__", ""))).resolve()
    try:
        return path.relative_to(Path.cwd()).as_posix()
    except Exception:
        return str(path)


def _source_steps_for_recipe(relative_path: str) -> tuple[SourceStep, ...]:
    cached = _source_steps_by_recipe.get(relative_path)
    if cached is not None:
        return cached
    spec = _selected_spec(relative_path)
    module = _recipe_module(relative_path)
    if spec is None or module is None or not getattr(module, "__file__", ""):
        _source_steps_by_recipe[relative_path] = ()
        return ()
    path = Path(str(module.__file__)).resolve()
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)
    except Exception:
        _source_steps_by_recipe[relative_path] = ()
        return ()

    steps: list[SourceStep] = []
    rel_file = _module_relative_file(module)
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef) or node.name != spec.factory:
            continue
        for child in ast.walk(node):
            if not isinstance(child, ast.Return) or not isinstance(child.value, ast.Call):
                continue
            children_node = next(
                (keyword.value for keyword in child.value.keywords if keyword.arg == "children"),
                None,
            )
            if not isinstance(children_node, ast.List):
                continue
            for index, element in enumerate(children_node.elts):
                if not isinstance(element, ast.Call):
                    continue
                source_segment = ast.get_source_segment(source, element) or _bt_call_name(element)
                steps.append(
                    SourceStep(
                        index=index,
                        file=rel_file,
                        line=int(getattr(element, "lineno", 0) or 0),
                        end_line=int(getattr(element, "end_lineno", getattr(element, "lineno", 0)) or 0),
                        call=_bt_call_name(element),
                        source=source_segment.strip(),
                        points=_points_from_call(element),
                    )
                )
            break

    result = tuple(steps)
    _source_steps_by_recipe[relative_path] = result
    return result


def _mark_source_step(step: SourceStep, total: int) -> BehaviorTree.Node:
    def _mark(node: BehaviorTree.Node, step: SourceStep = step, total: int = total) -> BehaviorTree.NodeState:
        node.blackboard["modular_tester_source_index"] = int(step.index)
        node.blackboard["modular_tester_source_total"] = int(total)
        node.blackboard["modular_tester_source_file"] = step.file
        node.blackboard["modular_tester_source_line"] = int(step.line)
        node.blackboard["modular_tester_source_end_line"] = int(step.end_line)
        node.blackboard["modular_tester_source_call"] = step.call
        node.blackboard["modular_tester_source_text"] = step.source
        node.blackboard["modular_tester_source_points"] = list(step.points)
        return BehaviorTree.NodeState.SUCCESS

    return BehaviorTree.ActionNode(
        name=f"MarkSource({step.index + 1}:{step.call})",
        action_fn=_mark,
        aftercast_ms=0,
    )


def _instrument_recipe_tree(tree: BehaviorTree, source_steps: tuple[SourceStep, ...]) -> BehaviorTree:
    if not source_steps or not isinstance(tree.root, BehaviorTree.SequenceNode):
        return tree
    children = list(tree.root.get_children())
    if not children:
        return tree
    wrapped_children: list[BehaviorTree.Node] = []
    total = len(source_steps)
    for index, child in enumerate(children):
        if index < total:
            wrapped_children.append(_mark_source_step(source_steps[index], total))
        wrapped_children.append(child)
    return BehaviorTree(BehaviorTree.SequenceNode(name=tree.root.name, children=wrapped_children))


def _instrumented_recipe_factory(spec: RecipeSpec, relative_path: str):
    base_factory = get_recipe_factory(spec)

    def _factory() -> BehaviorTree:
        return _instrument_recipe_tree(BehaviorTree.resolve_tree(base_factory), _source_steps_for_recipe(relative_path))

    return _factory


def _runtime_mode() -> bool:
    return _runner_is_running() or _runner_is_paused()


def _path_draw_blackboard() -> dict:
    if _runner is None:
        return {}
    blackboard = dict(_runner.blackboard)
    points = blackboard.get("move_path_points")
    if not isinstance(points, list) or not points:
        return {}
    state = str(blackboard.get("move_state") or "")
    if state not in ("running", "paused"):
        return {}
    blackboard["move_state"] = "running" if _runner_is_running() else "paused"
    return blackboard


def _draw_move_path_overlay() -> None:
    if not _draw_move_path:
        return
    blackboard = _path_draw_blackboard()
    if not blackboard:
        return
    _path_drawer.blackboard = blackboard
    _path_drawer.draw_move_path_labels = _draw_move_path_labels
    _path_drawer.draw_move_path_thickness = _draw_move_path_thickness
    _path_drawer.draw_move_waypoint_radius = _draw_move_waypoint_radius
    _path_drawer.draw_move_current_waypoint_radius = _draw_move_current_waypoint_radius
    _path_drawer.DrawMovePathIfEnabled()


def _recipe_run_state(relative_path: str) -> str:
    return _recipe_run_states.get(relative_path, RUN_PENDING)


def _set_recipe_run_state(relative_path: str, state: str) -> None:
    if not relative_path:
        return
    if state == RUN_PENDING:
        _recipe_run_states.pop(relative_path, None)
        _save_run_states(removals={relative_path})
        return
    _recipe_run_states[relative_path] = state
    if state in {RUN_SUCCESS, RUN_FAILED}:
        _save_run_states(updates={relative_path: state})


def _reset_recipe_run_states() -> None:
    global _status
    _recipe_run_states.clear()
    _save_run_states(replace=True)
    _status = "Recipe run states reset."


def _mark_runner_finished(success: bool, reason: str = "") -> None:
    global _runner, _status, _planner_step_total, _last_active_step_name
    recipe = _last_recipe or _selected_recipe_path()
    _set_recipe_run_state(recipe, RUN_SUCCESS if success else RUN_FAILED)
    _planner_step_total = 0
    _last_active_step_name = ""
    _status = f"{'Completed' if success else 'Ended early'} {recipe}." if recipe else reason


def _tick_runner() -> None:
    global _status
    if _runner is None or not _runner_is_running():
        return
    try:
        _runner.tick()
    except Exception as exc:
        _mark_runner_finished(False, str(exc))
        if _runner is not None:
            try:
                _runner.Stop()
            except Exception:
                pass
        _status = f"Run failed: {exc}"
        return

    if _runner is None or _runner_is_running() or _runner_is_paused():
        return
    planner_status = str(_runner.GetBlackboardValue("PLANNER_STATUS", "") or "")
    if planner_status == "PLANNER: Completed":
        _mark_runner_finished(True, planner_status)
    elif planner_status == "PLANNER: Failed":
        _mark_runner_finished(False, planner_status)


def _start_selected_recipe() -> None:
    global _runner, _status, _last_recipe, _planner_step_total, _last_active_step_name
    relative_path = _selected_recipe_path()
    if not relative_path:
        _status = "No recipe selected."
        return
    try:
        if _runner is not None and (_runner_is_running() or _runner_is_paused()):
            _mark_runner_finished(False, "Superseded")
            _runner.Stop()
            _runner = None
        elif _runner is not None:
            _runner = None
        spec = _selected_spec(relative_path)
        if spec is None:
            raise ValueError(f"Unknown recipe {relative_path}.")
        builder = _instrumented_recipe_factory(spec, relative_path)
        selected_steps = [(f"01. {spec.title or spec.factory}", builder)]
        _planner_step_total = len(selected_steps)
        _last_active_step_name = ""
        runner = BottingTree(
            bot_name=f"Modular Tester: {relative_path}",
            pause_on_combat=False,
            isolation_enabled=False,
        )
        runner.SetCurrentNamedPlannerSteps(
            selected_steps,
            name="ModularTester",
            auto_start=False,
            reset=True,
            repeat=bool(_loop),
        )
        runner.Start()
        _runner = runner
        _last_recipe = relative_path
        _set_recipe_run_state(relative_path, RUN_RUNNING)
        _status = f"Started {relative_path}."
    except Exception as exc:
        _runner = None
        _set_recipe_run_state(relative_path, RUN_FAILED)
        _status = f"Start failed: {exc}"


def _stop_runner() -> None:
    global _runner, _status, _planner_step_total, _last_active_step_name
    had_active_runner = _runner is not None and (_runner_is_running() or _runner_is_paused())
    if _runner is not None:
        _runner.Stop()
        _runner = None
    _planner_step_total = 0
    _last_active_step_name = ""
    if had_active_runner:
        _mark_runner_finished(False, "Stopped")
    else:
        _status = "Stopped."


def _pause_runner() -> None:
    global _status
    if _runner is not None:
        _runner.Pause(True)
    _status = "Paused."


def _resume_runner() -> None:
    global _status
    if _runner is not None:
        _runner.Pause(False)
    _status = "Resumed."


def _runner_is_running() -> bool:
    return _runner is not None and bool(_runner.IsStarted()) and not bool(_runner.IsPaused())


def _runner_is_paused() -> bool:
    return _runner is not None and bool(_runner.IsPaused())


def _active_step_name() -> str:
    global _last_active_step_name
    if _runner is None:
        return ""
    current_step_name = str(_runner.GetBlackboardValue("current_step_name", "") or "")
    if current_step_name:
        _last_active_step_name = current_step_name
        return current_step_name
    return _last_active_step_name


def _step_progress() -> tuple[int, int, str, str]:
    active_step = _active_step_name()
    if not active_step:
        return 0, _planner_step_total, _last_recipe, ""
    return 1, _planner_step_total, _last_recipe, active_step


def _progress_fraction() -> float:
    if _runner is None:
        return 0.0
    source_total = int(_runner.blackboard.get("modular_tester_source_total", 0) or 0)
    if source_total > 0:
        source_index = int(_runner.blackboard.get("modular_tester_source_index", 0))
        return max(0.0, min(1.0, float(source_index + 1) / float(source_total)))
    step_current, step_total, _recipe_title, _step_title = _step_progress()
    if step_total <= 0:
        return 0.0
    return max(0.0, min(1.0, float(step_current) / float(step_total)))


def _kind_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for relative_path in _status_filtered_recipe_files():
        summary = _recipe_summaries.get(relative_path)
        if summary is None:
            continue
        counts[summary.kind] = counts.get(summary.kind, 0) + 1
    return counts


def _run_state_counts() -> dict[str, int]:
    counts = {
        RUN_FILTER_PENDING: 0,
        RUN_FILTER_SUCCESS: 0,
        RUN_FILTER_FAILED: 0,
    }
    for relative_path in _recipe_files:
        state = _recipe_run_state(relative_path)
        if state == RUN_SUCCESS:
            counts[RUN_FILTER_SUCCESS] += 1
        elif state == RUN_FAILED:
            counts[RUN_FILTER_FAILED] += 1
        else:
            counts[RUN_FILTER_PENDING] += 1
    return counts


def _draw_text(label: str, color: tuple[float, float, float, float] = TEXT) -> None:
    PyImGui.text_colored(label, color)


def _draw_label_value(label: str, value: str, color: tuple[float, float, float, float] = TEXT) -> None:
    PyImGui.text_colored(label, MUTED)
    PyImGui.same_line(0, 6)
    PyImGui.text_colored(value, color)


def _draw_button_style(
    base: tuple[float, float, float, float],
    hover: tuple[float, float, float, float],
    active: tuple[float, float, float, float],
) -> None:
    PyImGui.push_style_color(PyImGui.ImGuiCol.Button, base)
    PyImGui.push_style_color(PyImGui.ImGuiCol.ButtonHovered, hover)
    PyImGui.push_style_color(PyImGui.ImGuiCol.ButtonActive, active)


def _pop_button_style() -> None:
    PyImGui.pop_style_color(3)


def _selectable_row(label: str, selected: bool = False) -> bool:
    return PyImGui.selectable(label, selected, int(PyImGui.SelectableFlags.SpanAllColumns), [0.0, 0.0])


def _push_tester_theme() -> int:
    colors = [
        (PyImGui.ImGuiCol.WindowBg, WINDOW_BG),
        (PyImGui.ImGuiCol.ChildBg, PANEL_BG),
        (PyImGui.ImGuiCol.PopupBg, PANEL_BG),
        (PyImGui.ImGuiCol.Border, BORDER),
        (PyImGui.ImGuiCol.FrameBg, PANEL_ALT_BG),
        (PyImGui.ImGuiCol.FrameBgHovered, (0.13, 0.17, 0.19, 1.0)),
        (PyImGui.ImGuiCol.FrameBgActive, (0.15, 0.22, 0.25, 1.0)),
        (PyImGui.ImGuiCol.TitleBg, (0.055, 0.070, 0.085, 1.0)),
        (PyImGui.ImGuiCol.TitleBgActive, (0.080, 0.125, 0.145, 1.0)),
        (PyImGui.ImGuiCol.Header, HEADER_BG),
        (PyImGui.ImGuiCol.HeaderHovered, HEADER_HOVER),
        (PyImGui.ImGuiCol.HeaderActive, HEADER_ACTIVE),
        (PyImGui.ImGuiCol.Separator, BORDER),
        (PyImGui.ImGuiCol.SeparatorHovered, ACCENT),
        (PyImGui.ImGuiCol.SeparatorActive, ACCENT),
        (PyImGui.ImGuiCol.Tab, (0.075, 0.105, 0.125, 1.0)),
        (PyImGui.ImGuiCol.TabHovered, HEADER_HOVER),
        (PyImGui.ImGuiCol.TabActive, (0.10, 0.32, 0.38, 1.0)),
        (PyImGui.ImGuiCol.TabUnfocused, (0.065, 0.080, 0.095, 1.0)),
        (PyImGui.ImGuiCol.TabUnfocusedActive, (0.085, 0.145, 0.165, 1.0)),
        (PyImGui.ImGuiCol.TableHeaderBg, (0.09, 0.13, 0.15, 1.0)),
        (PyImGui.ImGuiCol.TableBorderStrong, BORDER),
        (PyImGui.ImGuiCol.TableBorderLight, (0.13, 0.18, 0.20, 0.70)),
        (PyImGui.ImGuiCol.TableRowBg, (0.08, 0.10, 0.12, 0.68)),
        (PyImGui.ImGuiCol.TableRowBgAlt, (0.10, 0.12, 0.14, 0.72)),
        (PyImGui.ImGuiCol.ScrollbarBg, (0.055, 0.070, 0.085, 0.88)),
        (PyImGui.ImGuiCol.ScrollbarGrab, (0.18, 0.29, 0.33, 0.90)),
        (PyImGui.ImGuiCol.ScrollbarGrabHovered, (0.23, 0.39, 0.45, 1.0)),
        (PyImGui.ImGuiCol.ScrollbarGrabActive, (0.28, 0.54, 0.62, 1.0)),
        (PyImGui.ImGuiCol.CheckMark, ACCENT),
        (PyImGui.ImGuiCol.TextSelectedBg, (0.22, 0.54, 0.62, 0.38)),
    ]
    for color_index, color in colors:
        PyImGui.push_style_color(color_index, color)
    return len(colors)


def _primary_button(label: str, width: float = 0.0) -> bool:
    _draw_button_style((0.10, 0.45, 0.52, 1.0), (0.12, 0.58, 0.66, 1.0), (0.08, 0.36, 0.42, 1.0))
    clicked = PyImGui.button(label, width, 28)
    _pop_button_style()
    return clicked


def _danger_button(label: str, width: float = 0.0) -> bool:
    _draw_button_style((0.56, 0.18, 0.18, 1.0), (0.70, 0.22, 0.22, 1.0), (0.42, 0.12, 0.12, 1.0))
    clicked = PyImGui.button(label, width, 28)
    _pop_button_style()
    return clicked


def _quiet_button(label: str, width: float = 0.0) -> bool:
    _draw_button_style((0.18, 0.21, 0.24, 1.0), (0.24, 0.28, 0.32, 1.0), (0.14, 0.16, 0.18, 1.0))
    clicked = PyImGui.button(label, width, 28)
    _pop_button_style()
    return clicked


def _status_filter_button(label: str, value: str, width: float = 0.0) -> bool:
    if _run_state_filter == value:
        return _primary_button(label, width)
    return _quiet_button(label, width)


def _highlight_button(label: str, width: float = 0.0) -> bool:
    PyImGui.push_style_color(PyImGui.ImGuiCol.Button, (0.46, 0.11, 0.12, 1.0))
    PyImGui.push_style_color(PyImGui.ImGuiCol.ButtonHovered, (0.62, 0.15, 0.16, 1.0))
    PyImGui.push_style_color(PyImGui.ImGuiCol.ButtonActive, (0.36, 0.08, 0.09, 1.0))
    PyImGui.push_style_color(PyImGui.ImGuiCol.Border, (1.0, 0.38, 0.38, 1.0))
    PyImGui.push_style_color(PyImGui.ImGuiCol.Text, (1.0, 0.94, 0.94, 1.0))
    try:
        PyImGui.push_style_var(PyImGui.ImGuiStyleVar.FrameBorderSize, 2.0)
        pushed_border_size = True
    except Exception:
        pushed_border_size = False
    clicked = PyImGui.button(label, width, 28)
    if pushed_border_size:
        PyImGui.pop_style_var(1)
    PyImGui.pop_style_color(5)
    return clicked


def _run_state_button_style(state: str, selected: bool) -> tuple[
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
    tuple[float, float, float, float],
]:
    if state == RUN_SUCCESS:
        base = (0.18, 0.46, 0.24, 1.0)
        hover = (0.24, 0.60, 0.32, 1.0)
        active = (0.13, 0.36, 0.18, 1.0)
        text = (0.92, 1.0, 0.94, 1.0)
    elif state == RUN_FAILED:
        base = (0.54, 0.16, 0.18, 1.0)
        hover = (0.70, 0.22, 0.24, 1.0)
        active = (0.40, 0.10, 0.12, 1.0)
        text = (1.0, 0.94, 0.94, 1.0)
    elif state == RUN_RUNNING:
        base = (0.10, 0.40, 0.50, 1.0)
        hover = (0.12, 0.53, 0.64, 1.0)
        active = (0.08, 0.32, 0.40, 1.0)
        text = (0.90, 0.98, 1.0, 1.0)
    else:
        base = (0.64, 0.46, 0.10, 1.0)
        hover = (0.78, 0.58, 0.14, 1.0)
        active = (0.48, 0.34, 0.08, 1.0)
        text = (1.0, 0.98, 0.88, 1.0)
    if selected:
        base = tuple(min(1.0, channel + 0.08) if index < 3 else channel for index, channel in enumerate(base))
    return base, hover, active, text


def _recipe_button(label: str, relative_path: str, selected: bool, width: float = 0.0) -> bool:
    state = _recipe_run_state(relative_path)
    base, hover, active, text = _run_state_button_style(state, selected)
    _draw_button_style(base, hover, active)
    PyImGui.push_style_color(PyImGui.ImGuiCol.Text, text)
    PyImGui.push_style_color(PyImGui.ImGuiCol.Border, ACCENT if selected else BORDER)
    pushed_border_size = False
    try:
        PyImGui.push_style_var(PyImGui.ImGuiStyleVar.FrameBorderSize, 2.0 if selected else 1.0)
        pushed_border_size = True
    except Exception:
        pass
    clicked = PyImGui.button(label, width, 28)
    if pushed_border_size:
        PyImGui.pop_style_var(1)
    PyImGui.pop_style_color(2)
    _pop_button_style()
    return clicked


def _status_color() -> tuple[float, float, float, float]:
    if _runner_is_running():
        return GOOD
    if _runner_is_paused():
        return WARN
    if _status.lower().startswith("start failed"):
        return BAD
    if _runner is not None:
        return WARN
    return MUTED


def _status_text() -> str:
    if _runner_is_running():
        return "Running"
    if _runner_is_paused():
        return "Paused"
    if _runner is None:
        return "Ready"
    return "Stopped"


def _draw_top_bar() -> None:
    global _loop, _debug_logging, _draw_move_path, _draw_move_path_labels
    PyImGui.begin_group()
    PyImGui.text_scaled("Modular Tester", ACCENT, 1.22)
    if _runtime_mode():
        PyImGui.text_colored("Runtime diagnostics for the active modular recipe.", MUTED)
    else:
        PyImGui.text_colored("Browse Python modular recipes, choose one, and run it.", MUTED)
    PyImGui.end_group()
    PyImGui.same_line(max(0.0, PyImGui.get_content_region_avail()[0] - 84.0), 10)
    _draw_text(_status_text(), _status_color())
    PyImGui.separator()
    _loop = PyImGui.checkbox("Loop", _loop)
    PyImGui.same_line(0, 14)
    _debug_logging = PyImGui.checkbox("Debug logging", _debug_logging)
    PyImGui.same_line(0, 14)
    _draw_move_path = PyImGui.checkbox("Draw live path", _draw_move_path)
    PyImGui.same_line(0, 14)
    _draw_move_path_labels = PyImGui.checkbox("Path labels", _draw_move_path_labels)


def _draw_recipe_picker() -> None:
    global _filter_text
    if not _recipe_files:
        _refresh_recipe_files()

    visible_count = len(_status_filtered_recipe_files())
    total_label = f"{visible_count}/{len(_recipe_files)} shown" if visible_count != len(_recipe_files) else f"{len(_recipe_files)} loaded"
    _draw_section_title("Recipes", total_label)
    _draw_selection_controls()
    PyImGui.spacing()
    _draw_run_state_filters()
    PyImGui.spacing()
    PyImGui.set_next_item_width(max(120.0, PyImGui.get_content_region_avail()[0] - 82.0))
    _filter_text = PyImGui.input_text("##modular_tester_filter", _filter_text, 128)
    PyImGui.same_line(0, 6)
    if _quiet_button("Refresh", 74):
        _refresh_recipe_files(reload_run_states=True)
    PyImGui.spacing()
    _draw_kind_strip()
    PyImGui.spacing()
    if _filter_text.strip():
        _draw_filtered_recipes()
    else:
        _draw_button_browser()


def _draw_run_state_filters() -> None:
    global _run_state_filter
    counts = _run_state_counts()
    all_count = len(_recipe_files)
    buttons = (
        (RUN_FILTER_ALL, f"All {all_count}", 64.0),
        (RUN_FILTER_PENDING, f"Pending {counts[RUN_FILTER_PENDING]}", 96.0),
        (RUN_FILTER_SUCCESS, f"Done {counts[RUN_FILTER_SUCCESS]}", 78.0),
        (RUN_FILTER_FAILED, f"Failed {counts[RUN_FILTER_FAILED]}", 86.0),
    )
    for index, (value, label, width) in enumerate(buttons):
        if index > 0:
            PyImGui.same_line(0, 6)
        if _status_filter_button(f"{label}##run_state_filter_{value}", value, width):
            _run_state_filter = value


def _draw_selection_controls() -> None:
    selected = _selected_recipe_path()
    running = _runner_is_running()
    paused = _runner_is_paused()
    can_go_up = bool(_browser_path) and not _filter_text.strip()
    PyImGui.begin_disabled(not can_go_up)
    if _quiet_button("Up", 42):
        _go_up()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not selected or running)
    if _primary_button("Run", 58):
        _start_selected_recipe()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not running)
    if _quiet_button("Pause", 58):
        _pause_runner()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not paused)
    if _primary_button("Resume", 68):
        _resume_runner()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not (running or paused))
    if _danger_button("Stop", 52):
        _stop_runner()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not _recipe_run_states)
    if _quiet_button("Reset states", 96):
        _reset_recipe_run_states()
    PyImGui.end_disabled()


def _go_up() -> None:
    global _browser_path
    if _browser_path:
        _browser_path = _browser_path[:-1]


def _draw_kind_strip() -> None:
    global _browser_path, _filter_text
    counts = _kind_counts()
    if not counts:
        PyImGui.text_colored("No recipes found.", MUTED)
        return
    if PyImGui.begin_child("##modular_tester_kind_strip", (0, 118), True, PyImGui.WindowFlags.NoFlag):
        flags = PyImGui.TableFlags.SizingStretchSame | PyImGui.TableFlags.NoSavedSettings
        if PyImGui.begin_table("##modular_tester_kind_table", 2, flags):
            for index, kind in enumerate(sorted(counts)):
                if index % 2 == 0:
                    PyImGui.table_next_row()
                PyImGui.table_set_column_index(index % 2)
                selected = bool(_browser_path and _browser_path[0] == kind)
                label = f"{kind}  {counts[kind]}##kind_{kind}"
                if selected:
                    _draw_button_style(
                        (0.10, 0.45, 0.52, 1.0),
                        (0.12, 0.58, 0.66, 1.0),
                        (0.08, 0.36, 0.42, 1.0),
                    )
                if PyImGui.button(label, max(96.0, PyImGui.get_content_region_avail()[0]), 24):
                    _browser_path = [kind]
                    _filter_text = ""
                if selected:
                    _pop_button_style()
            PyImGui.end_table()
    PyImGui.end_child()


def _draw_filtered_recipes() -> None:
    visible = _visible_recipe_files()
    _draw_section_title("Matches", f"{len(visible)}")
    if PyImGui.begin_child("##modular_tester_matches", (0, 0), True, PyImGui.WindowFlags.HorizontalScrollbar):
        if not visible:
            PyImGui.text_colored("No matching recipes.", MUTED)
        for relative_path in visible:
            _draw_recipe_row(relative_path)
    PyImGui.end_child()


def _draw_button_browser() -> None:
    _draw_breadcrumbs()
    node = _browser_node()
    dirs = node.get("dirs", {})
    files = node.get("files", [])
    if PyImGui.begin_child("##modular_tester_recipe_browser", (0, 0), True, PyImGui.WindowFlags.HorizontalScrollbar):
        drew_any = False
        if isinstance(dirs, dict):
            for folder_name in sorted(str(name) for name in dirs):
                _draw_folder_row(folder_name)
                drew_any = True
        if isinstance(files, list):
            for relative_path in sorted(str(path) for path in files):
                _draw_recipe_row(relative_path)
                drew_any = True
        if not drew_any:
            PyImGui.text_colored("No recipes here.", MUTED)
    PyImGui.end_child()


def _draw_breadcrumbs() -> None:
    global _browser_path
    PyImGui.text_colored("Path", MUTED)
    PyImGui.same_line(0, 8)
    if PyImGui.small_button("modular_recipes##crumb_root"):
        _browser_path = []
    current: list[str] = []
    for depth, folder in enumerate(_browser_path):
        current.append(folder)
        PyImGui.same_line(0, 4)
        PyImGui.text_colored("/", MUTED)
        PyImGui.same_line(0, 4)
        if PyImGui.small_button(f"{folder}##crumb_{depth}_{'/'.join(current)}"):
            _browser_path = list(current)
    if _browser_path:
        PyImGui.same_line(0, 10)
        if PyImGui.small_button("Up##browser_up"):
            _go_up()


def _draw_folder_row(folder_name: str) -> None:
    global _browser_path
    label = f"> {folder_name}##folder_{_browser_label()}_{folder_name}"
    if _selectable_row(label):
        _browser_path = [*_browser_path, folder_name]
    PyImGui.text_colored(f"  {_browser_label()}/{folder_name}", MUTED)


def _draw_recipe_row(relative_path: str) -> None:
    global _selected_recipe
    summary = _recipe_summaries.get(relative_path) or _recipe_summary(relative_path)
    selected = relative_path == _selected_recipe
    status = _recipe_run_state(relative_path)
    status_label = {
        RUN_SUCCESS: "done",
        RUN_FAILED: "failed",
        RUN_RUNNING: "running",
    }.get(status, "pending")
    label = f"{summary.title}  [{status_label}]##recipe_{relative_path}"
    if _recipe_button(label, relative_path, selected, max(120.0, PyImGui.get_content_region_avail()[0])):
        _selected_recipe = relative_path
    PyImGui.text_colored(f"  {relative_path}  |  {summary.module}:{summary.factory}", MUTED)


def _draw_section_title(title: str, meta: str = "") -> None:
    PyImGui.text_colored(title, ACCENT)
    if meta:
        PyImGui.same_line(0, 8)
        PyImGui.text_colored(meta, MUTED)


def _draw_recipe_overview() -> None:
    selected = _selected_recipe_path()
    summary = _recipe_summaries.get(selected)
    if not selected or summary is None:
        PyImGui.text_colored("Select a Python recipe from Sources/modular_recipes.", MUTED)
        return

    _draw_section_title(summary.title, summary.kind)
    PyImGui.text_wrapped(selected)
    PyImGui.spacing()
    metric_flags = PyImGui.TableFlags.SizingStretchSame | PyImGui.TableFlags.NoSavedSettings
    if PyImGui.begin_table("##modular_tester_metrics", 3, metric_flags):
        PyImGui.table_next_row()
        PyImGui.table_set_column_index(0)
        _draw_metric("Internal", str(summary.steps), ACCENT)
        PyImGui.table_set_column_index(1)
        _draw_metric("Source", str(len(_source_steps_for_recipe(selected))), GOOD)
        PyImGui.table_set_column_index(2)
        _draw_metric("Mode", "Loop" if _loop else "Single", GOOD if _loop else TEXT)
        PyImGui.end_table()
    _draw_label_value("Factory", f"{summary.module}:{summary.factory}", ACCENT)
    PyImGui.spacing()


def _draw_metric(label: str, value: str, color: tuple[float, float, float, float]) -> None:
    PyImGui.text_colored(label, MUTED)
    PyImGui.text_scaled(value, color, 1.12)


def _draw_progress_panel() -> None:
    if _runner is None:
        PyImGui.progress_bar(0.0, -1.0, 0.0, "Idle")
        return

    running = _runner_is_running()
    paused = _runner_is_paused()
    step_current, step_total, recipe_title, step_title = _step_progress()
    source_index = int(_runner.blackboard.get("modular_tester_source_index", -1))
    source_total = int(_runner.blackboard.get("modular_tester_source_total", 0) or 0)
    planner_status = str(_runner.GetBlackboardValue("PLANNER_STATUS", "") or "")
    overlay = f"{source_index + 1}/{source_total}" if source_total > 0 and source_index >= 0 else _status_text()
    PyImGui.progress_bar(_progress_fraction(), -1.0, 0.0, overlay)
    PyImGui.spacing()
    run_state = "Running" if running else "Paused" if paused else "Stopped"
    _draw_label_value("Run", run_state, GOOD if running else WARN)
    if planner_status:
        _draw_label_value("Planner", planner_status)
    if recipe_title:
        _draw_label_value("Recipe", recipe_title)
    if source_total > 0 and source_index >= 0:
        _draw_label_value("Source", f"{source_index + 1}/{source_total}", ACCENT)
    if step_total > 0:
        _draw_label_value("Phase", f"{step_current}/{step_total} {step_title}", ACCENT)
    else:
        _draw_label_value("Phase", "not started", MUTED)
    target_error = str(_runner.blackboard.get("modular_target_error", "") or "")
    if target_error:
        PyImGui.text_colored("Target", BAD)
        PyImGui.same_line(0, 6)
        PyImGui.text_wrapped(target_error)
    move_state = str(_runner.blackboard.get("move_state", "") or "")
    if move_state:
        move_reason = str(_runner.blackboard.get("move_reason", "") or "")
        _draw_label_value("Move", move_state if not move_reason else f"{move_state}: {move_reason}", GOOD)


def _target_issue_available() -> bool:
    return _runner is not None and bool(str(_runner.blackboard.get("modular_target_error", "") or ""))


def _draw_runtime_controls() -> None:
    selected = _selected_recipe_path()
    running = _runner_is_running()
    paused = _runner_is_paused()
    PyImGui.begin_disabled(_runner is None)
    if _highlight_button("Copy context", 112):
        _copy_runtime_context()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not _target_issue_available())
    if _highlight_button("Copy target issue", 132):
        _copy_target_issue_context()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not selected or running)
    if _primary_button("Run selected", 116):
        _start_selected_recipe()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not running)
    if _quiet_button("Pause", 78):
        _pause_runner()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not paused)
    if _primary_button("Resume", 82):
        _resume_runner()
    PyImGui.end_disabled()
    PyImGui.same_line(0, 6)
    PyImGui.begin_disabled(not (running or paused))
    if _danger_button("Stop", 70):
        _stop_runner()
    PyImGui.end_disabled()


def _fmt_runtime_value(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.0f}"
    if isinstance(value, tuple):
        return "(" + ", ".join(_fmt_runtime_value(item) for item in value) + ")"
    if isinstance(value, list):
        return "[" + ", ".join(_fmt_runtime_value(item) for item in value) + "]"
    return str(value)


def _append_target_issue_context(lines: list[str], bb: dict) -> None:
    target_error = str(bb.get("modular_target_error", "") or "")
    if not target_error:
        return
    target_keys = (
        "modular_target_reason",
        "modular_target_kind",
        "modular_target_key",
        "modular_target_display_name",
        "modular_target_max_dist",
        "modular_target_registry_path",
        "modular_target_collection_path",
    )
    lines.append("")
    lines.append("Target error:")
    lines.append(f"- message: {target_error}")
    for key in target_keys:
        value = bb.get(key)
        if value not in (None, "", []):
            lines.append(f"- {key}: {_fmt_runtime_value(value)}")


def _runtime_context_text() -> str:
    selected = _selected_recipe_path() or _last_recipe or "<none>"
    summary = _recipe_summaries.get(selected)
    spec = _selected_spec(selected)
    step = _current_source_step_from_blackboard()
    bb = _runner.blackboard if _runner is not None else {}

    lines = [
        "Modular Tester stuck context",
        f"Run state: {_status_text()}",
        f"Status: {_status or '<none>'}",
        f"Recipe: {selected}",
    ]
    if summary is not None:
        lines.append(f"Title: {summary.title}")
    if spec is not None:
        lines.append(f"Factory: {spec.module}:{spec.factory}")

    planner_status = str(bb.get("PLANNER_STATUS", "") or "")
    if planner_status:
        lines.append(f"Planner: {planner_status}")
    current_step_name = str(bb.get("current_step_name", "") or _last_active_step_name or "")
    if current_step_name:
        lines.append(f"Phase: {current_step_name}")

    source_total = int(bb.get("modular_tester_source_total", 0) or 0)
    if step is not None:
        lines.extend(
            [
                "",
                "Current source:",
                f"- Progress: {step.index + 1}/{source_total}" if source_total > 0 else f"- Progress: {step.index + 1}",
                f"- Location: {step.file}:{step.line}",
                f"- Call: {step.call}",
                "```python",
                step.source,
                "```",
            ]
        )
    else:
        lines.extend(["", "Current source:", "- <not marked yet>"])

    _append_target_issue_context(lines, bb)

    move_keys = (
        "move_state",
        "move_reason",
        "move_target",
        "move_path_index",
        "move_path_count",
        "move_current_waypoint",
        "move_current_waypoint_index",
        "move_last_move_point",
        "move_current_pause_reason",
        "move_resume_recovery_active",
        "move_resume_recovery_reason",
        "move_stall_retry_count",
    )
    lines.append("")
    lines.append("Move blackboard:")
    found_move_value = False
    for key in move_keys:
        if key in bb and bb.get(key) not in (None, "", []):
            found_move_value = True
            lines.append(f"- {key}: {_fmt_runtime_value(bb.get(key))}")
    if not found_move_value:
        lines.append("- <no active move data>")

    if step is not None and step.points:
        lines.append("")
        lines.append("Source waypoints:")
        current_index = int(bb.get("move_current_waypoint_index", -1))
        for index, point in enumerate(step.points):
            marker = ">" if index == current_index else "-"
            lines.append(f"{marker} {index + 1}. ({point[0]:.0f}, {point[1]:.0f})")

    return "\n".join(lines).rstrip() + "\n"


def _copy_runtime_context() -> None:
    global _status
    PyImGui.set_clipboard_text(_runtime_context_text())
    _status = "Copied runtime context."


def _copy_target_issue_context() -> None:
    global _status
    PyImGui.set_clipboard_text(_runtime_context_text())
    _status = "Copied target issue context."


def _current_source_step_from_blackboard() -> SourceStep | None:
    if _runner is None:
        return None
    bb = _runner.blackboard
    line = int(bb.get("modular_tester_source_line", 0) or 0)
    if line <= 0:
        return None
    raw_points = bb.get("modular_tester_source_points", [])
    points: list[tuple[float, float]] = []
    if isinstance(raw_points, list):
        for point in raw_points:
            if isinstance(point, tuple) and len(point) == 2:
                points.append((float(point[0]), float(point[1])))
    return SourceStep(
        index=int(bb.get("modular_tester_source_index", 0)),
        file=str(bb.get("modular_tester_source_file", "") or ""),
        line=line,
        end_line=int(bb.get("modular_tester_source_end_line", line) or line),
        call=str(bb.get("modular_tester_source_call", "") or "BT step"),
        source=str(bb.get("modular_tester_source_text", "") or ""),
        points=tuple(points),
    )


def _draw_source_text(step: SourceStep) -> None:
    PyImGui.text_colored(f"{step.file}:{step.line}", ACCENT)
    source_lines = step.source.splitlines() or [step.call]
    if PyImGui.begin_child("##modular_tester_current_source", (0, 150), True, PyImGui.WindowFlags.HorizontalScrollbar):
        for offset, line in enumerate(source_lines):
            line_no = step.line + offset
            color = GOOD if offset == 0 else TEXT
            PyImGui.text_colored(f"{line_no:04d}: {line}", color)
    PyImGui.end_child()


def _draw_current_waypoint(step: SourceStep) -> None:
    if _runner is None:
        return
    bb = _runner.blackboard
    move_state = str(bb.get("move_state", "") or "")
    if move_state not in ("running", "paused") or not step.points:
        return
    current_index = int(bb.get("move_current_waypoint_index", -1))
    current_raw = bb.get("move_current_waypoint")
    current_text = ""
    if isinstance(current_raw, tuple) and len(current_raw) == 2:
        current_text = f" x={float(current_raw[0]):.0f}, y={float(current_raw[1]):.0f}"
    PyImGui.spacing()
    _draw_label_value("Waypoint", f"{current_index + 1}/{len(step.points)}{current_text}", GOOD)
    for index, point in enumerate(step.points):
        color = GOOD if index == current_index else MUTED
        prefix = ">" if index == current_index else " "
        PyImGui.text_colored(f"{prefix} {index + 1:02d}. ({point[0]:.0f}, {point[1]:.0f})", color)


def _draw_current_source_panel() -> None:
    step = _current_source_step_from_blackboard()
    if step is None:
        PyImGui.text_colored("Waiting for the first recipe step.", MUTED)
        return
    total = 0
    if _runner is not None:
        total = int(_runner.blackboard.get("modular_tester_source_total", 0) or 0)
    _draw_section_title("Current Code", f"{step.index + 1}/{total}" if total > 0 else "")
    _draw_label_value("Call", step.call, ACCENT)
    _draw_source_text(step)
    _draw_current_waypoint(step)


def _draw_recipe_detail() -> None:
    selected = _selected_recipe_path()
    spec = _selected_spec(selected)
    summary = _recipe_summaries.get(selected)
    if spec is None or summary is None:
        PyImGui.text_colored("No recipe selected.", MUTED)
        return
    _draw_section_title(summary.title, spec.kind)
    PyImGui.spacing()
    detail_flags = PyImGui.TableFlags.SizingStretchProp | PyImGui.TableFlags.RowBg
    if PyImGui.begin_table("##modular_tester_recipe_detail", 2, detail_flags):
        _draw_detail_row("Kind", spec.kind)
        _draw_detail_row("Key", spec.key)
        _draw_detail_row("Module", spec.module)
        _draw_detail_row("Function", spec.factory)
        _draw_detail_row("Internal actions", str(spec.source_steps))
        _draw_detail_row("Raw legacy actions", str(spec.raw_steps))
        _draw_detail_row("Source steps", str(len(_source_steps_for_recipe(selected))))
        PyImGui.end_table()


def _draw_detail_row(label: str, value: str) -> None:
    PyImGui.table_next_row()
    PyImGui.table_set_column_index(0)
    PyImGui.text_colored(label, MUTED)
    PyImGui.table_set_column_index(1)
    PyImGui.text_wrapped(value or "-")


def _draw_right_panel() -> None:
    _draw_recipe_overview()
    _draw_runtime_controls()
    PyImGui.spacing()
    _draw_progress_panel()
    if _status:
        PyImGui.spacing()
        PyImGui.text_colored(_status, _status_color())
    PyImGui.separator()
    if PyImGui.begin_tab_bar("##modular_tester_tabs", PyImGui.TabBarFlags.NoFlag):
        if PyImGui.begin_tab_item("Recipe Detail"):
            _draw_recipe_detail()
            PyImGui.end_tab_item()
        PyImGui.end_tab_bar()


def _draw_runtime_dashboard() -> None:
    _draw_runtime_controls()
    PyImGui.spacing()
    _draw_progress_panel()
    if _status:
        PyImGui.spacing()
        PyImGui.text_colored(_status, _status_color())
    PyImGui.separator()
    if PyImGui.begin_table(
        "##modular_tester_runtime_grid", 2, PyImGui.TableFlags.Resizable | PyImGui.TableFlags.SizingStretchProp
    ):
        PyImGui.table_setup_column("##runtime_current", PyImGui.TableColumnFlags.WidthStretch)
        PyImGui.table_setup_column("##runtime_detail", PyImGui.TableColumnFlags.WidthStretch)
        PyImGui.table_next_row()
        PyImGui.table_set_column_index(0)
        _draw_current_source_panel()
        PyImGui.table_set_column_index(1)
        _draw_recipe_detail()
        PyImGui.end_table()
    else:
        _draw_current_source_panel()
        PyImGui.separator()
        _draw_recipe_detail()


def _draw_main_layout() -> None:
    if _runtime_mode():
        if PyImGui.begin_child("##modular_tester_runtime", (0, 0), True, PyImGui.WindowFlags.NoFlag):
            _draw_runtime_dashboard()
        PyImGui.end_child()
        return

    flags = PyImGui.TableFlags.Resizable | PyImGui.TableFlags.SizingStretchProp | PyImGui.TableFlags.BordersInnerV
    if PyImGui.begin_table("##modular_tester_layout", 2, flags, 0.0, 0.0):
        PyImGui.table_setup_column("##recipes", PyImGui.TableColumnFlags.WidthFixed, 320.0)
        PyImGui.table_setup_column("##runner", PyImGui.TableColumnFlags.WidthStretch)
        PyImGui.table_next_row()
        PyImGui.table_set_column_index(0)
        if PyImGui.begin_child("##modular_tester_left", (0, 0), True, PyImGui.WindowFlags.NoFlag):
            _draw_recipe_picker()
        PyImGui.end_child()
        PyImGui.table_set_column_index(1)
        if PyImGui.begin_child("##modular_tester_right", (0, 0), True, PyImGui.WindowFlags.NoFlag):
            _draw_right_panel()
        PyImGui.end_child()
        PyImGui.end_table()
    else:
        _draw_recipe_picker()
        PyImGui.separator()
        _draw_right_panel()


def _main_impl() -> None:
    _tick_runner()

    PyImGui.set_next_window_size((880, 640), PyImGui.ImGuiCond.FirstUseEver)
    PyImGui.set_next_window_bg_alpha(1.0)
    theme_colors = _push_tester_theme()
    if not PyImGui.begin(MODULE_NAME):
        PyImGui.end()
        PyImGui.pop_style_color(theme_colors)
        return
    _draw_top_bar()
    _draw_main_layout()
    PyImGui.end()
    _draw_move_path_overlay()
    PyImGui.pop_style_color(theme_colors)


def main() -> None:
    guarded_widget_main(MODULE_NAME, _main_impl)


def tooltip() -> None:
    PyImGui.set_next_window_size((430, 0))
    PyImGui.begin_tooltip()
    PyImGui.text(MODULE_NAME)
    PyImGui.separator()
    PyImGui.text_wrapped("Run one Python modular BottingTree recipe.")
    PyImGui.text_wrapped("Use this for checking a newly recorded bot before adding it to a campaign.")
    PyImGui.end_tooltip()


if __name__ == "__main__":
    main()
