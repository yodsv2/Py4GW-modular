from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from .scenario_paths import get_botting_base_dir
from .scenario_types import ScenarioKind


class ScenarioRegistry:
    def __init__(self, base_dir: Path | None = None):
        self._base_dir = base_dir if base_dir is not None else get_botting_base_dir()
        self._manifest_path = self._base_dir / "scenarios" / "manifest.json"
        self._manifest_cache: Dict[str, Any] | None = None

    def _load_manifest(self) -> Dict[str, Any]:
        if self._manifest_cache is not None:
            return self._manifest_cache

        if not self._manifest_path.exists():
            self._manifest_cache = {}
            return self._manifest_cache

        with self._manifest_path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict):
            raise ValueError(f"Invalid scenarios manifest format: {self._manifest_path}")
        self._manifest_cache = data
        return data

    def resolve_path(self, kind: ScenarioKind | str, scenario: Any) -> Path:
        normalized_kind = ScenarioKind.normalize(kind)
        manifest = self._load_manifest()

        section_name = f"{normalized_kind.value}s"
        section = manifest.get(section_name, {})
        if not isinstance(section, dict):
            raise ValueError(f"Invalid manifest section: {section_name}")

        scenario_key = getattr(scenario, "name", None) or str(scenario)
        scenario_key = scenario_key.strip()
        if scenario_key not in section:
            raise KeyError(f"Scenario '{scenario_key}' not registered in {section_name}")

        rel_path = section[scenario_key]
        if not isinstance(rel_path, str):
            raise ValueError(f"Invalid path for scenario '{scenario_key}' in {section_name}")

        return (self._base_dir / "scenarios" / rel_path).resolve()

