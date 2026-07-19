"""Quests Nightfall Istan BehaviorTree recipes."""

from __future__ import annotations

from Py4GWCoreLib.py4gwcorelib_src.BehaviorTree import BehaviorTree
from Sources.ApoSource.ApoBottingLib import wrappers as BT


def take_the_shortcut() -> BehaviorTree:
    return BT.Sequence(
        name='Take the Shortcut',
        children=[
            BT.Dialog(kind='npc', key='KORMIR', dialog_ids=['0x82a503']),
            BT.Dialog(kind='npc', key='KORMIR', dialog_ids=['0x82a501']),
            BT.GetNodeByProfession(
                DervishNode=BT.EquipItemByModelID(15591),
                ParagonNode=BT.EquipItemByModelID(15593),
                ElementalistNode=BT.EquipItemByModelID(2742),
                MesmerNode=BT.EquipItemByModelID(2652),
                NecromancerNode=BT.EquipItemByModelID(2694),
                RangerNode=BT.EquipItemByModelID(477),
                WarriorNode=BT.EquipItemByModelID(2982),
                MonkNode=BT.EquipItemByModelID(2787),
            ),
            BT.MoveAndKill(pos=[(4653, -1754)], pause_on_combat=False),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_JAHDUGAR', dialog_ids=['0x82a504']),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_JAHDUGAR', dialog_ids=['0x84']),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_JAHDUGAR', dialog_ids=['0x85']),
            BT.WaitForMapLoad(map_id=544, timeout_ms=10000),
            BT.Move(pos=[(3558, -5398)]),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_JAHDUGAR', dialog_ids=['0x82a507']),
        ],
    )


def quiz_the_recruits() -> BehaviorTree:
    return BT.Sequence(
        name='Quiz the Recruits',
        children=[
            BT.Dialog(
                kind='npc',
                key='FIRST_SPEAR_JAHDUGAR',
                dialog_ids=['0x82c503'],
                pos=(3482, -5167),
            ),
            BT.Dialog(
                kind='npc',
                key='FIRST_SPEAR_JAHDUGAR',
                dialog_ids=['0x82c501'],
                pos=(3482, -5167),
            ),
            BT.Dialog(kind='npc', key='SUNSPEAR_RECRUIT', dialog_ids=['0x82c504'], pos=(4776, -6023)),
            BT.Dialog(kind='npc', key='SUNSPEAR_RECRUIT', dialog_ids=['0x82c504'], pos=(5077, -7017)),
            BT.Dialog(kind='npc', key='SUNSPEAR_RECRUIT', dialog_ids=['0x82c504'], pos=(3457, -6284)),
            BT.Dialog(
                kind='npc',
                key='FIRST_SPEAR_JAHDUGAR',
                dialog_ids=['0x82c507'],
                pos=(3482, -5167),
            ),
        ],
    )


def primary_training() -> BehaviorTree:
    return BT.Sequence(
        name='Primary Training',
        children=[
            BT.MoveAndKill(pos=(-7234.90, 4793.62), pause_on_combat=False),
            BT.DialogAtXY(pos=(-7234.90, 4793.62), dialog_id='0x825801'),
            BT.GetNodeByProfession(
                DervishNode=BT.Sequence(
                    name='Primary Training Skills Dervish',
                    children=[
                        BT.MoveAndKill(pos=(-12107, -705), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-12107, -705), dialog_id='0x7f'),
                        BT.MoveAndKill(pos=(-12200, 473), pause_on_combat=False),
                    ],
                ),
                ParagonNode=BT.Sequence(
                    name='Primary Training Skills Paragon',
                    children=[
                        BT.MoveAndKill(pos=(-10724, -3364), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-10724, -3364), dialog_id='0x7f'),
                        BT.MoveAndKill(pos=(-12200, 473), pause_on_combat=False),
                    ],
                ),
                ElementalistNode=BT.Sequence(
                    name='Primary Training Skills Elementalist',
                    children=[
                        BT.MoveAndKill(pos=(-12011.00, -639.00), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-12011.00, -639.00), dialog_id='0x7f'),
                        BT.MoveAndKill(pos=(-12200, 473), pause_on_combat=False),
                    ],
                ),
                MesmerNode=BT.Sequence(
                    name='Primary Training Skills Mesmer',
                    children=[
                        BT.MoveAndKill(pos=(-7149.00, 1830.00), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-7149.00, 1830.00), dialog_id='0x7f'),
                    ],
                ),
                NecromancerNode=BT.Sequence(
                    name='Primary Training Skills Necromancer',
                    children=[
                        BT.MoveAndKill(pos=(-6557.00, 1837.00), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-6557.00, 1837.00), dialog_id='0x7f'),
                    ],
                ),
                RangerNode=BT.Sequence(
                    name='Primary Training Skills Ranger',
                    children=[
                        BT.MoveAndKill(pos=(-9498.00, 1426.00), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-9498.00, 1426.00), dialog_id='0x7f'),
                        BT.MoveAndKill(pos=(-12200, 473), pause_on_combat=False),
                    ],
                ),
                WarriorNode=BT.Sequence(
                    name='Primary Training Skills Warrior',
                    children=[
                        BT.MoveAndKill(pos=(-9663.00, 1506.00), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-9663.00, 1506.00), dialog_id='0x7f'),
                        BT.MoveAndKill(pos=(-12200, 473), pause_on_combat=False),
                    ],
                ),
                MonkNode=BT.Sequence(
                    name='Primary Training Skills Monk',
                    children=[
                        BT.MoveAndKill(pos=(-11658.00, -1414.00), pause_on_combat=False),
                        BT.DialogAtXY(pos=(-11658.00, -1414.00), dialog_id='0x7f'),
                        BT.MoveAndKill(pos=(-12200, 473), pause_on_combat=False),
                    ],
                ),
            ),
            BT.MoveAndKill(pos=(-7234.90, 4793.62), pause_on_combat=False),
            BT.DialogAtXY(pos=(-7234.90, 4793.62), dialog_id='0x825807'),
            BT.CancelSkillRewardWindow(),
        ],
    )


