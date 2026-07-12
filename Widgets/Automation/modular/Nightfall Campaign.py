"""Widget wrapper for the prebuilt Nightfall modular campaign."""

from __future__ import annotations

from pathlib import Path

from Sources.modular_recipes.prebuilt._campaign_widget import CampaignWidget
from Sources.modular_recipes.prebuilt.modular_nightfall import NIGHTFALL_PHASE_SPECS
from Sources.modular_recipes.prebuilt.modular_nightfall import NightfallCampaignOptions
from Sources.modular_recipes.prebuilt.modular_nightfall import build_nightfall_campaign_specs
from Sources.modular_recipes.prebuilt.modular_nightfall import create_nightfall_campaign_bot
from Widgets.Automation.modular.widget_guard import guarded_widget_main

MODULE_NAME = 'Modular Nightfall Campaign'
MODULE_ICON = 'Textures/Module_Icons/Route Planner.png'
MODULE_TAGS = ['Automation', 'modular_bot', 'nightfall', 'campaign']

_WIDGET = CampaignWidget(
    module_name=MODULE_NAME,
    title='Nightfall Campaign',
    rows=NIGHTFALL_PHASE_SPECS,
    build_specs=build_nightfall_campaign_specs,
    options_type=NightfallCampaignOptions,
    create_bot=create_nightfall_campaign_bot,
    state_path=Path(__file__).with_suffix('.run_state.json'),
)


def _main_impl() -> None:
    _WIDGET.draw()


def main() -> None:
    guarded_widget_main(MODULE_NAME, _main_impl)


def tooltip() -> None:
    _WIDGET.tooltip()


if __name__ == '__main__':
    main()
