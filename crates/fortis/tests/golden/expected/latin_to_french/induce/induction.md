# Induction — `projects/latin_to_french`

Each interval's rule cascade, induced by greedy MDL boosting from the attested source
forms toward the attested targets. A rule is accepted only when it strictly lowers the
description length `L = fit_bits + rule_bits` — the bits it saves in the residual must
exceed the bits it costs to write. `ΔL` is that change (negative = a net saving), split
into its fit and rule-cost parts. `place` is where the rule was inserted in the
cascade (`append`, or `@i` when the placement search found an earlier slot fed a later
rule).

## Interval `input→300`

**1 → 245 / 304 exact** (81%), fit **1444423014 → 46895659** bits, **32 rules** induced — stopped: _converged_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `m → ∅ / _ #` | -671310537 | -671310563 | 26 | 208 | 1→6 | append |
| 2 | `u → o` | -125995406 | -125995437 | 31 | 113 | 6→26 | append |
| 3 | `e → ɛ` | -100739078 | -100739108 | 31 | 154 | 26→50 | append |
| 4 | `[back, -consonantal, +continuant, glottal, glottal_aperture: neutral, larynx_height: neutral, length: long, lingual, manner, oral, +sonorant, +syllabic, tension: neutral, +voice] → [length: short]` | -164530193 | -164530296 | 103 | 121 | 50→93 | append |
| 5 | `i → e` | -36809904 | -36809934 | 31 | 95 | 93→112 | append |
| 6 | `e → ʝ / _ [+syllabic]` | -80685036 | -80685076 | 40 | 16 | 112→117 | @0 |
| 7 | `e → ʝ / _ [+syllabic]` | -40843706 | -40843745 | 40 | 42 | 117→131 | append |
| 8 | `[advancement: atr, -consonantal, +continuant, front, glottal, glottal_aperture: neutral, larynx_height: neutral, length: long, lingual, manner, oral, +sonorant, +syllabic, tension: neutral, +voice] → [length: short]` | -29442780 | -29442889 | 109 | 45 | 131→152 | append |
| 9 | `w → β / _ [+syllabic]` | -24484137 | -24484176 | 40 | 23 | 152→163 | @0 |
| 10 | `k → x / _ [anterior]` | -21790186 | -21790225 | 40 | 19 | 163→169 | append |
| 11 | `l → ɫ / _ [-continuant]` | -6855520 | -6855560 | 40 | 10 | 169→175 | append |
| 12 | `ˈo → ˈɔ / [labial] _ [trill]` | -5361323 | -5361372 | 48 | 7 | 175→181 | @0 |
| 13 | `b → β / ˌɑ _` | -4560642 | -4560683 | 41 | 4 | 181→183 | append |
| 14 | `ˈo → ˈɔ / [labial] _ [-sonorant]` | -4018837 | -4018885 | 48 | 3 | 183→186 | @6 |
| 15 | `ˈo → ˈɔ / _ [aperture: high]` | -2617621 | -2617660 | 40 | 5 | 186→187 | @0 |
| 16 | `k → c / _ [front]` | -2277095 | -2277135 | 40 | 18 | 187→200 | append |
| 17 | `g → ɣ / [-consonantal] _` | -10252816 | -10252855 | 40 | 19 | 200→206 | append |
| 18 | `ˌo → ˌɔ / [labial] _` | -1156652 | -1156692 | 40 | 6 | 206→211 | @0 |
| 19 | `x → ŋ / [+consonantal] _` | -2782021 | -2782060 | 40 | 6 | 211→211 | append |
| 20 | `t̪ → t͡sʲ / _ ʝ` | -6135535 | -6135576 | 41 | 5 | 211→216 | append |
| 21 | `b → β / [advancement: atr] _` | -809122 | -809162 | 40 | 8 | 216→222 | append |
| 22 | `ɣ → ʝ / [aperture: low] _ [front]` | -26276809 | -26276858 | 48 | 5 | 222→224 | append |
| 23 | `ˈo → ˈɔ / _ [lateral]` | -463046 | -463085 | 40 | 3 | 224→226 | @0 |
| 24 | `o → ∅ / _ l` | -1946656 | -1946690 | 34 | 15 | 226→229 | append |
| 25 | `o → ɔ / ʝ _` | -22283240 | -22283281 | 41 | 7 | 229→229 | @12 |
| 26 | `n̪ → ∅ / _ ŋ` | -439038 | -439071 | 34 | 6 | 229→235 | append |
| 27 | `n̪ → ŋ / _ g` | -408566 | -408607 | 41 | 5 | 235→237 | @0 |
| 28 | `ˈo → ˈɔ / [-voice] _ [trill]` | -994817 | -994866 | 48 | 3 | 237→238 | @0 |
| 29 | `g → ɟ / [+consonantal] _ [aperture: mid]` | -74569 | -74618 | 48 | 4 | 238→240 | append |
| 30 | `n̪ → ∅ / [back] _ [strident]` | -806628 | -806669 | 41 | 2 | 240→242 | append |
| 31 | `d̪ → ɟ / [+consonantal] _ [+consonantal]` | -236025 | -236073 | 48 | 2 | 242→243 | append |
| 32 | `j → ʝ` | -138416 | -138447 | 31 | 2 | 243→245 | append |

