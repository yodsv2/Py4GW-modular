from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class ScenarioKind(Enum):
    QUEST = "quest"
    MISSION = "mission"
    RUN = "run"
    VANQUISH = "vanquish"

    @staticmethod
    def normalize(kind: "ScenarioKind | str") -> "ScenarioKind":
        if isinstance(kind, ScenarioKind):
            return kind
        text = str(kind).strip().lower()
        for item in ScenarioKind:
            if item.value == text:
                return item
        raise ValueError(f"Unsupported scenario kind: {kind!r}")


@dataclass(slots=True)
class ScenarioAction:
    action: str
    args: List[Any] = field(default_factory=list)
    kwargs: Dict[str, Any] = field(default_factory=dict)
    optional: bool = False
    description: str = ""


@dataclass(slots=True)
class ScenarioDefinition:
    scenario_id: str
    kind: ScenarioKind
    name: str
    actions: List[ScenarioAction]
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ScenarioExecutionResult:
    ok: bool
    scenario_id: str = ""
    kind: str = ""
    failed_action_index: int = -1
    failed_action_name: str = ""
    reason: str = ""

