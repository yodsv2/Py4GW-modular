"""Quests Eotn Norn BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def northern_allies_reward() -> BehaviorTree:
    return BT.Sequence(
        name='Northern Allies Reward', children=[BT.Dialog(kind='npc', key='JALIS_IRONHAMMER', dialog_ids=['0x838907'])]
    )


def tracking_the_nornbear() -> BehaviorTree:
    return BT.Sequence(
        name='Tracking the Nornbear',
        children=[
            BT.Travel(target_map_id=644, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(24014, -7458), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GUNNAR_POUNDFIST', dialog_ids=['0x832804']),
            BT.Travel(target_map_id=643, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(14297, 23859), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SIF_SHADOWHUNTER', dialog_ids=['0x832804', '0x84']),
            BT.WaitForMapLoad(map_id=678, timeout_ms=10000),
            BT.MoveAndKill(pos=(10413, 23949), pause_on_combat=True),
            BT.Wait(duration_ms=6200),
            BT.WaitForMapLoad(map_id=643, timeout_ms=10000),
            BT.MoveAndKill(pos=(14356, 23862), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SIF_SHADOWHUNTER', dialog_ids=['0x832807']),
        ],
    )


def flames_of_the_bear_spirit() -> BehaviorTree:
    return BT.Sequence(
        name='Flames of the Bear Spirit',
        children=[
            BT.Travel(target_map_id=643, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(15958, 22933), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(16690, 22876), target_map_id=546, move_tolerance=300),
            BT.MoveAndKill(pos=(4450, 5881), pause_on_combat=True),
            BT.Dialog(kind='npc', key='EGIL_FIRETELLER', dialog_ids=['0x832003', '0x832001']),
            BT.MoveAndKill(pos=(9551, -21100), pause_on_combat=True),
            BT.FlagAllHeroes(9415, -21413),
            BT.Wait(duration_ms=25000),
            BT.Wait(duration_ms=100000),
            BT.WaitForMapLoad(map_id=546, timeout_ms=10000),
            BT.MoveAndKill(pos=(9459, -21539), pause_on_combat=True),
            BT.Dialog(kind='npc', key='EGIL_FIRETELLER', dialog_ids=['0x832007']),
        ],
    )


def vision_of_the_raven_spirit() -> BehaviorTree:
    return BT.Sequence(
        name='Vision of the Raven Spirit',
        children=[
            BT.Travel(target_map_id=645, leave_party=True),
            BT.MoveAndKill(pos=(276, -631), pause_on_combat=True),
            BT.Dialog(kind='npc', key='OLAF_OLAFSON', dialog_ids=['0x832E01']),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-873, 1194), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-1427, 1185), target_map_id=553, move_tolerance=300),
            BT.MoveAndKill(pos=(-15505, 8669), pause_on_combat=True),
            BT.Dialog(kind='npc', key='OLAF_OLAFSON', dialog_ids=['0x832E04', '0x85']),
            BT.MoveAndKill(pos=[(-15630, 7992), (-14808, 8584), (-15645, 9041)], pause_on_combat=True),
            BT.Wait(duration_ms=60000),
            BT.MoveAndKill(pos=[(-15431, 7350), (-14077, 8356), (-15203, 8677)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='OLAF_OLAFSON', dialog_ids=['0x832E07']),
        ],
    )


def the_big_unfriendly_yotun() -> BehaviorTree:
    return BT.Sequence(
        name='The Big Unfriendly Yotun',
        children=[
            BT.Travel(target_map_id=643, leave_party=True),
            BT.MoveAndKill(pos=(12222, 24571), pause_on_combat=True),
            BT.Dialog(kind='npc', key='UNDRATH_BLASTROCK', dialog_ids=['0x837E03', '0x837E01']),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(13360, 19952), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(13568, 19423), target_map_id=513, move_tolerance=300),
            BT.MoveAndKill(pos=[(15058, 14305), (15077, 11936)], pause_on_combat=True),
            BT.Travel(target_map_id=643, leave_party=True),
            BT.MoveAndKill(pos=(12191, 24580), pause_on_combat=True),
            BT.Dialog(kind='npc', key='UNDRATH_BLASTROCK', dialog_ids=['0x837E07']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'northern_allies_reward': (),
    'tracking_the_nornbear': ((24014.0, -7458.0), (14297.0, 23859.0), (10413.0, 23949.0), (14356.0, 23862.0)),
    'flames_of_the_bear_spirit': (
        (15958.0, 22933.0),
        (16690.0, 22876.0),
        (4450.0, 5881.0),
        (9551.0, -21100.0),
        (9459.0, -21539.0),
    ),
    'vision_of_the_raven_spirit': (
        (276.0, -631.0),
        (-873.0, 1194.0),
        (-1427.0, 1185.0),
        (-15505.0, 8669.0),
        (-15630.0, 7992.0),
        (-14808.0, 8584.0),
        (-15645.0, 9041.0),
        (-15431.0, 7350.0),
        (-14077.0, 8356.0),
        (-15203.0, 8677.0),
    ),
    'the_big_unfriendly_yotun': (
        (12222.0, 24571.0),
        (13360.0, 19952.0),
        (13568.0, 19423.0),
        (15058.0, 14305.0),
        (15077.0, 11936.0),
        (12191.0, 24580.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'eotn/northern_allies_reward',
        'title': 'Northern Allies Reward',
        'factory': 'northern_allies_reward',
        'source_steps': 1,
        'raw_steps': 1,
    },
    {
        'kind': 'quest',
        'key': 'eotn/tracking_the_nornbear',
        'title': 'Tracking the Nornbear',
        'factory': 'tracking_the_nornbear',
        'source_steps': 14,
        'raw_steps': 14,
    },
    {
        'kind': 'quest',
        'key': 'eotn/flames_of_the_bear_spirit',
        'title': 'Flames of the Bear Spirit',
        'factory': 'flames_of_the_bear_spirit',
        'source_steps': 12,
        'raw_steps': 12,
    },
    {
        'kind': 'quest',
        'key': 'eotn/vision_of_the_raven_spirit',
        'title': 'Vision of the Raven Spirit',
        'factory': 'vision_of_the_raven_spirit',
        'source_steps': 12,
        'raw_steps': 12,
    },
    {
        'kind': 'quest',
        'key': 'eotn/the_big_unfriendly_yotun',
        'title': 'The Big Unfriendly Yotun',
        'factory': 'the_big_unfriendly_yotun',
        'source_steps': 10,
        'raw_steps': 10,
    },
)
