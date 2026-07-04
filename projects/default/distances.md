# Distances — the shipped `projects/default`

Engine output vs. attested forms. `d` is the phone edit distance (exact = 0);
`fd` is the feature edit distance (features that differ, so a near-miss scores
far below a gross one). Both drop syllable dots and count an adjacent-segment
swap as one edit.

> **Reading the stage rows.** Each intermediate stage is graded by matching the engine's _rule-time_ to the target's _stage-time_ — the derived snapshot after all rules dated ≤ T, against the attested form at stage T. If those two timescales are not calibrated (e.g. rule times assigned for ordering, target periods from another scheme), the intermediate rows read low for an alignment reason, not a phonological one — only the `final` row is independent of that alignment. Where a word carries both a last-stage form and `final`, those two rows measure the same thing.

## Summary

| stage | graded | exact | ≤1 phone | mean phone | mean feature |
| ----- | -----: | ----: | -------: | ---------: | -----------: |
| 100   |      1 |     1 |        1 |      0.000 |        0.000 |
| 200   |      1 |     1 |        1 |      0.000 |        0.000 |
| 300   |      1 |     1 |        1 |      0.000 |        0.000 |
| final |     17 |    17 |       17 |      0.000 |        0.000 |

## 100

All 1 graded words exact.

## 200

All 1 graded words exact.

## 300

All 1 graded words exact.

## final

All 17 graded words exact.
