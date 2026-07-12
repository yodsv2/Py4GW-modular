"""Catalog for native Python modular BottingTree recipes."""

from __future__ import annotations

from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Sequence
from dataclasses import dataclass
from importlib import import_module
from types import ModuleType

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree

RECIPE_MODULES: tuple[str, ...] = (
    'Sources.modular_recipes.dungeons.eotn',
    'Sources.modular_recipes.farms.general',
    'Sources.modular_recipes.farms.nightfall.sunspear',
    'Sources.modular_recipes.missions.eotn.norn',
    'Sources.modular_recipes.missions.eotn.asura',
    'Sources.modular_recipes.missions.eotn.vanguard',
    'Sources.modular_recipes.missions.eotn.shared',
    'Sources.modular_recipes.missions.nightfall.desolation',
    'Sources.modular_recipes.missions.nightfall.istan',
    'Sources.modular_recipes.missions.nightfall.kourna',
    'Sources.modular_recipes.missions.nightfall.realm_of_torment',
    'Sources.modular_recipes.missions.nightfall.vabbi',
    'Sources.modular_recipes.missions.prophecies.ascalon',
    'Sources.modular_recipes.missions.prophecies.crystal_desert',
    'Sources.modular_recipes.missions.prophecies.kryta',
    'Sources.modular_recipes.missions.prophecies.maguuma_jungle',
    'Sources.modular_recipes.missions.prophecies.northern_shiverpeaks',
    'Sources.modular_recipes.missions.prophecies.ring_of_fire',
    'Sources.modular_recipes.missions.prophecies.southern_shiverpeaks',
    'Sources.modular_recipes.quests.eotn.norn',
    'Sources.modular_recipes.quests.eotn.asura',
    'Sources.modular_recipes.quests.eotn.vanguard',
    'Sources.modular_recipes.quests.eotn.shared',
    'Sources.modular_recipes.quests.factions.story',
    'Sources.modular_recipes.quests.fow.fissure_of_woe',
    'Sources.modular_recipes.quests.general',
    'Sources.modular_recipes.quests.nightfall.story',
    'Sources.modular_recipes.quests.prophecies.ascalon',
    'Sources.modular_recipes.quests.prophecies.kryta',
    'Sources.modular_recipes.quests.prophecies.maguuma_jungle',
    'Sources.modular_recipes.quests.prophecies.northern_shiverpeaks',
    'Sources.modular_recipes.quests.prophecies.ring_of_fire',
    'Sources.modular_recipes.quests.prophecies.story',
    'Sources.modular_recipes.routes.eotn.transit',
    'Sources.modular_recipes.routes.prophecies.transit',
)


@dataclass(frozen=True)
class RecipeSpec:
    kind: str
    key: str
    title: str = ''
    module: str = ''
    factory: str = ''
    source_steps: int = 0
    raw_steps: int = 0

    @property
    def steps(self) -> int:
        return self.source_steps


def _recipe_spec_from_entry(module_name: str, entry: object) -> RecipeSpec:
    if isinstance(entry, RecipeSpec):
        return (
            entry
            if entry.module
            else RecipeSpec(
                kind=entry.kind,
                key=entry.key,
                title=entry.title,
                module=module_name,
                factory=entry.factory,
                source_steps=entry.source_steps,
                raw_steps=entry.raw_steps,
            )
        )
    if isinstance(entry, dict):
        return RecipeSpec(
            kind=str(entry.get('kind', '')),
            key=str(entry.get('key', '')),
            title=str(entry.get('title', '')),
            module=module_name,
            factory=str(entry.get('factory', '')),
            source_steps=int(entry.get('source_steps', 0) or 0),
            raw_steps=int(entry.get('raw_steps', 0) or 0),
        )
    kind, key, title, factory, source_steps, raw_steps = entry  # type: ignore[misc]
    return RecipeSpec(
        kind=str(kind),
        key=str(key),
        title=str(title),
        module=module_name,
        factory=str(factory),
        source_steps=int(source_steps),
        raw_steps=int(raw_steps),
    )


def _load_recipes() -> tuple[RecipeSpec, ...]:
    specs: list[RecipeSpec] = []
    for module_name in RECIPE_MODULES:
        module = import_module(module_name)
        for entry in getattr(module, 'RECIPES', ()):  # module-local metadata only
            spec = _recipe_spec_from_entry(module_name, entry)
            if not spec.kind or not spec.key or not spec.factory:
                raise ValueError(f'Invalid modular recipe metadata in {module_name}: {entry!r}')
            specs.append(spec)
    return tuple(specs)


RECIPES: tuple[RecipeSpec, ...] = _load_recipes()
RECIPE_COUNT = len(RECIPES)
SOURCE_STEP_COUNT = sum(spec.source_steps for spec in RECIPES)
RAW_STEP_COUNT = sum(spec.raw_steps for spec in RECIPES)

