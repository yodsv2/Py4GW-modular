"""Quests Prophecies Kryta BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def passage_through_the_dark_river() -> BehaviorTree:
    return BT.Sequence(
        name='Passage Through the Dark River',
        children=[
            BT.Travel(target_map_id=49, leave_party=True),
            BT.Interact(kind='npc', pos=(4981, -4354)),
            BT.Wait(duration_ms=500),
            BT.Dialog(pos=(4981, -4354), dialog_ids=['0x806401']),
            BT.Wait(duration_ms=500),
            BT.MoveAndKill(
                pos=[(5464, -5216), (6364, -8267), (6415, -10538)], pause_on_combat=True
            ),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(6200, -10650), target_map_id=48, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (12566, 12158),
                    (14655, 8635),
                    (17417, 6812),
                    (19783, 2474),
                    (21057, -49),
                    (22319, -4402),
                    (24534, -5286),
                    (25876, -7722),
                    (23570, -9965),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(23599, -10038), dialog_ids=['0x2', '0x15', '0x3', '0x1F', '0x4']),
            BT.WaitForMapLoad(map_id=73, timeout_ms=10000),
            BT.MoveAndKill(pos=[(-24358, 10243), (-22209, 7665)], pause_on_combat=True),
            BT.Dialog(pos=(-22117, 7501), dialog_ids=['0x806407']),
        ],
    )


def report_to_the_white_mantle() -> BehaviorTree:
    return BT.Sequence(
        name='Report to the White Mantle',
        children=[
            BT.Travel(target_map_id=55, leave_party=True),
            BT.Interact(kind='npc', pos=(2376, 9268)),
            BT.Wait(duration_ms=2000),
            BT.Dialog(pos=(2376, 9268), dialog_ids=['0x801303', '0x801301'], interval_ms=2000),
            BT.Wait(duration_ms=2000),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(200, 12400), target_map_id=58, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (5294, -16988),
                    (1043, -16842),
                    (-3345, -16503),
                    (-8249, -15776),
                    (-10616, -16863),
                    (-11547, -19370),
                ],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(-11700, -19700), target_map_id=15, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(16506, 15402), (18592, 12867), (21877, 9855)], pause_on_combat=True
            ),
            BT.Dialog(pos=(21771, 9699), dialog_ids=['0x801307']),
        ],
    )


def mhenlos_request() -> BehaviorTree:
    return BT.Sequence(
        name="Mhenlo's Request",
        children=[
            BT.Travel(target_map_id=55),
            BT.Move(pos=[(1051, 9580)]),
            BT.Dialog(kind='npc', key='FIRSTWATCH_SERGIO_SKILLS', dialog_ids=['0x81b403'], pos=(328, 9594)),
            BT.Dialog(kind='npc', key='FIRSTWATCH_SERGIO_SKILLS', dialog_ids=['0x81b401'], pos=(328, 9594)),
            BT.Move(pos=[(1323, 9767), (731, 11460)]),
            BT.MoveAndExitMap(pos=(320, 12305), target_map_id=58, move_tolerance=300),
            BT.Dialog(kind='npc', key='MHENLO', dialog_ids=['0x81b404'], pos=(5658, -17135)),
            BT.MoveAndExitMap(pos=(6325, -18291), target_map_id=55, move_tolerance=300),
            BT.Move(pos=[(1338, 2070)]),
            BT.Dialog(kind='npc', key='JIAJU_TAI', dialog_ids=['0x81b404'], pos=(1444, 1925)),
            BT.Dialog(kind='npc', key='JIAJU_TAI', dialog_ids=['0x86'], pos=(1444, 1925)),
            BT.Dialog(kind='npc', key='JIAJU_TAI', dialog_ids=['0x87'], pos=(1444, 1925)),
            BT.Dialog(kind='npc', key='JIAJU_TAI', dialog_ids=['0x84'], pos=(1444, 1925)),
            BT.WaitForMapLoad(map_id=290, timeout_ms=10000),
            BT.Move(pos=[(-5302, 6909)]),
            BT.Dialog(kind='npc', key='DOCKHAND_QUANGNAI', dialog_ids=['0x81b407'], pos=(-5161, 6940)),
        ],
    )


def to_kryta_refugees_icecave_journeyend() -> BehaviorTree:
    return BT.Sequence(
        name='To kryta: Refugees',
        children=[
            BT.Travel(target_map_id=133, leave_party=True),
            BT.Interact(kind='npc', pos=(-10183, 35115)),
            BT.Wait(duration_ms=2000),
            BT.Dialog(pos=(-10183, 35115), dialog_ids=['0x80C703', '0x80C701'], interval_ms=2000),
            BT.Wait(duration_ms=2000),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndExitMap(pos=(-10800, 35400), target_map_id=100, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (16456, -14885),
                    (13831, -13262),
                    (7011, -16575),
                    (3708, -20223),
                    (-562, -19354),
                    (-3197, -17726),
                    (-6971, -17766),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(-7070, -18028), dialog_ids=['0x80C707']),
            BT.MoveAndKill(pos=[(-7086, -20774), (-10818, -21968)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-13820, -23050), target_map_id=27, move_tolerance=300),
            BT.WaitForMapLoad(map_id=27, timeout_ms=10000),
            BT.Interact(kind='npc', pos=(7376, 5948)),
            BT.Wait(duration_ms=2000),
            BT.Dialog(pos=(7376, 5948), dialog_ids=['0x80B301']),
            BT.Wait(duration_ms=2000),
            BT.MoveAndKill(
                pos=[
                    (3191, 8329),
                    (-126, 7270),
                    (-2977, 7689),
                    (-5901, 3994),
                    (-6562, -154),
                    (-3521, -1323),
                    (-1601, -3120),
                    (-2302, -7371),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(-2206, -7537), dialog_ids=['0x80B307']),
            BT.MoveAndKill(pos=[(172, -6473), (-2270, -7409)], pause_on_combat=True),
            BT.Interact(kind='npc', pos=(-2206, -7537)),
            BT.Wait(duration_ms=2000),
            BT.Dialog(pos=(-2206, -7537), dialog_ids=['0x800401']),
            BT.Wait(duration_ms=2000),
            BT.MoveAndKill(
                pos=[(-4224, -6972), (-6140, -6063), (-7719, -7262)], pause_on_combat=True
            ),
            BT.MoveAndExitMap(pos=(-7750, -7500), target_map_id=54, move_tolerance=300),
            BT.WaitForMapLoad(map_id=54, timeout_ms=10000),
            BT.Dialog(pos=(7630, 7520), dialog_ids=['0x800404']),
            BT.MoveAndKill(
                pos=[(7435, 6732), (6179, 3505), (4165, -1131), (1043, -2484), (-2181, -5573)],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(-1200, -7100), target_map_id=14, move_tolerance=300),
            BT.WaitForMapLoad(map_id=14, timeout_ms=10000),
            BT.MoveAndKill(pos=[(-2248, 25151), (-701, 24655)], pause_on_combat=True),
            BT.Dialog(pos=(425, 23794), dialog_ids=['0x800407']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'passage_through_the_dark_river': (
        (5464.0, -5216.0),
        (6364.0, -8267.0),
        (6415.0, -10538.0),
        (6200.0, -10650.0),
        (12566.0, 12158.0),
        (14655.0, 8635.0),
        (17417.0, 6812.0),
        (19783.0, 2474.0),
        (21057.0, -49.0),
        (22319.0, -4402.0),
        (24534.0, -5286.0),
        (25876.0, -7722.0),
        (23570.0, -9965.0),
        (-24358.0, 10243.0),
        (-22209.0, 7665.0),
    ),
    'report_to_the_white_mantle': (
        (200.0, 12400.0),
        (5294.0, -16988.0),
        (1043.0, -16842.0),
        (-3345.0, -16503.0),
        (-8249.0, -15776.0),
        (-10616.0, -16863.0),
        (-11547.0, -19370.0),
        (-11700.0, -19700.0),
        (16506.0, 15402.0),
        (18592.0, 12867.0),
        (21877.0, 9855.0),
    ),
    'mhenlos_request': (
        (1051.0, 9580.0),
        (1323.0, 9767.0),
        (731.0, 11460.0),
        (1338.0, 2070.0),
        (-5302.0, 6909.0),
    ),
    'to_kryta_refugees_icecave_journeyend': (
        (-10800.0, 35400.0),
        (16456.0, -14885.0),
        (13831.0, -13262.0),
        (7011.0, -16575.0),
        (3708.0, -20223.0),
        (-562.0, -19354.0),
        (-3197.0, -17726.0),
        (-6971.0, -17766.0),
        (-7086.0, -20774.0),
        (-10818.0, -21968.0),
        (-13820.0, -23050.0),
        (3191.0, 8329.0),
        (-126.0, 7270.0),
        (-2977.0, 7689.0),
        (-5901.0, 3994.0),
        (-6562.0, -154.0),
        (-3521.0, -1323.0),
        (-1601.0, -3120.0),
        (-2302.0, -7371.0),
        (172.0, -6473.0),
        (-2270.0, -7409.0),
        (-4224.0, -6972.0),
        (-6140.0, -6063.0),
        (-7719.0, -7262.0),
        (-7750.0, -7500.0),
        (7435.0, 6732.0),
        (6179.0, 3505.0),
        (4165.0, -1131.0),
        (1043.0, -2484.0),
        (-2181.0, -5573.0),
        (-1200.0, -7100.0),
        (-2248.0, 25151.0),
        (-701.0, 24655.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'prophecies/passage_through_the_dark_river',
        'title': 'Passage Through the Dark River',
        'factory': 'passage_through_the_dark_river',
        'source_steps': 11,
        'raw_steps': 11,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/report_to_the_white_mantle',
        'title': 'Report to the White Mantle',
        'factory': 'report_to_the_white_mantle',
        'source_steps': 9,
        'raw_steps': 9,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/mhenlos_request',
        'title': "Mhenlo's Request",
        'factory': 'mhenlos_request',
        'source_steps': 17,
        'raw_steps': 17,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/to_kryta_refugees_icecave_journeyend',
        'title': 'To kryta: Refugees',
        'factory': 'to_kryta_refugees_icecave_journeyend',
        'source_steps': 26,
        'raw_steps': 26,
    },
)
