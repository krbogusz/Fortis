# Tonal showcase

A small tonal language that exercises the autosegmental tier operations on real derivations —
the phenomena the curated PIE→Germanic sample (which uses *stress*) doesn't show. Run it:

```
python -m src.fortis.main examples/tonal
```

It reuses the shipped feature system, letters, and tone diacritics (high tone is a combining
acute, `a` + `◌́`), with its own `words.toml` and `rules.toml`. Two derivations:

- **`táka` — high-tone spread.** `High-tone spread` (left-to-right) carries the high off the
  first vowel onto the following toneless one — *one* autosegment, two anchors, not a copy:
  `ta˦.ka → ta˦.ka˦`.
- **`katá` — tonal stability.** `Final vowel loss` deletes the word-final vowel, and the high
  it bore survives on the preceding syllable instead of vanishing: `ka.ta˦ → ka˦t`.

This directory does not touch the canonical `inventories/`, so `python -m src.fortis.main`
(no argument) is unchanged. See `docs/change_notation_rules.md` §1.8/§2.12 and the project
README's "Autosegmental tiers" section for the notation.
