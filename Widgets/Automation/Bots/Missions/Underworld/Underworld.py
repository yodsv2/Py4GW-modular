"""
Underworld Helper — ModularBot conversion.

Original: Widgets/Automation/Bots/Missions/Underworld/Underworld.py (689 lines)
This:     ~540 lines  (routine setup boilerplate eliminated, phase functions identical)

Demonstrates:
- condition= for 13 optional quest phases (toggled via BotSettings checkboxes)
- use_custom_behaviors=True with CB event handlers
- on_party_wipe auto-recovery
- settings_ui / help_ui for custom ImGui panels
- Phase functions using full Botting API + CustomBehaviors party management
- config_draw_path=True passed through to Botting
"""

import sys, os
import Py4GW
import PyImGui

bots_dir = os.path.join(Py4GW.Console.get_projects_path(), "Bots")
if bots_dir not in sys.path:
    sys.path.insert(0, bots_dir)

from Py4GWCoreLib import (
    Botting, Routines, Agent, AgentArray, Player, GLOBAL_CACHE, ConsoleLog,
)
from Sources.oazix.CustomBehaviors.primitives.botting.botting_helpers import BottingHelpers
from Sources.oazix.CustomBehaviors.primitives.parties.custom_behavior_party import CustomBehaviorParty
from Sources.oazix.CustomBehaviors.primitives.botting.botting_fsm_helper import BottingFsmHelpers
from Sources.oazix.CustomBehaviors.primitives.custom_behavior_loader import CustomBehaviorLoader
from Sources.oazix.CustomBehaviors.primitives.behavior_state import BehaviorState

from modular_bot import ModularBot, Phase


# ══════════════════════════════════════════════════════════════════════════════
# Settings (unchanged from original)
# ══════════════════════════════════════════════════════════════════════════════

class BotSettings:
    RestoreVale: bool = False
    WrathfullSpirits: bool = False
    EscortOfSouls: bool = False
    UnwantedGuests: bool = False
    RestoreWastes: bool = True
    ServantsOfGrenth: bool = True
    PassTheMountains: bool = True
    RestoreMountains: bool = False
    DeamonAssassin: bool = False
    RestorePlanes: bool = True
    TheFourHorsemen: bool = True
    RestorePools: bool = True
    TerrorwebQueen: bool = True
    RestorePit: bool = False
    ImprisonedSpirits: bool = False
    Repeat: bool = True


# ══════════════════════════════════════════════════════════════════════════════
# CB toggle helpers (unchanged from original)
# ══════════════════════════════════════════════════════════════════════════════

def _toggle_wait_if_aggro(enabled: bool) -> None:
    behavior = CustomBehaviorLoader().custom_combat_behavior
    if behavior is None:
        return
    for utility in behavior.get_skills_final_list():
        if utility.custom_skill.skill_name == "wait_if_in_aggro":
            utility.is_enabled = enabled
            break

def _toggle_wait_for_party(enabled: bool) -> None:
    behavior = CustomBehaviorLoader().custom_combat_behavior
    if behavior is None:
        return
    for utility in behavior.get_skills_final_list():
        if utility.custom_skill.skill_name == "wait_if_party_member_too_far":
            utility.is_enabled = enabled
            break

def _toggle_move_if_aggro(enabled: bool) -> None:
    behavior = CustomBehaviorLoader().custom_combat_behavior
    if behavior is None:
        return
    for utility in behavior.get_skills_final_list():
        if utility.custom_skill.skill_name == "move_to_party_member_if_in_aggro":
            utility.is_enabled = enabled
            break

def _toggle_lock(enabled: bool) -> None:
    behavior = CustomBehaviorLoader().custom_combat_behavior
    if behavior is None:
        return
    for utility in behavior.get_skills_final_list():
        if utility.custom_skill.skill_name == "wait_if_lock_taken":
            utility.is_enabled = enabled
            break