def a_personal_vault() -> BehaviorTree:
    return BT.Sequence(
        name='A Personal Vault',
        children=[
            BT.Travel(target_map_id=449),
            BT.Move(pos=[(-9112, 11868)]),
            BT.Dialog(kind='npc', key='XUNLAI_AGENT_JUEH', dialog_ids=['0x82a101'], pos=(-9297, 11887)),
            BT.Move(pos=[(-7843, 14402)]),
            BT.Dialog(kind='npc', key='XUNLAI_AGENT_STORAGE', dialog_ids=['0x84'], pos=(-7711, 14455)),
            BT.Dialog(kind='npc', key='XUNLAI_AGENT_STORAGE', dialog_ids=['0x85'], pos=(-7711, 14455)),
            BT.Dialog(kind='npc', key='XUNLAI_AGENT_STORAGE', dialog_ids=['0x800001'], pos=(-7711, 14455)),
            BT.Dialog(kind='npc', key='XUNLAI_AGENT_STORAGE', dialog_ids=['0x800002'], pos=(-7711, 14455)),
            BT.Move(pos=[(-9148, 11931)]),
            BT.Dialog(kind='npc', key='XUNLAI_AGENT_JUEH', dialog_ids=['0x82a107'], pos=(-9297, 11887)),
        ],
    )


def material_girl() -> BehaviorTree:
    return BT.Sequence(
        name='Material Girl',
        children=[
            BT.Travel(target_map_id=449),
            BT.Move(pos=[(-11366, 9105)]),
            BT.Dialog(kind='npc', key='KAHLIM_MATERIAL_TRADER', dialog_ids=['0x826103'], pos=(-11442, 9092)),
            BT.Dialog(kind='npc', key='KAHLIM_MATERIAL_TRADER', dialog_ids=['0x826101'], pos=(-11442, 9092)),
            BT.CreateParty(hero_ids=[6], henchman_ids=[1, 2], multibox_invite=False, log=True),
            BT.Move(pos=[(-8473, 14739)]),
            BT.MoveAndExitMap(pos=(-9155, 16843), target_map_id=430, move_tolerance=300),
            BT.Move(pos=[(18342, 913)]),
            BT.Dialog(kind='npc', key='SUNSPEAR_SCOUT', dialog_ids=['0x84'], pos=(18469, 1078)),
            BT.Dialog(kind='npc', key='SUNSPEAR_SCOUT', dialog_ids=['0x85'], pos=(18469, 1078)),
            BT.Move(pos=[(7555, -539), (9358, -1968), (9152, -1342)]),
            BT.Dialog(kind='npc', key='PELEI', dialog_ids=['0x826104'], pos=(9253, -1287)),
            BT.Move(
                pos=[
                    (6386, -2286),
                    (9817, -3860),
                    (11367, -6787),
                    (9507, -9097),
                    (7279, -6558),
                    (3541, -4305),
                    (9108, -1195),
                ]
            ),
            BT.Move(pos=[(9108, -1195)]),
            BT.Dialog(kind='npc', key='PELEI', dialog_ids=['0x826104'], pos=(9253, -1287)),
            BT.Move(pos=[(-3054, 2155)]),
            BT.MoveAndExitMap(pos=(-3136, 3979), target_map_id=431, move_tolerance=300),
            BT.Travel(target_map_id=449),
            BT.Move(pos=[(-10891, 9188)]),
            BT.Dialog(kind='npc', key='KAHLIM_MATERIAL_TRADER', dialog_ids=['0x826107'], pos=(-11442, 9092)),
        ],
    )


def honing_your_skills() -> BehaviorTree:
    return BT.Sequence(
        name='Honing Your Skills',
        children=[
            BT.Travel(target_map_id=449),
            BT.Move(pos=[(-8036, 9745)]),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x828901'], pos=(-7874, 9799)),
            BT.Wait(duration_ms=6966),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x828907'], pos=(-7874, 9799)),
        ],
    )


