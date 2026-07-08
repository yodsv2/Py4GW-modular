"""Audit deterministic target coverage for native modular recipes."""

from __future__ import annotations

import ast
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]
RECIPE_ROOT = REPO_ROOT / 'Sources' / 'modular_recipes'
TARGET_REGISTRY_PATH = REPO_ROOT / 'Py4GWCoreLib' / 'modular' / 'domain' / 'target_registry.py'

TARGET_KINDS = {'npc', 'enemy', 'gadget'}
REGISTRY_NAMES = {
    'npc': 'NPC_TARGETS',
    'enemy': 'ENEMY_TARGETS',
    'gadget': 'GADGET_TARGETS',
}
TARGET_CALLS = {'Interact', 'Dialog', 'MoveToTarget', 'TargetNamedAgent'}


@dataclass(frozen=True)
class RegistryEntry:
    kind: str
    key: str
    display_name: str
    has_encoded_names: bool
    has_model_id: bool
    line: int


@dataclass(frozen=True)
class TargetUse:
    kind: str
    key: str
    display_name: str
    file: str
    line: int
    call: str
    reason: str


@dataclass(frozen=True)
class BareTargetCall:
    kind: str
    file: str
    line: int
    call: str
    has_position: bool


@dataclass(frozen=True)
class TargetAudit:
    registry_entries: tuple[RegistryEntry, ...]
    missing_encrypted_uses: tuple[TargetUse, ...]
    bare_target_calls: tuple[BareTargetCall, ...]

    @property
    def display_only_entries(self) -> tuple[RegistryEntry, ...]:
        return tuple(entry for entry in self.registry_entries if not entry.has_encoded_names and not entry.has_model_id)

    @property
    def has_failures(self) -> bool:
        return bool(self.display_only_entries or self.missing_encrypted_uses or self.bare_target_calls)


def _literal(node: ast.AST | None) -> Any:
    if node is None:
        return None
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def _has_encoded_names(value_node: ast.AST) -> tuple[bool, bool, str]:
    display_name = ''
    has_encoded_names = False
    has_model_id = False
    if isinstance(value_node, ast.Call):
        for keyword in value_node.keywords:
            if keyword.arg == 'display_name':
                display_name = str(_literal(keyword.value) or '')
            elif keyword.arg == 'encoded_names':
                has_encoded_names = bool(_literal(keyword.value))
            elif keyword.arg == 'model_id':
                has_model_id = _literal(keyword.value) is not None
        return has_encoded_names, has_model_id, display_name

    value = _literal(value_node)
    if isinstance(value, tuple) and len(value) >= 2:
        return bool(value[0]), False, str(value[1] or '')
    return False, False, ''


def read_registry_entries(path: Path = TARGET_REGISTRY_PATH) -> dict[str, dict[str, RegistryEntry]]:
    tree = ast.parse(path.read_text(encoding='utf-8'))
    registries: dict[str, dict[str, RegistryEntry]] = {kind: {} for kind in TARGET_KINDS}
    registry_to_kind = {registry_name: kind for kind, registry_name in REGISTRY_NAMES.items()}

    for node in tree.body:
        name: str | None = None
        value: ast.AST | None = None
        line = int(getattr(node, 'lineno', 0) or 0)
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            name = node.target.id
            value = node.value
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id
                    value = node.value
                    break
        kind = registry_to_kind.get(str(name or ''))
        if kind is None or not isinstance(value, ast.Dict):
            continue

        entries: dict[str, RegistryEntry] = {}
        for key_node, value_node in zip(value.keys, value.values):
            key = _literal(key_node)
            if not isinstance(key, str):
                continue
            has_encoded_names, has_model_id, display_name = _has_encoded_names(value_node)
            entries[key] = RegistryEntry(
                kind=kind,
                key=key,
                display_name=display_name,
                has_encoded_names=has_encoded_names,
                has_model_id=has_model_id,
                line=int(getattr(value_node, 'lineno', line) or line),
            )
        registries[kind] = entries
    return registries


def _recipe_module_paths(recipe_root: Path = RECIPE_ROOT) -> list[Path]:
    return sorted(
        path
        for path in recipe_root.rglob('*.py')
        if 'tools' not in path.parts and 'prebuilt' not in path.parts and path.name not in {'__init__.py', 'catalog.py'}
    )


def _bt_call_name(node: ast.AST) -> str | None:
    if not isinstance(node, ast.Call):
        return None
    func = node.func
    if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name) and func.value.id == 'BT':
        return str(func.attr)
    return None


def _keywords(node: ast.Call) -> dict[str, ast.AST]:
    return {keyword.arg: keyword.value for keyword in node.keywords if keyword.arg}


def _agent_kind(keywords: dict[str, ast.AST]) -> str:
    value = _literal(keywords.get('kind')) if 'kind' in keywords else 'npc'
    return str(value or 'npc').strip().lower()


def _has_meaningful_keyword(keywords: dict[str, ast.AST], name: str) -> bool:
    value = _literal(keywords.get(name))
    return value not in (None, '')


