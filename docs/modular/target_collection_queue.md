# Modular Target Collection Queue

This file is generated from the Python recipe source and target registry audit.
Collect encrypted names with the Modular Recorder, then replace display-name or nearest-fallback targeting.

## Summary

- Registry entries without encrypted names: 41
- Recipe keyed target uses missing encrypted names: 88
- Bare nearest-fallback target calls: 168

## Registry Entries Needing Encrypted Names

### Npc

- [ ] `BARTHOLOS` - Bartholos (`Py4GWCoreLib/modular/domain/target_registry.py:326`)
- [ ] `BLIMM` - Blimm (`Py4GWCoreLib/modular/domain/target_registry.py:328`)
- [ ] `BUDGER_BLACKPOWDER` - Budger Blackpowder (`Py4GWCoreLib/modular/domain/target_registry.py:333`)
- [ ] `CAPTAIN_LANGMAR` - Captain Langmar (`Py4GWCoreLib/modular/domain/target_registry.py:334`)
- [ ] `CEMBRIEN` - Cembrien (`Py4GWCoreLib/modular/domain/target_registry.py:335`)
- [ ] `CREVASSE` - Crevasse (`Py4GWCoreLib/modular/domain/target_registry.py:336`)
- [ ] `EXPERIMENT_KREWE_MEMBER` - Experiment Krewe Member (`Py4GWCoreLib/modular/domain/target_registry.py:338`)
- [ ] `GADD` - Gadd (`Py4GWCoreLib/modular/domain/target_registry.py:339`)
- [ ] `GUARDSMAN_CHOW` - Guardsman Chow (`Py4GWCoreLib/modular/domain/target_registry.py:304`)
- [ ] `GUARDSMAN_CHOW_OUTPOST` - Guardsman Chow (`Py4GWCoreLib/modular/domain/target_registry.py:305`)
- [ ] `G_O_L_E_M_2_0_DEFENSE` - G.O.L.E.M. 2.0 [Defense] (`Py4GWCoreLib/modular/domain/target_registry.py:349`)
- [ ] `G_O_L_E_M_2_0_MELEE` - G.O.L.E.M. 2.0 [Melee] (`Py4GWCoreLib/modular/domain/target_registry.py:350`)
- [ ] `G_O_L_E_M_2_0_RANGED` - G.O.L.E.M. 2.0 [Ranged] (`Py4GWCoreLib/modular/domain/target_registry.py:351`)
- [ ] `HIGH_PRIEST_ALKAR` - High Priest Alkar (`Py4GWCoreLib/modular/domain/target_registry.py:352`)
- [ ] `INSCRIPTION_STONE` - Inscription Stone (`Py4GWCoreLib/modular/domain/target_registry.py:353`)
- [ ] `JALIS_IRONHAMMER` - Jalis Ironhammer (`Py4GWCoreLib/modular/domain/target_registry.py:354`)
- [ ] `LEFT_SIEGE_DEVOURER` - Left Siege Devourer (`Py4GWCoreLib/modular/domain/target_registry.py:356`)
- [ ] `LEN_CALDORON` - Len Caldoron (`Py4GWCoreLib/modular/domain/target_registry.py:357`)
- [ ] `LIVIA` - Livia (`Py4GWCoreLib/modular/domain/target_registry.py:358`)
- [ ] `LORK` - Lork (`Py4GWCoreLib/modular/domain/target_registry.py:359`)
- [ ] `MACHINE_KREWE_MEMBER` - Machine Krewe Member (`Py4GWCoreLib/modular/domain/target_registry.py:360`)
- [ ] `MAMP` - Mamp (`Py4GWCoreLib/modular/domain/target_registry.py:361`)
- [ ] `PLAXX` - Plaxx (`Py4GWCoreLib/modular/domain/target_registry.py:365`)
- [ ] `RENK` - Renk (`Py4GWCoreLib/modular/domain/target_registry.py:367`)
- [ ] `RIGHT_SIEGE_DEVOURER` - Right Siege Devourer (`Py4GWCoreLib/modular/domain/target_registry.py:368`)
- [ ] `SILISS_YASSITH` - Siliss Yassith (`Py4GWCoreLib/modular/domain/target_registry.py:383`)
- [ ] `SKY_KREWE_MEMBER` - Sky Krewe Member (`Py4GWCoreLib/modular/domain/target_registry.py:384`)
- [ ] `SOKKA` - Sokka (`Py4GWCoreLib/modular/domain/target_registry.py:385`)
- [ ] `WORKER_GOLEM` - Worker Golem (`Py4GWCoreLib/modular/domain/target_registry.py:387`)
- [ ] `YODS` - Yods (`Py4GWCoreLib/modular/domain/target_registry.py:388`)

### Enemy