# Backwards-compatible aliases for offline parity checks.
STEP_COUNT = RAW_STEP_COUNT
EXPANDED_STEP_COUNT = SOURCE_STEP_COUNT


def all_specs() -> list[RecipeSpec]:
    return list(RECIPES)


def _normalize_key(key: str) -> str:
    return str(key).strip().replace('\\', '/').casefold()


def get_spec(kind: str, key: str) -> RecipeSpec:
    normalized_kind = str(kind).strip().casefold()
    normalized_key = _normalize_key(key)
    for spec in RECIPES:
        if spec.kind.casefold() == normalized_kind and _normalize_key(spec.key) == normalized_key:
            return spec
    raise KeyError(f'Unknown modular recipe {normalized_kind}/{normalized_key}')


def resolve_spec(spec: RecipeSpec) -> RecipeSpec:
    if spec.module and spec.factory:
        return spec
    resolved = get_spec(spec.kind, spec.key)
    if spec.title and spec.title != resolved.title:
        return RecipeSpec(
            kind=resolved.kind,
            key=resolved.key,
            title=spec.title,
            module=resolved.module,
            factory=resolved.factory,
            source_steps=resolved.source_steps,
            raw_steps=resolved.raw_steps,
        )
    return resolved


def get_recipe_module(kind: str | RecipeSpec, key: str | None = None) -> ModuleType:
    spec = resolve_spec(kind) if isinstance(kind, RecipeSpec) else get_spec(str(kind), str(key or ''))
    return import_module(spec.module)


def get_recipe_factory(kind: str | RecipeSpec, key: str | None = None) -> Callable[[], BehaviorTree]:
    spec = resolve_spec(kind) if isinstance(kind, RecipeSpec) else get_spec(str(kind), str(key or ''))
    return getattr(import_module(spec.module), spec.factory)


def planner_steps_for_specs(
    specs: Sequence[RecipeSpec],
    *,
    start_index: int = 0,
    planner_prefix: str = '',
    debug_hook: Callable[[str], None] | None = None,
) -> list[tuple[str, Callable[[], BehaviorTree]]]:
    all_phase_specs = list(specs)
    start = max(0, int(start_index))
    selected_specs = all_phase_specs[start:]
    planner_steps: list[tuple[str, Callable[[], BehaviorTree]]] = []
    for offset, source_spec in enumerate(selected_specs, start=start):
        spec = resolve_spec(source_spec)
        if debug_hook is not None:
            debug_hook(
                f'Loading phase {offset + 1}/{len(all_phase_specs)} '
                f'{spec.kind}:{spec.key} from {spec.module}:{spec.factory}.'
            )
        step_name = f'{planner_prefix}{offset + 1:02d}. {spec.title or spec.factory}'
        planner_steps.append((step_name, get_recipe_factory(spec)))
    return planner_steps


def recipe_route_points(kind: str | RecipeSpec, key: str | None = None) -> list[tuple[float, float]]:
    spec = resolve_spec(kind) if isinstance(kind, RecipeSpec) else get_spec(str(kind), str(key or ''))
    module = import_module(spec.module)
    return list(getattr(module, 'ROUTE_POINTS_BY_RECIPE', {}).get(spec.factory, ()))


def specs_from_rows(rows: Iterable[tuple[str, str, str, str]]) -> list[RecipeSpec]:
    specs: list[RecipeSpec] = []
    for _region, kind, key, title in rows:
        spec = get_spec(kind, key)
        if title and title != spec.title:
            spec = RecipeSpec(
                kind=spec.kind,
                key=spec.key,
                title=title,
                module=spec.module,
                factory=spec.factory,
                source_steps=spec.source_steps,
                raw_steps=spec.raw_steps,
            )
        specs.append(spec)
    return specs


def derive_region_spans(rows: Sequence[tuple[str, str, str, str]]) -> list[tuple[str, int, int]]:
    if not rows:
        return []
    spans: list[tuple[str, int, int]] = []
    current_region = rows[0][0]
    start = 0
    for idx, row in enumerate(rows[1:], start=1):
        if row[0] != current_region:
            spans.append((current_region, start, idx - 1))
            current_region = row[0]
            start = idx
    spans.append((current_region, start, len(rows) - 1))
    return spans


def clamp_start_index(specs: Sequence[RecipeSpec], start_index: int) -> int:
    if not specs:
        return 0
    return max(0, min(int(start_index), len(specs) - 1))


__all__ = [
    'RECIPE_COUNT',
    'SOURCE_STEP_COUNT',
    'RAW_STEP_COUNT',
    'STEP_COUNT',
    'EXPANDED_STEP_COUNT',
    'RECIPE_MODULES',
    'RECIPES',
    'RecipeSpec',
    'all_specs',
    'clamp_start_index',
    'derive_region_spans',
    'get_recipe_factory',
    'get_recipe_module',
    'get_spec',
    'planner_steps_for_specs',
    'recipe_route_points',
    'resolve_spec',
    'specs_from_rows',
]
