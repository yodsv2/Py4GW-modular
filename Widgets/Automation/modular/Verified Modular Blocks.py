"""Track manual verification coverage for native modular recipes."""

from __future__ import annotations

import ast
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import PyImGui

from Py4GWCoreLib import Console
from Py4GWCoreLib import ConsoleLog
from Sources.modular_recipes.catalog import RecipeSpec
from Sources.modular_recipes.catalog import all_specs
from Sources.modular_recipes.tools.audit_targets import audit_targets
from Widgets.Automation.modular.widget_guard import guarded_widget_main

MODULE_NAME = "Verified Modular Blocks"
MODULE_ICON = "Textures/Module_Icons/Route Planner.png"
MODULE_TAGS = ["Automation", "modular_bot", "testing"]

REPO_ROOT = Path(__file__).resolve().parents[3]
STATE_PATH = Path(__file__).with_suffix(".state.json")
TARGET_REGISTRY_PATH = REPO_ROOT / "Py4GWCoreLib" / "modular" / "domain" / "target_registry.py"

ACCENT = (0.30, 0.78, 0.86, 1.0)
GOOD = (0.42, 0.88, 0.55, 1.0)
WARN = (1.00, 0.78, 0.32, 1.0)
BAD = (1.00, 0.38, 0.38, 1.0)
MUTED = (0.62, 0.66, 0.70, 1.0)
TEXT = (0.92, 0.94, 0.96, 1.0)


@dataclass(frozen=True)
class Issue:
    kind: str
    line: int
    call: str
    agent_kind: str
    detail: str
    note: str


@dataclass(frozen=True)
class RecipeRecord:
    recipe_id: str
    title: str
    spec: RecipeSpec
    issues: tuple[Issue, ...]


_records: list[RecipeRecord] = []
_records_by_id: dict[str, RecipeRecord] = {}
_state: dict[str, dict[str, Any]] = {}
_selected_id = ""
_filter_text = ""
_kind_filter = "all"
_status_filter = "open"
_loaded = False
_last_status = ""


def _recipe_id(spec: RecipeSpec) -> str:
    return f"{spec.kind}/{spec.key}"


def _safe_id(value: str) -> str:
    return value.replace("/", "_").replace(" ", "_").replace(":", "_")


def _default_entry() -> dict[str, Any]:
    return {"tested": False, "notes": ""}


def _entry(recipe_id: str) -> dict[str, Any]:
    value = _state.get(recipe_id)
    if not isinstance(value, dict):
        value = _default_entry()
        _state[recipe_id] = value
    value.setdefault("tested", False)
    value.setdefault("notes", "")
    return value


def _load_state() -> None:
    global _state, _last_status
    if not STATE_PATH.exists():
        _state = {}
        return
    try:
        raw = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        _state = {}
        _last_status = f"State load failed: {exc}"
        return
    recipes = raw.get("recipes", {}) if isinstance(raw, dict) else {}
    _state = recipes if isinstance(recipes, dict) else {}


def _save_state() -> None:
    global _last_status
    try:
        payload = {
            "version": 1,
            "recipes": _state,
        }
        STATE_PATH.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        _last_status = f"Saved {STATE_PATH.name}"
    except Exception as exc:
        _last_status = f"Save failed: {exc}"
        ConsoleLog(MODULE_NAME, _last_status, Console.MessageType.Error)


def _literal(node: ast.AST) -> Any:
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def _bt_call_name(node: ast.AST) -> str | None:
    if not isinstance(node, ast.Call):
        return None
    func = node.func
    if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name) and func.value.id == "BT":
        return str(func.attr)
    return None


def _keyword_map(node: ast.Call) -> dict[str, ast.AST]:
    return {keyword.arg: keyword.value for keyword in node.keywords if keyword.arg}


def _agent_kind(keywords: dict[str, ast.AST]) -> str:
    value = _literal(keywords["kind"]) if "kind" in keywords else "npc"
    return str(value or "npc").strip().lower()


def _has_meaningful_keyword(keywords: dict[str, ast.AST], name: str) -> bool:
    if name not in keywords:
        return False
    value = _literal(keywords[name])
    return value not in (None, "")


