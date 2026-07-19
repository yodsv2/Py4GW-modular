# Modular Target Collection Queue

This file is generated from the Python recipe source and target registry audit.
Collect encrypted names with the Modular Recorder, then replace display-name or nearest-fallback targeting.

## Summary

- Registry entries without encrypted names: 7
- Recipe keyed target uses missing encrypted names: 6
- Bare nearest-fallback target calls: 168

## Registry Entries Needing Encrypted Names

### Npc

- [ ] `CEMBRIEN` - Cembrien (`Py4GWCoreLib/modular/domain/target_registry.py:377`)
- [ ] `CREVASSE` - Crevasse (`Py4GWCoreLib/modular/domain/target_registry.py:378`)
- [ ] `GUARDSMAN_CHOW_OUTPOST` - Guardsman Chow (`Py4GWCoreLib/modular/domain/target_registry.py:345`)
- [ ] `LEN_CALDORON` - Len Caldoron (`Py4GWCoreLib/modular/domain/target_registry.py:412`)
- [ ] `SILISS_YASSITH` - Siliss Yassith (`Py4GWCoreLib/modular/domain/target_registry.py:441`)
- [ ] `YODS` - Yods (`Py4GWCoreLib/modular/domain/target_registry.py:452`)

### Enemy

- [ ] `ASURA_UNDERGATE` - Asura Undergate (`Py4GWCoreLib/modular/domain/target_registry.py:479`)

### Gadget

- Complete

## Keyed Recipe Uses Blocked By Missing Encrypted Names

### `npc:CEMBRIEN` - Cembrien (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/prophecies/ascalon.py:77` `Dialog`
- [ ] `Sources/modular_recipes/quests/prophecies/ascalon.py:88` `Dialog`

### `npc:CREVASSE` - Crevasse (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/shared.py:20` `Dialog`

### `npc:LEN_CALDORON` - Len Caldoron (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/shared.py:15` `Dialog`

### `npc:SILISS_YASSITH` - Siliss Yassith (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/prophecies/story.py:49` `Dialog`

### `npc:YODS` - Yods (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/prophecies/story.py:43` `Dialog`

## Bare Nearest-Fallback Calls

- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:32` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:57` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:76` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:81` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:86` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:89` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:94` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:97` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:104` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:106` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:108` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:110` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:124` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:126` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:128` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:168` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:319` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:321` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:361` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:395` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:412` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:418` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:434` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:451` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:459` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:467` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:469` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:471` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:504` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/crystal_desert.py:169` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:38` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:43` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:66` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:69` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:75` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:167` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:190` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:211` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:242` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:268` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:290` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:339` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:356` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:379` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:380` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:382` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:407` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:431` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:432` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:446` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:489` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:511` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:515` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:550` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:556` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:559` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:562` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:565` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:589` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:593` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:597` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:31` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:33` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:36` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:49` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:55` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:57` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:60` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:63` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:66` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:71` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:74` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:77` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:80` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:85` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:88` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:91` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:94` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:97` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:100` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:103` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:106` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:109` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:112` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:115` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:118` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:121` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:124` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:127` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:130` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:143` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:146` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:178` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:200` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:230` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:243` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:259` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:276` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:279` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:296` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:308` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:18` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:22` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:47` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:51` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:71` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:77` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:82` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:88` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:114` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:136` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:154` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:160` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:165` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:216` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:235` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:252` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:268` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:280` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:284` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:293` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:300` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:308` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ring_of_fire.py:51` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ring_of_fire.py:79` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ring_of_fire.py:81` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:21` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:33` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:88` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:107` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/factions/story.py:66` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/factions/story.py:68` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/fow/fissure_of_woe.py:22` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/nightfall/istan.py:536` `Dialog` `npc` without coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/ascalon.py:38` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/ascalon.py:40` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/ascalon.py:49` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:14` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:16` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:37` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:40` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:50` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:52` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:71` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:105` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:107` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:123` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:127` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:129` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:144` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:146` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:148` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:155` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:163` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/maguuma_jungle.py:36` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/maguuma_jungle.py:38` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/maguuma_jungle.py:60` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/maguuma_jungle.py:70` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/maguuma_jungle.py:80` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/maguuma_jungle.py:82` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/maguuma_jungle.py:111` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/northern_shiverpeaks.py:14` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/northern_shiverpeaks.py:16` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/northern_shiverpeaks.py:35` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/ring_of_fire.py:14` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/ring_of_fire.py:16` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/ring_of_fire.py:32` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/ring_of_fire.py:34` `Dialog` `npc` with coordinate
