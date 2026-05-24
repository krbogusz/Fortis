# Features

## Feature types

```
- unary (e.g., [oral])
- binary (e.g., [±sonorant])
- scalar (e.g., [position] – [-1: palatal, 0: postalveolar, 1: advanced])
```

## Segmental Features

```
ROOT
- [±consonantal]
- [±syllabic]
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
        - [coronal] → [anterior], [posterior], [apical], [retroflex]
        - [guttural]
        - [aperture] → [high], [low]
        - [advancement] → [RTR], [ATR]
- [glottal]
    - [±voice]
    - [aperture] – [-1: constricted, 0: neutral, 1: spread]
    - [tension] – [-1: slack, 0: neutral, 1: stiff]
    - [larynx height] – [-1: lowered; 0: neutral; 1: raised]
```

## Coronals

|             | [anterior]      | [posterior]          | [high]  |
| ----------- | --------------- | -------------------- | ------- |
| _unmarked_  | lamino-alveolar | palato-alveolar      | palatal |
| [apical]    | apico-alveolar  | apico-postalveolar   | -       |
| [retroflex] | -               | sub-apical retroflex | -       |

## Vowels & Consonants

(unrounded • rounded)

|            |       | [coronal] | _unmarked_ | [guttural] |
| ---------- | ----- | --------- | ---------- | ---------- |
| [high]     | [ATR] | i • y     | ɨ • ʉ      | ɯ • u      |
| [high]     | [RTR] | ɪ • ʏ     | -          | - • ʊ      |
| _unmarked_ | [ATR] | e • ø     | ɘ • ɵ      | ɤ • o      |
| _unmarked_ | -     |           | ə          |            |
| _unmarked_ | [RTR] | ɛ • œ     | ɜ • ɞ      | ʌ • ɔ      |
| [low]      | [ATR] | æ • -     | ɐ          | -          |
| [low]      | [RTR] | -         | a • ɶ      | ɑ • ɒ      |

Consonants are not marked for advancement

|                   | [coronal] | _unmarked_ | [guttural] |
| ----------------- | --------- | ---------- | ---------- |
| [high]            | i, j, c   | -          | u, w, k    |
| _unmarked_, [RTR] | -         | -          | ʌ, ʁ, q    |
| [low], [RTR]      | -         | -          | ɑ, ʕ, ʡ    |

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
