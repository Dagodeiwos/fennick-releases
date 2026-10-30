# Fennick add-ons

Free World of Warcraft add-ons for WoW Forever (Interface 16001). Beast Core is the shared base; every other add-on is a
module you can add or leave out. They are not for sale. License: PolyForm Noncommercial 1.0.0 (`LICENSE.md` in every
add-on folder).

- Website: https://fennickaddons.dev
- Downloads: https://github.com/Dagodeiwos/fennick-releases/releases
- Bug reports and questions: https://github.com/Dagodeiwos/fennick-releases/issues
- Version history: `CHANGELOG.md`, and one `CHANGELOG.md` per add-on

## The add-ons

| Folder | What it does | Requires |
|---|---|---|
| `Fennick_BeastCore` | Focus window, waypoint arrow, look, setup, settings, monster tooltip | Nothing |
| `Fennick_Guidepost` | Leveling guide 1 to 60 with PvE, Hardcore and PvP rulesets | Beast Core |
| `Fennick_Rest` | Rested XP and where to log out | Beast Core |
| `Fennick_Reputation` | Reputation turn-ins you can do with what is in your bags | Beast Core |
| `Fennick_MerchantsFavor` | Merchant's Favor crates, labels and writs | Beast Core |
| `Fennick_Trailmarks` | Records where you find nodes, chests and quest targets | Beast Core |
| `Fennick_Cartographer` | World map and minimap with routes, trips and pins | Beast Core |
| `Fennick_FoxTrials` | In-game checklist for playtesters (separate download) | Beast Core |

Each folder has its own `README.md` with what the add-on does, how to use it, and a short section for developers.

## Install
Download the install-all bundle (or single add-ons) from the releases page and unzip the folders into
`World of Warcraft/_forever_/Interface/AddOns/`. Install Beast Core plus only the modules you want. A module that needs a
newer Beast Core says so in one chat line and stays off.

## Principles
These are the rules every Fennick add-on follows:
1. One window and one thing to do next. Other modules add one short line each.
2. No build or spec recommendations, and profession content only for professions you have or picked.
3. Gear advice is the quest reward pick and nothing else.
4. No sounds unless you switch them on, and nothing can be imported. Copy boxes only copy out.
5. Nothing changes Blizzard's protected UI during combat.
6. No IDs or internal codes are ever shown to the player.

## Languages
German, French, Spanish, Italian, Portuguese (BR), Russian, Korean and Chinese (Simplified and Traditional) are machine
translations that people have not reviewed yet. The game says so in setup and Settings, and any missing text falls back
to English. To help with a translation, open an issue at https://github.com/Dagodeiwos/fennick-releases/issues.

## For developers
- The source includes `API.md` (the Beast Core API that modules use) and `SKINNING.md` (how to restyle Fennick frames).
- The add-ons are plain Lua 5.1, the language WoW embeds. If you come from C++: tables are the only data structure (they
  serve as arrays, maps and objects), `obj:Method()` passes `obj` as the first argument (`self`), and `local` limits a
  name to its block, while anything else is global and shared with every add-on.
- Docs follow `docs/TEMPLATE-README.md` and `docs/TEMPLATE-CHANGELOG.md`.

## License
PolyForm Noncommercial 1.0.0. See `LICENSE.md`.
