# Changelog


## 2026-10-27 Questie optional (Guidepost 4.5.0)
- Guidepost: no Questie dependency. Blizzard quest log, tracking and map by default; Questie only through an optional, off-by-default setting with automatic fallback. No Questie code or data shipped. Other modules unchanged.

## 2026-10-27 Fox Trials 1.3.0: datamine hidden-data checks
The author (2026-10-27): "Add the check to Fox Trials" (the in-game checks from the datamine obfuscation assessment).
- 3 new high-impact checks (54 total): PVP-ALL-11 server-side tuning on a target dummy, PVP-ALL-12 hidden talents or Legacy perks, REP-06 server-only item-started quests.
- Minor, IN-GAME-CHECKS.md only: LVL-16 no test/placeholder entries, LVL-17 optional discovery (Manor Mistmantle, hidden portals), FAV-06 hidden items fill in.
- Code review: Reputation lists only a fixed set of 15 real factions (test factions excluded); the flight network drops the placeholder node and test maps never reach Guidepost. No bug found.
- Other add-ons and the install-all bundle are unchanged.

## 2026-10-25 In-game icons (Core 1.4.1, Guidepost 4.4.2, Rest 1.2.2, Reputation 1.2.1, Merchant's Favor 1.2.1)
The author (2026-10-25): "Add the in-game logos that artzy made to the appropriate addons." Cosmetic only, no new features.
- New Artzy icons (fennec fox on a teal tile, gold rim, add-on emblem) as the 32px window-header icon. A 64x64 TGA is used so WoW scales it down.
- Rest, Reputation and Merchant's Favor now ship their own `Media/` icon. Core keeps matching copies as a fallback.
- `## IconTexture` added to each changed .toc, so the icon shows in the AddOns list where the client supports it.
- Core 1.4.1 also ships the support line already in source (fennick@fennickaddons.dev in `/fennick help`).
- Fox Trials is unchanged (1.2.1).

## 2026-10-25 Support address, landing page, bug form, launch dates (docs/site only)
- Support and bug reports: fennick@fennickaddons.dev (README, DESCRIPTIONS, `/fennick help` line in all 10 languages; source only, ships with the next Core release).
- `site/`: static landing page for fennickaddons.dev (downloads, changelog, donation placeholder), using Artzy's icons; hosting steps in site/README.md.
- GitHub bug-report form and contact link (`.github/ISSUE_TEMPLATE`).
- Dates: WoW Forever releases Nov 4, so Fox Trials results are due Nov 7 (was Oct 29), in-game checks start Nov 4, and the freeze's live-play week runs Nov 4 to about Nov 11.

## 2026-10 Sleeping-bag notification (Rest 1.2.1, Guidepost 4.4.1, Fox Trials 1.2.1)
The author (2026-10-24): "The reminder should be there but more as a notification that is just to remind the player."
- Rest: the Cozy Sleeping Bag reminder is now a light notification: one brief on-screen message (UI error area) plus one chat line. Same conditions as before (you own the bag, it is off cooldown, buff missing or under 15 min, out of combat, outside a rest area, idle 1 min or logging out). Once per opportunity: it re-arms only after the conditions lapse. Fires whichever module has focus, Guidepost included. No longer in the Rest window or riders. New Rest setting "Sleeping bag reminder" (on by default). Optional sound through Core's "Sleeping bag reminder" cue (off by default). Nothing is used for you.
- Guidepost: no longer shows its own sleeping-bag line; Rest is the single owner.
- Fox Trials: LVL-15 rewritten for the one-notification rule (translated in all 9 languages). Still 51 checks.
- Install-all bundle name now includes the Rest version. RC-96 replaced (fires under Guidepost focus, once, never duplicated).