def _function_parents(tree: ast.AST) -> dict[ast.AST, ast.FunctionDef]:
    parents: dict[ast.AST, ast.AST] = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parents[child] = node

    result: dict[ast.AST, ast.FunctionDef] = {}
    for node in ast.walk(tree):
        current = node
        while current in parents:
            current = parents[current]
            if isinstance(current, ast.FunctionDef):
                result[node] = current
                break
    return result


def _registry_assignments() -> dict[str, dict[str, tuple[bool, bool]]]:
    registries: dict[str, dict[str, tuple[bool, bool]]] = {}
    if not TARGET_REGISTRY_PATH.exists():
        return registries

    tree = ast.parse(TARGET_REGISTRY_PATH.read_text(encoding="utf-8"))

    def _read_registry(name: str, value: ast.AST) -> None:
        if name not in {"NPC_TARGETS", "GADGET_TARGETS", "ENEMY_TARGETS"}:
            return
        entries: dict[str, tuple[bool, bool]] = {}
        if not isinstance(value, ast.Dict):
            registries[name] = entries
            return
        for key_node, value_node in zip(value.keys, value.values):
            key = _literal(key_node) if key_node is not None else None
            if not isinstance(key, str):
                continue
            has_encoded = False
            has_model = False
            if isinstance(value_node, ast.Tuple):
                raw_value = _literal(value_node)
                if isinstance(raw_value, tuple) and raw_value:
                    has_encoded = bool(raw_value[0])
            elif isinstance(value_node, ast.Call):
                for keyword in value_node.keywords:
                    if keyword.arg == "encoded_names":
                        has_encoded = bool(_literal(keyword.value))
                    if keyword.arg == "model_id":
                        has_model = True
            entries[key] = (has_encoded, has_model)
        registries[name] = entries

    for node in tree.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            _read_registry(node.target.id, node.value)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    _read_registry(target.id, node.value)
    return registries


def _normalize_key(value: object) -> str:
    return str(value or "").strip().casefold().replace(" ", "_").replace("-", "_")


def _registry_status(
    registries: dict[str, dict[str, tuple[bool, bool]]],
    agent_kind: str,
    key: str,
) -> tuple[bool, bool] | None:
    registry_name = {"npc": "NPC_TARGETS", "gadget": "GADGET_TARGETS", "enemy": "ENEMY_TARGETS"}.get(agent_kind)
    registry = registries.get(str(registry_name or ""), {})
    if key in registry:
        return registry[key]
    normalized_key = _normalize_key(key)
    for registry_key, value in registry.items():
        if _normalize_key(registry_key) == normalized_key:
            return value
    return None


def _module_path(module_name: str) -> Path:
    return REPO_ROOT / Path(module_name.replace(".", "/") + ".py")


