# Fennick add-ons: changelog

Suite-wide changes, newest first. Dates are month and year only. Each add-on folder has its own `CHANGELOG.md` with the
full detail for that add-on.

## October 2026: OpenMap support (Cartographer 1.2.0, Trailmarks 1.1.2)
- Optional compatibility with OpenMap, a seamless world map add-on (MIT, not bundled). With OpenMap installed, the map key opens OpenMap, and Cartographer and Trailmarks draw pins, routes and the planned trip on its view through its public API. No OpenMap code or art is included. Without OpenMap nothing changes.

## October 2026: WoW Forever 1.60.1 (Core 1.6.1, Guidepost 4.5.4, Cartographer 1.1.1, Trailmarks 1.1.1)
- The game now hides your facing from add-ons during encounters. Rotating-minimap pins and the arrow's pointer hide until the encounter ends, with no error.
- Cartographer's square minimap finds Blizzard's header buttons while playing instead of from a fixed list.
- Creature IDs with scrambled server fields are read correctly; only the NPC ID is used.
- The game's shorter nameplate range is documented. The interface number stays 16001.

## October 2026: suite polish (Core 1.6.0, Guidepost 4.5.3, Rest 1.2.4, Reputation 1.2.3, Merchant's Favor 1.2.3, Trailmarks 1.1.0, Cartographer 1.1.0, Fox Trials 1.6.0)
- One map tooltip for every Fennick pin, `/fennick report` for bug reports, an optional tester mode, grouped settings with "More settings", and `/fennick <module> help` for every module.
- The shared pin art now lives once in Beast Core, which makes the install about 600 KB smaller.
- Bug reports go to GitHub issues.

## October 2026: Fennick's Cartographer 1.0 (new, optional)
- A detailed world map and minimap with travel routes, trip planning, icon filters and saved pins. Beast Core 1.5 adds the map pin broker that lets every module show pins on it.

## October 2026: Fennick's Trailmarks 1.0 (new, optional), Guidepost 4.5.1, Fox Trials 1.4.0
- Trailmarks records where you find nodes, chests, quest targets and quest givers, and shows them on your maps. Guidepost uses the finds for hunting loops.

## October 2026: Questie optional (Guidepost 4.5.0)
- Guidepost no longer needs Questie. It uses the game's own quest log and map by default; Questie data is an optional setting, off by default.

## October 2026: in-game icons (Core 1.4.1, Guidepost 4.4.2, Rest 1.2.2, Reputation 1.2.1, Merchant's Favor 1.2.1)
- Each add-on has its own icon in the window header and, where the client supports it, in the AddOns list. Cosmetic only.

## October 2026: sound cues and module summaries (Core 1.4.0, Guidepost 4.4.0, Rest 1.2.0, Reputation 1.2.0, Merchant's Favor 1.2.0, Fox Trials 1.2.0)
- Optional sound cues, each with its own switch, all off by default. One summary line per installed module in setup.
- Merchant's Favor shows writ customers and the daily reset; Reputation marks unconfirmed Darkmoon Faire dates.
- The sleeping-bag reminder became a light notification owned by Rest alone (Rest 1.2.1, Guidepost 4.4.1, Fox Trials 1.2.1).

## October 2026: Fennick's Guidepost (4.3.1)
- The Fennick Leveling Guide is now Fennick's Guidepost, in the folder `Fennick_Guidepost`. Delete any old `Fennick_LevelingGuide` folder.

## October 2026: nine languages (Core 1.3.0, Guidepost 4.3.0, Rest 1.1.0, Reputation 1.1.0, Merchant's Favor 1.1.0, Fox Trials 1.1.0)
- Machine-translated text for German, French, Spanish, Italian, Portuguese (BR), Russian, Korean and Chinese (Simplified and Traditional), labelled as such in the game. English is unchanged, and any missing text falls back to English.

## October 2026: first public versions (Core 1.2.0, Guidepost 4.2.0, Rest 1.0.1, Reputation 1.0.2, Merchant's Favor 1.0.2, Fox Trials 1.0.0)
- Beast Core became the shared base with one focus window, one arrow, one look and one setup. The leveling guide, Rest, Reputation and Merchant's Favor became modules of it, and Fox Trials was added for playtesters.
