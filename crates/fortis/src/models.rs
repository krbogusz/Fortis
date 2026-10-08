//! The data model: feature values, bundles, the rule AST, the inventories, forms and derivations.
//!
//! A feature is referred to by its index in the [`FeatureInventory`] (a [`FeatId`]). The index
//! of a feature never changes once assigned, so bundles parsed early stay valid when the tiers
//! register their own features later in the load.

use std::collections::{BTreeSet, HashMap};
use std::sync::Arc;

use indexmap::IndexMap;

pub type FeatId = u16;

/// The reserved key that marks a morpheme-boundary segment. No inventory declares it, so no
/// pattern references it and it never matches phonological material.
pub const MORPHEME_BOUNDARY: FeatId = u16::MAX;

// ---- Values -----------------------------------------------------------------------------------

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash, PartialOrd, Ord)]
pub enum AlphaOp {
    Same,
    Opposite,
    Other,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct AlphaRef {
    pub var: char,
    pub op: AlphaOp,
    pub unary: bool,
}

/// `~n=value`: bind the tier autosegment (or segmental node) carrying *value* under *n*.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct AutosegBind {
    pub r: i64,
    pub value: i64,
    pub optional: bool,
}

/// `~n`: recall the autosegment or node bound under *n*.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct AutosegRecall {
    pub r: i64,
    pub optional: bool,
}

/// One value of a feature, or one level of a contour.
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub enum Limb {
    Int(i64),
    /// Unspecified (`none`).
    None,
    /// A bare feature name in a pattern: present with any value.
    Any,
    Alpha(AlphaRef),
    Bind(AutosegBind),
    Recall(AutosegRecall),
}

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub enum Value {
    One(Limb),
    Contour(Arc<[Limb]>),
}

impl Value {
    pub const NONE: Value = Value::One(Limb::None);

    pub fn int(n: i64) -> Value {
        Value::One(Limb::Int(n))
    }

    pub fn is_none(&self) -> bool {
        matches!(self, Value::One(Limb::None))
    }

    pub fn limbs(&self) -> &[Limb] {
        match self {
            Value::One(limb) => std::slice::from_ref(limb),
            Value::Contour(limbs) => limbs,
        }
    }

    pub fn single(&self) -> Option<Limb> {
        match self {
            Value::One(limb) => Some(*limb),
            Value::Contour(_) => None,
        }
    }
}

/// The opposite pole of a value: what `-α` resolves to.
pub fn opposite_pole(atom: Limb, unary: bool) -> Limb {
    if unary {
        return if atom == Limb::Int(1) { Limb::None } else { Limb::Int(1) };
    }
    match atom {
        Limb::Int(0) => Limb::Int(1),
        Limb::Int(1) => Limb::Int(0),
        other => other,
    }
}

/// Build a value, folding runs of identical adjacent limbs and collapsing a single limb.
pub fn make_value(limbs: &[Limb]) -> Value {
    let mut folded: Vec<Limb> = Vec::with_capacity(limbs.len());
    for &limb in limbs {
        if folded.last() != Some(&limb) {
            folded.push(limb);
        }
    }
    if folded.len() == 1 { Value::One(folded[0]) } else { Value::Contour(folded.into()) }
}

/// A contour of two values, each of which may itself be a contour.
pub fn form_contour(a: &Value, b: &Value) -> Value {
    let mut limbs: Vec<Limb> = a.limbs().to_vec();
    limbs.extend_from_slice(b.limbs());
    make_value(&limbs)
}

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub enum ContourEdge {
    Initial,
    Final,
    Any,
    All,
}

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub enum ContourPosition {
    Edge(ContourEdge),
    Index(i64),
    List(Vec<i64>),
}

// ---- Specs and bundles ------------------------------------------------------------------------

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct PatternSpec {
    pub feature: FeatId,
    pub value: Value,
    pub negated: bool,
    pub contour_position: ContourPosition,
    pub condition_label: Option<i64>,
}

