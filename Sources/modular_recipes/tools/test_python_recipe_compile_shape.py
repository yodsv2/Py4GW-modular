"""Offline compile-shape check for Python modular recipes."""

from __future__ import annotations

import ast
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from Sources.modular_recipes.tools import _stubs
else:
    from . import _stubs


RECIPE_ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_GENERATED_SEQUENCE_NAMES = {
    "StepWithPostWait",
    "InteractNpc",
    "InteractNpcAtPoint",
    "InteractGadget",
    "InteractGadgetAtPoint",
    "InteractItem",
    "InteractDialog",
    "MoveToResolvedDialogTarget",
    "RouteToEnemyTarget",
    "MapTravel",
}
FORBIDDEN_RECIPE_HELPERS = {
    "MapTravel",
    "WithPostWait",
    "MoveToNamedTarget",
    "MoveToAgentByModelID",
    "MoveToNearestNPC",
    "InteractNamedTarget",
    "InteractNamedTargetAtPoint",
    "InteractNPC",
    "InteractNPCAtPoint",
    "InteractGadget",
    "InteractGadgetAtPoint",
    "InteractItem",
    "DialogWithNPC",
    "DialogWithNamedTarget",
    "DialogWithNamedTargetAtPoint",
    "DialogWithModelTarget",
    "DialogAtPoint",
    "ModularDialogSequence",
}


def _recipe_module_paths() -> list[Path]:
    return [
        path
        for path in RECIPE_ROOT.rglob("*.py")
        if "tools" not in path.parts and "prebuilt" not in path.parts and path.name not in {"__init__.py", "catalog.py"}
    ]


def _sequence_name(node: ast.Call) -> str | None:
    for keyword in node.keywords:
        if keyword.arg == "name":
            try:
                value = ast.literal_eval(keyword.value)
            except Exception:
                return None
            return value if isinstance(value, str) else None
    return None


def _assert_no_generated_sequence_literals() -> None:
    hits: list[str] = []
    for path in _recipe_module_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "BT"
                and node.func.attr == "Sequence"
            ):
                sequence_name = _sequence_name(node)
                if sequence_name in FORBIDDEN_GENERATED_SEQUENCE_NAMES:
                    rel_path = path.relative_to(RECIPE_ROOT.parent.parent)
                    hits.append(f"{rel_path}:{node.lineno} {sequence_name}")
    assert not hits, "Generated sequence literals remain:\n" + "\n".join(hits[:50])


def _assert_no_removed_recipe_helpers() -> None:
    hits: list[str] = []
    for path in _recipe_module_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "BT"
                and node.func.attr in FORBIDDEN_RECIPE_HELPERS
            ):
                rel_path = path.relative_to(RECIPE_ROOT.parent.parent)
                hits.append(f"{rel_path}:{node.lineno} BT.{node.func.attr}")
    assert not hits, "Removed recipe helpers remain:\n" + "\n".join(hits[:50])


def _assert_no_per_recipe_route_point_constants() -> None:
    hits: list[str] = []
    for path in _recipe_module_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            name: str | None = None
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                name = node.target.id
            elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
            if name and name.endswith("_ROUTE_POINTS") and name != "ROUTE_POINTS_BY_RECIPE":
                rel_path = path.relative_to(RECIPE_ROOT.parent.parent)
                hits.append(f"{rel_path}:{node.lineno} {name}")
    assert not hits, "Per-recipe route point constants remain:\n" + "\n".join(hits[:50])


def _assert_no_generated_metadata_constants() -> None:
    hits: list[str] = []
    forbidden_names = {"SOURCE_STEP_COUNTS", "TITLES"}
    for path in _recipe_module_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in tree.body:
            name: str | None = None
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                name = node.target.id
            elif isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
            elif isinstance(node, ast.FunctionDef) and node.name == "route_points":
                name = node.name
            if name and (
                name in forbidden_names
                or name == "route_points"
                or name.endswith("_TITLE")
                or name.endswith("_REQUIRED_HERO")
                or name.endswith("_SOURCE_STEP_COUNT")
            ):
                rel_path = path.relative_to(RECIPE_ROOT.parent.parent)
                hits.append(f"{rel_path}:{node.lineno} {name}")
    assert not hits, "Generated recipe metadata remains:\n" + "\n".join(hits[:50])


def _assert_no_zero_duration_waits() -> None:
    hits: list[str] = []
    for path in _recipe_module_paths():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "BT"
                and node.func.attr == "Wait"
            ):
                continue
            values = list(node.args)
            values.extend(keyword.value for keyword in node.keywords if keyword.arg == "duration_ms")
            for value_node in values:
                try:
                    value = ast.literal_eval(value_node)
                except Exception:
                    continue
                if value == 0:
                    rel_path = path.relative_to(RECIPE_ROOT.parent.parent)
                    hits.append(f"{rel_path}:{node.lineno}")
                    break
    assert not hits, "Zero-duration waits remain:\n" + "\n".join(hits[:50])


