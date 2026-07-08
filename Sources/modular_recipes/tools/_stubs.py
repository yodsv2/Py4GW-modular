"""Test stubs for importing modular recipes outside the injected runtime."""

from __future__ import annotations

import sys
import types
from enum import Enum
from enum import IntEnum
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[3]


class _NodeState(Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    RUNNING = "running"


class _PlayerStatus(IntEnum):
    Offline = 0
    Online = 1
    Away = 2
    DoNotDisturb = 3


class _Node:
    def __init__(self, name: str = "Node", **kwargs: Any) -> None:
        self.name = name
        self.kwargs = dict(kwargs)
        self.blackboard: dict = {}

    def reset(self) -> None:
        return

    def tick(self):
        return _NodeState.SUCCESS

    def get_children(self):
        return []


class _ActionNode(_Node):
    def __init__(self, name: str = "Action", action_fn=None, args=None, **kwargs: Any) -> None:
        super().__init__(name=name, **kwargs)
        self.action_fn = action_fn
        self.args = list(args or [])


class _SequenceNode(_Node):
    def __init__(self, children=None, name: str = "Sequence", **kwargs: Any) -> None:
        super().__init__(name=name, **kwargs)
        self.children = [BehaviorTree.Node._coerce_node(child) for child in (children or [])]

    def get_children(self):
        return list(self.children)


class _SubtreeNode(_Node):
    def __init__(self, name: str = "Subtree", subtree_fn=None, **kwargs: Any) -> None:
        super().__init__(name=name, **kwargs)
        self.subtree_fn = subtree_fn


class _WaitUntilNode(_ActionNode):
    pass


class _RepeaterNode(_Node):
    def __init__(self, child=None, children=None, repeat_count: int = 1, name: str = "Repeater", **kwargs: Any) -> None:
        super().__init__(name=name, repeat_count=repeat_count, **kwargs)
        source = [child] if child is not None else list(children or [])
        self.children = [BehaviorTree.Node._coerce_node(value) for value in source]

    def get_children(self):
        return list(self.children)


class BehaviorTree:
    NodeState = _NodeState
    Node = _Node
    ActionNode = _ActionNode
    SequenceNode = _SequenceNode
    SelectorNode = _SequenceNode
    SubtreeNode = _SubtreeNode
    WaitUntilNode = _WaitUntilNode
    SucceederNode = _Node
    FailerNode = _Node
    RepeaterNode = _RepeaterNode

    def __init__(self, root: _Node) -> None:
        self.root = self.Node._coerce_node(root)
        self.blackboard: dict = {}

    @staticmethod
    def as_tree(value):
        if isinstance(value, BehaviorTree):
            return value
        if isinstance(value, _Node):
            return BehaviorTree(value)
        raise TypeError(type(value).__name__)

    @staticmethod
    def resolve_tree(value_or_builder):
        value = value_or_builder() if callable(value_or_builder) else value_or_builder
        return BehaviorTree.as_tree(value)

    @staticmethod
    def build_sequence(children, name="Sequence", step_name_fn=None):
        nodes = [
            _SubtreeNode(
                name=step_name_fn(index, child) if step_name_fn else f"Step{index + 1}",
                subtree_fn=lambda _node, child=child: BehaviorTree.resolve_tree(child),
            )
            for index, child in enumerate(children)
        ]
        return BehaviorTree(_SequenceNode(children=nodes, name=name))

    @staticmethod
    def build_named_sequence(steps, start_from=None, name="NamedSequence", before_step=None, repeat=False):
        step_list = list(steps)
        if start_from is not None:
            names = [step_name for step_name, _builder in step_list]
            step_list = step_list[names.index(start_from) :]
        nodes = [
            _SubtreeNode(
                name=step_name,
                subtree_fn=lambda _node, builder=builder: BehaviorTree.resolve_tree(builder),
            )
            for step_name, builder in step_list
        ]
        return BehaviorTree(_SequenceNode(children=nodes, name=name))

    def reset(self) -> None:
        self.root.reset()

    def tick(self):
        return self.root.tick()


def _coerce_node(value) -> _Node:
    if isinstance(value, _Node):
        return value
    if isinstance(value, BehaviorTree):
        return value.root
    raise TypeError(type(value).__name__)


BehaviorTree.Node._coerce_node = staticmethod(_coerce_node)


class _BTNamespace:
    def __getattr__(self, name: str):
        def _factory(*args: Any, **kwargs: Any) -> BehaviorTree:
            return BehaviorTree(_ActionNode(name=name, args=args, **kwargs))

        return _factory


class _CompositeNamespace:
    @staticmethod
    def Sequence(*trees: BehaviorTree, name: str = "Sequence") -> BehaviorTree:
        return BehaviorTree(_SequenceNode(children=[BehaviorTree.Node._coerce_node(tree) for tree in trees], name=name))


class _Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = float(x)
        self.y = float(y)


class _PointPath:
    @staticmethod
    def as_path(value):
        return value

    @staticmethod
    def final_point(value):
        if isinstance(value, (list, tuple)) and value and isinstance(value[0], (list, tuple)):
            value = value[-1]
        if isinstance(value, (list, tuple)) and len(value) >= 2:
            return _Point(float(value[0]), float(value[1]))
        return _Point(0.0, 0.0)


class _CommandNamespace:
    def __getattr__(self, name: str) -> str:
        return name


class _BottingTree:
    def __init__(self, bot_name: str = "Botting Tree", pause_on_combat: bool = True, isolation_enabled=None, **_kwargs):
        self.bot_name = bot_name
        self.pause_on_combat = pause_on_combat
        self.isolation_enabled = isolation_enabled
        self.steps = []
        self.repeat = False

    def SetCurrentNamedPlannerSteps(
        self, steps, name="PlannerSequence", auto_start=False, reset=True, repeat=False, **_kwargs
    ):
        self.steps = list(steps)
        self.repeat = bool(repeat)

    @staticmethod
    def ActivateWidgetTree(widget_name: str, name: str | None = None):
        return BehaviorTree(_ActionNode(name=name or "ActivateWidget", widget_name=widget_name))

    @staticmethod
    def DeactivateWidgetTree(widget_name: str, name: str | None = None):
        return BehaviorTree(_ActionNode(name=name or "DeactivateWidget", widget_name=widget_name))

    @staticmethod
    def GetWidgetSetEnabledTree(widget_name: str, enabled: bool, name: str | None = None):
        return BehaviorTree(_ActionNode(name=name or "SetWidgetActive", widget_name=widget_name, enabled=enabled))

    @staticmethod
    def EnableAutoInventoryHandlerTree():
        return BehaviorTree(_ActionNode(name="EnableAutoInventoryHandler"))

    @staticmethod
    def DisableAutoInventoryHandlerTree():
        return BehaviorTree(_ActionNode(name="DisableAutoInventoryHandler"))

    @staticmethod
    def GetAutoInventoryHandlerSetEnabledTree(enabled: bool, name: str | None = None):
        return BehaviorTree(_ActionNode(name=name or "SetAutoInventoryHandlerActive", enabled=enabled))


def install() -> None:
    for name in list(sys.modules):
        if name == "Py4GWCoreLib" or name.startswith("Py4GWCoreLib."):
            sys.modules.pop(name, None)

    py4gwcorelib = types.ModuleType("Py4GWCoreLib")
    py4gwcorelib.__path__ = [str(REPO_ROOT / "Py4GWCoreLib")]
    sys.modules["Py4GWCoreLib"] = py4gwcorelib

    agent_mod = types.ModuleType("Py4GWCoreLib.Agent")
    agent_mod.Agent = types.SimpleNamespace(
        IsValid=lambda _agent_id: True,
        IsMoving=lambda _agent_id: False,
        IsAttacking=lambda _agent_id: False,
        GetXY=lambda _agent_id: (0.0, 0.0),
        GetModelID=lambda _agent_id: 0,
        GetNameByID=lambda _agent_id: "",
    )
    sys.modules["Py4GWCoreLib.Agent"] = agent_mod

    player_mod_core = types.ModuleType("Py4GWCoreLib.Player")
    player_mod_core.Player = types.SimpleNamespace(
        GetAgentID=lambda: 1,
        GetTargetID=lambda: 1,
        GetXY=lambda: (0.0, 0.0),
        ChangeTarget=lambda _agent_id: None,
        Move=lambda _x, _y: None,
    )
    sys.modules["Py4GWCoreLib.Player"] = player_mod_core

    global_cache_mod = types.ModuleType("Py4GWCoreLib.GlobalCache")
    global_cache_mod.GLOBAL_CACHE = types.SimpleNamespace(
        SkillBar=types.SimpleNamespace(GetCasting=lambda: 0),
        Skill=types.SimpleNamespace(GetID=lambda _name: 0),
    )
    sys.modules["Py4GWCoreLib.GlobalCache"] = global_cache_mod

    checks_mod = types.ModuleType("Py4GWCoreLib.routines_src.Checks")
    checks_mod.Checks = types.SimpleNamespace(
        Map=types.SimpleNamespace(MapValid=lambda: True, IsLoading=lambda: False),
        Player=types.SimpleNamespace(IsDead=lambda: False, IsKnockedDown=lambda: False, IsCasting=lambda: False),
    )
    sys.modules["Py4GWCoreLib.routines_src.Checks"] = checks_mod

    botting_mod = types.ModuleType("Py4GWCoreLib.BottingTree")
    botting_mod.BottingTree = _BottingTree
    sys.modules["Py4GWCoreLib.BottingTree"] = botting_mod

    behavior_pkg = types.ModuleType("Py4GWCoreLib.py4gwcorelib_src")
    behavior_pkg.__path__ = [str(REPO_ROOT / "Py4GWCoreLib" / "py4gwcorelib_src")]
    sys.modules["Py4GWCoreLib.py4gwcorelib_src"] = behavior_pkg

    behavior_mod = types.ModuleType("Py4GWCoreLib.py4gwcorelib_src.BehaviorTree")
    behavior_mod.BehaviorTree = BehaviorTree
    sys.modules["Py4GWCoreLib.py4gwcorelib_src.BehaviorTree"] = behavior_mod

    action_queue_mod = types.ModuleType("Py4GWCoreLib.py4gwcorelib_src.ActionQueue")
    action_queue_mod.ActionQueueManager = lambda: types.SimpleNamespace(
        ResetAllQueues=lambda: None,
        IsEmpty=lambda _queue_name: True,
    )
    sys.modules["Py4GWCoreLib.py4gwcorelib_src.ActionQueue"] = action_queue_mod

    routines_pkg = types.ModuleType("Py4GWCoreLib.routines_src")
    routines_pkg.__path__ = [str(REPO_ROOT / "Py4GWCoreLib" / "routines_src")]
    sys.modules["Py4GWCoreLib.routines_src"] = routines_pkg

    bt_mod = types.ModuleType("Py4GWCoreLib.routines_src.BehaviourTrees")
    bt_mod.BT = types.SimpleNamespace(
        Agents=_BTNamespace(),
        Composite=_CompositeNamespace(),
        Map=_BTNamespace(),
        Movement=_BTNamespace(),
        Party=_BTNamespace(),
        Player=_BTNamespace(),
        Shared=_BTNamespace(),
        Multibox=_BTNamespace(),
        Keybinds=_BTNamespace(),
        Items=_BTNamespace(),
        Skills=_BTNamespace(),
    )
    sys.modules["Py4GWCoreLib.routines_src.BehaviourTrees"] = bt_mod

    player_mod = types.ModuleType("Py4GWCoreLib.routines_src.behaviourtrees_src.player")
    player_mod.BT = bt_mod.BT
    sys.modules["Py4GWCoreLib.routines_src.behaviourtrees_src.player"] = player_mod

    enums_mod = types.ModuleType("Py4GWCoreLib.enums")
    enums_mod.Range = types.SimpleNamespace(
        Adjacent=types.SimpleNamespace(value=166.0),
        Nearby=types.SimpleNamespace(value=252.0),
        Area=types.SimpleNamespace(value=1000.0),
        Spellcast=types.SimpleNamespace(value=1248.0),
        Spirit=types.SimpleNamespace(value=2500.0),
        Earshot=types.SimpleNamespace(value=1012.0),
    )
    enums_mod.PlayerStatus = _PlayerStatus
    enums_mod.SharedCommandType = _CommandNamespace()
    sys.modules["Py4GWCoreLib.enums"] = enums_mod

    enum_pkg = types.ModuleType("Py4GWCoreLib.enums_src")
    enum_pkg.__path__ = [str(REPO_ROOT / "Py4GWCoreLib" / "enums_src")]
    sys.modules["Py4GWCoreLib.enums_src"] = enum_pkg

    multibox_mod = types.ModuleType("Py4GWCoreLib.enums_src.Multiboxing_enums")
    multibox_mod.SharedCommandType = _CommandNamespace()
    sys.modules["Py4GWCoreLib.enums_src.Multiboxing_enums"] = multibox_mod

    io_mod = types.ModuleType("Py4GWCoreLib.enums_src.IO_enums")
    io_mod.Key = types.SimpleNamespace(H=72, Escape=27)
    sys.modules["Py4GWCoreLib.enums_src.IO_enums"] = io_mod

    ui_mod = types.ModuleType("Py4GWCoreLib.enums_src.UI_enums")
    ui_mod.ControlAction = types.SimpleNamespace(ControlAction_OpenSkillsAndAttributes=types.SimpleNamespace(value=1))
    sys.modules["Py4GWCoreLib.enums_src.UI_enums"] = ui_mod

    botting_tree_pkg = types.ModuleType("Py4GWCoreLib.botting_tree_src")
    botting_tree_pkg.__path__ = [str(REPO_ROOT / "Py4GWCoreLib" / "botting_tree_src")]
    sys.modules["Py4GWCoreLib.botting_tree_src"] = botting_tree_pkg

    enums_tree_mod = types.ModuleType("Py4GWCoreLib.botting_tree_src.enums")
    enums_tree_mod.HeroAIStatus = types.SimpleNamespace(DISABLED=types.SimpleNamespace(value="disabled"))
    sys.modules["Py4GWCoreLib.botting_tree_src.enums"] = enums_tree_mod

    hero_setup_model = types.ModuleType("Py4GWCoreLib.botting_tree_src.hero_setup_model")
    hero_setup_model.resolve_hero_ids = _resolve_hero_ids
    hero_setup_model.get_team_by_priority = _get_team_by_priority
    sys.modules["Py4GWCoreLib.botting_tree_src.hero_setup_model"] = hero_setup_model

    native_pkg = types.ModuleType("Py4GWCoreLib.native_src")
    native_pkg.__path__ = [str(REPO_ROOT / "Py4GWCoreLib" / "native_src")]
    sys.modules["Py4GWCoreLib.native_src"] = native_pkg
    internals_pkg = types.ModuleType("Py4GWCoreLib.native_src.internals")
    internals_pkg.__path__ = [str(REPO_ROOT / "Py4GWCoreLib" / "native_src" / "internals")]
    sys.modules["Py4GWCoreLib.native_src.internals"] = internals_pkg
    types_mod = types.ModuleType("Py4GWCoreLib.native_src.internals.types")
    types_mod.PointPath = _PointPath
    types_mod.PointOrPath = object
    types_mod.Vec2f = _Point
    sys.modules["Py4GWCoreLib.native_src.internals.types"] = types_mod


def _resolve_hero_ids(value: Any) -> list[int]:
    if value is None:
        return []
    if isinstance(value, str):
        return [abs(hash(value)) % 100 + 1]
    if isinstance(value, list):
        return [abs(hash(str(item))) % 100 + 1 for item in value if item]
    return []


def _get_team_by_priority(max_heroes: int, required_hero_ids=None) -> list[int]:
    slots = max(0, int(max_heroes) - 1)
    team: list[int] = []
    for hero_id in list(required_hero_ids or []) + [24, 27, 21, 26, 25, 4, 37, 3]:
        hero_id = int(hero_id)
        if hero_id > 0 and hero_id not in team:
            team.append(hero_id)
    return team[:slots]
