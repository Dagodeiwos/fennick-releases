# Template: add-on CHANGELOG

Every add-on CHANGELOG follows this structure. The same file is used in both repositories.

Writing rules:
- Newest version first. One heading per version: `## <version> (<Month> <Year>)`. Never a day.
- Under each version, one bullet per change a player or developer would notice, written in plain words.
- No personal names, no internal process, no bot or reviewer names, no branch names, no internal ticket codes.
- Versions released before this add-on had its own changelog sit under `## Earlier versions`, one `### <version>` each.
- The first line under each version may say what it needs, for example "Needs Fennick's Beast Core 1.6."

---

```markdown
# Fennick's <Name>: changelog

All notable changes, newest first. Dates are month and year only.

## <x.y.z> (<Month> <Year>)
- <Change.>

## Earlier versions

### <x.y.z>
- <Change.>
```