#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct ResultSpec {
    pub feature: FeatId,
    pub value: Value,
    pub condition_label: Option<i64>,
}

/// Realized features in insertion order, one value per feature (a Python `dict`).
#[derive(Clone, Debug, Default)]
pub struct FeatureBundle {
    pub items: Vec<(FeatId, Value)>,
}

impl PartialEq for FeatureBundle {
    fn eq(&self, other: &Self) -> bool {
        self.items.len() == other.items.len()
            && self.items.iter().all(|(f, v)| other.get(*f) == Some(v))
    }
}

impl Eq for FeatureBundle {}

impl FeatureBundle {
    pub fn new() -> Self {
        Self::default()
    }

    pub fn len(&self) -> usize {
        self.items.len()
    }

    pub fn is_empty(&self) -> bool {
        self.items.is_empty()
    }

    pub fn get(&self, f: FeatId) -> Option<&Value> {
        self.items.iter().find(|(k, _)| *k == f).map(|(_, v)| v)
    }

    pub fn contains(&self, f: FeatId) -> bool {
        self.items.iter().any(|(k, _)| *k == f)
    }

    /// `bundle[f] = value`: replace in place, or append.
    pub fn set(&mut self, f: FeatId, value: Value) {
        if let Some(slot) = self.items.iter_mut().find(|(k, _)| *k == f) {
            slot.1 = value;
        } else {
            self.items.push((f, value));
        }
    }

    /// `bundle.pop(f, None)`.
    pub fn remove(&mut self, f: FeatId) {
        if let Some(i) = self.items.iter().position(|(k, _)| *k == f) {
            self.items.remove(i);
        }
    }

    pub fn keys(&self) -> impl Iterator<Item = FeatId> + '_ {
        self.items.iter().map(|(k, _)| *k)
    }

    /// The bundle's content as a canonical sorted key (a `frozenset` of its items).
    pub fn key(&self) -> BundleKey {
        let mut items = self.items.clone();
        items.sort_by_key(|(f, _)| *f);
        BundleKey(items)
    }
}

/// The content of a bundle, order-free: equal keys mean equal bundles.
#[derive(Clone, Debug, PartialEq, Eq, Hash)]
pub struct BundleKey(pub Vec<(FeatId, Value)>);

pub fn morpheme_boundary_bundle() -> FeatureBundle {
    FeatureBundle { items: vec![(MORPHEME_BOUNDARY, Value::int(1))] }
}

pub fn is_morpheme_boundary(bundle: &FeatureBundle) -> bool {
    bundle.contains(MORPHEME_BOUNDARY)
}

pub type PatternBundle = Vec<PatternSpec>;
pub type ResultBundle = Vec<ResultSpec>;

// ---- The rule AST -----------------------------------------------------------------------------

#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct Quantifier {
    pub min: usize,
    pub max: Option<usize>,
}

#[derive(Clone, Debug)]
pub enum Element {
    LetterRef(String),
    LetterBundle(FeatureBundle),
    ModifiedLetter(String, FeatureBundle),
    BundleElem(PatternBundle),
    FloatingAutoseg(PatternBundle),
    ResultElem(ResultBundle),
    Wildcard,
    SyllableBoundary,
    WordBoundary,
    MorphemeBoundary,
    Null,
    Group(Vec<Element>),
    Disjunction(Vec<Vec<Element>>),
    Negated(Box<Element>),
    Quantified(Box<Element>, Quantifier),
    Bound(i64, Box<Element>),
    RecallRef(i64),
}