# ══════════════════════════════════════════════════════════════════════════════
# Utility helpers (unchanged from original)
# ══════════════════════════════════════════════════════════════════════════════

def _ensure_minimum_gold(bot: Botting, minimum_gold: int = 1000, withdraw_amount: int = 10000) -> None:
    def _check_and_restock():
        gold_on_char = GLOBAL_CACHE.Inventory.GetGoldOnCharacter()
        if gold_on_char >= minimum_gold:
            return
        gold_in_storage = GLOBAL_CACHE.Inventory.GetGoldInStorage()
        amount = min(withdraw_amount, gold_in_storage)
        if amount <= 0:
            return
        ConsoleLog("UW", f"[GOLD] Withdrawing {amount}g from storage.")
        GLOBAL_CACHE.Inventory.WithdrawGold(amount)
    bot.States.AddCustomState(_check_and_restock, "Ensure Minimum Gold")
    bot.Wait.ForTime(1000)

def _auto_assign_flag_emails() -> None:
    CustomBehaviorParty().party_flagging_manager.auto_assign_emails_if_none_assigned()

def _set_flag_position(index: int, flag_x: int, flag_y: int) -> None:
    CustomBehaviorParty().party_flagging_manager.set_flag_position(index, flag_x, flag_y)

def FocusKeeperOfSouls(bot: Botting):
    def _focus_logic():
        enemies = [e for e in AgentArray.GetEnemyArray() if Agent.IsAlive(e) and Agent.GetModelID(e) == 2373]
        if not enemies:
            return
        player_pos = Player.GetXY()
        closest = min(enemies, key=lambda e: ((player_pos[0] - Agent.GetXYZ(e)[0])**2 + (player_pos[1] - Agent.GetXYZ(e)[1])**2)**0.5)
        CustomBehaviorParty().set_party_custom_target(closest)
    bot.States.AddCustomState(_focus_logic, "Focus Keeper of Souls")

def enable_default_party_behavior(bot: Botting):
    bot.States.AddCustomState(lambda: _toggle_move_if_aggro(True), "Enable MoveIfPartyMemberInAggro")
    bot.States.AddCustomState(lambda: _toggle_wait_for_party(True), "Enable WaitIfPartyMemberTooFar")
    bot.States.AddCustomState(lambda: _toggle_wait_if_aggro(True), "Enable WaitIfInAggro")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_following_enabled(True), "Enable Follow")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_looting_enabled(True), "Enable Looting")

def Wait_for_Spawns(bot: Botting, x, y):
    bot.Move.XY(x, y, "To the Vale")
    def runtime_check_logic():
        enemies = [e for e in AgentArray.GetEnemyArray() if Agent.IsAlive(e) and Agent.GetModelID(e) == 2380]
        if not enemies:
            return True
        bot.Move.XY(x, y, "Go Back")
        return False
    bot.Wait.UntilCondition(runtime_check_logic)
    bot.Wait.ForTime(1000)
    bot.Move.XY(x, y, "1")
    bot.Wait.UntilCondition(runtime_check_logic)
    bot.Wait.ForTime(1000)
    bot.Move.XY(x, y, "2")
    bot.Wait.UntilCondition(runtime_check_logic)
    bot.Wait.ForTime(1000)
    bot.Move.XY(x, y, "3")
    bot.Wait.UntilCondition(runtime_check_logic)


# ══════════════════════════════════════════════════════════════════════════════
# Phase functions — IDENTICAL bodies to the original, just removed the
# outer `if BotSettings.X` guard (handled by Phase condition= instead).
# ══════════════════════════════════════════════════════════════════════════════

def setup_and_travel(bot: Botting):
    """Initial setup: travel to Temple of Ages and enter UW."""
    CustomBehaviorParty().set_party_is_blessing_enabled(True)
    BottingFsmHelpers.SetBottingBehaviorAsAggressive(bot)
    bot.Map.Travel(target_map_id=138)
    bot.Party.SetHardMode(False)