def secondary_training() -> BehaviorTree:
    learn_necromancer = BT.Sequence(
        name='Secondary Training Learn Necromancer',
        children=[
            BT.Dialog(kind='npc', key='RAFIKI_EXPERT_NECROMANCER', dialog_ids=['0x7f'], pos=(-6557, 1837)),
            BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x825907'),
        ],
    )
    choose_warrior = BT.Sequence(
        name='Secondary Training Choose Warrior',
        children=[
            BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x88'),
            BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x825407'),
            BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x827801'),
        ],
    )
    choose_mesmer = BT.Sequence(
        name='Secondary Training Choose Mesmer',
        children=[
            BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x84'),
            BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x825407'),
            BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x827801'),
        ],
    )

    return BT.Sequence(
        name='Secondary Training',
        children=[
            BT.Travel(target_map_id=449),
            BT.LeaveParty(),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x825901'], pos=(-7910, 9740)),
            BT.Dialog(kind='npc', key='SECOND_SPEAR_BINAH', dialog_ids=['0x84'], pos=(-7525, 6288)),
            BT.WaitForMapLoad(map_id=456, timeout_ms=10000),
            BT.SetAutoCombat(enabled=False),
            BT.GetNodeByProfession(
                NecromancerNode=BT.Sequence(
                    name='Secondary Training Learn Mesmer',
                    children=[
                        BT.DialogAtXY(pos=(-7149, 1830), dialog_id='0x7f'),
                        BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x825907'),
                    ],
                ),
                DervishNode=learn_necromancer,
                ParagonNode=learn_necromancer,
                ElementalistNode=learn_necromancer,
                MesmerNode=learn_necromancer,
                RangerNode=learn_necromancer,
                WarriorNode=learn_necromancer,
                MonkNode=learn_necromancer,
                AssassinNode=learn_necromancer,
                RitualistNode=learn_necromancer,
            ),
            BT.GetNodeByProfession(
                WarriorNode=BT.Sequence(
                    name='Secondary Training Choose Dervish',
                    children=[
                        BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x8a'),
                        BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x825407'),
                        BT.DialogAtXY(pos=(-7161, 4808), dialog_id='0x827801'),
                    ],
                ),
                NecromancerNode=choose_mesmer,
                MonkNode=choose_mesmer,
                ElementalistNode=choose_mesmer,
                DervishNode=choose_warrior,
                ParagonNode=choose_warrior,
                MesmerNode=choose_warrior,
                RangerNode=choose_warrior,
                AssassinNode=choose_warrior,
                RitualistNode=choose_warrior,
            ),
            BT.Travel(target_map_id=449),
            BT.Move(pos=[(-8082, 9709)]),
            BT.LoadParty(max_heroes=4),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x825907'], pos=(-7874, 9799)),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x84'], pos=(-7874, 9799)),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x825407'], pos=(-7874, 9799)),
        ],
    )


def the_honorable_general() -> BehaviorTree:
    return BT.Sequence(
        name='The Honorable General',
        children=[
            BT.Travel(target_map_id=491, leave_party=True),
            BT.MoveAndKill(pos=[(3294, 1641), (2922, 2126)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='DIGMASTER_GATAH', dialog_ids=['0x827901']),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.Travel(target_map_id=502, leave_party=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndKill(pos=(-4255, 729), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-4647, 156), target_map_id=483, move_tolerance=300),
            BT.MoveAndKill(pos=[(16916, -4019), (17288, -5024)], pause_on_combat=True),
            BT.Wait(duration_ms=15000),
            BT.Dialog(kind='npc', key='GENERAL_MORGAHN', dialog_ids=['0x827904', '0x84']),
            BT.MoveAndKill(pos=[(18490, -5864), (17312, -5081)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='GENERAL_MORGAHN', dialog_ids=['0x827904']),
            BT.Travel(target_map_id=502, leave_party=True),
            BT.MoveAndKill(pos=(-1743, 3698), pause_on_combat=True),
            BT.Dialog(kind='npc', key='EMISSARY_DAJMIR', dialog_ids=['0x827907']),
        ],
    )


def signs_and_portents() -> BehaviorTree:
    return BT.Sequence(
        name='Signs and Portents',
        children=[
            BT.Travel(target_map_id=502, leave_party=True),
            BT.MoveAndKill(pos=(-1690, 3754), pause_on_combat=True),
            BT.Dialog(kind='npc', key='EMISSARY_DAJMIR', dialog_ids=['0x827A01']),
            BT.LoadParty(max_heroes=4, required_hero=['Koss']),
            BT.MoveAndKill(pos=(-4128, 859), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-4661, 178), target_map_id=483, move_tolerance=300),
            BT.MoveAndKill(pos=(19726, -4147), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SUNSPEAR_SCOUT', dialog_ids=['0x84']),
            BT.MoveAndKill(pos=(16647, -3808), pause_on_combat=True),
            BT.Dialog(kind='npc', key='EMISSARY_DAJMIR', dialog_ids=['0x827A04']),
            BT.MoveAndKill(pos=(-2004, -13641), pause_on_combat=True),
            BT.Dialog(kind='npc', key='MELONNI', dialog_ids=['0x827A04', '0x84']),
            BT.WaitForMapLoad(map_id=483, timeout_ms=10000),
            BT.MoveAndKill(pos=(-17887, -17582), pause_on_combat=True),
            BT.Dialog(kind='npc', key='INSCRIBED_WALL', dialog_ids=['0x827A04', '0x84', '0x85']),
            BT.WaitForMapLoad(map_id=491, timeout_ms=10000),
            BT.MoveAndKill(pos=(2943, 2079), pause_on_combat=True),
            BT.Dialog(kind='npc', key='DIGMASTER_GATAH', dialog_ids=['0x827A07']),
        ],
    )


def isle_of_the_dead() -> BehaviorTree:
    return BT.Sequence(
        name='Isle of the Dead',
        children=[
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7963, 9784), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x827B03', '0x827B01']),
            BT.Travel(target_map_id=479, leave_party=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndKill(pos=(23672, 6556), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(23393, 6421), target_map_id=432, move_tolerance=300),
            BT.MoveAndKill(pos=[(880, -2573), (748, -2473), (772, -2774)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='NERASHI', dialog_ids=['0x827B04']),
            BT.MoveAndKill(pos=(13908, -8511), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(14920, -10868), target_map_id=487, move_tolerance=300),
            BT.Travel(target_map_id=487, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(-16416, 11455), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-15820, 11247), target_map_id=486, move_tolerance=300),
            BT.MoveAndKill(pos=(-10842, 11359), pause_on_combat=True),
            BT.MoveAndKill(pos=(20, 3297), pause_on_combat=True),
            BT.MoveAndKill(pos=[(14391, 1898), (17580, 2618)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(18765, 12778), (16115, 12694), (17343, 11915)], pause_on_combat=True),
            BT.MoveAndKill(pos=(28311, 6972), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(29206, 6895), target_map_id=489, move_tolerance=300),
            BT.MoveAndKill(pos=(3847, -3771), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(4343, -3643), target_map_id=488, move_tolerance=300),
            BT.MoveAndKill(pos=[(-15276, 15823), (-14642, 14596), (-15452, 13806)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(-3491, 7240), (-3486, 8402), (-2536, 6577)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(4826, -7656), (6995, -8878)], pause_on_combat=True),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7981, 9822), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x827B07']),
        ],
    )


def bad_tide_rising() -> BehaviorTree:
    return BT.Sequence(
        name='Bad Tide Rising',
        children=[
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7971, 9807), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x827C01']),
            BT.MoveAndKill(pos=(-6691, 14919), pause_on_combat=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndExitMap(pos=(-5878, 14918), target_map_id=543, move_tolerance=300),
            BT.MoveAndKill(pos=(-3530, 14673), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GENERAL_YURUKARO', dialog_ids=['0x827C04', '0x86', '0x84']),
            BT.WaitForMapLoad(map_id=422, timeout_ms=10000),
            BT.MoveAndKill(
                pos=[(-9895, 15317), (-11780, 11934), (-10534, 9391), (-8005, 9094)],
                pause_on_combat=True,
            ),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-8011, 9783), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x827C07']),
        ],
    )


def zaishen_elite() -> BehaviorTree:
    return BT.Sequence(
        name='Zaishen Elite',
        children=[
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7894, 14739), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-5939, 14953), target_map_id=543, move_tolerance=300),
            BT.MoveAndKill(pos=(-3593, 14687), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIELD_GENERAL_HAYAO', dialog_ids=['0x826601']),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndKill(pos=(-9056, 16121), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-9242, 16816), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(13488, 3279), pause_on_combat=True),
            BT.Wait(duration_ms=10000),
            BT.WaitForMapLoad(map_id=430, timeout_ms=10000),
            BT.MoveAndKill(pos=(13033, 3537), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIELD_GENERAL_HAYAO', dialog_ids=['0x826607']),
        ],
    )


