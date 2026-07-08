"""Record native Python modular recipe snippets while playing."""

from __future__ import annotations

import re
import time
from dataclasses import dataclass
from typing import Any

import PyAgent
import PyImGui

try:
    import PyDialog
except Exception:
    PyDialog = None

from Py4GWCoreLib import Agent
from Py4GWCoreLib import AgentArray
from Py4GWCoreLib import Console
from Py4GWCoreLib import ConsoleLog
from Py4GWCoreLib import Item
from Py4GWCoreLib import Map
from Py4GWCoreLib import Party
from Py4GWCoreLib import Player
from Py4GWCoreLib.modular.domain.target_registry import get_target_registry
from Widgets.Automation.modular.widget_guard import guarded_widget_main

MODULE_NAME = 'Modular Recorder'
MODULE_ICON = 'Textures/Module_Icons/Route Planner.png'
MODULE_TAGS = ['Automation', 'modular_bot', 'recording']

ACCENT = (0.30, 0.78, 0.86, 1.0)
GOOD = (0.42, 0.88, 0.55, 1.0)
WARN = (1.00, 0.78, 0.32, 1.0)
BAD = (1.00, 0.38, 0.38, 1.0)
MUTED = (0.62, 0.66, 0.70, 1.0)


@dataclass(frozen=True)
class TargetCapture:
    kind: str
    key: str
    display_name: str
    encoded_name: tuple[int, ...]
    registry_entry: str


_recipe_name = 'New Recording'
_recipe_function = 'new_recording'
_recorded_lines: list[str] = []
_route_points: list[tuple[int, int]] = []
_captured_registry_entries: dict[str, dict[str, str]] = {'npc': {}, 'enemy': {}, 'gadget': {}}
_collection_notes: list[str] = []
_status = ''
_last_action_ts: float | None = None
_auto_capture_dialogs = True
_dialog_init_attempted = False
_dialog_init_ok = False
_dialog_init_last_attempt = 0.0
_dialog_last_tick = 0

_exit_recording_active = False
_exit_recording_waiting_load = False
_exit_record_last_x = 0
_exit_record_last_y = 0
_exit_record_source_map_id = 0
_exit_record_source_map_name = ''

_travel_recording_active = False
_travel_record_source_map_id = 0


def _set_status(message: str, *, error: bool = False) -> None:
    global _status
    _status = message
    if error:
        ConsoleLog(MODULE_NAME, message, Console.MessageType.Error)


def _safe_function_name(value: str) -> str:
    cleaned = re.sub(r'\W+', '_', str(value or '').strip().lower()).strip('_')
    return cleaned or 'new_recording'


def _enum_key_from_name(name: str, default_prefix: str) -> str:
    cleaned = re.sub(r'[^A-Z0-9]+', '_', str(name or '').upper()).strip('_')
    return cleaned or default_prefix


def _safe_string(value: str) -> str:
    return repr(str(value or ''))


def _fmt_point(point: tuple[int, int]) -> str:
    return f'({int(point[0])}, {int(point[1])})'


def _current_xy() -> tuple[int, int]:
    x, y = Player.GetXY()
    return int(x), int(y)


def _target_registry_for_kind(kind: str) -> dict[str, object]:
    return dict(get_target_registry().get(kind, {}))


def _registry_has_key(kind: str, key: str) -> bool:
    registry = _target_registry_for_kind(kind)
    if key in registry:
        return True
    normalized = key.casefold()
    return any(str(existing_key).casefold() == normalized for existing_key in registry)


def _target_capture(kind: str, agent_id: int) -> TargetCapture | None:
    if agent_id <= 0 or not Agent.IsValid(agent_id):
        _set_status('Select a valid target first.', error=True)
        return None
    if kind == 'npc' and (Agent.IsItem(agent_id) or Agent.IsGadget(agent_id) or agent_id in AgentArray.GetEnemyArray()):
        _set_status('Selected target is not an NPC.', error=True)
        return None
    if kind == 'enemy' and agent_id not in AgentArray.GetEnemyArray():
        _set_status('Selected target is not an enemy.', error=True)
        return None
    if kind == 'gadget' and not Agent.IsGadget(agent_id):
        _set_status('Selected target is not a gadget.', error=True)
        return None

    encoded_name = tuple(int(value) for value in (PyAgent.PyAgent.GetAgentEncName(agent_id) or ()))
    if not encoded_name:
        _set_status('Selected target has no encrypted name; cannot record registry-backed targeting.', error=True)
        return None

    display_name = Agent.GetNameByID(agent_id) or f'{kind.title()} {agent_id}'
    key = _enum_key_from_name(display_name, kind.upper())
    encoded_text = ', '.join(str(value) for value in encoded_name)
    entry = f'"{key}": ((({encoded_text}),), {_safe_string(display_name)}),'
    return TargetCapture(kind=kind, key=key, display_name=display_name, encoded_name=encoded_name, registry_entry=entry)


