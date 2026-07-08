"""Missions Prophecies Ring Of Fire BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def abaddons_mouth() -> BehaviorTree:
    return BT.Sequence(
        name="Abaddon's Mouth",
        children=[
            BT.Travel(target_map_id=123, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.EnterChallenge(target_map_id=123, delay_ms=6000),
            BT.MoveAndKill(
                pos=[(16815, 10580), (11738, 5359), (6022, 947), (1999, 2820), (-4335, 627), (-1520, -2907)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(
                pos=[(595, -5122), (2944, -7636), (7932, -6690), (11398, -7418), (15998, -6380), (19215, -5354)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=[(19992, -4981), (20807, -5803)], pause_on_combat=True),
            BT.WaitForMapLoad(map_id=124, timeout_ms=10000),
        ],
    )


def hells_precipice() -> BehaviorTree:
    return BT.Sequence(
        name="Hell's Precipice",
        children=[
            BT.Travel(target_map_id=124, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.EnterChallenge(target_map_id=124, delay_ms=6000),
            BT.UseConsumables(mode='all', multibox=False, leader_only=True),
            BT.Wait(duration_ms=1000),
            BT.MoveAndKill(
                pos=[(5500, 1067), (3558, -3826), (8963, -9388), (5413, -15683), (-4059, -19718), (-9061, -16683)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=124, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-2519, 2104), (-4608, 5911), (966, 9247), (4567, 9409)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=783, timeout_ms=10000),
            BT.Dialog(pos=(-8679, 5086), dialog_ids=['0x85']),
        ],
    )


def ring_of_fire() -> BehaviorTree:
    return BT.Sequence(
        name='Ring of Fire',
        children=[
            BT.Travel(target_map_id=122, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.EnterChallenge(target_map_id=122, delay_ms=6000),
            BT.UseConsumables(mode='all', multibox=False, leader_only=True),
            BT.Wait(duration_ms=1000),
            BT.MoveAndKill(
                pos=[(18118, -2086), (17515, 4197), (11605, 11759), (11498, 7711), (1679, 7158), (0, 7766)],
                pause_on_combat=True,
            ),
            BT.FlagAllHeroes(-2382, 6756),
            BT.Wait(duration_ms=5000),
            BT.FlagAllHeroes(-2335, 8972),
            BT.Wait(duration_ms=5000),
            BT.UnflagAllHeroes(),
            BT.MoveAndKill(
                pos=[(-3441, 6381), (-3551, 7891), (-6238, 4257), (-8638, 1750)],
                pause_on_combat=True,
            ),
            BT.Interact(kind='gadget', pos=(-3441, 6381)),
            BT.Wait(duration_ms=500),
            BT.Interact(kind='gadget', pos=(-8554, 2252)),
            BT.Wait(duration_ms=500),
            BT.MoveAndKill(pos=[(-10158, 1905), (-10834, 2981)], pause_on_combat=True),
            BT.WaitForMapLoad(map_id=123, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'abaddons_mouth': (
        (16815.0, 10580.0),
        (11738.0, 5359.0),
        (6022.0, 947.0),
        (1999.0, 2820.0),
        (-4335.0, 627.0),
        (-1520.0, -2907.0),
        (595.0, -5122.0),
        (2944.0, -7636.0),
        (7932.0, -6690.0),
        (11398.0, -7418.0),
        (15998.0, -6380.0),
        (19215.0, -5354.0),
        (19992.0, -4981.0),
        (20807.0, -5803.0),
    ),
    'hells_precipice': (
        (5500.0, 1067.0),
        (3558.0, -3826.0),
        (8963.0, -9388.0),
        (5413.0, -15683.0),
        (-4059.0, -19718.0),
        (-9061.0, -16683.0),
        (-2519.0, 2104.0),
        (-4608.0, 5911.0),
        (966.0, 9247.0),
        (4567.0, 9409.0),
    ),
    'ring_of_fire': (
        (18118.0, -2086.0),
        (17515.0, 4197.0),
        (11605.0, 11759.0),
        (11498.0, 7711.0),
        (1679.0, 7158.0),
        (0.0, 7766.0),
        (-3441.0, 6381.0),
        (-3551.0, 7891.0),
        (-6238.0, 4257.0),
        (-8638.0, 1750.0),
        (-10158.0, 1905.0),
        (-10834.0, 2981.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'prophecies/abaddons_mouth',
        'title': "Abaddon's Mouth",
        'factory': 'abaddons_mouth',
        'source_steps': 7,
        'raw_steps': 7,
    },
    {
        'kind': 'mission',
        'key': 'prophecies/hells_precipice',
        'title': "Hell's Precipice",
        'factory': 'hells_precipice',
        'source_steps': 9,
        'raw_steps': 9,
    },
    {
        'kind': 'mission',
        'key': 'prophecies/ring_of_fire',
        'title': 'Ring of Fire',
        'factory': 'ring_of_fire',
        'source_steps': 15,
        'raw_steps': 15,
    },
)
