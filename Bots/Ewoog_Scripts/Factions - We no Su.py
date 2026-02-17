"""
Factions — We no Su — ModularBot conversion.

Demonstrates:
- loop=False (linear questline — runs once, does NOT repeat)
- Per-phase managed coroutines (added/removed inside phase functions)
- Botting kwargs pass-through (upkeep config)
- Many phases (~8) with distinct quest logic
"""

from __future__ import annotations

import sys, os
import Py4GW

bots_dir = os.path.join(Py4GW.Console.get_projects_path(), "Bots")
if bots_dir not in sys.path:
    sys.path.insert(0, bots_dir)

from Py4GWCoreLib import (GLOBAL_CACHE, Routines, ModelID, Botting, Player)
from modular_bot import ModularBot, Phase

# ── Constants ─────────────────────────────────────────────────────────────────

MARKETPLACE = 303


# ── Multibox consumable upkeep (unchanged from original) ──────────────────────

def _upkeep_multibox_consumables(bot: Botting):
    """Background coroutine: keep pcons active on all accounts."""
    while True:
        yield from bot.Wait._coro_for_time(15000)
        if not Routines.Checks.Map.MapValid():
            continue
        if Routines.Checks.Map.IsOutpost():
            continue

        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Essence_Of_Celerity.value, GLOBAL_CACHE.Skill.GetID("Essence_of_Celerity_item_effect"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Grail_Of_Might.value, GLOBAL_CACHE.Skill.GetID("Grail_of_Might_item_effect"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Armor_Of_Salvation.value, GLOBAL_CACHE.Skill.GetID("Armor_of_Salvation_item_effect"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Birthday_Cupcake.value, GLOBAL_CACHE.Skill.GetID("Birthday_Cupcake_skill"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Golden_Egg.value, GLOBAL_CACHE.Skill.GetID("Golden_Egg_skill"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Candy_Corn.value, GLOBAL_CACHE.Skill.GetID("Candy_Corn_skill"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Candy_Apple.value, GLOBAL_CACHE.Skill.GetID("Candy_Apple_skill"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Slice_Of_Pumpkin_Pie.value, GLOBAL_CACHE.Skill.GetID("Pie_Induced_Ecstasy"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Drake_Kabob.value, GLOBAL_CACHE.Skill.GetID("Drake_Skin"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Bowl_Of_Skalefin_Soup.value, GLOBAL_CACHE.Skill.GetID("Skale_Vigor"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.Pahnai_Salad.value, GLOBAL_CACHE.Skill.GetID("Pahnai_Salad_item_effect"), 0, 0))
        yield from bot.helpers.Multibox._use_consumable_message((ModelID.War_Supplies.value, GLOBAL_CACHE.Skill.GetID("Well_Supplied"), 0, 0))
        for i in range(1, 5):
            GLOBAL_CACHE.Inventory.UseItem(ModelID.Honeycomb.value)
            yield from bot.Wait._coro_for_time(250)


# ── Phases (identical bodies to original) ─────────────────────────────────────

def travel_to_marketplace(bot: Botting):
    bot.Map.Travel(MARKETPLACE)
    bot.Wait.ForMapLoad(target_map_id=MARKETPLACE)
    bot.Move.XYAndExitMap(10672, 14376, 239)

def wajjun_bazaar(bot: Botting):
    WAJJUNBAZAARTOTOGO = [(9366.0, 14052), (4233, 13003), (3937, 6315), (-1526, 6795)]
    bot.Move.FollowAutoPath(WAJJUNBAZAARTOTOGO, "Wajjun Bazaar to Master Togo")
    bot.Move.XYAndDialog(-1813, 6920, 0x815D04)
    TOGOTOJIA = [(-2078.0, -3217), (4732, -4583), (9585, -5196), (12657, -5690), (15548, -9503), (16364, -9887)]
    bot.Move.FollowAutoPath(TOGOTOJIA, "Master Togo to Jia")
    bot.Move.XYAndDialog(10808.49, -6569, 0x815D04)
    bot.Wait.ForTime(400)

def kaineng_docks(bot: Botting):
    bot.Map.Travel(MARKETPLACE)
    bot.Move.XYAndExitMap(11295, 19509, 302)
    bot.Wait.ForMapLoad(target_map_id=302)
    bot.Move.XYAndDialog(9963, 20135, 0x815D07)
    bot.Move.XYAndDialog(9963, 20135, 0x817801)
    bot.Map.Travel(MARKETPLACE)
    bot.Wait.ForMapLoad(MARKETPLACE)
    bot.Move.XYAndExitMap(10672, 14376, 239)

def wajjun_bazaar_mayhem(bot: Botting):
    WAJJUNBAZAARTOKISAI = [(8728.0, 13952), (3160, 12596), (-4562, 12037), (-7724, 10410)]
    bot.Move.FollowAutoPath(WAJJUNBAZAARTOKISAI, "Wajjun Bazaar to Kisai")
    bot.Move.XYAndDialog(-8459, 10312, 0x817804)
    bot.Wait.ForTime(1000)
    bot.Move.XYAndDialog(-8142, 10104, 0x817804)
    bot.Move.XY(-3691, -1477)
    bot.Move.XYAndDialog(-3909, -2172, 0x817804)
    bot.Wait.ForTime(1000)
    bot.Move.XYAndDialog(-3809, -1779, 0x817804)
    bot.Wait.ForTime(1000)
    bot.Move.XYAndDialog(-4446, -1166, 0x817804)
    PATH2 = [(-2078.0, -3217), (4732, -4583), (14892, -9447), (16815, -9739)]
    bot.Move.FollowAutoPath(PATH2, "To Kisai to Turn in Quest")
    bot.Move.XYAndExitMap(18654, -10012, 241)
    bot.Wait.ForMapLoad(241)
    PATH3 = [(-14284.0, -5899), (-14272, 960), (-10521, 2585), (-10318, 10272), (-6000, 5087), (-1943, 7392), (283, 5556)]
    bot.Move.FollowAutoPath(PATH3, "Traverse Undercity")
    bot.Move.XYAndDialog(1479, 6122, 0x817804)
    bot.Wait.ForTime(1000)
    bot.Move.XYAndDialog(1389, 6119, 0x817804)
    bot.Dialogs.WithModel(54, 0x817804)
    PATH4 = [(2728.0, 5888), (11567, 6911), (17882, 10144), (17799, 14667)]
    bot.Move.FollowAutoPath(PATH4, "To Guardsman Pai")
    bot.Move.XYAndDialog(18081, 15275, 0x817804)
    bot.Wait.ForTime(500)
    bot.Move.XYAndDialog(18081, 15275, 0x800008)
    bot.Wait.ForTime(500)
    bot.Move.XYAndDialog(18081, 15275, 0x800009)
    bot.Wait.ForTime(500)
    bot.Move.XYAndDialog(18081, 15275, 0x80000B)
    bot.Wait.ForMapLoad(291)
    bot.Move.XYAndDialog(-7662, -16661, 0x817807)

def vizunah_square(bot: Botting):
    bot.Map.Travel(291)
    bot.Map.EnterChallenge(30000, target_map_id=215)
    bot.Wait.ForTime(60000)
    bot.States.AddManagedCoroutine("Upkeep Multibox Consumables", lambda: _upkeep_multibox_consumables(bot))
    bot.Move.XY(-3921, -6560)
    def _exit_condition():
        pos = Player.GetXY()
        if not pos:
            return False
        dx = pos[0] - 3131.0
        dy = pos[1] - (-16893.0)
        return (dx * dx + dy * dy) <= (1000.0 * 1000.0)
    bot.Move.FollowModel(3120, 100, exit_condition=lambda: _exit_condition())
    bot.Move.XY(377, -17383)
    bot.Wait.UntilOutOfCombat()
    bot.States.RemoveManagedCoroutine("Upkeep Multibox Consumables")
    bot.Wait.ForMapLoad(274)

def dragons_throat(bot: Botting):
    bot.Map.Travel(274)
    bot.Move.XYAndDialog(-11951, 5967, 0x816401)
    bot.Move.XYAndExitMap(-12042, 10529, 232)
    bot.Move.XYAndDialog(3477, 14804, 0x816404)
    PATH1 = [(3306.0, 14156), (3243, 18509), (-932, 13805), (-4580, 16829), (-8219, 18340), (-12197, 17652), (-12916, 15574)]
    bot.Move.FollowAutoPath(PATH1, "Traverse Shadow's Passage")
    bot.Move.XYAndExitMap(-15537, 15682, 240)
    PATH2 = [(10726, 12554.0), (5503, 9252), (7524, 6065), (7620, 1889), (5196, -2510), (7264, -4200)]
    bot.Move.FollowAutoPath(PATH2, "Traverse Budek Byway")
    bot.Move.XYAndDialog(7539, -4371, 0x816407)
    bot.Move.XYAndDialog(7539, -4371, 0x816501)

def closer_to_the_stars(bot: Botting):
    bot.Map.Travel(MARKETPLACE)
    bot.Move.XYAndExitMap(10672, 14376, 239)
    PATH1 = [(10263, 13994.0), (3794, 12941), (199, 12616), (199, 11128)]
    bot.Move.FollowAutoPath(PATH1, "Wajjun Bazaar to Closer to the Stars")
    bot.Move.XYAndDialog(-247, 10751, 0x816504)
    bot.Move.XY(-153, 11496)
    bot.Wait.ForTime(90000)
    bot.Wait.UntilOutOfCombat()
    bot.Move.XYAndDialog(-247, 10751, 0x816504)
    PATH2 = [(-250, 12360.0), (-5665, 12360), (-7470, 10133), (-7424, 6603), (-9003, 3753), (-8844, -969), (-12948, -4148), (-6635, -6166), (-827, -8374), (2405, -13958), (4181, -16694), (8261, -18470)]
    bot.Move.FollowAutoPath(PATH2, "Closer to the Stars Pt.2")
    bot.Move.XYAndDialog(9001, -19742, 0x816504)
    bot.Move.XYAndDialog(9001, -19742, 0x800008)
    bot.Move.XYAndDialog(9001, -19742, 0x800009)
    bot.Wait.ForMapLoad(216)
    bot.Move.XYAndDialog(-19612, 9541, 0x816507)

def napui_quarter(bot: Botting):
    bot.Map.Travel(216)
    bot.Map.EnterChallenge(3000, target_map_id=216)
    bot.Wait.ForMapLoad(216)
    bot.Move.XY(-15279, 2433)
    bot.Wait.ForTime(30000)
    bot.States.AddManagedCoroutine("Upkeep Multibox Consumables", lambda: _upkeep_multibox_consumables(bot))
    bot.Move.XY(-14221, 3156, forced_timeout=10000)
    bot.Wait.ForTime(2600)
    PATH1 = [(-8566, 4177.0), (-7872, 5528), (-8804, 7997), (-7597, 9889), (-6391, 9834), (-4282, 7208), (-1067, 8828), (2636, 8892), (1612, 6076), (564, 5372), (1524, 4412), (564, 1580), (-1115, -3075), (-4571, -7299), (-6687, -7390), (-6971, -4891), (-7353, -2042), (-12105, -2138), (-12968, -6362), (-17768, -8853)]
    bot.Move.FollowAutoPath(PATH1, "Napui Quarter Mission Path")
    bot.States.RemoveManagedCoroutine("Upkeep Multibox Consumables")
    bot.Wait.ForMapLoad(51)


# ── Bot ───────────────────────────────────────────────────────────────────────

bot = ModularBot(
    name="Factions - We no Su",
    phases=[
        Phase("Marketplace and Wajjun Bazaar",      travel_to_marketplace),
        Phase("Wajjun Bazaar - Finding Master Togo", wajjun_bazaar),
        Phase("Kaineng Docks",                       kaineng_docks),
        Phase("Wajjun Bazaar - Mayhem in the Market", wajjun_bazaar_mayhem),
        Phase("Vizunah Square",                      vizunah_square),
        Phase("Dragon's Throat",                     dragons_throat),
        Phase("Closer to the Stars",                 closer_to_the_stars),
        Phase("Napui Quarter",                       napui_quarter),
    ],
    loop=False,
    template="aggressive",
    upkeep_birthday_cupcake_restock=10,
    upkeep_honeycomb_restock=20,
    upkeep_war_supplies_restock=2,
    upkeep_auto_inventory_management_active=False,
    upkeep_auto_combat_active=False,
    upkeep_auto_loot_active=True,
)


def main():
    bot.update()


if __name__ == "__main__":
    main()
