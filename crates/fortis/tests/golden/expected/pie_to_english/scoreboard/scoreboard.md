# Induction scoreboard — `projects/pie_to_english`

The MDL loss `L = fit_bits + rule_bits` of the identity cascade (no rules) and the
hand cascade, on the real lexicon and on the synthetic one (the hand cascade's own
output — the learnability floor, where its residual is zero). Every later induction
milestone is assessed against these numbers.

| cascade | fit_bits | rule_bits | L (total) | exact | mean dist |
| --- | ---: | ---: | ---: | ---: | ---: |
| real · identity      | 9,280,663,794 |          0 | 9,280,663,794 |    0/343  |  4.863 |
| real · hand          |   72,840,717 |     30,231 |   72,870,948 |  314/343  |  0.195 |
| synthetic · identity | 9,469,828,427 |          0 | 9,469,828,427 |    0/737  |  5.065 |
| synthetic · hand     |            0 |     30,231 |       30,231 |  737/737  |  0.000 |

**Loss the hand rules buy on real data:** L(identity) − L(hand) = 9,207,792,846 bits.

**Learnability floor:** the hand cascade's synthetic `fit_bits` is 0 (target 0).
