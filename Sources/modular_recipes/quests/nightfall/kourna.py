"""Quests Nightfall Kourna BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def hunted() -> BehaviorTree:
    return BT.Sequence(
        name='Hunted!',
        children=[
            BT.Travel(target_map_id=381, leave_party=True),
            BT.MoveAndKill(pos=(2095, 307), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SUNSPEAR_MODIKI', dialog_ids=['0x84', '0x85', '0x86', '0x822401']),
            BT.MoveAndKill(pos=(-976, 1524), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ZUDASH_DEJARIN', dialog_ids=['0x822404']),
            BT.MoveAndKill(pos=(-3765, 4583), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(-5001, 4859), target_map_id=371, move_tolerance=300),
            BT.MoveAndKill(pos=(8252, 12668), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_JONAH', dialog_ids=['0x822404']),
            BT.MoveAndKill(pos=(8252, 12668), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_JONAH', dialog_ids=['0x822404']),
            BT.MoveAndKill(pos=(11927, 14638), pause_on_combat=True),
            BT.Interact(kind='npc', key='GUARDSMAN_BAHSI'),
            BT.MoveAndExitMap(pos=(12858, 14874), target_map_id=420, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(1402, -1952), (2870, 1221), (-567, 810), (-3804, 1821), (-3432, -2436)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=387, timeout_ms=2000),
            BT.Wait(duration_ms=2000),
            BT.MoveAndKill(pos=(-840, 1572), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LONAI', dialog_ids=['0x822407']),
        ],
    )


def the_great_escape() -> BehaviorTree:
    return BT.Sequence(
        name='The Great Escape',
        children=[
            BT.Travel(target_map_id=387, leave_party=True),
            BT.MoveAndKill(pos=(-753, 1588), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LONAI', dialog_ids=['0x822503', '0x822501']),
            BT.MoveAndKill(pos=(-961, 2690), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(-480, 3913), target_map_id=436, move_tolerance=300),
            BT.MoveAndKill(pos=(3689, 4609), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(5032, 3847), target_map_id=380, move_tolerance=300),
            BT.MoveAndKill(pos=(-14185, 13346), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NERASHI', dialog_ids=['0x822504']),
            BT.MoveAndKill(
                pos=[
                    (-6844, 8329),
                    (7287, 1842),
                    (5769, -8954),
                    (9590, -1760),
                    (12850, -3249),
                    (11435, -6714),
                    (11273, -11690),
                    (8873, -11517),
                    (9799, -10868),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='KOSS', dialog_ids=['0x822504']),
            BT.MoveAndKill(pos=[(12518, -13342), (19975, -19365)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(20686, -20173), target_map_id=426, move_tolerance=300),
            BT.Travel(target_map_id=387, leave_party=True),
            BT.MoveAndKill(pos=(-789, 1596), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LONAI', dialog_ids=['0x822507']),
        ],
    )


def and_a_hero_shall_lead_them() -> BehaviorTree:
    return BT.Sequence(
        name='And a Hero Shall Lead Them',
        children=[
            BT.Travel(target_map_id=387, leave_party=True),
            BT.MoveAndKill(pos=(-755, 1625), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LONAI', dialog_ids=['0x822603', '0x822601']),
            BT.MoveAndKill(pos=(-937, 2921), pause_on_combat=True),
            BT.LoadParty(max_heroes=8, required_hero=['Koss']),
            BT.MoveAndExitMap(pos=(-480, 3916), target_map_id=436, move_tolerance=300),
            BT.MoveAndKill(pos=(-2716, 8121), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-3393, 9260), target_map_id=373, move_tolerance=300),
            BT.MoveAndKill(pos=(21494, 13243), pause_on_combat=True),
            BT.Dialog(kind='npc', key='COMMANDER_SUHA', dialog_ids=['0x84', '0x85']),
            BT.WaitForMapLoad(map_id=421, timeout_ms=10000),
            BT.MoveAndKill(pos=(25434, 14990), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ROJIS', dialog_ids=['0x822607']),
        ],
    )


def the_council_is_called() -> BehaviorTree:
    return BT.Sequence(
        name='The Council is Called',
        children=[
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=[(-8151, 9111), (-4625, 10059)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='DOCKMASTER_AHLARO', dialog_ids=['0x81EA01']),
            BT.MoveAndKill(pos=[(-8152, 9342), (-6780, 16693)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-5928, 16758), target_map_id=429, move_tolerance=300),
            BT.MoveAndKill(pos=[(-5187, 16716), (-4707, 16582)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_DAHUT', dialog_ids=['0x81EA04']),
            BT.MoveAndKill(pos=[(-5187, 16716), (-4664, 16850)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_NAHLO', dialog_ids=['0x81EA04']),
            BT.MoveAndKill(pos=[(-5187, 16716), (-4374, 16819)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_SUHL', dialog_ids=['0x81EA04']),
            BT.Wait(duration_ms=60000),
            BT.Dialog(kind='npc', key='ELDER_SUHL', dialog_ids=['0x81EA07']),
        ],
    )


def to_vabbi() -> BehaviorTree:
    return BT.Sequence(
        name='To Vabbi!',
        children=[
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7024, 16600), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-5977, 16718), target_map_id=429, move_tolerance=300),
            BT.MoveAndKill(pos=(-4938, 17129), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_SUHL', dialog_ids=['0x822701']),
            BT.Travel(target_map_id=387, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-844, 1699), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-489, 3940), target_map_id=436, move_tolerance=300),
            BT.MoveAndKill(pos=(770, 6616), pause_on_combat=True),
            BT.Dialog(kind='npc', key='DUNKORO', dialog_ids=['0x822704']),
            BT.MoveAndKill(pos=(4277, 7539), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(5248, 7608), target_map_id=369, move_tolerance=300),
            BT.MoveAndKill(pos=(-7600, 8970), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NERASHI', dialog_ids=['0x822704', '0x85']),
            BT.MoveAndKill(
                pos=[
                    (199, 6757),
                    (6760, 7209),
                    (11726, 7343),
                    (17021, 1657),
                    (20628, 2554),
                    (17419, 1817),
                    (15957, -332),
                ],
                pause_on_combat=True,
            ),
            BT.Travel(target_map_id=387, leave_party=True),
            BT.MoveAndKill(pos=(-701, 1551), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LONAI', dialog_ids=['0x822707']),
        ],
    )


def centaur_blackmail() -> BehaviorTree:
    return BT.Sequence(
        name='Centaur Blackmail',
        children=[
            BT.Travel(target_map_id=387, leave_party=True),
            BT.MoveAndKill(pos=(-737, 1618), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LONAI', dialog_ids=['0x822803', '0x822801']),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-769, 3132), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-449, 3896), target_map_id=436, move_tolerance=300),
            BT.MoveAndKill(pos=(1999, 5706), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ZHED_SHADOWHOOF', dialog_ids=['0x822804']),
            BT.MoveAndKill(pos=(4640, 7583), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(5180, 7655), target_map_id=369, move_tolerance=300),
            BT.MoveAndKill(pos=[(-6077, 9970), (-4347, 8729)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='MASTER_OF_WHISPERS', dialog_ids=['0x822804']),
            BT.MoveAndKill(pos=(21040, -15935), pause_on_combat=True),
            BT.Dialog(kind='npc', key='HAROJ_FIREMANE', dialog_ids=['0x822804', '0x84', '0x85']),
            BT.Wait(duration_ms=10000),
            BT.WaitForMapLoad(map_id=424, timeout_ms=10000),
            BT.MoveAndKill(pos=(-872, 2644), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ESTATE_GUARD_RIKESH', dialog_ids=['0x822807']),
        ],
    )


def mysterious_message() -> BehaviorTree:
    return BT.Sequence(
        name='Mysterious Message',
        children=[
            BT.Travel(target_map_id=387, leave_party=True),
            BT.MoveAndKill(pos=(-797, 1635), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LONAI', dialog_ids=['0x822903', '0x822901']),
            BT.MoveAndKill(pos=(-817, 3105), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(-421, 3890), target_map_id=436, move_tolerance=300),
            BT.MoveAndKill(pos=(4443, 7496), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(5239, 7534), target_map_id=369, move_tolerance=300),
            BT.MoveAndKill(pos=(-4325, 14179), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=369, timeout_ms=10000),
            BT.MoveAndKill(pos=(-4325, 14179), pause_on_combat=True),
            BT.Wait(duration_ms=60000),
            BT.Dialog(kind='npc', key='WHISPERS_ADEPT', dialog_ids=['0x822907']),
        ],
    )


def secrets_in_the_shadow() -> BehaviorTree:
    return BT.Sequence(
        name='Secrets in the Shadow',
        children=[
            BT.MoveAndKill(pos=(-4325, 14155), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MASTER_OF_WHISPERS', dialog_ids=['0x822A01']),
            BT.Travel(target_map_id=424, leave_party=True),
            BT.WaitForMapLoad(map_id=424, timeout_ms=10000),
            BT.MoveAndKill(pos=(2247, -3676), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(3282, -4413), target_map_id=379, move_tolerance=300),
            BT.MoveAndKill(pos=[(-4738, 16914), (-6487, 17178)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='DEHJAH', dialog_ids=['0x822A04']),
            BT.Wait(duration_ms=39900),
            BT.MoveAndKill(
                pos=[(-7313, 16338), (-4702, 15579), (-7668, 16229), (-6369, 17153)],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='MASTER_OF_WHISPERS', dialog_ids=['0x822A07']),
        ],
    )


def to_kill_a_demon() -> BehaviorTree:
    return BT.Sequence(
        name='To Kill a Demon',
        children=[
            BT.MoveAndKill(pos=(-6397, 17116), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MASTER_OF_WHISPERS', dialog_ids=['0x822B01']),
            BT.Travel(target_map_id=424, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=[(469, 1495), (3484, 3567)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(4862, 4408), target_map_id=384, move_tolerance=300),
            BT.MoveAndKill(pos=(-18894, -13512), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MASTER_OF_WHISPERS', dialog_ids=['0x822B04']),
            BT.MoveAndKill(
                pos=[(-15662, -7617), (-14242, -5346), (-13974, -5072), (-14178, -5295)],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='DEHJAH', dialog_ids=['0x85']),
            BT.WaitForMapLoad(map_id=425, timeout_ms=10000),
            BT.MoveAndKill(pos=(-15858, 11098), pause_on_combat=True),
            BT.Dialog(kind='npc', key='DEHJAH', dialog_ids=['0x822B07']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'hunted': (
        (2095.0, 307.0),
        (-976.0, 1524.0),
        (-3765.0, 4583.0),
        (-5001.0, 4859.0),
        (8252.0, 12668.0),
        (8252.0, 12668.0),
        (11927.0, 14638.0),
        (12858.0, 14874.0),
        (1402.0, -1952.0),
        (2870.0, 1221.0),
        (-567.0, 810.0),
        (-3804.0, 1821.0),
        (-3432.0, -2436.0),
        (-840.0, 1572.0),
    ),
    'the_great_escape': (
        (-753.0, 1588.0),
        (-961.0, 2690.0),
        (-480.0, 3913.0),
        (3689.0, 4609.0),
        (5032.0, 3847.0),
        (-14185.0, 13346.0),
        (-6844.0, 8329.0),
        (7287.0, 1842.0),
        (5769.0, -8954.0),
        (9590.0, -1760.0),
        (12850.0, -3249.0),
        (11435.0, -6714.0),
        (11273.0, -11690.0),
        (8873.0, -11517.0),
        (9799.0, -10868.0),
        (12518.0, -13342.0),
        (19975.0, -19365.0),
        (20686.0, -20173.0),
        (-789.0, 1596.0),
    ),
    'and_a_hero_shall_lead_them': (
        (-755.0, 1625.0),
        (-937.0, 2921.0),
        (-480.0, 3916.0),
        (-2716.0, 8121.0),
        (-3393.0, 9260.0),
        (21494.0, 13243.0),
        (25434.0, 14990.0),
    ),
    'the_council_is_called': (
        (-8151.0, 9111.0),
        (-4625.0, 10059.0),
        (-8152.0, 9342.0),
        (-6780.0, 16693.0),
        (-5928.0, 16758.0),
        (-5187.0, 16716.0),
        (-4707.0, 16582.0),
        (-5187.0, 16716.0),
        (-4664.0, 16850.0),
        (-5187.0, 16716.0),
        (-4374.0, 16819.0),
    ),
    'to_vabbi': (
        (-7024.0, 16600.0),
        (-5977.0, 16718.0),
        (-4938.0, 17129.0),
        (-844.0, 1699.0),
        (-489.0, 3940.0),
        (770.0, 6616.0),
        (4277.0, 7539.0),
        (5248.0, 7608.0),
        (-7600.0, 8970.0),
        (199.0, 6757.0),
        (6760.0, 7209.0),
        (11726.0, 7343.0),
        (17021.0, 1657.0),
        (20628.0, 2554.0),
        (17419.0, 1817.0),
        (15957.0, -332.0),
        (-701.0, 1551.0),
    ),
    'centaur_blackmail': (
        (-737.0, 1618.0),
        (-769.0, 3132.0),
        (-449.0, 3896.0),
        (1999.0, 5706.0),
        (4640.0, 7583.0),
        (5180.0, 7655.0),
        (-6077.0, 9970.0),
        (-4347.0, 8729.0),
        (21040.0, -15935.0),
        (-872.0, 2644.0),
    ),
    'mysterious_message': (
        (-797.0, 1635.0),
        (-817.0, 3105.0),
        (-421.0, 3890.0),
        (4443.0, 7496.0),
        (5239.0, 7534.0),
        (-4325.0, 14179.0),
        (-4325.0, 14179.0),
    ),
    'secrets_in_the_shadow': (
        (-4325.0, 14155.0),
        (2247.0, -3676.0),
        (3282.0, -4413.0),
        (-4738.0, 16914.0),
        (-6487.0, 17178.0),
        (-7313.0, 16338.0),
        (-4702.0, 15579.0),
        (-7668.0, 16229.0),
        (-6369.0, 17153.0),
    ),
    'to_kill_a_demon': (
        (-6397.0, 17116.0),
        (469.0, 1495.0),
        (3484.0, 3567.0),
        (4862.0, 4408.0),
        (-18894.0, -13512.0),
        (-15662.0, -7617.0),
        (-14242.0, -5346.0),
        (-13974.0, -5072.0),
        (-14178.0, -5295.0),
        (-15858.0, 11098.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'nightfall/hunted',
        'title': 'Hunted!',
        'factory': 'hunted',
        'source_steps': 19,
        'raw_steps': 19,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/the_great_escape',
        'title': 'The Great Escape',
        'factory': 'the_great_escape',
        'source_steps': 17,
        'raw_steps': 17,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/and_a_hero_shall_lead_them',
        'title': 'And a Hero Shall Lead Them',
        'factory': 'and_a_hero_shall_lead_them',
        'source_steps': 13,
        'raw_steps': 13,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/the_council_is_called',
        'title': 'The Council is Called',
        'factory': 'the_council_is_called',
        'source_steps': 13,
        'raw_steps': 13,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/to_vabbi',
        'title': 'To Vabbi!',
        'factory': 'to_vabbi',
        'source_steps': 19,
        'raw_steps': 19,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/centaur_blackmail',
        'title': 'Centaur Blackmail',
        'factory': 'centaur_blackmail',
        'source_steps': 18,
        'raw_steps': 18,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/mysterious_message',
        'title': 'Mysterious Message',
        'factory': 'mysterious_message',
        'source_steps': 13,
        'raw_steps': 13,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/secrets_in_the_shadow',
        'title': 'Secrets in the Shadow',
        'factory': 'secrets_in_the_shadow',
        'source_steps': 12,
        'raw_steps': 12,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/to_kill_a_demon',
        'title': 'To Kill a Demon',
        'factory': 'to_kill_a_demon',
        'source_steps': 13,
        'raw_steps': 13,
    },
)
