# Fonts (D-031)

All three families are licensed under the SIL Open Font License 1.1; each licence file is kept
beside the fonts, as the licence requires.

| Files | Family | Source | Licence |
|---|---|---|---|
| `inter-latin-{400,500,600}-normal.woff2`, `inter-latin-400-italic.woff2` | Inter, © 2016 The Inter Project Authors | Latin subsets from the `@fontsource/inter` 5.1.0 package | `LICENSE-inter.txt` |
| `inter-latin-ext-{400,500,600}-normal.woff2`, `inter-latin-ext-400-italic.woff2` | Inter, as above | Latin Extended subsets from the same package, loaded with the package's `unicode-range` | `LICENSE-inter.txt` |
| `jetbrains-mono-latin-{400,500}-normal.woff2` | JetBrains Mono, © 2020 The JetBrains Mono Project Authors | Latin subsets from the `@fontsource/jetbrains-mono` 5.1.0 package | `LICENSE-jetbrains-mono.txt` |
| `IBMPlexMono-Regular-Pi.woff2` (arrows) | IBM Plex Mono, © 2017 IBM Corp., Reserved Font Name "Plex" | IBM's own file, unmodified, from the `@ibm/plex-mono` 2.5.0 package (`fonts/split/woff2/`) | `LICENSE-ibm-plex-mono.txt` (IBM's `LICENSE.txt`, verbatim) |

IBM Plex Mono is used as IBM distributes it: the file is not subset or converted here, because the
Reserved Font Name may only be used by unmodified versions. It supplies only the arrows (← → ↔),
which the Inter subsets lack.
