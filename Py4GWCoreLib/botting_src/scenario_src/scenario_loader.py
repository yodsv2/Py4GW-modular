from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .scenario_types import ScenarioAction, ScenarioDefinition, ScenarioKind


class ScenarioLoader:
    _RESERVED_ACTION_KEYS = {"action", "args", "kwargs", "optional", "description"}

    @staticmethod
    def load(path: Path) -> ScenarioDefinition:
        if not path.exists():
            raise FileNotFoundError(f"Scenario file not found: {path}")

        with path.open("r", encoding="utf-8") as fh:
            data = json.load(fh)

        if not isinstance(data, dict):
            raise ValueError(f"Invalid scenario file format: {path}")

        scenario_id = str(data.get("id", "")).strip()
        if not scenario_id:
            raise ValueError(f"Scenario id is required: {path}")

        kind_raw = data.get("kind", "")
        kind = ScenarioKind.normalize(kind_raw)

        name = str(data.get("name", scenario_id)).strip() or scenario_id
        actions_raw = data.get("actions", [])
        if not isinstance(actions_raw, list):
            raise ValueError(f"Scenario actions must be a list: {path}")

        actions: List[ScenarioAction] = []
        for index, item in enumerate(actions_raw):
            actions.append(ScenarioLoader._parse_action(item, path, index))

        metadata = data.get("metadata", {})
        if metadata is None:
            metadata = {}
        if not isinstance(metadata, dict):
            raise ValueError(f"Scenario metadata must be an object: {path}")

        return ScenarioDefinition(
            scenario_id=scenario_id,
            kind=kind,
            name=name,
            actions=actions,
            metadata=metadata,
        )

    @staticmethod
    def _parse_action(raw: Any, path: Path, index: int) -> ScenarioAction:
        if not isinstance(raw, dict):
            raise ValueError(f"Action at index {index} must be an object: {path}")

        action_name = str(raw.get("action", "")).strip()
        if not action_name:
            raise ValueError(f"Action name is required at index {index}: {path}")

        args = raw.get("args", [])
        if args is None:
            args = []
        if not isinstance(args, list):
            raise ValueError(f"Action args must be an array at index {index}: {path}")

        kwargs = raw.get("kwargs", {})
        if kwargs is None:
            kwargs = {}
        if not isinstance(kwargs, dict):
            raise ValueError(f"Action kwargs must be an object at index {index}: {path}")

        for key, value in raw.items():
            if key in ScenarioLoader._RESERVED_ACTION_KEYS:
                continue
            kwargs[key] = value

        optional = bool(raw.get("optional", False))
        description = str(raw.get("description", "")).strip()

        return ScenarioAction(
            action=action_name,
            args=args,
            kwargs=kwargs,
            optional=optional,
            description=description,
        )

