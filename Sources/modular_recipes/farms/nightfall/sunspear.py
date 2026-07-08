"""Farms Nightfall Sunspear BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def yohlon_insects() -> BehaviorTree:
    return BT.Sequence(
        name='Yohlon Insects',
        children=[
            BT.MoveAndExitMap(pos=(4425, 857), target_map_id=380, move_tolerance=300),
            BT.MoveAndKill(pos=(-17221, -12662), pause_on_combat=True),
            BT.Dialog(kind='npc', key='WANDERING_PRIEST', dialog_ids=['0x85']),
            BT.MoveAndKill(
                pos=[(-18394, -9036), (-17207, -17056), (-19523, -14412)], pause_on_combat=True
            ),
            BT.MoveAndExitMap(pos=(-20133, -14568), target_map_id=381, move_tolerance=300),
        ],
    )


def yohlon_insects_setup() -> BehaviorTree:
    return BT.Sequence(
        name='Yohlon Insects Setup',
        children=[
            BT.Travel(target_map_id=381, leave_party=True),
            BT.MoveAndKill(pos=[(-891, 1876), (2387, 362), (3896, 738)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(4425, 857), target_map_id=380, move_tolerance=300),
            BT.MoveAndExitMap(pos=(-20133, -14568), target_map_id=381, move_tolerance=300),
            BT.LoadParty(max_heroes=8),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'yohlon_insects': (
        (4425.0, 857.0),
        (-17221.0, -12662.0),
        (-18394.0, -9036.0),
        (-17207.0, -17056.0),
        (-19523.0, -14412.0),
        (-20133.0, -14568.0),
    ),
    'yohlon_insects_setup': ((-891.0, 1876.0), (2387.0, 362.0), (3896.0, 738.0), (4425.0, 857.0), (-20133.0, -14568.0)),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'farm',
        'key': 'sunspear/yohlon_insects',
        'title': 'Yohlon Insects',
        'factory': 'yohlon_insects',
        'source_steps': 5,
        'raw_steps': 5,
    },
    {
        'kind': 'farm',
        'key': 'sunspear/yohlon_insects_setup',
        'title': 'Yohlon Insects Setup',
        'factory': 'yohlon_insects_setup',
        'source_steps': 5,
        'raw_steps': 5,
    },
)