def enter_uw(bot: Botting):
    _ensure_minimum_gold(bot)
    CustomBehaviorParty().set_party_leader_email(Player.GetAccountEmail())
    bot.Move.XY(-4199, 19845, "go to Statue")
    bot.States.AddCustomState(lambda: Player.SendChatCommand("kneel"), "kneel")
    bot.Wait.ForTime(3000)
    bot.Dialogs.AtXY(-4199, 19845, 0x86, "accept to enter")
    bot.Wait.ForMapLoad(target_map_id=72)
    bot.Properties.ApplyNow("pause_on_danger", "active", True)

def clear_the_chamber(bot: Botting):
    CustomBehaviorParty().set_party_leader_email(Player.GetAccountEmail())
    bot.States.AddCustomState(lambda: _toggle_lock(False), "Disable Lock Wait")
    enable_default_party_behavior(bot)
    bot.Move.XYAndInteractNPC(295, 7221, "go to NPC")
    bot.Dialogs.AtXY(295, 7221, 0x806501, "take quest")
    bot.Move.XY(769, 6564, "Prepare to clear the chamber")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(BehaviorState.CLOSE_TO_AGGRO), "Force Close_to_Aggro")
    bot.Wait.ForTime(30000)
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(None), "Release Close_to_Aggro")
    bot.Move.XY(-1505, 6352, "Left")
    bot.Move.XY(-755, 8982, "Mid")
    bot.Move.XY(1259, 10214, "Right")
    bot.Move.XY(-3729, 13414, "Right")
    bot.Move.XY(-5855, 11202, "Clear the Room")
    bot.Wait.ForTime(3000)
    bot.Move.XYAndInteractNPC(-5806, 12831, "go to NPC")
    bot.Wait.ForTime(3000)
    bot.Dialogs.AtXY(-5806, 12831, 0x806D01, "take quest")
    bot.Wait.ForTime(3000)

def restore_vale(bot: Botting):
    BottingFsmHelpers.SetBottingBehaviorAsAggressive(bot)
    if BotSettings.EscortOfSouls:
        bot.Dialogs.AtXY(-5806, 12831, 0x806C03, "take quest")
        bot.Dialogs.AtXY(-5806, 12831, 0x806C01, "take quest")
    bot.Move.XY(-8660, 5655, "To the Vale 1")
    bot.Move.XY(-9431, 1659, "To the Vale 2")
    bot.Move.XY(-11123, 2531, "To the Vale 3")
    bot.Move.XY(-10212, 251, "To the Vale 4")
    bot.Move.XY(-13085, 849, "To the Vale 5")
    bot.Move.XY(-15274, 1432, "To the Vale 6")
    bot.Move.XY(-13246, 5110, "To the Vale 7")
    bot.Move.XYAndInteractNPC(-13275, 5261, "go to NPC")
    if not BotSettings.WrathfullSpirits:
        bot.Dialogs.AtXY(5755, 12769, 0x8D, "Back to Chamber")
    bot.Wait.ForTime(3000)

