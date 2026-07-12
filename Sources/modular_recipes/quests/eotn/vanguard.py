"""Quests Eotn Vanguard BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def search_for_the_ebon_vanguard() -> BehaviorTree:
    return BT.Sequence(
        name='Search for the Ebon Vanguard',
        children=[
            BT.Travel(target_map_id=650, leave_party=True),
            BT.MoveAndKill(pos=(-25104, 13667), pause_on_combat=True),
            BT.Dialog(kind='npc', key='OLFUN_LONGEYE', dialog_ids=['0x831801']),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-22533, 13311), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-22051, 12850), target_map_id=649, move_tolerance=300),
            BT.MoveAndKill(pos=(-9598, -2985), pause_on_combat=True),
            BT.Interact(kind='npc', key='VANGUARD_HELMET'),
            BT.Dialog(kind='npc', key='VANGUARD_HELMET', dialog_ids=['0x831807']),
        ],
    )


def the_dawn_of_rebellion() -> BehaviorTree:
    return BT.Sequence(
        name='The Dawn of Rebellion',
        children=[
            BT.MoveAndKill(pos=(19009, 589), pause_on_combat=True),
            BT.Dialog(kind='npc', key='PYRE_FIERCESHOT', dialog_ids=['0x838C01']),
            BT.MoveAndKill(pos=[(14319, -3778), (11180, 4001), (24292, 15195)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(25058, 15327), target_map_id=647, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(-16405, 6898), (-14933, 10870), (-15468, 13454), (-17616, 14913), (-16927, 16674)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=648, timeout_ms=10000),
            BT.MoveAndKill(pos=(-19024, 17888), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GRON_FIERCECLAW_MERCHANT', dialog_ids=['0x838C07']),
        ],
    )


def what_must_be_done() -> BehaviorTree:
    return BT.Sequence(
        name='What Must be Done',
        children=[
            BT.Travel(target_map_id=648, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-14462, 17060), pause_on_combat=True),
            BT.Dialog(kind='npc', key='BONWOR_FIERCEBLADE', dialog_ids=['0x838D01']),
            BT.MoveAndKill(pos=(-15842, 14281), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-15303, 13602), target_map_id=647, move_tolerance=300),
            BT.MoveAndKill(pos=(-2616, 6456), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SEER_FIERCEREIGN', dialog_ids=['0x838D04']),
            BT.MoveAndKill(
                pos=[(8888, 6497), (9995, 4300), (10755, 8875), (14723, 5059)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=30300),
            BT.MoveAndKill(pos=(-9201, -662), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GRON_FIERCECLAW', dialog_ids=['0x838D04']),
            BT.MoveAndKill(pos=(-6579, -7723), pause_on_combat=True),
            BT.MoveToTarget(kind='enemy', key='ARMORED_SAURUS'),
            BT.Travel(target_map_id=648, leave_party=True),
            BT.MoveAndKill(pos=(-14384, 17107), pause_on_combat=True),
            BT.Dialog(kind='npc', key='BONWOR_FIERCEBLADE', dialog_ids=['0x838D04', '0x84']),
            BT.WaitForMapLoad(map_id=674, timeout_ms=10000),
            BT.MoveAndKill(pos=(-16532, 16929), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=648, timeout_ms=10000),
            BT.MoveAndKill(pos=(-14397, 17097), pause_on_combat=True),
            BT.Dialog(kind='npc', key='BONWOR_FIERCEBLADE', dialog_ids=['0x838D07']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'search_for_the_ebon_vanguard': ((-25104.0, 13667.0), (-22533.0, 13311.0), (-22051.0, 12850.0), (-9598.0, -2985.0)),
    'the_dawn_of_rebellion': (
        (19009.0, 589.0),
        (14319.0, -3778.0),
        (11180.0, 4001.0),
        (24292.0, 15195.0),
        (25058.0, 15327.0),
        (-16405.0, 6898.0),
        (-14933.0, 10870.0),
        (-15468.0, 13454.0),
        (-17616.0, 14913.0),
        (-16927.0, 16674.0),
        (-19024.0, 17888.0),
    ),
    'what_must_be_done': (
        (-14462.0, 17060.0),
        (-15842.0, 14281.0),
        (-15303.0, 13602.0),
        (-2616.0, 6456.0),
        (8888.0, 6497.0),
        (9995.0, 4300.0),
        (10755.0, 8875.0),
        (14723.0, 5059.0),
        (-9201.0, -662.0),
        (-6579.0, -7723.0),
        (-14384.0, 17107.0),
        (-16532.0, 16929.0),
        (-14397.0, 17097.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'eotn/search_for_the_ebon_vanguard',
        'title': 'Search for the Ebon Vanguard',
        'factory': 'search_for_the_ebon_vanguard',
        'source_steps': 9,
        'raw_steps': 9,
    },
    {
        'kind': 'quest',
        'key': 'eotn/the_dawn_of_rebellion',
        'title': 'The Dawn of Rebellion',
        'factory': 'the_dawn_of_rebellion',
        'source_steps': 8,
        'raw_steps': 8,
    },
    {
        'kind': 'quest',
        'key': 'eotn/what_must_be_done',
        'title': 'What Must be Done',
        'factory': 'what_must_be_done',
        'source_steps': 22,
        'raw_steps': 22,
    },
)
