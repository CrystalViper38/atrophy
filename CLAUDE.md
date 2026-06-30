# CLAUDE.md — `atrophy`

Local, private macOS tool: reads your own Claude Code transcripts (aggregates only) and
mirrors **judgment vs autopilot** when coding with AI agents. Read-only, stdlib-only, zero
network. Full context: `README.md` + `atrophy.py` header ("REASON FOR BEING").

## Commands
```bash
python3 atrophy.py            # on-demand report (terminal render, no upload)
python3 atrophy.py --llm      # with local LLM scoring (--llm-model <path.gguf> to override)
python3 -m pytest             # tests: test_atrophy.py, test_atrophy_llm.py  (CI runs this)
./install.sh / ./uninstall.sh # launchd nightly report
```

## The one rule that governs every change
**MIRROR, NOT JUDGE — and never let the metric become a target (Goodhart).** The whole point
is *seeing* yourself, not scoring yourself. The moment the tool nudges the user to push a number,
it makes them *perform* engagement instead of creating it — the mirror lies. So:
- No leaderboards, no streaks, no guilt framing, no "improve your score" affordances.
- Silent + capacity framing (celebrate what's held, don't induce guilt) is a design constraint, not a style choice.
- Re-read `atrophy.py`'s REASON-FOR-BEING block before any feature that touches scoring or display.

## Constraints
- **Aggregates only, never raw transcript content.** Privacy is the product. No network, ever.
- **stdlib-only core** (the `--llm` path is the only optional dep). Don't add deps to the reader.

## Priority
This is a tool *about* not over-relying on tools. The `~/code/CLAUDE.md` freeze rule applies
hard here: don't "optimize" atrophy unless a real need is blocked — that's the exact behavior it exists to catch.
