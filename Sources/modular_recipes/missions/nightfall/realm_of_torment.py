"""Missions Nightfall Realm Of Torment BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def abbadons_gate() -> BehaviorTree:
    return BT.Sequence(
        name="Abaddon's Gate",
        children=[
            BT.Travel(target_map_id=496, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(15403, -3885), pause_on_combat=True),
            BT.Dialog(kind='npc', key='KEEPER_SHARISSH', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=7600),
            BT.WaitForMapLoad(map_id=496, timeout_ms=10000),
            BT.WaitUntilOnExplorable(timeout_ms=30000),
            BT.MoveAndKill(
                pos=[(-138, 4798), (-388, 3011), (-1493, 3553)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-138, 4798), (-388, 3011), (-1493, 3553)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-138, 4798), (-388, 3011), (-1493, 3553)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-138, 4798), (-388, 3011), (-1493, 3553)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-138, 4798), (-388, 3011), (-1493, 3553)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-138, 4798), (-388, 3011), (-1493, 3553)], pause_on_combat=True
            ),
            BT.WaitForMapLoad(map_id=503, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-8239, 5458), (-7954, 7502), (-8409, 9688), (-9796, 12722)],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='ACOLYTE_SOUSUKE', dialog_ids=['0x82DE01']),
            BT.Dialog(kind='npc', key='MARGRID_THE_SLY', dialog_ids=['0x82DB01']),
            BT.Dialog(kind='npc', key='ACOLYTE_JIN', dialog_ids=['0x82DD01']),
            BT.MoveAndKill(pos=(-12713, 12334), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NORGU', dialog_ids=['0x82D901']),
            BT.Dialog(kind='npc', key='GOREN', dialog_ids=['0x82DA01']),
            BT.MoveAndKill(pos=[(-15665, 10064), (-17207, 5884)], pause_on_combat=True),
            BT.Interact(kind='npc', key='KEEPER_OF_SECRETS'),
            BT.Dialog(kind='npc', key='VOLATISS', dialog_ids=['0x84', '0x85']),
            BT.MoveAndExitMap(pos=(-18593, 6156), target_map_id=370, move_tolerance=300),
        ],
    )


def gate_of_madness() -> BehaviorTree:
    return BT.Sequence(
        name='Gate of Madness',
        children=[
            BT.Travel(target_map_id=495, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-11265, -9912), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RUNIC_ORACLE', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=10000),
            BT.WaitForMapLoad(map_id=495, timeout_ms=10000),
            BT.WaitUntilOnExplorable(timeout_ms=30000),
            BT.MoveAndKill(
                pos=[(5149, 14955), (9919, 7402), (10562, -1123)], pause_on_combat=True
            ),
            BT.MoveAndKill(pos=[(13301, -761), (13292, 342)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(17699, -2046), (17176, -4602)], pause_on_combat=True),
            BT.Wait(duration_ms=22000),
            BT.MoveAndKill(
                pos=[(12692, -5092), (13314, -8726), (12309, -5112), (8256, -4721), (8327, -8077), (8643, -11623)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=[(8910, -8122), (7738, -10554)], pause_on_combat=True),
            BT.MoveAndKill(pos=(5255, -10677), pause_on_combat=True),
            BT.FlagAllHeroes(4476, -7780),
            BT.MoveAndKill(pos=(15837, -6917), pause_on_combat=True),
            BT.FlagAllHeroes(4476, -7780),
            BT.Wait(duration_ms=60000),
            BT.FlagAllHeroes(1885, -6792),
            BT.Wait(duration_ms=60000),
            BT.FlagAllHeroes(-1888, -12953),
            BT.Wait(duration_ms=60000),
            BT.FlagAllHeroes(1576, -14819),
            BT.Wait(duration_ms=60000),
            BT.FlagAllHeroes(4222, -13762),
            BT.Wait(duration_ms=60000),
            BT.FlagAllHeroes(6871, -10371),
            BT.Wait(duration_ms=20000),
            BT.MoveAndKill(pos=(6871, -10371), pause_on_combat=True),
            BT.UnflagAllHeroes(),
            BT.MoveAndKill(pos=(1634, -11180), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=496, timeout_ms=10000),
        ],
    )


def gate_of_pain() -> BehaviorTree:
    return BT.Sequence(
        name='Gate of Pain',
        children=[
            BT.Travel(target_map_id=494, leave_party=True),
            BT.MoveAndKill(pos=[(-14599, 3887), (-15068, 3333)], pause_on_combat=True),
            BT.LoadParty(max_heroes=8, required_hero=['Dunkoro']),
            BT.Dialog(kind='npc', key='JARINDOK', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=9200),
            BT.WaitForMapLoad(map_id=494, timeout_ms=10000),
            BT.WaitUntilOnExplorable(timeout_ms=30000),
            BT.MoveAndKill(
                pos=[(26156, -7688), (23130, -9431), (18595, -10875), (15266, -12130), (10988, -11961), (7709, -9382)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=(8435, -3406), pause_on_combat=True),
            BT.MoveAndKill(pos=(8058, -355), pause_on_combat=True),
            BT.MoveAndKill(pos=(3696, -3782), pause_on_combat=True),
            BT.MoveAndKill(pos=(1095, -6310), pause_on_combat=True),
            BT.MoveAndKill(pos=(3156, -9160), pause_on_combat=True),
            BT.MoveAndKill(pos=[(1528, -5447), (7867, 753), (89, 476)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(7867, 753), (4902, 5615), (7310, 7092)], pause_on_combat=True),
            BT.MoveAndKill(pos=(1858, 5150), pause_on_combat=True),
            BT.MoveAndKill(pos=(-1917, 7772), pause_on_combat=True),
            BT.MoveAndKill(pos=(-2198, 4307), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=469, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'abbadons_gate': (
        (15403.0, -3885.0),
        (-138.0, 4798.0),
        (-388.0, 3011.0),
        (-1493.0, 3553.0),
        (-138.0, 4798.0),
        (-388.0, 3011.0),
        (-1493.0, 3553.0),
        (-138.0, 4798.0),
        (-388.0, 3011.0),
        (-1493.0, 3553.0),
        (-138.0, 4798.0),
        (-388.0, 3011.0),
        (-1493.0, 3553.0),
        (-138.0, 4798.0),
        (-388.0, 3011.0),
        (-1493.0, 3553.0),
        (-138.0, 4798.0),
        (-388.0, 3011.0),
        (-1493.0, 3553.0),
        (-8239.0, 5458.0),
        (-7954.0, 7502.0),
        (-8409.0, 9688.0),
        (-9796.0, 12722.0),
        (-12713.0, 12334.0),
        (-15665.0, 10064.0),
        (-17207.0, 5884.0),
        (-18593.0, 6156.0),
    ),
    'gate_of_madness': (
        (-11265.0, -9912.0),
        (5149.0, 14955.0),
        (9919.0, 7402.0),
        (10562.0, -1123.0),
        (13301.0, -761.0),
        (13292.0, 342.0),
        (17699.0, -2046.0),
        (17176.0, -4602.0),
        (12692.0, -5092.0),
        (13314.0, -8726.0),
        (12309.0, -5112.0),
        (8256.0, -4721.0),
        (8327.0, -8077.0),
        (8643.0, -11623.0),
        (8910.0, -8122.0),
        (7738.0, -10554.0),
        (5255.0, -10677.0),
        (15837.0, -6917.0),
        (6871.0, -10371.0),
        (1634.0, -11180.0),
    ),
    'gate_of_pain': (
        (-14599.0, 3887.0),
        (-15068.0, 3333.0),
        (26156.0, -7688.0),
        (23130.0, -9431.0),
        (18595.0, -10875.0),
        (15266.0, -12130.0),
        (10988.0, -11961.0),
        (7709.0, -9382.0),
        (8435.0, -3406.0),
        (8058.0, -355.0),
        (3696.0, -3782.0),
        (1095.0, -6310.0),
        (3156.0, -9160.0),
        (1528.0, -5447.0),
        (7867.0, 753.0),
        (89.0, 476.0),
        (7867.0, 753.0),
        (4902.0, 5615.0),
        (7310.0, 7092.0),
        (1858.0, 5150.0),
        (-1917.0, 7772.0),
        (-2198.0, 4307.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'nightfall/abbadons_gate',
        'title': "Abaddon's Gate",
        'factory': 'abbadons_gate',
        'source_steps': 25,
        'raw_steps': 25,
    },
    {
        'kind': 'mission',
        'key': 'nightfall/gate_of_madness',
        'title': 'Gate of Madness',
        'factory': 'gate_of_madness',
        'source_steps': 32,
        'raw_steps': 32,
    },
    {
        'kind': 'mission',
        'key': 'nightfall/gate_of_pain',
        'title': 'Gate of Pain',
        'factory': 'gate_of_pain',
        'source_steps': 19,
        'raw_steps': 19,
    },
)