def student_sousuke() -> BehaviorTree:
    return BT.Sequence(
        name='Student Sousuke',
        children=[
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7755, 14876), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-5924, 14948), target_map_id=543, move_tolerance=300),
            BT.MoveAndKill(pos=(-3634, 14638), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIELD_GENERAL_HAYAO', dialog_ids=['0x826803', '0x826801']),
            BT.Travel(target_map_id=502, leave_party=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndKill(pos=(-4319, 670), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-4705, 157), target_map_id=483, move_tolerance=300),
            BT.MoveAndKill(pos=[(16934, -9707), (17517, -10644)], pause_on_combat=True),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7751, 14907), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-5918, 14907), target_map_id=543, move_tolerance=300),
            BT.MoveAndKill(pos=(-3601, 14650), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIELD_GENERAL_HAYAO', dialog_ids=['0x826807']),
        ],
    )


def special_delivery() -> BehaviorTree:
    return BT.Sequence(
        name='Special Delivery',
        children=[
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7989, 9766), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIRST_SPEAR_DEHVAD', dialog_ids=['0x827D01']),
            BT.MoveAndKill(pos=[(-7805, 14892), (-6932, 14939)], pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-5928, 14961), target_map_id=543, move_tolerance=300),
            BT.MoveAndKill(pos=(-3754, 14612), pause_on_combat=True),
            BT.Dialog(kind='npc', key='FIELD_GENERAL_HAYAO', dialog_ids=['0x827D04']),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=[(-4442, 5268), (-4090, 5389)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x827D04']),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.MoveAndKill(pos=[(-3426, -1765), (-4123, -2281)], pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(-4689, -2313), target_map_id=486, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(26388, 6196), (22440, 2495), (15986, 1620), (14049, 1067)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=3000),
            BT.MoveAndKill(pos=(13938, 934), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JEREK', dialog_ids=['0x827D04']),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4071, 5342), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x827D07']),
        ],
    )


def big_news_small_package() -> BehaviorTree:
    return BT.Sequence(
        name='Big News, Small Package',
        children=[
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4046, 5237), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x827E03', '0x827E01']),
            BT.MoveAndKill(pos=(-3448, 4693), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-3186, 3906), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(-4088, 2485), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JEREK', dialog_ids=['0x827E04']),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndKill(pos=(3595, -3953), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(4355, -3709), target_map_id=488, move_tolerance=300),
            BT.MoveAndKill(pos=(-7141, -2778), pause_on_combat=True),
            BT.OptionalInteractItemByModel(model_id=15793, point=None, max_dist=4500),
            BT.OptionalInteractItemByModel(model_id=17075, point=None, max_dist=4500),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-3315, 4629), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-3085, 3895), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(-3918, 2329), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JEREK', dialog_ids=['0x827E07']),
        ],
    )


