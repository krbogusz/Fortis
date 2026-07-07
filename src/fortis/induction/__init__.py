"""Supervised rule induction: recover a rule cascade from attested targets.

Given a ``words.toml`` of proto inputs and attested targets (``final`` and, ideally,
intermediate ``stages``), induce the sound-change cascade that derives the targets — the
ancestor-given sub-problem of reconstruction. This is the topmost consumer layer: it treats
the engine as a fixed black box and sits atop the ``analysis`` tools, reusing ``accuracy``,
``diagnosis``, ``blame``, and the parallel derivation drivers rather than being used by them.

The modules:

- :mod:`objective` — the two-part MDL bits objective (fit bits + rule bits) that prices a
  candidate rule against the corrections it makes unnecessary.
- :mod:`intervals` — stage bucketing into per-interval mini-projects (teacher forcing) and
  the synthetic-lexicon generator that machine-generates a clean, self-consistent benchmark.
- :mod:`evaluate` — the append-scoring fast path (score a candidate by applying one rule to
  each word's cached derivation, no full re-derivation).
- :mod:`correspond` — residual correspondences read from the derived side, with phi-ranked
  conditioning environments.
- :mod:`notation` — render feature material back to Fortis notation (round-trip-tested).
- :mod:`candidates` — the proposal lattice (literal, contextual, and natural-class rules),
  parse-validated through ``load_rule``.
- :mod:`boost` — the greedy MDL boosting loop per interval, with the shrink pass and the
  escape ladder.
- :mod:`scoreboard` — the reference scores (identity vs hand cascade, real and synthetic).
"""
