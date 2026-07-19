"""Quests Nightfall Realm Of Torment BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def uncharted_territory() -> BehaviorTree:
    return BT.Sequence(
        name='Uncharted Territory',
        children=[
            BT.Travel(target_map_id=450, leave_party=True),
            BT.LoadParty(max_heroes=8, required_hero=['Dunkoro']),
            BT.MoveAndKill(pos=(-972, 8443), pause_on_combat=True),
            BT.Dialog(kind='npc', key='PEHAI', dialog_ids=['0x82BD01']),
            BT.MoveAndKill(pos=(-8124, 12271), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-7849, 13854), target_map_id=465, move_tolerance=300),
            BT.MoveAndKill(pos=(-2475, -14276), pause_on_combat=True),
            BT.Dialog(kind='npc', key='KORMIR', dialog_ids=['0x82BD04']),
            BT.MoveAndKill(pos=(3241, -1519), pause_on_combat=True),
            BT.MoveAndKill(pos=(19690, 16090), pause_on_combat=True),
            BT.Dialog(kind='npc', key='TORTURED_SUNSPEAR', dialog_ids=['0x85']),
            BT.WaitForMapLoad(map_id=494, timeout_ms=10000),
            BT.Dialog(kind='npc', key='JARINDOK', dialog_ids=['0x82BD07']),
        ],
    )


def kormirs_crusade() -> BehaviorTree:
    return BT.Sequence(
        name="Kormir's Crusade",
        children=[
            BT.Travel(target_map_id=469, leave_party=True),
            BT.MoveAndKill(pos=(9728, 20952), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RAHMOR', dialog_ids=['0x82BE01']),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(8597, 19399), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(8322, 19037), target_map_id=468, move_tolerance=300),
            BT.MoveAndKill(pos=(9801, 5698), pause_on_combat=True),
            BT.Wait(duration_ms=43700),
            BT.Dialog(kind='npc', key='KORMIR', dialog_ids=['0x82BE04']),
            BT.MoveAndKill(
                pos=[(5363, 6263), (4528, 9747), (3918, 10515), (2690, 11697), (-9627, -2096)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=10000),
            BT.MoveAndExitMap(pos=(-10441, -2732), target_map_id=473, move_tolerance=300),
            BT.MoveAndKill(pos=(14165, -2801), pause_on_combat=True),
            BT.Dialog(kind='npc', key='KEEPER_HALYSSI', dialog_ids=['0x82BE07']),
        ],
    )


def all_alone_in_the_darkness() -> BehaviorTree:
    return BT.Sequence(
        name='All Alone in the Darkness',
        children=[
            BT.Travel(target_map_id=473, leave_party=True),
            BT.Dialog(kind='npc', key='KEEPER_HALYSSI', dialog_ids=['0x82BF01']),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(12226, -2074), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(11900, -1728), target_map_id=472, move_tolerance=300),
            BT.MoveAndKill(pos=(13655, 18542), pause_on_combat=True),
            BT.Dialog(kind='npc', key='KORMIR', dialog_ids=['0x82BF04']),
            BT.MoveAndKill(pos=[(-13159, -11636), (-11746, -11708)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='SCOUT_AHTOK', dialog_ids=['0x82BF04', '0x84', '0x85']),
            BT.WaitForMapLoad(map_id=495, timeout_ms=10000),
            BT.MoveAndKill(pos=(-11265, -9877), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RUNIC_ORACLE', dialog_ids=['0x82BF07']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'uncharted_territory': (
        (-972.0, 8443.0),
        (-8124.0, 12271.0),
        (-7849.0, 13854.0),
        (-2475.0, -14276.0),
        (3241.0, -1519.0),
        (19690.0, 16090.0),
    ),
    'kormirs_crusade': (
        (9728.0, 20952.0),
        (8597.0, 19399.0),
        (8322.0, 19037.0),
        (9801.0, 5698.0),
        (5363.0, 6263.0),
        (4528.0, 9747.0),
        (3918.0, 10515.0),
        (2690.0, 11697.0),
        (-9627.0, -2096.0),
        (-10441.0, -2732.0),
        (14165.0, -2801.0),
    ),
    'all_alone_in_the_darkness': (
        (12226.0, -2074.0),
        (11900.0, -1728.0),
        (13655.0, 18542.0),
        (-13159.0, -11636.0),
        (-11746.0, -11708.0),
        (-11265.0, -9877.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'nightfall/uncharted_territory',
        'title': 'Uncharted Territory',
        'factory': 'uncharted_territory',
        'source_steps': 14,
        'raw_steps': 14,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/kormirs_crusade',
        'title': "Kormir's Crusade",
        'factory': 'kormirs_crusade',
        'source_steps': 14,
        'raw_steps': 14,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/all_alone_in_the_darkness',
        'title': 'All Alone in the Darkness',
        'factory': 'all_alone_in_the_darkness',
        'source_steps': 12,
        'raw_steps': 12,
    },
)
