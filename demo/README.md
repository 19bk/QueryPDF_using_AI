# Demo Assets

Programmatically-generated demo GIFs for the project README.

## Files

| File | Purpose |
|---|---|
| `quickstart.tape` | VHS script for the terminal quick-start GIF |
| `quickstart.gif` | Generated output (committed when regenerated) |

## Regenerate the GIF

The terminal demo is built with [VHS by Charm](https://github.com/charmbracelet/vhs) — a tool that turns a text script into a recorded terminal GIF.

```bash
# Install VHS (one time)
brew install charmbracelet/tap/vhs

# From the repo root
vhs demo/quickstart.tape
```

The command runs the tape in a sandbox shell, records the session, and writes `demo/quickstart.gif`. Commit the new GIF alongside any tape changes.

## Why a tape, not a screen recorder

- Reproducible. The same script renders identically on any machine with VHS installed.
- Editable. Tweak typing speed, theme, or window size by changing one line.
- Reviewable. The tape diff shows exactly what changed between recordings.
- No screen-recording manual labour.

## Theme and dimensions

Current settings:

- Theme: `Dracula`
- Window: 1200 x 520
- Font: 16 px
- Typing speed: 50 ms per character

Pick a different theme from the [VHS theme list](https://github.com/charmbracelet/vhs#themes) — for example `Catppuccin Mocha`, `Tokyo Night`, or `Solarized Dark`.

## Adding new demos

Drop another `.tape` file in this folder. Name it after the flow it captures (e.g. `upload-and-ask.tape`). Reference the generated GIF from the main README so visitors see it on first scroll.