## 2026-10 Scope audit (Core 1.4.0, Guidepost 4.4.0, Rest 1.2.0, Reputation 1.2.0, Merchant's Favor 1.2.0, Fox Trials 1.2.0)
Applies the reviewed scope-audit fix list (reviews/scope/COMBINED.md), approved by the author on 2026-10-24, in five batches.
- Docs: SCOPE-AUDIT corrections, rule clarifications (build/profession advice was a setup-menu and leveling scope limit; audio is allowed as optional, toggled cues), API.md module boundaries, HOTFIX.md, download and language notes.
- Core: sound cue registry with per-cue toggles (all off), plain-language version-mismatch line, one line per module in setup and `/beast help`.
- Guidepost: cues through Core; the old upgrade step no longer switches off Sounds suite-wide; opacity and minimap left to Core. Profession hints unchanged.
- Reputation: Darkmoon Faire dates marked unconfirmed, calendar fallback after the last known week. Merchant's Favor: writ customer locations (unconfirmed) and daily reset countdown.
- Fox Trials: 51 checks. It is now a tester-only download; players get the install-all bundle without it.
- CI: S5 boundary guard. Regression tests RC-91..RC-100.

## 2026-10 Guidepost (Guidepost 4.3.1)
- The Fennick Leveling Guide is now **Fennick's Guidepost**: new name in the AddOns list (Notes say "formerly the Fennick Leveling Guide"), window and module titles, Core module picker, Settings, setup page, minimap tooltip, key bindings and Fox Trials filter. The name stays in English in every language.
- Folder and .toc are now `Fennick_Guidepost`; saved variables are `Fennick_GuidepostDB` (per character) and `Fennick_GuidepostProfiles` (account). Saved data starts fresh (pre-release, no migration). Delete any old `Fennick_LevelingGuide` folder. Module key `leveling` and all slash commands are unchanged.
- New Guidepost icon from Artzy's brand art (`Fennick_Guidepost/Media`).

