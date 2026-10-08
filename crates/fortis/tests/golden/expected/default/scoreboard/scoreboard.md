# Induction scoreboard — `projects/default`

The MDL loss `L = fit_bits + rule_bits` of the identity cascade (no rules) and the
hand cascade, on the real lexicon and on the synthetic one (the hand cascade's own
output — the learnability floor, where its residual is zero). Every later induction
milestone is assessed against these numbers.

| cascade | fit_bits | rule_bits | L (total) | exact | mean dist |
| --- | ---: | ---: | ---: | ---: | ---: |
| real · identity      |          505 |          0 |          505 |    4/21   |  1.095 |
| real · hand          |            0 |      1,320 |        1,320 |   21/21   |  0.000 |
| synthetic · identity |          537 |          0 |          537 |    4/25   |  1.080 |
| synthetic · hand     |            0 |      1,320 |        1,320 |   25/25   |  0.000 |

**Loss the hand rules buy on real data:** L(identity) − L(hand) = -816 bits.

**Learnability floor:** the hand cascade's synthetic `fit_bits` is 0 (target 0).
