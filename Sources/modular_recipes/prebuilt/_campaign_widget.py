"""Shared ImGui widget helpers for prebuilt modular campaign runners."""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path

import PyImGui

from Py4GWCoreLib.BottingTree import BottingTree
from Py4GWCoreLib.Player import Player
from Py4GWCoreLib.enums_src.Map_enums import explorables
from Py4GWCoreLib.enums_src.Map_enums import outposts

GOOD = (0.22, 0.50, 0.28, 1.0)
GOOD_HOVER = (0.28, 0.62, 0.35, 1.0)
GOOD_ACTIVE = (0.18, 0.40, 0.22, 1.0)
BAD = (0.55, 0.18, 0.18, 1.0)
BAD_HOVER = (0.68, 0.24, 0.24, 1.0)
BAD_ACTIVE = (0.42, 0.13, 0.13, 1.0)
NEUTRAL = (0.18, 0.21, 0.24, 1.0)
NEUTRAL_HOVER = (0.25, 0.29, 0.33, 1.0)
NEUTRAL_ACTIVE = (0.14, 0.16, 0.18, 1.0)
SELECTED = (0.10, 0.45, 0.52, 1.0)
SELECTED_HOVER = (0.12, 0.58, 0.66, 1.0)
SELECTED_ACTIVE = (0.08, 0.36, 0.42, 1.0)
TEXT = (0.92, 0.94, 0.96, 1.0)
MUTED = (0.62, 0.66, 0.70, 1.0)
WARN = (1.00, 0.78, 0.32, 1.0)

_MAP_NAMES = {**outposts, **explorables}
_MISSION_ID_CACHE: dict[tuple[str, str, str], tuple[int, ...]] = {}


@dataclass(frozen=True)
class CampaignPhase:
    region: str
    kind: str
    key: str
    title: str


def _normalize(text: str) -> str:
    return re.sub(r'[^a-z0-9]+', '', str(text or '').casefold())


def _display_kind(kind: str) -> str:
    return str(kind or '').replace('_', ' ').title()


ColorTuple = tuple[float, float, float, float]


def _button_style(base: ColorTuple, hover: ColorTuple, active: ColorTuple) -> None:
    PyImGui.push_style_color(PyImGui.ImGuiCol.Button, base)
    PyImGui.push_style_color(PyImGui.ImGuiCol.ButtonHovered, hover)
    PyImGui.push_style_color(PyImGui.ImGuiCol.ButtonActive, active)


def _pop_button_style() -> None:
    PyImGui.pop_style_color(3)


def _character_key() -> str:
    try:
        name = str(Player.GetName() or '').strip()
    except Exception:
        name = ''
    return name or 'Unknown Character'


def _safe_int(value: object) -> int | None:
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 0)
        except ValueError:
            return None
    return None


def _call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Attribute):
        return node.attr
    if isinstance(node, ast.Name):
        return node.id
    return ''


def _keyword_int(call: ast.Call, *names: str) -> int | None:
    for keyword in call.keywords:
        if keyword.arg in names:
            try:
                return _safe_int(ast.literal_eval(keyword.value))
            except (ValueError, TypeError):
                return None
    return None


def _factory_source_ids(module_name: str, factory: str) -> list[tuple[str, int]]:
    try:
        module = import_module(module_name)
        source_path = Path(str(getattr(module, '__file__', '') or ''))
        if not source_path.is_file():
            return []
        tree = ast.parse(source_path.read_text(encoding='utf-8'))
    except Exception:
        return []

    target_func: ast.FunctionDef | None = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == factory:
            target_func = node
            break
    if target_func is None:
        return []

    ids: list[tuple[str, int]] = []
    for node in ast.walk(target_func):
        if not isinstance(node, ast.Call):
            continue
        name = _call_name(node.func)
        if name == 'Travel':
            map_id = _keyword_int(node, 'target_map_id', 'map_id')
        elif name in {'EnterChallenge', 'MoveAndExitMap'}:
            map_id = _keyword_int(node, 'target_map_id', 'map_id')
        elif name == 'WaitForMapLoad':
            map_id = _keyword_int(node, 'map_id', 'target_map_id')
        else:
            continue
        if map_id is not None and map_id > 0:
            ids.append((name, int(map_id)))
    return ids


def _map_name_matches_title(map_id: int, title: str, factory: str) -> bool:
    map_name = _MAP_NAMES.get(int(map_id), '')
    if not map_name:
        return False
    clean_map = re.sub(r'\s+\((?:level \d+|mission|explorable area)\)$', '', map_name, flags=re.IGNORECASE)
    clean_map = re.sub(r'\s+outpost$', '', clean_map, flags=re.IGNORECASE)
    title_norm = _normalize(title)
    factory_norm = _normalize(factory.replace('_', ' '))
    map_norm = _normalize(clean_map)
    return bool(
        map_norm
        and (map_norm.startswith(title_norm) or title_norm.startswith(map_norm) or map_norm.startswith(factory_norm))
    )