## 2026-10 l10n (Core 1.3.0, Leveling 4.3.0, Rest 1.1.0, Reputation 1.1.0, Merchant's Favor 1.1.0, Fox Trials 1.1.0)
- Multi-language (Option D): locale framework in Core; machine-translated UI text, Leveling step notes and Fox Trials texts for deDE, frFR, esES (esMX), itIT, ptBR (ptPT), ruRU, koKR, zhCN, zhTW, labelled "machine translation" in Settings and on the setup welcome page until reviewed. Coverage: translations/STATUS.md.
- English text, fonts and slash commands unchanged. Quest/item/zone/faction/spell names come from the client by ID; NPC names from Questie when installed.
- Five English-text dependencies removed (hearth, buying hints, inn bind, danger notes, Merchant's Favor currency). Cinzel titles fall back to the client font on ruRU/koKR/zhCN/zhTW. Buttons size to their label.
- Reviewers: CONTRIBUTING-TRANSLATIONS.md and translations/<locale>.csv (repo only). Fox Trials 48 checks (+CORE-L1); minor locale checks in IN-GAME-CHECKS.md.

## 2026-10 (Core 1.2.0, Leveling 4.2.0, Rest 1.0.1, Reputation 1.0.2, Merchant's Favor 1.0.2, Fox Trials 1.0.0)
- Core: module API gate (a module needing a newer Core refuses with one chat line), Core-owned `/fennick` with module subcommands and help, view hash (no redraw when nothing changed), saved-settings schema with `_unknown` keys kept, shared event frame and idle clock, Arrow/TomTom only removes its own waypoints and never touches TomTom in combat, Edit Mode nudge keys only after a click, setup X counts as Skip, guidance overflow tooltip, minimap left-click = window / Shift-click = module, combat tooltip off by default, realm date for Darkmoon Faire and daily resets.
- Look: Artzy's teal and gold look with module icons, focus card and gold progress bar; shared status colours honour the colour-blind option.
- Leveling: progress keyed by stable step IDs (reloads, regenerated data and inserted steps no longer shift your place or skips), bounded saved tables, protected init, coalesced events, one rule for showing the window, settings duplicated in Core removed, hub index built out of combat, kills-to-level counts rested XP, unknown race uses your faction's route, reward pick waits for item data, item and spell IDs instead of English names.
- Rest: cached advice, keeps the hearthstone when the route uses it soon, hidden at max level. Reputation: every item of a multi-item turn-in needs its own count, calendar hint after the faire schedule ends, "Unskip all". Merchant's Favor: realm daily reset, currency by ID.
- Fox Trials (new): in-game test checklist for playtesters.

## Leveling v3.5 changes
- **Layout**: one constants table (`E.LAYOUT`) plus settings for window width, padding (14), step spacing (8), line spacing (3), font size. Every text line has an explicit width, its measured height, and the window resizes to fit. The header has its own padding and a divider line. The current step sits in a highlighted box. `/fennick layout` outlines every region in game so you can check spacing.
- **Interaction steps**: vendor, trainer, flight path, hearthstone, bank, stable, "talk to" and deathskip steps now say exactly what to do. They complete only after you do it: the merchant window is opened and closed, or the bought items are in your bags; the trainer window is closed or the spell is known; the flight map is opened; your bind location matches; and so on. Getting to the spot never completes them. Only plain "go to" steps with no NPC complete on arrival (within 15 yd).
- **Arrow**: every step you still need to do has a waypoint. If a step had no coordinates, it uses the nearest coordinate from the plan. Hunt steps use Questie spawn clusters when Questie is loaded, otherwise the plan's hotspots, as a 2-6 point patrol. The next patrol point comes up when you get within *Patrol arrival radius* (default 50 yd). The step itself still waits for your quest objectives. The waypoint is set again if TomTom drops it, after combat and after a zone change. If TomTom fails, the built-in arrow is used.

## Leveling v3.7 changes
- **Gear:** only the one-line quest reward pick is left. Vendor upgrade stops, weapon warnings, weapon-skill reminders and gear notes are gone.
- **Route data cleanup:**
  - Steps that could never show for your class are removed.
  - Turn-ins and objectives that came before their pickup are moved after it.
  - Duplicate pickups are removed.
  - Patrols are kept within 400 yd.
  - Quest and NPC steps use that quest's or NPC's real location where one is known. Otherwise the location shows as "approx.".
- **NPC checks:** vendor, trainer, flight, bank and stable steps now count only when you use the NPC named on the step.
- **Old settings:** settings from earlier versions are cleaned up when you log in.

## Leveling v3.7.1 changes
- Patrols: the arrow moves to the next patrol point when you arrive within the Patrol arrival radius, once per arrival, and loops until your objectives are done. The step itself completes only on objectives. Points closer than 2x the radius are merged, and the patrol position survives reloads. `/fennick debug` logs each patrol arrival.
- Arrow: only one arrow is ever shown (TomTom or the built-in one). In combat an existing TomTom arrow stays as is; the built-in arrow is never shown on top of it. Leftover Fennick TomTom waypoints are removed on login.

## Leveling v3.8 changes
- PvP escape: the arrow switches to the escape route immediately, also in combat. The TomTom waypoint is swapped once, guarded, and the normal target comes back after combat; the built-in arrow switches immediately too.
- Patrol: one continuous loop with no point counter. The arrow first goes to the patrol point closest to you (on entering the step, after a reload, zone change, resurrect, branch/escape, or when you stray more than 2x the radius off the loop), then loops in the direction with the nearer next point. Loops are ordered at build as a shortest closed tour. The step completes only on its objectives.
- Focused view: only the current step, with live quest objectives, a thin separator and a Guidance section of up to 3 short lines (tips, plus Watch out items for HC/danger/escape, elites, contested zones). Hover the Guidance section for the full list.

## Leveling v3.8.1 changes
- Fixed ADDON_ACTION_FORBIDDEN at login and on minimap left-click: the add-on no longer registers the combat log event, which this client forbids. Kill tracking and PvP hit detection use unit events instead. The on/off toggle no longer re-registers events. `/fennick debuglog` now shows the blocked function and what the add-on was doing.
- The focused view is the only view. The List view, its header button, setting and wizard page are gone; saved list choices move to focused. The list layout code is kept but switched off (E.FEATURE_LIST_VIEW = false).
- More room: width 400, padding 16, line spacing 4 (old saved defaults are updated), larger header line. Guidance lines wrap instead of being cut off, up to 3 lines; anything more is "(+n)" and in the hover tooltip. Watch-out items are kept first when space is short.

## Leveling v3.8.2
- Hunt points checked against Questie Forever spawns; 135 off-target hunts re-pointed (incl. Wiry Swoop).
- Missed pickups: a short callback to the quest giver, or the quest's steps are skipped. Restored when you accept it.
- Skip/Back/jump rebuilds the arrow and patrol at once, also in combat.

## Leveling v3.8.3
- '#completewith' background steps (e.g. Well Stones) no longer block the main step (cleanse the well). Use-item steps say 'Use <item>'.
- Buy steps complete on buying from the vendor or when bags hold the items. The text says why (mana drink, food, ammo).
- No sounds: TomTom waypoints are silent; own sounds only if you switch Sounds on.

## Leveling v4.1.0
- **Re-pathing**: when bonuses (rested, food, bag, perks) put you ahead of the route, low-value steps drop out. +1 level: gap-fill grinds and extra hunting. +1.5: optional quests worth under 60% of the leg's XP per minute, or grey at turn-in. Hardcore needs 0.5 more. PvP trims contested-zone quests first. Below +0.5 everything comes back. Never trimmed: class quests, chain steps and anything a later quest needs, big turn-ins, chain-end (gear) quests, quests in your log, and steps you went Back to. Focus shows one line; `/fennick why` lists what was skipped and why. No next-zone jumps.
- **Boost prompts** (one line, no sound, never used for you): XP food before kill-heavy hunts when Well Fed is missing or under 3 min and you carry XP food for your level; Archmagister's Wisdom before Undead hunts; the sleeping bag at breaks. Quiet in combat, with an elite or boss targeted, on turn-in/travel steps, while escaping and in Hardcore contested zones.
- Every bind and hearth step on every route is checked against friendly innkeepers (75 binds, all friendly); text-only binds now carry the innkeeper's real location.
- Needs Core 1.1 (text size offset replaces the old font setting).

## Leveling v4.0.0
- Now a module of Fennick's Beast Core: the arrow, look, setup, settings, minimap button and frame moving come from Core.
- Optional cloth donations: on a capital visit already on your route, if you carry 60 of the cloth, a donation step appears (otherwise it is skipped). Never farm cloth for it.
- Tooltip lines XP per kill and kills to level.

## Leveling v3.11.0
- Library books: the route picks up cheap books along the way (towns and low camps), and you hand them in at your librarian (Garion Wendell, Stormwind / Owen Thadd, Undercity) when the route passes the city. The hand-in only shows if you have the book.
- Forever-new quests: 33 placements (accept, hunt with patrol, turn-in) where the XP per added minute beats the route. Hardcore skips contested zones and elites.
- Every race start route is evaluated equally. Details and sources: FOREVER-EXTRAS-INVENTORY.md.

## Leveling v3.10.0
- Forever loot-started quests: when a hunt's mob can drop a quest-starting item, a short "along the way" line says so. When the item lands in your bags you get one chat line and a Focus tip to right-click it (no sound). The turn-in step only shows if you actually got the quest.
- Added this build: Elmpaw's Head (Elwynn), Harvesting the Harvesters (Westfall), Baron Marinous (Darkshore). All three are solo for every class and in every ruleset. Elite or group drops are never routed.
- Full inventory (item-started, librarian/book and exploration quests, class fit, data gaps): FOREVER-EXTRAS-INVENTORY.md.

## Leveling v3.9.0
- NPCs and mobs are matched by creature ID, so steps work on non-English clients.
- No missed-quest decisions until the quest log has loaded (status line "Retrieving quest log..."); re-checked after every loading screen.
- A failed escort or timed quest gets a step: abandon and take it again from the quest giver.
- Forever quest variants: only with strong evidence (see VARIANT-REVIEW.md; this build: 0 merged), and only when your quest log shows the same title and objectives. Setting: "Match Forever quest variants" (on).
- Hardcore: escort/timed quests are never auto-accepted (setting, on). Gold-cost quests are never auto-completed. `/fennick noauto` (target an NPC) adds or removes it from the don't-automate list; `/fennick noauto list`.
- Quest log full: one line telling you which quest to drop.
- Hearth steps complete with any hearth item (cast, then arrival at your bind location).
- If you remove the Fennick waypoint in TomTom, it stays off until the next step.
- Hardcore: one-line warning when a step is in a zone well above your level.
- `/fennick why` (or `/flg why`): what the current step is still waiting for, and which quest ID matched.
- `/fennick restore`: puts back Blizzard settings Fennick changed (instant quest text).
- Saved settings are checked at login; a broken part is reset on its own.