## Interval `300→1000`

**0 → 21 / 304 exact** (7%), fit **1869530551 → 522579873** bits, **53 rules** induced — stopped: _max_rules_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `ɑ → ə` | -177726205 | -177726236 | 31 | 190 | 0→4 | append |
| 2 | `ˈə → ˈeː` | -65420098 | -65420129 | 31 | 122 | 4→5 | append |
| 3 | `ˈo → ˈu / _ [+sonorant]` | -24543415 | -24543455 | 40 | 35 | 5→8 | @0 |
| 4 | `ˈeː → ˈa / _ [+continuant]` | -174020647 | -174020687 | 40 | 30 | 8→10 | append |
| 5 | `l → ∅ / [aperture: high] _` | -9790199 | -9790231 | 32 | 16 | 10→9 | append |
| 6 | `ˈu → ˈy / [-continuant] _` | -80437761 | -80437800 | 40 | 15 | 9→10 | @0 |
| 7 | `ˌə → ˌa` | -55489688 | -55489719 | 31 | 35 | 10→10 | append |
| 8 | `β → v` | -22655395 | -22655426 | 31 | 30 | 10→11 | append |
| 9 | `t̪ → ð / [advancement: atr] _` | -12512949 | -12512988 | 40 | 28 | 11→13 | append |
| 10 | `ˈeː → ˈa / _ [-continuant]` | -10090089 | -10090129 | 40 | 76 | 13→15 | append |
| 11 | `ˈa → ˈeː / _ [trill]` | -2147229 | -2147269 | 40 | 45 | 15→14 | append |
| 12 | `ˈa → ˈã / _ [nasal]` | -25971491 | -25971531 | 40 | 20 | 14→14 | append |
| 13 | `ˈu → ˈo / [-voice] _ [trill]` | -732798 | -732847 | 48 | 3 | 14→14 | append |
| 14 | `k → ∅ / [advancement: atr] _` | -623788 | -623820 | 32 | 9 | 14→15 | append |
| 15 | `x → j` | -59994582 | -59994612 | 31 | 10 | 15→16 | append |
| 16 | `k → t͡ʃ / # _ [aperture: low]` | -38466268 | -38466310 | 43 | 12 | 16→16 | @0 |
| 17 | `ˈɛ → ˈi / _ [dental]` | -28754962 | -28755002 | 40 | 13 | 16→16 | append |
| 18 | `ɛ → r` | -15355386 | -15355416 | 31 | 136 | 16→14 | append |
| 19 | `r → e̯ / [-sonorant] _` | -10903610 | -10903650 | 40 | 89 | 14→13 | append |
| 20 | `r → ə / e̯ _` | -10091834 | -10091875 | 41 | 29 | 13→13 | append |
| 21 | `e̯ → r / [glottal_aperture: neutral] _ [+syllabic]` | -48574116 | -48574164 | 48 | 43 | 13→16 | append |
| 22 | `e̯ → ∅ / _ #` | -8110784 | -8110811 | 26 | 26 | 16→21 | append |
| 23 | `c → t͡s` | -4211121 | -4211151 | 31 | 19 | 21→22 | append |
| 24 | `ˌu → ˌy` | -111745505 | -111745536 | 31 | 9 | 22→23 | append |
| 25 | `r → e̯ / [length: long] _` | -2467545 | -2467585 | 40 | 45 | 23→23 | append |
| 26 | `r → ∅ / [+syllabic] _ #` | -172122 | -172158 | 35 | 13 | 23→26 | append |
| 27 | `ˈeː → ˈi / [-voice] _ [+sonorant]` | -2379038 | -2379087 | 48 | 13 | 26→28 | append |
| 28 | `e̯ → ∅ / [aperture: mid] _` | -607367 | -607399 | 32 | 32 | 28→34 | append |
| 29 | `e̯ → ∅ / _ [lateral]` | -462226 | -462258 | 32 | 7 | 34→34 | append |
| 30 | `ˈeː → e̯ / [aperture: high] _` | -1111596 | -1111635 | 40 | 8 | 34→34 | append |
| 31 | `∅ → j / _ s` | -41384468 | -41384502 | 34 | 79 | 34→28 | append |
| 32 | `j → ∅ / # _` | -4689648 | -4689674 | 26 | 22 | 28→29 | append |
| 33 | `j → ∅ / ˌe _ [+continuant]` | -93649 | -93691 | 43 | 7 | 29→31 | append |
| 34 | `j → ∅ / [back] _ [+continuant]` | -2756951 | -2756992 | 41 | 28 | 31→31 | append |
| 35 | `j → ∅ / [-syllabic] _` | -1228186 | -1228218 | 32 | 15 | 31→33 | append |
| 36 | `∅ → j / ˈe _` | -10537786 | -10537820 | 34 | 28 | 33→34 | @0 |
| 37 | `j → ∅ / _ k` | -143697 | -143731 | 34 | 4 | 34→34 | append |
| 38 | `j → ∅ / ˈa _ [strident]` | -260396 | -260438 | 43 | 4 | 34→34 | append |
| 39 | `ð → ∅ / _ [-sonorant]` | -5868351 | -5868383 | 32 | 3 | 34→36 | append |
| 40 | `ʝ → ʎ` | -5014323 | -5014354 | 31 | 62 | 36→37 | append |
| 41 | `ʎ → ∅ / [advancement: rtr] _` | -16913075 | -16913107 | 32 | 7 | 37→37 | append |
| 42 | `j → ∅ / _ [lateral]` | -6477954 | -6477986 | 32 | 2 | 37→38 | @20 |
| 43 | `ʎ → ∅ / [-sonorant] _` | -1861200 | -1861232 | 32 | 16 | 38→38 | append |
| 44 | `ˈu → ˈo / [aperture: high] _ [trill]` | -2718571 | -2718620 | 48 | 3 | 38→38 | append |
| 45 | `k → ∅ / [advancement: atr] _` | -3035656 | -3035688 | 32 | 8 | 38→38 | append |
| 46 | `∅ → j / ˈa _` | -96229587 | -96229621 | 34 | 41 | 38→35 | append |
| 47 | `j → ∅ / _ [lateral]` | -1806455 | -1806487 | 32 | 14 | 35→37 | append |
| 48 | `j → ∅ / ˈa _ [strident]` | -582636 | -582679 | 43 | 9 | 37→37 | append |
| 49 | `j → ∅ / _ [aperture: high]` | -6502186 | -6502218 | 32 | 15 | 37→37 | append |
| 50 | `∅ → j / ˌa _` | -7177300 | -7177334 | 34 | 35 | 37→34 | append |
| 51 | `j → ∅ / ˌa _ [+voice]` | -7979790 | -7979833 | 43 | 32 | 34→37 | append |
| 52 | `ˈɔ → ˈy / _ [-sonorant]` | -28426724 | -28426763 | 40 | 6 | 37→37 | append |
| 53 | `∅ → ˈi / _ r` | -46256395 | -46256429 | 34 | 142 | 37→18 | append |
| 54 | `ˈi → ∅ / [aperture: mid] _` | -4630533 | -4630565 | 32 | 47 | 18→28 | append |
| 55 | `r → ∅ / [aperture: high] _ ˈi` | -4614221 | -4614264 | 43 | 16 | 28→28 | append |
| 56 | `ˈi → ∅ / _ ˈi` | -4714854 | -4714888 | 34 | 17 | 28→28 | append |
| 57 | `l → ∅ / _ [anterior]` | -1457799 | -1457831 | 32 | 14 | 28→28 | append |
| 58 | `n̪ → ∅ / ˈi _` | -1439759 | -1439793 | 34 | 16 | 28→27 | append |
| 59 | `v → ∅ / [back] _` | -47522 | -47554 | 32 | 3 | 27→27 | append |
| 60 | `ˈu → ˈo / _ [+continuant]` | -4213234 | -4213274 | 40 | 7 | 27→28 | append |

