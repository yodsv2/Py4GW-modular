"""Widget wrapper for the prebuilt Eye of the North modular campaign."""

from __future__ import annotations

from pathlib import Path

from Sources.modular_recipes.prebuilt._campaign_widget import CampaignWidget
from Sources.modular_recipes.prebuilt.modular_eotn import EOTN_PHASE_SPECS
from Sources.modular_recipes.prebuilt.modular_eotn import EotnCampaignOptions
from Sources.modular_recipes.prebuilt.modular_eotn import build_eotn_campaign_specs
from Sources.modular_recipes.prebuilt.modular_eotn import create_eotn_campaign_bot
from Widgets.Automation.modular.widget_guard import guarded_widget_main

MODULE_NAME = 'Modular EotN Campaign'
MODULE_ICON = 'Textures/Module_Icons/Route Planner.png'
MODULE_TAGS = ['Automation', 'modular_bot', 'eotn', 'campaign']

_WIDGET = CampaignWidget(
    module_name=MODULE_NAME,
    title='Eye of the North Campaign',
    rows=EOTN_PHASE_SPECS,
    build_specs=build_eotn_campaign_specs,
    options_type=EotnCampaignOptions,
    create_bot=create_eotn_campaign_bot,
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