def following_the_trail() -> BehaviorTree:
    return BT.Sequence(
        name='Following the Trail',
        children=[
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-3159, 4594), pause_on_combat=True),
            BT.LoadParty(max_heroes=4, required_hero=['Tahlkora']),
            BT.MoveAndExitMap(pos=(-3087, 3925), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(-4013, 2411), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JEREK', dialog_ids=['0x827F01']),
            BT.Travel(target_map_id=491, leave_party=True),
            BT.MoveAndKill(pos=(3826, -4344), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(4735, -4401), target_map_id=432, move_tolerance=300),
            BT.MoveAndKill(pos=[(-21348, 2581), (-19095, -3427), (-15804, -6771)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='CAPTAIN_MINDHEBEH', dialog_ids=['0x827F04', '0x84', '0x85']),
            BT.WaitForMapLoad(map_id=492, timeout_ms=10000),
            BT.MoveAndKill(pos=(1931, 754), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SAVAGE_NUNBE', dialog_ids=['0x827F07']),
        ],
    )


def the_iron_truth() -> BehaviorTree:
    return BT.Sequence(
        name='The Iron Truth',
        children=[
            BT.Dialog(kind='npc', dialog_ids=['0x81', '0x84']),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4114, 5239), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828003', '0x828001']),
            BT.MoveAndExitMap(pos=(-3070, 3914), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(-4000, 2388), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JEREK', dialog_ids=['0x828004']),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.Travel(target_map_id=492, leave_party=True),
            BT.MoveAndKill(pos=(2107, 844), pause_on_combat=True),
            BT.Dialog(kind='npc', key='SAVAGE_NUNBE', dialog_ids=['0x828004']),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.MoveAndKill(pos=(3637, -3918), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(4338, -3671), target_map_id=488, move_tolerance=300),
            BT.MoveAndKill(
                pos=[(-6401, -5666), (436, -11007), (3842, -13987), (9085, -13336)],
                pause_on_combat=True,
            ),
            BT.Wait(duration_ms=3000),
            BT.MoveAndKill(pos=[(8164, -10115), (8459, -12639), (8906, -13387)], pause_on_combat=True),
            BT.Wait(duration_ms=3000),
            BT.Dialog(kind='npc', key='IRONFIST', dialog_ids=['0x828004']),
            BT.Dialog(kind='npc', key='IRONFIST', dialog_ids=['0x828004']),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4041, 5189), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-3119, 3920), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(-4074, 2424), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JEREK', dialog_ids=['0x828007']),
        ],
    )


def trial_by_fire() -> BehaviorTree:
    return BT.Sequence(
        name='Trial by Fire',
        children=[
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndExitMap(pos=(-3070, 3910), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(-4066, 2448), pause_on_combat=True),
            BT.Dialog(kind='npc', key='JEREK', dialog_ids=['0x828101', '0x84']),
            BT.WaitForMapLoad(map_id=423, timeout_ms=10000),
            BT.MoveAndKill(pos=(-4983, 16725), pause_on_combat=True),
            BT.Wait(duration_ms=42600),
            BT.MoveAndKill(pos=(-4782, 16649), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_SUHL', dialog_ids=['0x88']),
            BT.MoveAndKill(pos=(-4896, 16735), pause_on_combat=True),
            BT.Wait(duration_ms=64500),
            BT.MoveAndKill(pos=(-4751, 16829), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GENERAL_MORGAHN', dialog_ids=['0x85']),
            BT.MoveAndKill(pos=(-4722, 16656), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_SUHL', dialog_ids=['0x84']),
            BT.MoveAndKill(pos=(-4868, 16673), pause_on_combat=True),
            BT.Wait(duration_ms=78400),
            BT.MoveAndKill(pos=(-4727, 16823), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GENERAL_MORGAHN', dialog_ids=['0x87']),
            BT.MoveAndKill(pos=(-4720, 16641), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ELDER_SUHL', dialog_ids=['0x86']),
            BT.MoveAndKill(pos=(-4877, 16694), pause_on_combat=True),
            BT.Wait(duration_ms=55700),
            BT.MoveAndKill(pos=(-4733, 16843), pause_on_combat=True),
            BT.Dialog(kind='npc', key='GENERAL_MORGAHN', dialog_ids=['0x8A']),
            BT.MoveAndKill(pos=(-4831, 16741), pause_on_combat=True),
            BT.Wait(duration_ms=88000),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4000, 5319), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828107']),
        ],
    )


def war_preparations_recruit_training() -> BehaviorTree:
    return BT.Sequence(
        name='War Preparations (Recruit Training)',
        children=[
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-3915, 5352), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828203', '0x828201']),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-9223, 16397), pause_on_combat=True),
            BT.LoadParty(max_heroes=4),
            BT.MoveAndExitMap(pos=(-9270, 16806), target_map_id=430, move_tolerance=300),
            BT.MoveAndKill(pos=(16504, 2244), pause_on_combat=True),
            BT.Dialog(kind='npc', key='KORMIR', dialog_ids=['0x828204']),
            BT.MoveAndKill(pos=(17238, 1677), pause_on_combat=True),
            BT.Dialog(kind='npc', key='NERASHI', dialog_ids=['0x828204']),
            BT.MoveAndKill(pos=[(6297, -11273), (5615, -11959)], pause_on_combat=True),
            BT.MoveAndKill(pos=[(6682, -9365), (16503, 926), (17845, 1421)], pause_on_combat=True),
            BT.Dialog(kind='npc', key='AHTOK', dialog_ids=['0x828204']),
            BT.MoveAndKill(pos=(18211, 1439), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ROJIS', dialog_ids=['0x828204']),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4126, 5338), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828207']),
        ],
    )


def war_preparations_ghost_reconnaissance() -> BehaviorTree:
    return BT.Sequence(
        name='War Preparations (Ghost Reconnaissance)',
        children=[
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4086, 5343), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828403', '0x828401']),
            BT.Travel(target_map_id=492, leave_party=True),
            BT.MoveAndKill(pos=(249, -3037), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(347, -4492), target_map_id=484, move_tolerance=300),
            BT.MoveAndKill(pos=[(11315, 2931), (11429, 4772)], pause_on_combat=True),
            BT.Wait(duration_ms=1400),
            BT.SendChatCommand(command='kneel'),
            BT.Wait(duration_ms=28000),
            BT.MoveAndKill(
                pos=[(11552, 4953), (11199, 4782), (11433, 4435), (11347, 4715)],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='SOGOLON_THE_PROTECTOR', dialog_ids=['0x828404']),
            BT.Travel(target_map_id=492, leave_party=True),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4006, 5326), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828407']),
        ],
    )


