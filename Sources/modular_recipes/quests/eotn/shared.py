"""Quests Eotn Shared BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


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


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
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
    'the_final_vision': ((-3717.0, 4387.0), (-4596.0, 5017.0), (-6462.0, 6448.0)),
}


RECIPES: tuple[dict[str, object], ...] = (
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
        'key': 'eotn/against_the_destroyers_start',
        'title': 'Against the Destroyers Start',
        'factory': 'against_the_destroyers_start',
        'source_steps': 18,
        'raw_steps': 18,
    },
    {
        'kind': 'quest',
        'key': 'eotn/the_final_vision',
        'title': 'The Final Vision',
        'factory': 'the_final_vision',
        'source_steps': 8,
        'raw_steps': 8,
    },
)
