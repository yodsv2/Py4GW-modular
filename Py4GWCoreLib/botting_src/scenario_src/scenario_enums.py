from __future__ import annotations

import json
from enum import Enum
from typing import Dict, Iterable

from .scenario_paths import get_scenarios_dir

def _manifest_entries(section: str) -> Dict[str, str]:
    manifest_path = get_scenarios_dir() / "manifest.json"
    if not manifest_path.exists():
        return {}

    with manifest_path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    section_data = data.get(section, {})
    if not isinstance(section_data, dict):
        return {}
    return {str(k): str(v) for k, v in section_data.items()}


def _build_enum(name: str, values: Iterable[str]) -> type[Enum]:
    clean_values = [value.strip() for value in values if value and value.strip()]
    if not clean_values:
        clean_values = ["NONE"]
    members = {value: value for value in clean_values}
    return Enum(name, members)


MissionEnum = _build_enum("MissionEnum", _manifest_entries("missions").keys())
QuestScenarioEnum = _build_enum("QuestScenarioEnum", _manifest_entries("quests").keys())
RunEnum = _build_enum("RunEnum", _manifest_entries("runs").keys())
VanquishEnum = _build_enum("VanquishEnum", _manifest_entries("vanquishes").keys())

# Convenience aliases matching common usage styles.
missionEnum = MissionEnum
questEnum = QuestScenarioEnum
runEnum = RunEnum
vanquishEnum = VanquishEnum