def war_preparations_wind_and_water() -> BehaviorTree:
    return BT.Sequence(
        name='War Preparations (Wind and Water)',
        children=[
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4018, 5311), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828303', '0x828301']),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.MoveAndKill(pos=(-3460, 2108), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CAPTAIN_BOLDUHR', dialog_ids=['0x828304']),
            BT.MoveAndKill(pos=(3731, -3955), pause_on_combat=True),
            BT.LoadParty(max_heroes=8),
            BT.MoveAndExitMap(pos=(4343, -3686), target_map_id=488, move_tolerance=300),
            BT.MoveAndKill(pos=(-15203, 8261), pause_on_combat=True),
            BT.Wait(duration_ms=20000),
            BT.MoveAndKill(
                pos=[(-15405, 8144), (-14826, 8499), (-15535, 7993), (-14913, 8371), (-15419, 8030)],
                pause_on_combat=True,
            ),
            BT.Dialog(kind='npc', key='KINYA_KELA', dialog_ids=['0x828304']),
            BT.Travel(target_map_id=489, leave_party=True),
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4004, 5335), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828307']),
        ],
    )


def the_time_is_nigh() -> BehaviorTree:
    return BT.Sequence(
        name='The Time is Nigh',
        children=[
            BT.Travel(target_map_id=431, leave_party=True),
            BT.MoveAndKill(pos=(-4043, 5316), pause_on_combat=True),
            BT.Dialog(kind='npc', key='CASTELLAN_PUUBA', dialog_ids=['0x828503', '0x828501']),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7447, 6474), pause_on_combat=True),
            BT.LoadParty(max_heroes=4),
            BT.Dialog(kind='npc', key='SECOND_SPEAR_BINAH', dialog_ids=['0x81', '0x84']),
            BT.MoveAndKill(pos=(-1277, 1099), pause_on_combat=True),
            BT.Wait(duration_ms=42000),
            BT.Dialog(kind='npc', key='KORMIR', dialog_ids=['0x828504']),
            BT.Travel(target_map_id=449, leave_party=True),
            BT.MoveAndKill(pos=(-7464, 16387), pause_on_combat=True),
            BT.MoveAndExitMap(pos=(-5954, 16721), target_map_id=429, move_tolerance=300),
            BT.MoveAndKill(pos=(-4746, 16739), pause_on_combat=True),
            BT.Dialog(kind='npc', key='ASSISTANT_HAHNNA', dialog_ids=['0x828504', '0x84', '0x85']),
            BT.WaitForMapLoad(map_id=493, timeout_ms=10000),
            BT.MoveAndKill(pos=(-1631, 16737), pause_on_combat=True),
            BT.Dialog(kind='npc', key='RAIDMARSHAL_MEHDARA', dialog_ids=['0x82E207']),
        ],
    )