def _assert_wrapper_helpers_compile() -> None:
    from Sources.ApoSource.ApoBottingLib import wrappers as BT

    auto_party_tree = BT.LoadParty(max_heroes=8, required_hero=["Koss"])
    assert auto_party_tree.root.kwargs["target_hero_count"] == 7
    assert len(auto_party_tree.root.kwargs["hero_ids"]) > 7

    exact_party_tree = BT.LoadParty(hero_ids=[6])
    assert exact_party_tree.root.kwargs["hero_ids"] == [6]
    assert exact_party_tree.root.kwargs["target_hero_count"] is None

    helper_trees = [
        auto_party_tree,
        exact_party_tree,
        BT.TargetNearest(0, 0),
        BT.TargetNearestGadget(0, 0),
        BT.TargetAgentByModelID(123),
        BT.InteractTarget(),
        BT.Travel(target_map_id=1),
        BT.Travel(target_map_id=1, leave_party=True),
        BT.LeaveParty(),
        BT.TargetNamedAgent(kind="npc", key="BROTHER_MHENLO"),
        BT.MoveToTarget(kind="npc", key="BROTHER_MHENLO"),
        BT.MoveToTarget(kind="enemy", key="RINKHAL_MONITOR"),
        BT.MoveToTarget(kind="gadget"),
        BT.MoveToTarget(kind="npc", model_id=123),
        BT.Interact(kind="npc"),
        BT.Interact(kind="npc", key="BROTHER_MHENLO"),
        BT.Interact(kind="gadget", key="CHEST_OF_BURROWS"),
        BT.Interact(kind="gadget", pos=(0, 0)),
        BT.Interact(kind="item"),
        BT.Dialog(["0x84"], kind="npc"),
        BT.Dialog(["0x84"], kind="npc", key="BROTHER_MHENLO"),
        BT.Dialog(["0x84"], kind="npc", model_id=123),
        BT.Dialog(["0x84"], pos=(0, 0)),
    ]
    for tree in helper_trees:
        assert tree.__class__.__name__ == "BehaviorTree"


def main() -> int:
    _stubs.install()
    from Sources.modular_recipes.catalog import EXPANDED_STEP_COUNT
    from Sources.modular_recipes.catalog import RAW_STEP_COUNT
    from Sources.modular_recipes.catalog import RECIPE_COUNT
    from Sources.modular_recipes.catalog import RECIPE_MODULES
    from Sources.modular_recipes.catalog import SOURCE_STEP_COUNT
    from Sources.modular_recipes.catalog import STEP_COUNT
    from Sources.modular_recipes.catalog import all_specs
    from Sources.modular_recipes.catalog import get_recipe_factory
    from Sources.modular_recipes.catalog import get_recipe_module
    from Sources.modular_recipes.catalog import recipe_route_points

    specs = all_specs()
    assert RECIPE_COUNT == len(specs)
    assert STEP_COUNT == RAW_STEP_COUNT
    assert EXPANDED_STEP_COUNT == SOURCE_STEP_COUNT
    assert SOURCE_STEP_COUNT == sum(int(spec.source_steps) for spec in specs)
    assert RAW_STEP_COUNT == sum(int(spec.raw_steps) for spec in specs)
    _assert_wrapper_helpers_compile()
    _assert_no_generated_sequence_literals()
    _assert_no_removed_recipe_helpers()
    _assert_no_per_recipe_route_point_constants()
    _assert_no_generated_metadata_constants()
    _assert_no_zero_duration_waits()

    recipes = 0
    source_steps = 0
    grouped_modules = set()
    route_point_recipes = 0
    for spec in specs:
        module = get_recipe_module(spec)
        factory = get_recipe_factory(spec)
        assert callable(factory), spec
        assert hasattr(module, spec.factory), spec
        assert not hasattr(module, "STEPS"), spec.module
        assert not hasattr(module, "STEP_META"), spec.module
        assert not hasattr(module, "planner_steps"), spec.module
        assert factory().__class__.__name__ == "BehaviorTree"
        recipes += 1
        source_steps += int(spec.source_steps)
        grouped_modules.add(spec.module)
        if recipe_route_points(spec):
            route_point_recipes += 1

    assert recipes == RECIPE_COUNT
    assert source_steps == EXPANDED_STEP_COUNT
    assert grouped_modules == set(RECIPE_MODULES)
    assert route_point_recipes >= 150
    print(
        "python_recipe_compile_shape: "
        f"compiled {recipes} recipe function(s) across {len(grouped_modules)} module(s), "
        f"verified {source_steps} internal action(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