def _remember_capture(capture: TargetCapture) -> None:
    _captured_registry_entries[capture.kind][capture.key] = capture.registry_entry
    note = f'{capture.kind}:{capture.key} -> {capture.display_name}'
    if not _registry_has_key(capture.kind, capture.key):
        note += ' (new registry entry)'
    if note not in _collection_notes:
        _collection_notes.append(note)


def _add_line(line: str) -> None:
    global _last_action_ts
    _recorded_lines.append(line)
    _last_action_ts = time.monotonic()
    _set_status(f'Recorded {len(_recorded_lines)} snippet line(s).')


def _line_block() -> str:
    return '\n'.join(_recorded_lines)


def _registry_block() -> str:
    sections: list[str] = []
    for kind, title in (('npc', 'NPC_TARGETS'), ('enemy', 'ENEMY_TARGETS'), ('gadget', 'GADGET_TARGETS')):
        entries = _captured_registry_entries[kind]
        if not entries:
            continue
        sections.append(f'# {title}')
        sections.extend(entries[key] for key in sorted(entries))
    return '\n'.join(sections)


def _route_points_block() -> str:
    if not _route_points:
        return ''
    points = ', '.join(_fmt_point(point) for point in _route_points)
    return f"ROUTE_POINTS_BY_RECIPE = {{\n    '{_safe_function_name(_recipe_function)}': ({points},),\n}}\n"


def _collection_notes_block() -> str:
    return '\n'.join(f'- {note}' for note in _collection_notes)


def _recipe_function_text() -> str:
    function_name = _safe_function_name(_recipe_function)
    title = _recipe_name.strip() or function_name.replace('_', ' ').title()
    children = _recorded_lines or ['BT.Succeeder()']
    child_lines = '\n'.join(f'            {line},' for line in children)
    return (
        f'def {function_name}() -> BehaviorTree:\n'
        '    return BT.Sequence(\n'
        f'        name={_safe_string(title)},\n'
        '        children=[\n'
        f'{child_lines}\n'
        '        ],\n'
        '    )\n'
    )


def _full_output() -> str:
    blocks = [_recipe_function_text()]
    registry = _registry_block()
    if registry:
        blocks.append('# Registry entries\n' + registry)
    route_points = _route_points_block()
    if route_points:
        blocks.append('# Route preview points\n' + route_points)
    notes = _collection_notes_block()
    if notes:
        blocks.append('# Collection notes\n' + notes)
    return '\n\n'.join(blocks)


def _copy(text: str, label: str) -> None:
    PyImGui.set_clipboard_text(text)
    _set_status(f'Copied {label}.')


def _copy_current_xy() -> None:
    _copy(_fmt_point(_current_xy()), 'current player coordinate')


def _ensure_dialog_initialized() -> bool:
    global _dialog_init_attempted, _dialog_init_last_attempt, _dialog_init_ok
    if PyDialog is None or not hasattr(PyDialog, 'PyDialog'):
        return False
    if _dialog_init_attempted and _dialog_init_ok:
        return True
    now = time.monotonic()
    if _dialog_init_attempted and now - _dialog_init_last_attempt < 5.0:
        return False
    _dialog_init_attempted = True
    _dialog_init_last_attempt = now
    try:
        init_fn = getattr(PyDialog.PyDialog, 'initialize', None)
        if init_fn is not None:
            init_fn()
        _dialog_init_ok = True
    except Exception as exc:
        _dialog_init_ok = False
        _set_status(f'PyDialog initialize failed: {exc}', error=True)
    return _dialog_init_ok