def wrathful_spirits(bot: Botting):
    bot.Move.XYAndInteractNPC(-13275, 5261, "go to NPC")
    bot.Dialogs.AtXY(5755, 12769, 0x806E03, "Back to Chamber")
    bot.Dialogs.AtXY(5755, 12769, 0x806E01, "Back to Chamber")
    bot.Templates.Pacifist()
    bot.States.AddCustomState(lambda: _toggle_wait_for_party(False), "Disable WaitIfPartyMemberTooFar")
    bot.States.AddCustomState(lambda: _toggle_wait_if_aggro(False), "Disable WaitIfInAggro")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_combat_enabled(False), "Disable Combat")
    bot.Move.XY(-13422, 973, "Wrathfull Spirits 1")
    bot.Templates.Aggressive()
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_combat_enabled(True), "Enable Combat")
    bot.States.AddCustomState(lambda: _toggle_wait_for_party(True), "Enable WaitIfPartyMemberTooFar")
    bot.States.AddCustomState(lambda: _toggle_wait_if_aggro(True), "Enable WaitIfInAggro")
    bot.Move.XY(-10207, 1746, "Wrathfull Spirits 2")
    bot.Move.XY(-13287, 1996, "Wrathfull Spirits 3")
    bot.Move.XY(-15226, 4129, "Wrathfull Spirits 4")
    bot.Move.XYAndInteractNPC(-13275, 5261, "go to NPC")
    bot.Dialogs.AtXY(5755, 12769, 0x8D, "Back to Chamber")
    bot.Wait.ForTime(3000)

def escort_of_souls(bot: Botting):
    bot.Wait.ForTime(5000)
    bot.Move.XY(-4764, 11845, "Escort of Souls 1")
    bot.Move.XYAndInteractNPC(-5806, 12831, "go to NPC")
    bot.Wait.ForTime(3000)
    bot.Dialogs.AtXY(-5806, 12831, 0x806C03, "take quest")
    bot.Dialogs.AtXY(-5806, 12831, 0x806C01, "take quest")
    bot.Move.XY(-6833, 7077, "Escort of Souls 2")
    bot.Move.XY(-9606, 2110, "Escort of Souls 3")
    bot.Move.XYAndInteractNPC(-13275, 5261, "go to NPC")
    bot.Dialogs.AtXY(5755, 12769, 0x8D, "Back to Chamber")
    bot.Wait.ForTime(3000)

def unwanted_guests(bot: Botting):
    bot.Wait.ForTime(5000)
    bot.Move.XY(-1533, 10502)
    bot.Move.XY(-1039, -572)
    bot.Move.XY(-41, 2686)
    bot.Move.XY(5797, 10405)
    bot.Move.XY(3225, 12916)
    bot.Move.XY(-2965, 10260)
    bot.Wait.ForTime(5000)
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_following_enabled(False), "Disable Following")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(BehaviorState.CLOSE_TO_AGGRO), "Force Close_to_Aggro")
    bot.Move.XYAndInteractNPC(-5806, 12831, "go to NPC")
    bot.Dialogs.AtXY(-5806, 12831, 0x806701, "take quest")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(None), "Release Close_to_Aggro")
    FocusKeeperOfSouls(bot)
    bot.Wait.ForTime(500)
    FocusKeeperOfSouls(bot)
    bot.Wait.ForTime(500)
    FocusKeeperOfSouls(bot)
    bot.Wait.ForTime(20000)
    bot.Move.XYAndInteractNPC(-5806, 12831, "go to NPC")
    bot.Dialogs.AtXY(-5806, 12831, 0x91, "take quest")
    bot.Move.XY(-12953, 750)
    bot.Move.XY(-8371, 4865)
    FocusKeeperOfSouls(bot)
    bot.Wait.ForTime(500)
    FocusKeeperOfSouls(bot)
    bot.Move.XY(-6907, 7256)

def restore_wastes(bot: Botting):
    bot.Templates.Aggressive()
    bot.Properties.ApplyNow("pause_on_danger", "active", True)
    bot.Move.XY(3891, 7572, "Restore Wastes 1")
    bot.Move.XY(4106, 16031, "Restore Wastes 2")
    bot.Move.XY(2486, 21723, "Restore Wastes 3")
    bot.Move.XY(-1452, 21202, "Restore Wastes 4")
    bot.Move.XY(542, 18310, "Restore Wastes 5")
    if not BotSettings.ServantsOfGrenth:
        bot.Move.XYAndInteractNPC(554, 18384, "go to NPC")
        bot.Dialogs.AtXY(5755, 12769, 0x8D, "Back to Chamber")
    bot.Wait.ForTime(3000)

