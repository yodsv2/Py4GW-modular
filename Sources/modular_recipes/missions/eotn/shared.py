"""Missions Eotn Shared BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def a_time_for_heroes() -> BehaviorTree:
    return BT.Sequence(
        name='A Time for Heroes',
        children=[
            BT.Travel(target_map_id=652, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(17, -820), pause_on_combat=True),
            BT.Dialog(kind='npc', key='HIGH_PRIEST_ALKAR', dialog_ids=['0x86', '0x84']),
            BT.WaitForMapLoad(map_id=673, timeout_ms=10000),
            BT.WaitUntilOnExplorable(timeout_ms=30000),
            BT.MoveAndKill(pos=[(-15488, 19062), (-14486, 16187)], pause_on_combat=True),
            BT.MoveToTarget(kind='enemy', key='THE_GREAT_DESTROYER'),
            BT.WaitForMapLoad(map_id=710, timeout_ms=10000),
        ],
    )


def destructions_depths() -> BehaviorTree:
    return BT.Sequence(
        name="Destruction's Depths",
        children=[
            BT.Dialog(kind='npc', key='JALIS_IRONHAMMER', dialog_ids=['0x86', '0x84']),
            BT.MoveAndKill(pos=(14812, -709), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_RANGED', dialog_ids=['0x88', '0x87']),
            BT.MoveAndKill(pos=(14526, -557), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_DEFENSE', dialog_ids=['0x88']),
            BT.MoveAndKill(pos=(14205, -456), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_MELEE', dialog_ids=['0x88', '0x87']),
            BT.MoveAndKill(pos=(7838, -3886), pause_on_combat=True),
            BT.Interact(kind='npc', key='SOKKA'),
            BT.MoveAndKill(pos=(4742, -4053), pause_on_combat=True),
            BT.Wait(duration_ms=6200),
            BT.MoveAndKill(
                pos=[(-390, -6147), (-3118, -10794), (-3767, -16185), (-7428, -17477)],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(-7636, -18030), target_map_id=671, move_tolerance=300),
            BT.Wait(duration_ms=100),
            BT.MoveAndKill(pos=(1857, 2561), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_RANGED', dialog_ids=['0x88', '0x87']),
            BT.MoveAndKill(pos=(2082, 2596), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_DEFENSE', dialog_ids=['0x88']),
            BT.MoveAndKill(pos=(2334, 2643), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_MELEE', dialog_ids=['0x88', '0x87']),
            BT.MoveAndKill(pos=(2370, 3762), pause_on_combat=True),
            BT.Wait(duration_ms=100),
            BT.MoveAndKill(pos=[(5756, 526), (6913, -2398)], pause_on_combat=True),
            BT.Wait(duration_ms=100),
            BT.MoveAndKill(pos=(4901, -5051), pause_on_combat=True),
            BT.Wait(duration_ms=6300),
            BT.MoveAndKill(
                pos=[
                    (2643, -3608),
                    (5422, -4884),
                    (7698, -3307),
                    (5644, -5661),
                    (3273, -8011),
                    (2225, -3573),
                    (6520, -3836),
                    (5658, -5163),
                ],
                pause_on_combat=True,
            ),
            BT.Interact(kind='npc', key='SIF_SHADOWHUNTER'),
            BT.MoveAndKill(pos=(14731, -5776), pause_on_combat=True),
            BT.Wait(duration_ms=100),
            BT.MoveAndKill(pos=(15432, -17509), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(15446, -18281), target_map_id=672, move_tolerance=300),
            BT.MoveAndKill(pos=(313, 3810), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_RANGED', dialog_ids=['0x88']),
            BT.MoveAndKill(pos=(-11, 3815), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_DEFENSE', dialog_ids=['0x88']),
            BT.MoveAndKill(pos=(-329, 3818), pause_on_combat=True),
            BT.Dialog(kind='npc', key='G_O_L_E_M_2_0_MELEE', dialog_ids=['0x88']),
            BT.Wait(duration_ms=100),
            BT.MoveAndKill(pos=[(-1805, 3022), (0, 4120), (1958, 3226)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(1269, 2013), (-820, 778), (15, 153), (-167, 684)], pause_on_combat=True),
            BT.WaitForMapLoad(map_id=652, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'a_time_for_heroes': ((17.0, -820.0), (-15488.0, 19062.0), (-14486.0, 16187.0)),
    'destructions_depths': (
        (14812.0, -709.0),
        (14526.0, -557.0),
        (14205.0, -456.0),
        (7838.0, -3886.0),
        (4742.0, -4053.0),
        (-390.0, -6147.0),
        (-3118.0, -10794.0),
        (-3767.0, -16185.0),
        (-7428.0, -17477.0),
        (-7636.0, -18030.0),
        (1857.0, 2561.0),
        (2082.0, 2596.0),
        (2334.0, 2643.0),
        (2370.0, 3762.0),
        (5756.0, 526.0),
        (6913.0, -2398.0),
        (4901.0, -5051.0),
        (2643.0, -3608.0),
        (5422.0, -4884.0),
        (7698.0, -3307.0),
        (5644.0, -5661.0),
        (3273.0, -8011.0),
        (2225.0, -3573.0),
        (6520.0, -3836.0),
        (5658.0, -5163.0),
        (14731.0, -5776.0),
        (15432.0, -17509.0),
        (15446.0, -18281.0),
        (313.0, 3810.0),
        (-11.0, 3815.0),
        (-329.0, 3818.0),
        (-1805.0, 3022.0),
        (0.0, 4120.0),
        (1958.0, 3226.0),
        (1269.0, 2013.0),
        (-820.0, 778.0),
        (15.0, 153.0),
        (-167.0, 684.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'eotn/a_time_for_heroes',
        'title': 'A Time for Heroes',
        'factory': 'a_time_for_heroes',
        'source_steps': 9,
        'raw_steps': 9,
    },
    {
        'kind': 'mission',
        'key': 'eotn/destructions_depths',
        'title': "Destruction's Depths",
        'factory': 'destructions_depths',
        'source_steps': 42,
        'raw_steps': 42,
    },
)
