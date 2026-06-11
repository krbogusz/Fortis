```
fortis/
├── pyproject.toml
├── data/                        # user-authored inventories
│   ├── features.toml  letters.csv  diacritics.toml
│   ├── sonorities.toml  syllable_parts.toml
│   └── words.toml  rules.toml
├── docs/reference.md
├── tests/
└── src/fortis/
    ├── config.py                # paths, value symbols, greek alphabet, special symbols
    ├── result.py                # Result / Ok / Err
    │
    ├── general/                 # generic helpers, zero domain knowledge
    │   ├── file_handling.py     #   load_toml_file, load_csv_file
    │   ├── presentation.py      #   present_symbol, trace formatting
    │   └── utils.py             #   safe_int, ...
    │
    ├── models/                  # INERT DATA — imports only stdlib + within models
    │   ├── values.py            #   SingleValue, ContourValue, Value, AlphaOp, ContourEdge
    │   ├── tiers.py             #   Tier
    │   ├── specs.py             #   PatternSpec, ResultSpec
    │   ├── bundles.py           #   FeatureBundle, PatternBundle, ResultBundle
    │   ├── bindings.py          #   Bindings (alpha + element-ref state)
    │   ├── elements.py          #   Element union (LetterRef, Group, Quantified, Boundary…)
    │   ├── rules.py             #   ApplicationMode, StructuralDescription, Rule
    │   ├── features.py          #   FeatureKind, Feature, FeatureInventory
    │   ├── inventories.py       #   Letter/Diacritic/Sonority/Syllable/Word defs + Inventories
    │   ├── derivation.py        #   DerivationStep, Derivation
    │   └── syllable.py          #   Syllable (placeholder for future syllable structure)
    │
    ├── parsing/                 # STRING → models       (depends on: models)
    │   ├── bundles.py           #   parse_value, parse_*_spec, parse_*_bundle
    │   └── notation.py          #   parse_definition: SPE string → StructuralDescription/Elements
    │
    ├── loaders/                 # FILE → models         (depends on: models, parsing)
    │   ├── features.py          #   features.toml      → FeatureInventory
    │   ├── letters.py           #   letters.csv        → LetterInventory
    │   ├── diacritics.py
    │   ├── sonorities.py
    │   ├── syllable_parts.py
    │   ├── words.py
    │   ├── rules.py             #   rules.toml (bodies parsed via parsing.notation)
    │   └── project.py           #   load everything    → Project
    │
    └── application/             # THE ENGINE            (depends on: models, parsing, loaders)
        ├── segmenter.py         #   IPA string → Sequence
        ├── merge.py             #   apply_bundle: combine + node-delink (shared)
        ├── matcher.py           #   locate loci where a rule's SD holds; bind alpha/refs
        ├── applier.py           #   rewrite a locus from a ResultBundle + Bindings
        ├── syllabifier.py       #   (planned) sonority-driven boundaries
        ├── renderer.py          #   Sequence → IPA string
        └── engine.py            #   DerivationEngine: derive a word → Derivation
```