def _active_dialog_options() -> list[tuple[int, str]]:
    if not _ensure_dialog_initialized():
        return []
    getter = getattr(PyDialog.PyDialog, 'get_active_dialog_buttons', None)
    if getter is None:
        return []
    options: list[tuple[int, str]] = []
    seen: set[int] = set()
    for button in getter() or []:
        dialog_id = int(getattr(button, 'dialog_id', 0) or 0)
        if dialog_id <= 0 or dialog_id in seen:
            continue
        seen.add(dialog_id)
        message = str(getattr(button, 'message_decoded', '') or getattr(button, 'message', '') or '').strip()
        options.append((dialog_id, message))
    return options


def _poll_dialog_recorder() -> None:
    global _dialog_last_tick
    if not _auto_capture_dialogs or not _ensure_dialog_initialized():
        return
    getter = getattr(PyDialog.PyDialog, 'get_dialog_callback_journal_sent', None)
    if getter is None:
        return
    max_tick = _dialog_last_tick
    for entry in getter() or []:
        tick = int(getattr(entry, 'tick', 0) or 0)
        if tick <= _dialog_last_tick:
            continue
        max_tick = max(max_tick, tick)
        dialog_id = int(getattr(entry, 'dialog_id', 0) or 0)
        if dialog_id > 0:
            _record_dialog(dialog_id)
    _dialog_last_tick = max_tick


def _record_route_point() -> None:
    point = _current_xy()
    _route_points.append(point)
    if _recorded_lines and _recorded_lines[-1].startswith('BT.Move(pos=['):
        previous = _recorded_lines.pop()
        prefix = previous.removesuffix(')')
        _recorded_lines.append(prefix[:-1] + f', {_fmt_point(point)}])')
    else:
        _add_line(f'BT.Move(pos=[{_fmt_point(point)}])')
    _set_status(f'Recorded route point {_fmt_point(point)}.')


def _record_wait() -> None:
    elapsed_ms = 1000
    if _last_action_ts is not None:
        elapsed_ms = max(100, int((time.monotonic() - _last_action_ts) * 1000))
    _add_line(f'BT.Wait(duration_ms={elapsed_ms})')


def _record_interact(kind: str) -> None:
    capture = _target_capture(kind, int(Player.GetTargetID() or 0))
    if capture is None:
        return
    _remember_capture(capture)
    _add_line(f"BT.Interact(kind='{kind}', key='{capture.key}')")


def _record_dialog(dialog_id: int) -> None:
    capture = _target_capture('npc', int(Player.GetTargetID() or 0))
    if capture is None:
        return
    _remember_capture(capture)
    _add_line(f"BT.Dialog(kind='npc', key='{capture.key}', dialog_ids=[{_safe_string(hex(int(dialog_id)))}])")


def _record_enemy_target() -> None:
    capture = _target_capture('enemy', int(Player.GetTargetID() or 0))
    if capture is None:
        return
    _remember_capture(capture)
    _add_line(f"BT.MoveToTarget(kind='enemy', key='{capture.key}')")


def _record_item_pickup() -> None:
    target_id = int(Player.GetTargetID() or 0)
    if target_id <= 0 or not Agent.IsValid(target_id) or not Agent.IsItem(target_id):
        _set_status('Selected target is not an item.', error=True)
        return
    item_id = int(Agent.GetItemAgentItemID(target_id) or 0)
    model_id = int(Item.GetModelID(item_id) or 0) if item_id > 0 else 0
    if model_id <= 0:
        _set_status('Selected item has no model id.', error=True)
        return
    _add_line(f'BT.OptionalInteractItemByModel(model_id={model_id}, point=None, max_dist=4500)')


def _record_party_load() -> None:
    party_size = 7
    try:
        party_size = max(1, int(Party.GetPartySize() or 0) - 1)
    except Exception:
        party_size = 7
    _add_line(f'BT.LoadParty(max_heroes={party_size})')


def _start_exit_map_recording() -> None:
    global _exit_recording_active, _exit_recording_waiting_load
    global _exit_record_last_x, _exit_record_last_y, _exit_record_source_map_id, _exit_record_source_map_name
    _exit_record_last_x, _exit_record_last_y = _current_xy()
    _exit_record_source_map_id = int(Map.GetMapID() or 0)
    _exit_record_source_map_name = str(Map.GetMapName(_exit_record_source_map_id) or '').strip()
    _exit_recording_active = True
    _exit_recording_waiting_load = False
    _set_status(f'Exit-map recording started at {_fmt_point((_exit_record_last_x, _exit_record_last_y))}.')