#[derive(Clone, Debug, Default)]
pub struct StructuralDescription {
    pub target: Vec<Element>,
    pub result: Vec<Element>,
    pub left_context: Vec<Element>,
    pub right_context: Vec<Element>,
    pub left_exception: Vec<Element>,
    pub right_exception: Vec<Element>,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum ApplicationMode {
    Simultaneous,
    LeftToRight,
    RightToLeft,
}

impl ApplicationMode {
    pub const ALL: [(&'static str, ApplicationMode); 3] = [
        ("simultaneous", ApplicationMode::Simultaneous),
        ("left_to_right", ApplicationMode::LeftToRight),
        ("right_to_left", ApplicationMode::RightToLeft),
    ];
}

#[derive(Clone, Debug)]
pub struct Rule {
    pub id: String,
    pub time: Option<i64>,
    pub raw_definition: String,
    pub sd: StructuralDescription,
    pub application: ApplicationMode,
    pub name: Option<String>,
    pub description: Option<String>,
    pub words: Vec<String>,
    pub categories: Vec<String>,
}

/// Rules keyed by time in first-appearance order, file order within a time. `None` holds the
/// untimed rules, applied after every timed one.
#[derive(Clone, Debug, Default)]
pub struct RuleInventory {
    pub by_time: IndexMap<Option<i64>, Vec<Arc<Rule>>>,
}

/// The engine's sort key for a time: the untimed slot (`None`) last.
pub fn time_order(t: Option<i64>) -> (bool, i64) {
    (t.is_none(), t.unwrap_or(0))
}

impl RuleInventory {
    /// The times in application order (ascending, untimed last).
    pub fn sorted_times(&self) -> Vec<Option<i64>> {
        let mut times: Vec<Option<i64>> = self.by_time.keys().copied().collect();
        times.sort_by_key(|t| time_order(*t));
        times
    }

    /// Every rule in application order.
    pub fn in_order(&self) -> Vec<Arc<Rule>> {
        self.sorted_times().iter().flat_map(|t| self.by_time[t].iter().cloned()).collect()
    }

    /// Every rule in the inventory's own order (`for rules in inventory.values()`).
    pub fn in_file_order(&self) -> impl Iterator<Item = &Arc<Rule>> {
        self.by_time.values().flatten()
    }
}

// ---- Features ---------------------------------------------------------------------------------

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Tier {
    Segment,
    Syllable,
}

impl Tier {
    pub fn name(self) -> &'static str {
        match self {
            Tier::Segment => "segment",
            Tier::Syllable => "syllable",
        }
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum FeatureKind {
    Unary,
    Binary,
    Scalar,
}

impl FeatureKind {
    pub fn name(self) -> &'static str {
        match self {
            FeatureKind::Unary => "unary",
            FeatureKind::Binary => "binary",
            FeatureKind::Scalar => "scalar",
        }
    }
}

#[derive(Clone, Debug)]
pub struct Feature {
    pub name: String,
    pub tier: Tier,
    pub kind: FeatureKind,
    pub short_name: String,
    /// Integer code → label, in declaration order.
    pub values: Vec<(i64, String)>,
    pub children: Option<Vec<String>>,
    pub parent: Option<String>,
}

impl Feature {
    pub fn label_of(&self, value: i64) -> Option<&str> {
        self.values.iter().find(|(k, _)| *k == value).map(|(_, v)| v.as_str())
    }
}

/// The features in declaration order, with the lookups the parser and engine need.
#[derive(Clone, Debug, Default)]
pub struct FeatureInventory {
    features: Vec<Feature>,
    index: HashMap<String, FeatId>,
    names_by_length: Vec<FeatId>,
    short_names_by_length: Vec<String>,
    short_to_long: HashMap<String, FeatId>,
    children_ids: Vec<Vec<FeatId>>,
    parent_ids: Vec<Option<FeatId>>,
    descendants: Vec<Vec<FeatId>>,
}

impl FeatureInventory {
    /// `inventory[name] = feature`: replace in place, or append; then rebuild the lookups.
    pub fn insert(&mut self, feature: Feature) {
        match self.index.get(&feature.name) {
            Some(&id) => self.features[id as usize] = feature,
            None => {
                let id = self.features.len() as FeatId;
                self.index.insert(feature.name.clone(), id);
                self.features.push(feature);
            }
        }
        self.rebuild();
    }

