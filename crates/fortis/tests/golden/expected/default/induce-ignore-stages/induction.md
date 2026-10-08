# Induction — `projects/default`

Each interval's rule cascade, induced by greedy MDL boosting from the attested source
forms toward the attested targets. A rule is accepted only when it strictly lowers the
description length `L = fit_bits + rule_bits` — the bits it saves in the residual must
exceed the bits it costs to write. `ΔL` is that change (negative = a net saving), split
into its fit and rule-cost parts. `place` is where the rule was inserted in the
cascade (`append`, or `@i` when the placement search found an earlier slot fed a later
rule).

## Interval `input→final`

**4 → 4 / 21 exact** (19%), fit **462 → 408** bits, **1 rules** induced — stopped: _converged_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `i → u / [-voice] _ [+voice]` | -6 | -54 | 48 | 2 | 4→4 | append |
