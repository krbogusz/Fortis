Derivation-model features

- Optional / sporadic / probabilistic rules. Lexurgy and others let a rule fire only sometimes — a fixed probability, or on a random % of the lexicon — to model lexical diffusion and dialectal variation. Fortis has word-scoped rules (a
  deterministic lexical restriction), but not a stochastic "applies 30% of the time" mode. This matters for realistic diachrony and for the induction work's "systematic coincidence" risk.
- Multiple / branching outputs. Brassica can produce several candidate outputs from one input when a change is nondeterministic (an "or" that doesn't collapse). Fortis is strictly single-valued. Supporting a result set would model uncertain
  or split outcomes.
- Iterate-to-fixpoint application. Fortis deliberately applies each rule in exactly one pass (documented in deriving.py). Peers offer a "propagate/repeat until stable" mode, natural for iterative harmony, cluster reduction, or stress-shift
  chains. This would be an opt-in application mode alongside your simultaneous/left-to-right/right-to-left.
- Persistent rules. Rules that re-apply after every subsequent rule (Lexurgy's "persistent"). Fortis's untimed rules apply once after all timed ones — a persistent mode is stronger.

Diachronic-specific

- Multiple-daughter / tree derivation. The big one: one proto-lexicon → many daughters via a shared early cascade that branches into divergent later cascades (a phylogenetic tree). This is core comparative-method machinery and directly
  serves the reconstruction sketch (projects/romance/). Fortis currently derives one lineage at a time.
- Reverse / backward application. Applying rules in reverse to hypothesize earlier forms — Brassica does a constrained version. Squarely relevant to the reconstruction goal (abduction), and a natural companion to your rule induction.
- Relative-chronology diagnostics. Automatic feeding/bleeding/counterbleeding detection and visualization. Your blame already localizes errors by the culprit rule and its time; a dedicated ordering-interaction report would extend this.
- Cognate correspondence tooling + multiple-sequence alignment. The reconstruction sketch names this explicitly — MSA over ≥3 daughters and conditioned correspondence sets. Your error-context phi-autopsy is already a conditioned-correspondence
  engine that could be re-pointed daughter-to-daughter.

Ergonomics / notation

- Named categories/classes (C, V, or user-defined natural-class abbreviations). Fortis's feature bundles are more principled but verbose; named classes are a big usability win and would also shrink induced-rule notation.
- Romanization / orthography layers. A separate spelling↔phonology mapping (Lexurgy's romanizers/deromanizers), so inputs and outputs can be in orthography while rules operate on phonemes.
- Sound-change diff / highlighting. Show exactly which segment each rule changed, inline in output. Your DerivationStep trace has the data; this is a presentation layer.
- Intermediate-stage output at named checkpoints. You already snapshot via form_at_time for the accuracy analysis; exposing labeled stage outputs as first-class user output (not just measured internally) mirrors Lexurgy's stages.

Alternative paradigms (larger)

- Constraint-based / OT derivation. A GEN+EVAL+ranked-constraints mode as an alternative to ordered rewrite rules — a whole second engine, but some phonologists want it, and your autosegmental representation would feed it well.
- Analogical / morphological change. Paradigm leveling and morphological analogy — genuinely hard, outside pure sound change, but it's the systematic gap that makes real cognate data noisy (a limit the induction plan already acknowledges).

Analysis / corpus tooling

- Phonotactic / inventory learning from a lexicon (extract the phoneme inventory and syllable templates automatically).
- Functional load, minimal-pair generation, phoneme-frequency stats — standard phonological-corpus utilities that would complement your accuracy/errors analysis layer.

If I had to rank by leverage for Fortis specifically: (1) multiple-daughter/tree derivation + reverse application and (2) named categories/classes are the highest-value and most aligned with your reconstruction+induction direction; (3)
optional/sporadic rules and (4) iterate-to-fixpoint are cheap, well-scoped additions to the existing rule model; OT is the biggest lift and the least aligned with the rule-based core.
