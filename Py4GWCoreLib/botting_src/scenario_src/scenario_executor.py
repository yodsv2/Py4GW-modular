from __future__ import annotations

import inspect
import re
from typing import Any, Callable, Dict, Generator, Iterable, Tuple

from .scenario_types import ScenarioAction, ScenarioDefinition, ScenarioExecutionResult


class ScenarioExecutor:
    _PLACEHOLDER_PATTERN = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)\}")
    _HEX_PATTERN = re.compile(r"^0x[0-9a-fA-F]+$")

    def __init__(self, bot: Any):
        self._bot = bot
        self._action_index: Dict[str, Tuple[Any, str]] | None = None

    def _build_action_index(self) -> Dict[str, Tuple[Any, str]]:
        if self._action_index is not None:
            return self._action_index

        index: Dict[str, Tuple[Any, str]] = {}
        components: Iterable[str] = (
            "Map",
            "Move",
            "Wait",
            "Dialogs",
            "Interact",
            "Party",
            "Target",
            "Items",
            "Merchant",
            "SkillBar",
            "Multibox",
            "Properties",
            "Templates",
            "Quest",
            "Player",
        )

        for component_name in components:
            component = getattr(self._bot, component_name, None)
            if component is None:
                continue
            for method_name in dir(component):
                if method_name.startswith("_"):
                    continue
                method = getattr(component, method_name, None)
                if not callable(method):
                    continue

                comp_key = component_name.lower()
                name_key = method_name.lower()
                snake_name_key = _camel_to_snake(method_name).lower()

                keys = (
                    f"{comp_key}.{name_key}",
                    f"{comp_key}.{snake_name_key}",
                    f"{comp_key}_{name_key}",
                    f"{comp_key}_{snake_name_key}",
                )
                for key in keys:
                    index.setdefault(_normalize_token(key), (component, method_name))

                short_key = _normalize_token(name_key)
                index.setdefault(short_key, (component, method_name))

                short_snake_key = _normalize_token(snake_name_key)
                index.setdefault(short_snake_key, (component, method_name))

        self._action_index = index
        return index

    def _resolve_callable(self, action_name: str) -> tuple[Callable[..., Any], bool]:
        normalized = _normalize_token(action_name)

        # Explicit dotted form is preferred when provided.
        if "." in action_name:
            component_name, method_name = action_name.split(".", 1)
            component = getattr(self._bot, component_name.strip(), None)
            if component is None:
                raise KeyError(f"Unknown action component: {component_name!r}")
            callable_obj, is_coro = self._resolve_method_callable(component, method_name.strip())
            return callable_obj, is_coro

        action_index = self._build_action_index()
        if normalized not in action_index:
            raise KeyError(f"Unknown scenario action: {action_name!r}")

        component, method_name = action_index[normalized]
        callable_obj, is_coro = self._resolve_method_callable(component, method_name)
        return callable_obj, is_coro

    @staticmethod
    def _resolve_method_callable(component: Any, method_name: str) -> tuple[Callable[..., Any], bool]:
        snake_name = _camel_to_snake(method_name)
        coro_name = f"_coro_{snake_name}"
        maybe_coro = getattr(component, coro_name, None)
        if callable(maybe_coro):
            return maybe_coro, True

        maybe_public = getattr(component, method_name, None)
        if not callable(maybe_public):
            raise KeyError(f"Action method not callable: {type(component).__name__}.{method_name}")

        if inspect.isgeneratorfunction(maybe_public):
            return maybe_public, True
        return maybe_public, False

    def _apply_params(self, value: Any, params: Dict[str, Any]) -> Any:
        if isinstance(value, str):
            def _replace(match: re.Match[str]) -> str:
                key = match.group(1)
                if key not in params:
                    return match.group(0)
                return str(params[key])

            replaced = self._PLACEHOLDER_PATTERN.sub(_replace, value)
            # If token is exactly one placeholder and value exists, preserve type.
            if value.startswith("${") and value.endswith("}") and len(value) > 3:
                key = value[2:-1]
                if key in params:
                    return params[key]
            return replaced

        if isinstance(value, list):
            return [self._apply_params(item, params) for item in value]

        if isinstance(value, dict):
            return {k: self._apply_params(v, params) for k, v in value.items()}

        return value

    def _coerce_literals(self, value: Any) -> Any:
        if isinstance(value, str) and self._HEX_PATTERN.match(value.strip()):
            return int(value.strip(), 16)
        if isinstance(value, list):
            return [self._coerce_literals(item) for item in value]
        if isinstance(value, dict):
            return {k: self._coerce_literals(v) for k, v in value.items()}
        return value

    def _call_action(
        self,
        action: ScenarioAction,
        params: Dict[str, Any],
    ) -> Generator[Any, Any, bool]:
        args = self._coerce_literals(self._apply_params(action.args, params))
        kwargs = self._coerce_literals(self._apply_params(action.kwargs, params))

        callable_obj, is_coro = self._resolve_callable(action.action)
        if is_coro:
            result = yield from callable_obj(*args, **kwargs)
        else:
            result = callable_obj(*args, **kwargs)

        if isinstance(result, bool):
            return result
        return True

    def execute(
        self,
        definition: ScenarioDefinition,
        params: Dict[str, Any] | None = None,
    ) -> Generator[Any, Any, ScenarioExecutionResult]:
        safe_params = params or {}

        for index, action in enumerate(definition.actions):
            try:
                success = yield from self._call_action(action, safe_params)
                if not success:
                    if action.optional:
                        continue
                    return ScenarioExecutionResult(
                        ok=False,
                        scenario_id=definition.scenario_id,
                        kind=definition.kind.value,
                        failed_action_index=index,
                        failed_action_name=action.action,
                        reason="Action returned False",
                    )
            except Exception as exc:  # noqa: BLE001
                if action.optional:
                    continue
                return ScenarioExecutionResult(
                    ok=False,
                    scenario_id=definition.scenario_id,
                    kind=definition.kind.value,
                    failed_action_index=index,
                    failed_action_name=action.action,
                    reason=str(exc),
                )

        return ScenarioExecutionResult(
            ok=True,
            scenario_id=definition.scenario_id,
            kind=definition.kind.value,
        )


def _camel_to_snake(name: str) -> str:
    first = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first).lower()


def _normalize_token(value: str) -> str:
    return re.sub(r"[\s\-_/]+", ".", value.strip().lower())