**Shrink pass** removed 7 now-redundant rule(s):

- removed `j → ∅ / [back] _ [+continuant]` (L 544897831 → 532085166)
- removed `ˈa → ˈã / _ [nasal]` (L 532085166 → 528054398)
- removed `r → ∅ / [aperture: high] _ ˈi` (L 528054398 → 526613564)
- removed `r → e̯ / [length: long] _` (L 526613564 → 525599003)
- removed `ˈi → ∅ / _ ˈi` (L 525599003 → 522581838)
- removed `j → ∅ / _ [lateral]` (L 522581838 → 522581806)
- removed `e̯ → ∅ / [aperture: mid] _` (L 522581806 → 522581774)

## Interval `1000→1200`

**52 → 213 / 303 exact** (70%), fit **700467720 → 71312704** bits, **42 rules** induced — stopped: _converged_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `ˈi → j / _ [advancement: atr]` | -52112167 | -52112207 | 40 | 35 | 52→52 | append |
| 2 | `j → ˈɛ / [+syllabic] _` | -166337469 | -166337509 | 40 | 44 | 52→50 | append |
| 3 | `ˈeː → ˈe` | -30288947 | -30288978 | 31 | 38 | 50→62 | append |
| 4 | `e̯ → ˈe` | -18305037 | -18305068 | 31 | 43 | 62→70 | append |
| 5 | `[+consonantal, front, glottal, glottal_aperture: neutral, larynx_height: neutral, length: short, lingual, manner, oral, -sonorant, strident, -syllabic, tension: neutral] → [+continuant]` | -21652698 | -21652795 | 97 | 53 | 70→92 | append |
| 6 | `ɫ → w` | -21167074 | -21167104 | 31 | 24 | 92→98 | append |
| 7 | `ˈu → ˈũ` | -12421106 | -12421136 | 31 | 27 | 98→107 | append |
| 8 | `ˈe → w / _ [+syllabic]` | -62335867 | -62335907 | 40 | 11 | 107→115 | append |
| 9 | `ˈo → ˈu` | -17088402 | -17088432 | 31 | 25 | 115→125 | append |
| 10 | `w → ˈø / [advancement: atr] _` | -39886553 | -39886593 | 40 | 19 | 125→125 | append |
| 11 | `ˈa → ∅ / _ [+syllabic]` | -20327373 | -20327405 | 32 | 11 | 125→131 | append |
| 12 | `ˈã → ˈɛ̃ / _ [+continuant]` | -3861075 | -3861115 | 40 | 9 | 131→138 | append |
| 13 | `ˈu → ∅ / _ [advancement: atr]` | -3613808 | -3613840 | 32 | 10 | 138→139 | append |
| 14 | `m → n̪ / _ [-sonorant]` | -15465827 | -15465867 | 40 | 8 | 139→144 | append |
| 15 | `ˈɛ → ˌɛ / [+syllabic] _` | -2633261 | -2633301 | 40 | 23 | 144→144 | append |
| 16 | `ˈy → ∅ / _ [advancement: atr]` | -2160490 | -2160522 | 32 | 8 | 144→144 | @0 |
| 17 | `ˌa → ∅ / _ [advancement: rtr]` | -1976607 | -1976639 | 32 | 7 | 144→149 | append |
| 18 | `ˈɛ̃ → ˈã / _ [-continuant]` | -3899329 | -3899368 | 40 | 7 | 149→154 | append |
| 19 | `ˈe → ˈẽ / _ [nasal]` | -16164952 | -16164992 | 40 | 7 | 154→158 | append |
| 20 | `ˈe → ˈø / [labial] _ [-voice]` | -6154278 | -6154327 | 48 | 4 | 158→161 | append |
| 21 | `ˌu → ˌũ` | -1580222 | -1580253 | 31 | 9 | 161→167 | append |
| 22 | `ˌo → ˌu` | -1318791 | -1318822 | 31 | 10 | 167→173 | append |
| 23 | `∅ → e̯ / b _ ˈɛ` | -1302612 | -1302656 | 44 | 2 | 173→173 | append |
| 24 | `ˈi → ˈĩ / _ [nasal]` | -1129546 | -1129585 | 40 | 8 | 173→179 | append |
| 25 | `z → ∅ / _ [+consonantal]` | -298237 | -298269 | 32 | 5 | 179→180 | append |
| 26 | `ˌe → w / _ [+syllabic]` | -8459421 | -8459460 | 40 | 5 | 180→184 | append |
| 27 | `w → ∅ / [back] _` | -599332 | -599364 | 32 | 5 | 184→184 | append |
| 28 | `ˈy → ɥ / _ [advancement: rtr]` | -3467893 | -3467933 | 40 | 3 | 184→184 | append |
| 29 | `ˈẽ → ˈã / [-sonorant] _` | -3794205 | -3794245 | 40 | 5 | 184→188 | @0 |
| 30 | `j̃ → ˈĩ / [aperture: high] _` | -2853789 | -2853828 | 40 | 5 | 188→188 | append |
| 31 | `ˈø → ∅ / [rounded] _` | -101326 | -101358 | 32 | 3 | 188→191 | @15 |
| 32 | `ˌy → ˌỹ` | -69952618 | -69952649 | 31 | 9 | 191→192 | append |
| 33 | `ˈũ → w / _ [+syllabic]` | -3503243 | -3503282 | 40 | 3 | 192→195 | append |
| 34 | `ˈe → ∅ / [aperture: high] _ [+syllabic]` | -1299472 | -1299513 | 41 | 2 | 195→197 | append |
| 35 | `ˌɛ → ˈi / ɥ _` | -2530027 | -2530068 | 41 | 3 | 197→200 | append |
| 36 | `ˈɛ → ˈa / _ [aperture: high]` | -204960 | -205000 | 40 | 3 | 200→201 | append |
| 37 | `s → ˈɛː / _ [+consonantal]` | -7928977 | -7929016 | 40 | 10 | 201→201 | @0 |
| 38 | `ˈũ → ˈu / _ [-sonorant]` | -161482 | -161521 | 40 | 3 | 201→204 | append |
| 39 | `ˌẽ → ˌã` | -97227 | -97257 | 31 | 6 | 204→207 | append |
| 40 | `ˌi → ˌĩ / _ [nasal]` | -43646 | -43686 | 40 | 3 | 207→209 | append |
| 41 | `ˌã → ˌɛ̃ / _ [+continuant]` | -499846 | -499885 | 40 | 3 | 209→211 | append |
| 42 | `ˈø → ˈu / [labial] _ [+voice]` | -174212 | -174260 | 48 | 2 | 211→213 | append |

