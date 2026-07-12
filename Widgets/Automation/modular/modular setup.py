"""Configure the account-scoped hero priority used by modular recipes."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

import Py4GW
import PyImGui

from Py4GWCoreLib import Console
from Py4GWCoreLib import ConsoleLog
from Py4GWCoreLib import Player
from Py4GWCoreLib.enums_src.Hero_enums import HeroType
from Widgets.Automation.modular.widget_guard import guarded_widget_main


MODULE_NAME = "Modular Hero Setup"
MODULE_ICON = "Textures/Module_Icons/Route Planner.png"
MODULE_TAGS = ["Automation", "modular_bot", "heroes"]

GOOD = (0.42, 0.88, 0.55, 1.0)
WARN = (1.00, 0.78, 0.32, 1.0)
HERO_IDS = [int(hero.value) for hero in HeroType if int(hero.value) > 0]

_priority: list[int] = list(HERO_IDS)
_loaded_account_key = ""
_status = ""
_status_is_error = False


def _hero_name(hero_id: int) -> str:
    try:
        enum_name = HeroType(int(hero_id)).name
    except (TypeError, ValueError):
        return f"Hero {hero_id}"
    display_name = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", enum_name)
    return re.sub(r"(?<=[A-Za-z])(?=[0-9])|(?<=[0-9])(?=[A-Za-z])", " ", display_name)


def _project_root() -> Path:
    try:
        project_path = str(Py4GW.Console.get_projects_path() or "").strip()
        if project_path:
            return Path(project_path)
    except Exception:
        pass
    return Path.cwd()


def _account_key() -> str:
    try:
        email = str(Player.GetAccountEmail() or "").strip()
    except Exception:
        email = ""
    if not email:
        email = "default"
    safe_key = re.sub(r'[<>:"/\\|?*]+', "_", email).strip(" .")
    return safe_key or "default"


def _config_path(account_key: str | None = None) -> Path:
    return _project_root() / "Settings" / "ModularBot" / "configs" / f"{account_key or _account_key()}.json"


def _normalize_priority(raw: Any) -> list[int]:
    valid_ids = set(HERO_IDS)
    normalized: list[int] = []
    if isinstance(raw, list):
        for value in raw:
            try:
                hero_id = int(value)
            except (TypeError, ValueError):
                continue
            if hero_id in valid_ids and hero_id not in normalized:
                normalized.append(hero_id)
    normalized.extend(hero_id for hero_id in HERO_IDS if hero_id not in normalized)
    return normalized


def _read_config(path: Path) -> dict[str, Any]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return raw if isinstance(raw, dict) else {}


def _load_priority(account_key: str, *, reloading: bool = False) -> None:
    global _priority, _loaded_account_key, _status, _status_is_error

    path = _config_path(account_key)
    _loaded_account_key = account_key
    _status_is_error = False
    if not path.is_file():
        _priority = list(HERO_IDS)
        _status = "No saved priority found; using numerical order."
        return

    try:
        config = _read_config(path)
        _priority = _normalize_priority(config.get("priority", []))
        _status = "Priority reloaded." if reloading else "Priority loaded."
    except Exception as exc:
        _priority = list(HERO_IDS)
        _status = f"Could not load priority; using numerical order: {exc}"
        _status_is_error = True
        ConsoleLog(MODULE_NAME, f"Failed to load {path}: {exc}", Console.MessageType.Error)


def _ensure_loaded() -> None:
    account_key = _account_key()
    if account_key != _loaded_account_key:
        _load_priority(account_key)


def _save_priority() -> None:
    global _priority, _status, _status_is_error

    path = _config_path(_loaded_account_key or _account_key())
    temp_path: Path | None = None
    try:
        try:
            config = _read_config(path) if path.is_file() else {}
        except Exception:
            config = {}
        _priority = _normalize_priority(_priority)
        config["version"] = 1
        config["priority"] = list(_priority)

        path.parent.mkdir(parents=True, exist_ok=True)
        temp_path = path.with_name(f"{path.name}.{os.getpid()}.tmp")
        temp_path.write_text(json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(str(temp_path), str(path))
        _status = f"Priority saved for {_loaded_account_key}."
        _status_is_error = False
    except Exception as exc:
        _status = f"Could not save priority: {exc}"
        _status_is_error = True
        ConsoleLog(MODULE_NAME, f"Failed to save {path}: {exc}", Console.MessageType.Error)
    finally:
        if temp_path is not None and temp_path.exists():
            try:
                temp_path.unlink()
            except OSError:
                pass


def _move_to_top(index: int) -> None:
    if 0 < index < len(_priority):
        _priority.insert(0, _priority.pop(index))


def _move_up(index: int) -> None:
    if 0 < index < len(_priority):
        _priority[index - 1], _priority[index] = _priority[index], _priority[index - 1]


def _move_down(index: int) -> None:
    if 0 <= index < len(_priority) - 1:
        _priority[index], _priority[index + 1] = _priority[index + 1], _priority[index]


def _move_to_bottom(index: int) -> None:
    if 0 <= index < len(_priority) - 1:
        _priority.append(_priority.pop(index))


def _draw_priority_rows() -> None:
    if PyImGui.begin_child("##modular_hero_priority", (0, 0), True, PyImGui.WindowFlags.NoFlag):
        for index, hero_id in enumerate(list(_priority)):
            PyImGui.text(f"[::] {index + 1:02d}. {_hero_name(hero_id)} ({hero_id})")

            PyImGui.same_line(0, 0)
            try:
                available_width = float(PyImGui.get_content_region_avail()[0])
                button_width = 154.0
                if available_width > button_width:
                    PyImGui.set_cursor_pos_x(PyImGui.get_cursor_pos_x() + available_width - button_width)
            except Exception:
                pass

            if PyImGui.button(f"Top##hero_top_{index}"):
                _move_to_top(index)
            PyImGui.same_line(0, 4)
            if PyImGui.button(f"Up##hero_up_{index}"):
                _move_up(index)
            PyImGui.same_line(0, 4)
            if PyImGui.button(f"Dn##hero_down_{index}"):
                _move_down(index)
            PyImGui.same_line(0, 4)
            if PyImGui.button(f"Bottom##hero_bottom_{index}"):
                _move_to_bottom(index)
    PyImGui.end_child()


def _main_impl() -> None:
    _ensure_loaded()

    PyImGui.set_next_window_size((800, 720), PyImGui.ImGuiCond.FirstUseEver)
    if not PyImGui.begin(MODULE_NAME):
        PyImGui.end()
        return

    PyImGui.text("Global Hero Priority")
    PyImGui.text("Required heroes are added first, then this order fills remaining slots.")
    PyImGui.text(f"Account: {_loaded_account_key}")
    PyImGui.text(f"Priority entries loaded: {len(_priority)}")

    if PyImGui.button("Save Priority"):
        _save_priority()
    PyImGui.same_line(0, 8)
    if PyImGui.button("Reload Priority"):
        _load_priority(_account_key(), reloading=True)

    if _status:
        PyImGui.same_line(0, 12)
        PyImGui.text_colored(_status, WARN if _status_is_error else GOOD)

    _draw_priority_rows()
    PyImGui.end()


def main() -> None:
    guarded_widget_main(MODULE_NAME, _main_impl)


def tooltip() -> None:
    PyImGui.begin_tooltip()
    PyImGui.text(MODULE_NAME)
    PyImGui.separator()
    PyImGui.text_wrapped("Reorder and save the ModularBot hero priority for the active account.")
    PyImGui.end_tooltip()


if __name__ == "__main__":
    main()