def _audit_records() -> list[RecipeRecord]:
    specs = all_specs()
    specs_by_factory: dict[tuple[str, str], list[RecipeSpec]] = defaultdict(list)
    issues_by_id: dict[str, list[Issue]] = defaultdict(list)

    for spec in specs:
        specs_by_factory[(spec.module, spec.factory)].append(spec)

    module_function_for_line: dict[str, list[tuple[int, int, str]]] = {}
    for module_name in sorted({spec.module for spec in specs}):
        path = _module_path(module_name)
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(text)
        except SyntaxError as exc:
            for spec in specs_by_factory.get((module_name, ""), []):
                issues_by_id[_recipe_id(spec)].append(
                    Issue("syntax", exc.lineno or 0, "module", "", "syntax", str(exc))
                )
            continue
        rel_path = path.relative_to(REPO_ROOT).as_posix()
        function_spans: list[tuple[int, int, str]] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_spans.append(
                    (int(node.lineno), int(getattr(node, "end_lineno", node.lineno) or node.lineno), node.name)
                )
        module_function_for_line[rel_path] = function_spans

    def _recipe_specs_for_location(file: str, line: int) -> list[RecipeSpec]:
        module_name = "Sources." + file.removeprefix("Sources/").removesuffix(".py").replace("/", ".")
        for start, end, function_name in module_function_for_line.get(file, []):
            if start <= line <= end:
                return specs_by_factory.get((module_name, function_name), [])
        return []

    audit = audit_targets()
    for use in audit.missing_encrypted_uses:
        note = (
            "Registry key is missing."
            if use.reason == "missing registry key"
            else "Registry entry lacks encrypted-name data."
        )
        issue_kind = "registry-missing" if use.reason == "missing registry key" else "registry-encoded"
        issue = Issue(
            kind=issue_kind,
            line=use.line,
            call=use.call,
            agent_kind=use.kind,
            detail=use.key,
            note=note,
        )
        for spec in _recipe_specs_for_location(use.file, use.line):
            issues_by_id[_recipe_id(spec)].append(issue)

    for call in audit.bare_target_calls:
        note = "Uses nearest target near a coordinate; replace with encrypted-name key or model_id."
        if not call.has_position:
            note = "Uses nearest target fallback; replace with encrypted-name key or model_id."
        issue = Issue(
            kind="nearest",
            line=call.line,
            call=call.call,
            agent_kind=call.kind,
            detail="missing key/model_id",
            note=note,
        )
        for spec in _recipe_specs_for_location(call.file, call.line):
            issues_by_id[_recipe_id(spec)].append(issue)

    records: list[RecipeRecord] = []
    for spec in specs:
        recipe_id = _recipe_id(spec)
        title = str(spec.title or spec.factory).strip()
        records.append(
            RecipeRecord(
                recipe_id=recipe_id,
                title=title,
                spec=spec,
                issues=tuple(sorted(issues_by_id.get(recipe_id, ()), key=lambda issue: issue.line)),
            )
        )
    return sorted(records, key=lambda record: (record.spec.kind, record.spec.key))


def _ensure_loaded() -> None:
    global _loaded, _records, _records_by_id, _selected_id
    if _loaded:
        return
    _load_state()
    _records = _audit_records()
    _records_by_id = {record.recipe_id: record for record in _records}
    if not _selected_id and _records:
        _selected_id = _records[0].recipe_id
    _loaded = True


def _tested(record: RecipeRecord) -> bool:
    return bool(_entry(record.recipe_id).get("tested", False))


def _notes(record: RecipeRecord) -> str:
    return str(_entry(record.recipe_id).get("notes", "") or "")


def _set_tested(record: RecipeRecord, value: bool) -> None:
    _entry(record.recipe_id)["tested"] = bool(value)
    _save_state()


def _set_notes(record: RecipeRecord, value: str) -> None:
    _entry(record.recipe_id)["notes"] = str(value or "")
    _save_state()


def _visible_records() -> list[RecipeRecord]:
    needle = _filter_text.strip().casefold()
    records = []
    for record in _records:
        if _kind_filter != "all" and record.spec.kind != _kind_filter:
            continue
        if _status_filter == "open" and _tested(record):
            continue
        if _status_filter == "tested" and not _tested(record):
            continue
        if _status_filter == "issues" and not record.issues:
            continue
        if needle:
            haystack = f"{record.recipe_id} {record.title} {record.spec.module} {record.spec.factory}".casefold()
            if needle not in haystack:
                continue
        records.append(record)
    return records


def _status_color(record: RecipeRecord) -> tuple[float, float, float, float]:
    if _tested(record):
        return GOOD
    if record.issues:
        return WARN
    return TEXT


def _issue_summary(record: RecipeRecord) -> str:
    if not record.issues:
        return "clean scan"
    counts: dict[str, int] = defaultdict(int)
    for issue in record.issues:
        counts[issue.kind] += 1
    parts = []
    if counts.get("nearest"):
        parts.append(f"nearest {counts['nearest']}")
    if counts.get("registry-encoded"):
        parts.append(f"missing enc {counts['registry-encoded']}")
    if counts.get("registry-missing"):
        parts.append(f"missing key {counts['registry-missing']}")
    return ", ".join(parts)


