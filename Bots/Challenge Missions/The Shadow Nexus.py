"""
The Shadow Nexus — ModularBot conversion.

Demonstrates:
- loop_to= targeting a specific phase (not the first)
- on_party_wipe= jumping to a different phase than loop target
- Challenge mission entry pattern (NPC dialog)
- Build-time loop for repeated path registration
"""

import sys, os
import Py4GW

bots_dir = os.path.join(Py4GW.Console.get_projects_path(), "Bots")
if bots_dir not in sys.path:
    sys.path.insert(0, bots_dir)

from Py4GWCoreLib import Botting
from modular_bot import ModularBot, Phase

# ── Data ──────────────────────────────────────────────────────────────────────

OUTPOST_GATE_OF_TORMENT = 450
OUTPOST_SHADOW_NEXUS = 555

LOOP_PATH = [
    (4479, 2496),   (36, 3428),     (-3145, 3648),
    (-4626, 1563),  (-1938, 1014),  (-4132, -3867),
    (530, -3812),   (1321, -987),
]

# ── Phases ────────────────────────────────────────────────────────────────────

def prepare(bot: Botting):
    bot.Properties.Enable("halt_on_death")
    bot.Map.Travel(target_map_id=OUTPOST_SHADOW_NEXUS)

def start_mission(bot: Botting):
    bot.Move.XYAndInteractNPC(-2237, -4961)
    bot.Multibox.SendDialogToTarget(0x88)
    # Same MapID before/after — use timed wait instead of ForMapLoad
    bot.Wait.ForTime(50000)

def combat_loop(bot: Botting):
    # Run the portal loop 10 times (registered as 10 FollowAutoPath states)
    for _ in range(10):
        bot.Move.FollowAutoPath(LOOP_PATH)
    bot.Wait.UntilOutOfCombat()

def restart(bot: Botting):
    bot.Map.Travel(OUTPOST_GATE_OF_TORMENT)
    bot.Map.Travel(OUTPOST_SHADOW_NEXUS)

# ── Bot ───────────────────────────────────────────────────────────────────────

bot = ModularBot(
    name="The Shadow Nexus",
    phases=[
        Phase("Prepare",        prepare),
        Phase("Start Mission",  start_mission),
        Phase("Loop",           combat_loop),
        Phase("Restart",        restart),
    ],
    loop=True,
    loop_to="Start Mission",               # loop back to mission entry, not travel
    template="multibox_aggressive",
    on_party_wipe="Restart",               # wipe → restart (resign & re-enter)
)


def main():
    bot.update()


if __name__ == "__main__":
    main()
