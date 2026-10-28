# Fennick's Beast — Core + modules (Forever, Interface 16001)

Free add-ons. Not for sale; donations only. License: PolyForm Noncommercial 1.0.0 (`LICENSE.md` in every add-on folder).

Donations: not yet open (pending approval)

**Support and bug reports:** fennick@fennickaddons.dev, or open a bug report at https://github.com/Dagodeiwos/fennick-releases/issues/new/choose. Downloads: https://github.com/Dagodeiwos/fennick-releases/releases. In game, `/fennick help` shows the same address.

## Launch timeline
- **Nov 4, 2026:** WoW Forever releases. No in-game testing is possible before this date; every in-game check (Fox Trials, "unconfirmed" data) starts Nov 4 or later.
- **Sat Nov 7, 2026:** Fox Trials results due (moved from Thu Oct 29). Anything still Untested or Failed ships as a known issue or is switched off by default.
- **Nov 4 to about Nov 11, 2026:** the feature freeze's one week of live play. Feature work resumes only after it shows no P0 or P1 defects.

| Folder | Zip | Needs |
|---|---|---|
| `Fennick_BeastCore` | Fennick-Beast-Core-v1.4.0.zip | nothing (works alone or with any modules) |
| `Fennick_Guidepost` | Fennick-Guidepost-v4.4.1.zip (Fennick's Guidepost, formerly the Leveling Guide) | Fennick_BeastCore 1.2 |
| `Fennick_Rest` | Fennick-Rest-v1.2.1.zip | Fennick_BeastCore 1.2 |
| `Fennick_Reputation` | Fennick-Reputation-v1.2.0.zip | Fennick_BeastCore 1.2 |
| `Fennick_MerchantsFavor` | Fennick-Merchants-Favor-v1.2.0.zip | Fennick_BeastCore 1.2 |
| `Fennick_Trailmarks` | Fennick-Trailmarks-v1.0.2.zip (Fennick's Trailmarks: map finds, optional) | Fennick_BeastCore 1.2 |
| `Fennick_Cartographer` | Fennick-Cartographer-v1.0.1.zip (Fennick's Cartographer: world map and minimap, optional) | Fennick_BeastCore 1.2 (1.5 for other modules' pins) |
| `Fennick_FoxTrials` | Fennick-Fox-Trials-v1.3.0.zip | Fennick_BeastCore 1.2 (testers only; not in the install-all bundle) |

Install Core plus only the modules you want. Guidepost is optional: Core has no leveling content, and the setup and Focus list show only the modules you installed. A module that needs a newer Core says so in one chat line and stays off (no Lua error). Fennick's Guidepost (formerly the Fennick Leveling Guide) unpacks into `Fennick_Guidepost` and needs Beast Core; delete any older `Fennick_LevelingGuide` folder first. Version history: `CHANGELOG.md`.

## Downloads
- **Players:** the *install all* bundle (`Fennick-Suite-Install-All-…zip`): Beast Core, Guidepost, Rest, Reputation, Merchant's Favor, Trailmarks (optional) and Cartographer (optional). Or pick single add-ons; only Beast Core is required.
- **Testers only:** Fennick's Fox Trials, a separate zip. It is not in the install-all bundle.
- **Languages:** German, French, Spanish, Italian, Portuguese (BR), Russian, Korean and Chinese (Simplified/Traditional) are machine translations that people have not reviewed yet. The game shows a note about this in setup and Settings, and any missing or broken string falls back to English. English is unchanged.
- **Hotfixes and rollback:** see `HOTFIX.md`. The current and previous version of every add-on stay available.

## Core (v1.4.0)
One window (Focus view), one waypoint arrow, shared look, setup, settings, minimap button, monster tooltip and frame moving. Core owns every Fennick command: `/fennick`, `/beast` or `/fbc` with `setup`, `move`, `move reset`, `why`, `focuson <module|auto>`, `minimap`, `debug`, `help`. Modules add their own words (for example `/fennick skip`, `/fennick lvl list`, `/fennick trials`); `/fennick help` lists everything and an unknown word prints the list.
- **Minimap button:** left-click shows or hides the window, Shift-click turns the focused module on or off, right-click opens Settings, drag to move.
- **Look (1.2):** teal and gold by default, with module icons, a gold 1 px edge, a focus card with an amber bar and gold GUIDANCE label. Style "dark" is the old neutral look, "minimal" has no frame. Colour-blind colours (Settings) apply to every module.
- **Focus**: pick one module or Auto. The focused module owns the arrow (and TomTom, when installed). In Auto, the first module with something to do owns it and the others add one short line each. Two modules never drive the arrow at once.
- **Monster tooltip**: level range, elite/rare, health (when known), quests in your log or on your route, notable and quest-starting drops, cloth for humanoids. With Leveling installed, it adds XP per kill and kills to level. Each line can be turned off; the tooltip stops at 8 lines, and nothing is added in combat unless you turn that on. Hooks only (no taint), and no IDs are ever shown.
- **Moving frames**: with the game's Edit Mode, Fennick frames show up there (scale, width, height, alpha sliders, saved per Edit Mode layout). Without it, use `/beast move`, right-click the minimap button, or the setup page: drag, resize grip, arrow keys to nudge (while the mouse is over the frame), optional grid snap, reset per frame or all. Frames lock again when combat starts. Positions are per profile, or per character if you choose.
- No sounds by default. Optional sound cues (PvP escape alert, quest step done) each have their own toggle under Settings → Sounds; all start off. TomTom stays silent.
- Credit: Edit Mode support uses **LibEditMode** by p3lim (MIT, unmodified, `Libs/LibEditMode/LICENSE.txt`) and LibStub (public domain).

### Core v1.1.0: matching your UI
- **Font face never changes** (except window titles, which use Cinzel, SIL OFL 1.1, at the same size and offset). Every other Fennick text uses a private copy of a Blizzard font object (same face and outline); only the size moves. Settings → *Text size ±N* (−4..+6) applies live to every module.
- **Scale** follows your UI scale (UIParent); Fennick's own scale only multiplies it.
- **Match**: Auto (ElvUI if loaded, else Blizzard) / Blizzard / Objective Tracker size / ElvUI / Custom. ElvUI is read only: its font size, pixel unit (E.mult) and border colours. Custom adds a *Pixel borders* switch.
- **Pixel-perfect** borders, padding, gaps and the divider line snap to whole screen pixels (768 / screen height / scale; the game's PixelUtil when present).
- **Live re-layout** after UI scale, resolution, Edit Mode layout or text-size changes; in combat it waits until combat ends.
- The SharedMedia font choice is gone (it changed the face). Bar, border and background media are unchanged.

## Rest (v1.2.1)
Rested XP and where to log out. Works with Core alone.
- Line and thin bar: rested now, the cap (raised by the Well Rested perk, which is measured, not assumed), time until full here, and per day logged out outside vs in an inn (outside earns a quarter).
- **Where to log out (friendly inns only, every ruleset):** hearthstone ready → "Hearth to *your inn* and log out (no travel)". On cooldown → time left plus the nearest friendly inn or capital. With Leveling installed, inns on your next route leg win, and it suggests rebinding there when that saves travel. The arrow (and TomTom) points there only when Rest has focus; in Auto it adds one line while you log out.
- **Cozy Sleeping Bag** reminder when you own it, it is ready, you are outside a rest area, out of combat, the buff is missing or under 15 min, and you are idle a minute or logging out. Never used for you.
- **Camp Tent** line at a campfire when rested is under 5% and Boosted Rest is not on you.
- Each login compares rested gained with the expected amount; the result appears only in `/fennick why` and debug.

## Reputation (v1.2.0)
Shows rep turn-ins you can do with what is already in your bags: city cloth donations, Timbermaw, Argent Dawn, Thorium Brotherhood, Cenarion Circle, Darkmoon Faire (only in the faire's week and zone; dates marked unconfirmed until checked in game, and after the last known week it points you to the in-game calendar). Forever factions are added once their turn-in data is confirmed. Checks your side, level, standing caps and earlier quests. Turn-ins that are not confirmed on Forever's client data are marked so. No dungeon or raid reps, auction or profession advice. Library books stay in the Leveling module, because they give XP on the route.

## Merchant's Favor (v1.2.0)
Tracks Waylaid crates, Craftsman's Writs and Shipping Labels in your bags, several at once, sorted by readiness: right-click to start → live objectives (have/need plus bag counts) → turn in at the camp/NPC. Steps finish only when the game reports the turn-in. Favor is shown when the game exposes it. Materials say "buy or gather" only.
- **Writ customers (1.2):** while you work on a Craftsman's Writ it shows the customer's name and map spot from quest data, marked *unconfirmed* until checked in game. Writs with no customer in the data say so instead of guessing. A delivered daily writ shows the time left to the realm's daily reset.

Sources for facts and coordinates (cited, no text copied): foreverchanges.pro, wow-professions.com, urgametips.com; the client datamine is the authority where they disagree.

# Fennick's Guidepost (formerly the Fennick Leveling Guide) — stand-alone leveling guides (Forever, Interface 16001)

Free add-on. Not for sale; donations only (Blizzard UI Add-On Development Policy). No RXPGuides needed.

## Install
Unzip into `Interface/AddOns/` together with **Fennick_BeastCore** (required since v4.0.0). Folder: `Fennick_Guidepost` (engine + all route data).

Routes are race-first (start zone), then shared faction routes; class steps (trainers, class quests) appear only for your class.
Routes: Tauren (Mulgore), Undead (Tirisfal), Durotar (Orc/Troll), DunMorogh (Gnome/Dwarf), Elwynn (Human), Teldrassil (Night Elf). Windshaper Skyborne uses Tauren, High Order Skyborne uses Westfall (`/fennick route Westfall`). An unknown race gets a route of its own faction, with a chat line saying so. Elwynn/Teldrassil 1-12 and 31-60 are quest-hub steps: with Questie installed they expand into concrete accept/objective/turn-in steps at runtime; without it they are hub notes.
Rulesets: `PvE` fastest (optional deathskips, faster non-HC 22-30 route, transport shortcuts), `HC` (no death routing, safe transport, contested zones avoided for gap fills), `PvP` (goes INTO contested zones as one quick trip each, exposure-weighted transport; when an enemy player hits you the arrow switches to the nearest escape - guard town, flight master, outpost or water - and a warning shows; after 3 enemy players in 2 minutes or a PvP death you get a Branch prompt to an equal-level quieter hub; `Main` returns).

Optional (install separately, not bundled): **TomTom** (waypoint arrow; otherwise a built-in arrow + coordinates is shown) and **Questie** (not required). By default the guide uses Blizzard's own quest log, quest tracking and map with our built-in route data. If you have Questie, you can turn on "Use Questie data when installed" in the Guidepost settings for localized NPC names and runtime quest-hub steps; if Questie is missing, changes or errors, the guide quietly switches back to the Blizzard default. No Questie code or data is included.

## First run
A short setup opens on your first login: welcome, route and class (detected), ruleset, professions, arrow, quest helpers (auto-accept, auto turn-in, quest chat, instant quest text), style, minimap button. Run it again any time with `/fennick setup` or Settings → Run setup.

## Use
- **The window:**
  - The header shows the add-on name, your route, class, level and XP/hour. The ruleset button sits in the corner.
  - The top line is the one thing to do next: a verb, a target and a location, e.g. "Accept Wildmane Totem from Grull Hawkwind  Mulgore (45, 78)".
  - Below it, a small orange line (hover for details) appears only when something is relevant: Hardcore danger, safe path or PvP escape.
  - Then come the next steps, short notes, a progress bar, and Back / Skip (plus Branch / Main on the PvP ruleset).
- **How steps complete:**
  - **Accept:** when you have the quest, or have already turned it in.
  - **Turn in:** when the turn-in registers.
  - **Objectives:** when the quest log shows them finished.
  - **Train / level:** when you know the spell or reach the level.

  Reaching a waypoint only completes a pure travel step. It can never complete or skip a quest step. A "go to X" followed by "accept at X" is one step.
- **Slash commands:** `/fennick` (Core-owned; `/beast` and `/fbc` work too) with:
  - `skip`, `back`, `list`, `lvl <n>` (jump to guide n), `hide`;
  - `rules PvE|PvP|HC`, `class WARRIOR`, `route Tauren|Undead|Durotar|DunMorogh|Elwynn|Teldrassil|Westfall`;
  - `branch`, `main`, `escape`, `loadout` (pick your loadout focus), `noauto`, `restore`;
  - `prof detected|none|<list>`, `config`, `toggle`, `debuglog`; Core words `setup`, `minimap`, `debug`, `why`, `help`.
- **Saving:** progress (guide, step, skips), settings and the setup-done flag are saved per character and restored after `/reload` or relog. Named profiles are shared across characters.

## Hardcore (HC ruleset)
Routes never use dying, spirit rez, corpse runs or graveyards. Travel is by road, flight path, boat/zeppelin and a pre-bound hearthstone.

## Settings (v4)
- Style, text size, sounds, SharedMedia, colour-blind colours and the minimap button are Beast Core settings (`/beast`), shared by every module.
- **Leveling settings** (`/fennick config`):
  - **Route:** ruleset, route, class.
  - **Professions:** pick yours (multi-select), "Use detected" or "None".
  - **Display:** scale, opacity, lock.
  - **Arrow:** on/off, TomTom or built-in.
  - **Hints:** trainer and profession hints, quest reward pick, loadout focus.
  - **PvP:** sensitivity.
  - **Hiding:** hide in combat or in instances.
  - **Extras:** XP/hour, named profiles (save, load, reset), debug.
- **Quest helpers** (all off by default; only quests on your route; never in combat; hold Shift to bypass):
  - Auto-accept and auto turn-in. It never chooses between reward items; the best pick for your build is printed instead.
  - Auto-select quests in NPC chat.
  - **Instant quest text** is the game's own option (Interface → Display). The button changes it only when you click it, out of combat.
- **Keybinds:** Key Bindings → "Fennick's Guidepost" (skip, back, on/off, settings, escape).
- **Skins:** Masque and LibSharedMedia are used if installed. Skin authors: see SKINNING.md. Planned features: QOL-GAP-ANALYSIS.md.
- **Interface Options:** Fennick is not added to Blizzard's Interface Options by default, because adding categories there is a known source of "blocked" errors. You can turn it on in Settings (needs `/reload`).

## Loadout focus
Choose how you fight in the setup wizard, in Settings, or with `/fennick loadout`. The list only shows loadouts your class can use, based on its weapon and armor skills in the datamine:
- two-handed melee;
- polearm/staff melee;
- dual wield (daggers, 1H, fist);
- 1H + shield (DPS or tank);
- caster (staff, 1H + off-hand, 1H + shield);
- healer (staff, 1H + off-hand, 1H + shield);
- ranged physical;
- wand caster;
- feral;
- hybrid.

Nothing is recommended. If your equipped weapons fit exactly one loadout, that one is preselected; otherwise you are asked to choose.

Your loadout only decides the quest reward pick. When a quest offers a choice, you get one line in the guide window and chat: **Reward: Pick <item>**. There are no other gear suggestions.

## Professions
The guide never recommends a profession. It uses only the professions your character has trained (detected automatically) or the ones you pick in setup or Settings: pick several, "Use detected", or "None". `/fennick prof detected|none|Mining,Skinning` does the same. Training-tier reminders, gathering-on-route tips and crafting notes appear only for those professions; with none, you see no profession content.

## If you see "An action only available to the Blizzard UI was blocked"
The guide is combat-safe: in combat it never calls TomTom or Questie (when enabled), never creates or focuses UI, and never touches Blizzard frames. Its windows use their own close buttons, not Blizzard's panel system. The built-in arrow covers combat; everything else catches up when combat ends.

If the message still appears, please capture the exact blocked function:
1. **Quickest:** type `/fennick debug` (turns logging on). Play until it happens, then type `/fennick debuglog` and copy the lines that start with `ADDON_ACTION_BLOCKED` / `ADDON_ACTION_FORBIDDEN`: they name the add-on and the function that was blocked. The log is also saved in `WTF/Account/<ACCOUNT>/SavedVariables/Fennick_Guidepost.lua` (`blocked` and `debugLog`) after you log out or `/reload`.
2. **Taint log (most detail):** type `/console taintLog 1`, reproduce the problem, then `/reload` or log out. Open `World of Warcraft/<client folder>/Logs/taint.log` and send the lines around `Blocked` / `An action was blocked`. They show which add-on's code touched the variable that caused it. Turn logging off afterwards with `/console taintLog 0` (it slows the client a little). Use `taintLog 2` only if 1 shows nothing.
3. **BugGrabber + BugSack:** install both, reproduce, click the BugSack icon, and copy the entry. It records the addon name and function for blocked actions.
4. To check whether it's us at all, reproduce once with only Fennick enabled (plus TomTom/Questie if you use them), then with Fennick disabled.

### Manual test: gamepad UI (WoW Forever)
Offline checks can't drive the native gamepad UI. With a controller and Blizzard's gamepad mode on:
1. Open and close the world map 5 times, and click a quest on the map.
2. Left- and right-click the minimap button; use Skip and Back.
3. Enter combat, then open the map.
4. Pass: no ADDON_ACTION_BLOCKED/FORBIDDEN, and `/fennick debuglog` shows no blocked lines.
