# Induction — `projects/spe`

Each interval's rule cascade, induced by greedy MDL boosting from the attested source
forms toward the attested targets. A rule is accepted only when it strictly lowers the
description length `L = fit_bits + rule_bits` — the bits it saves in the residual must
exceed the bits it costs to write. `ΔL` is that change (negative = a net saving), split
into its fit and rule-cost parts. `place` is where the rule was inserted in the
cascade (`append`, or `@i` when the placement search found an earlier slot fed a later
rule).

## Interval `input→final`

**0 → 0 / 6 exact** (0%), fit **72 → 72** bits, **0 rules** induced — stopped: _converged_.

No rule lowered the loss — nothing induced.
