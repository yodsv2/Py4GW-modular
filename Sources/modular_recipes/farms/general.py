"""Farms General BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def cleaner() -> BehaviorTree:
    return BT.Succeeder(name='Inventory Cleaner::NoOp')


def farmer_hamnet() -> BehaviorTree:
    return BT.Sequence(
        name='Farmer Hamnet',
        children=[
            BT.MoveAndExitMap(pos=(392, 7782), target_map_id=161, move_tolerance=300),
            BT.MoveAndKill(pos=[(2353, 6219), (2683, 4302)], pause_on_combat=True),
            BT.Travel(target_map_id=165, leave_party=True),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'cleaner': (),
    'farmer_hamnet': ((392.0, 7782.0), (2353.0, 6219.0), (2683.0, 4302.0)),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'farm',
        'key': 'cleaner',
        'title': 'Inventory Cleaner',
        'factory': 'cleaner',
        'source_steps': 0,
        'raw_steps': 0,
    },
    {
        'kind': 'farm',
        'key': 'farmer_hamnet',
        'title': 'Farmer Hamnet',
        'factory': 'farmer_hamnet',
        'source_steps': 3,
        'raw_steps': 3,
    },
)