## Interval `1200→1500`

**159 → 206 / 300 exact** (69%), fit **623688063 → 134702162** bits, **27 rules** induced — stopped: _converged_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `n̪ → ˈãː / [nasal] _` | -147223387 | -147223426 | 40 | 75 | 159→153 | append |
| 2 | `ˈãː → ˈũː / [aperture: high] _ #` | -58413086 | -58413128 | 43 | 15 | 153→153 | append |
| 3 | `ˈãː → n̪ / _ [+sonorant]` | -166501970 | -166502009 | 40 | 15 | 153→159 | append |
| 4 | `w → ˈoː / [+syllabic] _` | -14436946 | -14436986 | 40 | 12 | 159→159 | append |
| 5 | `ˈã → ∅ / _ [+continuant]` | -4069221 | -4069253 | 32 | 15 | 159→173 | append |
| 6 | `ˈɛ̃ → ∅ / [labial] _` | -524117 | -524149 | 32 | 5 | 173→173 | append |
| 7 | `j → ∅ / ʒ _` | -261583 | -261617 | 34 | 3 | 173→175 | append |
| 8 | `j → ∅ / [aperture: high] _` | -21770 | -21802 | 32 | 4 | 175→177 | append |
| 9 | `j → ∅ / [aperture: low] _` | -18506 | -18539 | 32 | 3 | 177→177 | append |
| 10 | `ˈãː → ˈũː / [rounded] _` | -25460977 | -25461016 | 40 | 12 | 177→177 | append |
| 11 | `ˈãː → ˈẽː / [advancement: atr] _` | -24171171 | -24171210 | 40 | 8 | 177→177 | append |
| 12 | `ˈẽ → ∅ / _ [+continuant]` | -6077376 | -6077408 | 32 | 4 | 177→181 | append |
| 13 | `ə → ˈɛː / [+syllabic] _` | -11072145 | -11072185 | 40 | 15 | 181→181 | append |
| 14 | `ˈũː → ˈɛ̃ː / [+consonantal] _` | -6708481 | -6708521 | 40 | 4 | 181→181 | append |
| 15 | `ˌã → ∅ / _ [+continuant]` | -455317 | -455349 | 32 | 6 | 181→181 | append |
| 16 | `ˈe → ∅ / _ [+syllabic]` | -232643 | -232676 | 32 | 4 | 181→181 | append |
| 17 | `w → ∅ / [trill] _` | -14973 | -15005 | 32 | 4 | 181→183 | append |
| 18 | `ˈɛː → ˈeː / _ #` | -2633793 | -2633827 | 34 | 15 | 183→186 | append |
| 19 | `ˈeː → ˈɛː / [advancement: rtr] _` | -195951 | -195990 | 40 | 6 | 186→186 | append |
| 20 | `ˈãː → ˈɛ̃ː / j̃ _` | -260472 | -260513 | 41 | 6 | 186→186 | append |
| 21 | `ɲ → ˈɛ̃ː / _ #` | -5258870 | -5258904 | 34 | 5 | 186→186 | @0 |
| 22 | `ˈĩ → ˈi` | -316247 | -316277 | 31 | 12 | 186→189 | append |
| 23 | `ˈi → ∅ / _ [+syllabic]` | -2060921 | -2060953 | 32 | 11 | 189→192 | append |
| 24 | `ˌa → ∅ / _ [+syllabic]` | -232446 | -232479 | 32 | 4 | 192→193 | append |
| 25 | `ˌũ → ∅ / [labial] _` | -51906 | -51938 | 32 | 3 | 193→193 | append |
| 26 | `ˈũː → ˌũː / [+consonantal] _` | -51898 | -51938 | 40 | 6 | 193→195 | append |
| 27 | `ˌə → ə̯` | -3229488 | -3229519 | 31 | 10 | 195→193 | append |
| 28 | `ˈa → ∅ / _ [+syllabic]` | -1751369 | -1751401 | 32 | 12 | 193→200 | append |
| 29 | `e̯ → ə̯` | -1208236 | -1208267 | 31 | 6 | 200→203 | append |
| 30 | `ə̯ → ˌə / _ [+consonantal]` | -824158 | -824197 | 40 | 6 | 203→207 | append |
| 31 | `ˈeː → ˈiː` | -2895283 | -2895314 | 31 | 9 | 207→206 | append |
| 32 | `ˌũː → ˈẽː` | -2017971 | -2018002 | 31 | 6 | 206→206 | append |