def _select_next_issue(delta: int) -> None:
    global _selected_id
    issue_records = [record for record in _records if record.issues]
    if not issue_records:
        return
    current_index = 0
    for index, record in enumerate(issue_records):
        if record.recipe_id == _selected_id:
            current_index = index
            break
    _selected_id = issue_records[(current_index + delta) % len(issue_records)].recipe_id


def _draw_top_bar() -> None:
    global _filter_text, _kind_filter, _status_filter
    total = len(_records)
    tested = sum(1 for record in _records if _tested(record))
    issue_count = sum(1 for record in _records if record.issues)
    PyImGui.text_colored(MODULE_NAME, ACCENT)
    PyImGui.same_line(0, 12)
    PyImGui.text_colored(f"{tested}/{total} tested  |  {issue_count} with notes", MUTED)
    if _last_status:
        PyImGui.same_line(0, 12)
        PyImGui.text_colored(_last_status, MUTED)

    PyImGui.separator()
    new_filter = PyImGui.input_text("Filter##verified_modular_filter", _filter_text, 128)
    if new_filter != _filter_text:
        _filter_text = new_filter

    kinds = ["all", "dungeon", "farm", "mission", "quest", "route"]
    current_kind = kinds.index(_kind_filter) if _kind_filter in kinds else 0
    next_kind = PyImGui.combo("Kind##verified_modular_kind", current_kind, kinds)
    if next_kind != current_kind and 0 <= next_kind < len(kinds):
        _kind_filter = kinds[next_kind]

    statuses = ["open", "all", "tested", "issues"]
    current_status = statuses.index(_status_filter) if _status_filter in statuses else 0
    next_status = PyImGui.combo("View##verified_modular_status", current_status, statuses)
    if next_status != current_status and 0 <= next_status < len(statuses):
        _status_filter = statuses[next_status]

    if PyImGui.button("Previous Issue##verified_modular_prev_issue", 130, 0):
        _select_next_issue(-1)
    PyImGui.same_line(0, 6)
    if PyImGui.button("Next Issue##verified_modular_next_issue", 110, 0):
        _select_next_issue(1)
    PyImGui.same_line(0, 6)
    if PyImGui.button("Reload Scan##verified_modular_reload", 110, 0):
        global _loaded
        _loaded = False
        _ensure_loaded()


def _draw_record_row(record: RecipeRecord) -> None:
    global _selected_id
    row_id = _safe_id(record.recipe_id)
    tested = _tested(record)
    next_tested = PyImGui.checkbox(f"##tested_{row_id}", tested)
    if next_tested != tested:
        _set_tested(record, next_tested)

    PyImGui.same_line(0, 4)
    marker = "[!]" if record.issues else "[ ]"
    label = f"{marker} {record.title}##select_{row_id}"
    if PyImGui.selectable(
        label, record.recipe_id == _selected_id, int(PyImGui.SelectableFlags.SpanAllColumns), [0.0, 0.0]
    ):
        _selected_id = record.recipe_id
    PyImGui.text_colored(f"   {record.recipe_id}  |  {_issue_summary(record)}", _status_color(record))


def _draw_record_list() -> None:
    visible = _visible_records()
    PyImGui.text_colored(f"Recipes ({len(visible)})", MUTED)
    if PyImGui.begin_child("##verified_modular_recipe_list", (0, 0), True, PyImGui.WindowFlags.HorizontalScrollbar):
        for record in visible:
            _draw_record_row(record)
    PyImGui.end_child()


def _draw_issue(issue: Issue) -> None:
    color = BAD if issue.kind == "nearest" else WARN
    PyImGui.text_colored(f"{issue.line}: {issue.call} {issue.agent_kind} {issue.detail}", color)
    PyImGui.text_wrapped(f"  {issue.note}")


