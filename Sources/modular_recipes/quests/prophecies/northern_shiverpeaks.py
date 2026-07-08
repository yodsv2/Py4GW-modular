"""Quests Prophecies Northern Shiverpeaks BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def the_way_is_blocked() -> BehaviorTree:
    return BT.Sequence(
        name='The Way is blocked',
        children=[
            BT.Travel(target_map_id=134, leave_party=True),
            BT.Interact(kind='npc', pos=(9086, 5816)),
            BT.Wait(duration_ms=500),
            BT.Dialog(pos=(9086, 5816), dialog_ids=['0x80C603', '0x80C601'], interval_ms=500),
            BT.Wait(duration_ms=500),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(9200, 4000), target_map_id=99, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (7508, -1496),
                    (3061, -4286),
                    (2134, -9007),
                    (135, -11701),
                    (-1453, -12890),
                    (-5887, -12414),
                    (-8536, -9960),
                    (-10752, -8461),
                ],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(-11100, -8500), target_map_id=25, move_tolerance=300),
            BT.MoveAndKill(pos=(24274, -2211), pause_on_combat=True),
            BT.Dialog(pos=(23672, -2776), dialog_ids=['0x80C607']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'the_way_is_blocked': (
        (9200.0, 4000.0),
        (7508.0, -1496.0),
        (3061.0, -4286.0),
        (2134.0, -9007.0),
        (135.0, -11701.0),
        (-1453.0, -12890.0),
        (-5887.0, -12414.0),
        (-8536.0, -9960.0),
        (-10752.0, -8461.0),
        (-11100.0, -8500.0),
        (24274.0, -2211.0),
    )
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'prophecies/the_way_is_blocked',
        'title': 'The Way is blocked',
        'factory': 'the_way_is_blocked',
        'source_steps': 9,
        'raw_steps': 9,
    },
)
