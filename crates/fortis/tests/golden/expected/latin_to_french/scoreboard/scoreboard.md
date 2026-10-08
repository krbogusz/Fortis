# Induction scoreboard — `projects/latin_to_french`

The MDL loss `L = fit_bits + rule_bits` of the identity cascade (no rules) and the
hand cascade, on the real lexicon and on the synthetic one (the hand cascade's own
output — the learnability floor, where its residual is zero). Every later induction
milestone is assessed against these numbers.

| cascade | fit_bits | rule_bits | L (total) | exact | mean dist |
| --- | ---: | ---: | ---: | ---: | ---: |
| real · identity      | 10,586,736,456 |          0 | 10,586,736,456 |    0/304  |  5.283 |
| real · hand          |  559,740,393 |     24,994 |  559,765,387 |  271/304  |  0.164 |
| synthetic · identity | 10,618,552,351 |          0 | 10,618,552,351 |    0/304  |  5.299 |
| synthetic · hand     |            0 |     24,994 |       24,994 |  304/304  |  0.000 |

**Loss the hand rules buy on real data:** L(identity) − L(hand) = 10,026,971,069 bits.

**Learnability floor:** the hand cascade's synthetic `fit_bits` is 0 (target 0).
