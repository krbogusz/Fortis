# SPE showcase — a flat, geometry-free feature system

This project exists to demonstrate that the Fortis engine does **not** require a feature
geometry. The shipped `projects/default` uses a full autosegmental feature tree (a `root`
node over `oral`/`glottal`/`manner` class nodes, place under `lingual`, etc.). This project
throws all of that away and uses the classic **SPE** (Chomsky & Halle, *The Sound Pattern of
English*, 1968) distinctive-feature matrix instead: a flat list of binary ± features with no
parent/child structure.

## How "no feature tree" works here

`features.toml` declares fifteen binary features and **no `children`**. The feature loader
parents every unparented segmental feature to a single synthesised `root` node, so the
geometry is a depth-1 tree — i.e. no tree at all. A segment is just an unstructured set of ±
values, exactly the SPE conception.

Because everything hangs directly off `root`, the letter loader's "a feature implies its
parent" geometry check is vacuous, and rules can set any feature without touching a node
above it.

## What it demonstrates

Each of the six words in `words.toml` is scoped to one rule in `rules.toml`, all graded 100%
exact against their `final` forms:

- **Intervocalic voicing** (`ata → ada`) and **final devoicing** (`tad → tat`) — natural
  classes (`[-sonorant]`) and word-edge conditioning on a flat matrix.
- **Nasal place assimilation** (`anpa → ampa`, `anka → aŋka`) — the centrepiece. With no
  place node to spread, place assimilation is done by agreeing the flat tongue-blade and
  tongue-body features `[α coronal, β anterior, γ high, δ back]` between the nasal and the
  following consonant. One rule with four α-variables covers labial *and* velar.
- **Backness & rounding harmony** (`uti → utu`) and **metaphony** (`beti → biti`) — SPE's
  signature economy: vowels are described with the *same* tongue-body features `[high, low,
  back, round]` as consonants, so ordinary feature rules handle vowel harmony and raising.

The project is fully self-contained: it supplies its own `features.toml`, `letters.csv`,
`sonorities.toml`, `syllable_parts.toml`, a minimal `diacritics.toml`, and an empty
`tiers.toml` (no suprasegmentals), because the shipped defaults for those reference features
that this flat system does not define. `words.toml` and `rules.toml` are its own.
