"""Nightfall transit BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def ferry_kamadan_docks() -> BehaviorTree:
    return BT.Sequence(
        name='Ferry Kamadan Docks',
        children=[
            BT.Travel(target_map_id=449),
            BT.Move(pos=[(-7048, 16587)]),
            BT.MoveAndExitMap(pos=(-5962, 16729), target_map_id=429, move_tolerance=300),
            BT.Dialog(kind='npc', key='ASSISTANT_HAHNNA', dialog_ids=['0x85'], pos=(-4559, 16717)),
            BT.WaitForMapLoad(map_id=493, timeout_ms=10000),
        ],
    )


def ferry_docks_la() -> BehaviorTree:
    return BT.Sequence(
        name='Ferry Docks LA',
        children=[
            BT.Travel(target_map_id=493, leave_party=True),
            BT.Dialog(kind='npc', key='DINJA', pos=(-2428, 16752), dialog_ids=['0x830E03', '0x830E01']),
            BT.Dialog(kind='npc', key='MHENLO', pos=(-2540, 16210), dialog_ids=['0x89']),
            BT.WaitForMapLoad(map_id=415, timeout_ms=10000),
            BT.MoveAndKill(pos=(-1197, 983), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LIONGUARD_NEIRO', dialog_ids=['0x85']),
            BT.Dialog(kind='npc', key='LIONGUARD_NEIRO', dialog_ids=['0x85']),
            BT.MoveAndKill(pos=(-1961, 1460), pause_on_combat=True),
            BT.NudgeMove(pos=(-2000, 1500), pulses=2, pulse_ms=180),
            BT.WaitForMapLoad(map_id=55, timeout_ms=10000),
        ],
    )

ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'ferry_kamadan_docks': ((-7048.0, 16587.0),),
    'ferry_docks_la': (
        (-2428.0, 16752.0),
        (-2540.0, 16210.0),
        (-1197.0, 983.0),
        (-1961.0, 1460.0),
        (-2000.0, 1500.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'route',
        'key': 'nightfall/ferry_kamadan_docks',
        'title': 'Ferry Kamadan Docks',
        'factory': 'ferry_kamadan_docks',
        'source_steps': 5,
        'raw_steps': 5,
    },
    {
        'kind': 'route',
        'key': 'nightfall/ferry_docks_la',
        'title': 'Ferry Docks LA',
        'factory': 'ferry_docks_la',
        'source_steps': 10,
        'raw_steps': 10,
    },
)
