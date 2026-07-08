"""Missions Nightfall Desolation BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def gate_of_desolation() -> BehaviorTree:
    return BT.Sequence(
        name='Gate of Desolation',
        children=[
            BT.Travel(target_map_id=478, leave_party=True),
            BT.MoveAndKill(pos=(2274, -354), pause_on_combat=True),
            BT.LoadParty(max_heroes=8, required_hero=['Zhed Shadowhoof']),
            BT.Dialog(kind='npc', key='LAPH_LONGMANE', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=10300),
            BT.WaitForMapLoad(map_id=478, timeout_ms=10000),
            BT.Interact(kind='npc', key='PALAWA_JOKO'),
            BT.Wait(duration_ms=43900),
            BT.FlagAllHeroes(16339, -8235),
            BT.MoveAndKill(pos=(18525, -11208), pause_on_combat=True),
            BT.Wait(duration_ms=165000),
            BT.FlagAllHeroes(15578, -8586),
            BT.Wait(duration_ms=300000),
            BT.FlagAllHeroes(15966, -9078),
            BT.MoveAndKill(pos=(15966, -9078), pause_on_combat=True),
            BT.UnflagAllHeroes(),
            BT.Wait(duration_ms=3000),
            BT.Interact(kind='gadget', key='WURM_SPOOR', pos=(15933, -9103)),
            BT.MoveAndKill(pos=(15966, -9078), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.Interact(kind='gadget', key='WURM_SPOOR', pos=(15933, -9103)),
            BT.MoveAndKill(
                pos=[(11107, -12526), (3940, -12402), (-3588, -13121), (-7339, -9230)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=500),
            BT.MoveAndKill(pos=[(-4446, -3363), (-4830, -3305)], pause_on_combat=True),
            BT.Wait(duration_ms=1700),
            BT.Interact(kind='gadget', key='WURM_SPOOR', pos=(-4897, -3359)),
            BT.MoveAndKill(
                pos=[(-4567, -2022), (-4503, 1807), (-3694, 3284), (-539, 5811)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=(409, 3014), pause_on_combat=True),
            BT.Interact(kind='gadget', key='WURM_SPOOR', pos=(484, 2790)),
            BT.MoveAndKill(
                pos=[
                    (2459, -1749),
                    (4288, -404),
                    (7856, -231),
                    (10668, 4207),
                    (8295, 9233),
                    (6829, 7778),
                    (9116, 10453),
                ],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=1100),
            BT.MoveAndKill(
                pos=[(9167, 13253), (6255, 13864), (4645, 14440), (1879, 12608), (-87, 12656), (-1468, 15466)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=700),
            BT.MoveAndKill(
                pos=[(-2371, 16370), (-2437, 16434), (-2600, 16600), (-2346, 16889)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=545, timeout_ms=10000),
        ],
    )


def ruins_of_morah() -> BehaviorTree:
    return BT.Sequence(
        name='Ruins of Morah',
        children=[
            BT.Travel(target_map_id=480, leave_party=True),
            BT.LoadParty(max_heroes=8, required_hero=['General Morgahn']),
            BT.MoveAndKill(pos=[(-3140, 13174), (-4758, 12996)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='CAPTAIN_MEHHAN', dialog_ids=['0x81', '0x84']),
            BT.Wait(duration_ms=7200),
            BT.MoveAndKill(pos=(-4414, -6307), pause_on_combat=True),
            BT.WaitForMapLoad(map_id=480, timeout_ms=10000),
            BT.MoveAndKill(pos=(-4414, -6307), pause_on_combat=True),
            BT.FlagAllHeroes(-4414, -6307),
            BT.MoveAndKill(pos=[(-2494, -5438), (-4230, -6155)], pause_on_combat=True),
            BT.MoveAndKill(pos=(-4429, -6308), pause_on_combat=True),
            BT.Wait(duration_ms=8000),
            BT.MoveAndKill(pos=[(-2827, -5532), (-4615, -6219)], pause_on_combat=True),
            BT.UnflagAllHeroes(),
            BT.WaitForMapLoad(map_id=450, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'gate_of_desolation': (
        (2274.0, -354.0),
        (18525.0, -11208.0),
        (15966.0, -9078.0),
        (15966.0, -9078.0),
        (11107.0, -12526.0),
        (3940.0, -12402.0),
        (-3588.0, -13121.0),
        (-7339.0, -9230.0),
        (-4446.0, -3363.0),
        (-4830.0, -3305.0),
        (-4567.0, -2022.0),
        (-4503.0, 1807.0),
        (-3694.0, 3284.0),
        (-539.0, 5811.0),
        (409.0, 3014.0),
        (2459.0, -1749.0),
        (4288.0, -404.0),
        (7856.0, -231.0),
        (10668.0, 4207.0),
        (8295.0, 9233.0),
        (6829.0, 7778.0),
        (9116.0, 10453.0),
        (9167.0, 13253.0),
        (6255.0, 13864.0),
        (4645.0, 14440.0),
        (1879.0, 12608.0),
        (-87.0, 12656.0),
        (-1468.0, 15466.0),
        (-2371.0, 16370.0),
        (-2437.0, 16434.0),
        (-2600.0, 16600.0),
        (-2346.0, 16889.0),
    ),
    'ruins_of_morah': (
        (-3140.0, 13174.0),
        (-4758.0, 12996.0),
        (-4414.0, -6307.0),
        (-4414.0, -6307.0),
        (-2494.0, -5438.0),
        (-4230.0, -6155.0),
        (-4429.0, -6308.0),
        (-2827.0, -5532.0),
        (-4615.0, -6219.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'mission',
        'key': 'nightfall/gate_of_desolation',
        'title': 'Gate of Desolation',
        'factory': 'gate_of_desolation',
        'source_steps': 35,
        'raw_steps': 35,
    },
    {
        'kind': 'mission',
        'key': 'nightfall/ruins_of_morah',
        'title': 'Ruins of Morah',
        'factory': 'ruins_of_morah',
        'source_steps': 15,
        'raw_steps': 15,
    },
)