def servants_of_grenth(bot: Botting):
    bot.Templates.Aggressive()
    bot.Move.XY(2700, 19952, "Servants of Grenth 1")
    bot.Party.FlagAllHeroes(2559, 20301)
    FLAG_POINTS = [(2559,20301),(3032,20148),(2813,20590),(2516,19665),(3231,19472),(3691,19979),(2039,20175)]
    bot.States.AddCustomState(lambda: _auto_assign_flag_emails(), "Set Flag")
    for idx, (fx, fy) in enumerate(FLAG_POINTS, start=1):
        bot.States.AddCustomState(lambda i=idx, x=fx, y=fy: _set_flag_position(i, x, y), f"Set Flag {idx}")
    bot.States.AddCustomState(lambda: _toggle_wait_for_party(False), "Disable WaitIfPartyMemberTooFar")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(BehaviorState.CLOSE_TO_AGGRO), "Force Close_to_Aggro")
    bot.Move.XYAndInteractNPC(554, 18384, "go to NPC")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_following_enabled(False), "Disable Following")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().party_flagging_manager.clear_all_flags(), "Clear Flags")
    bot.Dialogs.AtXY(5755, 12769, 0x806601, "Back to Chamber")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(None), "Release Close_to_Aggro")
    bot.Move.XY(2700, 19952, "Servants of Grenth 2")
    bot.States.AddCustomState(lambda: _toggle_wait_for_party(True), "Enable WaitIfPartyMemberTooFar")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_following_enabled(True), "Enable Following")
    bot.Party.UnflagAllHeroes()
    bot.Wait.ForTime(10000)
    bot.Move.XYAndInteractNPC(554, 18384, "go to NPC")
    bot.Dialogs.AtXY(5755, 12769, 0x8D, "Back to Chamber")
    bot.Wait.ForTime(3000)

def pass_the_mountains(bot: Botting):
    bot.Move.XY(-220, 1691, "Pass the Mountains 1")
    bot.Move.XY(7035, 1973, "Pass the Mountains 2")
    bot.Move.XY(8089, -3303, "Pass the Mountains 3")
    bot.Move.XY(8121, -6054, "Pass the Mountains 4")

def restore_mountains(bot: Botting):
    bot.Move.XY(7013, -7582, "Restore the Mountains 1")
    bot.Move.XY(1420, -9126, "Restore the Mountains 2")
    bot.Move.XY(-8373, -5016, "Restore the Mountains 3")

def daemon_assassin(bot: Botting):
    bot.Move.XYAndInteractNPC(-8250, -5171, "go to NPC")
    bot.Wait.ForTime(3000)
    bot.Dialogs.AtXY(-8250, -5171, 0x806801, "take quest")
    bot.Move.XY(-1384, -3929, "Deamon Assassin 1")
    bot.Wait.ForTime(30000)

def restore_planes(bot: Botting):
    Wait_for_Spawns(bot, 10371, -10510)
    Wait_for_Spawns(bot, 12795, -8811)
    Wait_for_Spawns(bot, 11180, -13780)
    Wait_for_Spawns(bot, 13740, -15087)
    bot.Move.XY(11546, -13787, "Restore Planes 1")
    bot.Move.XY(8530, -11585, "Restore Planes 2")
    Wait_for_Spawns(bot, 8533, -13394)
    Wait_for_Spawns(bot, 8579, -20627)
    Wait_for_Spawns(bot, 11218, -17404)

