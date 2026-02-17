"""
Sunspear Title Farm — ModularBot conversion.

Demonstrates:
- Simple loop (travel → bounty → kill → resign → repeat)
- template="multibox_aggressive"
- on_party_wipe auto-recovery to a named phase
"""

import sys, os
import Py4GW

bots_dir = os.path.join(Py4GW.Console.get_projects_path(), "Bots")
if bots_dir not in sys.path:
    sys.path.insert(0, bots_dir)

from Py4GWCoreLib import Botting
from modular_bot import ModularBot, Phase

# ── Data ──────────────────────────────────────────────────────────────────────

KILLING_PATH = [
    (-18601.0, -12507.0), (-18103.0, -8169.0), (-16868.0, -7706.0),
    (-18433.0, -14250.0), (-16334.0, -17663.0), (-14982.0, -16881.0),
]

# ── Phases ────────────────────────────────────────────────────────────────────

def travel(bot: Botting):
    bot.Map.Travel(target_map_id=381)
    bot.Party.SetHardMode(True)

def exit_to_arkjok(bot: Botting):
    bot.Move.XYAndExitMap(5580, 946, 380)
    bot.Wait.ForMapLoad(target_map_id=380)

def get_bounty(bot: Botting):
    bot.Move.XYAndInteractNPC(-17223, -12543)
    bot.Wait.ForTime(2000)
    bot.Multibox.SendDialogToTarget(0x85)
    bot.Wait.ForTime(6000)

def combat(bot: Botting):
    bot.Move.FollowAutoPath(KILLING_PATH, "Kill Route")
    bot.Wait.UntilOutOfCombat()

def resign(bot: Botting):
    bot.Multibox.ResignParty()
    bot.Wait.ForMapToChange(target_map_id=381)
    bot.UI.PrintMessageToConsole("Sunspear Title Farm", "Finished routine")

# ── Bot ───────────────────────────────────────────────────────────────────────

bot = ModularBot(
    name="Sunspear Title Farm - Yohlon Haven",
    phases=[
        Phase("Travel to Yohlon Haven",            travel),
        Phase("Exit to Arkjok Ward",               exit_to_arkjok),
        Phase("Get Bounty from Sunspear Agent",    get_bounty),
        Phase("Start Combat",                      combat),
        Phase("Resign Party and Return",           resign),
    ],
    loop=True,
    template="multibox_aggressive",
    on_party_wipe="Start Combat",
)


def main():
    bot.update()


if __name__ == "__main__":
    main()