- [ ] `ASURA_UNDERGATE` - Asura Undergate (`Py4GWCoreLib/modular/domain/target_registry.py:415`)
- [ ] `CYNDR_THE_MOUNTAIN_HEART` - Cyndr the Mountain Heart (`Py4GWCoreLib/modular/domain/target_registry.py:420`)
- [ ] `INDESTRUCTIBLE_GOLEM` - Indestructible Golem (`Py4GWCoreLib/modular/domain/target_registry.py:422`)
- [ ] `INSCRIBED_ETTIN` - Inscribed Ettin (`Py4GWCoreLib/modular/domain/target_registry.py:423`)
- [ ] `INSCRIBED_SENTRY` - Inscribed Sentry (`Py4GWCoreLib/modular/domain/target_registry.py:424`)
- [ ] `THE_GREAT_DESTROYER` - The Great Destroyer (`Py4GWCoreLib/modular/domain/target_registry.py:425`)

### Gadget

- [ ] `GOLEM_DISABLING_LEVER` - Golem Disabling Lever (`Py4GWCoreLib/modular/domain/target_registry.py:449`)
- [ ] `INSCRIPTION_STONE` - Inscription Stone (`Py4GWCoreLib/modular/domain/target_registry.py:450`)
- [ ] `MOUNTAIN_HEART_CHEST` - Mountain Heart Chest (`Py4GWCoreLib/modular/domain/target_registry.py:451`)
- [ ] `MYSTICAL_KEYHOLDER` - Mystical Keyholder (`Py4GWCoreLib/modular/domain/target_registry.py:452`)
- [ ] `UNSTABLE_MAGICAL_ENERGY_STORAGE` - Unstable Magical Energy Storage (`Py4GWCoreLib/modular/domain/target_registry.py:453`)

## Keyed Recipe Uses Blocked By Missing Encrypted Names

### `enemy:CYNDR_THE_MOUNTAIN_HEART` - Cyndr the Mountain Heart (missing encrypted names)

- [ ] `Sources/modular_recipes/dungeons/eotn.py:136` `MoveToTarget`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:141` `MoveToTarget`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:146` `MoveToTarget`

### `enemy:INDESTRUCTIBLE_GOLEM` - Indestructible Golem (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:139` `MoveToTarget`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:144` `MoveToTarget`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:149` `MoveToTarget`

### `enemy:INSCRIBED_ETTIN` - Inscribed Ettin (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:29` `MoveToTarget`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:30` `MoveToTarget`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:35` `MoveToTarget`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:36` `MoveToTarget`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:41` `MoveToTarget`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:42` `MoveToTarget`

### `enemy:INSCRIBED_SENTRY` - Inscribed Sentry (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:16` `MoveToTarget`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:17` `MoveToTarget`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:25` `MoveToTarget`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:26` `MoveToTarget`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:27` `MoveToTarget`

### `enemy:THE_GREAT_DESTROYER` - The Great Destroyer (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/shared.py:19` `MoveToTarget`

### `gadget:GOLEM_DISABLING_LEVER` - Golem Disabling Lever (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:82` `Interact`

### `gadget:INSCRIPTION_STONE` - Inscription Stone (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:21` `Interact`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:31` `Interact`

### `gadget:MOUNTAIN_HEART_CHEST` - Mountain Heart Chest (missing encrypted names)

- [ ] `Sources/modular_recipes/dungeons/eotn.py:152` `Interact`

### `gadget:MYSTICAL_KEYHOLDER` - Mystical Keyholder (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:86` `Interact`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:91` `Interact`

### `gadget:UNSTABLE_MAGICAL_ENERGY_STORAGE` - Unstable Magical Energy Storage (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:138` `Interact`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:143` `Interact`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:148` `Interact`

### `npc:BARTHOLOS` - Bartholos (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:20` `Dialog`

### `npc:BLIMM` - Blimm (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:74` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:65` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:71` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:75` `Interact`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:76` `Dialog`

### `npc:BUDGER_BLACKPOWDER` - Budger Blackpowder (missing encrypted names)

- [ ] `Sources/modular_recipes/dungeons/eotn.py:97` `Dialog`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:100` `Interact`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:110` `Interact`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:120` `Interact`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:126` `Interact`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:135` `Interact`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:140` `Interact`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:145` `Interact`

### `npc:CAPTAIN_LANGMAR` - Captain Langmar (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/vanguard.py:52` `Dialog`

### `npc:CEMBRIEN` - Cembrien (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/prophecies/ascalon.py:77` `Dialog`
- [ ] `Sources/modular_recipes/quests/prophecies/ascalon.py:88` `Dialog`

### `npc:CREVASSE` - Crevasse (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/shared.py:20` `Dialog`

### `npc:EXPERIMENT_KREWE_MEMBER` - Experiment Krewe Member (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:69` `Dialog`

### `npc:GADD` - Gadd (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:47` `Interact`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:48` `Dialog`

### `npc:GUARDSMAN_CHOW` - Guardsman Chow (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/factions/story.py:94` `Dialog`

### `npc:GUARDSMAN_CHOW_OUTPOST` - Guardsman Chow (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/factions/story.py:97` `Dialog`