def the_four_horsemen(bot: Botting):
    bot.Move.XY(13473, -12091, "The Four Horseman 1")
    bot.Wait.ForTime(10000)
    bot.Party.FlagAllHeroes(13473, -12091)
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_following_enabled(False), "Disable Following")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_looting_enabled(False), "Disable Looting")
    bot.States.AddCustomState(lambda: _toggle_wait_for_party(False), "Disable WaitIfPartyMemberTooFar")
    bot.States.AddCustomState(lambda: _toggle_move_if_aggro(False), "Disable MoveIfPartyMemberInAggro")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(BehaviorState.CLOSE_TO_AGGRO), "Force Close_to_Aggro")
    bot.Move.XYAndInteractNPC(11371, -17990, "go to NPC")
    bot.Dialogs.AtXY(-8250, -5171, 0x806A01, "take quest")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_forced_state(None), "Release Close_to_Aggro")
    bot.Wait.ForTime(35000)
    bot.Move.XYAndInteractNPC(11371, -17990, "TP to Chamber")
    bot.Dialogs.AtXY(11371, -17990, 0x8D, "take quest")
    bot.Wait.ForTime(1000)
    bot.Move.XYAndInteractNPC(-5782, 12819, "TP back to Chaos")
    bot.Dialogs.AtXY(11371, -17990, 0x8B, "take quest")
    bot.Wait.ForTime(1000)
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_following_enabled(True), "Enable Following")
    bot.Party.UnflagAllHeroes()
    bot.Wait.ForTime(5000)
    bot.Move.XY(11371, -17990, "The Four Horseman 2")
    bot.Wait.ForTime(30000)
    bot.Move.XY(11371, -17990, "The Four Horseman 3")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_following_enabled(True), "Enable Follow")
    bot.States.AddCustomState(lambda: _toggle_wait_for_party(True), "Enable WaitIfPartyMemberTooFar")
    bot.States.AddCustomState(lambda: _toggle_move_if_aggro(True), "Enable MoveIfPartyMemberInAggro")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().set_party_is_looting_enabled(True), "Enable Looting")

def restore_pools(bot: Botting):
    Wait_for_Spawns(bot, 4647, -16833)
    Wait_for_Spawns(bot, 2098, -15543)
    bot.Move.XY(-12703, -10990, "Restore Pools 1")
    bot.Move.XY(-11849, -11986, "Restore Pools 2")
    bot.Move.XY(-7217, -19394, "Restore Pools 3")
    if not BotSettings.TerrorwebQueen:
        bot.Move.XYAndInteractNPC(-6957, -19478, "go to NPC")
        bot.Dialogs.AtXY(-6957, -19478, 0x8B, "Back to Chamber")
    bot.Wait.ForTime(3000)

def terrorweb_queen(bot: Botting):
    bot.Move.XYAndInteractNPC(-6961, -19499, "go to NPC")
    bot.Dialogs.AtXY(-6961, -19499, 0x806B01, "take quest")
    bot.Move.XY(-12303, -15213, "Terrorweb Queen 1")
    bot.Move.XYAndInteractNPC(-6957, -19478, "go to NPC")
    bot.Dialogs.AtXY(-6957, -19478, 0x8B, "Back to Chamber")

def restore_pit(bot: Botting):
    bot.Move.XY(13145, -8740, "Restore Pit 1")
    bot.Move.XY(12188, 4249, "Restore Pit 2")
    bot.Move.XY(14959, 4851, "Restore Pit 3")
    bot.Move.XY(15460, 3125, "Restore Pit 4")
    bot.Move.XY(8970, 6813, "Restore Pit 5")
    if not BotSettings.ImprisonedSpirits:
        bot.Move.XYAndInteractNPC(8698, 6324, "go to NPC")
        bot.Dialogs.AtXY(8698, 6324, 0x8D, "Back to Chamber")
    bot.Wait.ForTime(3000)

def imprisoned_spirits(bot: Botting):
    bot.Move.XY(12329, 4632, "Imprisoned Spirits 1")
    bot.States.AddCustomState(lambda: CustomBehaviorParty().party_flagging_manager.assign_formation_for_current_party("preset_1"), "Set Flag")
    bot.Party.FlagAllHeroes(12329, 4632)
    bot.Move.XYAndInteractNPC(8666, 6308, "go to NPC")
    bot.Dialogs.AtXY(8666, 6308, 0x806901, "Back to Chamber")
    bot.Move.XY(12329, 4632, "Imprisoned Spirits 2")

