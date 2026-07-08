"""Validate the Python modular recipe hard cutover."""

from __future__ import annotations

import argparse
import ast
import re
from pathlib import Path

if __package__ in (None, ""):
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from Sources.modular_recipes.tools.audit_targets import architecture_failures
    from Sources.modular_recipes.tools.audit_targets import audit_targets
else:
    from .audit_targets import architecture_failures
    from .audit_targets import audit_targets

REPO_ROOT = Path(__file__).resolve().parents[3]
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the Python modular recipe hard cutover.")
    parser.add_argument(
        "--strict-targets",
        action="store_true",
        help="Fail when recipe target audit debt remains instead of reporting it as a collection warning.",
    )
    args = parser.parse_args(argv)

    failures: list[str] = []
    if (REPO_ROOT / "Py4GWCoreLib" / "modular" / "json_bt_compiler.py").exists():
        failures.append("[JSON] Py4GWCoreLib/modular/json_bt_compiler.py should be removed.")
    if (REPO_ROOT / "Sources" / "modular_data").exists():
        failures.append("[JSON] Sources/modular_data should be removed after recipe conversion.")
    if (REPO_ROOT / "Sources" / "modular_recipes" / "_runtime.py").exists():
        failures.append("[RECIPES] Sources/modular_recipes/_runtime.py should not exist in the native recipe model.")

    tester = REPO_ROOT / "Widgets" / "Automation" / "modular" / "Modular Tester.py"
    if tester.exists():
        text = tester.read_text(encoding="utf-8")
        for forbidden in (
            "load_recipe",
            "compile_recipe_steps_to_named_planner_steps",
            "modular_data_root",
            "RecipeStepMetadata",
            "planner_steps(",
            "STEPS",
            "STEP_META",
        ):
            if forbidden in text:
                failures.append(f"[WIDGET] Modular Tester still references {forbidden}.")

    coder = REPO_ROOT / "Widgets" / "Automation" / "modular" / "Modular Coder.py"
    if coder.exists():
        failures.append("[WIDGET] Modular Coder JSON recorder should be removed.")

    recorder = REPO_ROOT / "Widgets" / "Automation" / "modular" / "Modular Recorder.py"
    if not recorder.exists():
        failures.append("[WIDGET] Modular Recorder.py should exist for native Python recipe capture.")

    recipe_root = REPO_ROOT / "Sources" / "modular_recipes"
    for path in recipe_root.rglob("*.py"):
        if "tools" in path.parts or path.name in {"catalog.py", "__init__.py"}:
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in ("STEPS", "STEP_META", "planner_steps("):
            if forbidden in text:
                failures.append(f"[RECIPES] {path.relative_to(REPO_ROOT)} still exposes {forbidden}.")
        for forbidden in ("SOURCE_STEP_COUNTS", "TITLES", "route_points("):
            if forbidden in text:
                failures.append(
                    f"[RECIPES] {path.relative_to(REPO_ROOT)} still exposes generated metadata {forbidden}."
                )
        if re.search(r"def\s+build\s*\(", text):
            failures.append(f"[RECIPES] {path.relative_to(REPO_ROOT)} still uses generic build().")
        try:
            tree = ast.parse(text)
        except SyntaxError as exc:
            failures.append(f"[RECIPES] {path.relative_to(REPO_ROOT)} has invalid syntax: {exc}.")
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                assigned_name = node.target.id
                if (
                    assigned_name.endswith("_TITLE")
                    or assigned_name.endswith("_REQUIRED_HERO")
                    or assigned_name.endswith("_SOURCE_STEP_COUNT")
                ):
                    failures.append(
                        f"[RECIPES] {path.relative_to(REPO_ROOT)}:{node.lineno} still exposes generated metadata "
                        f"{assigned_name}."
                    )
                    continue
                if assigned_name.endswith("_ROUTE_POINTS") and assigned_name != "ROUTE_POINTS_BY_RECIPE":
                    failures.append(
                        f"[RECIPES] {path.relative_to(REPO_ROOT)}:{node.lineno} still exposes generated route point "
                        f"constant {assigned_name}."
                    )
                    continue
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                assigned_name = node.targets[0].id
                if (
                    assigned_name.endswith("_TITLE")
                    or assigned_name.endswith("_REQUIRED_HERO")
                    or assigned_name.endswith("_SOURCE_STEP_COUNT")
                ):
                    failures.append(
                        f"[RECIPES] {path.relative_to(REPO_ROOT)}:{node.lineno} still exposes generated metadata "
                        f"{assigned_name}."
                    )
                    continue
                if assigned_name.endswith("_ROUTE_POINTS") and assigned_name != "ROUTE_POINTS_BY_RECIPE":
                    failures.append(
                        f"[RECIPES] {path.relative_to(REPO_ROOT)}:{node.lineno} still exposes generated route point "
                        f"constant {assigned_name}."
                    )
                    continue
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name)
                and node.func.value.id == "BT"
            ):
                if node.func.attr in FORBIDDEN_RECIPE_HELPERS:
                    failures.append(
                        f"[RECIPES] {path.relative_to(REPO_ROOT)}:{node.lineno} still calls removed helper "
                        f"BT.{node.func.attr}."
                    )
                    continue
                if node.func.attr == "Wait":
                    values = list(node.args)
                    values.extend(keyword.value for keyword in node.keywords if keyword.arg == "duration_ms")
                    for value_node in values:
                        try:
                            wait_ms = ast.literal_eval(value_node)
                        except Exception:
                            continue
                        if wait_ms == 0:
                            failures.append(
                                f"[RECIPES] {path.relative_to(REPO_ROOT)}:{node.lineno} still has a zero-duration wait."
                            )
                            break
                if node.func.attr != "Sequence":
                    continue
                for keyword in node.keywords:
                    if keyword.arg != "name":
                        continue
                    try:
                        sequence_name = ast.literal_eval(keyword.value)
                    except Exception:
                        continue
                    if sequence_name in FORBIDDEN_GENERATED_SEQUENCE_NAMES:
                        failures.append(
                            f"[RECIPES] {path.relative_to(REPO_ROOT)}:{node.lineno} still uses generated sequence "
                            f"{sequence_name!r}."
                        )

    target_failures = architecture_failures(audit_targets())
    if args.strict_targets:
        failures.extend(target_failures)

    if failures:
        for failure in failures:
            print(failure)
        return 1
    for failure in target_failures:
        print(f"[TARGET AUDIT] {failure}")
    if target_failures:
        print(
            "PASS: Python modular recipe architecture validation passed; "
            "target collection warnings remain. Run with --strict-targets to fail on them."
        )
        return 0
    print("PASS: Python modular recipe architecture validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
