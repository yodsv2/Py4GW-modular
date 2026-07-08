"""Quests Prophecies Story BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def elegy_for_those_left_behind() -> BehaviorTree:
    return BT.Sequence(
        name='Elegy for Those Left Behind',
        children=[
            BT.Travel(target_map_id=40, leave_party=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndKill(pos=(20233, 8381), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(20212, 7645), target_map_id=102, move_tolerance=300),
            BT.MoveAndKill(pos=(18208, -1661), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x85B201']),
            BT.MoveAndExitMap(pos=(17755, -1482), target_map_id=880, move_tolerance=300),
            BT.MoveAndKill(pos=(-6973, -10209), pause_on_combat=True),
            BT.Wait(duration_ms=50000),
            BT.MoveAndKill(pos=(-6973, -10209), pause_on_combat=True),
            BT.Wait(duration_ms=50000),
            BT.MoveAndKill(pos=(-5511, -7451), pause_on_combat=True),
            BT.Wait(duration_ms=50000),
            BT.MoveAndKill(pos=(-5511, -7451), pause_on_combat=True),
            BT.Wait(duration_ms=50000),
            BT.MoveAndKill(pos=(-4764, -12726), pause_on_combat=True),
            BT.Wait(duration_ms=50000),
            BT.MoveAndKill(pos=(-4764, -12726), pause_on_combat=True),
            BT.Wait(duration_ms=50000),
            BT.MoveAndKill(pos=(-7467, -9525), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x85B207']),
        ],
    )


def forgotten_wisdom() -> BehaviorTree:
    return BT.Sequence(
        name='Forgotten Wisdom',
        children=[
            BT.MoveAndKill(pos=(6449, -6568), pause_on_combat=True),
            BT.Dialog(kind='npc', key='YODS', dialog_ids=['0x801801']),
            BT.MoveAndKill(pos=(6856, -18390), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(7093, -19256), target_map_id=112, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(14190, -7863), (7525, -7063), (773, -6599)], pause_on_combat=True
            ),
            BT.Dialog(kind='npc', key='SILISS_YASSITH', dialog_ids=['0x801807']),
        ],
    )


def the_cost_of_survival() -> BehaviorTree:
    return BT.Sequence(
        name='The Cost of Survival',
        children=[
            BT.Travel(target_map_id=40, leave_party=True),
            BT.MoveAndKill(pos=(22634, 10267), pause_on_combat=True),
            BT.Dialog(kind='npc', key='KOPP_THE_QUICK', dialog_ids=['0x85B301']),
            BT.MoveAndKill(pos=(20222, 8212), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(20218, 7644), target_map_id=102, move_tolerance=300),
            BT.MoveAndKill(pos=(18144, -1984), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(17759, -1435), target_map_id=880, move_tolerance=300),
            BT.MoveAndKill(pos=(-7426, -9351), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x85B304', '0x85B304']),
            BT.MoveAndKill(pos=(-8760, -6086), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=38301, point=None, max_dist=4500),
            BT.MoveAndKill(pos=[(-8654, 3322), (-8621, 4130)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-8645, 4672), target_map_id=881, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (1408, 16426),
                    (-7437, 20924),
                    (-16195, 19388),
                    (-19326, 16501),
                    (-6780, 17707),
                    (-10618, 16002),
                    (-16598, 9208),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='DUKE_WILLGROVE', dialog_ids=['0x85B304']),
            BT.Travel(target_map_id=40, leave_party=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndExitMap(pos=(20206, 7645), target_map_id=102, move_tolerance=300),
            BT.MoveAndKill(pos=(18213, -2167), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(17765, -1422), target_map_id=880, move_tolerance=300),
            BT.MoveAndKill(pos=(-7471, -9318), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x85B304']),
            BT.MoveAndKill(pos=(-7614, -9268), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x85B307']),
        ],
    )


def the_dreamer_and_the_zealot() -> BehaviorTree:
    return BT.Sequence(
        name='The Dreamer and the Zealot',
        children=[
            BT.MoveAndKill(pos=(-7569, -9231), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x85B401']),
            BT.MoveAndKill(pos=(-8906, -4811), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=38301, point=None, max_dist=4500),
            BT.MoveAndKill(pos=[(-8744, 3134), (-8702, 3909)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-8692, 4687), target_map_id=881, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(-524, 19425), (-16516, 5885), (-16693, 5225)], pause_on_combat=True
            ),
            BT.MoveAndExitMap(pos=(-16773, 4430), target_map_id=882, move_tolerance=300),
            BT.MoveAndKill(pos=[(-17022, -1566), (-12479, -5705)], pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=25416, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-6256, -4310), pause_on_combat=True),
            BT.Interact(kind='gadget', key='BOSS_LOCK', pos=(-6471, -4283)),
            BT.MoveAndKill(
                pos=[
                    (-9551, -8035),
                    (-13331, -8604),
                    (-13746, -7877),
                    (-14061, -8130),
                    (-13214, -8943),
                    (-13631, -7805),
                    (-14089, -9093),
                    (-12917, -8624),
                    (-13500, -7703),
                    (-14271, -8268),
                    (-15863, -8644),
                ],
                pause_on_combat=True,
            ),
            BT.Interact(kind='gadget', key='ZEALOT_S_CHEST', pos=(-16068, -8484)),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x85B407']),
            BT.Travel(target_map_id=40, leave_party=True),
        ],
    )


def the_forgotten_ones() -> BehaviorTree:
    return BT.Sequence(
        name='The Forgotten Ones',
        children=[
            BT.Travel(target_map_id=154, leave_party=True),
            BT.MoveAndKill(pos=(-14899, 18776), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ANNELLE_FIPPS', dialog_ids=['0x801701']),
            BT.MoveAndKill(pos=(-14833, 18798), pause_on_combat=True),
            BT.Travel(target_map_id=38, leave_party=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndKill(pos=(-15272, 1501), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-15248, 2187), target_map_id=115, move_tolerance=300),
            BT.MoveAndKill(pos=(6357, -6758), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SARISS_YASSITH', dialog_ids=['0x801707']),
        ],
    )


def the_heros_challenge() -> BehaviorTree:
    return BT.Sequence(
        name="The Hero's Challenge",
        children=[
            BT.Travel(target_map_id=20, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-2122, 7481), pause_on_combat=True),
            BT.Dialog(kind='npc', key='VANYI', dialog_ids=['0x80C303', '0x80C301']),
            BT.Travel(target_map_id=24, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-6535, -31856), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-7355, -31759), target_map_id=98, move_tolerance=300),
            BT.MoveAndKill(pos=[(-18119, 8968), (-10243, 12232)], pause_on_combat=True),
            BT.Wait(duration_ms=99999),
            BT.MoveAndKill(
                pos=[(-9511, 11986), (-10163, 11753), (-10036, 12274)], pause_on_combat=True
            ),
            BT.Travel(target_map_id=20, leave_party=True),
            BT.MoveAndKill(pos=(-2102, 7486), pause_on_combat=True),
            BT.Dialog(kind='npc', key='VANYI', dialog_ids=['0x80C307']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'elegy_for_those_left_behind': (
        (20233.0, 8381.0),
        (20212.0, 7645.0),
        (18208.0, -1661.0),
        (17755.0, -1482.0),
        (-6973.0, -10209.0),
        (-6973.0, -10209.0),
        (-5511.0, -7451.0),
        (-5511.0, -7451.0),
        (-4764.0, -12726.0),
        (-4764.0, -12726.0),
        (-7467.0, -9525.0),
    ),
    'forgotten_wisdom': (
        (6449.0, -6568.0),
        (6856.0, -18390.0),
        (7093.0, -19256.0),
        (14190.0, -7863.0),
        (7525.0, -7063.0),
        (773.0, -6599.0),
    ),
    'the_cost_of_survival': (
        (22634.0, 10267.0),
        (20222.0, 8212.0),
        (20218.0, 7644.0),
        (18144.0, -1984.0),
        (17759.0, -1435.0),
        (-7426.0, -9351.0),
        (-8760.0, -6086.0),
        (-8654.0, 3322.0),
        (-8621.0, 4130.0),
        (-8645.0, 4672.0),
        (1408.0, 16426.0),
        (-7437.0, 20924.0),
        (-16195.0, 19388.0),
        (-19326.0, 16501.0),
        (-6780.0, 17707.0),
        (-10618.0, 16002.0),
        (-16598.0, 9208.0),
        (20206.0, 7645.0),
        (18213.0, -2167.0),
        (17765.0, -1422.0),
        (-7471.0, -9318.0),
        (-7614.0, -9268.0),
    ),
    'the_dreamer_and_the_zealot': (
        (-7569.0, -9231.0),
        (-8906.0, -4811.0),
        (-8744.0, 3134.0),
        (-8702.0, 3909.0),
        (-8692.0, 4687.0),
        (-524.0, 19425.0),
        (-16516.0, 5885.0),
        (-16693.0, 5225.0),
        (-16773.0, 4430.0),
        (-17022.0, -1566.0),
        (-12479.0, -5705.0),
        (-6256.0, -4310.0),
        (-9551.0, -8035.0),
        (-13331.0, -8604.0),
        (-13746.0, -7877.0),
        (-14061.0, -8130.0),
        (-13214.0, -8943.0),
        (-13631.0, -7805.0),
        (-14089.0, -9093.0),
        (-12917.0, -8624.0),
        (-13500.0, -7703.0),
        (-14271.0, -8268.0),
        (-15863.0, -8644.0),
    ),
    'the_forgotten_ones': (
        (-14899.0, 18776.0),
        (-14833.0, 18798.0),
        (-15272.0, 1501.0),
        (-15248.0, 2187.0),
        (6357.0, -6758.0),
    ),
    'the_heros_challenge': (
        (-2122.0, 7481.0),
        (-6535.0, -31856.0),
        (-7355.0, -31759.0),
        (-18119.0, 8968.0),
        (-10243.0, 12232.0),
        (-9511.0, 11986.0),
        (-10163.0, 11753.0),
        (-10036.0, 12274.0),
        (-2102.0, 7486.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'prophecies/elegy_for_those_left_behind',
        'title': 'Elegy for Those Left Behind',
        'factory': 'elegy_for_those_left_behind',
        'source_steps': 21,
        'raw_steps': 21,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/forgotten_wisdom',
        'title': 'Forgotten Wisdom',
        'factory': 'forgotten_wisdom',
        'source_steps': 6,
        'raw_steps': 6,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/the_cost_of_survival',
        'title': 'The Cost of Survival',
        'factory': 'the_cost_of_survival',
        'source_steps': 24,
        'raw_steps': 24,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/the_dreamer_and_the_zealot',
        'title': 'The Dreamer and the Zealot',
        'factory': 'the_dreamer_and_the_zealot',
        'source_steps': 16,
        'raw_steps': 16,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/the_forgotten_ones',
        'title': 'The Forgotten Ones',
        'factory': 'the_forgotten_ones',
        'source_steps': 10,
        'raw_steps': 10,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/the_heros_challenge',
        'title': "The Hero's Challenge",
        'factory': 'the_heros_challenge',
        'source_steps': 14,
        'raw_steps': 14,
    },
)