def _issue_share_text(record: RecipeRecord) -> str:
    lines = [
        "Verified Modular Blocks issue report",
        f"Recipe: {record.recipe_id}",
        f"Title: {record.title}",
        f"Factory: {record.spec.module}:{record.spec.factory}",
        f"Target registry: {TARGET_REGISTRY_PATH.relative_to(REPO_ROOT).as_posix()}",
        "",
        f"Watch list ({len(record.issues)}):",
    ]
    if not record.issues:
        lines.append("- <no nearest-fallback or missing encrypted-name issues found>")
    for issue in record.issues:
        lines.append(
            f"- line {issue.line}: {issue.call} kind={issue.agent_kind} detail={issue.detail} "
            f"issue={issue.kind}; {issue.note}"
        )
    notes = _notes(record).strip()
    if notes:
        lines.extend(["", "Tester notes:", notes])
    return "\n".join(lines).rstrip() + "\n"


def _copy_issue_share_text(record: RecipeRecord) -> None:
    global _last_status
    PyImGui.set_clipboard_text(_issue_share_text(record))
    _last_status = f"Copied issue data for {record.recipe_id}"


def _draw_detail() -> None:
    selected = _records_by_id.get(_selected_id)
    if selected is None:
        PyImGui.text_colored("Select a recipe.", MUTED)
        return

    row_id = _safe_id(selected.recipe_id)
    PyImGui.text_colored(selected.title, ACCENT)
    PyImGui.text_colored(selected.recipe_id, MUTED)
    PyImGui.separator()

    tested = _tested(selected)
    next_tested = PyImGui.checkbox(f"Tested##detail_tested_{row_id}", tested)
    if next_tested != tested:
        _set_tested(selected, next_tested)
    PyImGui.same_line(0, 8)
    if PyImGui.button(f"Copy Issue Data##detail_copy_{row_id}", 130, 0):
        _copy_issue_share_text(selected)

    notes = _notes(selected)
    next_notes = PyImGui.input_text(f"Notes##detail_notes_{row_id}", notes, 512)
    if next_notes != notes:
        _set_notes(selected, next_notes)

    PyImGui.spacing()
    PyImGui.text_colored("Recipe", MUTED)
    PyImGui.text(f"Module: {selected.spec.module}")
    PyImGui.text(f"Function: {selected.spec.factory}")
    PyImGui.text(f"Source actions: {selected.spec.source_steps}")
    PyImGui.text(f"Raw legacy actions: {selected.spec.raw_steps}")

    PyImGui.spacing()
    PyImGui.text_colored(f"Watch List ({len(selected.issues)})", WARN if selected.issues else GOOD)
    if not selected.issues:
        PyImGui.text_colored("No nearest-fallback or missing encrypted-name issues found.", GOOD)
        return
    if PyImGui.begin_child("##verified_modular_issue_detail", (0, 0), True, PyImGui.WindowFlags.HorizontalScrollbar):
        for issue in selected.issues:
            _draw_issue(issue)
            PyImGui.separator()
    PyImGui.end_child()


def _draw_main() -> None:
    _ensure_loaded()
    _draw_top_bar()
    PyImGui.separator()
    if PyImGui.begin_table("##verified_modular_layout", 2, PyImGui.TableFlags.SizingStretchProp):
        PyImGui.table_next_row()
        PyImGui.table_set_column_index(0)
        _draw_record_list()
        PyImGui.table_set_column_index(1)
        _draw_detail()
        PyImGui.end_table()


def _main_impl() -> None:
    PyImGui.set_next_window_size((960, 640), PyImGui.ImGuiCond.FirstUseEver)
    PyImGui.set_next_window_bg_alpha(1.0)
    if not PyImGui.begin(MODULE_NAME):
        PyImGui.end()
        return
    _draw_main()
    PyImGui.end()


def main() -> None:
    guarded_widget_main(MODULE_NAME, _main_impl)


def configure() -> None:
    _ensure_loaded()
    PyImGui.text_colored("State File", ACCENT)
    PyImGui.text(str(STATE_PATH))
    if PyImGui.button("Reload Verification State##verified_modular_reload_state"):
        _load_state()


def tooltip() -> None:
    PyImGui.begin_tooltip()
    PyImGui.text(MODULE_NAME)
    PyImGui.separator()
    PyImGui.text_wrapped("Track which native modular recipes have been manually tested.")
    PyImGui.text_wrapped("Recipes with targeting issues are annotated from the current Python source scan.")
    PyImGui.end_tooltip()


if __name__ == "__main__":
    main()
