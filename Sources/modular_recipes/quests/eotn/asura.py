"""Quests Eotn Asura BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def finding_gadd() -> BehaviorTree:
    return BT.Sequence(
        name='Finding Gadd',
        children=[
            BT.Travel(target_map_id=624, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(16304, 15742), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LIVIA', dialog_ids=['0x833301']),
            BT.Travel(target_map_id=638, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-8405, -23510), pause_on_combat=True),
            BT.Dialog(kind='npc', key='BARTHOLOS', dialog_ids=['0x833304']),
            BT.MoveAndKill(pos=(-9215, -21820), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-9528, -20315), target_map_id=558, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(-2300, -20218), (2392, -20893), (6911, -19863), (11722, -23627)],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='LIVIA', dialog_ids=['0x833304']),
            BT.MoveAndKill(pos=[(8714, -18746), (8756, -14334)], pause_on_combat=True),
            BT.MoveToTarget(kind='enemy', key='INSCRIBED_ETTIN'),
            BT.MoveToTarget(kind='enemy', key='INSCRIBED_ETTIN'),
            BT.Wait(duration_ms=5000),
            BT.MoveAndKill(pos=(11362, -13960), pause_on_combat=True),
            BT.Wait(duration_ms=5000),
            BT.MoveAndKill(pos=(-5766, -13633), pause_on_combat=True),
            BT.MoveToTarget(kind='enemy', key='INSCRIBED_ETTIN'),
            BT.MoveToTarget(kind='enemy', key='INSCRIBED_ETTIN'),
            BT.Wait(duration_ms=5000),
            BT.MoveAndKill(pos=(-6709, -21983), pause_on_combat=True),
            BT.Wait(duration_ms=5000),
            BT.MoveAndKill(pos=[(-2464, -19708), (2185, -21518), (2690, -22827)], pause_on_combat=True),
            BT.MoveToTarget(kind='enemy', key='INSCRIBED_ETTIN'),
            BT.MoveToTarget(kind='enemy', key='INSCRIBED_ETTIN'),
            BT.Wait(duration_ms=5000),
            BT.MoveAndKill(pos=(2827, -25231), pause_on_combat=True),
            BT.Wait(duration_ms=5000),
            BT.MoveAndKill(pos=[(7662, -19975), (11937, -24061)], pause_on_combat=True),
            BT.Interact(kind='npc', key='GADD'),
            BT.Dialog(kind='npc', key='GADD', dialog_ids=['0x833304']),
            BT.Interact(kind='npc', key='INSCRIPTION_STONE'),
            BT.Dialog(kind='npc', key='INSCRIPTION_STONE', dialog_ids=['0x833307']),
        ],
    )


def lab_space() -> BehaviorTree:
    return BT.Sequence(
        name='Lab Space',
        children=[
            BT.Travel(target_map_id=624, leave_party=True),
            BT.MoveAndKill(pos=(16313, 16016), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LORK', dialog_ids=['0x832C01']),
            BT.Travel(target_map_id=640, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(16064, 18401), pause_on_combat=True),
            BT.Dialog(kind='npc', key='BLIMM', dialog_ids=['0x832C04']),
            BT.MoveAndKill(pos=(16532, 14408), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(16407, 13739), target_map_id=569, move_tolerance=300),
            BT.MoveAndKill(pos=(14811, 13087), pause_on_combat=True),
            BT.Dialog(kind='npc', key='EXPERIMENT_KREWE_MEMBER', dialog_ids=['0x84']),
            BT.MoveAndKill(pos=(10371, 11459), pause_on_combat=True),
            BT.Dialog(kind='npc', key='BLIMM', dialog_ids=['0x832C04']),
            BT.MoveAndKill(pos=(-17395, 14998), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=24628, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-16325, 14284), pause_on_combat=True),
            BT.Interact(kind='npc', key='BLIMM'),
            BT.Dialog(kind='npc', key='BLIMM', dialog_ids=['0x832C07']),
        ],
    )


def a_little_help() -> BehaviorTree:
    return BT.Sequence(
        name='A Little Help',
        children=[
            BT.Travel(target_map_id=624, leave_party=True),
            BT.MoveAndKill(pos=(16569, 15999), pause_on_combat=True),
            BT.Dialog(kind='npc', key='PLAXX', dialog_ids=['0x833401']),
            BT.Travel(target_map_id=640, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(18915, 16758), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(20051, 16797), target_map_id=501, move_tolerance=300),
            BT.MoveAndKill(pos=(-24231, -5562), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SKY_KREWE_MEMBER', dialog_ids=['0x84']),
            BT.MoveAndKill(pos=[(-10529, -11988), (-3596, -10821), (17413, -9350)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='RENK', dialog_ids=['0x833404']),
            BT.MoveAndKill(pos=[(-5210, -11643), (-7698, -12251), (-8439, -13153)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-8569, -13698), target_map_id=572, move_tolerance=300),
            BT.MoveAndKill(pos=(-5387, 16137), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MACHINE_KREWE_MEMBER', dialog_ids=['0x84']),
            BT.MoveAndKill(pos=[(-21948, -9462), (-23997, -10397)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='RENK', dialog_ids=['0x833404']),
            BT.Travel(target_map_id=640, leave_party=True),
            BT.MoveAndKill(pos=(16093, 15293), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MAMP', dialog_ids=['0x833407']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'finding_gadd': (
        (16304.0, 15742.0),
        (-8405.0, -23510.0),
        (-9215.0, -21820.0),
        (-9528.0, -20315.0),
        (-2300.0, -20218.0),
        (2392.0, -20893.0),
        (6911.0, -19863.0),
        (11722.0, -23627.0),
        (8714.0, -18746.0),
        (8756.0, -14334.0),
        (11362.0, -13960.0),
        (-5766.0, -13633.0),
        (-6709.0, -21983.0),
        (-2464.0, -19708.0),
        (2185.0, -21518.0),
        (2690.0, -22827.0),
        (2827.0, -25231.0),
        (7662.0, -19975.0),
        (11937.0, -24061.0),
    ),
    'lab_space': (
        (16313.0, 16016.0),
        (16064.0, 18401.0),
        (16532.0, 14408.0),
        (16407.0, 13739.0),
        (14811.0, 13087.0),
        (10371.0, 11459.0),
        (-17395.0, 14998.0),
        (-16325.0, 14284.0),
    ),
    'a_little_help': (
        (16569.0, 15999.0),
        (18915.0, 16758.0),
        (20051.0, 16797.0),
        (-24231.0, -5562.0),
        (-10529.0, -11988.0),
        (-3596.0, -10821.0),
        (17413.0, -9350.0),
        (-5210.0, -11643.0),
        (-7698.0, -12251.0),
        (-8439.0, -13153.0),
        (-8569.0, -13698.0),
        (-5387.0, 16137.0),
        (-21948.0, -9462.0),
        (-23997.0, -10397.0),
        (16093.0, 15293.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'eotn/finding_gadd',
        'title': 'Finding Gadd',
        'factory': 'finding_gadd',
        'source_steps': 35,
        'raw_steps': 35,
    },
    {
        'kind': 'quest',
        'key': 'eotn/lab_space',
        'title': 'Lab Space',
        'factory': 'lab_space',
        'source_steps': 18,
        'raw_steps': 18,
    },
    {
        'kind': 'quest',
        'key': 'eotn/a_little_help',
        'title': 'A Little Help',
        'factory': 'a_little_help',
        'source_steps': 20,
        'raw_steps': 20,
    },
)