def _poll_exit_map_recording() -> None:
    global _exit_recording_active, _exit_recording_waiting_load, _exit_record_last_x, _exit_record_last_y
    if not _exit_recording_active:
        return
    map_ready = bool(Map.IsMapReady())
    if not _exit_recording_waiting_load:
        if map_ready:
            _exit_record_last_x, _exit_record_last_y = _current_xy()
            return
        _exit_recording_waiting_load = True
        return
    if not map_ready:
        return
    target_map_id = int(Map.GetMapID() or 0)
    if target_map_id <= 0 or target_map_id == _exit_record_source_map_id:
        _exit_recording_active = False
        _exit_recording_waiting_load = False
        _set_status('Exit-map recording canceled; map did not change.', error=True)
        return
    _add_line(
        f'BT.MoveAndExitMap(pos={_fmt_point((_exit_record_last_x, _exit_record_last_y))}, '
        f'target_map_id={target_map_id}, move_tolerance=300)'
    )
    _exit_recording_active = False
    _exit_recording_waiting_load = False


def _start_travel_recording() -> None:
    global _travel_recording_active, _travel_record_source_map_id
    _travel_record_source_map_id = int(Map.GetMapID() or 0)
    _travel_recording_active = True
    _set_status(f'Travel recording started from map {_travel_record_source_map_id}.')


def _poll_travel_recording() -> None:
    global _travel_recording_active
    if not _travel_recording_active:
        return
    current_map_id = int(Map.GetMapID() or 0)
    if current_map_id <= 0 or current_map_id == _travel_record_source_map_id:
        return
    _add_line(f'BT.Travel(target_map_id={current_map_id})')
    _travel_recording_active = False


def _grid_button(label: str, column: int, *, help_text: str = '') -> bool:
    if column > 0:
        PyImGui.same_line(0, 6)
    clicked = PyImGui.button(label, 150, 0)
    if help_text and PyImGui.is_item_hovered():
        PyImGui.set_tooltip(help_text)
    return clicked


def _draw_controls() -> None:
    global _recipe_name, _recipe_function, _auto_capture_dialogs, _recorded_lines, _route_points, _collection_notes
    global _captured_registry_entries

    _recipe_name = PyImGui.input_text('Recipe Name##modular_recorder_name', _recipe_name, 120)
    next_function = PyImGui.input_text('Function##modular_recorder_function', _recipe_function, 120)
    _recipe_function = _safe_function_name(next_function)
    _auto_capture_dialogs = PyImGui.checkbox(
        'Auto Capture Dialog Clicks##modular_recorder_dialogs', _auto_capture_dialogs
    )

    PyImGui.separator()
    PyImGui.text_colored('Movement', MUTED)
    if _grid_button('Route Point', 0, help_text='Append current player XY to route preview and a BT.Move path.'):
        _record_route_point()
    if _grid_button('Exit Map', 1, help_text='Start watching the next portal transition.'):
        _start_exit_map_recording()
    if _grid_button('Travel', 2, help_text='Start watching the next map id change as a travel step.'):
        _start_travel_recording()
    if _grid_button('Wait', 0, help_text='Record elapsed wait since the previous action.'):
        _record_wait()
    if _grid_button('Wait Map Load', 1, help_text='Record wait for current map id.'):
        _add_line(f'BT.WaitForMapLoad(map_id={int(Map.GetMapID() or 0)}, timeout_ms=10000)')

    PyImGui.spacing()
    PyImGui.text_colored('Target', MUTED)
    if _grid_button('NPC Interact', 0):
        _record_interact('npc')
    if _grid_button('Gadget Interact', 1):
        _record_interact('gadget')
    if _grid_button('Enemy Target', 2):
        _record_enemy_target()
    if _grid_button('Item Pickup', 0):
        _record_item_pickup()

    PyImGui.spacing()
    PyImGui.text_colored('Party', MUTED)
    if _grid_button('Load Party', 0):
        _record_party_load()
    if _grid_button('Resign', 1):
        _add_line('BT.Resign(wait_for_map_load=True)')

    PyImGui.spacing()
    PyImGui.text_colored('Clipboard', MUTED)
    if _grid_button('Copy XY', 0, help_text='Copy the current player coordinate as an (x, y) tuple.'):
        _copy_current_xy()
    if _grid_button('Copy Function', 1):
        _copy(_recipe_function_text(), 'recipe function')
    if _grid_button('Copy Registry', 2):
        _copy(_registry_block(), 'registry entries')
    if _grid_button('Copy Routes', 0):
        _copy(_route_points_block(), 'route points')
    if _grid_button('Copy All', 1):
        _copy(_full_output(), 'full recording')
    if _grid_button('Copy Notes', 2):
        _copy(_collection_notes_block(), 'collection notes')
    if _grid_button('Clear', 0):
        _recorded_lines = []
        _route_points = []
        _collection_notes = []
        _captured_registry_entries = {'npc': {}, 'enemy': {}, 'gadget': {}}
        _set_status('Cleared recording.')


