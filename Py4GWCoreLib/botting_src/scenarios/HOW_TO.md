# Scenario How-To

This layer is for reusable objective content only.

## Design Rule

- Keep setup and flow in the bot script.
- Keep reusable route/objective actions in scenario JSON.

Examples of setup/flow that should stay in bot scripts:
- HeroAI or CustomBehaviors toggles
- Multibox summon/invite/party logic
- retries, jump-to-step, loop control
- custom states and managed coroutines

Examples of reusable scenario content:
- movement route
- map travel segments
- interaction/dialog steps
- generic waits tied to route completion

## Files

- Manifest: `Py4GWCoreLib/botting_src/scenarios/manifest.json`
- Scenario files:
  - `Py4GWCoreLib/botting_src/scenarios/missions/*.json`
  - `Py4GWCoreLib/botting_src/scenarios/quests/*.json`
  - `Py4GWCoreLib/botting_src/scenarios/runs/*.json`
  - `Py4GWCoreLib/botting_src/scenarios/vanquishes/*.json`

## Register A Scenario

1. Add a key in the correct manifest section.
2. Point it to the scenario JSON file.

Example:

```json
{
  "vanquishes": {
    "MOUNT_QINKAI": "vanquishes/mount_qinkai.json"
  }
}
```

Enum values are generated from manifest keys at import time, so this key becomes:
- `vanquishEnum.MOUNT_QINKAI`
- `VanquishEnum.MOUNT_QINKAI`

## JSON Format

Required top-level fields:

- `id` (string)
- `kind` (`"mission" | "quest" | "run" | "vanquish"`)
- `actions` (array)

Optional:

- `name`
- `metadata`

Action object fields:

- `action` (string)
- `args` (array, optional)
- `kwargs` (object, optional)
- `optional` (bool, optional, default false)
- `description` (string, optional)

Any extra keys inside an action object are treated as `kwargs`.

Dialog IDs:
- `Dialogs.WithModel` and `Dialogs.AtXY` require `dialog_id`.
- Write dialog IDs in hex style as strings.
  - Example: `"0x86"`
- The scenario executor converts hex strings to integers before calling Botting methods.

## Action Naming

Preferred:
- `Component.Method` (explicit and stable), e.g.:
  - `Move.FollowAutoPath`
  - `Wait.UntilOutOfCombat`
  - `Map.Travel`
  - `Dialogs.WithModel`

The executor also supports normalized aliases, but explicit dotted names are recommended.

## Bot Usage

Use the same scenario call regardless of setup style.

```python
from Py4GWCoreLib import Botting, vanquishEnum

bot = Botting("Any Bot")

# setup style can differ per script (HeroAI, CustomBehaviors, multibox, etc.)
# ...

bot.vanquish(vanquishEnum.MOUNT_QINKAI)
```

## Runtime Result

Scenario calls enqueue execution into the FSM.

- queue/resolve result from call: `True/False`
- runtime outcome after execution:
  - `bot.Scenarios.LastSuccess()`
  - `bot.Scenarios.LastResult()`

Example:

```python
queued = bot.vanquish(vanquishEnum.MOUNT_QINKAI)
if not queued:
    # failed to resolve/register scenario
    pass

# later after FSM updates:
if not bot.Scenarios.LastSuccess():
    result = bot.Scenarios.LastResult()
    # bot-script decides retry/jump/fallback behavior
```