def resign_and_repeat(bot: Botting):
    bot.Multibox.ResignParty()


# ══════════════════════════════════════════════════════════════════════════════
# GUI panels (unchanged from original)
# ══════════════════════════════════════════════════════════════════════════════

def _draw_help():
    PyImGui.text("Hey, this is my first bot in Python, be gentle :)")
    PyImGui.separator()
    PyImGui.text_wrapped("This Bot automates the Underworld")
    PyImGui.text("It is optimized for 8x Custom Behaviors")
    PyImGui.separator()
    PyImGui.text("What is working Well:")
    PyImGui.bullet_text("Restoring Grenth's Monuments (exept Pits)")
    PyImGui.bullet_text("Wrathfull Spirits, Escort of Souls, Servants of Grenth, Deamon Assassin, The Four Horsemen, Terrorweb Queen")
    PyImGui.text("What is working Bad:")
    PyImGui.bullet_text("Imprisoned Spirits, Restore Pits")
    PyImGui.separator()
    PyImGui.bullet_text("Have fun :) - sch0l0ka")

def _draw_settings():
    BotSettings.RestoreVale = PyImGui.checkbox("Restore Vale", BotSettings.RestoreVale)
    DisableVale = not BotSettings.RestoreVale
    if DisableVale: BotSettings.WrathfullSpirits = False
    if DisableVale: BotSettings.EscortOfSouls = False
    PyImGui.begin_disabled(DisableVale)
    BotSettings.WrathfullSpirits = PyImGui.checkbox("Wrathfull Spirits", BotSettings.WrathfullSpirits)
    BotSettings.EscortOfSouls = PyImGui.checkbox("Escort of Souls", BotSettings.EscortOfSouls)
    PyImGui.end_disabled()
    PyImGui.begin_disabled(True)
    BotSettings.UnwantedGuests = PyImGui.checkbox("Unwanted Guests", BotSettings.UnwantedGuests)
    PyImGui.end_disabled()
    BotSettings.RestoreWastes = PyImGui.checkbox("Restore Wastes", BotSettings.RestoreWastes)
    if not BotSettings.RestoreWastes: BotSettings.ServantsOfGrenth = False
    PyImGui.begin_disabled(not BotSettings.RestoreWastes)
    BotSettings.ServantsOfGrenth = PyImGui.checkbox("Servants of Grenth", BotSettings.ServantsOfGrenth)
    PyImGui.end_disabled()
    BotSettings.PassTheMountains = BotSettings.RestoreMountains or BotSettings.RestorePlanes or BotSettings.RestorePools
    PyImGui.begin_disabled(True)
    PyImGui.checkbox("Pass the Mountains", BotSettings.PassTheMountains)
    PyImGui.end_disabled()
    BotSettings.RestoreMountains = PyImGui.checkbox("Restore Mountains", BotSettings.RestoreMountains)
    if not BotSettings.RestoreMountains: BotSettings.DeamonAssassin = False
    PyImGui.begin_disabled(not BotSettings.RestoreMountains)
    BotSettings.DeamonAssassin = PyImGui.checkbox("Deamon Assassin", BotSettings.DeamonAssassin)
    PyImGui.end_disabled()
    BotSettings.RestorePlanes = PyImGui.checkbox("Restore Planes", BotSettings.RestorePlanes)
    if not BotSettings.RestorePlanes:
        BotSettings.TheFourHorsemen = False
        BotSettings.RestorePools = False
        BotSettings.TerrorwebQueen = False
    PyImGui.begin_disabled(not BotSettings.RestorePlanes)
    BotSettings.TheFourHorsemen = PyImGui.checkbox("The Four Horsemen", BotSettings.TheFourHorsemen)
    BotSettings.RestorePools = PyImGui.checkbox("Restore Pools", BotSettings.RestorePools)
    PyImGui.end_disabled()
    if not BotSettings.RestorePools: BotSettings.TerrorwebQueen = False
    PyImGui.begin_disabled(not BotSettings.RestorePools)
    BotSettings.TerrorwebQueen = PyImGui.checkbox("Terrorweb Queen", BotSettings.TerrorwebQueen)
    PyImGui.end_disabled()
    PyImGui.begin_disabled(True)
    PyImGui.checkbox("Restore Pit - Disabled", BotSettings.RestorePit)
    PyImGui.checkbox("Imprisoned Spirits - Disabled", BotSettings.ImprisonedSpirits)
    PyImGui.end_disabled()
    PyImGui.separator()
    BotSettings.Repeat = PyImGui.checkbox("Resign and Repeat after", BotSettings.Repeat)