ROUTE_POINTS_BY_RECIPE: dict[str, tuple[tuple[float, float], ...]] = {
    'take_the_shortcut': ((4653.0, -1754.0), (3558.0, -5398.0)),
    'quiz_the_recruits': (
        (3482.0, -5167.0),
        (4776.0, -6023.0),
        (5077.0, -7017.0),
        (3457.0, -6284.0),
        (3482.0, -5167.0),
    ),
    'primary_training': (
        (-7234.90, 4793.62),
        (-12107.0, -705.0),
        (-10724.0, -3364.0),
        (-12011.0, -639.0),
        (-7149.0, 1830.0),
        (-6557.0, 1837.0),
        (-9498.0, 1426.0),
        (-9663.0, 1506.0),
        (-11658.0, -1414.0),
        (-12200.0, 473.0),
        (-7234.90, 4793.62),
    ),
    'a_personal_vault': (
        (-9112.0, 11868.0),
        (-7843.0, 14402.0),
        (-9148.0, 11931.0),
    ),
    'material_girl': (
        (-11366.0, 9105.0),
        (-8473.0, 14739.0),
        (18342.0, 913.0),
        (7555.0, -539.0),
        (9358.0, -1968.0),
        (9152.0, -1342.0),
        (6386.0, -2286.0),
        (9817.0, -3860.0),
        (11367.0, -6787.0),
        (9507.0, -9097.0),
        (7279.0, -6558.0),
        (3541.0, -4305.0),
        (9108.0, -1195.0),
        (-3054.0, 2155.0),
        (-10891.0, 9188.0),
    ),
    'honing_your_skills': ((-8036.0, 9745.0),),
    'secondary_training': (
        (-7910.0, 9740.0),
        (-7525.0, 6288.0),
        (-7149.0, 1830.0),
        (-6557.0, 1837.0),
        (-7161.0, 4808.0),
    ),
    'the_honorable_general': (
        (3294.0, 1641.0),
        (2922.0, 2126.0),
        (-4255.0, 729.0),
        (-4647.0, 156.0),
        (16916.0, -4019.0),
        (17288.0, -5024.0),
        (18490.0, -5864.0),
        (17312.0, -5081.0),
        (-1743.0, 3698.0),
    ),
    'signs_and_portents': (
        (-1690.0, 3754.0),
        (-4128.0, 859.0),
        (-4661.0, 178.0),
        (19726.0, -4147.0),
        (16647.0, -3808.0),
        (-2004.0, -13641.0),
        (-17887.0, -17582.0),
        (2943.0, 2079.0),
    ),
    'isle_of_the_dead': (
        (-7963.0, 9784.0),
        (23672.0, 6556.0),
        (23393.0, 6421.0),
        (880.0, -2573.0),
        (748.0, -2473.0),
        (772.0, -2774.0),
        (13908.0, -8511.0),
        (14920.0, -10868.0),
        (-16416.0, 11455.0),
        (-15820.0, 11247.0),
        (-10842.0, 11359.0),
        (20.0, 3297.0),
        (14391.0, 1898.0),
        (17580.0, 2618.0),
        (18765.0, 12778.0),
        (16115.0, 12694.0),
        (17343.0, 11915.0),
        (28311.0, 6972.0),
        (29206.0, 6895.0),
        (3847.0, -3771.0),
        (4343.0, -3643.0),
        (-15276.0, 15823.0),
        (-14642.0, 14596.0),
        (-15452.0, 13806.0),
        (-3491.0, 7240.0),
        (-3486.0, 8402.0),
        (-2536.0, 6577.0),
        (4826.0, -7656.0),
        (6995.0, -8878.0),
        (-7981.0, 9822.0),
    ),
    'bad_tide_rising': (
        (-7971.0, 9807.0),
        (-6691.0, 14919.0),
        (-5878.0, 14918.0),
        (-3530.0, 14673.0),
        (-9895.0, 15317.0),
        (-11780.0, 11934.0),
        (-10534.0, 9391.0),
        (-8005.0, 9094.0),
        (-8011.0, 9783.0),
    ),
    'zaishen_elite': (
        (-7894.0, 14739.0),
        (-5939.0, 14953.0),
        (-3593.0, 14687.0),
        (-9056.0, 16121.0),
        (-9242.0, 16816.0),
        (13488.0, 3279.0),
        (13033.0, 3537.0),
    ),
    'student_sousuke': (
        (-7755.0, 14876.0),
        (-5924.0, 14948.0),
        (-3634.0, 14638.0),
        (-4319.0, 670.0),
        (-4705.0, 157.0),
        (16934.0, -9707.0),
        (17517.0, -10644.0),
        (-7751.0, 14907.0),
        (-5918.0, 14907.0),
        (-3601.0, 14650.0),
    ),
    'special_delivery': (
        (-7989.0, 9766.0),
        (-7805.0, 14892.0),
        (-6932.0, 14939.0),
        (-5928.0, 14961.0),
        (-3754.0, 14612.0),
        (-4442.0, 5268.0),
        (-4090.0, 5389.0),
        (-3426.0, -1765.0),
        (-4123.0, -2281.0),
        (-4689.0, -2313.0),
        (26388.0, 6196.0),
        (22440.0, 2495.0),
        (15986.0, 1620.0),
        (14049.0, 1067.0),
        (13938.0, 934.0),
        (-4071.0, 5342.0),
    ),
    'big_news_small_package': (
        (-4046.0, 5237.0),
        (-3448.0, 4693.0),
        (-3186.0, 3906.0),
        (-4088.0, 2485.0),
        (3595.0, -3953.0),
        (4355.0, -3709.0),
        (-7141.0, -2778.0),
        (-3315.0, 4629.0),
        (-3085.0, 3895.0),
        (-3918.0, 2329.0),
    ),
    'following_the_trail': (
        (-3159.0, 4594.0),
        (-3087.0, 3925.0),
        (-4013.0, 2411.0),
        (3826.0, -4344.0),
        (4735.0, -4401.0),
        (-21348.0, 2581.0),
        (-19095.0, -3427.0),
        (-15804.0, -6771.0),
        (1931.0, 754.0),
    ),
    'the_iron_truth': (
        (-4114.0, 5239.0),
        (-3070.0, 3914.0),
        (-4000.0, 2388.0),
        (2107.0, 844.0),
        (3637.0, -3918.0),
        (4338.0, -3671.0),
        (-6401.0, -5666.0),
        (436.0, -11007.0),
        (3842.0, -13987.0),
        (9085.0, -13336.0),
        (8164.0, -10115.0),
        (8459.0, -12639.0),
        (8906.0, -13387.0),
        (-4041.0, 5189.0),
        (-3119.0, 3920.0),
        (-4074.0, 2424.0),
    ),
    'trial_by_fire': (
        (-3070.0, 3910.0),
        (-4066.0, 2448.0),
        (-4983.0, 16725.0),
        (-4782.0, 16649.0),
        (-4896.0, 16735.0),
        (-4751.0, 16829.0),
        (-4722.0, 16656.0),
        (-4868.0, 16673.0),
        (-4727.0, 16823.0),
        (-4720.0, 16641.0),
        (-4877.0, 16694.0),
        (-4733.0, 16843.0),
        (-4831.0, 16741.0),
        (-4000.0, 5319.0),
    ),
    'war_preparations_recruit_training': (
        (-3915.0, 5352.0),
        (-9223.0, 16397.0),
        (-9270.0, 16806.0),
        (16504.0, 2244.0),
        (17238.0, 1677.0),
        (6297.0, -11273.0),
        (5615.0, -11959.0),
        (6682.0, -9365.0),
        (16503.0, 926.0),
        (17845.0, 1421.0),
        (18211.0, 1439.0),
        (-4126.0, 5338.0),
    ),
    'war_preparations_ghost_reconnaissance': (
        (-4086.0, 5343.0),
        (249.0, -3037.0),
        (347.0, -4492.0),
        (11315.0, 2931.0),
        (11429.0, 4772.0),
        (11552.0, 4953.0),
        (11199.0, 4782.0),
        (11433.0, 4435.0),
        (11347.0, 4715.0),
        (-4006.0, 5326.0),
    ),
    'war_preparations_wind_and_water': (
        (-4018.0, 5311.0),
        (-3460.0, 2108.0),
        (3731.0, -3955.0),
        (4343.0, -3686.0),
        (-15203.0, 8261.0),
        (-15405.0, 8144.0),
        (-14826.0, 8499.0),
        (-15535.0, 7993.0),
        (-14913.0, 8371.0),
        (-15419.0, 8030.0),
        (-4004.0, 5335.0),
    ),
    'the_time_is_nigh': (
        (-4043.0, 5316.0),
        (-7447.0, 6474.0),
        (-1277.0, 1099.0),
        (-7464.0, 16387.0),
        (-5954.0, 16721.0),
        (-4746.0, 16739.0),
        (-1631.0, 16737.0),
    ),
}