def _draw_target_panel() -> None:
    target_id = int(Player.GetTargetID() or 0)
    PyImGui.text_colored('Current Target', MUTED)
    if target_id <= 0 or not Agent.IsValid(target_id):
        PyImGui.text_colored('No valid target selected.', WARN)
        return
    x, y = Agent.GetXY(target_id)
    name = Agent.GetNameByID(target_id) or ''
    encoded = tuple(int(value) for value in (PyAgent.PyAgent.GetAgentEncName(target_id) or ()))
    PyImGui.text(f'[{target_id}] {name}')
    PyImGui.text(f'XY: {_fmt_point((int(x), int(y)))}')
    PyImGui.text(f"Encoded: {encoded if encoded else '<missing>'}")

    if PyImGui.button('Copy Target Registry Entry##modular_recorder_copy_target'):
        kind = 'item'
        if Agent.IsGadget(target_id):
            kind = 'gadget'
        elif target_id in AgentArray.GetEnemyArray():
            kind = 'enemy'
        elif not Agent.IsItem(target_id):
            kind = 'npc'
        capture = _target_capture(kind, target_id) if kind != 'item' else None
        if capture is not None:
            _copy(capture.registry_entry, 'target registry entry')


def _draw_dialog_options() -> None:
    PyImGui.spacing()
    PyImGui.text_colored('Active Dialog Options', MUTED)
    options = _active_dialog_options()
    if not options:
        PyImGui.text_colored('No active dialog buttons detected.', MUTED)
        return
    for dialog_id, message in options[:10]:
        if PyImGui.button(f'Record {hex(dialog_id)}##dialog_{dialog_id}', 120, 0):
            _record_dialog(dialog_id)
        PyImGui.same_line(0, 6)
        PyImGui.text_wrapped(message or hex(dialog_id))


def _draw_preview() -> None:
    PyImGui.text_colored('Preview', MUTED)
    if PyImGui.begin_child('##modular_recorder_preview', (0, 0), True, PyImGui.WindowFlags.HorizontalScrollbar):
        PyImGui.text(_full_output())
    PyImGui.end_child()


def _main_impl() -> None:
    _poll_dialog_recorder()
    _poll_exit_map_recording()
    _poll_travel_recording()

    PyImGui.set_next_window_size((1020, 680), PyImGui.ImGuiCond.FirstUseEver)
    if not PyImGui.begin(MODULE_NAME):
        PyImGui.end()
        return
    PyImGui.text_colored(MODULE_NAME, ACCENT)
    PyImGui.same_line(0, 12)
    PyImGui.text_colored(
        f'{len(_recorded_lines)} lines  |  {sum(len(v) for v in _captured_registry_entries.values())} registry entries',
        MUTED,
    )
    if _status:
        PyImGui.text_colored(_status, BAD if 'failed' in _status.lower() or 'cannot' in _status.lower() else GOOD)
    if _exit_recording_active:
        PyImGui.text_colored('Exit-map recorder active.', WARN)
    if _travel_recording_active:
        PyImGui.text_colored('Travel recorder active.', WARN)
    PyImGui.separator()

    if PyImGui.begin_table('##modular_recorder_layout', 2, PyImGui.TableFlags.SizingStretchProp):
        PyImGui.table_next_row()
        PyImGui.table_set_column_index(0)
        _draw_controls()
        _draw_target_panel()
        _draw_dialog_options()
        PyImGui.table_set_column_index(1)
        _draw_preview()
        PyImGui.end_table()
    PyImGui.end()


def main() -> None:
    guarded_widget_main(MODULE_NAME, _main_impl)


def tooltip() -> None:
    PyImGui.begin_tooltip()
    PyImGui.text(MODULE_NAME)
    PyImGui.separator()
    PyImGui.text_wrapped('Record concise Python BT recipe snippets and encrypted target registry entries.')
    PyImGui.end_tooltip()


if __name__ == '__main__':
    main()
