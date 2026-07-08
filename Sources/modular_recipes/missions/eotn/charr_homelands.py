"""Missions Eotn Charr Homelands BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def against_the_charr() -> BehaviorTree:
    return BT.Sequence(
        name='Against the Charr',
        children=[
            BT.MoveAndKill(pos=(-9660, -2967), pause_on_combat=True),
            BT.Dialog(kind='npc', key='VANGUARD_HELMET', dialog_ids=['0x84']),
            BT.WaitForMapLoad(map_id=665, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(12464, -8850), (18008, -2874), (17836, 2958), (19851, 3696)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=649, timeout_ms=10000),
        ],
    )


def assault_on_the_stronghold() -> BehaviorTree:
    return BT.Sequence(
        name='Assault on the Stronghold',
        children=[
            BT.Travel(target_map_id=648, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-15950, 14257), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-15272, 13607), target_map_id=647, move_tolerance=300),
            BT.MoveAndKill(pos=(-13666, 11318), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ROAN_FIERCEHEART', dialog_ids=['0x86', '0x84']),
            BT.WaitForMapLoad(map_id=669, timeout_ms=10000),
            BT.MoveAndKill(pos=[(5530, 11697), (6015, 9124)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='LEFT_SIEGE_DEVOURER', dialog_ids=['0x85']),
            BT.MoveAndKill(pos=(5215, 12149), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RIGHT_SIEGE_DEVOURER', dialog_ids=['0x85']),
            BT.MoveAndKill(pos=[(3821, 11103), (1292, 10679)], pause_on_combat=True),
            BT.Wait(duration_ms=42800),
            BT.MoveAndKill(pos=(1295, 10590), pause_on_combat=True),
            BT.Wait(duration_ms=21500),
            BT.MoveAndKill(
                pos=[(-2426, 11130), (-3164, 9874), (-4130, 10219)], pause_on_combat=True
            ),
            BT.Wait(duration_ms=600),
            BT.MoveAndKill(
                pos=[(-5225, 10896), (-6926, 14394), (-7230, 11892), (-8232, 10143), (-5958, 8958)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=649, timeout_ms=10000),
            BT.MoveAndKill(pos=(-20949, 12235), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CAPTAIN_LANGMAR', dialog_ids=['0x831907']),
        ],
    )


def warband_of_brothers() -> BehaviorTree:
    return BT.Sequence(
        name='Warband of Brothers',
        children=[
            BT.Travel(target_map_id=648, leave_party=True),
            BT.MoveAndKill(pos=(-18862, 17929), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GRON_FIERCECLAW_MERCHANT', dialog_ids=['0x86', '0x84']),
            BT.WaitForMapLoad(map_id=666, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-10008, 599), (-11045, 2230), (-12264, 3332), (-8019, 4391), (-6423, 5525)],
                pause_on_combat=True,
            ),
            BT.MoveToTarget(kind='enemy', key='CHARR_PRISON_GUARD'),
            BT.MoveAndKill(pos=(-4181, 6568), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-8108, 6180), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-10243, 4960), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-12704, 3484), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-4358, 6264), pause_on_combat=True),
            BT.Interact(kind='gadget', key='CHARR_PRISON_LOCK', pos=(-3963, 6390)),
            BT.MoveAndKill(pos=(3225, 8428), pause_on_combat=True),
            BT.MoveAndKill(pos=(-14309, 2504), pause_on_combat=True),
            BT.MoveAndKill(pos=(-18673, 818), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-19279, 552), target_map_id=667, move_tolerance=300),
            BT.MoveAndKill(pos=(-1702, 11590), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-2090, 11359), pause_on_combat=True),
            BT.Interact(kind='gadget', key='CHARR_PRISON_LOCK', pos=(-2254, 11176)),
            BT.MoveAndKill(pos=[(-2463, 8881), (-2051, 10637)], pause_on_combat=True),
            BT.Wait(duration_ms=5500),
            BT.MoveAndKill(pos=(16028, 8852), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(16657, 8712), target_map_id=668, move_tolerance=300),
            BT.MoveAndKill(pos=(17203, -6240), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.Interact(kind='gadget', key='CHARR_PRISON_LOCK', pos=(17159, -6461)),
            BT.MoveAndKill(
                pos=[(19008, -10634), (18661, -12008), (18073, -14440)], pause_on_combat=True
            ),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(18077, -14657), pause_on_combat=True),
            BT.Interact(kind='gadget', key='CHARR_PRISON_LOCK', pos=(18147, -14974)),
            BT.MoveAndKill(pos=(8664, -10595), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(9610, -12208), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(10344, -13831), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(10298, -14635), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25413, point=None, max_dist=4500),
            BT.Interact(kind='gadget', key='CHARR_PRISON_LOCK', pos=(10034, -14899)),
            BT.MoveAndKill(pos=(1111, -8282), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=648, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'against_the_charr': (
        (-9660.0, -2967.0),
        (12464.0, -8850.0),
        (18008.0, -2874.0),
        (17836.0, 2958.0),
        (19851.0, 3696.0),
    ),
    'assault_on_the_stronghold': (
        (-15950.0, 14257.0),
        (-15272.0, 13607.0),
        (-13666.0, 11318.0),
        (5530.0, 11697.0),
        (6015.0, 9124.0),
        (5215.0, 12149.0),
        (3821.0, 11103.0),
        (1292.0, 10679.0),
        (1295.0, 10590.0),
        (-2426.0, 11130.0),
        (-3164.0, 9874.0),
        (-4130.0, 10219.0),
        (-5225.0, 10896.0),
        (-6926.0, 14394.0),
        (-7230.0, 11892.0),
        (-8232.0, 10143.0),
        (-5958.0, 8958.0),
        (-20949.0, 12235.0),
    ),
    'warband_of_brothers': (
        (-18862.0, 17929.0),
        (-10008.0, 599.0),
        (-11045.0, 2230.0),
        (-12264.0, 3332.0),
        (-8019.0, 4391.0),
        (-6423.0, 5525.0),
        (-4181.0, 6568.0),
        (-8108.0, 6180.0),
        (-10243.0, 4960.0),
        (-12704.0, 3484.0),
        (-4358.0, 6264.0),
        (3225.0, 8428.0),
        (-14309.0, 2504.0),
        (-18673.0, 818.0),
        (-19279.0, 552.0),
        (-1702.0, 11590.0),
        (-2090.0, 11359.0),
        (-2463.0, 8881.0),
        (-2051.0, 10637.0),
        (16028.0, 8852.0),
        (16657.0, 8712.0),
        (17203.0, -6240.0),
        (19008.0, -10634.0),
        (18661.0, -12008.0),
        (18073.0, -14440.0),
        (18077.0, -14657.0),
        (8664.0, -10595.0),
        (9610.0, -12208.0),
        (10344.0, -13831.0),
        (10298.0, -14635.0),
        (1111.0, -8282.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'eotn/against_the_charr',
        'title': 'Against the Charr',
        'factory': 'against_the_charr',
        'source_steps': 5,
        'raw_steps': 5,
    },
    {
        'kind': 'mission',
        'key': 'eotn/assault_on_the_stronghold',
        'title': 'Assault on the Stronghold',
        'factory': 'assault_on_the_stronghold',
        'source_steps': 21,
        'raw_steps': 21,
    },
    {
        'kind': 'mission',
        'key': 'eotn/warband_of_brothers',
        'title': 'Warband of Brothers',
        'factory': 'warband_of_brothers',
        'source_steps': 46,
        'raw_steps': 46,
    },
)