### `npc:G_O_L_E_M_2_0_DEFENSE` - G.O.L.E.M. 2.0 [Defense] (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/shared.py:33` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/shared.py:49` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/shared.py:79` `Dialog`

### `npc:G_O_L_E_M_2_0_MELEE` - G.O.L.E.M. 2.0 [Melee] (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/shared.py:35` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/shared.py:51` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/shared.py:81` `Dialog`

### `npc:G_O_L_E_M_2_0_RANGED` - G.O.L.E.M. 2.0 [Ranged] (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/shared.py:31` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/shared.py:47` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/shared.py:77` `Dialog`

### `npc:HIGH_PRIEST_ALKAR` - High Priest Alkar (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/shared.py:16` `Dialog`

### `npc:INSCRIPTION_STONE` - Inscription Stone (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:13` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:49` `Interact`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:50` `Dialog`

### `npc:JALIS_IRONHAMMER` - Jalis Ironhammer (missing encrypted names)

- [ ] `Sources/modular_recipes/dungeons/eotn.py:93` `Dialog`
- [ ] `Sources/modular_recipes/dungeons/eotn.py:154` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/shared.py:29` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/norn.py:11` `Dialog`

### `npc:LEFT_SIEGE_DEVOURER` - Left Siege Devourer (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/vanguard.py:37` `Dialog`

### `npc:LEN_CALDORON` - Len Caldoron (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/shared.py:15` `Dialog`

### `npc:LIVIA` - Livia (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:16` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:27` `Dialog`

### `npc:LORK` - Lork (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:61` `Dialog`

### `npc:MACHINE_KREWE_MEMBER` - Machine Krewe Member (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:99` `Dialog`

### `npc:MAMP` - Mamp (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:47` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:65` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:104` `Dialog`

### `npc:PLAXX` - Plaxx (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:87` `Dialog`

### `npc:RENK` - Renk (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:95` `Dialog`
- [ ] `Sources/modular_recipes/quests/eotn/asura.py:101` `Dialog`

### `npc:RIGHT_SIEGE_DEVOURER` - Right Siege Devourer (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/vanguard.py:39` `Dialog`

### `npc:SILISS_YASSITH` - Siliss Yassith (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/prophecies/story.py:49` `Dialog`

### `npc:SKY_KREWE_MEMBER` - Sky Krewe Member (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/eotn/asura.py:93` `Dialog`

### `npc:SOKKA` - Sokka (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/shared.py:37` `Interact`

### `npc:WORKER_GOLEM` - Worker Golem (missing encrypted names)

- [ ] `Sources/modular_recipes/missions/eotn/asura.py:78` `Dialog`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:106` `Interact`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:125` `Interact`
- [ ] `Sources/modular_recipes/missions/eotn/asura.py:127` `Interact`

### `npc:YODS` - Yods (missing encrypted names)

- [ ] `Sources/modular_recipes/quests/prophecies/story.py:43` `Dialog`

## Bare Nearest-Fallback Calls

- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:31` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:56` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:75` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:80` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:85` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:88` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:93` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:96` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:103` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:105` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:107` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:109` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:123` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:125` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:127` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:166` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:316` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:318` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:358` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:391` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:408` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:414` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:430` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:447` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:455` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:463` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:465` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:467` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ascalon.py:500` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/crystal_desert.py:165` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:37` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:42` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:65` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:68` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:74` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:166` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:189` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:210` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:240` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:266` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:288` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:337` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:353` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:376` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:377` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:379` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:404` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:428` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:429` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:443` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:485` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:507` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:511` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:545` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:551` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:554` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:557` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:560` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:584` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:588` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/kryta.py:592` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:30` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:32` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:35` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:48` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:54` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:56` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:59` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:62` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:65` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:70` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:73` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:76` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:79` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:84` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:87` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:90` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:93` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:96` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:99` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:102` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:105` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:108` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:111` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:114` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:117` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:120` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:123` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:126` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:129` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:142` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:145` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:176` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:198` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:228` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:241` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:257` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:274` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:277` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:294` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/maguuma_jungle.py:306` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:17` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:21` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:46` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:50` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:70` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:76` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:81` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:87` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:113` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:135` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:153` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:159` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:164` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:214` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:233` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:250` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:266` `Interact` `npc` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:278` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:282` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:291` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:298` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/northern_shiverpeaks.py:306` `Interact` `gadget` without coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ring_of_fire.py:49` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ring_of_fire.py:76` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/ring_of_fire.py:78` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:20` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:32` `Interact` `gadget` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:86` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/missions/prophecies/southern_shiverpeaks.py:104` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/factions/story.py:66` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/factions/story.py:68` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/fow/fissure_of_woe.py:22` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/nightfall/story.py:861` `Dialog` `npc` without coordinate
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
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:81` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:83` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:99` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:103` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:105` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:120` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:122` `Interact` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:124` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:131` `Dialog` `npc` with coordinate
- [ ] `Sources/modular_recipes/quests/prophecies/kryta.py:139` `Dialog` `npc` with coordinate
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
