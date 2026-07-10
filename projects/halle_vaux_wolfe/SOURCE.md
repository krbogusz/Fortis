# Source

Feature geometry and phenomena after:

Morris Halle, Bert Vaux & Andrew Wolfe (2000), "On Feature Spreading and the
Representation of Place of Articulation." *Linguistic Inquiry* 31(3): 387–444.

`features.toml` encodes their structure (1): the root's dependents ([consonantal],
[sonorant], [suction], [continuant], [strident], [lateral]), the Place node over the oral
articulators (Lips, Tongue Blade, Tongue Body), the Soft Palate (velic) node, and the
Guttural node over Tongue Root and Larynx. The designated-articulator features ([labial],
[coronal], [dorsal], [rhinal], [radical], [glottal]) are privative (`unary`); the gradient
properties are `binary`.

## Showcase rules (each word-scoped in rules.toml)

- **Nasal place assimilation** (ex. 44) — the *whole* Place node spreads (labial/coronal/
  dorsal at once): `anka -> aŋka`, `anpa -> ampa`.
- **Irish dorsal assimilation** (ex. 63–67), the paper's flagship — a coronal nasal takes
  the following consonant's **[dorsal]** (and the height realizing it) but keeps its **own
  [back]**: palatalized `anʲga -> aŋʲga`, velarized `anˠgʲa -> aŋgʲa`. Only terminal features
  spread, and [back] is not among them — contrast the whole-node case above.
- **Uyghur Raising** (ex. 12) — [+low] -> [+high] in a medial open syllable: `kalalar -> kalilar`.
- **Sibe uvularization** (ex. 50–52) — a dorsal consonant goes uvular ([−high]) when preceded
  anywhere by a [−high] vowel, [+high] vowels transparent: `dʒalukun -> dʒaluqun`, `bɔduxu ->
  bɔduχu`, `ulukun` unchanged.
- **Palestinian Arabic emphasis spread** (ex. 48) — [RTR] spreads leftward across consonants,
  vowels transparent: `tatatˤ -> tˤatˤatˤ`.
- **Igbo labial assimilation** (ex. 32–33) — a high prefix vowel rounds before a labial:
  `obibe -> obube`, `ofife -> ofufe`, `olile` unchanged.

The lexicons are minimal illustrations built to exercise each mechanism, not full paradigms
from the paper; the letter inventory covers only the segments these words need. Assimilations
formalized with `~n` (place, Irish dorsal) render in the Autosegmental view; the feature-changing
rules (raising, uvularization, emphasis, rounding) show as plain changes in the derivation trace.
