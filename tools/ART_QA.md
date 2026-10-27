# Art accuracy checklist (fennickaddons.dev images)

Run this every time the images are rebuilt:
1. `python3 tools/build_assets.py`. This build **fails** if any map placement is wrong. Every icon and route in the Trailmarks and Cartographer scenes is checked against the land/water mask the generator draws from:
   - Ore, herbs (except water herbs such as Stranglekelp), chests, quest targets, quest givers, flight masters, towers and your pins must sit on land, including an 8 px ring around each one.
   - Water herbs must sit on water.
   - Piers must be on a coast, with land and water both within 14 px.
   - Ship routes must join two piers, and the middle of the route must be all water.
   - A ship must sit on water, either on a ship route or at a pier.
   - Zeppelin routes must join two towers.
   - A zeppelin must be at a tower, or in the air on a tower-to-tower route (over land or sea).
   - Flight routes must join two flight masters, and every point of the route must be on land.
   - The placements are saved to `tools/scene_placements.json`.
2. `python3 tools/build_site.py`, then `python3 tools/art_qa.py`. This checks:
   - Every image in `tools/art_claims.json` exists at its stated size.
   - The versions on every page match the suite.
   - Every mockup figure has a Mockup caption.
   - No donation link is outside a comment.
3. A by-eye review of every final image, against the list below:
   - [ ] **Terrain:** every icon is on terrain where it can exist (no ore or herbs in water, no ships on land, zeppelins only at towers or in the air).
   - [ ] **Routes:** they are possible. Ships run pier to pier over water, zeppelins run tower to tower, and flight routes run between flight masters over land.
   - [ ] **Faction:** one consistent faction context (here: Horde), with no mixed-faction content.
   - [ ] **UI:** only UI that the add-on's README, CHANGELOG or docs describe (cite the source in art_claims.json).
   - [ ] **Labels and data:** they are plausible and sourced. Example data is marked "example"; unconfirmed data is marked "unconfirmed".
   - [ ] **Versions:** none shown in images, or they match the suite.
   - [ ] **Mockup marking:** a MOCKUP stamp plus a "Mockup: … / Not an in-game screenshot" bar, and the stamp covers no key content.
   - [ ] **Originality:** no Blizzard, Warcraft or RestedXP art, fonts or map tiles. Map scenes are labelled "Example terrain (original art, not a game map)".
   - [ ] **Readability:** text is legible at the size shown on the site (desktop and mobile).
