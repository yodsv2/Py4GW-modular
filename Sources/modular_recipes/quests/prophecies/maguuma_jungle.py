"""Quests Prophecies Maguuma Jungle BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def a_brothers_fury() -> BehaviorTree:
    return BT.Sequence(
        name="A Brother's Fury",
        children=[
            BT.Travel(target_map_id=140, leave_party=True),
            BT.Interact(kind='npc', pos=(4575, -9946)),
            BT.Wait(duration_ms=500),
            BT.Dialog(pos=(4575, -9946), dialog_ids=['0x805F03', '0x805F01'], interval_ms=500),
            BT.Wait(duration_ms=500),
            BT.MoveAndKill(pos=(4330, -10225), pause_on_combat=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(3150, -9450), target_map_id=41, move_tolerance=300),
            BT.WaitForMapLoad(map_id=41, timeout_ms=10000),
            BT.MoveAndKill(pos=[(1520, -8305), (1269, -6183)], pause_on_combat=True),
            BT.Dialog(pos=(1520, -8305), dialog_ids=['0x805F04']),
            BT.MoveAndKill(pos=(2817, -5953), pause_on_combat=True),
            BT.Dialog(pos=(2817, -5953), dialog_ids=['0x805F04']),
            BT.MoveAndKill(pos=[(638, -3198), (166, -2255), (0, -1750)], pause_on_combat=True),
            BT.Dialog(pos=(-40, -1859), dialog_ids=['0x805F04']),
            BT.MoveAndKill(
                pos=[(-945.82, 1488.35), (-4336.98, 2136.03), (-6339.26, 3538.42)],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(-6438, 3482), dialog_ids=['0x805F04']),
            BT.MoveAndKill(
                pos=[
                    (-5413.57, 6429.74),
                    (-7885.27, 7606.53),
                    (-10742.3, 11073),
                    (-13928.2, 9754.99),
                    (-16480, 10136.5),
                ],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(-16900, 9900), target_map_id=11, move_tolerance=300),
            BT.WaitForMapLoad(map_id=11, timeout_ms=10000),
            BT.MoveAndKill(pos=[(24314, -11233), (24042, -11911)], pause_on_combat=True),
            BT.Dialog(pos=(24113, -12030), dialog_ids=['0x805F07']),
        ],
    )


def urgent_warning() -> BehaviorTree:
    return BT.Sequence(
        name='Urgent Warning',
        children=[
            BT.Interact(kind='npc', pos=(-15405, 7)),
            BT.Wait(duration_ms=500),
            BT.Dialog(pos=(-15405, 7), dialog_ids=['0x805C03', '0x805C01'], interval_ms=500),
            BT.Wait(duration_ms=500),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(-15000, 450), target_map_id=139, move_tolerance=300),
            BT.MoveAndExitMap(pos=(-15050, 400), target_map_id=44, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (-16720, -742),
                    (-14675, -4311),
                    (-13116, -7296),
                    (-11331, -5355),
                    (-7797, 354),
                    (-2891, -1380),
                    (1567, 877),
                    (7402, 1212),
                    (10711, 2856),
                    (13645, 4237),
                    (17275, 792),
                    (22096, 2278),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(22279, 2186), dialog_ids=['0x805C04']),
            BT.MoveAndKill(
                pos=[(22064, 2698), (21552, 6952), (22353, 10167), (24571, 10041), (24471, 11819), (23356, 12579)],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(23200, 12650), target_map_id=12, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(-17637, -1477), (-16575, 562), (-19652, 1390), (-19652, 1390), (-16814, 4909)],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(-16848, 5092), dialog_ids=['0x805C07']),
        ],
    )


def white_mantle_wrath_demagogue_vanguard() -> BehaviorTree:
    return BT.Sequence(
        name="White Mantle Wrath: Demagogue's Vanguard",
        children=[
            BT.Travel(target_map_id=142, leave_party=True),
            BT.Interact(kind='npc', pos=(533, -4100)),
            BT.Wait(duration_ms=500),
            BT.Dialog(pos=(533, -4100), dialog_ids=['0x806301']),
            BT.Wait(duration_ms=500),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(1950, -2300), target_map_id=43, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(2030, -140), (-933, 394), (-2405, -1373), (-3601, -5423)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=[(-4638, -6690), (-6456, -9027)], pause_on_combat=True),
            BT.MoveAndKill(
                pos=[(-8218, -10502), (-10695, -13087), (-13552, -13392), (-14712, -16862), (-12739, -18888)],
                pause_on_combat=True,
            ),
            BT.MoveAndKill(pos=[(-11629, -18777), (-9806, -19777)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-9800, -20000), target_map_id=44, move_tolerance=300),
            BT.WaitForMapLoad(map_id=44, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[
                    (-19314, 12858),
                    (-20259, 10973),
                    (-18314, 8292),
                    (-23444, 5531),
                    (-23741, 4345),
                    (-20351, 563),
                    (-17363, -1148),
                    (-15532, -50),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(-15405, 7), dialog_ids=['0x806307']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'a_brothers_fury': (
        (4330.0, -10225.0),
        (3150.0, -9450.0),
        (1520.0, -8305.0),
        (1269.0, -6183.0),
        (2817.0, -5953.0),
        (638.0, -3198.0),
        (166.0, -2255.0),
        (0.0, -1750.0),
        (-945.82, 1488.35),
        (-4336.98, 2136.03),
        (-6339.26, 3538.42),
        (-5413.57, 6429.74),
        (-7885.27, 7606.53),
        (-10742.32, 11073.03),
        (-13928.21, 9754.99),
        (-16479.97, 10136.52),
        (-16900.0, 9900.0),
        (24314.0, -11233.0),
        (24042.0, -11911.0),
    ),
    'urgent_warning': (
        (-15000.0, 450.0),
        (-15050.0, 400.0),
        (-16720.0, -742.0),
        (-14675.0, -4311.0),
        (-13116.0, -7296.0),
        (-11331.0, -5355.0),
        (-7797.0, 354.0),
        (-2891.0, -1380.0),
        (1567.0, 877.0),
        (7402.0, 1212.0),
        (10711.0, 2856.0),
        (13645.0, 4237.0),
        (17275.0, 792.0),
        (22096.0, 2278.0),
        (22064.0, 2698.0),
        (21552.0, 6952.0),
        (22353.0, 10167.0),
        (24571.0, 10041.0),
        (24471.0, 11819.0),
        (23356.0, 12579.0),
        (23200.0, 12650.0),
        (-17637.0, -1477.0),
        (-16575.0, 562.0),
        (-19652.0, 1390.0),
        (-19652.0, 1390.0),
        (-16814.0, 4909.0),
    ),
    'white_mantle_wrath_demagogue_vanguard': (
        (1950.0, -2300.0),
        (2030.0, -140.0),
        (-933.0, 394.0),
        (-2405.0, -1373.0),
        (-3601.0, -5423.0),
        (-4638.0, -6690.0),
        (-6456.0, -9027.0),
        (-8218.0, -10502.0),
        (-10695.0, -13087.0),
        (-13552.0, -13392.0),
        (-14712.0, -16862.0),
        (-12739.0, -18888.0),
        (-11629.0, -18777.0),
        (-9806.0, -19777.0),
        (-9800.0, -20000.0),
        (-19314.0, 12858.0),
        (-20259.0, 10973.0),
        (-18314.0, 8292.0),
        (-23444.0, 5531.0),
        (-23741.0, 4345.0),
        (-20351.0, 563.0),
        (-17363.0, -1148.0),
        (-15532.0, -50.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'prophecies/a_brothers_fury',
        'title': "A Brother's Fury",
        'factory': 'a_brothers_fury',
        'source_steps': 20,
        'raw_steps': 20,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/urgent_warning',
        'title': 'Urgent Warning',
        'factory': 'urgent_warning',
        'source_steps': 11,
        'raw_steps': 11,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/white_mantle_wrath_demagogue_vanguard',
        'title': "White Mantle Wrath: Demagogue's Vanguard",
        'factory': 'white_mantle_wrath_demagogue_vanguard',
        'source_steps': 13,
        'raw_steps': 13,
    },
)
