"""Offline check for coordinate-aware modular named target selection."""

from __future__ import annotations

import sys
import types
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from Sources.modular_recipes.tools import _stubs
else:
    from . import _stubs


def _distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    return ((float(a[0]) - float(b[0])) ** 2 + (float(a[1]) - float(b[1])) ** 2) ** 0.5


def main() -> int:
    _stubs.install()

    from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
    from Py4GWCoreLib.modular.domain import target_registry
    from Sources.ApoSource.ApoBottingLib import wrappers as BT

    target_registry.NPC_TARGETS["DUPLICATE_TEST_TARGET"] = (((9, 9, 9),), "Duplicate Test Target")

    positions = {
        101: (0.0, 0.0),
        202: (120.0, 120.0),
        303: (125.0, 125.0),
    }
    enc_names = {
        101: (9, 9, 9),
        202: (9, 9, 9),
        303: (8, 8, 8),
    }
    selected: list[int] = []

    py4gwcorelib = sys.modules["Py4GWCoreLib"]
    py4gwcorelib.Agent = types.SimpleNamespace(
        IsValid=lambda agent_id: int(agent_id) in positions,
        GetXY=lambda agent_id: positions[int(agent_id)],
    )
    py4gwcorelib.AgentArray = types.SimpleNamespace(
        GetNPCMinipetArray=lambda: list(positions),
        GetEnemyArray=lambda: [],
        GetGadgetArray=lambda: [],
        GetItemArray=lambda: [],
        Filter=types.SimpleNamespace(
            ByDistance=lambda agents, pos, distance: [
                agent_id for agent_id in agents if _distance(positions[int(agent_id)], pos) <= float(distance)
            ]
        ),
        Sort=types.SimpleNamespace(
            ByDistance=lambda agents, pos: sorted(agents, key=lambda agent_id: _distance(positions[int(agent_id)], pos))
        ),
    )
    py4gwcorelib.Player = types.SimpleNamespace(
        GetXY=lambda: (0.0, 0.0),
        ChangeTarget=lambda agent_id: selected.append(int(agent_id)),
    )

    pyagent = types.ModuleType("PyAgent")
    pyagent.PyAgent = types.SimpleNamespace(GetAgentEncName=lambda agent_id: enc_names.get(int(agent_id), ()))
    sys.modules["PyAgent"] = pyagent

    by_player = BT.TargetNamedAgent(kind="npc", key="DUPLICATE_TEST_TARGET", max_dist=1000)
    assert by_player.root.action_fn(by_player.root) == BehaviorTree.NodeState.SUCCESS
    assert selected[-1] == 101

    by_recorded_pos = BT.TargetNamedAgent(kind="npc", key="DUPLICATE_TEST_TARGET", max_dist=1000, pos=(130, 130))
    assert by_recorded_pos.root.action_fn(by_recorded_pos.root) == BehaviorTree.NodeState.SUCCESS
    assert selected[-1] == 202

    print("modular_named_target_position_selection: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
