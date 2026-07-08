"""Offline target audit smoke check for Python modular recipes."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from Sources.modular_recipes.tools.audit_targets import architecture_failures
    from Sources.modular_recipes.tools.audit_targets import audit_targets
    from Sources.modular_recipes.tools.audit_targets import render_markdown_report
else:
    from .audit_targets import architecture_failures
    from .audit_targets import audit_targets
    from .audit_targets import render_markdown_report


def main() -> int:
    audit = audit_targets()
    report = render_markdown_report(audit)
    assert "# Modular Target Collection Queue" in report
    assert "## Summary" in report
    assert audit.has_failures == bool(architecture_failures(audit))
    print(
        "modular_target_audit: "
        f"{len(audit.display_only_entries)} registry placeholder(s), "
        f"{len(audit.missing_encrypted_uses)} keyed issue(s), "
        f"{len(audit.bare_target_calls)} bare call(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
