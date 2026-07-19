"""Offline emitter smoke check for the native Modular Recorder widget."""

from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
    from Sources.modular_recipes.tools import _stubs
else:
    from . import _stubs


def _install_widget_stubs() -> None:
    _stubs.install()
    py4gwcorelib = sys.modules["Py4GWCoreLib"]
    py4gwcorelib.Console = types.SimpleNamespace(MessageType=types.SimpleNamespace(Error="error"))
    py4gwcorelib.ConsoleLog = lambda *_args, **_kwargs: None
    py4gwcorelib.Agent = types.SimpleNamespace(
        IsValid=lambda _agent_id: True,
        IsItem=lambda _agent_id: False,
        IsGadget=lambda _agent_id: False,
        GetXY=lambda _agent_id: (100.0, 200.0),
        GetNameByID=lambda _agent_id: "Test Target",
        GetItemAgentItemID=lambda _agent_id: 0,
    )
    py4gwcorelib.AgentArray = types.SimpleNamespace(GetEnemyArray=lambda: [])
    py4gwcorelib.Item = types.SimpleNamespace(GetModelID=lambda _item_id: 0)
    py4gwcorelib.Map = types.SimpleNamespace(
        GetMapID=lambda: 1,
        GetMapName=lambda _map_id: "Test Map",
        IsMapReady=lambda: True,
    )
    py4gwcorelib.Party = types.SimpleNamespace(GetPartySize=lambda: 8)
    py4gwcorelib.Player = types.SimpleNamespace(GetTargetID=lambda: 1, GetXY=lambda: (100.0, 200.0))

    pyimgui = types.ModuleType("PyImGui")
    pyimgui.WindowFlags = types.SimpleNamespace(HorizontalScrollbar=1)
    pyimgui.TableFlags = types.SimpleNamespace(SizingStretchProp=1)
    pyimgui.ImGuiCond = types.SimpleNamespace(FirstUseEver=1)
    pyimgui.clipboard_text = ""
    pyimgui.set_clipboard_text = lambda text: setattr(pyimgui, "clipboard_text", text)
    sys.modules["PyImGui"] = pyimgui

    pyagent = types.ModuleType("PyAgent")
    pyagent.PyAgent = types.SimpleNamespace(GetAgentEncName=lambda _agent_id: [1, 2, 3, 4])
    sys.modules["PyAgent"] = pyagent

    pydialog = types.ModuleType("PyDialog")
    pydialog.PyDialog = types.SimpleNamespace(initialize=lambda: None)
    sys.modules["PyDialog"] = pydialog


def main() -> int:
    _install_widget_stubs()
    widget_path = Path(__file__).resolve().parents[3] / "Widgets" / "Automation" / "modular" / "Modular Recorder.py"
    spec = importlib.util.spec_from_file_location("modular_recorder_widget", widget_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    capture = module._target_capture("npc", 1)
    assert capture is not None
    module._remember_capture(capture)
    module._record_interact("npc")
    module._record_dialog(0x82C504)
    module._record_wait_until_explorable()
    module._add_line("BT.Wait(duration_ms=100)")
    output = module._full_output()
    assert "def new_recording() -> BehaviorTree:" in output
    assert "BT.Interact(kind='npc', key='TEST_TARGET', pos=(100, 200))" in output
    assert "BT.Dialog(kind='npc', key='TEST_TARGET', dialog_ids=['0x82c504'], pos=(100, 200))" in output
    assert "BT.WaitUntilOnExplorable(timeout_ms=30000)" in output
    assert "BT.Wait(duration_ms=100)" in output
    assert (
        "ADD or EXTEND the following NPCs in enum `NPC_TARGETS` at "
        "`Py4GWCoreLib/modular/domain/target_registry.py`:"
    ) in output
    assert '"TEST_TARGET": (((1, 2, 3, 4),), ' in output
    assert module._registry_block_for_capture(capture).startswith("ADD or EXTEND the following NPCs")
    module._copy_current_xy()
    assert sys.modules["PyImGui"].clipboard_text == "(100, 200)"
    print("modular_recorder_emitters: ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