    pub fn rebuild(&mut self) {
        let n = self.features.len();
        let mut order: Vec<FeatId> = (0..n as FeatId).collect();
        order.sort_by_key(|&id| std::cmp::Reverse(crate::py::char_len(&self.features[id as usize].name)));
        self.names_by_length = order;
        let mut shorts: Vec<String> = self.features.iter().map(|f| f.short_name.clone()).collect();
        shorts.sort_by_key(|s| std::cmp::Reverse(crate::py::char_len(s)));
        self.short_names_by_length = shorts;
        self.short_to_long = HashMap::new();
        for (id, f) in self.features.iter().enumerate() {
            self.short_to_long.insert(f.short_name.clone(), id as FeatId);
        }
        self.children_ids = self
            .features
            .iter()
            .map(|f| {
                f.children
                    .iter()
                    .flatten()
                    .filter_map(|c| self.index.get(c).copied())
                    .collect()
            })
            .collect();
        self.parent_ids = self
            .features
            .iter()
            .map(|f| f.parent.as_ref().and_then(|p| self.index.get(p).copied()))
            .collect();
        let mut descendants = vec![Vec::new(); n];
        for id in 0..n {
            let mut out = Vec::new();
            self.collect_descendants(id as FeatId, &mut out, 0);
            descendants[id] = out;
        }
        self.descendants = descendants;
    }

    fn collect_descendants(&self, id: FeatId, out: &mut Vec<FeatId>, depth: usize) {
        if depth > self.features.len() {
            return; // a circular chain, reported by validation
        }
        for &child in &self.children_ids[id as usize] {
            out.push(child);
            self.collect_descendants(child, out, depth + 1);
        }
    }

    pub fn len(&self) -> usize {
        self.features.len()
    }

    pub fn is_empty(&self) -> bool {
        self.features.is_empty()
    }

    pub fn id(&self, name: &str) -> Option<FeatId> {
        self.index.get(name).copied()
    }

    pub fn contains(&self, name: &str) -> bool {
        self.index.contains_key(name)
    }

    pub fn get(&self, id: FeatId) -> &Feature {
        &self.features[id as usize]
    }

    pub fn try_get(&self, id: FeatId) -> Option<&Feature> {
        self.features.get(id as usize)
    }

    pub fn get_mut(&mut self, id: FeatId) -> &mut Feature {
        &mut self.features[id as usize]
    }

    pub fn name(&self, id: FeatId) -> &str {
        if id == MORPHEME_BOUNDARY {
            return "\u{0}morpheme-boundary";
        }
        &self.features[id as usize].name
    }

    pub fn iter(&self) -> impl Iterator<Item = (FeatId, &Feature)> {
        self.features.iter().enumerate().map(|(i, f)| (i as FeatId, f))
    }

    pub fn names_by_length(&self) -> &[FeatId] {
        &self.names_by_length
    }

    pub fn short_names_by_length(&self) -> &[String] {
        &self.short_names_by_length
    }

    pub fn short_to_long(&self, short: &str) -> Option<FeatId> {
        self.short_to_long.get(short).copied()
    }

    pub fn is_segmental(&self, id: FeatId) -> bool {
        self.try_get(id).is_some_and(|f| f.tier == Tier::Segment)
    }

    pub fn is_syllable(&self, id: FeatId) -> bool {
        self.try_get(id).is_some_and(|f| f.tier == Tier::Syllable)
    }

    pub fn children(&self, id: FeatId) -> &[FeatId] {
        self.children_ids.get(id as usize).map_or(&[], |v| v.as_slice())
    }

    pub fn descendants(&self, id: FeatId) -> &[FeatId] {
        self.descendants.get(id as usize).map_or(&[], |v| v.as_slice())
    }

    pub fn parent(&self, id: FeatId) -> Option<FeatId> {
        self.parent_ids.get(id as usize).copied().flatten()
    }

    /// Ancestor nodes, nearest first.
    pub fn ancestors(&self, id: FeatId) -> Vec<FeatId> {
        let mut out = Vec::new();
        let mut current = self.parent(id);
        while let Some(p) = current {
            if out.contains(&p) {
                break;
            }
            out.push(p);
            current = self.parent(p);
        }
        out
    }