def _mission_map_ids(module_name: str, factory: str, title: str) -> tuple[int, ...]:
    cache_key = (module_name, factory, title)
    cached = _MISSION_ID_CACHE.get(cache_key)
    if cached is not None:
        return cached

    source_ids = _factory_source_ids(module_name, factory)
    seen: set[int] = set()
    matched: list[int] = []
    for _kind, map_id in source_ids:
        if map_id not in seen and _map_name_matches_title(map_id, title, factory):
            seen.add(map_id)
            matched.append(map_id)

    if not matched:
        for preferred in ('EnterChallenge', 'WaitForMapLoad', 'MoveAndExitMap', 'Travel'):
            for kind, map_id in source_ids:
                if kind == preferred and map_id not in seen:
                    seen.add(map_id)
                    matched.append(map_id)
            if matched:
                break

    result = tuple(matched)
    _MISSION_ID_CACHE[cache_key] = result
    return result


def _mission_bit_is_set(bits: list[int], map_id: int) -> bool:
    if map_id < 0:
        return False
    bucket = int(map_id) // 32
    bit = int(map_id) % 32
    if bucket < 0 or bucket >= len(bits):
        return False
    return bool((int(bits[bucket]) >> bit) & 1)


def _completed_mission_ids() -> list[int]:
    try:
        return list(Player.GetMissionsCompleted() or [])
    except Exception:
        return []


