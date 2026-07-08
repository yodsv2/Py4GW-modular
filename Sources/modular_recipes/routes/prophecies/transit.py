"""Routes Prophecies Transit BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def augury_rock_to_dunes_of_despair() -> BehaviorTree:
    return BT.Sequence(
        name='Augury Rock to Dunes of Despair',
        children=[
            BT.Travel(target_map_id=38, leave_party=True),
            BT.MoveAndKill(pos=(-18302, -652), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-20027, -464), target_map_id=113, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(2187, -11202), (-3588, -13863), (1243, -19123)], pause_on_combat=True
            ),
            BT.MoveAndExitMap(pos=(1269, -19679), target_map_id=111, move_tolerance=300),
            BT.MoveAndKill(pos=(-4964, -12682), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-4744, -12271), target_map_id=116, move_tolerance=300),
        ],
    )


def augury_rock_to_heroes_audience() -> BehaviorTree:
    return BT.Sequence(
        name='Augury Rock to Heroes Audience',
        children=[
            BT.Travel(target_map_id=38, leave_party=True),
            BT.MoveAndKill(pos=(-18484, -489), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-19968, -448), target_map_id=113, move_tolerance=300),
            BT.MoveAndKill(pos=(-14603, -14507), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-14947, -14569), target_map_id=152, move_tolerance=300),
        ],
    )


def beacons_to_rankor() -> BehaviorTree:
    return BT.Sequence(
        name='Beacons to Camp Rankor',
        children=[
            BT.MoveAndKill(
                pos=[(-6850, 4881), (-2906, 156), (-1932, -5887), (-6047, -6092), (-7323, -7153), (-7347, -7629)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=91, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[
                    (-5645, 41872),
                    (2714, 38619),
                    (2291, 32756),
                    (-2178, 24582),
                    (-148, 3311),
                    (-3159, -8177),
                    (-3500, -30102),
                    (3340, -39165),
                    (5815, -41288),
                    (6229, -41568),
                ],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=155, timeout_ms=10000),
        ],
    )


def bergen_hot_springs_to_temple_of_ages() -> BehaviorTree:
    return BT.Sequence(
        name='Bergen Hot Springs to Temple of the Ages',
        children=[
            BT.Travel(target_map_id=57, leave_party=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndKill(pos=[(15521, -15378), (15450, -15050)], pause_on_combat=True),
            BT.WaitForMapLoad(map_id=59, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(13276, -14317), (8660, -12109), (1522, -7990), (-3489, -11607), (-4290, -11599)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=56, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-4523, -9755), (-7331, -6178), (-9610, -2136), (-12517, 5459), (-18010, 7033), (-20100, 9025)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=18, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(8716, 18587), (3795, 17750), (592, 16243), (-1968, 14407), (-5004, 15424), (-5180, 16000)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=138, timeout_ms=10000),
        ],
    )


def camp_rankor_to_droks() -> BehaviorTree:
    return BT.Sequence(
        name="Camp Rankor to Droknar's Forge",
        children=[
            BT.Travel(target_map_id=155, leave_party=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(7669, -45072), target_map_id=26, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (-22278, 16193),
                    (-17952, 14216),
                    (-14931, 4803),
                    (-12319, -850),
                    (-4801, -6345),
                    (2555, -11337),
                    (6038, -14065),
                    (8624, -16461),
                    (8900, -16750),
                ],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=20, timeout_ms=10000),
        ],
    )


def d_alessio_seaboard_to_bergen_hot_springs() -> BehaviorTree:
    return BT.Sequence(
        name="D'Alessio Seaboard to Bergen Hot Springs",
        children=[
            BT.Travel(target_map_id=15, leave_party=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndKill(pos=[(16000, 17080), (16030, 17200)], pause_on_combat=True),
            BT.WaitForMapLoad(map_id=58, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[
                    (-11453, -18065),
                    (-10558, -9708),
                    (-10958, -1009),
                    (-12931, 6726),
                    (-16653, 16226),
                    (-19550, 15625),
                ],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=59, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(19271, 5207), (17801, 2710), (14927, -8731), (15425, -15035)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=57, timeout_ms=10000),
        ],
    )


def droks_to_ice_caves() -> BehaviorTree:
    return BT.Sequence(
        name="Droknar's Forge to Ice Caves",
        children=[
            BT.Travel(target_map_id=20, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(844, 9625), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-324, 10936), target_map_id=26, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(6543, -13584), (10734, -9478), (18536, -8461), (19649, -12416), (22608, -11858)],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(23217, -11592), target_map_id=22, move_tolerance=300),
        ],
    )


def la_to_beacons() -> BehaviorTree:
    return BT.Sequence(
        name="Lion's Arch to Beacons Perch",
        children=[
            BT.Travel(target_map_id=55, leave_party=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(292, 12443), target_map_id=58, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(6202, -18031), (11673, -10051), (14864, 11661), (19275, 10826), (20300, 11377)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=54, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-7232, 8380), (-1379, 7598), (3519, 6648), (7437, 7633), (7624, 8200)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=27, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-7077, -6441), (-2283, -2144), (-1020, 4597), (3813, 7841), (7514, 7308), (7683, 7958)],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=100, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[
                    (-13556, -22347),
                    (-6928, -19974),
                    (2527, -20407),
                    (10051, -14518),
                    (15587, -17156),
                    (13671, -22583),
                    (13906, -23051),
                ],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=133, timeout_ms=10000),
        ],
    )


def lions_arch_to_d_alessio_seaboard() -> BehaviorTree:
    return BT.Sequence(
        name="Lion's Arch to D'Alessio Seaboard",
        children=[
            BT.Travel(target_map_id=55, leave_party=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndKill(
                pos=[(1219, 7222), (1021, 10651), (250, 12350)], pause_on_combat=True
            ),
            BT.WaitForMapLoad(map_id=58, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[
                    (5116, -17415),
                    (757, -16768),
                    (-6042, -16126),
                    (-9893, -17625),
                    (-11600, -19500),
                    (-11708, -19957),
                ],
                pause_on_combat=True,
            ),
            BT.WaitForMapLoad(map_id=15, timeout_ms=10000),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'augury_rock_to_dunes_of_despair': (
        (-18302.0, -652.0),
        (-20027.0, -464.0),
        (2187.0, -11202.0),
        (-3588.0, -13863.0),
        (1243.0, -19123.0),
        (1269.0, -19679.0),
        (-4964.0, -12682.0),
        (-4744.0, -12271.0),
    ),
    'augury_rock_to_heroes_audience': (
        (-18484.0, -489.0),
        (-19968.0, -448.0),
        (-14603.0, -14507.0),
        (-14947.0, -14569.0),
    ),
    'beacons_to_rankor': (
        (-6850.0, 4881.0),
        (-2906.0, 156.0),
        (-1932.0, -5887.0),
        (-6047.0, -6092.0),
        (-7323.0, -7153.0),
        (-7347.0, -7629.0),
        (-5645.0, 41872.0),
        (2714.0, 38619.0),
        (2291.0, 32756.0),
        (-2178.0, 24582.0),
        (-148.0, 3311.0),
        (-3159.0, -8177.0),
        (-3500.0, -30102.0),
        (3340.0, -39165.0),
        (5815.0, -41288.0),
        (6229.0, -41568.0),
    ),
    'bergen_hot_springs_to_temple_of_ages': (
        (15521.0, -15378.0),
        (15450.0, -15050.0),
        (13276.0, -14317.0),
        (8660.0, -12109.0),
        (1522.0, -7990.0),
        (-3489.0, -11607.0),
        (-4290.0, -11599.0),
        (-4523.0, -9755.0),
        (-7331.0, -6178.0),
        (-9610.0, -2136.0),
        (-12517.0, 5459.0),
        (-18010.0, 7033.0),
        (-20100.0, 9025.0),
        (8716.0, 18587.0),
        (3795.0, 17750.0),
        (592.0, 16243.0),
        (-1968.0, 14407.0),
        (-5004.0, 15424.0),
        (-5180.0, 16000.0),
    ),
    'camp_rankor_to_droks': (
        (7669.0, -45072.0),
        (-22278.0, 16193.0),
        (-17952.0, 14216.0),
        (-14931.0, 4803.0),
        (-12319.0, -850.0),
        (-4801.0, -6345.0),
        (2555.0, -11337.0),
        (6038.0, -14065.0),
        (8624.0, -16461.0),
        (8900.0, -16750.0),
    ),
    'd_alessio_seaboard_to_bergen_hot_springs': (
        (16000.0, 17080.0),
        (16030.0, 17200.0),
        (-11453.0, -18065.0),
        (-10558.0, -9708.0),
        (-10958.0, -1009.0),
        (-12931.0, 6726.0),
        (-16653.0, 16226.0),
        (-19550.0, 15625.0),
        (19271.0, 5207.0),
        (17801.0, 2710.0),
        (14927.0, -8731.0),
        (15425.0, -15035.0),
    ),
    'droks_to_ice_caves': (
        (844.0, 9625.0),
        (-324.0, 10936.0),
        (6543.0, -13584.0),
        (10734.0, -9478.0),
        (18536.0, -8461.0),
        (19649.0, -12416.0),
        (22608.0, -11858.0),
        (23217.0, -11592.0),
    ),
    'la_to_beacons': (
        (292.0, 12443.0),
        (6202.0, -18031.0),
        (11673.0, -10051.0),
        (14864.0, 11661.0),
        (19275.0, 10826.0),
        (20300.0, 11377.0),
        (-7232.0, 8380.0),
        (-1379.0, 7598.0),
        (3519.0, 6648.0),
        (7437.0, 7633.0),
        (7624.0, 8200.0),
        (-7077.0, -6441.0),
        (-2283.0, -2144.0),
        (-1020.0, 4597.0),
        (3813.0, 7841.0),
        (7514.0, 7308.0),
        (7683.0, 7958.0),
        (-13556.0, -22347.0),
        (-6928.0, -19974.0),
        (2527.0, -20407.0),
        (10051.0, -14518.0),
        (15587.0, -17156.0),
        (13671.0, -22583.0),
        (13906.0, -23051.0),
    ),
    'lions_arch_to_d_alessio_seaboard': (
        (1219.0, 7222.0),
        (1021.0, 10651.0),
        (250.0, 12350.0),
        (5116.0, -17415.0),
        (757.0, -16768.0),
        (-6042.0, -16126.0),
        (-9893.0, -17625.0),
        (-11600.0, -19500.0),
        (-11708.0, -19957.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'route',
        'key': 'augury_rock_to_dunes_of_despair',
        'title': 'Augury Rock to Dunes of Despair',
        'factory': 'augury_rock_to_dunes_of_despair',
        'source_steps': 7,
        'raw_steps': 7,
    },
    {
        'kind': 'route',
        'key': 'augury_rock_to_heroes_audience',
        'title': 'Augury Rock to Heroes Audience',
        'factory': 'augury_rock_to_heroes_audience',
        'source_steps': 5,
        'raw_steps': 5,
    },
    {
        'kind': 'route',
        'key': 'beacons_to_rankor',
        'title': 'Beacons to Camp Rankor',
        'factory': 'beacons_to_rankor',
        'source_steps': 4,
        'raw_steps': 4,
    },
    {
        'kind': 'route',
        'key': 'bergen_hot_springs_to_temple_of_ages',
        'title': 'Bergen Hot Springs to Temple of the Ages',
        'factory': 'bergen_hot_springs_to_temple_of_ages',
        'source_steps': 10,
        'raw_steps': 10,
    },
    {
        'kind': 'route',
        'key': 'camp_rankor_to_droks',
        'title': "Camp Rankor to Droknar's Forge",
        'factory': 'camp_rankor_to_droks',
        'source_steps': 5,
        'raw_steps': 5,
    },
    {
        'kind': 'route',
        'key': 'd_alessio_seaboard_to_bergen_hot_springs',
        'title': "D'Alessio Seaboard to Bergen Hot Springs",
        'factory': 'd_alessio_seaboard_to_bergen_hot_springs',
        'source_steps': 8,
        'raw_steps': 8,
    },
    {
        'kind': 'route',
        'key': 'droks_to_ice_caves',
        'title': "Droknar's Forge to Ice Caves",
        'factory': 'droks_to_ice_caves',
        'source_steps': 6,
        'raw_steps': 6,
    },
    {
        'kind': 'route',
        'key': 'la_to_beacons',
        'title': "Lion's Arch to Beacons Perch",
        'factory': 'la_to_beacons',
        'source_steps': 11,
        'raw_steps': 11,
    },
    {
        'kind': 'route',
        'key': 'lions_arch_to_d_alessio_seaboard',
        'title': "Lion's Arch to D'Alessio Seaboard",
        'factory': 'lions_arch_to_d_alessio_seaboard',
        'source_steps': 6,
        'raw_steps': 6,
    },
)
