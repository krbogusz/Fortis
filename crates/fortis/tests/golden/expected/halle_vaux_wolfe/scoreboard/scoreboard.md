# Induction scoreboard — `projects/halle_vaux_wolfe`

The MDL loss `L = fit_bits + rule_bits` of the identity cascade (no rules) and the
hand cascade, on the real lexicon and on the synthetic one (the hand cascade's own
output — the learnability floor, where its residual is zero). Every later induction
milestone is assessed against these numbers.

| cascade | fit_bits | rule_bits | L (total) | exact | mean dist |
| --- | ---: | ---: | ---: | ---: | ---: |
| real · identity      |          310 |          0 |          310 |    3/13   |  0.846 |
| real · hand          |            0 |        393 |          393 |   13/13   |  0.000 |
| synthetic · identity |          310 |          0 |          310 |    3/13   |  0.846 |
| synthetic · hand     |            0 |        393 |          393 |   13/13   |  0.000 |

**Loss the hand rules buy on real data:** L(identity) − L(hand) = -83 bits.

**Learnability floor:** the hand cascade's synthetic `fit_bits` is 0 (target 0).
