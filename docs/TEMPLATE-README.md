# Template: add-on README

Every add-on README follows this structure, in this order. Copy the skeleton below, keep every heading, and write
"None." under a heading that does not apply. The same file is used in both repositories.

Writing rules:
- I write in the first person ("I"). No personal names, no internal process, no bot or reviewer names, no email addresses.
- Dates are month and year only (for example "October 2026"), never a day.
- Plain words first. Where a Lua idiom or a WoW concept appears, explain it in one short sentence for a reader who
  knows C++ but is new to Lua and the WoW API.
- Support always points to https://github.com/Dagodeiwos/fennick-releases/issues.

---

```markdown
# Fennick's <Name>

<One or two sentences: what the add-on does and who it is for.>

| | |
|---|---|
| Version | <x.y.z, the same as `## Version` in the .toc> |
| Game | WoW Forever (Interface <number>) |
| Requires | <add-on folders, or "Nothing"> |
| Works with (optional) | <add-ons, or "None"> |
| License | PolyForm Noncommercial 1.0.0 (`LICENSE.md`) |

## What it does
<Short bullet list of features, as a player sees them.>

## Install
<Where the folder goes and what else must be installed.>

## Use
<Commands and the main clicks. One bullet each.>

## Settings
<Where the settings live and what the main ones do.>

## Compatibility
<Other add-ons it works with or avoids, and what happens without them.>

## How it works (for developers)
<A few bullets on the design, the files, and the WoW or Lua concepts a newcomer needs.>

## Support
Bug reports and questions: https://github.com/Dagodeiwos/fennick-releases/issues

## License
PolyForm Noncommercial 1.0.0. See `LICENSE.md` in this folder.
```
