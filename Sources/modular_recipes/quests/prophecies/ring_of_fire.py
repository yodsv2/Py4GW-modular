"""Quests Prophecies Ring Of Fire BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def final_blow() -> BehaviorTree:
    return BT.Sequence(
        name='Final Blow',
        children=[
            BT.Travel(target_map_id=35, leave_party=True),
            BT.Interact(kind='npc', pos=(3415, -10984)),
            BT.Wait(duration_ms=1200),
            BT.Dialog(pos=(3415, -10984), dialog_ids=['0x80D501']),
            BT.Wait(duration_ms=1200),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(3802, -8636), target_map_id=121, move_tolerance=300),
            BT.MoveAndKill(
                pos=[
                    (4602, -6403),
                    (3762, -904),
                    (405, 1578),
                    (-3137, 4954),
                    (-6485, 4724),
                    (-8433, 3640),
                    (-8487, 4509),
                ],
                pause_on_combat=True,
            ),
            BT.Dialog(pos=(-8487, 4509), dialog_ids=['0x2']),
            BT.WaitForMapLoad(map_id=122, timeout_ms=10000),
            BT.Dialog(pos=(6365, -7458), dialog_ids=['0x80D507']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'final_blow': (
        (3802.0, -8636.0),
        (4602.0, -6403.0),
        (3762.0, -904.0),
        (405.0, 1578.0),
        (-3137.0, 4954.0),
        (-6485.0, 4724.0),
        (-8433.0, 3640.0),
        (-8487.0, 4509.0),
    )
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'prophecies/final_blow',
        'title': 'Final Blow',
        'factory': 'final_blow',
        'source_steps': 10,
        'raw_steps': 10,
    },
)
