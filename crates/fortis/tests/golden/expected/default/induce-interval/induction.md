# Induction — `projects/default`

Each interval's rule cascade, induced by greedy MDL boosting from the attested source
forms toward the attested targets. A rule is accepted only when it strictly lowers the
description length `L = fit_bits + rule_bits` — the bits it saves in the residual must
exceed the bits it costs to write. `ΔL` is that change (negative = a net saving), split
into its fit and rule-cost parts. `place` is where the rule was inserted in the
cascade (`append`, or `@i` when the placement search found an earlier slot fed a later
rule).

## Interval `100→200`

**0 → 0 / 1 exact** (0%), fit **10 → 10** bits, **0 rules** induced — stopped: _converged_.

No rule lowered the loss — nothing induced.