**Shrink pass** removed 5 now-redundant rule(s):

- removed `ˌũ → ∅ / [labial] _` (L 135035384 → 134703249)
- removed `ˈãː → ˈũː / [aperture: high] _ #` (L 134703249 → 134703207)
- removed `ˈũː → ˈɛ̃ː / [+consonantal] _` (L 134703207 → 134703167)
- removed `ˈũː → ˌũː / [+consonantal] _` (L 134703167 → 134703128)
- removed `ˌũː → ˈẽː` (L 134703128 → 134703097)

## Interval `1500→final`

**0 → 0 / 300 exact** (0%), fit **1154751006 → 441692716** bits, **9 rules** induced — stopped: _converged_.

| # | rule | ΔL | Δfit | cost | words | exact | place |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | `r → ʁ` | -325241873 | -325241904 | 31 | 133 | 0→0 | append |
| 2 | `ə → ∅ / _ #` | -41245568 | -41245595 | 26 | 95 | 0→0 | append |
| 3 | `ˈũː → ɔ̃` | -6470873 | -6470903 | 31 | 15 | 0→0 | append |
| 4 | `ʎ → j` | -3359311 | -3359342 | 31 | 13 | 0→0 | append |
| 5 | `ˈẽː → ɛ̃` | -19631454 | -19631485 | 31 | 10 | 0→0 | append |
| 6 | `[advancement: rtr, aperture: mid, -consonantal, +continuant, front, glottal, glottal_aperture: neutral, larynx_height: neutral, length: long, lingual, manner, oral, +sonorant, +syllabic, tension: neutral, +voice] → [length: short]` | -2249736 | -2249851 | 115 | 27 | 0→0 | append |
| 7 | `t̪ → ∅ / _ #` | -301555109 | -301555135 | 26 | 31 | 0→0 | @0 |
| 8 | `ˈãː → ɑ̃` | -7727892 | -7727923 | 31 | 16 | 0→0 | append |
| 9 | `ˈoː → o` | -5576122 | -5576153 | 31 | 13 | 0→0 | append |
