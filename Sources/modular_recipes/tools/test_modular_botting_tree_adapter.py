"""Offline BottingTree adapter check for Python modular recipes."""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from Sources.modular_recipes.tools import _stubs
else:
    from . import _stubs


def main() -> int:
    _stubs.install()
    from Sources.modular_recipes.catalog import planner_steps_for_specs
    from Sources.modular_recipes.prebuilt.modular_eotn import build_eotn_campaign_specs
    from Sources.modular_recipes.prebuilt.modular_eotn import create_eotn_campaign_bot

    specs = build_eotn_campaign_specs()
    assert specs
    steps = planner_steps_for_specs(specs[:2])
    assert len(steps) == 2
    assert steps[0][0].startswith("01.")
    assert steps[0][1]().__class__.__name__ == "BehaviorTree"

    bot = create_eotn_campaign_bot()
    assert len(bot.steps) == len(specs)
    assert bot.repeat is False
    loop_bot = create_eotn_campaign_bot(options=type("Options", (), {"start_phase_index": 1, "loop": True})())
    assert len(loop_bot.steps) == len(specs) - 1
    assert loop_bot.repeat is True
    print("modular_botting_tree_adapter: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
