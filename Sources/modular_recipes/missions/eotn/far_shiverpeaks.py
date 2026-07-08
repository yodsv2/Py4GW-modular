"""Missions Eotn Far Shiverpeaks BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def blood_washes_blood() -> BehaviorTree:
    return BT.Sequence(
        name='Blood Washes Blood',
        children=[
            BT.MoveAndKill(pos=(9852, -21129), pause_on_combat=True),
            BT.Dialog(kind='npc', key='BEAR_SPIRIT', dialog_ids=['0x84']),
            BT.MoveAndKill(pos=(15075, -20374), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(15589, -20504), target_map_id=654, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(2676, 13968), (1923, 12097), (147, 12953), (499, 15733), (890, 14115)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=500),
            BT.Interact(kind='npc', key='SHRINE_OF_THE_BEAR_SPIRIT'),
            BT.MoveAndKill(
                pos=[(8150, 12058), (11390, 11327), (13030, 9321), (14485, 5848), (13322, 3666), (14086, 2207)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=400),
            BT.MoveAndKill(
                pos=[(15484, 3382), (16878, 3503), (16801, 4951), (18194, 3516), (17283, 1185)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=644, timeout_ms=10000),
        ],
    )


def curse_of_the_nornbear() -> BehaviorTree:
    return BT.Sequence(
        name='Curse of the Nornbear',
        children=[
            BT.Travel(target_map_id=643, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.Dialog(kind='npc', key='SIF_SHADOWHUNTER', dialog_ids=['0x81', '0x86']),
            BT.WaitForMapLoad(map_id=653, timeout_ms=10000),
            BT.MoveAndKill(pos=(7227, 23631), pause_on_combat=True),
            BT.Wait(duration_ms=600),
            BT.Wait(duration_ms=100),
            BT.MoveAndKill(pos=(-5735, 15902), pause_on_combat=True),
            BT.Wait(duration_ms=24000),
            BT.MoveAndKill(pos=(8023, 14368), pause_on_combat=True),
            BT.Wait(duration_ms=400),
            BT.MoveAndKill(pos=(4136, 15376), pause_on_combat=True),
            BT.Wait(duration_ms=400),
            BT.MoveAndKill(pos=(3831, 5747), pause_on_combat=True),
            BT.Wait(duration_ms=900),
            BT.Wait(duration_ms=100),
            BT.MoveAndKill(pos=(4765, 6711), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=643, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'blood_washes_blood': (
        (9852.0, -21129.0),
        (15075.0, -20374.0),
        (15589.0, -20504.0),
        (2676.0, 13968.0),
        (1923.0, 12097.0),
        (147.0, 12953.0),
        (499.0, 15733.0),
        (890.0, 14115.0),
        (8150.0, 12058.0),
        (11390.0, 11327.0),
        (13030.0, 9321.0),
        (14485.0, 5848.0),
        (13322.0, 3666.0),
        (14086.0, 2207.0),
        (15484.0, 3382.0),
        (16878.0, 3503.0),
        (16801.0, 4951.0),
        (18194.0, 3516.0),
        (17283.0, 1185.0),
    ),
    'curse_of_the_nornbear': (
        (7227.0, 23631.0),
        (-5735.0, 15902.0),
        (8023.0, 14368.0),
        (4136.0, 15376.0),
        (3831.0, 5747.0),
        (4765.0, 6711.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'eotn/blood_washes_blood',
        'title': 'Blood Washes Blood',
        'factory': 'blood_washes_blood',
        'source_steps': 11,
        'raw_steps': 11,
    },
    {
        'kind': 'mission',
        'key': 'eotn/curse_of_the_nornbear',
        'title': 'Curse of the Nornbear',
        'factory': 'curse_of_the_nornbear',
        'source_steps': 18,
        'raw_steps': 18,
    },
)
