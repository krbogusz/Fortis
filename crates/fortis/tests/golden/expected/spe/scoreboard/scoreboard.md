# Induction scoreboard — `projects/spe`

The MDL loss `L = fit_bits + rule_bits` of the identity cascade (no rules) and the
hand cascade, on the real lexicon and on the synthetic one (the hand cascade's own
output — the learnability floor, where its residual is zero). Every later induction
milestone is assessed against these numbers.

| cascade | fit_bits | rule_bits | L (total) | exact | mean dist |
| --- | ---: | ---: | ---: | ---: | ---: |
| real · identity      |           72 |          0 |           72 |    0/6    |  1.000 |
| real · hand          |            0 |        253 |          253 |    6/6    |  0.000 |
| synthetic · identity |           72 |          0 |           72 |    0/6    |  1.000 |
| synthetic · hand     |            0 |        253 |          253 |    6/6    |  0.000 |

**Loss the hand rules buy on real data:** L(identity) − L(hand) = -181 bits.

**Learnability floor:** the hand cascade's synthetic `fit_bits` is 0 (target 0).