    pub fn kind(&self, id: FeatId) -> FeatureKind {
        self.get(id).kind
    }
}

// ---- Inventories ------------------------------------------------------------------------------

#[derive(Clone, Debug)]
pub struct Letter {
    pub symbol: String,
    pub bundle: Arc<FeatureBundle>,
}

/// Letters in file order, with the longest-first symbol list the segmenter needs.
#[derive(Clone, Debug, Default)]
pub struct LetterInventory {
    pub letters: Vec<Letter>,
    index: HashMap<String, usize>,
    sorted_keys: Vec<usize>,
}

impl LetterInventory {
    pub fn insert(&mut self, letter: Letter) {
        self.index.insert(letter.symbol.clone(), self.letters.len());
        self.letters.push(letter);
        let mut order: Vec<usize> = (0..self.letters.len()).collect();
        order.sort_by_key(|&i| std::cmp::Reverse(crate::py::char_len(&self.letters[i].symbol)));
        self.sorted_keys = order;
    }

    pub fn get(&self, symbol: &str) -> Option<&Letter> {
        self.index.get(symbol).map(|&i| &self.letters[i])
    }

    pub fn contains(&self, symbol: &str) -> bool {
        self.index.contains_key(symbol)
    }

    pub fn sorted(&self) -> impl Iterator<Item = &Letter> {
        self.sorted_keys.iter().map(|&i| &self.letters[i])
    }

    pub fn len(&self) -> usize {
        self.letters.len()
    }