def audit_targets(
    *,
    recipe_root: Path = RECIPE_ROOT,
    target_registry_path: Path = TARGET_REGISTRY_PATH,
) -> TargetAudit:
    registries = read_registry_entries(target_registry_path)
    missing_encrypted_uses: list[TargetUse] = []
    bare_target_calls: list[BareTargetCall] = []

    for path in _recipe_module_paths(recipe_root):
        tree = ast.parse(path.read_text(encoding='utf-8'))
        rel_path = path.relative_to(REPO_ROOT).as_posix()
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            call_name = _bt_call_name(node)
            if call_name not in TARGET_CALLS:
                continue
            keywords = _keywords(node)
            kind = _agent_kind(keywords)
            if kind not in TARGET_KINDS:
                continue

            key = _literal(keywords.get('key'))
            has_key = isinstance(key, str) and bool(key.strip())
            has_model_id = _has_meaningful_keyword(keywords, 'model_id')
            has_position = _has_meaningful_keyword(keywords, 'pos')
            line = int(getattr(node, 'lineno', 0) or 0)

            if has_key:
                entry = registries.get(kind, {}).get(str(key))
                if entry is None:
                    missing_encrypted_uses.append(
                        TargetUse(kind, str(key), '', rel_path, line, call_name, 'missing registry key')
                    )
                elif not entry.has_encoded_names and not entry.has_model_id:
                    missing_encrypted_uses.append(
                        TargetUse(
                            kind, str(key), entry.display_name, rel_path, line, call_name, 'missing encrypted names'
                        )
                    )
                continue

            if not has_model_id:
                bare_target_calls.append(BareTargetCall(kind, rel_path, line, call_name, has_position))

    all_entries: list[RegistryEntry] = []
    for kind in sorted(TARGET_KINDS):
        all_entries.extend(registries.get(kind, {}).values())
    return TargetAudit(
        registry_entries=tuple(sorted(all_entries, key=lambda entry: (entry.kind, entry.key))),
        missing_encrypted_uses=tuple(
            sorted(missing_encrypted_uses, key=lambda use: (use.kind, use.key, use.file, use.line))
        ),
        bare_target_calls=tuple(sorted(bare_target_calls, key=lambda call: (call.file, call.line))),
    )


def architecture_failures(audit: TargetAudit) -> list[str]:
    failures: list[str] = []
    display_by_kind: dict[str, list[RegistryEntry]] = defaultdict(list)
    for entry in audit.display_only_entries:
        display_by_kind[entry.kind].append(entry)
    for kind, entries in sorted(display_by_kind.items()):
        failures.append(f'[TARGETS] {kind} registry has {len(entries)} entries without encrypted names.')
    if audit.missing_encrypted_uses:
        failures.append(f'[TARGETS] {len(audit.missing_encrypted_uses)} recipe target use(s) lack encrypted names.')
    if audit.bare_target_calls:
        failures.append(f'[TARGETS] {len(audit.bare_target_calls)} recipe target call(s) rely on nearest fallback.')
    return failures


def render_markdown_report(audit: TargetAudit) -> str:
    lines = [
        '# Modular Target Collection Queue',
        '',
        'This file is generated from the Python recipe source and target registry audit.',
        'Collect encrypted names with the Modular Recorder, then replace display-name or nearest-fallback targeting.',
        '',
        '## Summary',
        '',
        f'- Registry entries without encrypted names: {len(audit.display_only_entries)}',
        f'- Recipe keyed target uses missing encrypted names: {len(audit.missing_encrypted_uses)}',
        f'- Bare nearest-fallback target calls: {len(audit.bare_target_calls)}',
        '',
    ]

    lines.extend(['## Registry Entries Needing Encrypted Names', ''])
    for kind in ('npc', 'enemy', 'gadget'):
        entries = [entry for entry in audit.display_only_entries if entry.kind == kind]
        lines.extend([f'### {kind.title()}', ''])
        if not entries:
            lines.extend(['- Complete', ''])
            continue
        for entry in entries:
            display = f' - {entry.display_name}' if entry.display_name else ''
            lines.append(
                f'- [ ] `{entry.key}`{display} (`Py4GWCoreLib/modular/domain/target_registry.py:{entry.line}`)'
            )
        lines.append('')

    lines.extend(['## Keyed Recipe Uses Blocked By Missing Encrypted Names', ''])
    if not audit.missing_encrypted_uses:
        lines.extend(['- Complete', ''])
    else:
        grouped: dict[tuple[str, str, str, str], list[TargetUse]] = defaultdict(list)
        for use in audit.missing_encrypted_uses:
            grouped[(use.kind, use.key, use.display_name, use.reason)].append(use)
        for (kind, key, display_name, reason), uses in sorted(grouped.items()):
            display = f' - {display_name}' if display_name else ''
            lines.append(f'### `{kind}:{key}`{display} ({reason})')
            lines.append('')
            for use in uses:
                lines.append(f'- [ ] `{use.file}:{use.line}` `{use.call}`')
            lines.append('')

    lines.extend(['## Bare Nearest-Fallback Calls', ''])
    if not audit.bare_target_calls:
        lines.extend(['- Complete', ''])
    else:
        for call in audit.bare_target_calls:
            position = 'with coordinate' if call.has_position else 'without coordinate'
            lines.append(f'- [ ] `{call.file}:{call.line}` `{call.call}` `{call.kind}` {position}')
        lines.append('')

    return '\n'.join(lines).rstrip() + '\n'


def main() -> int:
    audit = audit_targets()
    print(render_markdown_report(audit), end='')
    return 1 if audit.has_failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
