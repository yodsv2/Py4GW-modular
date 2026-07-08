"""Quests Fow Fissure Of Woe BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def army_of_darkness() -> BehaviorTree:
    return BT.Sequence(
        name='Army of Darkness',
        children=[
            BT.MoveAndKill(pos=(2361, 14877), pause_on_combat=True),
            BT.MoveAndKill(pos=(4200, 15193), pause_on_combat=True),
            BT.Interact(kind='item'),
            BT.MoveAndKill(pos=(2482, 14749), pause_on_combat=True),
            BT.Interact(kind='item'),
            BT.MoveAndKill(pos=(1184, 15347), pause_on_combat=True),
            BT.Interact(kind='item'),
            BT.MoveAndKill(pos=(-762, 11836), pause_on_combat=True),
            BT.MoveAndKill(pos=(-7154, 11644), pause_on_combat=True),
            BT.Dialog(pos=(-7382, 11942), dialog_ids=['0x80CB07']),
        ],
    )


def defend_the_temple() -> BehaviorTree:
    return BT.Sequence(
        name='Defend the Temple',
        children=[
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80CA01']),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80CA01']),
            BT.SendChatCommand(command='stuck'),
            BT.MoveAndKill(pos=[(1853, 2303), (1412, -884)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(1755, -2670), (1922, -2937)], pause_on_combat=True),
            BT.MoveAndKill(pos=(1840, -179), pause_on_combat=True),
            BT.Wait(duration_ms=2000),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80CA07']),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80CA07']),
            BT.SendChatCommand(command='stuck'),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80E003', '0x80E001']),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80CF03', '0x80CF01']),
            BT.SendChatCommand(command='stuck'),
            BT.Interact(kind='gadget', key='CHEST'),
            BT.Interact(kind='gadget', key='CHEST'),
            BT.MoveAndKill(pos=(265, -1966), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ETERNAL_LORD_TAERES', dialog_ids=['0x80D301']),
            BT.Dialog(kind='npc', key='ETERNAL_LORD_TAERES', dialog_ids=['0x80D301']),
        ],
    )


def eternal_forgemaster() -> BehaviorTree:
    return BT.Sequence(
        name='Eternal Forgemaster',
        children=[
            BT.MoveAndKill(
                pos=[
                    (-15127, -2036),
                    (-9092, -6192),
                    (-4615, 2965),
                    (-9907, 6948),
                    (-3023, 9966),
                    (-6595, 13499),
                    (-6913, 10067),
                    (-7280, 11820),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='ETERNAL_WEAPONSMITH', dialog_ids=['0x80D101']),
            BT.Dialog(kind='npc', key='KROMRIL_THE_ETERNAL', dialog_ids=['0x80CB01']),
            BT.MoveAndKill(pos=(-7280, 11820), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ETERNAL_WEAPONSMITH', dialog_ids=['0x80D101']),
            BT.Dialog(kind='npc', key='KROMRIL_THE_ETERNAL', dialog_ids=['0x80CB01']),
            BT.MoveAndKill(
                pos=[(-4677, 12072), (-301, 13675), (-929, 6405), (1725, 3037)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[
                    (2837, 1757),
                    (4273, -19),
                    (2427, -2889),
                    (-864, -1054),
                    (909, 2064),
                    (3429, 1247),
                    (1542, 51),
                    (1862, -152),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80D107']),
            BT.MoveAndKill(pos=(1862, -152), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80D107']),
        ],
    )


def gift_of_griffons() -> BehaviorTree:
    return BT.Sequence(
        name='Gift of Griffons',
        children=[
            BT.MoveAndKill(
                pos=[(-21448, 15704), (-21291, 14579), (-22434, 14498)], pause_on_combat=True
            ),
            BT.Dialog(kind='npc', key='WAILING_LORD', dialog_ids=['0x80CD01']),
            BT.MoveAndKill(pos=(-22434, 14498), pause_on_combat=True),
            BT.Dialog(kind='npc', key='WAILING_LORD', dialog_ids=['0x80CD01']),
            BT.Interact(kind='gadget', key='CHEST'),
            BT.MoveAndKill(pos=(-22414, 10332), pause_on_combat=True),
            BT.MoveAndKill(
                pos=[
                    (-21581, 9833),
                    (-16464, 9013),
                    (-12956, 6918),
                    (-7304, 5782),
                    (-6884, 3818),
                    (-5846, 1027),
                    (-6697, -2132),
                    (-6493, -3923),
                    (-9330, -5987),
                    (-8542, -4384),
                    (-15905, -1381),
                ],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=5000),
            BT.Dialog(kind='npc', key='RASTIGAN_THE_ETERNAL', dialog_ids=['0x80CC06', '0x80CC07', '0x80CD07']),
            BT.Interact(kind='gadget', key='CHEST'),
            BT.Dialog(kind='npc', key='RASTIGAN_THE_ETERNAL', dialog_ids=['0x80CC06', '0x80CC07', '0x80CD07']),
            BT.MoveAndKill(pos=(-16695, -3375), pause_on_combat=True),
            BT.MoveAndKill(pos=[(-17183, -2958), (-14207, -2778)], pause_on_combat=True),
        ],
    )


def khobay() -> BehaviorTree:
    return BT.Sequence(
        name='Traitor Khobay',
        children=[
            BT.EnemyBlacklist(enemy='Infernal Wurm', mode='remove'),
            BT.MoveAndKill(pos=(18834, -8963), pause_on_combat=True),
            BT.MoveAndKill(pos=(19668, -15397), pause_on_combat=True),
            BT.EnemyBlacklist(enemy='Infernal Wurm', mode='add'),
            BT.FlagAllHeroes(19909, -12109),
            BT.Wait(duration_ms=3000),
            BT.MoveAndKill(pos=(19909, -12109), pause_on_combat=True),
            BT.UnflagAllHeroes(),
            BT.MoveAndKill(pos=(11665, -8820), pause_on_combat=True),
            BT.EnemyBlacklist(enemy='Infernal Wurm', mode='remove'),
        ],
    )


def restore_the_temple() -> BehaviorTree:
    return BT.Sequence(
        name='Restore the Temple',
        children=[
            BT.MoveAndKill(pos=(2766, -14730), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NIMROS_THE_HUNTER', dialog_ids=['0x80D001']),
            BT.MoveAndKill(pos=(2766, -14730), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NIMROS_THE_HUNTER', dialog_ids=['0x80D001']),
            BT.MoveAndKill(pos=(-9126, -18554), pause_on_combat=True),
            BT.MoveAndKill(pos=(-11222, -18382), pause_on_combat=True),
            BT.MoveAndKill(pos=(1749, -6954), pause_on_combat=True),
        ],
    )


def reward_time() -> BehaviorTree:
    return BT.Sequence(
        name='Reward Time',
        children=[
            BT.MoveAndKill(
                pos=[
                    (-12332, -3539),
                    (-9712, -4812),
                    (-6595, -3453),
                    (-4494, 3700),
                    (1752, 5342),
                    (266, 1273),
                    (1857, 215),
                ],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=5000),
            BT.Interact(kind='gadget', key='CHEST_OF_WOE'),
            BT.MoveAndKill(pos=(1869, 260), pause_on_combat=True),
            BT.Interact(kind='gadget', key='CHEST_OF_WOE'),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80CF06', '0x80CF07', '0x80E007']),
            BT.MoveAndKill(pos=(1869, 260), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ETERNAL_FORGEMASTER', dialog_ids=['0x80CF06', '0x80CF07', '0x80E007']),
            BT.Wait(duration_ms=5000),
            BT.Interact(kind='gadget', key='CHEST', pos=(1624, -540)),
            BT.MoveAndKill(pos=(1865, 216), pause_on_combat=True),
            BT.Resign(),
            BT.Wait(duration_ms=15000),
        ],
    )


def slaves_of_menzies() -> BehaviorTree:
    return BT.Sequence(
        name='Slaves of Menzies',
        children=[
            BT.MoveAndKill(pos=(12009, 6356), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MIKO_THE_UNCHAINED', dialog_ids=['0x80CE01']),
            BT.MoveAndKill(pos=(12009, 6356), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MIKO_THE_UNCHAINED', dialog_ids=['0x80CE01']),
            BT.MoveAndKill(pos=[(19000, 8400), (21462, 11027)], pause_on_combat=True),
            BT.MoveAndKill(pos=(22946, 12727), pause_on_combat=True),
            BT.MoveAndKill(pos=[(20900, 15900), (22511, 16038)], pause_on_combat=True),
            BT.MoveAndKill(pos=(19240, 12803), pause_on_combat=True),
            BT.MoveAndKill(
                pos=[(13611, 9281), (12122, 8326), (12157, 6555)], pause_on_combat=True
            ),
            BT.Dialog(kind='npc', key='MIKO_THE_UNCHAINED', dialog_ids=['0x80CE07']),
            BT.MoveAndKill(pos=(12157, 6555), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MIKO_THE_UNCHAINED', dialog_ids=['0x80CE07']),
            BT.MoveAndKill(pos=[(10830, 10524), (8682, 12324)], pause_on_combat=True),
        ],
    )


def tower_of_courage() -> BehaviorTree:
    return BT.Sequence(
        name='Tower of Courage',
        children=[
            BT.MoveAndKill(
                pos=[
                    (-21068, 1542),
                    (-19238, 370),
                    (-20026, -2707),
                    (-21051, -3053),
                    (-17447, -4380),
                    (-14187, -718),
                    (-14596, -2576),
                ],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=(-15479, -1824), pause_on_combat=True),
            BT.Wait(duration_ms=5000),
            BT.Dialog(kind='npc', key='RASTIGAN_THE_ETERNAL', dialog_ids=['0x80D401', '0x80D407', '0x80CC01']),
            BT.MoveAndKill(pos=(-15479, -1824), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RASTIGAN_THE_ETERNAL', dialog_ids=['0x80D401', '0x80D407', '0x80CC01']),
            BT.Interact(kind='gadget', key='CHEST'),
        ],
    )


def tower_of_strength() -> BehaviorTree:
    return BT.Sequence(
        name='Tower of Strength',
        children=[
            BT.MoveAndKill(
                pos=[(11077, -5531), (12993, -4084), (15425, -1647), (17165, 930), (14415, -893)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=[(13241, -4485), (1770, -4690)], pause_on_combat=True),
            BT.MoveAndKill(
                pos=[(11062, -5421), (14169, -3101), (15635, -1324)], pause_on_combat=True
            ),
            BT.MoveAndKill(pos=[(13440, -738), (16729, -1837)], pause_on_combat=True),
            BT.Wait(duration_ms=5000),
        ],
    )


def wailing_lord() -> BehaviorTree:
    return BT.Sequence(
        name='Wailing lord',
        children=[
            BT.MoveAndKill(pos=(-11294, 15897), pause_on_combat=True),
            BT.EnemyBlacklist(enemy='Wailing Lord', mode='add'),
            BT.MoveAndKill(
                pos=[(-12225, 13500), (-13011, 12108), (-14922, 12513)], pause_on_combat=True
            ),
            BT.MoveAndKill(pos=(-21254, 14651), pause_on_combat=True),
            BT.MoveAndKill(
                pos=[(-19021, 11061), (-20432, 12077), (-19924, 9299), (-17795, 9806), (-14996, 8168)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(-18459, 9629), (-20705, 10996), (-21385, 15152)], pause_on_combat=True
            ),
            BT.Interact(kind='gadget', key='CHEST'),
            BT.Interact(kind='gadget', key='CHEST'),
            BT.EnemyBlacklist(enemy='Wailing Lord', mode='remove'),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'army_of_darkness': (
        (2361.0, 14877.0),
        (4200.0, 15193.0),
        (2482.0, 14749.0),
        (1184.0, 15347.0),
        (-762.0, 11836.0),
        (-7154.0, 11644.0),
    ),
    'defend_the_temple': (
        (1853.0, 2303.0),
        (1412.0, -884.0),
        (1755.0, -2670.0),
        (1922.0, -2937.0),
        (1840.0, -179.0),
        (265.0, -1966.0),
    ),
    'eternal_forgemaster': (
        (-15127.0, -2036.0),
        (-9092.0, -6192.0),
        (-4615.0, 2965.0),
        (-9907.0, 6948.0),
        (-3023.0, 9966.0),
        (-6595.0, 13499.0),
        (-6913.0, 10067.0),
        (-7280.0, 11820.0),
        (-7280.0, 11820.0),
        (-4677.0, 12072.0),
        (-301.0, 13675.0),
        (-929.0, 6405.0),
        (1725.0, 3037.0),
        (2837.0, 1757.0),
        (4273.0, -19.0),
        (2427.0, -2889.0),
        (-864.0, -1054.0),
        (909.0, 2064.0),
        (3429.0, 1247.0),
        (1542.0, 51.0),
        (1862.0, -152.0),
        (1862.0, -152.0),
    ),
    'gift_of_griffons': (
        (-21448.0, 15704.0),
        (-21291.0, 14579.0),
        (-22434.0, 14498.0),
        (-22434.0, 14498.0),
        (-22414.0, 10332.0),
        (-21581.0, 9833.0),
        (-16464.0, 9013.0),
        (-12956.0, 6918.0),
        (-7304.0, 5782.0),
        (-6884.0, 3818.0),
        (-5846.0, 1027.0),
        (-6697.0, -2132.0),
        (-6493.0, -3923.0),
        (-9330.0, -5987.0),
        (-8542.0, -4384.0),
        (-15905.0, -1381.0),
        (-16695.0, -3375.0),
        (-17183.0, -2958.0),
        (-14207.0, -2778.0),
    ),
    'khobay': ((18834.0, -8963.0), (19668.0, -15397.0), (19909.0, -12109.0), (11665.0, -8820.0)),
    'restore_the_temple': (
        (2766.0, -14730.0),
        (2766.0, -14730.0),
        (-9126.0, -18554.0),
        (-11222.0, -18382.0),
        (1749.0, -6954.0),
    ),
    'reward_time': (
        (-12332.0, -3539.0),
        (-9712.0, -4812.0),
        (-6595.0, -3453.0),
        (-4494.0, 3700.0),
        (1752.0, 5342.0),
        (266.0, 1273.0),
        (1857.0, 215.0),
        (1869.0, 260.0),
        (1869.0, 260.0),
        (1865.0, 216.0),
    ),
    'slaves_of_menzies': (
        (12009.0, 6356.0),
        (12009.0, 6356.0),
        (19000.0, 8400.0),
        (21462.0, 11027.0),
        (22946.0, 12727.0),
        (20900.0, 15900.0),
        (22511.0, 16038.0),
        (19240.0, 12803.0),
        (13611.0, 9281.0),
        (12122.0, 8326.0),
        (12157.0, 6555.0),
        (12157.0, 6555.0),
        (10830.0, 10524.0),
        (8682.0, 12324.0),
    ),
    'tower_of_courage': (
        (-21068.0, 1542.0),
        (-19238.0, 370.0),
        (-20026.0, -2707.0),
        (-21051.0, -3053.0),
        (-17447.0, -4380.0),
        (-14187.0, -718.0),
        (-14596.0, -2576.0),
        (-15479.0, -1824.0),
        (-15479.0, -1824.0),
    ),
    'tower_of_strength': (
        (11077.0, -5531.0),
        (12993.0, -4084.0),
        (15425.0, -1647.0),
        (17165.0, 930.0),
        (14415.0, -893.0),
        (13241.0, -4485.0),
        (1770.0, -4690.0),
        (11062.0, -5421.0),
        (14169.0, -3101.0),
        (15635.0, -1324.0),
        (13440.0, -738.0),
        (16729.0, -1837.0),
    ),
    'wailing_lord': (
        (-11294.0, 15897.0),
        (-12225.0, 13500.0),
        (-13011.0, 12108.0),
        (-14922.0, 12513.0),
        (-21254.0, 14651.0),
        (-19021.0, 11061.0),
        (-20432.0, 12077.0),
        (-19924.0, 9299.0),
        (-17795.0, 9806.0),
        (-14996.0, 8168.0),
        (-18459.0, 9629.0),
        (-20705.0, 10996.0),
        (-21385.0, 15152.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'fow/army_of_darkness',
        'title': 'Army of Darkness',
        'factory': 'army_of_darkness',
        'source_steps': 10,
        'raw_steps': 10,
    },
    {
        'kind': 'quest',
        'key': 'fow/defend_the_temple',
        'title': 'Defend the Temple',
        'factory': 'defend_the_temple',
        'source_steps': 17,
        'raw_steps': 16,
    },
    {
        'kind': 'quest',
        'key': 'fow/eternal_forgemaster',
        'title': 'Eternal Forgemaster',
        'factory': 'eternal_forgemaster',
        'source_steps': 11,
        'raw_steps': 11,
    },
    {
        'kind': 'quest',
        'key': 'fow/gift_of_griffons',
        'title': 'Gift of Griffons',
        'factory': 'gift_of_griffons',
        'source_steps': 13,
        'raw_steps': 13,
    },
    {
        'kind': 'quest',
        'key': 'fow/khobay',
        'title': 'Traitor Khobay',
        'factory': 'khobay',
        'source_steps': 9,
        'raw_steps': 9,
    },
    {
        'kind': 'quest',
        'key': 'fow/restore_the_temple',
        'title': 'Restore the Temple',
        'factory': 'restore_the_temple',
        'source_steps': 7,
        'raw_steps': 7,
    },
    {
        'kind': 'quest',
        'key': 'fow/reward_time',
        'title': 'Reward Time',
        'factory': 'reward_time',
        'source_steps': 12,
        'raw_steps': 12,
    },
    {
        'kind': 'quest',
        'key': 'fow/slaves_of_menzies',
        'title': 'Slaves of Menzies',
        'factory': 'slaves_of_menzies',
        'source_steps': 13,
        'raw_steps': 13,
    },
    {
        'kind': 'quest',
        'key': 'fow/tower_of_courage',
        'title': 'Tower of Courage',
        'factory': 'tower_of_courage',
        'source_steps': 7,
        'raw_steps': 7,
    },
    {
        'kind': 'quest',
        'key': 'fow/tower_of_strength',
        'title': 'Tower of Strength',
        'factory': 'tower_of_strength',
        'source_steps': 4,
        'raw_steps': 4,
    },
    {
        'kind': 'quest',
        'key': 'fow/wailing_lord',
        'title': 'Wailing lord',
        'factory': 'wailing_lord',
        'source_steps': 9,
        'raw_steps': 8,
    },
)