    pub fn is_empty(&self) -> bool {
        self.letters.is_empty()
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum DiacriticKind {
    Before,
    Combining,
    After,
}

impl DiacriticKind {
    pub const ALL: [(&'static str, DiacriticKind); 3] = [
        ("before", DiacriticKind::Before),
        ("combining", DiacriticKind::Combining),
        ("after", DiacriticKind::After),
    ];
}

#[derive(Clone, Debug)]
pub struct Diacritic {
    pub symbol: String,
    pub tier: Tier,
    pub kind: DiacriticKind,
    pub bundle: FeatureBundle,
    pub contour: bool,
    pub read_only: bool,
    pub marks_boundary: bool,
}

#[derive(Clone, Debug, Default)]
pub struct DiacriticInventory {
    pub diacritics: Vec<Diacritic>,
    index: HashMap<String, usize>,
    before_keys: Vec<usize>,
    attaching_keys: Vec<usize>,
}

impl DiacriticInventory {
    pub fn insert(&mut self, diacritic: Diacritic) {
        self.index.insert(diacritic.symbol.clone(), self.diacritics.len());
        self.diacritics.push(diacritic);
        let by_length = |pred: &dyn Fn(&Diacritic) -> bool| {
            let mut order: Vec<usize> =
                (0..self.diacritics.len()).filter(|&i| pred(&self.diacritics[i])).collect();
            order.sort_by_key(|&i| {
                std::cmp::Reverse(crate::py::char_len(&self.diacritics[i].symbol))
            });
            order
        };
        self.before_keys = by_length(&|d| d.kind == DiacriticKind::Before);
        self.attaching_keys = by_length(&|d| d.kind != DiacriticKind::Before);
    }

    pub fn get(&self, symbol: &str) -> Option<&Diacritic> {
        self.index.get(symbol).map(|&i| &self.diacritics[i])
    }

    pub fn contains(&self, symbol: &str) -> bool {
        self.index.contains_key(symbol)
    }

    pub fn before(&self) -> impl Iterator<Item = &Diacritic> {
        self.before_keys.iter().map(|&i| &self.diacritics[i])
    }

    pub fn attaching(&self) -> impl Iterator<Item = &Diacritic> {
        self.attaching_keys.iter().map(|&i| &self.diacritics[i])
    }
}

#[derive(Clone, Debug)]
pub struct Sonority {
    pub label: String,
    pub level: i64,
    pub bundle: Option<PatternBundle>,
}

#[derive(Clone, Debug)]
pub struct SyllablePart {
    pub part_type: String,
    pub time: i64,
    pub definition: Option<PatternBundle>,
    pub pattern: Option<Vec<Element>>,
}

/// Syllable-part constraints by time; each part carries forward until a later time redefines it.
#[derive(Clone, Debug, Default)]
pub struct SyllablePartsInventory {
    pub by_time: IndexMap<i64, IndexMap<String, Arc<SyllablePart>>>,
}

impl SyllablePartsInventory {
    /// The `part_type` in force at `time` (`None`: the latest).
    pub fn get_part(&self, time: Option<i64>, part_type: &str) -> Option<&Arc<SyllablePart>> {
        let mut times: Vec<i64> =
            self.by_time.keys().copied().filter(|t| time.is_none_or(|time| *t <= time)).collect();
        times.sort_unstable_by(|a, b| b.cmp(a));
        times.into_iter().find_map(|t| self.by_time[&t].get(part_type))
    }

    pub fn get_nucleus(&self, time: Option<i64>) -> Option<&Arc<SyllablePart>> {
        self.get_part(time, "nucleus")
    }

    pub fn nucleus_definition(&self, time: Option<i64>) -> Option<&PatternBundle> {
        self.get_nucleus(time).and_then(|p| p.definition.as_ref())
    }
}

#[derive(Clone, Debug)]
pub struct TierDeclaration {
    pub name: String,
    pub carries: Vec<FeatId>,
    pub anchor: PatternBundle,
    pub melody: bool,
    pub ocp: bool,
    pub stray_erase: bool,
    pub stability: String,
}

pub type TierInventory = IndexMap<String, TierDeclaration>;

// ---- Words ------------------------------------------------------------------------------------

#[derive(Clone, Debug, Default)]
pub struct Attestation {
    pub ipa: String,
    pub category: String,
    /// The target segmented against the inventory (set by `ingest_targets`).
    pub form: Option<Form>,
    pub note: String,
}

#[derive(Clone, Debug, Default)]
pub struct Word {
    pub id: String,
    /// Attested forms in file order; `None` is the untimed surface (`final`).
    pub forms: Vec<(Option<i64>, Attestation)>,
    pub gloss: String,
    pub frequency: i64,
    pub note: String,
}

impl Word {
    /// The time the derivation starts from: the earliest form (`None` if that is the surface).
    pub fn seed_time(&self) -> Option<i64> {
        self.seed_time_slot()
    }

    pub fn seed(&self) -> &Attestation {
        let seed_time = self.seed_time_slot();
        &self.forms.iter().find(|(t, _)| *t == seed_time).unwrap().1
    }

    /// The seed's time slot, `None` included (a word whose only form is its surface).
    fn seed_time_slot(&self) -> Option<i64> {
        self.forms.iter().map(|(t, _)| *t).min_by_key(|t| time_order(*t)).unwrap_or(None)
    }

    pub fn form_at(&self, time: Option<i64>) -> Option<&Attestation> {
        self.forms.iter().find(|(t, _)| *t == time).map(|(_, a)| a)
    }

    /// Every attestation but the seed, in file order.
    pub fn targets(&self) -> impl Iterator<Item = &(Option<i64>, Attestation)> {
        let seed = self.seed_time_slot();
        self.forms.iter().filter(move |(t, _)| *t != seed)
    }

    pub fn category_at(&self, time: Option<i64>) -> String {
        let best = self
            .forms
            .iter()
            .filter(|(t, _)| time_order(*t) <= time_order(time))
            .max_by_key(|(t, _)| time_order(*t));
        match best {
            Some((_, a)) => a.category.clone(),
            None => self.seed().category.clone(),
        }
    }

    pub fn ipa(&self) -> &str {
        &self.seed().ipa
    }

    pub fn final_ipa(&self) -> Option<&str> {
        self.form_at(None).map(|a| a.ipa.as_str())
    }

    pub fn final_form(&self) -> Option<&Form> {
        self.form_at(None).and_then(|a| a.form.as_ref())
    }

    /// The timed targets (every attestation but the seed and the surface), in file order.
    pub fn stages(&self) -> Vec<(i64, &str)> {
        let seed = self.seed_time_slot();
        self.forms
            .iter()
            .filter_map(|(t, a)| match t {
                Some(time) if *t != seed => Some((*time, a.ipa.as_str())),
                _ => None,
            })
            .collect()
    }

    pub fn stage_ipa(&self, time: i64) -> Option<&str> {
        self.stages().into_iter().find(|(t, _)| *t == time).map(|(_, s)| s)
    }

    /// The timed targets that segmented.
    pub fn stage_form(&self, time: i64) -> Option<&Form> {
        let seed = self.seed_time_slot();
        if seed == Some(time) {
            return None;
        }
        self.form_at(Some(time)).and_then(|a| a.form.as_ref())
    }

    pub fn stage_form_times(&self) -> Vec<i64> {
        let seed = self.seed_time_slot();
        self.forms
            .iter()
            .filter_map(|(t, a)| match t {
                Some(time) if *t != seed && a.form.is_some() => Some(*time),
                _ => None,
            })
            .collect()
    }
}

pub type WordInventory = IndexMap<String, Word>;

// ---- Settings ---------------------------------------------------------------------------------

#[derive(Clone, Debug)]
pub struct AccuracySettings {
    pub transposition_cost: i64,
}

#[derive(Clone, Debug)]
pub struct DiagnosisSettings {
    pub min_support: i64,
    pub min_support_percent: i64,
    pub min_errors: i64,
    pub report_top: i64,
    pub focus_count: i64,
}

#[derive(Clone, Debug)]
pub struct InductionSettings {
    pub min_improved_words: i64,
    pub top_confusions: i64,
    pub contexts_per_confusion: i64,
    pub placement_candidates: i64,
    pub max_rules_per_interval: i64,
    pub alignment_distance_cap: i64,
    pub final_weight: f64,
}

#[derive(Clone, Debug)]
pub struct Settings {
    pub accuracy: AccuracySettings,
    pub diagnosis: DiagnosisSettings,
    pub induction: InductionSettings,
}

impl Default for Settings {
    fn default() -> Self {
        Settings {
            accuracy: AccuracySettings { transposition_cost: 1 },
            diagnosis: DiagnosisSettings {
                min_support: 3,
                min_support_percent: 10,
                min_errors: 2,
                report_top: 8,
                focus_count: 5,
            },
            induction: InductionSettings {
                min_improved_words: 2,
                top_confusions: 5,
                contexts_per_confusion: 25,
                placement_candidates: 5,
                max_rules_per_interval: 60,
                alignment_distance_cap: 4,
                final_weight: 1.0,
            },
        }
    }
}

// ---- Forms ------------------------------------------------------------------------------------

#[derive(Clone, Debug)]
pub struct Segment {
    pub bundle: Arc<FeatureBundle>,
    pub id: u32,
}

#[derive(Clone, Debug)]
pub struct Autoseg {
    pub bundle: FeatureBundle,
    pub id: u32,
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
pub enum Side {
    Before,
    After,
}

impl Side {
    pub fn name(self) -> &'static str {
        match self {
            Side::Before => "before",
            Side::After => "after",
        }
    }
}

#[derive(Clone, Debug, Default)]
pub struct AutosegmentalTier {
    pub autosegs: Vec<Autoseg>,
    /// `(autoseg id, segment id)` association lines.
    pub links: BTreeSet<(u32, u32)>,
    pub float_hosts: IndexMap<u32, (u32, Side)>,
}

#[derive(Clone, Debug, Default)]
pub struct Form {
    pub segments: Vec<Segment>,
    pub tiers: IndexMap<String, AutosegmentalTier>,
    pub next_id: u32,
}

impl Form {
    pub fn from_bundles(bundles: Vec<FeatureBundle>) -> Form {
        let segments: Vec<Segment> = bundles
            .into_iter()
            .enumerate()
            .map(|(i, b)| Segment { bundle: Arc::new(b), id: i as u32 })
            .collect();
        let next_id = segments.len() as u32;
        Form { segments, tiers: IndexMap::new(), next_id }
    }

    pub fn fresh_id(&mut self) -> u32 {
        let id = self.next_id;
        self.next_id += 1;
        id
    }

    /// The segmental tier as a bundle list.
    pub fn bundles(&self) -> Vec<Arc<FeatureBundle>> {
        self.segments.iter().map(|s| s.bundle.clone()).collect()
    }

    pub fn tier_mut(&mut self, name: &str) -> &mut AutosegmentalTier {
        if !self.tiers.contains_key(name) {
            self.tiers.insert(name.to_string(), AutosegmentalTier::default());
        }
        self.tiers.get_mut(name).unwrap()
    }
}

/// Syllable boundaries: a boundary at `k` sits before segment `k`.
pub type Boundaries = BTreeSet<usize>;

#[derive(Clone, Copy, Debug)]
pub struct Syllable {
    pub start: usize,
    pub end: usize,
    pub nucleus: Option<usize>,
}

// ---- Bindings ---------------------------------------------------------------------------------

/// The matcher's environment: alpha values, back-references, conditions, branch choices.
#[derive(Clone, Debug, Default)]
pub struct Bindings {
    pub alpha: Vec<(char, Limb)>,
    pub reference: Vec<(i64, Arc<[Arc<FeatureBundle>]>)>,
    pub autoseg_reference: Vec<(i64, usize)>,
    pub floating_reference: Vec<(i64, u32)>,
    pub node_reference: Vec<(i64, FeatureBundle)>,
    pub permissive_alpha: bool,
    pub conditions: Vec<(i64, bool)>,
    pub disjunction_choices: Vec<usize>,
    pub pending_other: Vec<(char, Limb)>,
}

pub fn map_get<K: PartialEq + Copy, V>(map: &[(K, V)], key: K) -> Option<&V> {
    map.iter().find(|(k, _)| *k == key).map(|(_, v)| v)
}

pub fn map_set<K: PartialEq + Copy, V>(map: &mut Vec<(K, V)>, key: K, value: V) {
    if let Some(slot) = map.iter_mut().find(|(k, _)| *k == key) {
        slot.1 = value;
    } else {
        map.push((key, value));
    }
}

impl Bindings {
    /// Whether two reference maps hold the same entries (`dict ==`).
    pub fn same_references(&self, other: &Bindings) -> bool {
        self.reference.len() == other.reference.len()
            && self.reference.iter().all(|(k, v)| {
                map_get(&other.reference, *k).is_some_and(|w| {
                    v.len() == w.len() && v.iter().zip(w.iter()).all(|(a, b)| a == b)
                })
            })
    }
}

// ---- Project and derivations ------------------------------------------------------------------

#[derive(Clone, Debug)]
pub struct Project {
    pub features: FeatureInventory,
    pub letters: LetterInventory,
    pub diacritics: DiacriticInventory,
    pub sonorities: Vec<Sonority>,
    pub syllable_parts: SyllablePartsInventory,
    pub words: WordInventory,
    pub rules: RuleInventory,
    pub time: i64,
    pub tiers: TierInventory,
    pub settings: Settings,
    /// The syllable-tier feature ids, in declaration order.
    pub syllable_features: Vec<FeatId>,
}

impl Project {
    pub fn is_syllable_feature(&self, f: FeatId) -> bool {
        self.features.is_syllable(f)
    }
}

#[derive(Clone, Debug)]
pub struct DerivationStep {
    pub before: Arc<Form>,
    pub rule: Arc<Rule>,
    pub after: Arc<Form>,
    pub before_boundaries: Boundaries,
    pub after_boundaries: Boundaries,
}

#[derive(Clone, Debug)]
pub struct Derivation {
    pub word: Word,
    pub input: Arc<Form>,
    pub steps: Vec<DerivationStep>,
    pub surface: Arc<Form>,
    pub surface_boundaries: Boundaries,
}
