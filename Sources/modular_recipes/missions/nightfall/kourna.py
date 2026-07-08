"""Missions Nightfall Kourna BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def kodonur_crossroads() -> BehaviorTree:
    return BT.Sequence(
        name='Kodonur Crossroads',
        children=[
            BT.Travel(target_map_id=424, leave_party=True),
            BT.MoveAndKill(pos=(-873, 2639), pause_on_combat=True),
            BT.LoadParty(max_heroes=8, required_hero=['Zhed Shadowhoof']),
            BT.Dialog(kind='npc', key='ESTATE_GUARD_RIKESH', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=10000),
            BT.WaitForMapLoad(map_id=424, timeout_ms=10000),
            BT.Wait(duration_ms=80000),
            BT.MoveAndKill(pos=(-14413, -2183), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.MoveAndKill(pos=[(-14002, 4376), (-12771, 5943)], pause_on_combat=True),
            BT.MoveAndKill(pos=(-12140, 7992), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-14020, 4491), pause_on_combat=True),
            BT.Interact(kind='gadget', key='CELL_LOCK', pos=(-14282, 4269)),
            BT.Interact(kind='gadget', key='CELL_LOCK', pos=(-14521, 4928)),
            BT.MoveAndKill(pos=(-12382, 10589), pause_on_combat=True),
            BT.MoveAndKill(pos=(-11678, 11911), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-8992, 14803), pause_on_combat=True),
            BT.MoveAndKill(pos=(-8314, 16370), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.MoveAndKill(pos=(-14049, 13440), pause_on_combat=True),
            BT.Interact(kind='gadget', key='CELL_LOCK', pos=(-14667, 13701)),
            BT.MoveAndKill(pos=[(-8308, 15648), (-4176, 16628)], pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.MoveAndKill(pos=[(-4172, 16305), (-1250, 10408)], pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.MoveAndKill(pos=[(-1722, 7317), (1958, 7730)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(313, -1975), (4791, -1569)], pause_on_combat=True),
            BT.MoveAndKill(pos=(-2714, 6739), pause_on_combat=True),
            BT.Interact(kind='gadget', key='CELL_LOCK', pos=(-2558, 6562)),
            BT.MoveAndKill(
                pos=[(-5777, 7581), (-5896, 9824), (-7105, 8832), (-6112, 10014)],
                pause_on_combat=True,
            ),
            BT.Interact(kind='gadget', key='CELL_LOCK', pos=(-6102, 10345)),
            BT.MoveAndKill(
                pos=[(-1469, 2632), (-5163, 7302), (-5835, 5124)], pause_on_combat=True
            ),
            BT.MoveAndKill(pos=(-6694, 3685), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15565, point=None, max_dist=4500),
            BT.MoveAndKill(pos=[(-9904, 3443), (-10308, 1339)], pause_on_combat=True),
            BT.Interact(kind='gadget', key='CELL_LOCK', pos=(-10040, 964)),
            BT.MoveAndKill(
                pos=[(-11745, 2603), (-9608, -1336), (-9696, -3720), (-8136, -5813)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(-6159, -7421), (-7791, 374), (-6106, -799)], pause_on_combat=True
            ),
            BT.Wait(duration_ms=3000),
            BT.WaitForMapLoad(map_id=387, timeout_ms=10000),
        ],
    )


def moddock_crevice() -> BehaviorTree:
    return BT.Sequence(
        name='Moddok Crevice',
        children=[
            BT.Travel(target_map_id=427, leave_party=True),
            BT.MoveAndKill(pos=(-13781, -12741), pause_on_combat=True),
            BT.LoadParty(max_heroes=8, required_hero=['Dunkoro']),
            BT.Dialog(kind='npc', key='UNLUCKY_SIMON', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=7500),
            BT.WaitForMapLoad(map_id=427, timeout_ms=10000),
            BT.MoveAndKill(pos=(-9348, -7283), pause_on_combat=True),
            BT.Wait(duration_ms=62500),
            BT.Dialog(kind='npc', key='CAPTAIN_BOHSEDA', dialog_ids=['0x85']),
            BT.MoveAndKill(
                pos=[
                    (-7623, -6494),
                    (-7658, -1379),
                    (-9414, -1777),
                    (-8084, -610),
                    (-7361, 1049),
                    (-8134, -925),
                    (-9470, -1767),
                ],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=74500),
            BT.MoveAndKill(
                pos=[(-7387, 1161), (-12409, -140), (-10183, 4382)], pause_on_combat=True
            ),
            BT.Wait(duration_ms=14800),
            BT.MoveAndKill(pos=[(-9887, 4356), (-6836, 5123)], pause_on_combat=True),
            BT.MoveAndKill(
                pos=[(-5530, 9781), (-7930, 13807), (-11567, 10159)], pause_on_combat=True
            ),
            BT.MoveAndKill(pos=(-11007, 12443), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=427, timeout_ms=10000),
            BT.FlagAllHeroes(-12653, 15023),
            BT.MoveAndKill(pos=(-12653, 15023), pause_on_combat=True),
            BT.UnflagAllHeroes(),
            BT.Wait(duration_ms=32900),
            BT.WaitForMapLoad(map_id=378, timeout_ms=10000),
        ],
    )


def nundu_bay() -> BehaviorTree:
    return BT.Sequence(
        name='Nundu Bay',
        children=[
            BT.Travel(target_map_id=477, leave_party=True),
            BT.LoadParty(max_heroes=8, required_hero=['Melonni']),
            BT.MoveAndKill(pos=(-15809, -7668), pause_on_combat=True),
            BT.Dialog(kind='npc', key='DREAMER_RAJA', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=7000),
            BT.WaitForMapLoad(map_id=477, timeout_ms=10000),
            BT.MoveAndKill(pos=(8356, 12851), pause_on_combat=True),
            BT.Wait(duration_ms=60000),
            BT.Dialog(kind='npc', key='ELDER_JONAH', dialog_ids=['0x1']),
            BT.MoveAndKill(
                pos=[
                    (4623, 12080),
                    (2368, 10290),
                    (3400, 8547),
                    (1477, 6492),
                    (-443, 5369),
                    (-943, 1143),
                    (-2299, -527),
                    (-2199, 1292),
                    (-2785, 5242),
                ],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=387, timeout_ms=10000),
        ],
    )


def rihlon_refuge() -> BehaviorTree:
    return BT.Sequence(
        name='Rilohn Refuge',
        children=[
            BT.Travel(target_map_id=425, leave_party=True),
            BT.MoveAndKill(pos=(-15846, 11178), pause_on_combat=True),
            BT.LoadParty(max_heroes=8, required_hero=['Master of Whispers']),
            BT.Dialog(kind='npc', key='DEHJAH', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=13200),
            BT.WaitForMapLoad(map_id=425, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-14090, 4570), (-15456, 496), (-13489, -3934), (-11266, -6473), (-8278, -4390), (-7576, 777)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=25800),
            BT.MoveAndKill(
                pos=[(-5150, 330), (-1800, -585), (-531, 1193)], pause_on_combat=True
            ),
            BT.Wait(duration_ms=24300),
            BT.MoveAndKill(
                pos=[(2464, 366), (2652, 4477), (5670, 3369), (6799, 4647)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=32600),
            BT.MoveAndKill(pos=(8341, 6225), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=427, timeout_ms=10000),
        ],
    )


def venta_cemetery() -> BehaviorTree:
    return BT.Sequence(
        name='Venta Cemetery',
        children=[
            BT.Travel(target_map_id=421, leave_party=True),
            BT.MoveAndKill(pos=(25351, 14922), pause_on_combat=True),
            BT.LoadParty(max_heroes=8, required_hero=['Koss']),
            BT.Dialog(kind='npc', key='ROJIS', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=6400),
            BT.WaitForMapLoad(map_id=421, timeout_ms=10000),
            BT.MoveAndKill(pos=(21776, 13123), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ROJIS', dialog_ids=['0x84']),
            BT.MoveAndKill(pos=[(21167, 12587), (19473, 5603)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(17641, -633), (17402, -2474)], pause_on_combat=True),
            BT.MoveAndKill(
                pos=[(17523, 514), (13107, 4879), (7600, 4950)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(6248, 8055), (6845, 10454), (7053, 11647), (5526, 11607)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(3087, 14262), (70, 13740), (-1435, 12151)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-4956, 12396), (-10078, 9400), (-8936, 8168), (-14375, 8009)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(-8985, 7473), (-5935, 7968), (-4058, 6947)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-6641, 8067), (-7720, 5809), (-7353, 3132)], pause_on_combat=True
            ),
            BT.MoveAndKill(
                pos=[(-9455, 6759), (-12164, 6240), (-12069, 2023), (-12292, -404)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(-11070, -4148), (-10580, -6933), (-8705, -5624), (-7616, -5386)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(-6123, -7131), (-3420, -9428), (-2292, -9912)], pause_on_combat=True
            ),
            BT.MoveAndKill(pos=[(1343, -11903), (3617, -10774)], pause_on_combat=True),
            BT.MoveAndKill(
                pos=[(-1021, -10991), (-4580, -8381), (-10190, -7394)], pause_on_combat=True
            ),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(
                pos=[(-15439, -7585), (-17060, -8484), (-21180, -8247), (-22540, -8289)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=11200),
            BT.Interact(kind='npc', key='MARGRID_THE_SLY'),
            BT.WaitForMapLoad(map_id=449, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'kodonur_crossroads': (
        (-873.0, 2639.0),
        (-14413.0, -2183.0),
        (-14002.0, 4376.0),
        (-12771.0, 5943.0),
        (-12140.0, 7992.0),
        (-14020.0, 4491.0),
        (-12382.0, 10589.0),
        (-11678.0, 11911.0),
        (-8992.0, 14803.0),
        (-8314.0, 16370.0),
        (-14049.0, 13440.0),
        (-8308.0, 15648.0),
        (-4176.0, 16628.0),
        (-4172.0, 16305.0),
        (-1250.0, 10408.0),
        (-1722.0, 7317.0),
        (1958.0, 7730.0),
        (313.0, -1975.0),
        (4791.0, -1569.0),
        (-2714.0, 6739.0),
        (-5777.0, 7581.0),
        (-5896.0, 9824.0),
        (-7105.0, 8832.0),
        (-6112.0, 10014.0),
        (-1469.0, 2632.0),
        (-5163.0, 7302.0),
        (-5835.0, 5124.0),
        (-6694.0, 3685.0),
        (-9904.0, 3443.0),
        (-10308.0, 1339.0),
        (-11745.0, 2603.0),
        (-9608.0, -1336.0),
        (-9696.0, -3720.0),
        (-8136.0, -5813.0),
        (-6159.0, -7421.0),
        (-7791.0, 374.0),
        (-6106.0, -799.0),
    ),
    'moddock_crevice': (
        (-13781.0, -12741.0),
        (-9348.0, -7283.0),
        (-7623.0, -6494.0),
        (-7658.0, -1379.0),
        (-9414.0, -1777.0),
        (-8084.0, -610.0),
        (-7361.0, 1049.0),
        (-8134.0, -925.0),
        (-9470.0, -1767.0),
        (-7387.0, 1161.0),
        (-12409.0, -140.0),
        (-10183.0, 4382.0),
        (-9887.0, 4356.0),
        (-6836.0, 5123.0),
        (-5530.0, 9781.0),
        (-7930.0, 13807.0),
        (-11567.0, 10159.0),
        (-11007.0, 12443.0),
        (-12653.0, 15023.0),
    ),
    'nundu_bay': (
        (-15809.0, -7668.0),
        (8356.0, 12851.0),
        (4623.0, 12080.0),
        (2368.0, 10290.0),
        (3400.0, 8547.0),
        (1477.0, 6492.0),
        (-443.0, 5369.0),
        (-943.0, 1143.0),
        (-2299.0, -527.0),
        (-2199.0, 1292.0),
        (-2785.0, 5242.0),
    ),
    'rihlon_refuge': (
        (-15846.0, 11178.0),
        (-14090.0, 4570.0),
        (-15456.0, 496.0),
        (-13489.0, -3934.0),
        (-11266.0, -6473.0),
        (-8278.0, -4390.0),
        (-7576.0, 777.0),
        (-5150.0, 330.0),
        (-1800.0, -585.0),
        (-531.0, 1193.0),
        (2464.0, 366.0),
        (2652.0, 4477.0),
        (5670.0, 3369.0),
        (6799.0, 4647.0),
        (8341.0, 6225.0),
    ),
    'venta_cemetery': (
        (25351.0, 14922.0),
        (21776.0, 13123.0),
        (21167.0, 12587.0),
        (19473.0, 5603.0),
        (17641.0, -633.0),
        (17402.0, -2474.0),
        (17523.0, 514.0),
        (13107.0, 4879.0),
        (7600.0, 4950.0),
        (6248.0, 8055.0),
        (6845.0, 10454.0),
        (7053.0, 11647.0),
        (5526.0, 11607.0),
        (3087.0, 14262.0),
        (70.0, 13740.0),
        (-1435.0, 12151.0),
        (-4956.0, 12396.0),
        (-10078.0, 9400.0),
        (-8936.0, 8168.0),
        (-14375.0, 8009.0),
        (-8985.0, 7473.0),
        (-5935.0, 7968.0),
        (-4058.0, 6947.0),
        (-6641.0, 8067.0),
        (-7720.0, 5809.0),
        (-7353.0, 3132.0),
        (-9455.0, 6759.0),
        (-12164.0, 6240.0),
        (-12069.0, 2023.0),
        (-12292.0, -404.0),
        (-11070.0, -4148.0),
        (-10580.0, -6933.0),
        (-8705.0, -5624.0),
        (-7616.0, -5386.0),
        (-6123.0, -7131.0),
        (-3420.0, -9428.0),
        (-2292.0, -9912.0),
        (1343.0, -11903.0),
        (3617.0, -10774.0),
        (-1021.0, -10991.0),
        (-4580.0, -8381.0),
        (-10190.0, -7394.0),
        (-15439.0, -7585.0),
        (-17060.0, -8484.0),
        (-21180.0, -8247.0),
        (-22540.0, -8289.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'nightfall/kodonur_crossroads',
        'title': 'Kodonur Crossroads',
        'factory': 'kodonur_crossroads',
        'source_steps': 43,
        'raw_steps': 43,
    },
    {
        'kind': 'mission',
        'key': 'nightfall/moddock_crevice',
        'title': 'Moddok Crevice',
        'factory': 'moddock_crevice',
        'source_steps': 22,
        'raw_steps': 22,
    },
    {
        'kind': 'mission',
        'key': 'nightfall/nundu_bay',
        'title': 'Nundu Bay',
        'factory': 'nundu_bay',
        'source_steps': 11,
        'raw_steps': 11,
    },
    {
        'kind': 'mission',
        'key': 'nightfall/rihlon_refuge',
        'title': 'Rilohn Refuge',
        'factory': 'rihlon_refuge',
        'source_steps': 14,
        'raw_steps': 14,
    },
    {
        'kind': 'mission',
        'key': 'nightfall/venta_cemetery',
        'title': 'Venta Cemetery',
        'factory': 'venta_cemetery',
        'source_steps': 26,
        'raw_steps': 26,
    },
)