class CampaignWidget:
    def __init__(
        self,
        *,
        module_name: str,
        title: str,
        rows: list[tuple[str, str, str, str]],
        build_specs,
        options_type,
        create_bot,
        state_path: Path,
    ) -> None:
        self.module_name = module_name
        self.title = title
        self.phases = [CampaignPhase(*row) for row in rows]
        self.build_specs = build_specs
        self.specs_by_key = {(str(spec.kind), str(spec.key)): spec for spec in build_specs()}
        self.options_type = options_type
        self.create_bot = create_bot
        self.state_path = state_path
        self.selected_index = 0
        self.loop = False
        self.skip_completed = True
        self.status = 'Ready.'
        self.runner: BottingTree | None = None
        self.last_active_index = 0

    def _phase_spec(self, phase: CampaignPhase):
        return self.specs_by_key.get((phase.kind, phase.key))

    def _phase_status_at(self, index: int) -> tuple[str, str]:
        phase = self.phases[index]
        if phase.kind == 'mission':
            spec = self._phase_spec(phase)
            if spec is not None:
                map_ids = _mission_map_ids(spec.module, spec.factory, phase.title)
                if map_ids:
                    completed = _completed_mission_ids()
                    if any(_mission_bit_is_set(completed, map_id) for map_id in map_ids):
                        return 'complete', 'completed'
                    return 'incomplete', 'not completed'
        return 'unknown', 'pending'

    def _phase_is_complete_at(self, index: int) -> bool:
        status, _label = self._phase_status_at(index)
        return status == 'complete'

    def _start_index(self) -> int:
        if not self.skip_completed:
            return self.selected_index
        start_index = self.selected_index
        while start_index < len(self.phases) and self._phase_is_complete_at(start_index):
            start_index += 1
        return start_index

    def _runner_is_running(self) -> bool:
        return self.runner is not None and bool(self.runner.IsStarted()) and not bool(self.runner.IsPaused())

    def _runner_is_paused(self) -> bool:
        return self.runner is not None and bool(self.runner.IsPaused())

    def _active_phase_index(self) -> int:
        if self.runner is None:
            return self.last_active_index
        try:
            step_name = str(self.runner.GetBlackboardValue('current_step_name', '') or '')
        except Exception:
            step_name = ''
        match = re.match(r'\s*(\d+)\.', step_name)
        if match:
            self.last_active_index = max(0, min(len(self.phases) - 1, int(match.group(1)) - 1))
        return self.last_active_index

    def _tick_runner(self) -> None:
        if self.runner is None or not self._runner_is_running():
            return
        try:
            self.runner.tick()
        except Exception as exc:
            active_phase = self.phases[self._active_phase_index()]
            self.status = f'Run failed at {active_phase.title}: {exc}'
            try:
                self.runner.Stop()
            except Exception:
                pass
            self.runner = None
            return

        if self.runner is None or self._runner_is_running() or self._runner_is_paused():
            return
        try:
            planner_status = str(self.runner.GetBlackboardValue('PLANNER_STATUS', '') or '')
        except Exception:
            planner_status = ''
        active_phase = self.phases[self._active_phase_index()]
        if planner_status == 'PLANNER: Failed':
            self.status = f'Ended early at {active_phase.title}.'
        else:
            self.status = f'Completed run from {self.phases[self.selected_index].title}.'

    def _start(self) -> None:
        if not self.phases:
            self.status = 'No phases configured.'
            return
        start_index = self._start_index()
        if start_index >= len(self.phases):
            self.status = f'All phases from {self.phases[self.selected_index].title} are already completed.'
            return
        if self.runner is not None:
            try:
                self.runner.Stop()
            except Exception:
                pass
        skipped_count = start_index - self.selected_index
        self.selected_index = start_index
        self.last_active_index = start_index
        options = self.options_type(start_phase_index=start_index, loop=self.loop)
        self.runner = self.create_bot(options=options)
        self.runner.Start()
        skipped_text = f' Skipped {skipped_count} completed phase(s).' if skipped_count else ''
        remaining_count = len(self.phases) - start_index
        self.status = (
            f'Started from {self.phases[start_index].title}; '
            f'continuing through {remaining_count} phase(s).{skipped_text}'
        )

    def _stop(self) -> None:
        had_runner = self.runner is not None
        if self.runner is not None:
            try:
                self.runner.Stop()
            except Exception:
                pass
        self.runner = None
        if had_runner:
            active_phase = self.phases[self._active_phase_index()]
            self.status = f'Stopped at {active_phase.title}.'
        else:
            self.status = 'Stopped.'

    def _pause(self) -> None:
        if self.runner is not None:
            self.runner.Pause(True)
            self.status = 'Paused.'

    def _resume(self) -> None:
        if self.runner is not None:
            self.runner.Pause(False)
            self.status = 'Resumed.'

    def _button_colors(self, status: str, selected: bool) -> tuple[ColorTuple, ColorTuple, ColorTuple]:
        if selected:
            return SELECTED, SELECTED_HOVER, SELECTED_ACTIVE
        if status == 'complete':
            return GOOD, GOOD_HOVER, GOOD_ACTIVE
        if status in {'failed', 'incomplete'}:
            return BAD, BAD_HOVER, BAD_ACTIVE
        return NEUTRAL, NEUTRAL_HOVER, NEUTRAL_ACTIVE

    def _draw_controls(self) -> None:
        running = self._runner_is_running()
        paused = self._runner_is_paused()
        if PyImGui.button('Run from selected', 132, 28):
            self._start()
        PyImGui.same_line(0, 6)
        PyImGui.begin_disabled(not running)
        if PyImGui.button('Pause', 62, 28):
            self._pause()
        PyImGui.end_disabled()
        PyImGui.same_line(0, 6)
        PyImGui.begin_disabled(not paused)
        if PyImGui.button('Resume', 72, 28):
            self._resume()
        PyImGui.end_disabled()
        PyImGui.same_line(0, 6)
        PyImGui.begin_disabled(not (running or paused))
        if PyImGui.button('Stop', 56, 28):
            self._stop()
        PyImGui.end_disabled()
        PyImGui.same_line(0, 12)
        self.loop = PyImGui.checkbox('Loop', self.loop)
        PyImGui.same_line(0, 12)
        self.skip_completed = PyImGui.checkbox('Skip completed', self.skip_completed)

    def _draw_phase_button(self, index: int, phase: CampaignPhase) -> None:
        status, status_label = self._phase_status_at(index)
        selected = index == self.selected_index
        base, hover, active = self._button_colors(status, selected)
        _button_style(base, hover, active)
        label = (
            f'{index + 1:02d}. {phase.title} '
            f'[{_display_kind(phase.kind)} | {status_label}]##{self.module_name}_{index}'
        )
        if PyImGui.button(label, max(150.0, PyImGui.get_content_region_avail()[0]), 26):
            self.selected_index = index
        _pop_button_style()

    def _draw_phase_rows(self) -> None:
        current_region = ''
        if PyImGui.begin_child(
            f'##{self.module_name}_phases',
            (0, 0),
            True,
            PyImGui.WindowFlags.HorizontalScrollbar,
        ):
            for index, phase in enumerate(self.phases):
                if phase.region != current_region:
                    current_region = phase.region
                    PyImGui.spacing()
                    PyImGui.text_colored(current_region, WARN)
                self._draw_phase_button(index, phase)
        PyImGui.end_child()

    def draw(self) -> None:
        self._tick_runner()
        PyImGui.set_next_window_size((760, 760), PyImGui.ImGuiCond.FirstUseEver)
        if not PyImGui.begin(self.module_name):
            PyImGui.end()
            return

        PyImGui.text_colored(self.title, TEXT)
        PyImGui.same_line(0, 12)
        PyImGui.text_colored(_character_key(), MUTED)
        status_color = WARN if 'failed' in self.status.casefold() or 'stopped' in self.status.casefold() else MUTED
        PyImGui.text_colored(self.status, status_color)
        self._draw_controls()
        PyImGui.separator()
        self._draw_phase_rows()
        PyImGui.end()

    def tooltip(self) -> None:
        PyImGui.begin_tooltip()
        PyImGui.text(self.module_name)
        PyImGui.separator()
        PyImGui.text_wrapped(
            'Run the prebuilt modular campaign and mark completed missions from the active character state.'
        )
        PyImGui.end_tooltip()
