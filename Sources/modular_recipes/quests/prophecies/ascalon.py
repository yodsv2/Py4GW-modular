"""Quests Prophecies Ascalon BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def altheas_ashes() -> BehaviorTree:
    return BT.Sequence(
        name="Althea's Ashes",
        children=[
            BT.Travel(target_map_id=40, leave_party=True),
            BT.Dialog(kind='npc', key='DUKE_BARRADIN', dialog_ids=['0x807B03', '0x807B01']),
            BT.Travel(target_map_id=36, leave_party=True),
            BT.MoveAndExitMap(pos=(1854, 13590), target_map_id=13, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(6190, 9828), (15764, 7523), (21129, 15655), (21431, 16614)],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(21365, 17259), target_map_id=106, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(-15736, -6954), (-5938, -2411), (-5984, -2488)], pause_on_combat=True
            ),
            BT.Interact(kind='gadget', key='CHARR_ALTAR', pos=(-6041, -2480)),
            BT.Travel(target_map_id=40, leave_party=True),
            BT.MoveAndKill(pos=(20667, 9084), pause_on_combat=True),
            BT.Dialog(kind='npc', key='DUKE_BARRADIN', dialog_ids=['0x807B07']),
        ],
    )


def ruins_of_surmia() -> BehaviorTree:
    return BT.Sequence(
        name='Ruins of Surmia',
        children=[
            BT.Travel(target_map_id=135, leave_party=True),
            BT.Interact(kind='npc', pos=(-16475, 3899)),
            BT.Wait(duration_ms=2000),
            BT.Dialog(pos=(-16475, 3899), dialog_ids=['0x80A503', '0x80A501'], interval_ms=2000),
            BT.Wait(duration_ms=2000),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndExitMap(pos=(-14000, 4350), target_map_id=107, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(-10719, 4271), (-8020, 9803), (-12602, 11498), (-13260, 14111), (-17824, 11671), (-19766, 10999)],
                pause_on_combat=True,
            ),
            BT.MoveAndExitMap(pos=(-19990, 10900), target_map_id=30, move_tolerance=300),
            BT.Dialog(pos=(-3503, -13764), dialog_ids=['0x80A507']),
        ],
    )


def the_dukes_daughter() -> BehaviorTree:
    return BT.Sequence(
        name="The Duke's Daughter",
        children=[
            BT.Travel(target_map_id=40, leave_party=True),
            BT.Dialog(kind='npc', key='VIGGO', dialog_ids=['0x808101']),
            BT.Travel(target_map_id=36, leave_party=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndExitMap(pos=(1926, 13682), target_map_id=13, move_tolerance=300),
            BT.MoveAndKill(pos=(10503, -7820), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GHOST_OF_ALTHEA', dialog_ids=['0x808104']),
            BT.Travel(target_map_id=40, leave_party=True),
            BT.Dialog(kind='npc', key='DUKE_BARRADIN', dialog_ids=['0x808107']),
        ],
    )


def the_elementalist_path() -> BehaviorTree:
    return BT.Sequence(
        name='The Elementalist Path',
        children=[
            BT.Travel(target_map_id=152, leave_party=True),
            BT.MoveAndKill(pos=(-18390, -17652), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CEMBRIEN', dialog_ids=['0x801F01']),
            BT.Travel(target_map_id=38, leave_party=True),
            BT.LoadParty(max_heroes=6),
            BT.MoveAndKill(pos=(-18966, -321), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-20011, -301), target_map_id=113, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(4166, -2345), (4328, -3822), (3903, -1628)], pause_on_combat=True
            ),
            BT.OptionalInteractItemByModel(model_id=2546, point=None, max_dist=4500),
            BT.Travel(target_map_id=152, leave_party=True),
            BT.MoveAndKill(pos=(-18442, -17662), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CEMBRIEN', dialog_ids=['0x801F07']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'altheas_ashes': (
        (1854.0, 13590.0),
        (6190.0, 9828.0),
        (15764.0, 7523.0),
        (21129.0, 15655.0),
        (21431.0, 16614.0),
        (21365.0, 17259.0),
        (-15736.0, -6954.0),
        (-5938.0, -2411.0),
        (-5984.0, -2488.0),
        (20667.0, 9084.0),
    ),
    'ruins_of_surmia': (
        (-14000.0, 4350.0),
        (-10719.0, 4271.0),
        (-8020.0, 9803.0),
        (-12602.0, 11498.0),
        (-13260.0, 14111.0),
        (-17824.0, 11671.0),
        (-19766.0, 10999.0),
        (-19990.0, 10900.0),
    ),
    'the_dukes_daughter': ((1926.0, 13682.0), (10503.0, -7820.0)),
    'the_elementalist_path': (
        (-18390.0, -17652.0),
        (-18966.0, -321.0),
        (-20011.0, -301.0),
        (4166.0, -2345.0),
        (4328.0, -3822.0),
        (3903.0, -1628.0),
        (-18442.0, -17662.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'prophecies/altheas_ashes',
        'title': "Althea's Ashes",
        'factory': 'altheas_ashes',
        'source_steps': 11,
        'raw_steps': 11,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/ruins_of_surmia',
        'title': 'Ruins of Surmia',
        'factory': 'ruins_of_surmia',
        'source_steps': 8,
        'raw_steps': 8,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/the_dukes_daughter',
        'title': "The Duke's Daughter",
        'factory': 'the_dukes_daughter',
        'source_steps': 9,
        'raw_steps': 9,
    },
    {
        'kind': 'quest',
        'key': 'prophecies/the_elementalist_path',
        'title': 'The Elementalist Path',
        'factory': 'the_elementalist_path',
        'source_steps': 12,
        'raw_steps': 12,
    },
)
