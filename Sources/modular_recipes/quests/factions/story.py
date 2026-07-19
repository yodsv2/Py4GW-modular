"""Quests Factions Story BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def closer_to_the_stars() -> BehaviorTree:
    return BT.Sequence(
        name='Finding The Oracle',
        children=[
            BT.MoveAndKill(pos=(7364, -4304), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NIKA', dialog_ids=['0x816501']),
            BT.MoveAndKill(pos=(-13871, -11052), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(-14110, -13509), target_map_id=303, move_tolerance=300),
            BT.MoveAndExitMap(pos=(10496, 14777), target_map_id=239, move_tolerance=300),
            BT.MoveAndKill(pos=(-225, 10850), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FISHMONGER_BIHZUN', dialog_ids=['0x816504']),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(-238, 10847), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.Dialog(kind='npc', key='FISHMONGER_BIHZUN', dialog_ids=['0x816504']),
            BT.MoveAndKill(pos=(8979, -19670), pause_on_combat=True),
            BT.Dialog(kind='npc', key='LOUD_KOU', dialog_ids=['0x816504', '0x800008', '0x800009', '0x80000B']),
            BT.WaitForMapLoad(map_id=216, timeout_ms=10000),
            BT.MoveAndKill(pos=(-19804, 9222), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ADEPT_NAI', dialog_ids=['0x816507']),
        ],
    )


def finding_the_oracle() -> BehaviorTree:
    return BT.Sequence(
        name='Finding The Oracle',
        children=[
            BT.Travel(target_map_id=274, leave_party=True),
            BT.Interact(kind='npc', pos=(-11925, 5841)),
            BT.Wait(duration_ms=500),
            BT.Dialog(pos=(-11925, 5841), dialog_ids=['0x816401']),
            BT.Wait(duration_ms=500),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(-12083, 9886), target_map_id=232, move_tolerance=300),
            BT.Dialog(kind='npc', key='BROTHER_MHENLO', dialog_ids=['0x816404']),
            BT.MoveAndKill(pos=(-13016, 15540), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-16176, -15826), target_map_id=240, move_tolerance=300),
            BT.MoveAndKill(pos=(7364, -4304), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.MoveAndKill(pos=(7364, -4304), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NIKA', dialog_ids=['0x816407']),
        ],
    )


def welcome_to_cantha() -> BehaviorTree:
    return BT.Sequence(
        name='Welcome to Cantha',
        children=[
            BT.Dialog(kind='npc', key='DOCKHAND_QUANGNAI', dialog_ids=['0x817901'], pos=(-5161, 6940)),
            BT.Travel(target_map_id=194),
            BT.Move(pos=[(2620, -4140)]),
            BT.CreateParty(henchman_ids=[1, 4, 6, 7, 9, 10, 12], multibox_invite=False, log=True),
            BT.MoveAndExitMap(pos=(3234, -4784), target_map_id=240, move_tolerance=300),
            BT.Move(pos=[(-6991, 18956)]),
            BT.Dialog(kind='npc', key='BROTHER_MHENLO', dialog_ids=['0x817904'], pos=(-7154, 18694)),
            BT.Move(pos=[(4927, 6529)]),
            BT.Wait(duration_ms=11477),
            BT.Move(pos=[(5705, 7052)]),
            BT.Wait(duration_ms=49432),
            BT.Move(pos=[(12400, 4980)]),
            BT.Dialog(kind='npc', key='GUARDSMAN_CHOW', dialog_ids=['0x817904'], pos=(12424, 5116)),
            BT.Dialog(kind='npc', key='GUARDSMAN_CHOW', dialog_ids=['0x800008'], pos=(12424, 5116)),
            BT.Dialog(kind='npc', key='GUARDSMAN_CHOW', dialog_ids=['0x800009'], pos=(12424, 5116)),
            BT.Dialog(kind='npc', key='GUARDSMAN_CHOW', dialog_ids=['0x80000b'], pos=(12424, 5116)),
            BT.WaitForMapLoad(map_id=292, timeout_ms=10000),
            BT.Move(pos=[(-11568, 6853)]),
            BT.CreateParty(hero_ids=[6], multibox_invite=False, log=True),
            BT.Dialog(kind='npc', key='GUARDSMAN_CHOW', dialog_ids=['0x817907'], pos=(-11706, 6950)),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'closer_to_the_stars': (
        (7364.0, -4304.0),
        (-13871.0, -11052.0),
        (-14110.0, -13509.0),
        (10496.0, 14777.0),
        (-225.0, 10850.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (-238.0, 10847.0),
        (8979.0, -19670.0),
        (-19804.0, 9222.0),
    ),
    'finding_the_oracle': (
        (-12083.0, 9886.0),
        (-13016.0, 15540.0),
        (-16176.0, -15826.0),
        (7364.0, -4304.0),
        (7364.0, -4304.0),
    ),
    'welcome_to_cantha': (
        (2620.0, -4140.0),
        (-6991.0, 18956.0),
        (4927.0, 6529.0),
        (5705.0, 7052.0),
        (12400.0, 4980.0),
        (-11568.0, 6853.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'factions/closer_to_the_stars',
        'title': 'Finding The Oracle',
        'factory': 'closer_to_the_stars',
        'source_steps': 30,
        'raw_steps': 16,
    },
    {
        'kind': 'quest',
        'key': 'factions/finding_the_oracle',
        'title': 'Finding The Oracle',
        'factory': 'finding_the_oracle',
        'source_steps': 14,
        'raw_steps': 14,
    },
    {
        'kind': 'quest',
        'key': 'factions/welcome_to_cantha',
        'title': 'Welcome to Cantha',
        'factory': 'welcome_to_cantha',
        'source_steps': 20,
        'raw_steps': 20,
    },
)
