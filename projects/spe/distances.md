# Distances — `projects/spe`

Engine output vs. attested forms. `d` is the phone edit distance (exact = 0);
`fd` is the feature edit distance (features that differ, so a near-miss scores
far below a gross one). Both drop syllable dots and count an adjacent-segment
swap as one edit.

> **Reading the stage rows.** Each intermediate stage is graded by matching the engine's *rule-time* to the target's *stage-time* — the derived snapshot after all rules dated ≤ T, against the attested form at stage T. If those two timescales are not calibrated (e.g. rule times assigned for ordering, target periods from another scheme), the intermediate rows read low for an alignment reason, not a phonological one — only the `final` row is independent of that alignment. Where a word carries both a last-stage form and `final`, those two rows measure the same thing.

## Summary

| stage | graded | exact | ≤1 phone | mean phone | mean feature |
| --- | ---: | ---: | ---: | ---: | ---: |
| final | 6 | 6 | 6 | 0.000 | 0.000 |

## final

All 6 graded words exact.