RECIPES: tuple[dict[str, object], ...] = (
    {
        'kind': 'quest',
        'key': 'nightfall/take_the_shortcut',
        'title': 'Take the Shortcut',
        'factory': 'take_the_shortcut',
        'source_steps': 10,
        'raw_steps': 10,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/quiz_the_recruits',
        'title': 'Quiz the Recruits',
        'factory': 'quiz_the_recruits',
        'source_steps': 6,
        'raw_steps': 6,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/primary_training',
        'title': 'Primary Training',
        'factory': 'primary_training',
        'source_steps': 6,
        'raw_steps': 6,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/a_personal_vault',
        'title': 'A Personal Vault',
        'factory': 'a_personal_vault',
        'source_steps': 10,
        'raw_steps': 10,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/material_girl',
        'title': 'Material Girl',
        'factory': 'material_girl',
        'source_steps': 20,
        'raw_steps': 20,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/honing_your_skills',
        'title': 'Honing Your Skills',
        'factory': 'honing_your_skills',
        'source_steps': 5,
        'raw_steps': 5,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/secondary_training',
        'title': 'Secondary Training',
        'factory': 'secondary_training',
        'source_steps': 8,
        'raw_steps': 8,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/the_honorable_general',
        'title': 'The Honorable General',
        'factory': 'the_honorable_general',
        'source_steps': 16,
        'raw_steps': 16,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/signs_and_portents',
        'title': 'Signs and Portents',
        'factory': 'signs_and_portents',
        'source_steps': 18,
        'raw_steps': 18,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/isle_of_the_dead',
        'title': 'Isle of the Dead',
        'factory': 'isle_of_the_dead',
        'source_steps': 30,
        'raw_steps': 30,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/bad_tide_rising',
        'title': 'Bad Tide Rising',
        'factory': 'bad_tide_rising',
        'source_steps': 13,
        'raw_steps': 13,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/zaishen_elite',
        'title': 'Zaishen Elite',
        'factory': 'zaishen_elite',
        'source_steps': 14,
        'raw_steps': 14,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/student_sousuke',
        'title': 'Student Sousuke',
        'factory': 'student_sousuke',
        'source_steps': 15,
        'raw_steps': 15,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/special_delivery',
        'title': 'Special Delivery',
        'factory': 'special_delivery',
        'source_steps': 22,
        'raw_steps': 22,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/big_news_small_package',
        'title': 'Big News, Small Package',
        'factory': 'big_news_small_package',
        'source_steps': 20,
        'raw_steps': 20,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/following_the_trail',
        'title': 'Following the Trail',
        'factory': 'following_the_trail',
        'source_steps': 14,
        'raw_steps': 14,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/the_iron_truth',
        'title': 'The Iron Truth',
        'factory': 'the_iron_truth',
        'source_steps': 27,
        'raw_steps': 27,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/trial_by_fire',
        'title': 'Trial by Fire',
        'factory': 'trial_by_fire',
        'source_steps': 30,
        'raw_steps': 30,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/war_preparations_recruit_training',
        'title': 'War Preparations (Recruit Training)',
        'factory': 'war_preparations_recruit_training',
        'source_steps': 19,
        'raw_steps': 19,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/war_preparations_ghost_reconnaissance',
        'title': 'War Preparations (Ghost Reconnaissance)',
        'factory': 'war_preparations_ghost_reconnaissance',
        'source_steps': 17,
        'raw_steps': 17,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/war_preparations_wind_and_water',
        'title': 'War Preparations (Wind and Water)',
        'factory': 'war_preparations_wind_and_water',
        'source_steps': 17,
        'raw_steps': 17,
    },
    {
        'kind': 'quest',
        'key': 'nightfall/the_time_is_nigh',
        'title': 'The Time is Nigh',
        'factory': 'the_time_is_nigh',
        'source_steps': 18,
        'raw_steps': 18,
    },
)