# ══════════════════════════════════════════════════════════════════════════════
# Bot — all the boilerplate is now declarative constructor args
# ══════════════════════════════════════════════════════════════════════════════

bot = ModularBot(
    name="Underworld Helper",
    phases=[
        # Always-run phases (unconditional, registered at build time)
        Phase("Setup and Travel",      setup_and_travel),
        Phase("Enter Underworld",      enter_uw),
        Phase("Clear the Chamber",     clear_the_chamber),
        # Conditional quest phases (checked at runtime via condition=)
        Phase("Restore Vale",          restore_vale,           condition=lambda: BotSettings.RestoreVale),
        Phase("Wrathfull Spirits",     wrathful_spirits,       condition=lambda: BotSettings.WrathfullSpirits),
        Phase("Escort of Souls",       escort_of_souls,        condition=lambda: BotSettings.EscortOfSouls),
        Phase("Unwanted Guests",       unwanted_guests,        condition=lambda: BotSettings.UnwantedGuests),
        Phase("Restore Wastes",        restore_wastes,         condition=lambda: BotSettings.RestoreWastes),
        Phase("Servants of Grenth",    servants_of_grenth,     condition=lambda: BotSettings.ServantsOfGrenth),
        Phase("Pass the Mountains",    pass_the_mountains,     condition=lambda: BotSettings.PassTheMountains),
        Phase("Restore Mountains",     restore_mountains,      condition=lambda: BotSettings.RestoreMountains),
        Phase("Deamon Assassin",       daemon_assassin,        condition=lambda: BotSettings.DeamonAssassin),
        Phase("Restore Planes",        restore_planes,         condition=lambda: BotSettings.RestorePlanes),
        Phase("The Four Horsemen",     the_four_horsemen,      condition=lambda: BotSettings.TheFourHorsemen),
        Phase("Restore Pools",         restore_pools,          condition=lambda: BotSettings.RestorePools),
        Phase("Terrorweb Queen",       terrorweb_queen,        condition=lambda: BotSettings.TerrorwebQueen),
        Phase("Restore Pit",           restore_pit,            condition=lambda: BotSettings.RestorePit),
        Phase("Imprisoned Spirits",    imprisoned_spirits,     condition=lambda: BotSettings.ImprisonedSpirits),
        Phase("Resign and Repeat",     resign_and_repeat,      condition=lambda: BotSettings.Repeat),
    ],
    loop=True,
    loop_to="Setup and Travel",
    template="aggressive",
    use_custom_behaviors=True,
    cb_on_death=BottingHelpers.botting_unrecoverable_issue,
    cb_on_stuck=BottingHelpers.botting_unrecoverable_issue,
    cb_on_party_death=BottingHelpers.botting_unrecoverable_issue,
    on_party_wipe="Setup and Travel",
    settings_ui=_draw_settings,
    help_ui=_draw_help,
    config_draw_path=True,
)


def main():
    bot.update()


if __name__ == "__main__":
    main()

