"""Missions Prophecies Southern Shiverpeaks BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def ice_caves_of_sorrow() -> BehaviorTree:
    return BT.Sequence(
        name='Ice Caves of Sorrow',
        children=[
            BT.Travel(target_map_id=22, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.EnterChallenge(target_map_id=22, delay_ms=6000),
            BT.MoveAndKill(
                pos=[(-11206, -8611), (-8752, -4005), (-12297, -2421), (-11471, 1089)],
                pause_on_combat=True,
            ),
            BT.Interact(kind='gadget', pos=(-11527, 1631)),
            BT.Wait(duration_ms=500),
            BT.MoveAndKill(
                pos=[(-9401, 1142), (-5630, 8011), (-8301, 9318), (-9963, 9414), (-4846, 8791)],
                pause_on_combat=True,
            ),
            BT.DropBundle(),
            BT.Wait(duration_ms=1000),
            BT.MoveAndKill(
                pos=[(-1935, 6265), (1210, 2060), (6206, -2207), (3992, -8299), (672, -8850)],
                pause_on_combat=True,
            ),
            BT.Interact(kind='gadget', pos=(672, -8850)),
            BT.Wait(duration_ms=500),
            BT.DropBundle(),
            BT.Wait(duration_ms=1000),
            BT.Wait(duration_ms=120000),
            BT.MoveAndKill(
                pos=[
                    (12584, -5498),
                    (13482, -3459),
                    (14557, -1083),
                    (16183, 730),
                    (16234, 3963),
                    (16426, 5994),
                    (16027, 7754),
                    (17709, 9102),
                ],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=30000),
            BT.MoveAndKill(
                pos=[(20754, 7642), (22400, 5225), (21841, -180), (22766, -2330), (23120, -5150)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=24, timeout_ms=10000),
        ],
    )


def iron_mines_of_moladune() -> BehaviorTree:
    return BT.Sequence(
        name='Iron Mines of Moladune',
        children=[
            BT.Travel(target_map_id=24, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.EnterChallenge(target_map_id=24, delay_ms=6000),
            BT.MoveAndKill(pos=[(3457, -30117), (5596, -28039)], pause_on_combat=True),
            BT.MoveAndKill(
                pos=[
                    (4582, -27888),
                    (-4109, -21772),
                    (-8715, -18607),
                    (-9044, -6374),
                    (-1560, 5933),
                    (-4658, 11518),
                    (-9052, 24796),
                ],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(-6484, 26674), (-1437, 26395), (168, 20440), (-1194, 19916), (-4743, 25671), (-9232, 26062)],
                pause_on_combat=True,
            ),
            BT.OptionalInteractItemByModel(model_id=2569, point=None, max_dist=5000),
            BT.Wait(duration_ms=1000),
            BT.Dialog(pos=(-9232, 26062), dialog_ids=['0x84']),
            BT.Wait(duration_ms=1000),
            BT.MoveAndKill(
                pos=[(-6826, 26617), (-3135, 31560), (297, 33766), (2346, 30930), (6493, 31897)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=23, timeout_ms=10000),
        ],
    )


def thunderhead_keep() -> BehaviorTree:
    return BT.Sequence(
        name='Thunderhead Keep',
        children=[
            BT.Travel(target_map_id=23, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.EnterChallenge(target_map_id=23, delay_ms=6000),
            BT.Dialog(pos=(-7940, -17877), dialog_ids=['0x84']),
            BT.MoveAndKill(
                pos=[
                    (-5502, -16415),
                    (-4463, -11956),
                    (-6991, -498),
                    (-4130, 2071),
                    (-515, 2644),
                    (-4652, 5066),
                    (-1182, 11111),
                    (-1465, 11940),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', model_id=1613, dialog_ids=['0x84']),
            BT.WaitForMapLoad(map_id=35, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'ice_caves_of_sorrow': (
        (-11206.0, -8611.0),
        (-8752.0, -4005.0),
        (-12297.0, -2421.0),
        (-11471.0, 1089.0),
        (-9401.0, 1142.0),
        (-5630.0, 8011.0),
        (-8301.0, 9318.0),
        (-9963.0, 9414.0),
        (-4846.0, 8791.0),
        (-1935.0, 6265.0),
        (1210.0, 2060.0),
        (6206.0, -2207.0),
        (3992.0, -8299.0),
        (672.0, -8850.0),
        (12584.0, -5498.0),
        (13482.0, -3459.0),
        (14557.0, -1083.0),
        (16183.0, 730.0),
        (16234.0, 3963.0),
        (16426.0, 5994.0),
        (16027.0, 7754.0),
        (17709.0, 9102.0),
        (20754.0, 7642.0),
        (22400.0, 5225.0),
        (21841.0, -180.0),
        (22766.0, -2330.0),
        (23120.0, -5150.0),
    ),
    'iron_mines_of_moladune': (
        (3457.0, -30117.0),
        (5596.0, -28039.0),
        (4582.0, -27888.0),
        (-4109.0, -21772.0),
        (-8715.0, -18607.0),
        (-9044.0, -6374.0),
        (-1560.0, 5933.0),
        (-4658.0, 11518.0),
        (-9052.0, 24796.0),
        (-6484.0, 26674.0),
        (-1437.0, 26395.0),
        (168.0, 20440.0),
        (-1194.0, 19916.0),
        (-4743.0, 25671.0),
        (-9232.0, 26062.0),
        (-6826.0, 26617.0),
        (-3135.0, 31560.0),
        (297.0, 33766.0),
        (2346.0, 30930.0),
        (6493.0, 31897.0),
    ),
    'thunderhead_keep': (
        (-5502.0, -16415.0),
        (-4463.0, -11956.0),
        (-6991.0, -498.0),
        (-4130.0, 2071.0),
        (-515.0, 2644.0),
        (-4652.0, 5066.0),
        (-1182.0, 11111.0),
        (-1465.0, 11940.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'prophecies/ice_caves_of_sorrow',
        'title': 'Ice Caves of Sorrow',
        'factory': 'ice_caves_of_sorrow',
        'source_steps': 15,
        'raw_steps': 15,
    },
    {
        'kind': 'mission',
        'key': 'prophecies/iron_mines_of_moladune',
        'title': 'Iron Mines of Moladune',
        'factory': 'iron_mines_of_moladune',
        'source_steps': 10,
        'raw_steps': 10,
    },
    {
        'kind': 'mission',
        'key': 'prophecies/thunderhead_keep',
        'title': 'Thunderhead Keep',
        'factory': 'thunderhead_keep',
        'source_steps': 7,
        'raw_steps': 7,
    },
)
