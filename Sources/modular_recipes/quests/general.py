"""Quests General BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def all_for_one_and_one_for_justice() -> BehaviorTree:
    return BT.Sequence(
        name='All for One and One for Justice',
        children=[
            BT.Travel(target_map_id=493, leave_party=True),
            BT.Dialog(kind='npc', key='DINJA', pos=(-2428, 16752), dialog_ids=['0x830E03', '0x830E01']),
            BT.Dialog(kind='npc', key='MHENLO', pos=(-2540, 16210), dialog_ids=['0x89']),
            BT.WaitForMapLoad(map_id=415, timeout_ms=10000),
            BT.MoveAndKill(pos=(-1197, 983), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LIONGUARD_NEIRO', dialog_ids=['0x85']),
            BT.Dialog(kind='npc', key='LIONGUARD_NEIRO', dialog_ids=['0x85']),
            BT.MoveAndKill(pos=(-1961, 1460), pause_on_combat=True),
            BT.NudgeMove(pos=(-2000, 1500), pulses=2, pulse_ms=180),
            BT.WaitForMapLoad(map_id=55, timeout_ms=10000),
            BT.LoadParty(max_heroes=6),
            BT.Dialog(kind='npc', key='LIONGUARD_FIGO', pos=(-432, 3486), dialog_ids=['0x830E04', '0x81', '0x84']),
            BT.WaitForMapLoad(map_id=471, timeout_ms=10000),
            BT.MoveAndKill(pos=(6520, 10601), pause_on_combat=True),
            BT.Dialog(kind='npc', key='OLIAS', dialog_ids=['0x830E04']),
            BT.MoveAndKill(pos=(7706, 2168), pause_on_combat=True),
            BT.MoveAndKill(pos=(9959, 1595), pause_on_combat=True),
            BT.Wait(duration_ms=15000),
            BT.MoveAndKill(pos=(10251, 2292), pause_on_combat=True),
            BT.Wait(duration_ms=120000),
            BT.WaitForMapLoad(map_id=55, timeout_ms=60000),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=[(-7446, 16370), (-6632, 16281)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='CLERK_ARLON', dialog_ids=['0x830E07']),
        ],
    )


def chasing_zenmai() -> BehaviorTree:
    return BT.Sequence(
        name='Chasing Zenmai',
        children=[
            BT.Travel(target_map_id=493, leave_party=True),
            BT.MoveAndKill(pos=(-2489, 16783), pause_on_combat=True),
            BT.Dialog(kind='npc', key='DINJA', dialog_ids=['0x830F01']),
            BT.Dialog(kind='npc', key='MHENLO', dialog_ids=['0x88']),
            BT.WaitForMapLoad(map_id=493, timeout_ms=10000),
            BT.Travel(target_map_id=194, leave_party=True),
            BT.MoveAndKill(pos=(-1227, 864), pause_on_combat=True),
            BT.Dialog(kind='npc', key='IMPERIAL_GUARDSMAN_LINRO', dialog_ids=['0x830F04']),
            BT.MoveAndKill(pos=(2711, -4331), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(3152, -4845), target_map_id=240, move_tolerance=300),
            BT.MoveAndKill(pos=(-5218, 2349), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ZENMAI', dialog_ids=['0x830F04']),
            BT.MoveAndKill(pos=[(-696, -11341), (4382, -16185)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(4306, -16801), target_map_id=241, move_tolerance=300),
            BT.WaitForMapLoad(map_id=241, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[
                    (8731, 10033),
                    (8695, 6382),
                    (9863, 4885),
                    (10832, 1253),
                    (10431, -1125),
                    (10922, -3419),
                    (10067, -6720),
                    (6850, -7716),
                ],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=81700),
            BT.MoveAndKill(pos=(6782, -7622), pause_on_combat=True),
            BT.Wait(duration_ms=68900),
            BT.MoveAndKill(
                pos=[(6418, -7542), (7725, -7014), (7440, -8373), (6449, -7685), (7435, -7287)],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='ZENMAI', dialog_ids=['0x830F04']),
            BT.Resign(),
            BT.WaitForMapLoad(map_id=194, timeout_ms=10000),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(
                pos=[(-8005, 15044), (-7231, 16051), (-6504, 16239)], pause_on_combat=True
            ),
            BT.Dialog(kind='npc', key='CLERK_ARLON', dialog_ids=['0x830F07']),
        ],
    )


def finding_a_purpose() -> BehaviorTree:
    return BT.Sequence(
        name='Finding a Purpose',
        children=[
            BT.Travel(target_map_id=393, leave_party=True),
            BT.MoveAndKill(pos=(-11910, 2412), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SEEKER_OF_WHISPERS_LIGHTBRINGER_RANKS', dialog_ids=['0x84', '0x85', '0x86']),
            BT.MoveAndKill(pos=(-13219, -53), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GUARDIAN_OF_WHISPERS', dialog_ids=['0x84', '0x85']),
            BT.MoveAndKill(pos=(-16967, -394), pause_on_combat=True),
            BT.SendChatCommand(command='kneel'),
            BT.Wait(duration_ms=5000),
            BT.Dialog(kind='npc', key='SEER_OF_TRUTH', dialog_ids=['0x85', '0x86']),
            BT.WaitForMapLoad(map_id=474, timeout_ms=10000),
            BT.MoveAndKill(pos=(6050, -17280), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CHAPLAIN_PHYRATYSS', dialog_ids=['0x831401']),
            BT.Travel(target_map_id=496, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(18635, -1967), pause_on_combat=True),
            BT.Dialog(kind='npc', key='KEEPER_SHAFOSS', dialog_ids=['0x831404', '0x81', '0x84']),
            BT.WaitForMapLoad(map_id=462, timeout_ms=10000),
            BT.MoveAndKill(pos=(21512, 1560), pause_on_combat=True),
            BT.Interact(kind='npc', key='BINDING_GUARDIAN'),
            BT.MoveAndKill(pos=(22706, 12882), pause_on_combat=True),
            BT.Interact(kind='npc', key='BINDING_GUARDIAN'),
            BT.MoveAndKill(pos=(21264, 14407), pause_on_combat=True),
            BT.Interact(kind='npc', key='BINDING_GUARDIAN'),
            BT.MoveAndKill(pos=(12228, 15716), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RAZAH', dialog_ids=['0x831404', '0x84', '0x85']),
            BT.MoveAndKill(
                pos=[(21218, 14526), (22957, 13110), (21732, 1398)], pause_on_combat=True
            ),
            BT.MoveAndKill(pos=(14291, 13407), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RAZAH', dialog_ids=['0x831404']),
            BT.Travel(target_map_id=474, leave_party=True),
            BT.MoveAndKill(pos=(6035, -17336), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CHAPLAIN_PHYRATYSS', dialog_ids=['0x831407']),
            BT.Travel(target_map_id=387, leave_party=True),
            BT.MoveAndKill(pos=(-765, 3259), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-488, 3917), target_map_id=436, move_tolerance=300),
            BT.MoveAndKill(pos=(-390, 4863), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RAZAH', dialog_ids=['0x8D', '0x97']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'all_for_one_and_one_for_justice': (
        (-1197.0, 983.0),
        (-1961.0, 1460.0),
        (-2000.0, 1500.0),
        (5191.0, 10422.0),
        (7706.0, 2168.0),
        (9959.0, 1595.0),
        (10251.0, 2292.0),
        (-7446.0, 16370.0),
        (-6632.0, 16281.0),
    ),
    'chasing_zenmai': (
        (-2489.0, 16783.0),
        (-1227.0, 864.0),
        (2711.0, -4331.0),
        (3152.0, -4845.0),
        (-5218.0, 2349.0),
        (-696.0, -11341.0),
        (4382.0, -16185.0),
        (4306.0, -16801.0),
        (8731.0, 10033.0),
        (8695.0, 6382.0),
        (9863.0, 4885.0),
        (10832.0, 1253.0),
        (10431.0, -1125.0),
        (10922.0, -3419.0),
        (10067.0, -6720.0),
        (6850.0, -7716.0),
        (6782.0, -7622.0),
        (6418.0, -7542.0),
        (7725.0, -7014.0),
        (7440.0, -8373.0),
        (6449.0, -7685.0),
        (7435.0, -7287.0),
        (-8005.0, 15044.0),
        (-7231.0, 16051.0),
        (-6504.0, 16239.0),
    ),
    'finding_a_purpose': (
        (-11910.0, 2412.0),
        (-13219.0, -53.0),
        (-16967.0, -394.0),
        (6050.0, -17280.0),
        (18635.0, -1967.0),
        (21512.0, 1560.0),
        (22706.0, 12882.0),
        (21264.0, 14407.0),
        (12228.0, 15716.0),
        (21218.0, 14526.0),
        (22957.0, 13110.0),
        (21732.0, 1398.0),
        (14291.0, 13407.0),
        (6035.0, -17336.0),
        (-765.0, 3259.0),
        (-488.0, 3917.0),
        (-390.0, 4863.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'all_for_one_and_one_for_justice',
        'title': 'All for One and One for Justice',
        'factory': 'all_for_one_and_one_for_justice',
        'source_steps': 23,
        'raw_steps': 23,
    },
    {
        'kind': 'quest',
        'key': 'chasing_zenmai',
        'title': 'Chasing Zenmai',
        'factory': 'chasing_zenmai',
        'source_steps': 27,
        'raw_steps': 27,
    },
    {
        'kind': 'quest',
        'key': 'finding_a_purpose',
        'title': 'Finding a Purpose',
        'factory': 'finding_a_purpose',
        'source_steps': 36,
        'raw_steps': 36,
    },
)
