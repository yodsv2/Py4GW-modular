"""Quests Eotn Story BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


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
            BT.MoveAndKill(
                pos=[(-10529, -11988), (-3596, -10821), (17413, -9350)], pause_on_combat=True
            ),
            BT.Dialog(kind='npc', key='RENK', dialog_ids=['0x833404']),
            BT.MoveAndKill(
                pos=[(-5210, -11643), (-7698, -12251), (-8439, -13153)], pause_on_combat=True
            ),
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


def against_the_destroyers_start() -> BehaviorTree:
    return BT.Sequence(
        name='Against the Destroyers Start',
        children=[
            BT.Travel(target_map_id=642, leave_party=True),
            BT.MoveAndKill(pos=(-3615, 4369), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-4547, 5064), target_map_id=646, move_tolerance=300),
            BT.MoveAndKill(pos=(-6545, 6562), pause_on_combat=True),
            BT.Interact(kind='npc', key='GWEN'),
            BT.Dialog(kind='npc', key='SCRYING_POOL', dialog_ids=['0x63A', '0x63C']),
            BT.Wait(duration_ms=7400),
            BT.WaitForMapLoad(map_id=646, timeout_ms=10000),
            BT.Dialog(kind='npc', key='GWEN', dialog_ids=['0x89', '0x89', '0x831904']),
            BT.MoveAndKill(pos=(-6134, 5830), pause_on_combat=True),
            BT.Dialog(kind='npc', key='OGDEN_STONEHEALER', dialog_ids=['0x838904']),
            BT.MoveAndKill(pos=(-5757, 6223), pause_on_combat=True),
            BT.Dialog(kind='npc', key='VEKK', dialog_ids=['0x839304']),
            BT.Travel(target_map_id=642, leave_party=True),
            BT.MoveAndKill(pos=(438, 1333), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(781, 1061), target_map_id=499, move_tolerance=300),
            BT.MoveAndKill(pos=(2851, -365), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JORA', dialog_ids=['0x832801']),
        ],
    )


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
            BT.MoveAndKill(
                pos=[(-2464, -19708), (2185, -21518), (2690, -22827)], pause_on_combat=True
            ),
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


def northern_allies_reward() -> BehaviorTree:
    return BT.Sequence(
        name='Northern Allies Reward', children=[BT.Dialog(kind='npc', key='JALIS_IRONHAMMER', dialog_ids=['0x838907'])]
    )


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


def the_dawn_of_rebellion() -> BehaviorTree:
    return BT.Sequence(
        name='The Dawn of Rebellion',
        children=[
            BT.MoveAndKill(pos=(19009, 589), pause_on_combat=True),
            BT.Dialog(kind='npc', key='PYRE_FIERCESHOT', dialog_ids=['0x838C01']),
            BT.MoveAndKill(
                pos=[(14319, -3778), (11180, 4001), (24292, 15195)], pause_on_combat=True
            ),
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


def the_final_vision() -> BehaviorTree:
    return BT.Sequence(
        name='The Final Vision',
        children=[
            BT.Travel(target_map_id=642, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-3717, 4387), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-4596, 5017), target_map_id=646, move_tolerance=300),
            BT.MoveAndKill(pos=(-6462, 6448), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SCRYING_POOL', dialog_ids=['0x63A', '0x63C']),
            BT.Wait(duration_ms=11800),
            BT.WaitForMapLoad(map_id=646, timeout_ms=10000),
        ],
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
            BT.MoveAndKill(
                pos=[(-15630, 7992), (-14808, 8584), (-15645, 9041)], pause_on_combat=True
            ),
            BT.Wait(duration_ms=60000),
            BT.MoveAndKill(
                pos=[(-15431, 7350), (-14077, 8356), (-15203, 8677)], pause_on_combat=True
            ),
            BT.Dialog(kind='npc', key='OLAF_OLAFSON', dialog_ids=['0x832E07']),
        ],
    )


def what_lies_beneath() -> BehaviorTree:
    return BT.Sequence(
        name='What lies Beneath',
        children=[
            BT.Travel(target_map_id=55, leave_party=True),
            BT.MoveAndKill(pos=(6251, 9421), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LEN_CALDORON', dialog_ids=['0x833701']),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndKill(pos=(636, 11736), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(310, 12279), target_map_id=58, move_tolerance=300),
            BT.MoveAndKill(pos=[(10129, -11419), (8213, -9498)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='CREVASSE', dialog_ids=['0x86', '0x84']),
            BT.WaitForMapLoad(map_id=691, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(2940, 8744), (3024, 12659), (6464, 14161), (9997, 14424), (10128, 17026)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=3100),
            BT.WaitForMapLoad(map_id=691, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[
                    (4544, 15271),
                    (238, 18431),
                    (-5223, 17352),
                    (-10128, 16472),
                    (-14250, 18795),
                    (-18206, 18636),
                    (-18709, 19068),
                ],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=675, timeout_ms=10000),
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
    'against_the_destroyers_start': (
        (-3615.0, 4369.0),
        (-4547.0, 5064.0),
        (-6545.0, 6562.0),
        (-6134.0, 5830.0),
        (-5757.0, 6223.0),
        (438.0, 1333.0),
        (781.0, 1061.0),
        (2851.0, -365.0),
    ),
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
    'flames_of_the_bear_spirit': (
        (15958.0, 22933.0),
        (16690.0, 22876.0),
        (4450.0, 5881.0),
        (9551.0, -21100.0),
        (9459.0, -21539.0),
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
    'northern_allies_reward': (),
    'search_for_the_ebon_vanguard': ((-25104.0, 13667.0), (-22533.0, 13311.0), (-22051.0, 12850.0), (-9598.0, -2985.0)),
    'the_big_unfriendly_yotun': (
        (12222.0, 24571.0),
        (13360.0, 19952.0),
        (13568.0, 19423.0),
        (15058.0, 14305.0),
        (15077.0, 11936.0),
        (12191.0, 24580.0),
    ),
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
    'the_final_vision': ((-3717.0, 4387.0), (-4596.0, 5017.0), (-6462.0, 6448.0)),
    'tracking_the_nornbear': ((24014.0, -7458.0), (14297.0, 23859.0), (10413.0, 23949.0), (14356.0, 23862.0)),
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
    'what_lies_beneath': (
        (6251.0, 9421.0),
        (636.0, 11736.0),
        (310.0, 12279.0),
        (10129.0, -11419.0),
        (8213.0, -9498.0),
        (2940.0, 8744.0),
        (3024.0, 12659.0),
        (6464.0, 14161.0),
        (9997.0, 14424.0),
        (10128.0, 17026.0),
        (4544.0, 15271.0),
        (238.0, 18431.0),
        (-5223.0, 17352.0),
        (-10128.0, 16472.0),
        (-14250.0, 18795.0),
        (-18206.0, 18636.0),
        (-18709.0, 19068.0),
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
        'key': 'eotn/a_little_help',
        'title': 'A Little Help',
        'factory': 'a_little_help',
        'source_steps': 20,
        'raw_steps': 20,
    },
    {
        'kind': 'quest',
        'key': 'eotn/against_the_destroyers_start',
        'title': 'Against the Destroyers Start',
        'factory': 'against_the_destroyers_start',
        'source_steps': 18,
        'raw_steps': 18,
    },
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
        'key': 'eotn/flames_of_the_bear_spirit',
        'title': 'Flames of the Bear Spirit',
        'factory': 'flames_of_the_bear_spirit',
        'source_steps': 12,
        'raw_steps': 12,
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
        'key': 'eotn/northern_allies_reward',
        'title': 'Northern Allies Reward',
        'factory': 'northern_allies_reward',
        'source_steps': 1,
        'raw_steps': 1,
    },
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
        'key': 'eotn/the_big_unfriendly_yotun',
        'title': 'The Big Unfriendly Yotun',
        'factory': 'the_big_unfriendly_yotun',
        'source_steps': 10,
        'raw_steps': 10,
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
        'key': 'eotn/the_final_vision',
        'title': 'The Final Vision',
        'factory': 'the_final_vision',
        'source_steps': 8,
        'raw_steps': 8,
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
        'key': 'eotn/vision_of_the_raven_spirit',
        'title': 'Vision of the Raven Spirit',
        'factory': 'vision_of_the_raven_spirit',
        'source_steps': 12,
        'raw_steps': 12,
    },
    {
        'kind': 'quest',
        'key': 'eotn/what_lies_beneath',
        'title': 'What lies Beneath',
        'factory': 'what_lies_beneath',
        'source_steps': 14,
        'raw_steps': 14,
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
