# Sound sources

The marsh sound on the home page (off until a visitor turns it on) is built only from public-domain recordings:
the loop from the U.S. National Park Service (works made by federal employees as part of their job are in the
public domain in the United States, and the NPS pages below say so), and the rare fox call from Wikimedia Commons.
I list each source so anyone can check.

| File it went into | Title | Author | Source | License |
|---|---|---|---|---|
| `assets/audio/marsh-loop.*` | Crickets | NPS | https://www.nps.gov/subjects/sound/sounds-crickets.htm (file: https://www.nps.gov/nps-audiovideo/legacy/mp3/nri/avElement/nri-Cricket.mp3) | Public domain ("The files are in the public domain and may be downloaded", https://www.nps.gov/subjects/sound/gallery.htm) |
| `assets/audio/marsh-loop.*` | Green Tree Frog (Everglades NP) | NPS / Theresa Thom | https://www.nps.gov/subjects/sound/sounds-green-treefrog.htm (file: .../nri-GreenTreeFrogEvergladesNP.mp3) | Public domain (same gallery statement) |
| `assets/audio/marsh-loop.*` | Pig Frog (Everglades NP) | NPS | https://www.nps.gov/subjects/sound/sounds-pigfrog.htm (file: .../nri-PigFrogEvergladesNP.mp3) | Public domain (same gallery statement) |
| `assets/audio/fox-call.*` | Fennec Singing (fennec fox, *Vulpes zerda*, "singing" in the morning) | Eosin-Y (English Wikipedia user), uploaded 2007-10-02 | https://commons.wikimedia.org/wiki/File:Fennec_Singing.ogg (file: https://upload.wikimedia.org/wikipedia/commons/5/5f/Fennec_Singing.ogg) | Public domain, {{PD-user-en\|Eosin-Y}}: released into the public domain by its author, worldwide |

Credits: National Park Service (as the NPS asks). Fennec fox recording by Eosin-Y, public domain, via Wikimedia Commons.

## How I made the files

- `marsh-loop`: the crickets as the bed, with the tree frog and the pig frog mixed in quietly, cut to 24 seconds.
  The last 3 seconds are crossfaded into the first 3 so the loop has no seam. Mono, Opus 40 kbps in Ogg
  (`.ogg`) plus an MP3 64 kbps fallback.
- `fox-call`: 1.8 seconds cut from the fennec recording (12.5 to 14.3 s), 200 Hz high-pass, short fades, loudness
  evened out to about -20 LUFS. Peak -6.6 dBFS, no clipping. Opus in Ogg plus an MP3 fallback. It plays once every
  2 to 5 minutes at 0.6 times the loop's volume, only while the sound is on.
