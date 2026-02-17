from __future__ import annotations

from typing import TYPE_CHECKING, Any, Dict

from ..scenario_src.scenario_executor import ScenarioExecutor
from ..scenario_src.scenario_loader import ScenarioLoader
from ..scenario_src.scenario_registry import ScenarioRegistry
from ..scenario_src.scenario_types import (
    ScenarioDefinition,
    ScenarioExecutionResult,
    ScenarioKind,
)

if TYPE_CHECKING:
    from Py4GWCoreLib.botting_src.helpers import BottingClass


class _SCENARIOS:
    def __init__(self, parent: "BottingClass"):
        self.parent = parent
        self._config = parent.config
        self._helpers = parent.helpers

        self._registry = ScenarioRegistry()
        self._executor = ScenarioExecutor(parent)

        self._last_result = ScenarioExecutionResult(ok=False, reason="No scenario executed yet")

    def LastResult(self) -> ScenarioExecutionResult:
        return self._last_result

    def LastSuccess(self) -> bool:
        return bool(self._last_result.ok)

    def _set_result(self, result: ScenarioExecutionResult) -> None:
        self._last_result = result

    def _load_definition(self, kind: ScenarioKind | str, identifier: Any) -> ScenarioDefinition:
        path = self._registry.resolve_path(kind, identifier)
        definition = ScenarioLoader.load(path)
        expected_kind = ScenarioKind.normalize(kind)
        if definition.kind != expected_kind:
            raise ValueError(
                f"Scenario kind mismatch for '{definition.scenario_id}': "
                f"expected {expected_kind.value}, got {definition.kind.value}"
            )
        return definition

    def _coro_execute(self, definition: ScenarioDefinition, params: Dict[str, Any] | None = None):
        result = yield from self._executor.execute(definition, params=params)
        self._set_result(result)
        return result.ok

    def _enqueue(self, definition: ScenarioDefinition, step_name: str = "", params: Dict[str, Any] | None = None) -> bool:
        if not step_name:
            step_name = f"Scenario_{definition.kind.value}_{self._config.get_counter('CUSTOM_STEP')}"

        self._config.FSM.AddSelfManagedYieldStep(
            name=step_name,
            coroutine_fn=lambda: self._coro_execute(definition, params=params),
        )
        return True

    def _queue_kind(
        self,
        kind: ScenarioKind | str,
        identifier: Any,
        *,
        step_name: str = "",
        params: Dict[str, Any] | None = None,
    ) -> bool:
        try:
            definition = self._load_definition(kind, identifier)
        except Exception as exc:  # noqa: BLE001
            self._set_result(
                ScenarioExecutionResult(
                    ok=False,
                    scenario_id=getattr(identifier, "name", str(identifier)),
                    kind=ScenarioKind.normalize(kind).value,
                    reason=str(exc),
                )
            )
            return False
        return self._enqueue(definition, step_name=step_name, params=params)

    def Mission(self, identifier: Any, *, step_name: str = "", params: Dict[str, Any] | None = None) -> bool:
        return self._queue_kind(ScenarioKind.MISSION, identifier, step_name=step_name, params=params)

    def Quest(self, identifier: Any, *, step_name: str = "", params: Dict[str, Any] | None = None) -> bool:
        return self._queue_kind(ScenarioKind.QUEST, identifier, step_name=step_name, params=params)

    def Run(self, identifier: Any, *, step_name: str = "", params: Dict[str, Any] | None = None) -> bool:
        return self._queue_kind(ScenarioKind.RUN, identifier, step_name=step_name, params=params)

    def Vanquish(self, identifier: Any, *, step_name: str = "", params: Dict[str, Any] | None = None) -> bool:
        return self._queue_kind(ScenarioKind.VANQUISH, identifier, step_name=step_name, params=params)

