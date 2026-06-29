# Features

## Feature types

```
- unary (e.g., [oral])
- binary (e.g., [±sonorant])
- scalar (e.g., [larynx_height] – [-1: lowered; 0: neutral; 1: raised])
```

## Segmental Features

```
ROOT
- [±syllabic]
- [±consonantal]
- [±sonorant]
- [click]
- [length] – [1: short, 2: long, 3: overlong]
- [manner]
    - [±continuant]
    - [strident]
    - [lateral]
    - [tap]
    - [trill]
- [nasal]
- [oral]
    - [labial] → [rounded], [compressed]
    - [dental]
    - [lingual]
        - [apical]
        - [retroflex]
        - [front] → [anterior], [posterior]
        - [back]
        - [aperture] → [high], [low]
        - [advancement] → [RTR], [ATR]
- [glottal]
    - [±voice]
    - [glottal_aperture] – [-1: constricted, 0: neutral, 1: spread]
    - [tension] – [-1: slack, 0: neutral, 1: stiff]
    - [larynx_height] – [-1: lowered; 0: neutral; 1: raised]
```

## Syllabic Features

```
ROOT
- [stress] – [1: secondary, 2: primary]
- [tone] – [1: extra-low, 2: low, 3: mid, 4: high, 5: extra-high]
```

## Front/Coronals

|             | [anterior]      | [posterior]          | [high]  |
| ----------- | --------------- | -------------------- | ------- |
| _unmarked_  | lamino-alveolar | palato-alveolar      | palatal |
| [apical]    | apico-alveolar  | apico-postalveolar   | -       |
| [retroflex] | -               | sub-apical retroflex | -       |

## Vowels & Consonants

(unrounded • rounded)

|            |       | [front] | _unmarked_ | [back] |
| ---------- | ----- | ------- | ---------- | ------ |
| [high]     | [ATR] | i • y   | ɨ • ʉ      | ɯ • u  |
| [high]     | [RTR] | ɪ • ʏ   | -          | - • ʊ  |
| _unmarked_ | [ATR] | e • ø   | ɘ • ɵ      | ɤ • o  |
| _unmarked_ | -     |         | ə          |        |
| _unmarked_ | [RTR] | ɛ • œ   | ɜ • ɞ      | ʌ • ɔ  |
| [low]      | [ATR] | æ • -   | ɐ          | -      |
| [low]      | [RTR] | -       | a • ɶ      | ɑ • ɒ  |

Coronal and dorsal consonants are not marked for advancement

|                   | [front] | _unmarked_ | [back]  |
| ----------------- | ------- | ---------- | ------- |
| [high]            | i, j, c | -          | u, w, k |
| _unmarked_, [RTR] | -       | -          | ʌ, ʁ, q |
| [low], [RTR]      | -       | -          | ɑ, ʕ, ʡ |

## Laryngeal features

|                                 | [voice] | [aperture]      | [tension] | [height]    |
| ------------------------------- | ------- | --------------- | --------- | ----------- |
| /p/ plain voiceless             | -       | 0               | 0         | 0           |
| /b/ plain voiced                | +       | 0               | 0         | 0           |
| /pʰ/ voiceless aspirated        | -       | +1: spread      | 0         | 0           |
| /bʱ/ voiced aspirated/breathy   | +       | +1: spread      | -1: slack | 0           |
| /p•/ Korean "tense"             | -       | 0               | +1: stiff | 0           |
| /p'/ ejective                   | -       | -1: constricted | +1: stiff | +1: raised  |
| /ɓ/ implosive                   | +       | 0               | -1: slack | -1: lowered |
| /ʔ/ glottal stop                | -       | -1: constricted | +1: stiff | 0           |
| /h/ voiceless glottal fricative | -       | +1: spread      | 0         | 0           |
| /ɦ/ breathy glottal             | +       | +1: spread      | -1: slack | 0           |
