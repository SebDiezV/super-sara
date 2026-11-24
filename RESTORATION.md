# Super Sara Restoration

This is a reconstruction starting point, not a recovered copy of the deleted game.
The original source and assets come from https://github.com/maurogeorge/segredario.
Original attribution and asset license notes remain in README.md.

## Run Locally

Double-click start-game.cmd, then open http://127.0.0.1:4000.
Python 3 must be installed. Close the server with Ctrl+C.

The local server automatically exports level.tmx and finale.tmx when the game
requests their JSON and the TMX or a TSX is newer. Save in Tiled, then refresh
the game to load the updated map. New tilesets/layer names still need registration
in Phaser. Restart the server once after changing serve.py itself.

## Restored So Far

- Original playable Phaser game, levels, finale, audio, and credits.
- Browser title and text header: Super Sara.
- Burgundy header background: rgba(86, 7, 34, 0.75).
- Local-only Python server with caching disabled.
- Removed original external analytics script.

## Reconstruction References From Our Conversation

- Final main-level NPCs: mario, yoshi, toad, dk, diddy, link.
- Luigi, fox, and pikachu were removed from runtime NPC lists.
- Sprite sheets have two horizontal frames. Frame dimensions:
  mario 21x26, yoshi 20x26, toad 20x25, dk 30x27,
  diddy 30x26, link 22x34; finale mauro 25x27.
- Last designs: mario was a tan dog, dk a black-and-white cat,
  toad a white dog, yoshi a brown-haired girl in a pink sweater,
  diddy a blue-haired girl in a yellow raincoat,
  link a brown-haired person in a dark jacket.
- Custom player, finale character, title logo, and heart-pattern page background
  need to be recreated from surviving references.
- Main map had backgroundLayer, bgLayer3, bgLayer2,
  backgroundElementsLayer, blockedLayer, and objectsLayer.
- Tilesets included super_mario_bros, sky, mountains, bg stars,
  and pixilart-drawing (1). Custom tile data is missing.
- Music and dialogue were customized; their final exact contents are unknown.
- Previous customized commits were fc344b4 and 24b8e41; these IDs alone
  do not contain the deleted files.

## Recovered From VS Code Local History

On November 24, 2026, actual saved edits were found in VS Code User/History.
All 18 saved versions across six resources were copied to the sibling folder
recovered-vscode-history, including the original entries.json metadata.

- game.js: NPC dialogue restored from -5d747ca4/VxXn.js, including the
  six-character roster. Other game logic still uses the upstream version.
- finale.js: mauroText restored from 9f662bf/ObbA.js.
- credits.js: entire file restored byte-for-byte from -7e0306da/BdHJ.js.
- Historical HTML, CSS, and full JavaScript versions remain in the recovery folder.
- The recovered credits also identify three music tracks, though audio is not recovered.

The earlier notes above describe what was known before this discovery. The dialogue
and credits are now recovered text, not a reconstruction from memory.

## Confirmed Music Mapping

Confirmed by Sevas on November 24, 2026. Audio files still need restoring;
the current game uses the upstream music.

| Scene | Track | Artist | Local asset |
| --- | --- | --- | --- |
| Main level, walking to the castle | Futile Devices | Sufjan Stevens | assets/audios/bmgs/level.mp3 |
| Castle finale and proposal | Comptine d'un autre ete | Yann Tiersen | assets/audios/bmgs/finale.mp3 |
| Credits | Married Life | Michael Giacchino | assets/audios/bmgs/credits.mp3 |

The short level-complete transition track has not been identified.

Futile Devices was restored from the supplied piano-cover MP3 on November 24,
2026 into assets/audios/bmgs/level.mp3. Its SHA-256 matches the supplied file.
The main level already loops the level audio and stops it at the castle transition.

The supplied Comptine dun autre ete, lapres-midi MP3 was restored on November 24,
2026 into assets/audios/bmgs/finale.mp3. Its SHA-256 matches the supplied file.
The finale loops this track during the castle/proposal scene and stops it before credits.

Married Life was restored from the supplied MP3 on November 24, 2026 into
assets/audios/bmgs/credits.mp3. Its SHA-256 matches the supplied file.
All three selected music tracks are now restored. At the user's request,
the Mario-style level-complete cue was removed from loading and playback;
entering the castle now starts the finale immediately instead of waiting seven seconds.

The Super Sara logo was recreated with image generation on November 24, 2026,
using the old screenshot as a descriptive reference. assets/images/logo.png is
a new approximation with pale pink lettering, a heart, and a burgundy backdrop;
it is displayed at 200x100 in the header and loading screen.

## Recovered Piskel Sprites

Edge's Default profile retained Piskel IndexedDB files. These were copied without
changing the browser's source data into ../recovered-piskel-edge.
Sixteen complete project snapshots were extracted from 000013.ldb, plus one
large imported dog reference from the external blob file. Every extracted project
and PNG is retained, including alternate versions.

Restored sprite PNGs from recovered-piskel-edge/snapshots:

- player.png: 004-player-layer0-chunk0.png (504x25, eighteen 28x25 frames).
- mauro.png: 008-mauro-layer0-chunk0.png (200x27, eight 25x27 frames).
- mario.png: 015-mario-layer0-chunk0.png (Lady).
- toad.png: 011-toad-layer0-chunk0.png (Snoopy).
- yoshi.png: 012-yoshi-layer0-chunk0.png (Mabel).
- diddy.png: 014-diddy-layer0-chunk0.png (Coraline).

Snapshot numbers indicate extraction order, not verified edit dates.
DK/Damian and Link/Edward have not been recovered from this Piskel data.

Edward's source image was subsequently supplied again as
Gemini_Generated_Image_1jlqaf1jlqaf1jlq.png. A preserved copy is at
../recovered-piskel-edge/edward-source.png. restore-edward.ps1 extracts the
two poses, removes blue backdrop pixels, and fits them proportionally into
22x34 frames in assets/sprites/link.png. This sheet is newly converted from
the supplied design, rather than a recovered copy of the old sheet.

Damian's Gemini source was also supplied again as
Gemini_Generated_Image_drq7ekdrq7ekdrq7.png, preserved at
../recovered-piskel-edge/damian-source.png. restore-damian.ps1 removes the
border-connected checkerboard and proportionally fits both poses into 30x27
frames in assets/sprites/dk.png. All character slots now have custom artwork,
with Edward and Damian newly converted from their supplied references.

## Download History Leads

Game-related Edge download records were exported to
../recovered-piskel-edge/game-download-sources.json.
These are source-page records, not recovered asset files.

- Most later Gemini sprite references were downloaded from
  https://gemini.google.com/app/0ecbb6e0270a0434
  (including the confirmed Mabel source 8doagd8doagd8doa).
  Which images are Damian and Edward still needs visual confirmation.
- Night Tileset 16x16: https://pixel-by-pixel.itch.io/night-tileset-16x16
- pixilart-drawing (1).png: https://gamer247.itch.io/lua
- Futile Devices download title: Sufjan Stevens - Futile Devices (piano cover)
  Call Me By Your Name. Exact performer/recording not yet confirmed.
- Two Comptine recordings and a Married Life download are recorded, but their
  deleted audio files were not found locally.
