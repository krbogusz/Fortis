# Output — `projects/latin_to_french`

Engine-generated run output. For each word: the surface form and the
firing-rule trace (only the rules that changed the form).

## avant

`ˌɑbˈɑnte` → `a.vɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑˈbɑn.te → ˌɑˈbɑn.tɛ   (e→ɛ)
-100: b lenites to β intervocalically / before a sonorant
    ˌɑˈbɑn.tɛ → ˌɑˈβɑn.tɛ   (b→β)
500: the low vowel fronts by default
    ˌɑˈβɑn.tɛ → ˌaˈβan.tɛ   (ˌɑ→ˌa, ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌaˈβan.tɛ → ˌaˈβan.tə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌaˈβan.tə → ˌaˈβantə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌaˈβantə̯ → ˌaˈβant   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˌaˈβant → ˌaˈvant   (β→v)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌaˈvant → ˌaˈvãnt   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌaˈvãnt → ˌaˈvãːt   (ˈãn→ˈãː)
1400: long a becomes back ɑː
    ˌaˈvãːt → ˌaˈvɑ̃ːt   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˌaˈvɑ̃ːt → ˌaˈvɑ̃ː   (t→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈvɑ̃ː → a.vɑ̃ː   (ˌa→a, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    a.vɑ̃ː → a.vɑ̃   (ɑ̃ː→ɑ̃)
```

## ami

`ˌɑˈmiːkum` → `a.mi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑˈmiː.kum → ˌɑˈmiː.kʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑˈmiː.kʊm → ˌɑˈmi.kʊm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌɑˈmi.kʊm → ˌɑˈmi.kom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑˈmi.kom → ˌɑˈmi.ko   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑˈmi.ko → ˌɑˈmiː.ko   (ˈi→ˈiː)
500: k voices to g intervocalically
    ˌɑˈmiː.ko → ˌɑˈmiː.go   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˌɑˈmiː.go → ˌɑˈmiː.ɣo   (g→ɣ)
500: the low vowel fronts by default
    ˌɑˈmiː.ɣo → ˌaˈmiː.ɣo   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌaˈmiː.ɣo → ˌaˈmiː.ɣə   (o→ə)
600: schwa becomes non-syllabic
    ˌaˈmiː.ɣə → ˌaˈmiːɣə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌaˈmiːɣə̯ → ˌaˈmiːɣ   (ə̯→∅)
750: all final obstruents devoice
    ˌaˈmiːɣ → ˌaˈmiːx   (ɣ→x)
750: vowel length resets to short
    ˌaˈmiːx → ˌaˈmix   (ˈiː→ˈi)
750: remaining x/ɣ front
    ˌaˈmix → ˌaˈmiç   (x→ç)
750: ç merges into ʝ
    ˌaˈmiç → ˌaˈmiʝ   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌaˈmiʝ → ˌaˈmij   (ʝ→j)
750: j deletes after a high front tense vowel
    ˌaˈmij → ˌaˈmi   (j→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌaˈmi → ˌãˈmi   (ˌa→ˌã)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˌãˈmi → ˌaˈmi   (ˌã→ˌa)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈmi → a.mi   (ˌa→a, ˈi→i)
```

## eau

`ˈɑkwɑm` → `ɛɥ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈɑ.kwɑm → ˈɑ.kɣʷɑm   (w→ɣʷ)
-100: the labiovelar approximant simplifies to w after a velar consonant
    ˈɑ.kɣʷɑm → ˈɑ.kwɑm   (ɣʷ→w)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑ.kwɑm → ˈɑ.kwɑ   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈɑ.kwɑ → ˈɑː.kwɑ   (ˈɑ→ˈɑː)
500: intervocalic k spirantizes to x before w + glide (qu-)
    ˈɑː.kwɑ → ˈɑː.xwɑ   (k→x)
500: the low vowel fronts by default
    ˈɑː.xwɑ → ˈaː.xwa   (ˈɑː→ˈaː, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈaː.xwa → ˈaː.xwʲa   (w→wʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈaː.xwʲa → ˈaː.xɥa   (wʲ→ɥ)
600: a voiceless consonant voices intervocalically
    ˈaː.xɥa → ˈaː.ɣɥa   (x→ɣ)
600: long stressed vowels diphthongize
    ˈaː.ɣɥa → ˈae̯.ɣɥa   (ˈaː→ˈae̯)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈae̯.ɣɥa → ˈae̯.ɣɥə   (a→ə)
750: the ae̯ diphthong's offglide fuses with a following ɣ to j, when a w still follows
    ˈae̯.ɣɥə → ˈaj.ɥə   (e̯ɣ→j)
1200: schwa desyllabifies after another vowel
    ˈaj.ɥə → ˈajɥə̯   (ə→ə̯)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈajɥə̯ → ˈɛːɥə̯   (ˈaj→ˈɛː)
1400: the final off-glide schwa is deleted elsewhere
    ˈɛːɥə̯ → ˈɛːɥ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛːɥ → ɛːɥ   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    ɛːɥ → ɛɥ   (ɛː→ɛ)
```

## aime

`ˈɑmɑt` → `ɛm`

```
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.mɑt → ˈɑː.mɑt   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑː.mɑt → ˈaː.mat   (ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˈaː.mat → ˈae̯.mat   (ˈaː→ˈae̯)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˈae̯.mat → ˈaj.mat   (e̯→j)
750: a word-final stop re-opens to a fricative after a vowel
    ˈaj.mat → ˈaj.maθ̠   (t→θ̠)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈaj.maθ̠ → ˈaj.məθ̠   (a→ə)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˈaj.məθ̠ → ˈaj̃.məθ̠   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈaj̃.məθ̠ → ˈãj̃.məθ̠   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈãj̃.məθ̠ → ˈɛ̃j̃.məθ̠   (ˈã→ˈɛ̃)
1200: a single final consonant effaces after schwa
    ˈɛ̃j̃.məθ̠ → ˈɛ̃j̃.mə   (θ̠→∅)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈɛ̃j̃.mə → ˈɛ̃.mə   (j̃→∅)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈɛ̃.mə → ˈɛ.mə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈɛ.mə → ˈɛmə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈɛmə̯ → ˈɛm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛm → ɛm   (ˈɛ→ɛ)
```

## an

`ˈɑnnum` → `ɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑn.num → ˈɑn.nʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈɑn.nʊm → ˈɑn.nom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑn.nom → ˈɑn.no   (m→∅)
500: the low vowel fronts by default
    ˈɑn.no → ˈan.no   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈan.no → ˈan.nə   (o→ə)
600: schwa becomes non-syllabic
    ˈan.nə → ˈannə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈannə̯ → ˈann   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˈann → ˈan   (n→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈan → ˈãn   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈãn → ˈãː   (ˈãn→ˈãː)
1400: long a becomes back ɑː
    ˈãː → ˈɑ̃ː   (ˈãː→ˈɑ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈɑ̃ː → ɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ɑ̃ː → ɑ̃   (ɑ̃ː→ɑ̃)
```

## arc

`ˈɑrkuːm` → `aʁk`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈɑr.kuːm → ˈɑr.kum   (uː→u)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑr.kum → ˈɑr.ku   (m→∅)
500: the low vowel fronts by default
    ˈɑr.ku → ˈar.ku   (ˈɑ→ˈa)
500: a high tense round non-nasal vowel centralizes
    ˈar.ku → ˈar.kʉ   (u→ʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈar.kʉ → ˈar.kə   (ʉ→ə)
600: schwa becomes non-syllabic
    ˈar.kə → ˈarkə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈarkə̯ → ˈark   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈark → ˈaɹk   (r→ɹ)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈaɹk → ˈaɹkə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈaɹkə̯ → ˈaɹk   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈaɹk → ˈark   (ɹ→r)
1400: r becomes uvular ʀ
    ˈark → ˈaʀk   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈaʀk → aʀk   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    aʀk → aʁk   (ʀ→ʁ)
```

## or

`ˈɑwrum` → `ɔʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑw.rum → ˈɑw.rʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈɑw.rʊm → ˈɑw.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑw.rom → ˈɑw.ro   (m→∅)
300: a stressed vowel lengthens before a voiced labial + r + vowel + word end
    ˈɑw.ro → ˈɑːw.ro   (ˈɑ→ˈɑː)
500: a vowel shortens before a consonant cluster
    ˈɑːw.ro → ˈɑw.ro   (ˈɑː→ˈɑ)
500: a stressed vowel lengthens before a voiced labial + r + vowel + word end
    ˈɑw.ro → ˈɑːw.ro   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑːw.ro → ˈaːw.ro   (ˈɑː→ˈaː)
500: a vowel shortens before a consonant cluster (recurrence)
    ˈaːw.ro → ˈaw.ro   (ˈaː→ˈa)
500: a stressed vowel lengthens before a voiced labial + r + vowel (recurrence)
    ˈaw.ro → ˈaːw.ro   (ˈa→ˈaː)
500: a vowel shortens before the high back round glide (w)
    ˈaːw.ro → ˈaw.ro   (ˈaː→ˈa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈaw.ro → ˈɔw.ro   (ˈa→ˈɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈɔw.ro → ˈɔw.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈɔw.rə → ˈɔwrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈɔwrə̯ → ˈɔwr   (ə̯→∅)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˈɔwr → ˈœr   (ˈɔw→ˈœ)
1400: the tonic vowel of or is back ɔ (au monophthong), not front œ
    ˈœr → ˈɔr   (ˈœ→ˈɔ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈɔr → ˈɔɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈɔɹ → ˈɔr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈɔr → ˈɔʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈɔʀ → ɔʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ɔʀ → ɔʁ   (ʀ→ʁ)
```

## aile

`ˈɑːlɑm` → `ɛl`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈɑː.lɑm → ˈɑ.lɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑ.lɑm → ˈɑ.lɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.lɑ → ˈɑː.lɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑː.lɑ → ˈaː.la   (ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˈaː.la → ˈae̯.la   (ˈaː→ˈae̯)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈae̯.la → ˈae̯.lə   (a→ə)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈae̯.lə → ˈeː.lə   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈeː.lə → ˈe.lə   (ˈeː→ˈe)
1400: e lowers to ɛ before a lateral
    ˈe.lə → ˈɛ.lə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈɛ.lə → ˈɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈɛlə̯ → ˈɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛl → ɛl   (ˈɛ→ɛ)
```

## amère

`ˌɑˈmɑːrɑm` → `a.mɛʁ`

```
-100: the length feature is dropped now that quality carries the contrast
    ˌɑˈmɑː.rɑm → ˌɑˈmɑ.rɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑˈmɑ.rɑm → ˌɑˈmɑ.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑˈmɑ.rɑ → ˌɑˈmɑː.rɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌɑˈmɑː.rɑ → ˌaˈmaː.ra   (ˌɑ→ˌa, ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˌaˈmaː.ra → ˌaˈmae̯.ra   (ˈaː→ˈae̯)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌaˈmae̯.ra → ˌaˈmae̯.rə   (a→ə)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌaˈmae̯.rə → ˌaˈmeː.rə   (ˈae̯→ˈeː)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌaˈmeː.rə → ˌãˈmeː.rə   (ˌa→ˌã)
1000: vowel length resets to short
    ˌãˈmeː.rə → ˌãˈme.rə   (ˈeː→ˈe)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˌãˈme.rə → ˌãˈmɛ.rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌãˈmɛ.rə → ˌãˈmɛrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌãˈmɛrə̯ → ˌãˈmɛr   (ə̯→∅)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˌãˈmɛr → ˌaˈmɛr   (ˌã→ˌa)
1400: r becomes uvular ʀ
    ˌaˈmɛr → ˌaˈmɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈmɛʀ → a.mɛʀ   (ˌa→a, ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    a.mɛʀ → a.mɛʁ   (ʀ→ʁ)
```

## ample

`ˈɑmplum` → `ɑ̃pl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑm.plum → ˈɑm.plʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈɑm.plʊm → ˈɑm.plom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑm.plom → ˈɑm.plo   (m→∅)
500: the low vowel fronts by default
    ˈɑm.plo → ˈam.plo   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈam.plo → ˈam.plə   (o→ə)
600: schwa becomes non-syllabic
    ˈam.plə → ˈamplə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈamplə̯ → ˈam.plə   (ə̯→ə)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈam.plə → ˈãm.plə   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈãm.plə → ˈãː.plə   (ˈãm→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈãː.plə → ˈãːplə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈãːplə̯ → ˈɑ̃ːplə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈɑ̃ːplə̯ → ˈɑ̃ːpl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɑ̃ːpl → ɑ̃ːpl   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ɑ̃ːpl → ɑ̃pl   (ɑ̃ː→ɑ̃)
```

## art

`ˈɑrtem` → `aʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑr.tem → ˈɑr.tɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑr.tɛm → ˈɑr.tɛ   (m→∅)
500: the low vowel fronts by default
    ˈɑr.tɛ → ˈar.tɛ   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈar.tɛ → ˈar.tə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈar.tə → ˈartə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈartə̯ → ˈart   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈart → ˈaɹt   (r→ɹ)
1400: final obstruents are lost
    ˈaɹt → ˈaɹ   (t→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈaɹ → ˈar   (ɹ→r)
1400: r becomes uvular ʀ
    ˈar → ˈaʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈaʀ → aʀ   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    aʀ → aʁ   (ʀ→ʁ)
```

## ail

`ˈɑllium` → `aj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑl.li.um → ˈɑl.lɪ.ʊm   (i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈɑl.lɪ.ʊm → ˈɑl.ljʊm   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˈɑl.ljʊm → ˈɑl.ɫjʊm   (l→ɫ)
-100: yod strengthens before a vowel
    ˈɑl.ɫjʊm → ˈɑlɫ.ʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈɑlɫ.ʝʊm → ˈɑlɫ.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑlɫ.ʝom → ˈɑlɫ.ʝo   (m→∅)
300: ll palatalizes to ʎ before yod
    ˈɑlɫ.ʝo → ˈɑ.ʎo   (lɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.ʎo → ˈɑː.ʎo   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑː.ʎo → ˈaː.ʎo   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaː.ʎo → ˈaː.ʎə   (o→ə)
600: schwa becomes non-syllabic
    ˈaː.ʎə → ˈaːʎə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈaːʎə̯ → ˈaːʎ   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈaːʎ → ˈae̯ʎ   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˈae̯ʎ → ˈaʎ   (e̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈaʎ → aʎ   (ˈa→a)
1400: ʎ becomes j
    aʎ → aj   (ʎ→j)
```

## aube

`ˈɑlbɑm` → `ob`

```
-100: l darkens before a non-lateral consonant
    ˈɑl.bɑm → ˈɑɫ.bɑm   (l→ɫ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑɫ.bɑm → ˈɑɫ.bɑ   (m→∅)
500: the low vowel fronts by default
    ˈɑɫ.bɑ → ˈaɫ.ba   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈaɫ.ba → ˈaɫ.bə   (a→ə)
1000: back dark-l variants vocalize to w
    ˈaɫ.bə → ˈaw.bə   (ɫ→w)
1200: aw becomes long oː
    ˈaw.bə → ˈoː.bə   (ˈaw→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˈoː.bə → ˈoːbə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈoːbə̯ → ˈoːb   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈoːb → oːb   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    oːb → ob   (oː→o)
```

## ane

`ˈɑnɑtem` → `ɑ̃t`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑ.nɑ.tem → ˈɑ.nɑ.tɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑ.nɑ.tɛm → ˈɑ.nɑ.tɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.nɑ.tɛ → ˈɑː.nɑ.tɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑː.nɑ.tɛ → ˈaː.na.tɛ   (ˈɑː→ˈaː, ɑ→a)
600: an unstressed a becomes schwa before consonants + vowel + optional consonants + word end
    ˈaː.na.tɛ → ˈaː.nə.tɛ   (a→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaː.nə.tɛ → ˈaː.nə.tə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈaː.nə.tə → ˈaːnə̯tə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈaːnə̯tə̯ → ˈaːnə̯.tə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈaːnə̯.tə → ˈaːn.tə   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈaːn.tə → ˈan.tə   (ˈaː→ˈa)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈan.tə → ˈãn.tə   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈãn.tə → ˈãː.tə   (ˈãn→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈãː.tə → ˈãːtə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈãːtə̯ → ˈɑ̃ːtə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈɑ̃ːtə̯ → ˈɑ̃ːt   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɑ̃ːt → ɑ̃ːt   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ɑ̃ːt → ɑ̃t   (ɑ̃ː→ɑ̃)
```

## able

`ˈɑːbilem` → `abl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑː.bi.lem → ˈɑː.bɪ.lɛm   (i→ɪ, e→ɛ)
-100: b lenites to β intervocalically / before a sonorant
    ˈɑː.bɪ.lɛm → ˈɑː.βɪ.lɛm   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˈɑː.βɪ.lɛm → ˈɑ.βɪ.lɛm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˈɑ.βɪ.lɛm → ˈɑ.βe.lɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑ.βe.lɛm → ˈɑ.βe.lɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.βe.lɛ → ˈɑː.βe.lɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑː.βe.lɛ → ˈaː.βe.lɛ   (ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈaː.βe.lɛ → ˈaː.βə.lɛ   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaː.βə.lɛ → ˈaː.βə.lə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈaː.βə.lə → ˈaːβə̯lə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈaːβə̯lə̯ → ˈaːβə̯.lə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈaːβə̯.lə → ˈaː.βlə   (ə̯→∅)
600: the bilabial fricative hardens to b before a lateral
    ˈaː.βlə → ˈaː.blə   (β→b)
600: a non-round vowel shortens before a stop + l
    ˈaː.blə → ˈa.blə   (ˈaː→ˈa)
1400: final ə becomes a non-syllabic off-glide
    ˈa.blə → ˈablə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈablə̯ → ˈabl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈabl → abl   (ˈa→a)
```

## auguste

`ˌɑwˈgustus` → `ɔ.u`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑwˈgus.tus → ˌɑwˈgʊs.tʊs   (ˈu→ˈʊ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˌɑwˈgʊs.tʊs → ˌɑwˈgos.tos   (ˈʊ→ˈo, ʊ→o)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˌɑwˈgos.tos → ˌɑwˈɣos.tos   (g→ɣ)
500: the velar fricative is lost before a primary-stressed tense round vowel (recurrence)
    ˌɑwˈɣos.tos → ˌɑˈwos.tos   (ɣ→∅)
500: the low vowel fronts by default
    ˌɑˈwos.tos → ˌaˈwos.tos   (ˌɑ→ˌa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌaˈwos.tos → ˌɔˈwos.tos   (ˌa→ˌɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɔˈwos.tos → ˌɔˈwos.təs   (o→ə)
600: schwa becomes non-syllabic
    ˌɔˈwos.təs → ˌɔˈwostə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌɔˈwostə̯s → ˌɔˈwosts   (ə̯→∅)
600: secondary-stressed ɔ raises to ɯ before w
    ˌɔˈwosts → ˌɯˈwosts   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌɯˈwosts → ˌɔˈwosts   (ˌɯ→ˌɔ)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌɔˈwosts → ˌɔˈwoss   (t→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˌɔˈwoss → ˌɔˈwos   (s→∅)
1000: ow simplifies to o before any coronal sonorant
    ˌɔˈwos → ˌɔˈos   (w→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌɔˈos → ˌɔˈus   (ˈo→ˈu)
1000: a primary-stressed vowel lengthens before word-final s
    ˌɔˈus → ˌɔˈuːs   (ˈu→ˈuː)
1400: final obstruents are lost
    ˌɔˈuːs → ˌɔˈuː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌɔˈuː → ɔ.uː   (ˌɔ→ɔ, ˈuː→uː)
1400: distinctive vowel length is lost entirely
    ɔ.uː → ɔ.u   (uː→u)
```

## avers

`ˌɑd̪ˈwersum` → `a.vjɛʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌɑˈd̪wer.sum → ˌɑˈd̪ɣʷer.sum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑˈd̪ɣʷer.sum → ˌɑˈd̪ɣʷɛr.sʊm   (ˈe→ˈɛ, u→ʊ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɑˈd̪ɣʷɛr.sʊm → ˌɑˈd̪βʷɛr.sʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˌɑˈd̪βʷɛr.sʊm → ˌɑˈd̪βʷɛr.som   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑˈd̪βʷɛr.som → ˌɑˈd̪βʷɛr.so   (m→∅)
500: labialized bilabial fricatives delabialize
    ˌɑˈd̪βʷɛr.so → ˌɑˈd̪βɛr.so   (βʷ→β)
500: the low vowel fronts by default
    ˌɑˈd̪βɛr.so → ˌaˈd̪βɛr.so   (ˌɑ→ˌa)
600: d becomes ð before a labial continuant consonant
    ˌaˈd̪βɛr.so → ˌaðˈβɛr.so   (d̪→ð)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌaðˈβɛr.so → ˌaðˈβɛr.sə   (o→ə)
600: schwa becomes non-syllabic
    ˌaðˈβɛr.sə → ˌaðˈβɛrsə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌaðˈβɛrsə̯ → ˌaðˈβɛrs   (ə̯→∅)
600: a stressed vowel lengthens before r + s + word end
    ˌaðˈβɛrs → ˌaðˈβɛːrs   (ˈɛ→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌaðˈβɛːrs → ˌaðˈβie̯rs   (ˈɛː→ˈie̯)
600: the remaining bilabial fricative becomes v
    ˌaðˈβie̯rs → ˌaðˈvie̯rs   (β→v)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌaðˈvie̯rs → ˌaðˈvjers   (ˈi→j, e̯→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌaðˈvjers → ˌaˈvjers   (ð→∅)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˌaˈvjers → ˌaˈvjɛrs   (ˈe→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌaˈvjɛrs → ˌaˈvjɛɹs   (r→ɹ)
1400: final obstruents are lost
    ˌaˈvjɛɹs → ˌaˈvjɛɹ   (s→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌaˈvjɛɹ → ˌaˈvjɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌaˈvjɛr → ˌaˈvjɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈvjɛʀ → a.vjɛʀ   (ˌa→a, ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    a.vjɛʀ → a.vjɛʁ   (ʀ→ʁ)
```

## alose

`ˌɑlˈɑwsɑm` → `a.loz`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑˈlɑw.sɑm → ˌɑˈlɑw.sɑ   (m→∅)
500: the low vowel fronts by default
    ˌɑˈlɑw.sɑ → ˌaˈlaw.sa   (ˌɑ→ˌa, ˈɑ→ˈa, ɑ→a)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌaˈlaw.sa → ˌaˈlɔw.sa   (ˈa→ˈɔ)
600: a voiceless consonant voices intervocalically
    ˌaˈlɔw.sa → ˌaˈlɔw.za   (s→z)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌaˈlɔw.za → ˌaˈlɔ.za   (w→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌaˈlɔ.za → ˌaˈlɔ.zə   (a→ə)
1200: lax back mid o lengthens before z or v
    ˌaˈlɔ.zə → ˌaˈlɔː.zə   (ˈɔ→ˈɔː)
1200: a long back mid o tenses to oː
    ˌaˈlɔː.zə → ˌaˈloː.zə   (ˈɔː→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˌaˈloː.zə → ˌaˈloːzə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌaˈloːzə̯ → ˌaˈloːz   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈloːz → a.loːz   (ˌa→a, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    a.loːz → a.loz   (oː→o)
```

## Aisne

`ˈɑkin̪um` → `ɛn̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑ.ki.n̪um → ˈɑ.kɪ.n̪ʊm   (i→ɪ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈɑ.kɪ.n̪ʊm → ˈɑ.ke.n̪om   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑ.ke.n̪om → ˈɑ.ke.n̪o   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈɑ.ke.n̪o → ˈɑ.kʲe.n̪o   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈɑ.kʲe.n̪o → ˈɑ.ce.n̪o   (kʲ→c)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈɑ.ce.n̪o → ˈɑ.cn̪o   (e→∅)
500: a palatal stop spirantizes before a dental/postalveolar fricative
    ˈɑ.cn̪o → ˈɑ.çn̪o   (c→ç)
500: the low vowel fronts by default
    ˈɑ.çn̪o → ˈa.çn̪o   (ˈɑ→ˈa)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈa.çn̪o → ˈa.çn̪ʲo   (n̪→n̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈa.çn̪ʲo → ˈa.çn̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈa.çn̪ʲə → ˈaçn̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈaçn̪ʲə̯ → ˈa.çn̪ʲə   (ə̯→ə)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈa.çn̪ʲə → ˈaçj.n̪ə   (n̪ʲ→jn̪)
600: j is lost after j or a consonant, before a consonant
    ˈaçj.n̪ə → ˈa.çn̪ə   (j→∅)
750: ç merges into ʝ
    ˈa.çn̪ə → ˈa.ʝn̪ə   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈa.ʝn̪ə → ˈaj.n̪ə   (ʝ→j)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˈaj.n̪ə → ˈaj̃.n̪ə   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈaj̃.n̪ə → ˈãj̃.n̪ə   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈãj̃.n̪ə → ˈɛ̃j̃.n̪ə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈɛ̃j̃.n̪ə → ˈɛ̃.n̪ə   (j̃→∅)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈɛ̃.n̪ə → ˈɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈɛ.n̪ə → ˈɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈɛn̪ə̯ → ˈɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛn̪ → ɛn̪   (ˈɛ→ɛ)
```

## angle

`ˈɑn̪gulum` → `ɑ̃gl`

```
-100: n assimilates to a following velar stop
    ˈɑn̪.gu.lum → ˈɑŋ.gu.lum   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑŋ.gu.lum → ˈɑŋ.gʊ.lʊm   (u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈɑŋ.gʊ.lʊm → ˈɑŋ.glʊm   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈɑŋ.glʊm → ˈɑŋ.glom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑŋ.glom → ˈɑŋ.glo   (m→∅)
500: the low vowel fronts by default
    ˈɑŋ.glo → ˈaŋ.glo   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaŋ.glo → ˈaŋ.glə   (o→ə)
600: schwa becomes non-syllabic
    ˈaŋ.glə → ˈaŋglə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈaŋglə̯ → ˈaŋ.glə   (ə̯→ə)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈaŋ.glə → ˈãŋ.glə   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈãŋ.glə → ˈãː.glə   (ˈãŋ→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈãː.glə → ˈãːglə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈãːglə̯ → ˈɑ̃ːglə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈɑ̃ːglə̯ → ˈɑ̃ːgl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɑ̃ːgl → ɑ̃ːgl   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ɑ̃ːgl → ɑ̃gl   (ɑ̃ː→ɑ̃)
```

## ardoise

`ˌɑrˈd̪eːsiɑm` → `aʁ.d̪waz`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑrˈd̪eː.si.ɑm → ˌɑrˈd̪eː.sɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɑrˈd̪eː.sɪ.ɑm → ˌɑrˈd̪eː.sjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɑrˈd̪eː.sjɑm → ˌɑrˈd̪eːs.ʝɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑrˈd̪eːs.ʝɑm → ˌɑrˈd̪es.ʝɑm   (ˈeː→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑrˈd̪es.ʝɑm → ˌɑrˈd̪es.ʝɑ   (m→∅)
500: a voiceless fricative voices before yod + a non-consonantal segment
    ˌɑrˈd̪es.ʝɑ → ˌɑrˈd̪ez.ʝɑ   (s→z)
500: z + yod becomes palatalized z
    ˌɑrˈd̪ez.ʝɑ → ˌɑrˈd̪e.zʲɑ   (zʝ→zʲ)
500: the low vowel fronts by default
    ˌɑrˈd̪e.zʲɑ → ˌarˈd̪e.zʲa   (ˌɑ→ˌa, ɑ→a)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌarˈd̪e.zʲa → ˌarˈd̪eː.zʲa   (ˈe→ˈeː)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌarˈd̪eː.zʲa → ˌarˈd̪eːj.za   (zʲ→jz)
600: a vowel shortens before a consonant cluster ending in an obstruent (recurrence)
    ˌarˈd̪eːj.za → ˌarˈd̪ej.za   (ˈeː→ˈe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌarˈd̪ej.za → ˌarˈd̪ej.zə   (a→ə)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌarˈd̪ej.zə → ˌarˈd̪oj.zə   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌarˈd̪oj.zə → ˌarˈd̪uj.zə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌarˈd̪uj.zə → ˌarˈd̪uɛ̯.zə   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌarˈd̪uɛ̯.zə → ˌarˈd̪wɛ.zə   (ˈu→w, ɛ̯→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌarˈd̪wɛ.zə → ˌarˈd̪wɛzə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌarˈd̪wɛzə̯ → ˌaɹˈd̪wɛzə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˌaɹˈd̪wɛzə̯ → ˌaɹˈd̪wɛz   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌaɹˈd̪wɛz → ˌarˈd̪wɛz   (ɹ→r)
1400: r becomes uvular ʀ
    ˌarˈd̪wɛz → ˌaʀˈd̪wɛz   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌaʀˈd̪wɛz → aʀ.d̪wɛz   (ˌa→a, ˈɛ→ɛ)
1400: wɛ becomes wa
    aʀ.d̪wɛz → aʀ.d̪waz   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    aʀ.d̪waz → aʁ.d̪waz   (ʀ→ʁ)
```

## oser

`ˌɑwˈsɑːre` → `o.ze`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑwˈsɑː.re → ˌɑwˈsɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑwˈsɑː.rɛ → ˌɑwˈsɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑwˈsɑ.rɛ → ˌɑwˈsɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌɑwˈsɑː.rɛ → ˌawˈsaː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌawˈsaː.rɛ → ˌɔwˈsaː.rɛ   (ˌa→ˌɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɔwˈsaː.rɛ → ˌɔwˈsaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌɔwˈsaː.rə → ˌɔwˈsaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌɔwˈsaːrə̯ → ˌɔwˈsaːr   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌɔwˈsaːr → ˌɔwˈzaːr   (s→z)
600: long stressed vowels diphthongize
    ˌɔwˈzaːr → ˌɔwˈzae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɔ raises to ɯ before w
    ˌɔwˈzae̯r → ˌɯwˈzae̯r   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌɯwˈzae̯r → ˌɔwˈzae̯r   (ˌɯ→ˌɔ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌɔwˈzae̯r → ˌɔˈzae̯r   (w→∅)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌɔˈzae̯r → ˌɔˈzeːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌɔˈzeːr → ˌɔˈzer   (ˈeː→ˈe)
1200: lax back mid o lengthens before z or v
    ˌɔˈzer → ˌɔːˈzer   (ˌɔ→ˌɔː)
1200: a long back mid o tenses to oː
    ˌɔːˈzer → ˌoːˈzer   (ˌɔː→ˌoː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌoːˈzer → ˌoːˈzeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌoːˈzeɹ → ˌoːˈze   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌoːˈze → oː.ze   (ˌoː→oː, ˈe→e)
1400: distinctive vowel length is lost entirely
    oː.ze → o.ze   (oː→o)
```

## barge

`ˈbɑrgɑm` → `baʁʒ`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɑr.gɑm → ˈbɑr.gɑ   (m→∅)
500: the low vowel fronts by default
    ˈbɑr.gɑ → ˈbar.ga   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈbar.ga → ˈbar.gʲa   (g→gʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈbar.gʲa → ˈbar.ɟa   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈbar.ɟa → ˈbar.d͡ʒa   (ɟ→d͡ʒ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈbar.d͡ʒa → ˈbar.d͡ʒə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈbar.d͡ʒə → ˈbar.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈbar.ʒə → ˈbarʒə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈbarʒə̯ → ˈbaɹʒə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈbaɹʒə̯ → ˈbaɹʒ   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈbaɹʒ → ˈbarʒ   (ɹ→r)
1400: r becomes uvular ʀ
    ˈbarʒ → ˈbaʀʒ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈbaʀʒ → baʀʒ   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    baʀʒ → baʁʒ   (ʀ→ʁ)
```

## belle

`ˈbellɑm` → `bɛl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbel.lɑm → ˈbɛl.lɑm   (ˈe→ˈɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɛl.lɑm → ˈbɛl.lɑ   (m→∅)
500: the low vowel fronts by default
    ˈbɛl.lɑ → ˈbɛl.la   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈbɛl.la → ˈbɛl.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈbɛl.lə → ˈbɛ.lə   (l→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈbɛ.lə → ˈbɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈbɛlə̯ → ˈbɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈbɛl → bɛl   (ˈɛ→ɛ)
```

## blanche

`blˈɑn̪kɑm` → `blɑ̃ʃ`

```
-100: n assimilates to a following velar stop
    ˈblɑn̪.kɑm → ˈblɑŋ.kɑm   (n̪→ŋ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈblɑŋ.kɑm → ˈblɑŋ.kɑ   (m→∅)
500: the low vowel fronts by default
    ˈblɑŋ.kɑ → ˈblaŋ.ka   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈblaŋ.ka → ˈblaŋ.kʲa   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈblaŋ.kʲa → ˈblaŋ.ca   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈblaŋ.ca → ˈblaŋ.t͡ʃa   (c→t͡ʃ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈblaŋ.t͡ʃa → ˈblaŋ.t͡ʃə   (a→ə)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈblaŋ.t͡ʃə → ˈblãŋ.t͡ʃə   (ˈa→ˈã)
1000: ŋ simplifies to n before a non-velar segment
    ˈblãŋ.t͡ʃə → ˈblãn̪.t͡ʃə   (ŋ→n̪)
1000: all affricates become sibilants (deaffrication)
    ˈblãn̪.t͡ʃə → ˈblãn̪.ʃə   (t͡ʃ→ʃ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈblãn̪.ʃə → ˈblãː.ʃə   (ˈãn̪→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈblãː.ʃə → ˈblãːʃə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈblãːʃə̯ → ˈblɑ̃ːʃə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈblɑ̃ːʃə̯ → ˈblɑ̃ːʃ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈblɑ̃ːʃ → blɑ̃ːʃ   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    blɑ̃ːʃ → blɑ̃ʃ   (ɑ̃ː→ɑ̃)
```

## brace

`brˈɑkʰiɑm` → `bʁas`

```
-100: aspiration lost on Greek loanwords (2nd century)
    ˈbrɑ.kʰi.ɑm → ˈbrɑ.ki.ɑm   (kʰ→k)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbrɑ.ki.ɑm → ˈbrɑ.kɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈbrɑ.kɪ.ɑm → ˈbrɑ.kjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈbrɑ.kjɑm → ˈbrɑ.kʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbrɑ.kʝɑm → ˈbrɑ.kʝɑ   (m→∅)
-100: k geminates (as palatal cc) intervocalically before yod + vowel
    ˈbrɑ.kʝɑ → ˈbrɑc.cʝɑ   (k→cc)
300: yod absorbed into a preceding palatalized consonant
    ˈbrɑc.cʝɑ → ˈbrɑc.cɑ   (ʝ→∅)
500: geminate palatal stop cc becomes t + tsʲ
    ˈbrɑc.cɑ → ˈbrɑ.t̪t͡sʲɑ   (c→t̪, c→t͡sʲ)
500: the low vowel fronts by default
    ˈbrɑ.t̪t͡sʲɑ → ˈbra.t̪t͡sʲa   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈbra.t̪t͡sʲa → ˈbra.t̪t͡sʲə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈbra.t̪t͡sʲə → ˈbra.t͡sʲə   (t̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈbra.t͡sʲə → ˈbra.sʲə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈbra.sʲə → ˈbra.sə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈbra.sə → ˈbrasə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈbrasə̯ → ˈbras   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈbras → ˈbʀas   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈbʀas → bʀas   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    bʀas → bʁas   (ʀ→ʁ)
```

## boîte

`bˈuksit̪ɑm` → `bwat̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbu.ksi.t̪ɑm → ˈbʊ.ksɪ.t̪ɑm   (ˈu→ˈʊ, i→ɪ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈbʊ.ksɪ.t̪ɑm → ˈbʊx.sɪ.t̪ɑm   (k→x)
-100: lax high vowels lower to tense mid vowels
    ˈbʊx.sɪ.t̪ɑm → ˈbox.se.t̪ɑm   (ˈʊ→ˈo, ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbox.se.t̪ɑm → ˈbox.se.t̪ɑ   (m→∅)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈbox.se.t̪ɑ → ˈboxs.t̪ɑ   (e→∅)
500: the low vowel fronts by default
    ˈboxs.t̪ɑ → ˈboxs.t̪a   (ɑ→a)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈboxs.t̪a → ˈboçs.t̪a   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈboçs.t̪a → ˈboçsʲ.t̪a   (s→sʲ)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈboçsʲ.t̪a → ˈboçsʲ.t̪ʲa   (t̪→t̪ʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈboçsʲ.t̪ʲa → ˈboçjsj.t̪a   (sʲt̪ʲ→jsjt̪)
600: j is lost after j or a consonant, before a consonant
    ˈboçjsj.t̪a → ˈboçs.t̪a   (jsj→s)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈboçs.t̪a → ˈboçs.t̪ə   (a→ə)
750: ç merges into ʝ
    ˈboçs.t̪ə → ˈboʝs.t̪ə   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈboʝs.t̪ə → ˈbojs.t̪ə   (ʝ→j)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈbojs.t̪ə → ˈbujs.t̪ə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈbujs.t̪ə → ˈbuɛ̯s.t̪ə   (j→ɛ̯)
1000: s becomes x after a vowel, before any consonant
    ˈbuɛ̯s.t̪ə → ˈbuɛ̯x.t̪ə   (s→x)
1000: the velar fricative x is lost
    ˈbuɛ̯x.t̪ə → ˈbuɛ̯.t̪ə   (x→∅)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈbuɛ̯.t̪ə → ˈbwɛ.t̪ə   (ˈu→w, ɛ̯→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈbwɛ.t̪ə → ˈbwɛt̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈbwɛt̪ə̯ → ˈbwɛt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈbwɛt̪ → bwɛt̪   (ˈɛ→ɛ)
1400: wɛ becomes wa
    bwɛt̪ → bwat̪   (ɛ→a)
```

## doit

`d̪ˈeːbet̪` → `d̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪eː.bet̪ → ˈd̪eː.bɛt̪   (e→ɛ)
-100: b lenites to β intervocalically / before a sonorant
    ˈd̪eː.bɛt̪ → ˈd̪eː.βɛt̪   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪eː.βɛt̪ → ˈd̪e.βɛt̪   (ˈeː→ˈe)
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪e.βɛt̪ → ˈd̪eː.βɛt̪   (ˈe→ˈeː)
600: t/d spirantize word-finally after a vowel
    ˈd̪eː.βɛt̪ → ˈd̪eː.βɛθ   (t̪→θ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪eː.βɛθ → ˈd̪eː.βəθ   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈd̪eː.βəθ → ˈd̪eːβə̯θ   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd̪eːβə̯θ → ˈd̪eːβθ   (ə̯→∅)
600: a dental fricative hardens to a stop after a consonant, word-finally
    ˈd̪eːβθ → ˈd̪eːβt̪   (θ→t̪)
600: a labial consonant becomes t before a voiceless coronal stop
    ˈd̪eːβt̪ → ˈd̪eːt̪t̪   (β→t̪)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈd̪eːt̪t̪ → ˈd̪et̪t̪   (ˈeː→ˈe)
750: a dental stop deletes before another coronal stop
    ˈd̪et̪t̪ → ˈd̪et̪   (t̪→∅)
1400: final obstruents are lost
    ˈd̪et̪ → ˈd̪e   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪e → d̪e   (ˈe→e)
```

## dieu

`d̪ˈeum` → `d̪jø`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪e.um → ˈd̪ɛ.ʊm   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈd̪ɛ.ʊm → ˈd̪ɛ.om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪ɛ.om → ˈd̪ɛ.o   (m→∅)
300: a stressed vowel lengthens before another vowel
    ˈd̪ɛ.o → ˈd̪ɛː.o   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈd̪ɛː.o → ˈd̪i.e̯o   (ˈɛː→ˈie̯)
500: an unstressed back round non-low vowel becomes a glide in hiatus after a stressed vowel
    ˈd̪i.e̯o → ˈd̪ie̯u̯   (o→u̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈd̪ie̯u̯ → ˈd̪jeu̯   (ˈi→j, e̯→ˈe)
1000: ew becomes øw
    ˈd̪jeu̯ → ˈd̪jøu̯   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈd̪jøu̯ → ˈd̪jø   (u̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪jø → d̪jø   (ˈø→ø)
```

## Dijon

`d̪ˌiːβˈjoːn̪em` → `d̪i.ʒɔ̃`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌd̪iːˈβjoː.n̪em → ˌd̪iːβˈʝoː.n̪em   (j→ʝ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌd̪iːβˈʝoː.n̪em → ˌd̪iːβˈʝoː.n̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌd̪iːβˈʝoː.n̪ɛm → ˌd̪iβˈʝo.n̪ɛm   (ˌiː→ˌi, ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌd̪iβˈʝo.n̪ɛm → ˌd̪iβˈʝo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌd̪iβˈʝo.n̪ɛ → ˌd̪iβˈʝoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌd̪iβˈʝoː.n̪ɛ → ˌd̪iβˈʝũː.n̪ɛ   (ˈoː→ˈũː)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˌd̪iβˈʝũː.n̪ɛ → ˌd̪iβˈɟũː.n̪ɛ   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˌd̪iβˈɟũː.n̪ɛ → ˌd̪iβˈd͡ʒũː.n̪ɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌd̪iβˈd͡ʒũː.n̪ɛ → ˌd̪iβˈd͡ʒũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌd̪iβˈd͡ʒũː.n̪ə → ˌd̪iβˈd͡ʒũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌd̪iβˈd͡ʒũːn̪ə̯ → ˌd̪iβˈd͡ʒũːn̪   (ə̯→∅)
600: a labial consonant becomes d before a voiced coronal stop
    ˌd̪iβˈd͡ʒũːn̪ → ˌd̪iˈd̪d͡ʒũːn̪   (β→d̪)
750: vowel length resets to short
    ˌd̪iˈd̪d͡ʒũːn̪ → ˌd̪iˈd̪d͡ʒũn̪   (ˈũː→ˈũ)
750: a dental stop deletes before another coronal stop
    ˌd̪iˈd̪d͡ʒũn̪ → ˌd̪iˈd͡ʒũn̪   (d̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˌd̪iˈd͡ʒũn̪ → ˌd̪iˈʒũn̪   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌd̪iˈʒũn̪ → ˌd̪iˈʒũː   (ˈũn̪→ˈũː)
1400: stress is leveled — no longer distinctive for vowels
    ˌd̪iˈʒũː → d̪i.ʒũː   (ˌi→i, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    d̪i.ʒũː → d̪i.ʒũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    d̪i.ʒũ → d̪i.ʒɔ̃   (ũ→ɔ̃)
```

## dort

`d̪ˈormit̪` → `d̪ɔʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪or.mit̪ → ˈd̪ɔr.mɪt̪   (ˈo→ˈɔ, i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈd̪ɔr.mɪt̪ → ˈd̪ɔr.met̪   (ɪ→e)
600: t/d spirantize word-finally after a vowel
    ˈd̪ɔr.met̪ → ˈd̪ɔr.meθ   (t̪→θ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪ɔr.meθ → ˈd̪ɔr.məθ   (e→ə)
600: schwa becomes non-syllabic
    ˈd̪ɔr.məθ → ˈd̪ɔrmə̯θ   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd̪ɔrmə̯θ → ˈd̪ɔrmθ   (ə̯→∅)
600: a dental fricative hardens to a stop after a consonant, word-finally
    ˈd̪ɔrmθ → ˈd̪ɔrmt̪   (θ→t̪)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈd̪ɔrmt̪ → ˈd̪ɔrt̪   (m→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈd̪ɔrt̪ → ˈd̪ɔɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈd̪ɔɹt̪ → ˈd̪ɔɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈd̪ɔɹ → ˈd̪ɔr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈd̪ɔr → ˈd̪ɔʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪ɔʀ → d̪ɔʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    d̪ɔʀ → d̪ɔʁ   (ʀ→ʁ)
```

## durs

`d̪ˈuːroːs` → `d̪yʁ`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪uː.roːs → ˈd̪u.ros   (ˈuː→ˈu, oː→o)
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪u.ros → ˈd̪uː.ros   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈd̪uː.ros → ˈd̪ʉː.ros   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪ʉː.ros → ˈd̪ʉː.rəs   (o→ə)
600: schwa becomes non-syllabic
    ˈd̪ʉː.rəs → ˈd̪ʉːrə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd̪ʉːrə̯s → ˈd̪ʉːrs   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈd̪ʉːrs → ˈd̪ʉrs   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈd̪ʉrs → ˈd̪yrs   (ˈʉ→ˈy)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈd̪yrs → ˈd̪yɹs   (r→ɹ)
1400: final obstruents are lost
    ˈd̪yɹs → ˈd̪yɹ   (s→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈd̪yɹ → ˈd̪yr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈd̪yr → ˈd̪yʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪yʀ → d̪yʀ   (ˈy→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    d̪yʀ → d̪yʁ   (ʀ→ʁ)
```

## ive

`ˈekwɑ` → `iɥ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈe.kwɑ → ˈe.kɣʷɑ   (w→ɣʷ)
-100: the labiovelar approximant simplifies to w after a velar consonant
    ˈe.kɣʷɑ → ˈe.kwɑ   (ɣʷ→w)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈe.kwɑ → ˈɛ.kwɑ   (ˈe→ˈɛ)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈɛ.kwɑ → ˈɛː.kwɑ   (ˈɛ→ˈɛː)
500: intervocalic k spirantizes to x before w + glide (qu-)
    ˈɛː.kwɑ → ˈɛː.xwɑ   (k→x)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈɛː.xwɑ → ˈie̯.xwɑ   (ˈɛː→ˈie̯)
500: the low vowel fronts by default
    ˈie̯.xwɑ → ˈie̯.xwa   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈie̯.xwa → ˈie̯.xwʲa   (w→wʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈie̯.xwʲa → ˈie̯.xɥa   (wʲ→ɥ)
600: a voiceless consonant voices intervocalically
    ˈie̯.xɥa → ˈie̯.ɣɥa   (x→ɣ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈie̯.ɣɥa → ˈie̯.ɣɥə   (a→ə)
750: remaining x/ɣ front
    ˈie̯.ɣɥə → ˈie̯.ʝɥə   (ɣ→ʝ)
750: ʝ becomes j everywhere
    ˈie̯.ʝɥə → ˈie̯j.ɥə   (ʝ→j)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈie̯j.ɥə → ˈij.ɥə   (e̯→∅)
1200: schwa desyllabifies after another vowel
    ˈij.ɥə → ˈijɥə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈijɥə̯ → ˈijɥ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈijɥ → ijɥ   (ˈi→i)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    ijɥ → iɥ   (j→∅)
```

## fait

`fˈɑkt̪um` → `fɛ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfɑk.t̪um → ˈfɑk.t̪ʊm   (u→ʊ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈfɑk.t̪ʊm → ˈfɑx.t̪ʊm   (k→x)
-100: lax high vowels lower to tense mid vowels
    ˈfɑx.t̪ʊm → ˈfɑx.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɑx.t̪om → ˈfɑx.t̪o   (m→∅)
500: the low vowel fronts by default
    ˈfɑx.t̪o → ˈfax.t̪o   (ˈɑ→ˈa)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈfax.t̪o → ˈfaç.t̪o   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈfaç.t̪o → ˈfaç.t̪ʲo   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfaç.t̪ʲo → ˈfaç.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈfaç.t̪ʲə → ˈfaçt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfaçt̪ʲə̯ → ˈfaçt̪ʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈfaçt̪ʲ → ˈfaçjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈfaçjt̪ → ˈfaçt̪   (j→∅)
750: ç merges into ʝ
    ˈfaçt̪ → ˈfaʝt̪   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈfaʝt̪ → ˈfajt̪   (ʝ→j)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈfajt̪ → ˈfɛːt̪   (ˈaj→ˈɛː)
1400: final obstruents are lost
    ˈfɛːt̪ → ˈfɛː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɛː → fɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    fɛː → fɛ   (ɛː→ɛ)
```

## fière

`fˈerɑm` → `fjɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfe.rɑm → ˈfɛ.rɑm   (ˈe→ˈɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɛ.rɑm → ˈfɛ.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfɛ.rɑ → ˈfɛː.rɑ   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈfɛː.rɑ → ˈfie̯.rɑ   (ˈɛː→ˈie̯)
500: the low vowel fronts by default
    ˈfie̯.rɑ → ˈfie̯.ra   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfie̯.ra → ˈfie̯.rə   (a→ə)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈfie̯.rə → ˈfje.rə   (ˈi→j, e̯→ˈe)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈfje.rə → ˈfjɛ.rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈfjɛ.rə → ˈfjɛrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈfjɛrə̯ → ˈfjɛr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈfjɛr → ˈfjɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfjɛʀ → fjɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    fjɛʀ → fjɛʁ   (ʀ→ʁ)
```

## fendre

`fˈin̪d̪ere` → `fɑ̃d̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfin̪.d̪e.re → ˈfɪn̪.d̪ɛ.rɛ   (ˈi→ˈɪ, e→ɛ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈfɪn̪.d̪ɛ.rɛ → ˈfen̪.d̪ɛ.rɛ   (ˈɪ→ˈe)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈfen̪.d̪ɛ.rɛ → ˈfen̪.d̪rɛ   (ɛ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfen̪.d̪rɛ → ˈfen̪.d̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈfen̪.d̪rə → ˈfen̪d̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfen̪d̪rə̯ → ˈfen̪d̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈfen̪d̪r → ˈfen̪.d̪rə   (∅→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈfen̪.d̪rə → ˈfẽn̪.d̪rə   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈfẽn̪.d̪rə → ˈfɛ̃n̪.d̪rə   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈfɛ̃n̪.d̪rə → ˈfãn̪.d̪rə   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈfãn̪.d̪rə → ˈfãː.d̪rə   (ˈãn̪→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈfãː.d̪rə → ˈfãːd̪rə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈfãːd̪rə̯ → ˈfɑ̃ːd̪rə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈfɑ̃ːd̪rə̯ → ˈfɑ̃ːd̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈfɑ̃ːd̪r → ˈfɑ̃ːd̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɑ̃ːd̪ʀ → fɑ̃ːd̪ʀ   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    fɑ̃ːd̪ʀ → fɑ̃d̪ʀ   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    fɑ̃d̪ʀ → fɑ̃d̪ʁ   (ʀ→ʁ)
```

## feuille

`fˈoliɑ` → `fœj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfo.li.ɑ → ˈfɔ.lɪ.ɑ   (ˈo→ˈɔ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈfɔ.lɪ.ɑ → ˈfɔ.ljɑ   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˈfɔ.ljɑ → ˈfɔ.ɫjɑ   (l→ɫ)
-100: yod strengthens before a vowel
    ˈfɔ.ɫjɑ → ˈfɔɫ.ʝɑ   (j→ʝ)
300: l palatalizes to ʎ before yod
    ˈfɔɫ.ʝɑ → ˈfɔ.ʎɑ   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfɔ.ʎɑ → ˈfɔː.ʎɑ   (ˈɔ→ˈɔː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈfɔː.ʎɑ → ˈfuo̯.ʎɑ   (ˈɔː→ˈuo̯)
500: the low vowel fronts by default
    ˈfuo̯.ʎɑ → ˈfuo̯.ʎa   (ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˈfuo̯.ʎa → ˈfʉo̯.ʎa   (ˈu→ˈʉ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfʉo̯.ʎa → ˈfʉo̯.ʎə   (a→ə)
1000: high round back vowels front (completion of u-fronting)
    ˈfʉo̯.ʎə → ˈfyo̯.ʎə   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈfyo̯.ʎə → ˈfye̯.ʎə   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈfye̯.ʎə → ˈfø.ʎə   (ˈye̯→ˈø)
1400: final ə becomes a non-syllabic off-glide
    ˈfø.ʎə → ˈføʎə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈføʎə̯ → ˈføʎ   (ə̯→∅)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈføʎ → ˈfœʎ   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfœʎ → fœʎ   (ˈœ→œ)
1400: ʎ becomes j
    fœʎ → fœj   (ʎ→j)
```

## fosse

`fˈossɑm` → `fos`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfos.sɑm → ˈfɔs.sɑm   (ˈo→ˈɔ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɔs.sɑm → ˈfɔs.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈfɔs.sɑ → ˈfɔs.sa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfɔs.sa → ˈfɔs.sə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈfɔs.sə → ˈfɔ.sə   (s→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈfɔ.sə → ˈfɔsə̯   (ə→ə̯)
1400: o stays close in fosse (lexical o/ɔ split)
    ˈfɔsə̯ → ˈfosə̯   (ˈɔ→ˈo)
1400: the final off-glide schwa is deleted elsewhere
    ˈfosə̯ → ˈfos   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfos → fos   (ˈo→o)
```

## fruit

`frˈuːkt̪um` → `fʁɥi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfruːk.t̪um → ˈfruːk.t̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈfruːk.t̪ʊm → ˈfruk.t̪ʊm   (ˈuː→ˈu)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈfruk.t̪ʊm → ˈfrux.t̪ʊm   (k→x)
-100: lax high vowels lower to tense mid vowels
    ˈfrux.t̪ʊm → ˈfrux.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfrux.t̪om → ˈfrux.t̪o   (m→∅)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈfrux.t̪o → ˈfruç.t̪o   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈfruç.t̪o → ˈfruç.t̪ʲo   (t̪→t̪ʲ)
500: a high tense round non-nasal vowel centralizes
    ˈfruç.t̪ʲo → ˈfrʉç.t̪ʲo   (ˈu→ˈʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfrʉç.t̪ʲo → ˈfrʉç.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈfrʉç.t̪ʲə → ˈfrʉçt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfrʉçt̪ʲə̯ → ˈfrʉçt̪ʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈfrʉçt̪ʲ → ˈfrʉçjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈfrʉçjt̪ → ˈfrʉçt̪   (j→∅)
750: ç merges into ʝ
    ˈfrʉçt̪ → ˈfrʉʝt̪   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈfrʉʝt̪ → ˈfrʉjt̪   (ʝ→j)
1000: high round back vowels front (completion of u-fronting)
    ˈfrʉjt̪ → ˈfryjt̪   (ˈʉ→ˈy)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˈfryjt̪ → ˈfrɥit̪   (ˈy→ɥ, j→ˈi)
1400: final obstruents are lost
    ˈfrɥit̪ → ˈfrɥi   (t̪→∅)
1400: r becomes uvular ʀ
    ˈfrɥi → ˈfʀɥi   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfʀɥi → fʀɥi   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    fʀɥi → fʁɥi   (ʀ→ʁ)
```

## joue

`gˈɑwt̪ɑ` → `ʒud̪`

```
500: the low vowel fronts by default
    ˈgɑw.t̪ɑ → ˈgaw.t̪a   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈgaw.t̪a → ˈgʲaw.t̪a   (g→gʲ)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈgʲaw.t̪a → ˈgʲɔw.t̪a   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈgʲɔw.t̪a → ˈɟɔw.t̪a   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟɔw.t̪a → ˈd͡ʒɔw.t̪a   (ɟ→d͡ʒ)
600: a voiceless consonant voices intervocalically
    ˈd͡ʒɔw.t̪a → ˈd͡ʒɔw.d̪a   (t̪→d̪)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd͡ʒɔw.d̪a → ˈd͡ʒɔw.d̪ə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒɔw.d̪ə → ˈʒɔw.d̪ə   (d͡ʒ→ʒ)
1200: the ow diphthong monophthongizes to u
    ˈʒɔw.d̪ə → ˈʒu.d̪ə   (ˈɔw→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈʒu.d̪ə → ˈʒud̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʒud̪ə̯ → ˈʒud̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒud̪ → ʒud̪   (ˈu→u)
```

## grand

`grˈɑn̪d̪em` → `gʁɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgrɑn̪.d̪em → ˈgrɑn̪.d̪ɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgrɑn̪.d̪ɛm → ˈgrɑn̪.d̪ɛ   (m→∅)
500: the low vowel fronts by default
    ˈgrɑn̪.d̪ɛ → ˈgran̪.d̪ɛ   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈgran̪.d̪ɛ → ˈgran̪.d̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈgran̪.d̪ə → ˈgran̪d̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈgran̪d̪ə̯ → ˈgran̪d̪   (ə̯→∅)
750: all final obstruents devoice
    ˈgran̪d̪ → ˈgran̪t̪   (d̪→t̪)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈgran̪t̪ → ˈgrãn̪t̪   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈgrãn̪t̪ → ˈgrãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈgrãːt̪ → ˈgrɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈgrɑ̃ːt̪ → ˈgrɑ̃ː   (t̪→∅)
1400: r becomes uvular ʀ
    ˈgrɑ̃ː → ˈgʀɑ̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈgʀɑ̃ː → gʀɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    gʀɑ̃ː → gʀɑ̃   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    gʀɑ̃ → gʁɑ̃   (ʀ→ʁ)
```

## avoir

`hˌɑbˈeːre` → `a.vwaʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌhɑˈbeː.re → ˌhɑˈbeː.rɛ   (e→ɛ)
-100: b lenites to β intervocalically / before a sonorant
    ˌhɑˈbeː.rɛ → ˌhɑˈβeː.rɛ   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌhɑˈβeː.rɛ → ˌhɑˈβe.rɛ   (ˈeː→ˈe)
300: a stressed vowel lengthens before a single consonant + glide
    ˌhɑˈβe.rɛ → ˌhɑˈβeː.rɛ   (ˈe→ˈeː)
500: h lost unconditionally (any remaining h)
    ˌhɑˈβeː.rɛ → ˌɑˈβeː.rɛ   (h→∅)
500: the low vowel fronts by default
    ˌɑˈβeː.rɛ → ˌaˈβeː.rɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌaˈβeː.rɛ → ˌaˈβeː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌaˈβeː.rə → ˌaˈβeːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌaˈβeːrə̯ → ˌaˈβeːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌaˈβeːr → ˌaˈβejr   (ˈeː→ˈej)
600: the remaining bilabial fricative becomes v
    ˌaˈβejr → ˌaˈvejr   (β→v)
1000: stressed e rounds early to o before j, after a voiced labial consonant
    ˌaˈvejr → ˌaˈvojr   (ˈe→ˈo)
1000: j lowers to ɛ̯ before r, in a back round diphthong
    ˌaˈvojr → ˌaˈvoɛ̯r   (j→ɛ̯)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌaˈvoɛ̯r → ˌaˈvuɛ̯r   (ˈo→ˈu)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌaˈvuɛ̯r → ˌaˈvwɛr   (ˈu→w, ɛ̯→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌaˈvwɛr → ˌaˈvwɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌaˈvwɛɹ → ˌaˈvwɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌaˈvwɛr → ˌaˈvwɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈvwɛʀ → a.vwɛʀ   (ˌa→a, ˈɛ→ɛ)
1400: wɛ becomes wa
    a.vwɛʀ → a.vwaʀ   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    a.vwaʀ → a.vwaʁ   (ʀ→ʁ)
```

## orge

`hˈord̪eum` → `ɔʁʒ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈhor.d̪e.um → ˈhɔr.d̪ɛ.ʊm   (ˈo→ˈɔ, e→ɛ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈhɔr.d̪ɛ.ʊm → ˈhɔr.d̪jʊm   (ɛ→j)
-100: yod strengthens before a vowel
    ˈhɔr.d̪jʊm → ˈhɔr.d̪ʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈhɔr.d̪ʝʊm → ˈhɔr.d̪ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈhɔr.d̪ʝom → ˈhɔr.d̪ʝo   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈhɔr.d̪ʝo → ˈhɔr.ɟʝo   (d̪→ɟ)
300: yod absorbed into a preceding palatalized consonant
    ˈhɔr.ɟʝo → ˈhɔr.ɟo   (ʝ→∅)
500: h lost unconditionally (any remaining h)
    ˈhɔr.ɟo → ˈɔr.ɟo   (h→∅)
500: a palatal stop affricates
    ˈɔr.ɟo → ˈɔr.d͡ʒo   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈɔr.d͡ʒo → ˈɔr.d͡ʒə   (o→ə)
600: schwa becomes non-syllabic
    ˈɔr.d͡ʒə → ˈɔrd͡ʒə̯   (ə→ə̯)
600: non-syllabic schwa restores after a postalveolar affricate
    ˈɔrd͡ʒə̯ → ˈɔr.d͡ʒə   (ə̯→ə)
1000: all affricates become sibilants (deaffrication)
    ˈɔr.d͡ʒə → ˈɔr.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈɔr.ʒə → ˈɔrʒə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈɔrʒə̯ → ˈɔɹʒə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈɔɹʒə̯ → ˈɔɹʒ   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈɔɹʒ → ˈɔrʒ   (ɹ→r)
1400: r becomes uvular ʀ
    ˈɔrʒ → ˈɔʀʒ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈɔʀʒ → ɔʀʒ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ɔʀʒ → ɔʁʒ   (ʀ→ʁ)
```

## jeune

`ˈjuwen̪em` → `ʒœn̪`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈju.we.n̪em → ˈʝu.ɣʷe.n̪em   (j→ʝ, w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈʝu.ɣʷe.n̪em → ˈʝʊ.ɣʷɛ.n̪ɛm   (ˈu→ˈʊ, e→ɛ, e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈʝʊ.ɣʷɛ.n̪ɛm → ˈʝʊ.βʷɛ.n̪ɛm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈʝʊ.βʷɛ.n̪ɛm → ˈʝo.βʷɛ.n̪ɛm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈʝo.βʷɛ.n̪ɛm → ˈʝo.βʷɛ.n̪ɛ   (m→∅)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈʝo.βʷɛ.n̪ɛ → ˈʝo.βʷn̪ɛ   (ɛ→∅)
500: labialized bilabial fricatives delabialize
    ˈʝo.βʷn̪ɛ → ˈʝo.βn̪ɛ   (βʷ→β)
600: yod hardens to ɟ word-initially before a vowel
    ˈʝo.βn̪ɛ → ˈɟo.βn̪ɛ   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟo.βn̪ɛ → ˈd͡ʒo.βn̪ɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd͡ʒo.βn̪ɛ → ˈd͡ʒo.βn̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈd͡ʒo.βn̪ə → ˈd͡ʒoβn̪ə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈd͡ʒoβn̪ə̯ → ˈd͡ʒo.βn̪ə   (ə̯→ə)
600: the bilabial fricative becomes w before a nasal consonant
    ˈd͡ʒo.βn̪ə → ˈd͡ʒow.n̪ə   (β→w)
1000: stressed o becomes e before a high back round glide
    ˈd͡ʒow.n̪ə → ˈd͡ʒew.n̪ə   (ˈo→ˈe)
1000: ew becomes øw
    ˈd͡ʒew.n̪ə → ˈd͡ʒøw.n̪ə   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈd͡ʒøw.n̪ə → ˈd͡ʒø.n̪ə   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒø.n̪ə → ˈʒø.n̪ə   (d͡ʒ→ʒ)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈʒø.n̪ə → ˈʒø̃.n̪ə   (ˈø→ˈø̃)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈʒø̃.n̪ə → ˈʒø.n̪ə   (ˈø̃→ˈø)
1400: final ə becomes a non-syllabic off-glide
    ˈʒø.n̪ə → ˈʒøn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʒøn̪ə̯ → ˈʒøn̪   (ə̯→∅)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈʒøn̪ → ˈʒœn̪   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒœn̪ → ʒœn̪   (ˈœ→œ)
```

## cieux

`kˈae̯loːs` → `sjø`

```
-100: low vowel backs by default
    ˈkae̯.loːs → ˈkɑe̯.loːs   (ˈa→ˈɑ)
-100: low vowel re-fronts before the e-glide
    ˈkɑe̯.loːs → ˈkae̯.loːs   (ˈɑ→ˈa)
-100: the length feature is dropped now that quality carries the contrast
    ˈkae̯.loːs → ˈkae̯.los   (oː→o)
-100: the ae diphthong monophthongizes to ɛ, preserving any stress mark
    ˈkae̯.los → ˈkɛ.los   (ˈae̯→ˈɛ)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈkɛ.los → ˈkʲɛ.los   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkʲɛ.los → ˈcɛ.los   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˈcɛ.los → ˈcɛː.los   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈcɛː.los → ˈcie̯.los   (ˈɛː→ˈie̯)
500: a palatal stop affricates
    ˈcie̯.los → ˈt͡sʲie̯.los   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡sʲie̯.los → ˈt͡sʲie̯.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡sʲie̯.ləs → ˈt͡sʲie̯lə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡sʲie̯lə̯s → ˈt͡sʲie̯ls   (ə̯→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈt͡sʲie̯ls → ˈt͡sʲie̯ɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˈt͡sʲie̯ɫs → ˈt͡sʲie̯ws   (ɫ→w)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt͡sʲie̯ws → ˈt͡sʲjews   (ˈi→j, e̯→ˈe)
1000: ew becomes øw
    ˈt͡sʲjews → ˈt͡sʲjøws   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈt͡sʲjøws → ˈt͡sʲjøs   (w→∅)
1000: a primary-stressed vowel lengthens before word-final s
    ˈt͡sʲjøs → ˈt͡sʲjøːs   (ˈø→ˈøː)
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲjøːs → ˈsʲjøːs   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲjøːs → ˈsjøːs   (sʲ→s)
1400: final obstruents are lost
    ˈsjøːs → ˈsjøː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsjøː → sjøː   (ˈøː→øː)
1400: distinctive vowel length is lost entirely
    sjøː → sjø   (øː→ø)
```

## chemise

`kˌɑmˈiːsiɑm` → `ʃə.miz`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkɑˈmiː.si.ɑm → ˌkɑˈmiː.sɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌkɑˈmiː.sɪ.ɑm → ˌkɑˈmiː.sjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌkɑˈmiː.sjɑm → ˌkɑˈmiːs.ʝɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkɑˈmiːs.ʝɑm → ˌkɑˈmis.ʝɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkɑˈmis.ʝɑm → ˌkɑˈmis.ʝɑ   (m→∅)
500: a voiceless fricative voices before yod + a non-consonantal segment
    ˌkɑˈmis.ʝɑ → ˌkɑˈmiz.ʝɑ   (s→z)
500: z + yod becomes palatalized z
    ˌkɑˈmiz.ʝɑ → ˌkɑˈmi.zʲɑ   (zʝ→zʲ)
500: the low vowel fronts by default
    ˌkɑˈmi.zʲɑ → ˌkaˈmi.zʲa   (ˌɑ→ˌa, ɑ→a)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌkaˈmi.zʲa → ˌkaˈmiː.zʲa   (ˈi→ˈiː)
500: the high back consonant w fronts before a front vowel
    ˌkaˈmiː.zʲa → ˌkʲaˈmiː.zʲa   (k→kʲ)
500: secondary-stressed a becomes ɛ after a front consonant, before a nasal + long vowel
    ˌkʲaˈmiː.zʲa → ˌkʲɛˈmiː.zʲa   (ˌa→ˌɛ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌkʲɛˈmiː.zʲa → ˌcɛˈmiː.zʲa   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˌcɛˈmiː.zʲa → ˌt͡ʃɛˈmiː.zʲa   (c→t͡ʃ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌt͡ʃɛˈmiː.zʲa → ˌt͡ʃɛˈmiːj.za   (zʲ→jz)
600: a vowel shortens before a consonant cluster ending in an obstruent (recurrence)
    ˌt͡ʃɛˈmiːj.za → ˌt͡ʃɛˈmij.za   (ˈiː→ˈi)
600: secondary-stressed ɛ raises to e before any two segments
    ˌt͡ʃɛˈmij.za → ˌt͡ʃeˈmij.za   (ˌɛ→ˌe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌt͡ʃeˈmij.za → ˌt͡ʃeˈmij.zə   (a→ə)
750: j deletes after a high front tense vowel
    ˌt͡ʃeˈmij.zə → ˌt͡ʃeˈmi.zə   (j→∅)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌt͡ʃeˈmi.zə → ˌt͡ʃəˈmi.zə   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌt͡ʃəˈmi.zə → ˌt͡ʃə̃ˈmi.zə   (ˌə→ˌə̃)
1000: all affricates become sibilants (deaffrication)
    ˌt͡ʃə̃ˈmi.zə → ˌʃə̃ˈmi.zə   (t͡ʃ→ʃ)
1400: final ə becomes a non-syllabic off-glide
    ˌʃə̃ˈmi.zə → ˌʃə̃ˈmizə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌʃə̃ˈmizə̯ → ˌʃə̃ˈmiz   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌʃə̃ˈmiz → ʃə̃.miz   (ˌə̃→ə̃, ˈi→i)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    ʃə̃.miz → ʃə.miz   (ə̃→ə)
```

## chenu

`kˌɑːn̪ˈuːt̪um` → `ʃə.n̪y`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkɑːˈn̪uː.t̪um → ˌkɑːˈn̪uː.t̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkɑːˈn̪uː.t̪ʊm → ˌkɑˈn̪u.t̪ʊm   (ˌɑː→ˌɑ, ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˌkɑˈn̪u.t̪ʊm → ˌkɑˈn̪u.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkɑˈn̪u.t̪om → ˌkɑˈn̪u.t̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌkɑˈn̪u.t̪o → ˌkɑˈn̪uː.t̪o   (ˈu→ˈuː)
500: the low vowel fronts by default
    ˌkɑˈn̪uː.t̪o → ˌkaˈn̪uː.t̪o   (ˌɑ→ˌa)
500: a high tense round non-nasal vowel centralizes
    ˌkaˈn̪uː.t̪o → ˌkaˈn̪ʉː.t̪o   (ˈuː→ˈʉː)
500: the high back consonant w fronts before a front vowel
    ˌkaˈn̪ʉː.t̪o → ˌkʲaˈn̪ʉː.t̪o   (k→kʲ)
500: secondary-stressed a becomes ɛ after a front consonant, before a nasal + long vowel
    ˌkʲaˈn̪ʉː.t̪o → ˌkʲɛˈn̪ʉː.t̪o   (ˌa→ˌɛ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌkʲɛˈn̪ʉː.t̪o → ˌcɛˈn̪ʉː.t̪o   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˌcɛˈn̪ʉː.t̪o → ˌt͡ʃɛˈn̪ʉː.t̪o   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt͡ʃɛˈn̪ʉː.t̪o → ˌt͡ʃɛˈn̪ʉː.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌt͡ʃɛˈn̪ʉː.t̪ə → ˌt͡ʃɛˈn̪ʉːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt͡ʃɛˈn̪ʉːt̪ə̯ → ˌt͡ʃɛˈn̪ʉːt̪   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌt͡ʃɛˈn̪ʉːt̪ → ˌt͡ʃeˈn̪ʉːt̪   (ˌɛ→ˌe)
750: a word-final stop re-opens to a fricative after a vowel
    ˌt͡ʃeˈn̪ʉːt̪ → ˌt͡ʃeˈn̪ʉːθ   (t̪→θ)
750: vowel length resets to short
    ˌt͡ʃeˈn̪ʉːθ → ˌt͡ʃeˈn̪ʉθ   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˌt͡ʃeˈn̪ʉθ → ˌt͡ʃeˈn̪yθ   (ˈʉ→ˈy)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌt͡ʃeˈn̪yθ → ˌt͡ʃəˈn̪yθ   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌt͡ʃəˈn̪yθ → ˌt͡ʃə̃ˈn̪yθ   (ˌə→ˌə̃)
1000: the interdental fricatives (plain and palatalized) efface
    ˌt͡ʃə̃ˈn̪yθ → ˌt͡ʃə̃ˈn̪y   (θ→∅)
1000: all affricates become sibilants (deaffrication)
    ˌt͡ʃə̃ˈn̪y → ˌʃə̃ˈn̪y   (t͡ʃ→ʃ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʃə̃ˈn̪y → ʃə̃.n̪y   (ˌə̃→ə̃, ˈy→y)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    ʃə̃.n̪y → ʃə.n̪y   (ə̃→ə)
```

## chartre

`kˈɑrkerem` → `ʃaʁt̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑr.ke.rem → ˈkɑr.kɛ.rɛm   (e→ɛ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑr.kɛ.rɛm → ˈkɑr.kɛ.rɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈkɑr.kɛ.rɛ → ˈkɑr.kʲɛ.rɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkɑr.kʲɛ.rɛ → ˈkɑr.cɛ.rɛ   (kʲ→c)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈkɑr.cɛ.rɛ → ˈkɑr.crɛ   (ɛ→∅)
500: a palatal stop becomes a dental fricative before a non-front consonant
    ˈkɑr.crɛ → ˈkɑr.t̪rɛ   (c→t̪)
500: the low vowel fronts by default
    ˈkɑr.t̪rɛ → ˈkar.t̪rɛ   (ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˈkar.t̪rɛ → ˈkʲar.t̪rɛ   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲar.t̪rɛ → ˈcar.t̪rɛ   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcar.t̪rɛ → ˈt͡ʃar.t̪rɛ   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃar.t̪rɛ → ˈt͡ʃar.t̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃar.t̪rə → ˈt͡ʃart̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃart̪rə̯ → ˈt͡ʃart̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈt͡ʃart̪r → ˈt͡ʃar.t̪rə   (∅→ə)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃar.t̪rə → ˈʃar.t̪rə   (t͡ʃ→ʃ)
1400: final ə becomes a non-syllabic off-glide
    ˈʃar.t̪rə → ˈʃart̪rə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈʃart̪rə̯ → ˈʃaɹt̪rə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃaɹt̪rə̯ → ˈʃaɹt̪r   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈʃaɹt̪r → ˈʃart̪r   (ɹ→r)
1400: r becomes uvular ʀ
    ˈʃart̪r → ˈʃaʀt̪ʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃaʀt̪ʀ → ʃaʀt̪ʀ   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃaʀt̪ʀ → ʃaʁt̪ʁ   (ʀ→ʁ, ʀ→ʁ)
```

## Chartres

`kˈɑrt̪un̪eːs` → `ʃaʁt̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑr.t̪u.n̪eːs → ˈkɑr.t̪ʊ.n̪eːs   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈkɑr.t̪ʊ.n̪eːs → ˈkɑr.t̪ʊ.n̪es   (eː→e)
-100: lax high vowels lower to tense mid vowels
    ˈkɑr.t̪ʊ.n̪es → ˈkɑr.t̪o.n̪es   (ʊ→o)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈkɑr.t̪o.n̪es → ˈkɑr.t̪ũ.n̪es   (o→ũ)
500: the low vowel fronts by default
    ˈkɑr.t̪ũ.n̪es → ˈkar.t̪ũ.n̪es   (ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˈkar.t̪ũ.n̪es → ˈkʲar.t̪ũ.n̪es   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲar.t̪ũ.n̪es → ˈcar.t̪ũ.n̪es   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcar.t̪ũ.n̪es → ˈt͡ʃar.t̪ũ.n̪es   (c→t͡ʃ)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈt͡ʃar.t̪ũ.n̪es → ˈt͡ʃar.t̪ə.n̪es   (ũ→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃar.t̪ə.n̪es → ˈt͡ʃar.t̪ə.n̪əs   (e→ə)
600: a coronal sonorant becomes a tap between (velar+schwa) and (schwa + optional s + word end)
    ˈt͡ʃar.t̪ə.n̪əs → ˈt͡ʃar.t̪ə.ɾəs   (n̪→ɾ)
600: schwa becomes non-syllabic
    ˈt͡ʃar.t̪ə.ɾəs → ˈt͡ʃart̪ə̯ɾə̯s   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃart̪ə̯ɾə̯s → ˈt͡ʃart̪ɾs   (ə̯ɾə̯→ɾ)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈt͡ʃart̪ɾs → ˈt͡ʃar.t̪ɾəs   (∅→ə)
600: a tap hardens to the trill
    ˈt͡ʃar.t̪ɾəs → ˈt͡ʃar.t̪rəs   (ɾ→r)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃar.t̪rəs → ˈʃar.t̪rəs   (t͡ʃ→ʃ)
1200: a single final consonant effaces after schwa
    ˈʃar.t̪rəs → ˈʃar.t̪rə   (s→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈʃar.t̪rə → ˈʃart̪rə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈʃart̪rə̯ → ˈʃaɹt̪rə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃaɹt̪rə̯ → ˈʃaɹt̪r   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈʃaɹt̪r → ˈʃart̪r   (ɹ→r)
1400: r becomes uvular ʀ
    ˈʃart̪r → ˈʃaʀt̪ʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃaʀt̪ʀ → ʃaʀt̪ʀ   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃaʀt̪ʀ → ʃaʁt̪ʁ   (ʀ→ʁ, ʀ→ʁ)
```

## chou

`kˈɑwlis` → `ʃɔl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑw.lis → ˈkɑw.lɪs   (i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈkɑw.lɪs → ˈkɑw.les   (ɪ→e)
500: the low vowel fronts by default
    ˈkɑw.les → ˈkaw.les   (ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˈkaw.les → ˈkʲaw.les   (k→kʲ)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈkʲaw.les → ˈkʲɔw.les   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲɔw.les → ˈcɔw.les   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcɔw.les → ˈt͡ʃɔw.les   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃɔw.les → ˈt͡ʃɔw.ləs   (e→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃɔw.ləs → ˈt͡ʃɔwlə̯s   (ə→ə̯)
600: non-syllabic schwa restores after a non-lateral consonant + l, before a consonant
    ˈt͡ʃɔwlə̯s → ˈt͡ʃɔw.ləs   (ə̯→ə)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈt͡ʃɔw.ləs → ˈt͡ʃɔ.ləs   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃɔ.ləs → ˈʃɔ.ləs   (t͡ʃ→ʃ)
1200: a single final consonant effaces after schwa
    ˈʃɔ.ləs → ˈʃɔ.lə   (s→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈʃɔ.lə → ˈʃɔlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃɔlə̯ → ˈʃɔl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃɔl → ʃɔl   (ˈɔ→ɔ)
```

## cerf

`kˈerwum` → `sɛʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈke.rwum → ˈker.ɣʷum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈker.ɣʷum → ˈkɛr.ɣʷʊm   (ˈe→ˈɛ, u→ʊ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈkɛr.ɣʷʊm → ˈkɛr.βʷʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈkɛr.βʷʊm → ˈkɛr.βʷom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɛr.βʷom → ˈkɛr.βʷo   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈkɛr.βʷo → ˈkʲɛr.βʷo   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkʲɛr.βʷo → ˈcɛr.βʷo   (kʲ→c)
500: labialized bilabial fricatives delabialize
    ˈcɛr.βʷo → ˈcɛr.βo   (βʷ→β)
500: a palatal stop affricates
    ˈcɛr.βo → ˈt͡sʲɛr.βo   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡sʲɛr.βo → ˈt͡sʲɛr.βə   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡sʲɛr.βə → ˈt͡sʲɛrβə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡sʲɛrβə̯ → ˈt͡sʲɛrβ   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˈt͡sʲɛrβ → ˈt͡sʲɛrv   (β→v)
750: all final obstruents devoice
    ˈt͡sʲɛrv → ˈt͡sʲɛrf   (v→f)
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲɛrf → ˈsʲɛrf   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲɛrf → ˈsɛrf   (sʲ→s)
1400: cerf loses its final f (silent, unlike boeuf)
    ˈsɛrf → ˈsɛr   (f→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsɛr → ˈsɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsɛɹ → ˈsɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsɛr → ˈsɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛʀ → sɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɛʀ → sɛʁ   (ʀ→ʁ)
```

## clair

`klˈɑːrum` → `klɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈklɑː.rum → ˈklɑː.rʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈklɑː.rʊm → ˈklɑ.rʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˈklɑ.rʊm → ˈklɑ.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈklɑ.rom → ˈklɑ.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈklɑ.ro → ˈklɑː.ro   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈklɑː.ro → ˈklaː.ro   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈklaː.ro → ˈklaː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈklaː.rə → ˈklaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈklaːrə̯ → ˈklaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈklaːr → ˈklae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈklae̯r → ˈkleːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈkleːr → ˈkler   (ˈeː→ˈe)
1400: e/ø lax before an r that closes the syllable
    ˈkler → ˈklɛr   (ˈe→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈklɛr → ˈklɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈklɛɹ → ˈklɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈklɛr → ˈklɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈklɛʀ → klɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    klɛʀ → klɛʁ   (ʀ→ʁ)
```

## coups

`kˈolpoːs` → `ku`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkol.poːs → ˈkɔl.poːs   (ˈo→ˈɔ)
-100: l darkens before a non-lateral consonant
    ˈkɔl.poːs → ˈkɔɫ.poːs   (l→ɫ)
-100: the length feature is dropped now that quality carries the contrast
    ˈkɔɫ.poːs → ˈkɔɫ.pos   (oː→o)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkɔɫ.pos → ˈkɔɫ.pəs   (o→ə)
600: schwa becomes non-syllabic
    ˈkɔɫ.pəs → ˈkɔɫpə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkɔɫpə̯s → ˈkɔɫps   (ə̯→∅)
600: a labial consonant becomes s before s
    ˈkɔɫps → ˈkɔɫss   (p→s)
600: an identical consonant geminate reduces to one, after a consonant or word start
    ˈkɔɫss → ˈkɔɫs   (s→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈkɔɫs → ˈkɔɫt͡sʲ   (s→t͡sʲ)
1000: back dark-l variants vocalize to w
    ˈkɔɫt͡sʲ → ˈkɔwt͡sʲ   (ɫ→w)
1000: all affricates become sibilants (deaffrication)
    ˈkɔwt͡sʲ → ˈkɔwsʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈkɔwsʲ → ˈkɔws   (sʲ→s)
1200: the ow diphthong monophthongizes to u
    ˈkɔws → ˈkus   (ˈɔw→ˈu)
1400: final obstruents are lost
    ˈkus → ˈku   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈku → ku   (ˈu→u)
```

## compagne

`kˌompˈɑːn̪iɑ` → `kɔ̃.paɲ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkomˈpɑː.n̪i.ɑ → ˌkɔmˈpɑː.n̪ɪ.ɑ   (ˌo→ˌɔ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌkɔmˈpɑː.n̪ɪ.ɑ → ˌkɔmˈpɑː.n̪jɑ   (ɪ→j)
-100: yod strengthens before a vowel
    ˌkɔmˈpɑː.n̪jɑ → ˌkɔmˈpɑːn̪.ʝɑ   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkɔmˈpɑːn̪.ʝɑ → ˌkɔmˈpɑn̪.ʝɑ   (ˈɑː→ˈɑ)
300: the coronal nasal palatalizes before yod
    ˌkɔmˈpɑn̪.ʝɑ → ˌkɔmˈpɑ.ɲɑ   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌkɔmˈpɑ.ɲɑ → ˌkɔmˈpɑː.ɲɑ   (ˈɑ→ˈɑː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌkɔmˈpɑː.ɲɑ → ˌkũmˈpɑː.ɲɑ   (ˌɔ→ˌũ)
500: the low vowel fronts by default
    ˌkũmˈpɑː.ɲɑ → ˌkũmˈpaː.ɲa   (ˈɑː→ˈaː, ɑ→a)
600: a vowel shortens before ɲ
    ˌkũmˈpaː.ɲa → ˌkũmˈpa.ɲa   (ˈaː→ˈa)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌkũmˈpa.ɲa → ˌkũmˈpa.ɲə   (a→ə)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌkũmˈpa.ɲə → ˌkũmˈpã.ɲə   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌkũmˈpã.ɲə → ˌkũːˈpã.ɲə   (ˌũm→ˌũː)
1400: final ə becomes a non-syllabic off-glide
    ˌkũːˈpã.ɲə → ˌkũːˈpãɲə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌkũːˈpãɲə̯ → ˌkũːˈpãɲ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌkũːˈpãɲ → kũː.pãɲ   (ˌũː→ũː, ˈã→ã)
1400: distinctive vowel length is lost entirely
    kũː.pãɲ → kũ.pãɲ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    kũ.pãɲ → kɔ̃.pãɲ   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    kɔ̃.pãɲ → kɔ̃.paɲ   (ã→a)
```

## cuir

`kˈorium` → `kɥiʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈko.ri.um → ˈkɔ.rɪ.ʊm   (ˈo→ˈɔ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈkɔ.rɪ.ʊm → ˈkɔ.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈkɔ.rjʊm → ˈkɔr.ʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈkɔr.ʝʊm → ˈkɔr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɔr.ʝom → ˈkɔr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˈkɔr.ʝo → ˈkɔ.rʲo   (rʝ→rʲ)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˈkɔ.rʲo → ˈkɔː.rʲo   (ˈɔ→ˈɔː)
500: long stressed ɛː/ɔː diphthongize (recurrence)
    ˈkɔː.rʲo → ˈkuo̯.rʲo   (ˈɔː→ˈuo̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkuo̯.rʲo → ˈkuo̯.rʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈkuo̯.rʲə → ˈkuo̯rʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkuo̯rʲə̯ → ˈkuo̯rʲ   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˈkuo̯rʲ → ˈkuo̯jrʲ   (∅→j)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈkuo̯jrʲ → ˈkʉo̯jrʲ   (ˈu→ˈʉ)
600: palatalized r depalatalizes
    ˈkʉo̯jrʲ → ˈkʉo̯jr   (rʲ→r)
1000: high round back vowels front (completion of u-fronting)
    ˈkʉo̯jr → ˈkyo̯jr   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈkyo̯jr → ˈkye̯jr   (o̯→e̯)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈkye̯jr → ˈkyjr   (e̯→∅)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˈkyjr → ˈkɥir   (ˈy→ɥ, j→ˈi)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈkɥir → ˈkɥiɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈkɥiɹ → ˈkɥir   (ɹ→r)
1400: r becomes uvular ʀ
    ˈkɥir → ˈkɥiʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkɥiʀ → kɥiʀ   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    kɥiʀ → kɥiʁ   (ʀ→ʁ)
```

## graal

`krˌɑːt̪ˈɑːlem` → `gʁal`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkrɑːˈt̪ɑː.lem → ˌkrɑːˈt̪ɑː.lɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkrɑːˈt̪ɑː.lɛm → ˌkrɑˈt̪ɑ.lɛm   (ˌɑː→ˌɑ, ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkrɑˈt̪ɑ.lɛm → ˌkrɑˈt̪ɑ.lɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌkrɑˈt̪ɑ.lɛ → ˌkrɑˈt̪ɑː.lɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌkrɑˈt̪ɑː.lɛ → ˌkraˈt̪aː.lɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌkraˈt̪aː.lɛ → ˌkraˈt̪aː.lə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌkraˈt̪aː.lə → ˌkraˈt̪aːlə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌkraˈt̪aːlə̯ → ˌkraˈt̪aːl   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌkraˈt̪aːl → ˌkraˈd̪aːl   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌkraˈd̪aːl → ˌkraˈðaːl   (d̪→ð)
600: long stressed vowels diphthongize
    ˌkraˈðaːl → ˌkraˈðae̯l   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌkraˈðae̯l → ˌkraˈðeːl   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌkraˈðeːl → ˌkraˈðel   (ˈeː→ˈe)
1000: word-initial k voices before r/l + a
    ˌkraˈðel → ˌgraˈðel   (k→g)
1000: the interdental fricatives (plain and palatalized) efface
    ˌgraˈðel → ˌgraˈel   (ð→∅)
1400: e lowers to ɛ before a lateral
    ˌgraˈel → ˌgraˈɛl   (ˈe→ˈɛ)
1400: graal levels its aɛ hiatus to a (learned word)
    ˌgraˈɛl → ˌgral   (ˈɛ→∅)
1400: r becomes uvular ʀ
    ˌgral → ˌgʀal   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌgʀal → gʀal   (ˌa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    gʀal → gʁal   (ʀ→ʁ)
```

## crus

`krˈuːd̪oːs` → `kʁy`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈkruː.d̪oːs → ˈkru.d̪os   (ˈuː→ˈu, oː→o)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈkru.d̪os → ˈkru.ðos   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkru.ðos → ˈkruː.ðos   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈkruː.ðos → ˈkrʉː.ðos   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkrʉː.ðos → ˈkrʉː.ðəs   (o→ə)
600: schwa becomes non-syllabic
    ˈkrʉː.ðəs → ˈkrʉːðə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkrʉːðə̯s → ˈkrʉːðs   (ə̯→∅)
600: a dental fricative + s becomes the affricate ts word-finally
    ˈkrʉːðs → ˈkrʉːt͡s   (ðs→t͡s)
750: a word-final stop re-opens to a fricative after a vowel
    ˈkrʉːt͡s → ˈkrʉːs   (t͡s→s)
750: vowel length resets to short
    ˈkrʉːs → ˈkrʉs   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈkrʉs → ˈkrys   (ˈʉ→ˈy)
1000: a primary-stressed vowel lengthens before word-final s
    ˈkrys → ˈkryːs   (ˈy→ˈyː)
1400: final obstruents are lost
    ˈkryːs → ˈkryː   (s→∅)
1400: r becomes uvular ʀ
    ˈkryː → ˈkʀyː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkʀyː → kʀyː   (ˈyː→yː)
1400: distinctive vowel length is lost entirely
    kʀyː → kʀy   (yː→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    kʀy → kʁy   (ʀ→ʁ)
```

## coin

`kˈun̪eum` → `kwɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈku.n̪e.um → ˈkʊ.n̪ɛ.ʊm   (ˈu→ˈʊ, e→ɛ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈkʊ.n̪ɛ.ʊm → ˈkʊ.n̪jʊm   (ɛ→j)
-100: yod strengthens before a vowel
    ˈkʊ.n̪jʊm → ˈkʊn̪.ʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈkʊn̪.ʝʊm → ˈkon̪.ʝom   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkon̪.ʝom → ˈkon̪.ʝo   (m→∅)
300: the coronal nasal palatalizes before yod
    ˈkon̪.ʝo → ˈko.ɲo   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈko.ɲo → ˈkoː.ɲo   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈkoː.ɲo → ˈkũː.ɲo   (ˈoː→ˈũː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkũː.ɲo → ˈkũː.ɲə   (o→ə)
600: schwa becomes non-syllabic
    ˈkũː.ɲə → ˈkũːɲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkũːɲə̯ → ˈkũːɲ   (ə̯→∅)
600: a vowel shortens before ɲ
    ˈkũːɲ → ˈkũɲ   (ˈũː→ˈũ)
1000: word-final ɲ ejects a nasalized j after a tense vowel
    ˈkũɲ → ˈkũj̃ɲ   (∅→j̃)
1000: the nasal diphthong ũj̃ becomes wĩ (syllabicity swap before a nasal)
    ˈkũj̃ɲ → kwj̩̃ɲ   (ˈũ→w, j̃→j̩̃)
1200: final ɲ becomes n
    kwj̩̃ɲ → kwj̩̃n̪   (ɲ→n̪)
1200: nasalized ĩ lowers after w
    kwj̩̃n̪ → kwj̩̃n̪   (j̩̃→j̩̃)
1200: a front unrounded non-low vowel laxes and lowers after w
    kwj̩̃n̪ → kwɛ̃n̪   (j̩̃→ɛ̃)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    kwɛ̃n̪ → kwɛ̃ː   (ɛ̃n̪→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    kwɛ̃ː → kwɛ̃   (ɛ̃ː→ɛ̃)
```

## quant

`kwˈɑn̪t̪um` → `kɑ̃`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈkwɑn̪.t̪um → ˈkɣʷɑn̪.t̪um   (w→ɣʷ)
-100: the labiovelar approximant simplifies to w after a velar consonant
    ˈkɣʷɑn̪.t̪um → ˈkwɑn̪.t̪um   (ɣʷ→w)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkwɑn̪.t̪um → ˈkwɑn̪.t̪ʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkwɑn̪.t̪ʊm → ˈkwɑn̪.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkwɑn̪.t̪om → ˈkwɑn̪.t̪o   (m→∅)
500: the low vowel fronts by default
    ˈkwɑn̪.t̪o → ˈkwan̪.t̪o   (ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˈkwan̪.t̪o → ˈkwʲan̪.t̪o   (w→wʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkwʲan̪.t̪o → ˈkɥan̪.t̪o   (wʲ→ɥ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkɥan̪.t̪o → ˈkɥan̪.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈkɥan̪.t̪ə → ˈkɥan̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkɥan̪t̪ə̯ → ˈkɥan̪t̪   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˈkɥan̪t̪ → ˈkɥɛn̪t̪   (ˈa→ˈɛ)
600: w is lost after k before a front non-low vowel
    ˈkɥɛn̪t̪ → ˈkɛn̪t̪   (ɥ→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈkɛn̪t̪ → ˈkɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈkɛ̃n̪t̪ → ˈkãn̪t̪   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈkãn̪t̪ → ˈkãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈkãːt̪ → ˈkɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈkɑ̃ːt̪ → ˈkɑ̃ː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkɑ̃ː → kɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    kɑ̃ː → kɑ̃   (ɑ̃ː→ɑ̃)
```

## quintaine

`kwˌiːn̪t̪ˈɑːn̪ɑm` → `kɛ̃.t̪ɛn̪`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌkwiːn̪ˈt̪ɑː.n̪ɑm → ˌkɣʷiːn̪ˈt̪ɑː.n̪ɑm   (w→ɣʷ)
-100: the labiovelar approximant simplifies to w after a velar consonant
    ˌkɣʷiːn̪ˈt̪ɑː.n̪ɑm → ˌkwiːn̪ˈt̪ɑː.n̪ɑm   (ɣʷ→w)
-100: the length feature is dropped now that quality carries the contrast
    ˌkwiːn̪ˈt̪ɑː.n̪ɑm → ˌkwin̪ˈt̪ɑ.n̪ɑm   (ˌiː→ˌi, ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkwin̪ˈt̪ɑ.n̪ɑm → ˌkwin̪ˈt̪ɑ.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌkwin̪ˈt̪ɑ.n̪ɑ → ˌkwin̪ˈt̪ɑː.n̪ɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌkwin̪ˈt̪ɑː.n̪ɑ → ˌkwin̪ˈt̪aː.n̪a   (ˈɑː→ˈaː, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˌkwin̪ˈt̪aː.n̪a → ˌkwʲin̪ˈt̪aː.n̪a   (w→wʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌkwʲin̪ˈt̪aː.n̪a → ˌkɥin̪ˈt̪aː.n̪a   (wʲ→ɥ)
600: w is lost after k before a front non-low vowel
    ˌkɥin̪ˈt̪aː.n̪a → ˌkin̪ˈt̪aː.n̪a   (ɥ→∅)
600: long stressed vowels diphthongize
    ˌkin̪ˈt̪aː.n̪a → ˌkin̪ˈt̪ae̯.n̪a   (ˈaː→ˈae̯)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˌkin̪ˈt̪ae̯.n̪a → ˌkin̪ˈt̪aj.n̪a   (e̯→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌkin̪ˈt̪aj.n̪a → ˌkin̪ˈt̪aj.n̪ə   (a→ə)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˌkin̪ˈt̪aj.n̪ə → ˌkin̪ˈt̪aj̃.n̪ə   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌkin̪ˈt̪aj̃.n̪ə → ˌkin̪ˈt̪ãj̃.n̪ə   (ˈa→ˈã)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌkin̪ˈt̪ãj̃.n̪ə → ˌkĩn̪ˈt̪ãj̃.n̪ə   (ˌi→ˌĩ)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌkĩn̪ˈt̪ãj̃.n̪ə → ˌkĩn̪ˈt̪ɛ̃j̃.n̪ə   (ˈã→ˈɛ̃)
1200: nasalized ĩ lowers to ẽ
    ˌkĩn̪ˈt̪ɛ̃j̃.n̪ə → ˌkẽn̪ˈt̪ɛ̃j̃.n̪ə   (ˌĩ→ˌẽ)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌkẽn̪ˈt̪ɛ̃j̃.n̪ə → ˌkẽn̪ˈt̪ɛ̃.n̪ə   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌkẽn̪ˈt̪ɛ̃.n̪ə → ˌkẽːˈt̪ɛ̃.n̪ə   (ˌẽn̪→ˌẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˌkẽːˈt̪ɛ̃.n̪ə → ˌkɛ̃ːˈt̪ɛ̃.n̪ə   (ˌẽː→ˌɛ̃ː)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˌkɛ̃ːˈt̪ɛ̃.n̪ə → ˌkɛ̃ːˈt̪ɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌkɛ̃ːˈt̪ɛ.n̪ə → ˌkɛ̃ːˈt̪ɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌkɛ̃ːˈt̪ɛn̪ə̯ → ˌkɛ̃ːˈt̪ɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌkɛ̃ːˈt̪ɛn̪ → kɛ̃ː.t̪ɛn̪   (ˌɛ̃ː→ɛ̃ː, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    kɛ̃ː.t̪ɛn̪ → kɛ̃.t̪ɛn̪   (ɛ̃ː→ɛ̃)
```

## lacs

`lˈɑkweum` → `la`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈlɑ.kwe.um → ˈlɑ.kɣʷe.um   (w→ɣʷ)
-100: the labiovelar approximant simplifies to w after a velar consonant
    ˈlɑ.kɣʷe.um → ˈlɑ.kwe.um   (ɣʷ→w)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlɑ.kwe.um → ˈlɑ.kwɛ.ʊm   (e→ɛ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈlɑ.kwɛ.ʊm → ˈlɑkw.jʊm   (ɛ→j)
-100: yod strengthens before a vowel
    ˈlɑkw.jʊm → ˈlɑkw.ʝʊm   (j→ʝ)
-100: the rounded glide is lost before the strengthened yod
    ˈlɑkw.ʝʊm → ˈlɑ.kʝʊm   (w→∅)
-100: lax high vowels lower to tense mid vowels
    ˈlɑ.kʝʊm → ˈlɑ.kʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɑ.kʝom → ˈlɑ.kʝo   (m→∅)
-100: k geminates (as palatal cc) intervocalically before yod + vowel
    ˈlɑ.kʝo → ˈlɑc.cʝo   (k→cc)
300: yod absorbed into a preceding palatalized consonant
    ˈlɑc.cʝo → ˈlɑc.co   (ʝ→∅)
500: geminate palatal stop cc becomes t + tsʲ
    ˈlɑc.co → ˈlɑ.t̪t͡sʲo   (c→t̪, c→t͡sʲ)
500: the low vowel fronts by default
    ˈlɑ.t̪t͡sʲo → ˈla.t̪t͡sʲo   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈla.t̪t͡sʲo → ˈla.t̪t͡sʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈla.t̪t͡sʲə → ˈlat̪t͡sʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈlat̪t͡sʲə̯ → ˈlat̪t͡sʲ   (ə̯→∅)
750: a dental stop deletes before another coronal stop
    ˈlat̪t͡sʲ → ˈlat͡sʲ   (t̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈlat͡sʲ → ˈlasʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈlasʲ → ˈlas   (sʲ→s)
1400: final obstruents are lost
    ˈlas → ˈla   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈla → la   (ˈa→a)
```

## laize

`lˈɑt̪iɑm` → `lɛz`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlɑ.t̪i.ɑm → ˈlɑ.t̪ɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈlɑ.t̪ɪ.ɑm → ˈlɑ.t̪jɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈlɑ.t̪jɑm → ˈlɑ.t̪ʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɑ.t̪ʝɑm → ˈlɑ.t̪ʝɑ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈlɑ.t̪ʝɑ → ˈlɑt͡sʲ.ʝɑ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized affricate
    ˈlɑt͡sʲ.ʝɑ → ˈlɑ.t͡sʲɑ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈlɑ.t͡sʲɑ → ˈlɑː.t͡sʲɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈlɑː.t͡sʲɑ → ˈlaː.t͡sʲa   (ˈɑː→ˈaː, ɑ→a)
600: a voiceless consonant voices intervocalically
    ˈlaː.t͡sʲa → ˈlaː.d͡zʲa   (t͡sʲ→d͡zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈlaː.d͡zʲa → ˈlaːj.d͡za   (d͡zʲ→jd͡z)
600: a vowel shortens before a consonant cluster ending in an obstruent (recurrence)
    ˈlaːj.d͡za → ˈlaj.d͡za   (ˈaː→ˈa)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlaj.d͡za → ˈlaj.d͡zə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈlaj.d͡zə → ˈlaj.zə   (d͡z→z)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈlaj.zə → ˈlɛː.zə   (ˈaj→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˈlɛː.zə → ˈlɛːzə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlɛːzə̯ → ˈlɛːz   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlɛːz → lɛːz   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    lɛːz → lɛz   (ɛː→ɛ)
```

## lit

`lˈekt̪um` → `li`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlek.t̪um → ˈlɛk.t̪ʊm   (ˈe→ˈɛ, u→ʊ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈlɛk.t̪ʊm → ˈlɛx.t̪ʊm   (k→x)
-100: lax high vowels lower to tense mid vowels
    ˈlɛx.t̪ʊm → ˈlɛx.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɛx.t̪om → ˈlɛx.t̪o   (m→∅)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈlɛx.t̪o → ˈlɛç.t̪o   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈlɛç.t̪o → ˈlɛç.t̪ʲo   (t̪→t̪ʲ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈlɛç.t̪ʲo → ˈlie̯ç.t̪ʲo   (ˈɛ→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈlie̯ç.t̪ʲo → ˈlie̯ç.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈlie̯ç.t̪ʲə → ˈlie̯çt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈlie̯çt̪ʲə̯ → ˈlie̯çt̪ʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈlie̯çt̪ʲ → ˈlie̯çjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈlie̯çjt̪ → ˈlie̯çt̪   (j→∅)
750: ç merges into ʝ
    ˈlie̯çt̪ → ˈlie̯ʝt̪   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈlie̯ʝt̪ → ˈlie̯jt̪   (ʝ→j)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈlie̯jt̪ → ˈlijt̪   (e̯→∅)
1400: final obstruents are lost
    ˈlijt̪ → ˈlij   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlij → lij   (ˈi→i)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    lij → li   (j→∅)
```

## lien

`lˌigˈɑːmen̪` → `lwa.jɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌliˈgɑː.men̪ → ˌlɪˈgɑː.mɛn̪   (ˌi→ˌɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌlɪˈgɑː.mɛn̪ → ˌlɪˈgɑ.mɛn̪   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌlɪˈgɑ.mɛn̪ → ˌleˈgɑ.mɛn̪   (ˌɪ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌleˈgɑ.mɛn̪ → ˌleˈgɑ.mɛ   (n̪→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌleˈgɑ.mɛ → ˌleˈɣɑ.mɛ   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌleˈɣɑ.mɛ → ˌleˈɣɑː.mɛ   (ˈɑ→ˈɑː)
500: the velar fricative is lost after a tense front-mid vowel before long stressed a
    ˌleˈɣɑː.mɛ → ˌleˈɑː.mɛ   (ɣ→∅)
500: j epenthesized after secondary-stressed e before a low vowel
    ˌleˈɑː.mɛ → ˌleˈjɑː.mɛ   (∅→j)
500: the low vowel fronts by default
    ˌleˈjɑː.mɛ → ˌleˈjaː.mɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌleˈjaː.mɛ → ˌleˈjaː.mə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌleˈjaː.mə → ˌleˈjaːmə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌleˈjaːmə̯ → ˌleˈjaːm   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌleˈjaːm → ˌleˈjɛːm   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌleˈjɛːm → ˌleˈjie̯m   (ˈɛː→ˈie̯)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌleˈjie̯m → ˌləˈjie̯m   (ˌe→ˌə)
1000: secondary-stressed schwa reverts to e before a palatal consonant
    ˌləˈjie̯m → ˌleˈjie̯m   (ˌə→ˌe)
1000: final m dentalizes after a vowel
    ˌleˈjie̯m → ˌleˈjie̯n̪   (m→n̪)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌleˈjie̯n̪ → ˌloˈjie̯n̪   (ˌe→ˌo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌloˈjie̯n̪ → ˌluˈjie̯n̪   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌluˈjie̯n̪ → ˌluˈɛ̯ie̯n̪   (j→ɛ̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌluˈɛ̯ie̯n̪ → ˌluɛ̯ˈjen̪   (ˈi→j, e̯→ˈe)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˌluɛ̯ˈjen̪ → ˌluɛ̯ˈjẽn̪   (ˈe→ˈẽ)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌluɛ̯ˈjẽn̪ → ˌlwɛˈjẽn̪   (ˌu→w, ɛ̯→ˌɛ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌlwɛˈjẽn̪ → ˌlwɛˈjẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˌlwɛˈjẽː → ˌlwɛˈjɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌlwɛˈjɛ̃ː → lwɛ.jɛ̃ː   (ˌɛ→ɛ, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    lwɛ.jɛ̃ː → lwɛ.jɛ̃   (ɛ̃ː→ɛ̃)
1400: wɛ becomes wa
    lwɛ.jɛ̃ → lwa.jɛ̃   (ɛ→a)
```

## lettre

`lˈit̪t̪erɑm` → `lɛt̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlit̪.t̪e.rɑm → ˈlɪt̪.t̪ɛ.rɑm   (ˈi→ˈɪ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈlɪt̪.t̪ɛ.rɑm → ˈlet̪.t̪ɛ.rɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlet̪.t̪ɛ.rɑm → ˈlet̪.t̪ɛ.rɑ   (m→∅)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈlet̪.t̪ɛ.rɑ → ˈlet̪.t̪rɑ   (ɛ→∅)
500: the low vowel fronts by default
    ˈlet̪.t̪rɑ → ˈlet̪.t̪ra   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlet̪.t̪ra → ˈlet̪.t̪rə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈlet̪.t̪rə → ˈle.t̪rə   (t̪→∅)
1000: stressed e laxes to ɛ before an obstruent + non-nasal coronal sonorant + vowel
    ˈle.t̪rə → ˈlɛ.t̪rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈlɛ.t̪rə → ˈlɛt̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlɛt̪rə̯ → ˈlɛt̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈlɛt̪r → ˈlɛt̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈlɛt̪ʀ → lɛt̪ʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    lɛt̪ʀ → lɛt̪ʁ   (ʀ→ʁ)
```

## lundi

`lˌuːn̪isd̪ˈiːem` → `lœ̃.d̪i`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌluː.n̪isˈd̪iː.em → ˌluː.n̪ɪsˈd̪iː.ɛm   (i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌluː.n̪ɪsˈd̪iː.ɛm → ˌlu.n̪ɪsˈd̪i.ɛm   (ˌuː→ˌu, ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌlu.n̪ɪsˈd̪i.ɛm → ˌlu.n̪esˈd̪i.ɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌlu.n̪esˈd̪i.ɛm → ˌlu.n̪esˈd̪i.ɛ   (m→∅)
300: a stressed vowel lengthens before another vowel
    ˌlu.n̪esˈd̪i.ɛ → ˌlu.n̪esˈd̪iː.ɛ   (ˈi→ˈiː)
500: a high tense round non-nasal vowel centralizes
    ˌlu.n̪esˈd̪iː.ɛ → ˌlʉ.n̪esˈd̪iː.ɛ   (ˌu→ˌʉ)
500: an unstressed front non-low vowel becomes a glide in hiatus after a stressed vowel
    ˌlʉ.n̪esˈd̪iː.ɛ → ˌlʉ.n̪esˈd̪iːɪ̯   (ɛ→ɪ̯)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˌlʉ.n̪esˈd̪iːɪ̯ → ˌlʉ.n̪əsˈd̪iːɪ̯   (e→ə)
600: schwa becomes non-syllabic
    ˌlʉ.n̪əsˈd̪iːɪ̯ → ˌlʉn̪ə̯sˈd̪iːɪ̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌlʉn̪ə̯sˈd̪iːɪ̯ → ˌlʉn̪sˈd̪iːɪ̯   (ə̯→∅)
750: vowel length resets to short
    ˌlʉn̪sˈd̪iːɪ̯ → ˌlʉn̪sˈd̪iɪ̯   (ˈiː→ˈi)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌlʉn̪sˈd̪iɪ̯ → ˌlʉn̪ˈd̪iɪ̯   (s→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌlʉn̪ˈd̪iɪ̯ → ˌlyn̪ˈd̪iɪ̯   (ˌʉ→ˌy)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌlyn̪ˈd̪iɪ̯ → ˌlỹn̪ˈd̪iɪ̯   (ˌy→ˌỹ)
1000: a high non-round glide deletes after stressed i
    ˌlỹn̪ˈd̪iɪ̯ → ˌlỹn̪ˈd̪i   (ɪ̯→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌlỹn̪ˈd̪i → ˌlỹːˈd̪i   (ˌỹn̪→ˌỹː)
1400: nasalized front vowels lower (wẽ, jẽ, ø̃ open to wɛ̃, jɛ̃, œ̃)
    ˌlỹːˈd̪i → ˌlœ̃ːˈd̪i   (ˌỹː→ˌœ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌlœ̃ːˈd̪i → lœ̃ː.d̪i   (ˌœ̃ː→œ̃ː, ˈi→i)
1400: distinctive vowel length is lost entirely
    lœ̃ː.d̪i → lœ̃.d̪i   (œ̃ː→œ̃)
```

## malade

`mˌɑloːhˈɑːbit̪oː` → `ma.lad̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmɑ.loːˈhɑː.bi.t̪oː → ˌmɑ.loːˈhɑː.bɪ.t̪oː   (i→ɪ)
-100: h lost word-internally (word-initial h survives at this stage)
    ˌmɑ.loːˈhɑː.bɪ.t̪oː → ˌmɑ.loːˈɑː.bɪ.t̪oː   (h→∅)
-100: b lenites to β intervocalically / before a sonorant
    ˌmɑ.loːˈɑː.bɪ.t̪oː → ˌmɑ.loːˈɑː.βɪ.t̪oː   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɑ.loːˈɑː.βɪ.t̪oː → ˌmɑ.loˈɑ.βɪ.t̪o   (oː→o, ˈɑː→ˈɑ, oː→o)
-100: lax high vowels lower to tense mid vowels
    ˌmɑ.loˈɑ.βɪ.t̪o → ˌmɑ.loˈɑ.βe.t̪o   (ɪ→e)
300: e becomes a schwa-glide between an unrounded labial and a distributed obstruent + non-low vowel
    ˌmɑ.loˈɑ.βe.t̪o → ˌmɑ.loˈɑβə̯.t̪o   (e→ə̯)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɑ.loˈɑβə̯.t̪o → ˌmɑ.loˈɑːβə̯.t̪o   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌmɑ.loˈɑːβə̯.t̪o → ˌma.loˈaːβə̯.t̪o   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌma.loˈaːβə̯.t̪o → ˌma.loˈaːβə̯.t̪ə   (o→ə)
600: an unstressed non-low tense vowel reduces to schwa unconditionally
    ˌma.loˈaːβə̯.t̪ə → ˌma.ləˈaːβə̯.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌma.ləˈaːβə̯.t̪ə → ˌmaˈlə̯aːβə̯t̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˌmaˈlə̯aːβə̯t̪ə̯ → ˌmaˈlə̯aːβə̯.t̪ə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˌmaˈlə̯aːβə̯.t̪ə → ˌmaˈlaːβ.t̪ə   (ˈə̯aːβə̯→ˈaːβ)
600: an anterior coronal voices after a non-high voiced labial consonant, before a non-low vowel
    ˌmaˈlaːβ.t̪ə → ˌmaˈlaːβ.d̪ə   (t̪→d̪)
600: a labial consonant becomes d before a voiced coronal stop
    ˌmaˈlaːβ.d̪ə → ˌmaˈlaːd̪.d̪ə   (β→d̪)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˌmaˈlaːd̪.d̪ə → ˌmaˈlad̪.d̪ə   (ˈaː→ˈa)
750: a dental stop deletes before another coronal stop
    ˌmaˈlad̪.d̪ə → ˌmaˈla.d̪ə   (d̪→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌmaˈla.d̪ə → ˌmaˈlad̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌmaˈlad̪ə̯ → ˌmaˈlad̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmaˈlad̪ → ma.lad̪   (ˌa→a, ˈa→a)
```

## manteau

`mˌɑn̪t̪ˈellum` → `mɑ̃.t̪o`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmɑn̪ˈt̪el.lum → ˌmɑn̪ˈt̪ɛl.lʊm   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˌmɑn̪ˈt̪ɛl.lʊm → ˌmɑn̪ˈt̪ɛl.lom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɑn̪ˈt̪ɛl.lom → ˌmɑn̪ˈt̪ɛl.lo   (m→∅)
500: the low vowel fronts by default
    ˌmɑn̪ˈt̪ɛl.lo → ˌman̪ˈt̪ɛl.lo   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌman̪ˈt̪ɛl.lo → ˌman̪ˈt̪ɛl.lə   (o→ə)
600: schwa becomes non-syllabic
    ˌman̪ˈt̪ɛl.lə → ˌman̪ˈt̪ɛllə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌman̪ˈt̪ɛllə̯ → ˌman̪ˈt̪ɛll   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˌman̪ˈt̪ɛll → ˌman̪ˈt̪ɛl   (l→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌman̪ˈt̪ɛl → ˌmãn̪ˈt̪ɛl   (ˌa→ˌã)
1000: final l labializes after a short mid vowel
    ˌmãn̪ˈt̪ɛl → ˌmãn̪ˈt̪ɛɫ   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˌmãn̪ˈt̪ɛɫ → ˌmãn̪ˈt̪ɛw   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌmãn̪ˈt̪ɛw → ˌmãn̪ˈt̪ɛa̯w   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌmãn̪ˈt̪ɛa̯w → ˌmãn̪ˈt̪e̯aw   (ˈɛ→e̯, a̯→ˈa)
1200: aw becomes long oː
    ˌmãn̪ˈt̪e̯aw → ˌmãn̪ˈt̪e̯oː   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌmãn̪ˈt̪e̯oː → ˌmãn̪ˈt̪ə̯oː   (e̯→ə̯)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmãn̪ˈt̪ə̯oː → ˌmãːˈt̪ə̯oː   (ˌãn̪→ˌãː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌmãːˈt̪ə̯oː → ˌmãːˈt̪oː   (ə̯→∅)
1400: long a becomes back ɑː
    ˌmãːˈt̪oː → ˌmɑ̃ːˈt̪oː   (ˌãː→ˌɑ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɑ̃ːˈt̪oː → mɑ̃ː.t̪oː   (ˌɑ̃ː→ɑ̃ː, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    mɑ̃ː.t̪oː → mɑ̃.t̪o   (ɑ̃ː→ɑ̃, oː→o)
```

## masse

`mˈɑssɑm` → `mas`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmɑs.sɑm → ˈmɑs.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈmɑs.sɑ → ˈmas.sa   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈmas.sa → ˈmas.sə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈmas.sə → ˈma.sə   (s→∅)
1000: a front unrounded vowel lengthens before s + final schwa
    ˈma.sə → ˈmaː.sə   (ˈa→ˈaː)
1400: final ə becomes a non-syllabic off-glide
    ˈmaː.sə → ˈmaːsə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈmaːsə̯ → ˈmɑːsə̯   (ˈaː→ˈɑː)
1400: the long a stays front in words that lexically resisted backing
    ˈmɑːsə̯ → ˈmaːsə̯   (ˈɑː→ˈaː)
1400: the final off-glide schwa is deleted elsewhere
    ˈmaːsə̯ → ˈmaːs   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmaːs → maːs   (ˈaː→aː)
1400: distinctive vowel length is lost entirely
    maːs → mas   (aː→a)
```

## matin

`mˌɑːt̪uːt̪ˈiːn̪um` → `ma.t̪ɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmɑː.t̪uːˈt̪iː.n̪um → ˌmɑː.t̪uːˈt̪iː.n̪ʊm   (u→ʊ)
-100: unstressed long u becomes a mid central vowel (sonus medius), not word-finally
    ˌmɑː.t̪uːˈt̪iː.n̪ʊm → ˌmɑː.t̪ɪˈt̪iː.n̪ʊm   (uː→ɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɑː.t̪ɪˈt̪iː.n̪ʊm → ˌmɑ.t̪ɪˈt̪i.n̪ʊm   (ˌɑː→ˌɑ, ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌmɑ.t̪ɪˈt̪i.n̪ʊm → ˌmɑ.t̪eˈt̪i.n̪om   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɑ.t̪eˈt̪i.n̪om → ˌmɑ.t̪eˈt̪i.n̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɑ.t̪eˈt̪i.n̪o → ˌmɑ.t̪eˈt̪iː.n̪o   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˌmɑ.t̪eˈt̪iː.n̪o → ˌma.t̪eˈt̪iː.n̪o   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌma.t̪eˈt̪iː.n̪o → ˌma.t̪əˈt̪iː.n̪ə   (e→ə, o→ə)
600: schwa becomes non-syllabic
    ˌma.t̪əˈt̪iː.n̪ə → ˌmat̪ə̯ˈt̪iːn̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmat̪ə̯ˈt̪iːn̪ə̯ → ˌmat̪ˈt̪iːn̪   (ˈə̯t̪iːn̪ə̯→ˈt̪iːn̪)
750: vowel length resets to short
    ˌmat̪ˈt̪iːn̪ → ˌmat̪ˈt̪in̪   (ˈiː→ˈi)
750: a dental stop deletes before another coronal stop
    ˌmat̪ˈt̪in̪ → ˌmaˈt̪in̪   (t̪→∅)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌmaˈt̪in̪ → ˌmaˈt̪ĩn̪   (ˈi→ˈĩ)
1200: nasalized ĩ lowers to ẽ
    ˌmaˈt̪ĩn̪ → ˌmaˈt̪ẽn̪   (ˈĩ→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmaˈt̪ẽn̪ → ˌmaˈt̪ẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˌmaˈt̪ẽː → ˌmaˈt̪ɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌmaˈt̪ɛ̃ː → ma.t̪ɛ̃ː   (ˌa→a, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    ma.t̪ɛ̃ː → ma.t̪ɛ̃   (ɛ̃ː→ɛ̃)
```

## moelle

`mˌed̪ˈullɑm` → `mul`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmeˈd̪ul.lɑm → ˌmɛˈd̪ʊl.lɑm   (ˌe→ˌɛ, ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˌmɛˈd̪ʊl.lɑm → ˌmɛˈd̪ol.lɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɛˈd̪ol.lɑm → ˌmɛˈd̪ol.lɑ   (m→∅)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌmɛˈd̪ol.lɑ → ˌmɛˈðol.lɑ   (d̪→ð)
500: the low vowel fronts by default
    ˌmɛˈðol.lɑ → ˌmɛˈðol.la   (ɑ→a)
600: secondary-stressed ɛ raises to e before any two segments
    ˌmɛˈðol.la → ˌmeˈðol.la   (ˌɛ→ˌe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌmeˈðol.la → ˌmeˈðol.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˌmeˈðol.lə → ˌmeˈðo.lə   (l→∅)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌmeˈðo.lə → ˌməˈðo.lə   (ˌe→ˌə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌməˈðo.lə → ˌməˈðu.lə   (ˈo→ˈu)
1000: the interdental fricatives (plain and palatalized) efface
    ˌməˈðu.lə → ˌməˈu.lə   (ð→∅)
1200: a stressless schwa desyllabifies before another vowel
    ˌməˈu.lə → ˈmə̯u.lə   (ˌə→ə̯)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˈmə̯u.lə → ˈmə̯uː.lə   (ˈu→ˈuː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈmə̯uː.lə → ˈmuː.lə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈmuː.lə → ˈmuːlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈmuːlə̯ → ˈmuːl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmuːl → muːl   (ˈuː→uː)
1400: distinctive vowel length is lost entirely
    muːl → mul   (uː→u)
```

## merci

`mˌerkˈeːd̪em` → `mɛʁ.si`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmerˈkeː.d̪em → ˌmɛrˈkeː.d̪ɛm   (ˌe→ˌɛ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɛrˈkeː.d̪ɛm → ˌmɛrˈke.d̪ɛm   (ˈeː→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɛrˈke.d̪ɛm → ˌmɛrˈke.d̪ɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌmɛrˈke.d̪ɛ → ˌmɛrˈkʲe.d̪ɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌmɛrˈkʲe.d̪ɛ → ˌmɛrˈce.d̪ɛ   (kʲ→c)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌmɛrˈce.d̪ɛ → ˌmɛrˈce.ðɛ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɛrˈce.ðɛ → ˌmɛrˈceː.ðɛ   (ˈe→ˈeː)
500: stressed eː raises to iː after a high-front consonant
    ˌmɛrˈceː.ðɛ → ˌmɛrˈciː.ðɛ   (ˈeː→ˈiː)
500: a palatal stop affricates
    ˌmɛrˈciː.ðɛ → ˌmɛrˈt͡sʲiː.ðɛ   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmɛrˈt͡sʲiː.ðɛ → ˌmɛrˈt͡sʲiː.ðə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌmɛrˈt͡sʲiː.ðə → ˌmɛrˈt͡sʲiːðə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmɛrˈt͡sʲiːðə̯ → ˌmɛrˈt͡sʲiːð   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌmɛrˈt͡sʲiːð → ˌmerˈt͡sʲiːð   (ˌɛ→ˌe)
750: all final obstruents devoice
    ˌmerˈt͡sʲiːð → ˌmerˈt͡sʲiːθ   (ð→θ)
750: vowel length resets to short
    ˌmerˈt͡sʲiːθ → ˌmerˈt͡sʲiθ   (ˈiː→ˈi)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌmerˈt͡sʲiθ → ˌmɛrˈt͡sʲiθ   (ˌe→ˌɛ)
1000: the interdental fricatives (plain and palatalized) efface
    ˌmɛrˈt͡sʲiθ → ˌmɛrˈt͡sʲi   (θ→∅)
1000: all affricates become sibilants (deaffrication)
    ˌmɛrˈt͡sʲi → ˌmɛrˈsʲi   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˌmɛrˈsʲi → ˌmɛrˈsi   (sʲ→s)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmɛrˈsi → ˌmɛɹˈsi   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌmɛɹˈsi → ˌmɛrˈsi   (ɹ→r)
1400: r becomes uvular ʀ
    ˌmɛrˈsi → ˌmɛʀˈsi   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɛʀˈsi → mɛʀ.si   (ˌɛ→ɛ, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    mɛʀ.si → mɛʁ.si   (ʀ→ʁ)
```

## mincer

`mˌin̪uːt̪iˈɑːre` → `mɛ̃.se`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmi.n̪uː.t̪iˈɑː.re → ˌmɪ.n̪uː.t̪ɪˈɑː.rɛ   (ˌi→ˌɪ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɪ.n̪uː.t̪ɪˈɑː.rɛ → ˌmɪ.n̪uːˈt̪jɑː.rɛ   (ɪ→j)
-100: unstressed long u becomes a mid central vowel (sonus medius), not word-finally
    ˌmɪ.n̪uːˈt̪jɑː.rɛ → ˌmɪ.n̪ɪˈt̪jɑː.rɛ   (uː→ɪ)
-100: yod strengthens before a vowel
    ˌmɪ.n̪ɪˈt̪jɑː.rɛ → ˌmɪ.n̪ɪˈt̪ʝɑː.rɛ   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɪ.n̪ɪˈt̪ʝɑː.rɛ → ˌmɪ.n̪ɪˈt̪ʝɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌmɪ.n̪ɪˈt̪ʝɑ.rɛ → ˌme.n̪eˈt̪ʝɑ.rɛ   (ˌɪ→ˌe, ɪ→e)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌme.n̪eˈt̪ʝɑ.rɛ → ˌme.n̪et͡sʲˈʝɑ.rɛ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌme.n̪et͡sʲˈʝɑ.rɛ → ˌme.n̪eˈt͡sʲɑ.rɛ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌme.n̪eˈt͡sʲɑ.rɛ → ˌme.n̪eˈt͡sʲɑː.rɛ   (ˈɑ→ˈɑː)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌme.n̪eˈt͡sʲɑː.rɛ → ˌmen̪ˈt͡sʲɑː.rɛ   (e→∅)
500: the low vowel fronts by default
    ˌmen̪ˈt͡sʲɑː.rɛ → ˌmen̪ˈt͡sʲaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmen̪ˈt͡sʲaː.rɛ → ˌmen̪ˈt͡sʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌmen̪ˈt͡sʲaː.rə → ˌmen̪ˈt͡sʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmen̪ˈt͡sʲaːrə̯ → ˌmen̪ˈt͡sʲaːr   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌmen̪ˈt͡sʲaːr → ˌmen̪ˈt͡sʲɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌmen̪ˈt͡sʲɛːr → ˌmen̪ˈt͡sʲie̯r   (ˈɛː→ˈie̯)
600: j epenthesized after secondary-stressed e before nts
    ˌmen̪ˈt͡sʲie̯r → ˌmejn̪ˈt͡sʲie̯r   (∅→j)
1000: j nasalizes after a mid front vowel, before a nasal (second nasalization)
    ˌmejn̪ˈt͡sʲie̯r → ˌmej̃n̪ˈt͡sʲie̯r   (j→j̃)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌmej̃n̪ˈt͡sʲie̯r → ˌmẽj̃n̪ˈt͡sʲie̯r   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌmẽj̃n̪ˈt͡sʲie̯r → ˌmɛ̃j̃n̪ˈt͡sʲie̯r   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌmɛ̃j̃n̪ˈt͡sʲie̯r → ˌmãj̃n̪ˈt͡sʲie̯r   (ˌɛ̃→ˌã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌmãj̃n̪ˈt͡sʲie̯r → ˌmɛ̃j̃n̪ˈt͡sʲie̯r   (ˌã→ˌɛ̃)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌmɛ̃j̃n̪ˈt͡sʲie̯r → ˌmɛ̃j̃n̪ˈt͡sʲjer   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌmɛ̃j̃n̪ˈt͡sʲjer → ˌmɛ̃j̃n̪ˈsʲjer   (t͡sʲ→sʲ)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌmɛ̃j̃n̪ˈsʲjer → ˌmɛ̃n̪ˈsʲjer   (j̃→∅)
1200: je becomes e after a palatal consonant
    ˌmɛ̃n̪ˈsʲjer → ˌmɛ̃n̪ˈsʲer   (j→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌmɛ̃n̪ˈsʲer → ˌmɛ̃n̪ˈser   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmɛ̃n̪ˈser → ˌmɛ̃ːˈser   (ˌɛ̃n̪→ˌɛ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmɛ̃ːˈser → ˌmɛ̃ːˈseɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌmɛ̃ːˈseɹ → ˌmɛ̃ːˈse   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɛ̃ːˈse → mɛ̃ː.se   (ˌɛ̃ː→ɛ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    mɛ̃ː.se → mɛ̃.se   (ɛ̃ː→ɛ̃)
```

## mous

`mˈolliːs` → `mu`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmol.liːs → ˈmɔl.liːs   (ˈo→ˈɔ)
-100: the length feature is dropped now that quality carries the contrast
    ˈmɔl.liːs → ˈmɔl.lis   (iː→i)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmɔl.lis → ˈmɔl.ləs   (i→ə)
600: schwa becomes non-syllabic
    ˈmɔl.ləs → ˈmɔllə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmɔllə̯s → ˈmɔlls   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˈmɔlls → ˈmɔls   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈmɔls → ˈmɔɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˈmɔɫs → ˈmɔws   (ɫ→w)
1200: the ow diphthong monophthongizes to u
    ˈmɔws → ˈmus   (ˈɔw→ˈu)
1400: final obstruents are lost
    ˈmus → ˈmu   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmu → mu   (ˈu→u)
```

## mort

`mˈort̪em` → `mɔʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmor.t̪em → ˈmɔr.t̪ɛm   (ˈo→ˈɔ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmɔr.t̪ɛm → ˈmɔr.t̪ɛ   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmɔr.t̪ɛ → ˈmɔr.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈmɔr.t̪ə → ˈmɔrt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmɔrt̪ə̯ → ˈmɔrt̪   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈmɔrt̪ → ˈmɔɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈmɔɹt̪ → ˈmɔɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈmɔɹ → ˈmɔr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈmɔr → ˈmɔʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɔʀ → mɔʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    mɔʀ → mɔʁ   (ʀ→ʁ)
```

## moût

`mˈust̪um` → `mu`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmus.t̪um → ˈmʊs.t̪ʊm   (ˈu→ˈʊ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈmʊs.t̪ʊm → ˈmos.t̪om   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmos.t̪om → ˈmos.t̪o   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmos.t̪o → ˈmos.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈmos.t̪ə → ˈmost̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmost̪ə̯ → ˈmost̪   (ə̯→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈmost̪ → ˈmust̪   (ˈo→ˈu)
1000: s becomes x after a vowel, before any consonant
    ˈmust̪ → ˈmuxt̪   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈmuxt̪ → ˈmuːt̪   (ˈux→ˈuː)
1400: final obstruents are lost
    ˈmuːt̪ → ˈmuː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmuː → muː   (ˈuː→uː)
1400: distinctive vowel length is lost entirely
    muː → mu   (uː→u)
```

## noue

`n̪ˈɑwikɑm` → `n̪œɥ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈn̪ɑ.wi.kɑm → ˈn̪ɑ.ɣʷi.kɑm   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪ɑ.ɣʷi.kɑm → ˈn̪ɑ.ɣʷɪ.kɑm   (i→ɪ)
-100: ɪ lost between the labiovelar approximant and k
    ˈn̪ɑ.ɣʷɪ.kɑm → ˈn̪ɑɣʷ.kɑm   (ɪ→∅)
-100: the labiovelar approximant simplifies to w before a consonant
    ˈn̪ɑɣʷ.kɑm → ˈn̪ɑw.kɑm   (ɣʷ→w)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪ɑw.kɑm → ˈn̪ɑw.kɑ   (m→∅)
500: k voices to g intervocalically
    ˈn̪ɑw.kɑ → ˈn̪ɑw.gɑ   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˈn̪ɑw.gɑ → ˈn̪ɑw.ɣɑ   (g→ɣ)
500: the velar fricative is lost after a rounded non-consonantal segment before a low vowel
    ˈn̪ɑw.ɣɑ → ˈn̪ɑ.wɑ   (ɣ→∅)
500: the low vowel fronts by default
    ˈn̪ɑ.wɑ → ˈn̪a.wa   (ˈɑ→ˈa, ɑ→a)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˈn̪a.wa → ˈn̪aː.wa   (ˈa→ˈaː)
500: the high back consonant w fronts before a front vowel
    ˈn̪aː.wa → ˈn̪aː.wʲa   (w→wʲ)
500: a vowel shortens before the high back round glide (w)
    ˈn̪aː.wʲa → ˈn̪a.wʲa   (ˈaː→ˈa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈn̪a.wʲa → ˈn̪ɔ.wʲa   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈn̪ɔ.wʲa → ˈn̪ɔ.ɥa   (wʲ→ɥ)
600: a stressed vowel lengthens before a consonant + vowel
    ˈn̪ɔ.ɥa → ˈn̪ɔː.ɥa   (ˈɔ→ˈɔː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˈn̪ɔː.ɥa → ˈn̪uo̯.ɥa   (ˈɔː→ˈuo̯)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈn̪uo̯.ɥa → ˈn̪ʉo̯.ɥa   (ˈu→ˈʉ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈn̪ʉo̯.ɥa → ˈn̪ʉo̯.ɥə   (a→ə)
1000: high round back vowels front (completion of u-fronting)
    ˈn̪ʉo̯.ɥə → ˈn̪yo̯.ɥə   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈn̪yo̯.ɥə → ˈn̪ye̯.ɥə   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈn̪ye̯.ɥə → ˈn̪ø.ɥə   (ˈye̯→ˈø)
1200: schwa desyllabifies after another vowel
    ˈn̪ø.ɥə → ˈn̪øɥə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈn̪øɥə̯ → ˈn̪øɥ   (ə̯→∅)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈn̪øɥ → ˈn̪œɥ   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪œɥ → n̪œɥ   (ˈœ→œ)
```

## nouer

`n̪ˌoːd̪ˈɑːre` → `n̪u̯e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌn̪oːˈd̪ɑː.re → ˌn̪oːˈd̪ɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌn̪oːˈd̪ɑː.rɛ → ˌn̪oˈd̪ɑ.rɛ   (ˌoː→ˌo, ˈɑː→ˈɑ)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌn̪oˈd̪ɑ.rɛ → ˌn̪oˈðɑ.rɛ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˌn̪oˈðɑ.rɛ → ˌn̪oˈðɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌn̪oˈðɑː.rɛ → ˌn̪oˈðaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌn̪oˈðaː.rɛ → ˌn̪oˈðaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌn̪oˈðaː.rə → ˌn̪oˈðaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌn̪oˈðaːrə̯ → ˌn̪oˈðaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌn̪oˈðaːr → ˌn̪oˈðae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌn̪oˈðae̯r → ˌn̪oˈðeːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌn̪oˈðeːr → ˌn̪oˈðer   (ˈeː→ˈe)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌn̪oˈðer → ˌn̪uˈðer   (ˌo→ˌu)
1000: the interdental fricatives (plain and palatalized) efface
    ˌn̪uˈðer → ˌn̪uˈer   (ð→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌn̪uˈer → ˌn̪uˈeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌn̪uˈeɹ → ˌn̪uˈe   (ɹ→∅)
1400: a countertonic high vowel consonantalizes before a lower vowel, ceding stress
    ˌn̪uˈe → ˌn̪u̯e   (ˌu→u̯, ˈe→ˌe)
1400: stress is leveled — no longer distinctive for vowels
    ˌn̪u̯e → n̪u̯e   (ˌe→e)
```

## notre

`n̪ˈost̪rum` → `n̪ɔt̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪os.t̪rum → ˈn̪ɔs.t̪rʊm   (ˈo→ˈɔ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈn̪ɔs.t̪rʊm → ˈn̪ɔs.t̪rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪ɔs.t̪rom → ˈn̪ɔs.t̪ro   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪ɔs.t̪ro → ˈn̪ɔs.t̪rə   (o→ə)
600: schwa becomes non-syllabic
    ˈn̪ɔs.t̪rə → ˈn̪ɔst̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪ɔst̪rə̯ → ˈn̪ɔst̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈn̪ɔst̪r → ˈn̪ɔs.t̪rə   (∅→ə)
1000: s becomes x after a vowel, before any consonant
    ˈn̪ɔs.t̪rə → ˈn̪ɔx.t̪rə   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈn̪ɔx.t̪rə → ˈn̪ɔː.t̪rə   (ˈɔx→ˈɔː)
1200: initial primary-stressed long ɔː shortens before a consonant cluster
    ˈn̪ɔː.t̪rə → ˈn̪ɔ.t̪rə   (ˈɔː→ˈɔ)
1400: final ə becomes a non-syllabic off-glide
    ˈn̪ɔ.t̪rə → ˈn̪ɔt̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈn̪ɔt̪rə̯ → ˈn̪ɔt̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈn̪ɔt̪r → ˈn̪ɔt̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪ɔt̪ʀ → n̪ɔt̪ʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    n̪ɔt̪ʀ → n̪ɔt̪ʁ   (ʀ→ʁ)
```

## nombre

`n̪ˈumerum` → `n̪ɔ̃bʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪u.me.rum → ˈn̪ʊ.mɛ.rʊm   (ˈu→ˈʊ, e→ɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈn̪ʊ.mɛ.rʊm → ˈn̪o.mɛ.rom   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪o.mɛ.rom → ˈn̪o.mɛ.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈn̪o.mɛ.ro → ˈn̪oː.mɛ.ro   (ˈo→ˈoː)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈn̪oː.mɛ.ro → ˈn̪oː.mro   (ɛ→∅)
500: b epenthesized between m and a coronal non-nasal sonorant glide
    ˈn̪oː.mro → ˈn̪oːm.bro   (∅→b)
500: a vowel shortens before a consonant cluster
    ˈn̪oːm.bro → ˈn̪om.bro   (ˈoː→ˈo)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈn̪om.bro → ˈn̪ũm.bro   (ˈo→ˈũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪ũm.bro → ˈn̪ũm.brə   (o→ə)
600: schwa becomes non-syllabic
    ˈn̪ũm.brə → ˈn̪ũmbrə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈn̪ũmbrə̯ → ˈn̪ũm.brə   (ə̯→ə)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈn̪ũm.brə → ˈn̪ũː.brə   (ˈũm→ˈũː)
1400: final ə becomes a non-syllabic off-glide
    ˈn̪ũː.brə → ˈn̪ũːbrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈn̪ũːbrə̯ → ˈn̪ũːbr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈn̪ũːbr → ˈn̪ũːbʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪ũːbʀ → n̪ũːbʀ   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    n̪ũːbʀ → n̪ũbʀ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    n̪ũbʀ → n̪ɔ̃bʀ   (ũ→ɔ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    n̪ɔ̃bʀ → n̪ɔ̃bʁ   (ʀ→ʁ)
```

## ornement

`ˈorn̪ɑːmˈen̪t̪um` → `ɔ.ʁn̪ə.mɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈor.n̪ɑːˈmen̪.t̪um → ˈɔr.n̪ɑːˈmɛn̪.t̪ʊm   (ˈo→ˈɔ, ˈe→ˈɛ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈɔr.n̪ɑːˈmɛn̪.t̪ʊm → ˈɔr.n̪ɑˈmɛn̪.t̪ʊm   (ɑː→ɑ)
-100: lax high vowels lower to tense mid vowels
    ˈɔr.n̪ɑˈmɛn̪.t̪ʊm → ˈɔr.n̪ɑˈmɛn̪.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɔr.n̪ɑˈmɛn̪.t̪om → ˈɔr.n̪ɑˈmɛn̪.t̪o   (m→∅)
500: the low vowel fronts by default
    ˈɔr.n̪ɑˈmɛn̪.t̪o → ˈɔr.n̪aˈmɛn̪.t̪o   (ɑ→a)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈɔr.n̪aˈmɛn̪.t̪o → ˈɔr.n̪aˈmɛn̪.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈɔr.n̪aˈmɛn̪.t̪ə → ˈɔr.n̪aˈmɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈɔr.n̪aˈmɛn̪t̪ə̯ → ˈɔr.n̪aˈmɛn̪t̪   (ə̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈɔr.n̪aˈmɛn̪t̪ → ˈɔr.n̪əˈmɛn̪t̪   (a→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈɔr.n̪əˈmɛn̪t̪ → ˈɔr.n̪əˈmɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈɔr.n̪əˈmɛ̃n̪t̪ → ˈɔr.n̪ə̃ˈmɛ̃n̪t̪   (ə→ə̃)
1000: unstressed nasalized schwa denasalizes
    ˈɔr.n̪ə̃ˈmɛ̃n̪t̪ → ˈɔr.n̪əˈmɛ̃n̪t̪   (ə̃→ə)
1000: nasalized front mid vowels become nasalized a
    ˈɔr.n̪əˈmɛ̃n̪t̪ → ˈɔr.n̪əˈmãn̪t̪   (ˈɛ̃→ˈã)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈɔr.n̪əˈmãn̪t̪ → ˈɔr.n̪ə̃ˈmãn̪t̪   (ə→ə̃)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈɔr.n̪ə̃ˈmãn̪t̪ → ˈɔr.n̪ə̃ˈmãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈɔr.n̪ə̃ˈmãːt̪ → ˈɔr.n̪ə̃ˈmɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈɔr.n̪ə̃ˈmɑ̃ːt̪ → ˈɔɹ.n̪ə̃ˈmɑ̃ːt̪   (r→ɹ)
1400: final obstruents are lost
    ˈɔɹ.n̪ə̃ˈmɑ̃ːt̪ → ˈɔɹ.n̪ə̃ˈmɑ̃ː   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈɔɹ.n̪ə̃ˈmɑ̃ː → ˈɔr.n̪ə̃ˈmɑ̃ː   (ɹ→r)
1400: r becomes uvular ʀ
    ˈɔr.n̪ə̃ˈmɑ̃ː → ˈɔʀ.n̪ə̃ˈmɑ̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈɔʀ.n̪ə̃ˈmɑ̃ː → ɔʀ.n̪ə̃.mɑ̃ː   (ˈɔ→ɔ, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ɔʀ.n̪ə̃.mɑ̃ː → ɔʀ.n̪ə̃.mɑ̃   (ɑ̃ː→ɑ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    ɔʀ.n̪ə̃.mɑ̃ → ɔʀ.n̪ə.mɑ̃   (ə̃→ə)
1400: the uvular trill ʀ becomes a fricative ʁ
    ɔʀ.n̪ə.mɑ̃ → ɔ.ʁn̪ə.mɑ̃   (ʀ→ʁ)
```

## paume

`pˈɑlmɑm` → `pom`

```
-100: l darkens before a non-lateral consonant
    ˈpɑl.mɑm → ˈpɑɫ.mɑm   (l→ɫ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpɑɫ.mɑm → ˈpɑɫ.mɑ   (m→∅)
500: the low vowel fronts by default
    ˈpɑɫ.mɑ → ˈpaɫ.ma   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpaɫ.ma → ˈpaɫ.mə   (a→ə)
1000: back dark-l variants vocalize to w
    ˈpaɫ.mə → ˈpaw.mə   (ɫ→w)
1200: aw becomes long oː
    ˈpaw.mə → ˈpoː.mə   (ˈaw→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˈpoː.mə → ˈpoːmə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpoːmə̯ → ˈpoːm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpoːm → poːm   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    poːm → pom   (oː→o)
```

## parent

`pˌɑrˈen̪t̪em` → `pa.ʁɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpɑˈren̪.t̪em → ˌpɑˈrɛn̪.t̪ɛm   (ˈe→ˈɛ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɑˈrɛn̪.t̪ɛm → ˌpɑˈrɛn̪.t̪ɛ   (m→∅)
500: the low vowel fronts by default
    ˌpɑˈrɛn̪.t̪ɛ → ˌpaˈrɛn̪.t̪ɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpaˈrɛn̪.t̪ɛ → ˌpaˈrɛn̪.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌpaˈrɛn̪.t̪ə → ˌpaˈrɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpaˈrɛn̪t̪ə̯ → ˌpaˈrɛn̪t̪   (ə̯→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌpaˈrɛn̪t̪ → ˌpaˈrɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌpaˈrɛ̃n̪t̪ → ˌpaˈrãn̪t̪   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌpaˈrãn̪t̪ → ˌpaˈrãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˌpaˈrãːt̪ → ˌpaˈrɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˌpaˈrɑ̃ːt̪ → ˌpaˈrɑ̃ː   (t̪→∅)
1400: r becomes uvular ʀ
    ˌpaˈrɑ̃ː → ˌpaˈʀɑ̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpaˈʀɑ̃ː → pa.ʀɑ̃ː   (ˌa→a, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    pa.ʀɑ̃ː → pa.ʀɑ̃   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    pa.ʀɑ̃ → pa.ʁɑ̃   (ʀ→ʁ)
```

## pâtre

`pˈɑːst̪or` → `pɑt̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpɑːs.t̪or → ˈpɑːs.t̪ɔr   (o→ɔ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpɑːs.t̪ɔr → ˈpɑs.t̪ɔr   (ˈɑː→ˈɑ)
500: the low vowel fronts by default
    ˈpɑs.t̪ɔr → ˈpas.t̪ɔr   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpas.t̪ɔr → ˈpas.t̪ər   (ɔ→ə)
600: schwa becomes non-syllabic
    ˈpas.t̪ər → ˈpast̪ə̯r   (ə→ə̯)
600: non-syllabic schwa + r/tap metathesizes word-finally
    ˈpast̪ə̯r → ˈpast̪rə̯   (ə̯→r, r→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpast̪rə̯ → ˈpast̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈpast̪r → ˈpas.t̪rə   (∅→ə)
1000: s becomes x after a vowel, before any consonant
    ˈpas.t̪rə → ˈpax.t̪rə   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈpax.t̪rə → ˈpaː.t̪rə   (ˈax→ˈaː)
1400: final ə becomes a non-syllabic off-glide
    ˈpaː.t̪rə → ˈpaːt̪rə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈpaːt̪rə̯ → ˈpɑːt̪rə̯   (ˈaː→ˈɑː)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɑːt̪rə̯ → ˈpɑːt̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈpɑːt̪r → ˈpɑːt̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɑːt̪ʀ → pɑːt̪ʀ   (ˈɑː→ɑː)
1400: distinctive vowel length is lost entirely
    pɑːt̪ʀ → pɑt̪ʀ   (ɑː→ɑ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɑt̪ʀ → pɑt̪ʁ   (ʀ→ʁ)
```

## piège

`pˈeːd̪ikum` → `pjɛʒ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpeː.d̪i.kum → ˈpeː.d̪ɪ.kʊm   (i→ɪ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpeː.d̪ɪ.kʊm → ˈpe.d̪ɪ.kʊm   (ˈeː→ˈe)
-100: lax high vowels lower to tense mid vowels
    ˈpe.d̪ɪ.kʊm → ˈpe.d̪e.kom   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpe.d̪e.kom → ˈpe.d̪e.ko   (m→∅)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈpe.d̪e.ko → ˈpe.ðe.ko   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpe.ðe.ko → ˈpeː.ðe.ko   (ˈe→ˈeː)
500: k voices to g intervocalically
    ˈpeː.ðe.ko → ˈpeː.ðe.go   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˈpeː.ðe.go → ˈpeː.ðe.ɣo   (g→ɣ)
600: stressed eː lowers to ɛː before ð + e + the velar fricative
    ˈpeː.ðe.ɣo → ˈpɛː.ðe.ɣo   (ˈeː→ˈɛː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈpɛː.ðe.ɣo → ˈpɛː.ðə.ɣo   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpɛː.ðə.ɣo → ˈpɛː.ðə.ɣə   (o→ə)
600: schwa becomes non-syllabic
    ˈpɛː.ðə.ɣə → ˈpɛːðə̯ɣə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after a non-strident coronal before the velar fricative
    ˈpɛːðə̯ɣə̯ → ˈpɛː.ðəɣə̯   (ə̯→ə)
600: non-syllabic schwa restores after a dental fricative + schwa + the velar fricative
    ˈpɛː.ðəɣə̯ → ˈpɛː.ðə.ɣə   (ə̯→ə)
600: t/d/ð + schwa + the velar fricative becomes an affricate
    ˈpɛː.ðə.ɣə → ˈpɛː.d̪d͡ʒə   (ðəɣ→d̪d͡ʒ)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˈpɛː.d̪d͡ʒə → ˈpie̯.d̪d͡ʒə   (ˈɛː→ˈie̯)
750: a dental stop deletes before another coronal stop
    ˈpie̯.d̪d͡ʒə → ˈpie̯.d͡ʒə   (d̪→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈpie̯.d͡ʒə → ˈpje.d͡ʒə   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈpje.d͡ʒə → ˈpje.ʒə   (d͡ʒ→ʒ)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈpje.ʒə → ˈpjɛ.ʒə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈpjɛ.ʒə → ˈpjɛʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpjɛʒə̯ → ˈpjɛʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpjɛʒ → pjɛʒ   (ˈɛ→ɛ)
```

## pinceau

`pˌeːn̪ikˈellum` → `pɛ̃.so`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpeː.n̪iˈkel.lum → ˌpeː.n̪ɪˈkɛl.lʊm   (i→ɪ, ˈe→ˈɛ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpeː.n̪ɪˈkɛl.lʊm → ˌpe.n̪ɪˈkɛl.lʊm   (ˌeː→ˌe)
-100: lax high vowels lower to tense mid vowels
    ˌpe.n̪ɪˈkɛl.lʊm → ˌpe.n̪eˈkɛl.lom   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpe.n̪eˈkɛl.lom → ˌpe.n̪eˈkɛl.lo   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌpe.n̪eˈkɛl.lo → ˌpe.n̪eˈkʲɛl.lo   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌpe.n̪eˈkʲɛl.lo → ˌpe.n̪eˈcɛl.lo   (kʲ→c)
500: a palatal stop affricates
    ˌpe.n̪eˈcɛl.lo → ˌpe.n̪eˈt͡sʲɛl.lo   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpe.n̪eˈt͡sʲɛl.lo → ˌpe.n̪əˈt͡sʲɛl.lə   (e→ə, o→ə)
600: schwa becomes non-syllabic
    ˌpe.n̪əˈt͡sʲɛl.lə → ˌpen̪ə̯ˈt͡sʲɛllə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpen̪ə̯ˈt͡sʲɛllə̯ → ˌpen̪ˈt͡sʲɛll   (ˈə̯t͡sʲɛllə̯→ˈt͡sʲɛll)
600: j epenthesized after secondary-stressed e before nts
    ˌpen̪ˈt͡sʲɛll → ˌpejn̪ˈt͡sʲɛll   (∅→j)
750: an identical consonant geminate reduces to one (recurrence)
    ˌpejn̪ˈt͡sʲɛll → ˌpejn̪ˈt͡sʲɛl   (l→∅)
1000: j nasalizes after a mid front vowel, before a nasal (second nasalization)
    ˌpejn̪ˈt͡sʲɛl → ˌpej̃n̪ˈt͡sʲɛl   (j→j̃)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌpej̃n̪ˈt͡sʲɛl → ˌpẽj̃n̪ˈt͡sʲɛl   (ˌe→ˌẽ)
1000: final l labializes after a short mid vowel
    ˌpẽj̃n̪ˈt͡sʲɛl → ˌpẽj̃n̪ˈt͡sʲɛɫ   (l→ɫ)
1000: nasalized front mid vowels begin to lower
    ˌpẽj̃n̪ˈt͡sʲɛɫ → ˌpɛ̃j̃n̪ˈt͡sʲɛɫ   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌpɛ̃j̃n̪ˈt͡sʲɛɫ → ˌpãj̃n̪ˈt͡sʲɛɫ   (ˌɛ̃→ˌã)
1000: back dark-l variants vocalize to w
    ˌpãj̃n̪ˈt͡sʲɛɫ → ˌpãj̃n̪ˈt͡sʲɛw   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌpãj̃n̪ˈt͡sʲɛw → ˌpãj̃n̪ˈt͡sʲɛa̯w   (∅→a̯)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌpãj̃n̪ˈt͡sʲɛa̯w → ˌpɛ̃j̃n̪ˈt͡sʲɛa̯w   (ˌã→ˌɛ̃)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌpɛ̃j̃n̪ˈt͡sʲɛa̯w → ˌpɛ̃j̃n̪ˈt͡sʲe̯aw   (ˈɛ→e̯, a̯→ˈa)
1000: all affricates become sibilants (deaffrication)
    ˌpɛ̃j̃n̪ˈt͡sʲe̯aw → ˌpɛ̃j̃n̪ˈsʲe̯aw   (t͡sʲ→sʲ)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌpɛ̃j̃n̪ˈsʲe̯aw → ˌpɛ̃n̪ˈsʲe̯aw   (j̃→∅)
1200: aw becomes long oː
    ˌpɛ̃n̪ˈsʲe̯aw → ˌpɛ̃n̪ˈsʲe̯oː   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌpɛ̃n̪ˈsʲe̯oː → ˌpɛ̃n̪ˈsʲə̯oː   (e̯→ə̯)
1200: the remaining anterior palatalized consonants depalatalize
    ˌpɛ̃n̪ˈsʲə̯oː → ˌpɛ̃n̪ˈsə̯oː   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌpɛ̃n̪ˈsə̯oː → ˌpɛ̃ːˈsə̯oː   (ˌɛ̃n̪→ˌɛ̃ː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌpɛ̃ːˈsə̯oː → ˌpɛ̃ːˈsoː   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌpɛ̃ːˈsoː → pɛ̃ː.soː   (ˌɛ̃ː→ɛ̃ː, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    pɛ̃ː.soː → pɛ̃.so   (ɛ̃ː→ɛ̃, oː→o)
```

## perse

`pˈersɑm` → `pɛʁs`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈper.sɑm → ˈpɛr.sɑm   (ˈe→ˈɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpɛr.sɑm → ˈpɛr.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈpɛr.sɑ → ˈpɛr.sa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpɛr.sa → ˈpɛr.sə   (a→ə)
1400: final ə becomes a non-syllabic off-glide
    ˈpɛr.sə → ˈpɛrsə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈpɛrsə̯ → ˈpɛɹsə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɛɹsə̯ → ˈpɛɹs   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈpɛɹs → ˈpɛrs   (ɹ→r)
1400: r becomes uvular ʀ
    ˈpɛrs → ˈpɛʀs   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɛʀs → pɛʀs   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɛʀs → pɛʁs   (ʀ→ʁ)
```

## pie

`pˈiːɑm` → `pi`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈpiː.ɑm → ˈpi.ɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpi.ɑm → ˈpi.ɑ   (m→∅)
300: a stressed vowel lengthens before another vowel
    ˈpi.ɑ → ˈpiː.ɑ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˈpiː.ɑ → ˈpiː.a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpiː.a → ˈpiː.ə   (a→ə)
750: vowel length resets to short
    ˈpiː.ə → ˈpi.ə   (ˈiː→ˈi)
1200: schwa desyllabifies after another vowel
    ˈpi.ə → ˈpiə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈpiə̯ → ˈpiː   (ˈiə̯→ˈiː)
1400: stress is leveled — no longer distinctive for vowels
    ˈpiː → piː   (ˈiː→iː)
1400: distinctive vowel length is lost entirely
    piː → pi   (iː→i)
```

## panne

`pˈin̪n̪ɑm` → `pan̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpin̪.n̪ɑm → ˈpɪn̪.n̪ɑm   (ˈi→ˈɪ)
-100: lax high vowels lower to tense mid vowels
    ˈpɪn̪.n̪ɑm → ˈpen̪.n̪ɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpen̪.n̪ɑm → ˈpen̪.n̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈpen̪.n̪ɑ → ˈpen̪.n̪a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpen̪.n̪a → ˈpen̪.n̪ə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈpen̪.n̪ə → ˈpe.n̪ə   (n̪→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈpe.n̪ə → ˈpẽ.n̪ə   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈpẽ.n̪ə → ˈpɛ̃.n̪ə   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈpɛ̃.n̪ə → ˈpã.n̪ə   (ˈɛ̃→ˈã)
1400: final ə becomes a non-syllabic off-glide
    ˈpã.n̪ə → ˈpãn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpãn̪ə̯ → ˈpãn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpãn̪ → pãn̪   (ˈã→ã)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    pãn̪ → pan̪   (ã→a)
```

## plaisir

`plˌɑkˈeːre` → `ple.ziʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌplɑˈkeː.re → ˌplɑˈkeː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌplɑˈkeː.rɛ → ˌplɑˈke.rɛ   (ˈeː→ˈe)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌplɑˈke.rɛ → ˌplɑˈkʲe.rɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌplɑˈkʲe.rɛ → ˌplɑˈce.rɛ   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˌplɑˈce.rɛ → ˌplɑˈceː.rɛ   (ˈe→ˈeː)
500: stressed eː raises to iː after a high-front consonant
    ˌplɑˈceː.rɛ → ˌplɑˈciː.rɛ   (ˈeː→ˈiː)
500: a palatal stop affricates
    ˌplɑˈciː.rɛ → ˌplɑˈt͡sʲiː.rɛ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌplɑˈt͡sʲiː.rɛ → ˌplaˈt͡sʲiː.rɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌplaˈt͡sʲiː.rɛ → ˌplaˈt͡sʲiː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌplaˈt͡sʲiː.rə → ˌplaˈt͡sʲiːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌplaˈt͡sʲiːrə̯ → ˌplaˈt͡sʲiːr   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌplaˈt͡sʲiːr → ˌplaˈd͡zʲiːr   (t͡sʲ→d͡zʲ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌplaˈd͡zʲiːr → ˌplaˈzʲiːr   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌplaˈzʲiːr → ˌplajˈziːr   (zʲ→jz)
600: a coronal palatalizes between two high-front segments
    ˌplajˈziːr → ˌplajˈzʲiːr   (z→zʲ)
750: vowel length resets to short
    ˌplajˈzʲiːr → ˌplajˈzʲir   (ˈiː→ˈi)
1200: the remaining anterior palatalized consonants depalatalize
    ˌplajˈzʲir → ˌplajˈzir   (zʲ→z)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌplajˈzir → ˌplɛːˈzir   (ˌaj→ˌɛː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌplɛːˈzir → ˌplɛːˈziɹ   (r→ɹ)
1400: countertonic ə/ɛ becomes ˌe after a labial + l
    ˌplɛːˈziɹ → ˌpleˈziɹ   (ˌɛː→ˌe)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌpleˈziɹ → ˌpleˈzir   (ɹ→r)
1400: r becomes uvular ʀ
    ˌpleˈzir → ˌpleˈziʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpleˈziʀ → ple.ziʀ   (ˌe→e, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ple.ziʀ → ple.ziʁ   (ʀ→ʁ)
```

## place

`plˈɑt̪t̪eɑm` → `plas`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈplɑt̪.t̪e.ɑm → ˈplɑt̪.t̪ɛ.ɑm   (e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈplɑt̪.t̪ɛ.ɑm → ˈplɑt̪.t̪jɑm   (ɛ→j)
-100: yod strengthens before a vowel
    ˈplɑt̪.t̪jɑm → ˈplɑt̪.t̪ʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈplɑt̪.t̪ʝɑm → ˈplɑt̪.t̪ʝɑ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈplɑt̪.t̪ʝɑ → ˈplɑt̪t͡sʲ.ʝɑ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˈplɑt̪t͡sʲ.ʝɑ → ˈplɑ.t̪t͡sʲɑ   (ʝ→∅)
500: the low vowel fronts by default
    ˈplɑ.t̪t͡sʲɑ → ˈpla.t̪t͡sʲa   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpla.t̪t͡sʲa → ˈpla.t̪t͡sʲə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈpla.t̪t͡sʲə → ˈpla.t͡sʲə   (t̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈpla.t͡sʲə → ˈpla.sʲə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈpla.sʲə → ˈpla.sə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈpla.sə → ˈplasə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈplasə̯ → ˈplas   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈplas → plas   (ˈa→a)
```

## plus

`plˈuːs` → `ply`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈpluːs → ˈplus   (ˈuː→ˈu)
300: a stressed vowel lengthens in a monosyllable before a final consonant
    ˈplus → ˈpluːs   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈpluːs → ˈplʉːs   (ˈuː→ˈʉː)
750: vowel length resets to short
    ˈplʉːs → ˈplʉs   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈplʉs → ˈplys   (ˈʉ→ˈy)
1000: a primary-stressed vowel lengthens before word-final s
    ˈplys → ˈplyːs   (ˈy→ˈyː)
1400: final obstruents are lost
    ˈplyːs → ˈplyː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈplyː → plyː   (ˈyː→yː)
1400: distinctive vowel length is lost entirely
    plyː → ply   (yː→y)
```

## porte

`pˈort̪ɑt̪` → `pɔʁt̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpor.t̪ɑt̪ → ˈpɔr.t̪ɑt̪   (ˈo→ˈɔ)
500: the low vowel fronts by default
    ˈpɔr.t̪ɑt̪ → ˈpɔr.t̪at̪   (ɑ→a)
600: t/d spirantize word-finally after a vowel
    ˈpɔr.t̪at̪ → ˈpɔr.t̪aθ   (t̪→θ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpɔr.t̪aθ → ˈpɔr.t̪əθ   (a→ə)
1000: the interdental fricatives (plain and palatalized) efface
    ˈpɔr.t̪əθ → ˈpɔr.t̪ə   (θ→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈpɔr.t̪ə → ˈpɔrt̪ə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈpɔrt̪ə̯ → ˈpɔɹt̪ə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɔɹt̪ə̯ → ˈpɔɹt̪   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈpɔɹt̪ → ˈpɔrt̪   (ɹ→r)
1400: r becomes uvular ʀ
    ˈpɔrt̪ → ˈpɔʀt̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɔʀt̪ → pɔʀt̪   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɔʀt̪ → pɔʁt̪   (ʀ→ʁ)
```

## prêter

`prˌɑe̯st̪ˈɑːre` → `pʁɛ.t̪e`

```
-100: low vowel re-fronts before the e-glide
    ˌprɑe̯sˈt̪ɑː.re → ˌprae̯sˈt̪ɑː.re   (ˌɑ→ˌa)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌprae̯sˈt̪ɑː.re → ˌprae̯sˈt̪ɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌprae̯sˈt̪ɑː.rɛ → ˌprae̯sˈt̪ɑ.rɛ   (ˈɑː→ˈɑ)
-100: the ae diphthong monophthongizes to ɛ, preserving any stress mark
    ˌprae̯sˈt̪ɑ.rɛ → ˌprɛsˈt̪ɑ.rɛ   (ˌae̯→ˌɛ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌprɛsˈt̪ɑ.rɛ → ˌprɛsˈt̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌprɛsˈt̪ɑː.rɛ → ˌprɛsˈt̪aː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌprɛsˈt̪aː.rɛ → ˌprɛsˈt̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌprɛsˈt̪aː.rə → ˌprɛsˈt̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌprɛsˈt̪aːrə̯ → ˌprɛsˈt̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌprɛsˈt̪aːr → ˌprɛsˈt̪ae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɛ raises to ɨ before a coronal non-nasal continuant + non-nasal consonant
    ˌprɛsˈt̪ae̯r → ˌprɨsˈt̪ae̯r   (ˌɛ→ˌɨ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌprɨsˈt̪ae̯r → ˌprɛsˈt̪ae̯r   (ˌɨ→ˌɛ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌprɛsˈt̪ae̯r → ˌprɛsˈt̪eːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌprɛsˈt̪eːr → ˌprɛsˈt̪er   (ˈeː→ˈe)
1000: s becomes x after a vowel, before any consonant
    ˌprɛsˈt̪er → ˌprɛxˈt̪er   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌprɛxˈt̪er → ˌprɛːˈt̪er   (ˌɛx→ˌɛː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌprɛːˈt̪er → ˌprɛːˈt̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌprɛːˈt̪eɹ → ˌprɛːˈt̪e   (ɹ→∅)
1400: r becomes uvular ʀ
    ˌprɛːˈt̪e → ˌpʀɛːˈt̪e   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpʀɛːˈt̪e → pʀɛː.t̪e   (ˌɛː→ɛː, ˈe→e)
1400: distinctive vowel length is lost entirely
    pʀɛː.t̪e → pʀɛ.t̪e   (ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀɛ.t̪e → pʁɛ.t̪e   (ʀ→ʁ)
```

## première

`prˌimˈɑːriɑm` → `pʁə.mjɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpriˈmɑː.ri.ɑm → ˌprɪˈmɑː.rɪ.ɑm   (ˌi→ˌɪ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌprɪˈmɑː.rɪ.ɑm → ˌprɪˈmɑː.rjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌprɪˈmɑː.rjɑm → ˌprɪˈmɑːr.ʝɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌprɪˈmɑːr.ʝɑm → ˌprɪˈmɑr.ʝɑm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌprɪˈmɑr.ʝɑm → ˌpreˈmɑr.ʝɑm   (ˌɪ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpreˈmɑr.ʝɑm → ˌpreˈmɑr.ʝɑ   (m→∅)
500: r + yod becomes palatalized r
    ˌpreˈmɑr.ʝɑ → ˌpreˈmɑ.rʲɑ   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌpreˈmɑ.rʲɑ → ˌpreˈma.rʲa   (ˈɑ→ˈa, ɑ→a)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌpreˈma.rʲa → ˌpreˈmaː.rʲa   (ˈa→ˈaː)
600: aːrʲ metathesizes to jɛːr
    ˌpreˈmaː.rʲa → ˌpreˈmjɛː.ra   (ˈaːrʲ→ˈjɛːr)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌpreˈmjɛː.ra → ˌpreˈmjie̯.ra   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌpreˈmjie̯.ra → ˌpreˈmie̯.ra   (j→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpreˈmie̯.ra → ˌpreˈmie̯.rə   (a→ə)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌpreˈmie̯.rə → ˌprəˈmie̯.rə   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌprəˈmie̯.rə → ˌprə̃ˈmie̯.rə   (ˌə→ˌə̃)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌprə̃ˈmie̯.rə → ˌprə̃ˈmje.rə   (ˈi→j, e̯→ˈe)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˌprə̃ˈmje.rə → ˌprə̃ˈmjɛ.rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌprə̃ˈmjɛ.rə → ˌprə̃ˈmjɛrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌprə̃ˈmjɛrə̯ → ˌprə̃ˈmjɛr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌprə̃ˈmjɛr → ˌpʀə̃ˈmjɛʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpʀə̃ˈmjɛʀ → pʀə̃.mjɛʀ   (ˌə̃→ə̃, ˈɛ→ɛ)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    pʀə̃.mjɛʀ → pʀə.mjɛʀ   (ə̃→ə)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀə.mjɛʀ → pʁə.mjɛʁ   (ʀ→ʁ, ʀ→ʁ)
```

## pucelle

`pˌuːlikˈellɑm` → `py.sɛl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpuː.liˈkel.lɑm → ˌpuː.lɪˈkɛl.lɑm   (i→ɪ, ˈe→ˈɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpuː.lɪˈkɛl.lɑm → ˌpu.lɪˈkɛl.lɑm   (ˌuː→ˌu)
-100: lax high vowels lower to tense mid vowels
    ˌpu.lɪˈkɛl.lɑm → ˌpu.leˈkɛl.lɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpu.leˈkɛl.lɑm → ˌpu.leˈkɛl.lɑ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌpu.leˈkɛl.lɑ → ˌpu.leˈkʲɛl.lɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌpu.leˈkʲɛl.lɑ → ˌpu.leˈcɛl.lɑ   (kʲ→c)
500: a palatal stop affricates
    ˌpu.leˈcɛl.lɑ → ˌpu.leˈt͡sʲɛl.lɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌpu.leˈt͡sʲɛl.lɑ → ˌpu.leˈt͡sʲɛl.la   (ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˌpu.leˈt͡sʲɛl.la → ˌpʉ.leˈt͡sʲɛl.la   (ˌu→ˌʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpʉ.leˈt͡sʲɛl.la → ˌpʉ.ləˈt͡sʲɛl.la   (e→ə)
600: schwa becomes non-syllabic
    ˌpʉ.ləˈt͡sʲɛl.la → ˌpʉlə̯ˈt͡sʲɛl.la   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpʉlə̯ˈt͡sʲɛl.la → ˌpʉlˈt͡sʲɛl.la   (ə̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpʉlˈt͡sʲɛl.la → ˌpʉlˈt͡sʲɛl.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˌpʉlˈt͡sʲɛl.lə → ˌpʉlˈt͡sʲɛ.lə   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌpʉlˈt͡sʲɛ.lə → ˌpʉɫˈt͡sʲɛ.lə   (l→ɫ)
1000: high round back vowels front (completion of u-fronting)
    ˌpʉɫˈt͡sʲɛ.lə → ˌpyɫˈt͡sʲɛ.lə   (ˌʉ→ˌy)
1000: back dark-l variants vocalize to w
    ˌpyɫˈt͡sʲɛ.lə → ˌpywˈt͡sʲɛ.lə   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˌpywˈt͡sʲɛ.lə → ˌpyˈt͡sʲɛ.lə   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˌpyˈt͡sʲɛ.lə → ˌpyˈsʲɛ.lə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˌpyˈsʲɛ.lə → ˌpyˈsɛ.lə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˌpyˈsɛ.lə → ˌpyˈsɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌpyˈsɛlə̯ → ˌpyˈsɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌpyˈsɛl → py.sɛl   (ˌy→y, ˈɛ→ɛ)
```

## pointure

`pˌun̪kt̪ˈuːrɑm` → `pwɛ̃.t̪yʁ`

```
-100: n assimilates to a following velar stop
    ˌpun̪kˈt̪uː.rɑm → ˌpuŋkˈt̪uː.rɑm   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpuŋkˈt̪uː.rɑm → ˌpʊŋkˈt̪uː.rɑm   (ˌu→ˌʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpʊŋkˈt̪uː.rɑm → ˌpʊŋkˈt̪u.rɑm   (ˈuː→ˈu)
-100: k lost after ŋ before a voiceless coronal
    ˌpʊŋkˈt̪u.rɑm → ˌpʊŋˈt̪u.rɑm   (k→∅)
-100: lax high vowels lower to tense mid vowels
    ˌpʊŋˈt̪u.rɑm → ˌpoŋˈt̪u.rɑm   (ˌʊ→ˌo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpoŋˈt̪u.rɑm → ˌpoŋˈt̪u.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpoŋˈt̪u.rɑ → ˌpoŋˈt̪uː.rɑ   (ˈu→ˈuː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌpoŋˈt̪uː.rɑ → ˌpũŋˈt̪uː.rɑ   (ˌo→ˌũ)
500: ŋ palatalizes to ɲ before a coronal
    ˌpũŋˈt̪uː.rɑ → ˌpũɲˈt̪uː.rɑ   (ŋ→ɲ)
500: the low vowel fronts by default
    ˌpũɲˈt̪uː.rɑ → ˌpũɲˈt̪uː.ra   (ɑ→a)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌpũɲˈt̪uː.ra → ˌpũɲˈt̪ʲuː.ra   (t̪→t̪ʲ)
500: a high tense round non-nasal vowel centralizes
    ˌpũɲˈt̪ʲuː.ra → ˌpũɲˈt̪ʲʉː.ra   (ˈuː→ˈʉː)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌpũɲˈt̪ʲʉː.ra → ˌpũɲjˈt̪ʉː.ra   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌpũɲjˈt̪ʉː.ra → ˌpũɲˈt̪ʉː.ra   (j→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpũɲˈt̪ʉː.ra → ˌpũɲˈt̪ʉː.rə   (a→ə)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˌpũɲˈt̪ʉː.rə → ˌpũj̃n̪ˈt̪ʉː.rə   (ɲ→j̃n̪)
750: vowel length resets to short
    ˌpũj̃n̪ˈt̪ʉː.rə → ˌpũj̃n̪ˈt̪ʉ.rə   (ˈʉː→ˈʉ)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌpũj̃n̪ˈt̪ʉ.rə → ˌpũj̃ˈt̪ʉ.rə   (n̪→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌpũj̃ˈt̪ʉ.rə → ˌpũj̃ˈt̪y.rə   (ˈʉ→ˈy)
1000: the nasal diphthong ũj̃ becomes wĩ (syllabicity swap before a nasal)
    ˌpũj̃ˈt̪y.rə → pwj̩̃ˈt̪y.rə   (ˌũ→w, j̃→j̩̃)
1200: nasalized ĩ lowers after w
    pwj̩̃ˈt̪y.rə → pwj̩̃ˈt̪y.rə   (j̩̃→j̩̃)
1200: a front unrounded non-low vowel laxes and lowers after w
    pwj̩̃ˈt̪y.rə → pwɛ̃ˈt̪y.rə   (j̩̃→ɛ̃)
1400: final ə becomes a non-syllabic off-glide
    pwɛ̃ˈt̪y.rə → pwɛ̃ˈt̪yrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    pwɛ̃ˈt̪yrə̯ → pwɛ̃ˈt̪yr   (ə̯→∅)
1400: r becomes uvular ʀ
    pwɛ̃ˈt̪yr → pwɛ̃ˈt̪yʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    pwɛ̃ˈt̪yʀ → pwɛ̃.t̪yʀ   (ˈy→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    pwɛ̃.t̪yʀ → pwɛ̃.t̪yʁ   (ʀ→ʁ)
```

## raine

`rˈɑːn̪ɑm` → `ʁɛn̪`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈrɑː.n̪ɑm → ˈrɑ.n̪ɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈrɑ.n̪ɑm → ˈrɑ.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈrɑ.n̪ɑ → ˈrɑː.n̪ɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈrɑː.n̪ɑ → ˈraː.n̪a   (ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˈraː.n̪a → ˈrae̯.n̪a   (ˈaː→ˈae̯)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˈrae̯.n̪a → ˈraj.n̪a   (e̯→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈraj.n̪a → ˈraj.n̪ə   (a→ə)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˈraj.n̪ə → ˈraj̃.n̪ə   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈraj̃.n̪ə → ˈrãj̃.n̪ə   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈrãj̃.n̪ə → ˈrɛ̃j̃.n̪ə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈrɛ̃j̃.n̪ə → ˈrɛ̃.n̪ə   (j̃→∅)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈrɛ̃.n̪ə → ˈrɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈrɛ.n̪ə → ˈrɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrɛn̪ə̯ → ˈrɛn̪   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrɛn̪ → ˈʀɛn̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀɛn̪ → ʀɛn̪   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀɛn̪ → ʁɛn̪   (ʀ→ʁ)
```

## rente

`rˈen̪d̪it̪ɑm` → `ʁɑ̃t̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈren̪.d̪i.t̪ɑm → ˈrɛn̪.d̪ɪ.t̪ɑm   (ˈe→ˈɛ, i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈrɛn̪.d̪ɪ.t̪ɑm → ˈrɛn̪.d̪e.t̪ɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈrɛn̪.d̪e.t̪ɑm → ˈrɛn̪.d̪e.t̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈrɛn̪.d̪e.t̪ɑ → ˈrɛn̪.d̪e.t̪a   (ɑ→a)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈrɛn̪.d̪e.t̪a → ˈrɛn̪.d̪ə.t̪a   (e→ə)
600: schwa becomes non-syllabic
    ˈrɛn̪.d̪ə.t̪a → ˈrɛn̪d̪ə̯.t̪a   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈrɛn̪d̪ə̯.t̪a → ˈrɛn̪d̪.t̪a   (ə̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈrɛn̪d̪.t̪a → ˈrɛn̪d̪.t̪ə   (a→ə)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈrɛn̪d̪.t̪ə → ˈrɛn̪.t̪ə   (d̪→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈrɛn̪.t̪ə → ˈrɛ̃n̪.t̪ə   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈrɛ̃n̪.t̪ə → ˈrãn̪.t̪ə   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈrãn̪.t̪ə → ˈrãː.t̪ə   (ˈãn̪→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈrãː.t̪ə → ˈrãːt̪ə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈrãːt̪ə̯ → ˈrɑ̃ːt̪ə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈrɑ̃ːt̪ə̯ → ˈrɑ̃ːt̪   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrɑ̃ːt̪ → ˈʀɑ̃ːt̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀɑ̃ːt̪ → ʀɑ̃ːt̪   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ʀɑ̃ːt̪ → ʀɑ̃t̪   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀɑ̃t̪ → ʁɑ̃t̪   (ʀ→ʁ)
```

## rouille

`rˌoːbˈiːkulɑm` → `ʁuj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌroːˈbiː.ku.lɑm → ˌroːˈbiː.kʊ.lɑm   (u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˌroːˈbiː.kʊ.lɑm → ˌroːˈbiː.klɑm   (ʊ→∅)
-100: b lenites to β intervocalically / before a sonorant
    ˌroːˈbiː.klɑm → ˌroːˈβiː.klɑm   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌroːˈβiː.klɑm → ˌroˈβi.klɑm   (ˌoː→ˌo, ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌroˈβi.klɑm → ˌroˈβi.klɑ   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˌroˈβi.klɑ → ˌroˈβiː.klɑ   (ˈi→ˈiː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˌroˈβiː.klɑ → ˌroˈβiː.xlɑ   (k→x)
500: a vowel shortens before a consonant cluster
    ˌroˈβiː.xlɑ → ˌroˈβi.xlɑ   (ˈiː→ˈi)
500: the low vowel fronts by default
    ˌroˈβi.xlɑ → ˌroˈβi.xla   (ɑ→a)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌroˈβi.xla → ˌroˈβi.çla   (x→ç)
500: a lateral palatalizes after a high-front consonant
    ˌroˈβi.çla → ˌroˈβi.çʎa   (l→ʎ)
600: yod lost before ʎ or palatalized r
    ˌroˈβi.çʎa → ˌroˈβi.ʎa   (ç→∅)
600: the bilabial fricative is lost between a secondary-stressed round back vowel and a front tense vowel
    ˌroˈβi.ʎa → ˌroˈi.ʎa   (β→∅)
600: a stressed vowel lengthens before a consonant + vowel
    ˌroˈi.ʎa → ˌroˈiː.ʎa   (ˈi→ˈiː)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌroˈiː.ʎa → ˌroˈiː.ʎə   (a→ə)
750: vowel length resets to short
    ˌroˈiː.ʎə → ˌroˈi.ʎə   (ˈiː→ˈi)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌroˈi.ʎə → ˌruˈi.ʎə   (ˌo→ˌu)
1400: final ə becomes a non-syllabic off-glide
    ˌruˈi.ʎə → ˌruˈiʎə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌruˈiʎə̯ → ˌruˈiʎ   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌruˈiʎ → ˌʀuˈiʎ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʀuˈiʎ → ʀu.iʎ   (ˌu→u, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀu.iʎ → ʁu.iʎ   (ʀ→ʁ)
1400: ʎ becomes j
    ʁu.iʎ → ʁu.ij   (ʎ→j)
1400: a high front vowel after another vowel is absorbed into a following j
    ʁu.ij → ʁuj   (i→∅)
```

## rousse

`rˈussɑm` → `ʁus`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈrus.sɑm → ˈrʊs.sɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈrʊs.sɑm → ˈros.sɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈros.sɑm → ˈros.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈros.sɑ → ˈros.sa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈros.sa → ˈros.sə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈros.sə → ˈro.sə   (s→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈro.sə → ˈru.sə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈru.sə → ˈrusə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrusə̯ → ˈrus   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrus → ˈʀus   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀus → ʀus   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀus → ʁus   (ʀ→ʁ)
```

## saunier

`sˌɑlin̪ˈɑːrium` → `sɔ.n̪je`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑ.liˈn̪ɑː.ri.um → ˌsɑ.lɪˈn̪ɑː.rɪ.ʊm   (i→ɪ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌsɑ.lɪˈn̪ɑː.rɪ.ʊm → ˌsɑ.lɪˈn̪ɑː.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌsɑ.lɪˈn̪ɑː.rjʊm → ˌsɑ.lɪˈn̪ɑːr.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑ.lɪˈn̪ɑːr.ʝʊm → ˌsɑ.lɪˈn̪ɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌsɑ.lɪˈn̪ɑr.ʝʊm → ˌsɑ.leˈn̪ɑr.ʝom   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɑ.leˈn̪ɑr.ʝom → ˌsɑ.leˈn̪ɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌsɑ.leˈn̪ɑr.ʝo → ˌsɑ.leˈn̪ɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌsɑ.leˈn̪ɑ.rʲo → ˌsa.leˈn̪a.rʲo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌsa.leˈn̪a.rʲo → ˌsa.leˈn̪aː.rʲo   (ˈa→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + a primary-stressed low vowel
    ˌsa.leˈn̪aː.rʲo → ˌsa.ləˈn̪aː.rʲo   (e→ə)
600: aːrʲ metathesizes to jɛːr
    ˌsa.ləˈn̪aː.rʲo → ˌsa.ləˈn̪jɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsa.ləˈn̪jɛː.ro → ˌsa.ləˈn̪jɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌsa.ləˈn̪jɛː.rə → ˌsalə̯ˈn̪jɛːrə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsalə̯ˈn̪jɛːrə̯ → ˌsalˈn̪jɛːr   (ˈə̯n̪jɛːrə̯→ˈn̪jɛːr)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌsalˈn̪jɛːr → ˌsalˈn̪jie̯r   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌsalˈn̪jie̯r → ˌsalˈn̪ie̯r   (j→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌsalˈn̪ie̯r → ˌsaɫˈn̪ie̯r   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˌsaɫˈn̪ie̯r → ˌsawˈn̪ie̯r   (ɫ→w)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌsawˈn̪ie̯r → ˌsawˈn̪jer   (ˈi→j, e̯→ˈe)
1200: aw becomes long oː
    ˌsawˈn̪jer → ˌsoːˈn̪jer   (ˌaw→ˌoː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsoːˈn̪jer → ˌsoːˈn̪jeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌsoːˈn̪jeɹ → ˌsoːˈn̪je   (ɹ→∅)
1400: back mid o opens before a consonant cluster
    ˌsoːˈn̪je → ˌsɔːˈn̪je   (ˌoː→ˌɔː)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɔːˈn̪je → sɔː.n̪je   (ˌɔː→ɔː, ˈe→e)
1400: distinctive vowel length is lost entirely
    sɔː.n̪je → sɔ.n̪je   (ɔː→ɔ)
```

## sauf

`sˈɑlwum` → `sof`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈsɑ.lwum → ˈsɑl.ɣʷum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsɑl.ɣʷum → ˈsɑl.ɣʷʊm   (u→ʊ)
-100: l darkens before a non-lateral consonant
    ˈsɑl.ɣʷʊm → ˈsɑɫ.ɣʷʊm   (l→ɫ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈsɑɫ.ɣʷʊm → ˈsɑɫ.βʷʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈsɑɫ.βʷʊm → ˈsɑɫ.βʷom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsɑɫ.βʷom → ˈsɑɫ.βʷo   (m→∅)
500: labialized bilabial fricatives delabialize
    ˈsɑɫ.βʷo → ˈsɑɫ.βo   (βʷ→β)
500: the low vowel fronts by default
    ˈsɑɫ.βo → ˈsaɫ.βo   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsaɫ.βo → ˈsaɫ.βə   (o→ə)
600: schwa becomes non-syllabic
    ˈsaɫ.βə → ˈsaɫβə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsaɫβə̯ → ˈsaɫβ   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˈsaɫβ → ˈsaɫv   (β→v)
750: all final obstruents devoice
    ˈsaɫv → ˈsaɫf   (v→f)
1000: back dark-l variants vocalize to w
    ˈsaɫf → ˈsawf   (ɫ→w)
1200: aw becomes long oː
    ˈsawf → ˈsoːf   (ˈaw→ˈoː)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈsoːf → ˈsoːfə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsoːfə̯ → ˈsoːf   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsoːf → soːf   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    soːf → sof   (oː→o)
```

## sade

`sˈɑpid̪um` → `sad̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsɑ.pi.d̪um → ˈsɑ.pɪ.d̪ʊm   (i→ɪ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈsɑ.pɪ.d̪ʊm → ˈsɑ.pe.d̪om   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsɑ.pe.d̪om → ˈsɑ.pe.d̪o   (m→∅)
300: e becomes a schwa-glide between an unrounded labial and a distributed obstruent + non-low vowel
    ˈsɑ.pe.d̪o → ˈsɑpə̯.d̪o   (e→ə̯)
300: a stressed vowel lengthens before a single consonant + glide
    ˈsɑpə̯.d̪o → ˈsɑːpə̯.d̪o   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈsɑːpə̯.d̪o → ˈsaːpə̯.d̪o   (ˈɑː→ˈaː)
600: a voiced stop spirantizes intervocalically or before r
    ˈsaːpə̯.d̪o → ˈsaːpə̯.ðo   (d̪→ð)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsaːpə̯.ðo → ˈsaːpə̯.ðə   (o→ə)
600: schwa becomes non-syllabic
    ˈsaːpə̯.ðə → ˈsaːpə̯ðə̯   (ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈsaːpə̯ðə̯ → ˈsaːpə̯.ðə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈsaːpə̯.ðə → ˈsaː.pðə   (ə̯→∅)
600: ð (plain or palatalized) hardens to d after a labial stop
    ˈsaː.pðə → ˈsaːp.d̪ə   (ð→d̪)
600: a labial consonant becomes d before a voiced coronal stop
    ˈsaːp.d̪ə → ˈsaːd̪.d̪ə   (p→d̪)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈsaːd̪.d̪ə → ˈsad̪.d̪ə   (ˈaː→ˈa)
750: a dental stop deletes before another coronal stop
    ˈsad̪.d̪ə → ˈsa.d̪ə   (d̪→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈsa.d̪ə → ˈsad̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsad̪ə̯ → ˈsad̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsad̪ → sad̪   (ˈa→a)
```

## six

`sˈeks` → `sis`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈseks → ˈsɛks   (ˈe→ˈɛ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈsɛks → ˈsɛxs   (k→x)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈsɛxs → ˈsɛçs   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈsɛçs → ˈsɛçsʲ   (s→sʲ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈsɛçsʲ → ˈsie̯çsʲ   (ˈɛ→ˈie̯)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈsie̯çsʲ → ˈsie̯çjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈsie̯çjs → ˈsie̯çs   (j→∅)
750: ç merges into ʝ
    ˈsie̯çs → ˈsie̯ʝs   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈsie̯ʝs → ˈsie̯js   (ʝ→j)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈsie̯js → ˈsijs   (e̯→∅)
1400: final obstruents are lost
    ˈsijs → ˈsij   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsij → sij   (ˈi→i)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    sij → si   (j→∅)
1500: six keeps its final s (numeral, pronounced in isolation)
    si → sis   (∅→s)
```

## sentir

`sˌen̪t̪ˈiːre` → `sɑ̃.t̪iʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsen̪ˈt̪iː.re → ˌsɛn̪ˈt̪iː.rɛ   (ˌe→ˌɛ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɛn̪ˈt̪iː.rɛ → ˌsɛn̪ˈt̪i.rɛ   (ˈiː→ˈi)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɛn̪ˈt̪i.rɛ → ˌsɛn̪ˈt̪iː.rɛ   (ˈi→ˈiː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsɛn̪ˈt̪iː.rɛ → ˌsɛn̪ˈt̪iː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsɛn̪ˈt̪iː.rə → ˌsɛn̪ˈt̪iːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsɛn̪ˈt̪iːrə̯ → ˌsɛn̪ˈt̪iːr   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌsɛn̪ˈt̪iːr → ˌsen̪ˈt̪iːr   (ˌɛ→ˌe)
750: vowel length resets to short
    ˌsen̪ˈt̪iːr → ˌsen̪ˈt̪ir   (ˈiː→ˈi)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌsen̪ˈt̪ir → ˌsẽn̪ˈt̪ir   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌsẽn̪ˈt̪ir → ˌsɛ̃n̪ˈt̪ir   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌsɛ̃n̪ˈt̪ir → ˌsãn̪ˈt̪ir   (ˌɛ̃→ˌã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsãn̪ˈt̪ir → ˌsãːˈt̪ir   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌsãːˈt̪ir → ˌsɑ̃ːˈt̪ir   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsɑ̃ːˈt̪ir → ˌsɑ̃ːˈt̪iɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌsɑ̃ːˈt̪iɹ → ˌsɑ̃ːˈt̪ir   (ɹ→r)
1400: r becomes uvular ʀ
    ˌsɑ̃ːˈt̪ir → ˌsɑ̃ːˈt̪iʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɑ̃ːˈt̪iʀ → sɑ̃ː.t̪iʀ   (ˌɑ̃ː→ɑ̃ː, ˈi→i)
1400: distinctive vowel length is lost entirely
    sɑ̃ː.t̪iʀ → sɑ̃.t̪iʀ   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɑ̃.t̪iʀ → sɑ̃.t̪iʁ   (ʀ→ʁ)
```

## soie

`sˈeːt̪ɑm` → `swa`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈseː.t̪ɑm → ˈse.t̪ɑm   (ˈeː→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈse.t̪ɑm → ˈse.t̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈse.t̪ɑ → ˈseː.t̪ɑ   (ˈe→ˈeː)
500: the low vowel fronts by default
    ˈseː.t̪ɑ → ˈseː.t̪a   (ɑ→a)
600: a voiceless consonant voices intervocalically
    ˈseː.t̪a → ˈseː.d̪a   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈseː.d̪a → ˈseː.ða   (d̪→ð)
600: long stressed vowels diphthongize
    ˈseː.ða → ˈsej.ða   (ˈeː→ˈej)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈsej.ða → ˈsej.ðə   (a→ə)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈsej.ðə → ˈsoj.ðə   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈsoj.ðə → ˈsuj.ðə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈsuj.ðə → ˈsuɛ̯.ðə   (j→ɛ̯)
1000: the interdental fricatives (plain and palatalized) efface
    ˈsuɛ̯.ðə → ˈsu.ɛ̯ə   (ð→∅)
1200: schwa desyllabifies after another vowel
    ˈsu.ɛ̯ə → ˈsuɛ̯ə̯   (ə→ə̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈsuɛ̯ə̯ → ˈswɛə̯   (ˈu→w, ɛ̯→ˈɛ)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈswɛə̯ → ˈswɛː   (ˈɛə̯→ˈɛː)
1400: stress is leveled — no longer distinctive for vowels
    ˈswɛː → swɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    swɛː → swɛ   (ɛː→ɛ)
1400: wɛ becomes wa
    swɛ → swa   (ɛ→a)
```

## sanglier

`sˌin̪gulˈɑːrem` → `sɑ̃.gle`

```
-100: n assimilates to a following velar stop
    ˌsin̪.guˈlɑː.rem → ˌsiŋ.guˈlɑː.rem   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsiŋ.guˈlɑː.rem → ˌsɪŋ.gʊˈlɑː.rɛm   (ˌi→ˌɪ, u→ʊ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɪŋ.gʊˈlɑː.rɛm → ˌsɪŋ.gʊˈlɑ.rɛm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌsɪŋ.gʊˈlɑ.rɛm → ˌseŋ.goˈlɑ.rɛm   (ˌɪ→ˌe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌseŋ.goˈlɑ.rɛm → ˌseŋ.goˈlɑ.rɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌseŋ.goˈlɑ.rɛ → ˌseŋ.goˈlɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌseŋ.goˈlɑː.rɛ → ˌseŋ.goˈlaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + a primary-stressed low vowel
    ˌseŋ.goˈlaː.rɛ → ˌseŋ.gəˈlaː.rɛ   (o→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌseŋ.gəˈlaː.rɛ → ˌseŋ.gəˈlaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌseŋ.gəˈlaː.rə → ˌseŋgə̯ˈlaːrə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌseŋgə̯ˈlaːrə̯ → ˌseŋˈglaːr   (ˈə̯laːrə̯→ˈlaːr)
600: long stressed vowels diphthongize
    ˌseŋˈglaːr → ˌseŋˈglae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌseŋˈglae̯r → ˌseŋˈgleːr   (ˈae̯→ˈeː)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌseŋˈgleːr → ˌsẽŋˈgleːr   (ˌe→ˌẽ)
1000: vowel length resets to short
    ˌsẽŋˈgleːr → ˌsẽŋˈgler   (ˈeː→ˈe)
1000: nasalized front mid vowels begin to lower
    ˌsẽŋˈgler → ˌsɛ̃ŋˈgler   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌsɛ̃ŋˈgler → ˌsãŋˈgler   (ˌɛ̃→ˌã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsãŋˈgler → ˌsãːˈgler   (ˌãŋ→ˌãː)
1400: long a becomes back ɑː
    ˌsãːˈgler → ˌsɑ̃ːˈgler   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsɑ̃ːˈgler → ˌsɑ̃ːˈgleɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌsɑ̃ːˈgleɹ → ˌsɑ̃ːˈgle   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɑ̃ːˈgle → sɑ̃ː.gle   (ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    sɑ̃ː.gle → sɑ̃.gle   (ɑ̃ː→ɑ̃)
```

## songe

`sˈomn̪ium` → `sɔ̃ʒ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsom.n̪i.um → ˈsɔm.n̪ɪ.ʊm   (ˈo→ˈɔ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈsɔm.n̪ɪ.ʊm → ˈsɔm.n̪jʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈsɔm.n̪jʊm → ˈsɔmn̪.ʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈsɔmn̪.ʝʊm → ˈsɔmn̪.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsɔmn̪.ʝom → ˈsɔmn̪.ʝo   (m→∅)
300: n assimilates to a preceding m before yod (mnj > mmj)
    ˈsɔmn̪.ʝo → ˈsɔmm.ʝo   (n̪→m)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈsɔmm.ʝo → ˈsũmm.ʝo   (ˈɔ→ˈũ)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˈsũmm.ʝo → ˈsũmm.ɟo   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈsũmm.ɟo → ˈsũmm.d͡ʒo   (ɟ→d͡ʒ)
600: m becomes n before dʒ
    ˈsũmm.d͡ʒo → ˈsũmn̪.d͡ʒo   (m→n̪)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsũmn̪.d͡ʒo → ˈsũmn̪.d͡ʒə   (o→ə)
600: schwa becomes non-syllabic
    ˈsũmn̪.d͡ʒə → ˈsũmn̪d͡ʒə̯   (ə→ə̯)
600: non-syllabic schwa restores after a postalveolar affricate
    ˈsũmn̪d͡ʒə̯ → ˈsũmn̪.d͡ʒə   (ə̯→ə)
600: n becomes m before m (recurrence)
    ˈsũmn̪.d͡ʒə → ˈsũmm.d͡ʒə   (n̪→m)
600: an identical consonant geminate reduces to one, before an obstruent or nasal
    ˈsũmm.d͡ʒə → ˈsũm.d͡ʒə   (m→∅)
1000: all affricates become sibilants (deaffrication)
    ˈsũm.d͡ʒə → ˈsũm.ʒə   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈsũm.ʒə → ˈsũː.ʒə   (ˈũm→ˈũː)
1400: final ə becomes a non-syllabic off-glide
    ˈsũː.ʒə → ˈsũːʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsũːʒə̯ → ˈsũːʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsũːʒ → sũːʒ   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    sũːʒ → sũʒ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    sũʒ → sɔ̃ʒ   (ũ→ɔ̃)
```

## époux

`spˈon̪sum` → `e.pu`

```
-100: vowel lengthens before ns when the next syllable is unstressed
    ˈspon̪.sum → ˈspoːn̪.sum   (ˈo→ˈoː)
-100: n lost after a long vowel before s (compensatory lengthening already applied)
    ˈspoːn̪.sum → ˈspoː.sum   (n̪→∅)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈspoː.sum → ˈspoː.sʊm   (u→ʊ)
-100: i-prosthesis before word-initial s + consonant
    ˈspoː.sʊm → ˌɪsˈpoː.sʊm   (∅→ˌɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɪsˈpoː.sʊm → ˌɪsˈpo.sʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ˌɪsˈpo.sʊm → ˌesˈpo.som   (ˌɪ→ˌe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌesˈpo.som → ˌesˈpo.so   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌesˈpo.so → ˌesˈpoː.so   (ˈo→ˈoː)
500: a voiceless fricative voices intervocalically
    ˌesˈpoː.so → ˌesˈpoː.zo   (s→z)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌesˈpoː.zo → ˌesˈpoː.zə   (o→ə)
600: schwa becomes non-syllabic
    ˌesˈpoː.zə → ˌesˈpoːzə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌesˈpoːzə̯ → ˌesˈpoːz   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌesˈpoːz → ˌesˈpowz   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌesˈpowz → ˌesˈpoz   (w→∅)
750: all final obstruents devoice
    ˌesˈpoz → ˌesˈpos   (z→s)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌesˈpos → ˌesˈpus   (ˈo→ˈu)
1000: s becomes x after a vowel, before any consonant
    ˌesˈpus → ˌexˈpus   (s→x)
1000: a primary-stressed vowel lengthens before word-final s
    ˌexˈpus → ˌexˈpuːs   (ˈu→ˈuː)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌexˈpuːs → ˌeːˈpuːs   (ˌex→ˌeː)
1400: final obstruents are lost
    ˌeːˈpuːs → ˌeːˈpuː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌeːˈpuː → eː.puː   (ˌeː→eː, ˈuː→uː)
1400: distinctive vowel length is lost entirely
    eː.puː → e.pu   (eː→e, uː→u)
```

## somme

`sˈummɑm` → `sɔm`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsum.mɑm → ˈsʊm.mɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈsʊm.mɑm → ˈsom.mɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsom.mɑm → ˈsom.mɑ   (m→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈsom.mɑ → ˈsũm.mɑ   (ˈo→ˈũ)
500: the low vowel fronts by default
    ˈsũm.mɑ → ˈsũm.ma   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈsũm.ma → ˈsũm.mə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈsũm.mə → ˈsũ.mə   (m→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈsũ.mə → ˈsũmə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsũmə̯ → ˈsũm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsũm → sũm   (ˈũ→ũ)
1400: nasal ũ opens to ɔ̃
    sũm → sɔ̃m   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    sɔ̃m → sɔm   (ɔ̃→ɔ)
```

## souche

`t͡sˈukkɑm` → `suʃ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt͡suk.kɑm → ˈt͡sʊk.kɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt͡sʊk.kɑm → ˈt͡sok.kɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt͡sok.kɑm → ˈt͡sok.kɑ   (m→∅)
500: the low vowel fronts by default
    ˈt͡sok.kɑ → ˈt͡sok.ka   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈt͡sok.ka → ˈt͡sok.kʲa   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈt͡sok.kʲa → ˈt͡sok.ca   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈt͡sok.ca → ˈt͡so.kt͡ʃa   (c→t͡ʃ)
600: a stop assimilates place to a following affricate (k/tʃ, g/dʒ)
    ˈt͡so.kt͡ʃa → ˈt͡so.t̪t͡ʃa   (k→t̪)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡so.t̪t͡ʃa → ˈt͡so.t̪t͡ʃə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈt͡so.t̪t͡ʃə → ˈt͡so.t͡ʃə   (t̪→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈt͡so.t͡ʃə → ˈt͡su.t͡ʃə   (ˈo→ˈu)
1000: all affricates become sibilants (deaffrication)
    ˈt͡su.t͡ʃə → ˈsu.ʃə   (t͡s→s, t͡ʃ→ʃ)
1400: final ə becomes a non-syllabic off-glide
    ˈsu.ʃə → ˈsuʃə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsuʃə̯ → ˈsuʃ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsuʃ → suʃ   (ˈu→u)
```

## talon

`t̪ˌɑlˈoːn̪em` → `t̪a.lɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪ɑˈloː.n̪em → ˌt̪ɑˈloː.n̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌt̪ɑˈloː.n̪ɛm → ˌt̪ɑˈlo.n̪ɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌt̪ɑˈlo.n̪ɛm → ˌt̪ɑˈlo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌt̪ɑˈlo.n̪ɛ → ˌt̪ɑˈloː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌt̪ɑˈloː.n̪ɛ → ˌt̪ɑˈlũː.n̪ɛ   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˌt̪ɑˈlũː.n̪ɛ → ˌt̪aˈlũː.n̪ɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪aˈlũː.n̪ɛ → ˌt̪aˈlũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt̪aˈlũː.n̪ə → ˌt̪aˈlũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪aˈlũːn̪ə̯ → ˌt̪aˈlũːn̪   (ə̯→∅)
750: vowel length resets to short
    ˌt̪aˈlũːn̪ → ˌt̪aˈlũn̪   (ˈũː→ˈũ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪aˈlũn̪ → ˌt̪aˈlũː   (ˈũn̪→ˈũː)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪aˈlũː → t̪a.lũː   (ˌa→a, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    t̪a.lũː → t̪a.lũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    t̪a.lũ → t̪a.lɔ̃   (ũ→ɔ̃)
```

## tempête

`t̪ˌempˈest̪ɑ` → `t̪ɑ̃.pɛt̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪emˈpes.t̪ɑ → ˌt̪ɛmˈpɛs.t̪ɑ   (ˌe→ˌɛ, ˈe→ˈɛ)
500: the low vowel fronts by default
    ˌt̪ɛmˈpɛs.t̪ɑ → ˌt̪ɛmˈpɛs.t̪a   (ɑ→a)
600: secondary-stressed ɛ raises to e before any two segments
    ˌt̪ɛmˈpɛs.t̪a → ˌt̪emˈpɛs.t̪a   (ˌɛ→ˌe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌt̪emˈpɛs.t̪a → ˌt̪emˈpɛs.t̪ə   (a→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌt̪emˈpɛs.t̪ə → ˌt̪ẽmˈpɛs.t̪ə   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌt̪ẽmˈpɛs.t̪ə → ˌt̪ɛ̃mˈpɛs.t̪ə   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌt̪ɛ̃mˈpɛs.t̪ə → ˌt̪ãmˈpɛs.t̪ə   (ˌɛ̃→ˌã)
1000: s becomes x after a vowel, before any consonant
    ˌt̪ãmˈpɛs.t̪ə → ˌt̪ãmˈpɛx.t̪ə   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌt̪ãmˈpɛx.t̪ə → ˌt̪ãmˈpɛː.t̪ə   (ˈɛx→ˈɛː)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪ãmˈpɛː.t̪ə → ˌt̪ãːˈpɛː.t̪ə   (ˌãm→ˌãː)
1400: final ə becomes a non-syllabic off-glide
    ˌt̪ãːˈpɛː.t̪ə → ˌt̪ãːˈpɛːt̪ə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌt̪ãːˈpɛːt̪ə̯ → ˌt̪ɑ̃ːˈpɛːt̪ə̯   (ˌãː→ˌɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˌt̪ɑ̃ːˈpɛːt̪ə̯ → ˌt̪ɑ̃ːˈpɛːt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪ɑ̃ːˈpɛːt̪ → t̪ɑ̃ː.pɛːt̪   (ˌɑ̃ː→ɑ̃ː, ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    t̪ɑ̃ː.pɛːt̪ → t̪ɑ̃.pɛt̪   (ɑ̃ː→ɑ̃, ɛː→ɛ)
```

## tieˈde

`t̪ˈepid̪um` → `t̪jɛd̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪e.pi.d̪um → ˈt̪ɛ.pɪ.d̪ʊm   (ˈe→ˈɛ, i→ɪ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪ɛ.pɪ.d̪ʊm → ˈt̪ɛ.pe.d̪om   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɛ.pe.d̪om → ˈt̪ɛ.pe.d̪o   (m→∅)
300: e becomes a schwa-glide between an unrounded labial and a distributed obstruent + non-low vowel
    ˈt̪ɛ.pe.d̪o → ˈt̪ɛpə̯.d̪o   (e→ə̯)
300: a stressed vowel lengthens before a single consonant + glide
    ˈt̪ɛpə̯.d̪o → ˈt̪ɛːpə̯.d̪o   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈt̪ɛːpə̯.d̪o → ˈt̪ie̯pə̯.d̪o   (ˈɛː→ˈie̯)
600: a voiced stop spirantizes intervocalically or before r
    ˈt̪ie̯pə̯.d̪o → ˈt̪ie̯pə̯.ðo   (d̪→ð)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ie̯pə̯.ðo → ˈt̪ie̯pə̯.ðə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪ie̯pə̯.ðə → ˈt̪ie̯pə̯ðə̯   (ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈt̪ie̯pə̯ðə̯ → ˈt̪ie̯pə̯.ðə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈt̪ie̯pə̯.ðə → ˈt̪ie̯.pðə   (ə̯→∅)
600: ð (plain or palatalized) hardens to d after a labial stop
    ˈt̪ie̯.pðə → ˈt̪ie̯p.d̪ə   (ð→d̪)
600: a labial consonant becomes d before a voiced coronal stop
    ˈt̪ie̯p.d̪ə → ˈt̪ie̯d̪.d̪ə   (p→d̪)
750: a dental stop deletes before another coronal stop
    ˈt̪ie̯d̪.d̪ə → ˈt̪ie̯.d̪ə   (d̪→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ie̯.d̪ə → ˈt̪je.d̪ə   (ˈi→j, e̯→ˈe)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈt̪je.d̪ə → ˈt̪jɛ.d̪ə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪jɛ.d̪ə → ˈt̪jɛd̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪jɛd̪ə̯ → ˈt̪jɛd̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪jɛd̪ → t̪jɛd̪   (ˈɛ→ɛ)
```

## toison

`t̪ˌoːn̪sˈjoːn̪em` → `t̪wa.zɔ̃`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌt̪oːn̪ˈsjoː.n̪em → ˌt̪oːn̪sˈʝoː.n̪em   (j→ʝ)
-100: n lost after a long vowel before s (compensatory lengthening already applied)
    ˌt̪oːn̪sˈʝoː.n̪em → ˌt̪oːsˈʝoː.n̪em   (n̪→∅)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪oːsˈʝoː.n̪em → ˌt̪oːsˈʝoː.n̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌt̪oːsˈʝoː.n̪ɛm → ˌt̪osˈʝo.n̪ɛm   (ˌoː→ˌo, ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌt̪osˈʝo.n̪ɛm → ˌt̪osˈʝo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌt̪osˈʝo.n̪ɛ → ˌt̪osˈʝoː.n̪ɛ   (ˈo→ˈoː)
500: a voiceless fricative voices before yod + a non-consonantal segment
    ˌt̪osˈʝoː.n̪ɛ → ˌt̪ozˈʝoː.n̪ɛ   (s→z)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌt̪ozˈʝoː.n̪ɛ → ˌt̪ozˈʝũː.n̪ɛ   (ˈoː→ˈũː)
500: z + yod becomes palatalized z
    ˌt̪ozˈʝũː.n̪ɛ → ˌt̪oˈzʲũː.n̪ɛ   (zʝ→zʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪oˈzʲũː.n̪ɛ → ˌt̪oˈzʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt̪oˈzʲũː.n̪ə → ˌt̪oˈzʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪oˈzʲũːn̪ə̯ → ˌt̪oˈzʲũːn̪   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌt̪oˈzʲũːn̪ → ˌt̪ojˈzũːn̪   (zʲ→jz)
750: vowel length resets to short
    ˌt̪ojˈzũːn̪ → ˌt̪ojˈzũn̪   (ˈũː→ˈũ)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌt̪ojˈzũn̪ → ˌt̪ujˈzũn̪   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌt̪ujˈzũn̪ → ˌt̪uɛ̯ˈzũn̪   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌt̪uɛ̯ˈzũn̪ → ˌt̪wɛˈzũn̪   (ˌu→w, ɛ̯→ˌɛ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪wɛˈzũn̪ → ˌt̪wɛˈzũː   (ˈũn̪→ˈũː)
1400: a vowel lengthens before an intervocalic z
    ˌt̪wɛˈzũː → ˌt̪wɛːˈzũː   (ˌɛ→ˌɛː)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪wɛːˈzũː → t̪wɛː.zũː   (ˌɛː→ɛː, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    t̪wɛː.zũː → t̪wɛ.zũ   (ɛː→ɛ, ũː→ũ)
1400: nasal ũ opens to ɔ̃
    t̪wɛ.zũ → t̪wɛ.zɔ̃   (ũ→ɔ̃)
1400: wɛ becomes wa
    t̪wɛ.zɔ̃ → t̪wa.zɔ̃   (ɛ→a)
```

## toute

`t̪ˈoːt̪t̪ɑm` → `t̪ut̪`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈt̪oːt̪.t̪ɑm → ˈt̪ot̪.t̪ɑm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ot̪.t̪ɑm → ˈt̪ot̪.t̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈt̪ot̪.t̪ɑ → ˈt̪ot̪.t̪a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt̪ot̪.t̪a → ˈt̪ot̪.t̪ə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈt̪ot̪.t̪ə → ˈt̪o.t̪ə   (t̪→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈt̪o.t̪ə → ˈt̪u.t̪ə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪u.t̪ə → ˈt̪ut̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪ut̪ə̯ → ˈt̪ut̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ut̪ → t̪ut̪   (ˈu→u)
```

## trois

`t̪rˈeːs` → `t̪ʁwa`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈt̪reːs → ˈt̪res   (ˈeː→ˈe)
300: a stressed vowel lengthens in a monosyllable before a final consonant
    ˈt̪res → ˈt̪reːs   (ˈe→ˈeː)
600: long stressed vowels diphthongize
    ˈt̪reːs → ˈt̪rejs   (ˈeː→ˈej)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈt̪rejs → ˈt̪rojs   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈt̪rojs → ˈt̪rujs   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈt̪rujs → ˈt̪ruɛ̯s   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈt̪ruɛ̯s → ˈt̪rwɛs   (ˈu→w, ɛ̯→ˈɛ)
1400: final obstruents are lost
    ˈt̪rwɛs → ˈt̪rwɛ   (s→∅)
1400: r becomes uvular ʀ
    ˈt̪rwɛ → ˈt̪ʀwɛ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ʀwɛ → t̪ʀwɛ   (ˈɛ→ɛ)
1400: wɛ becomes wa
    t̪ʀwɛ → t̪ʀwa   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪ʀwa → t̪ʁwa   (ʀ→ʁ)
```

## trogne

`t̪rˈugn̪ɑm` → `t̪ʁɔɲ`

```
-100: g assimilates to a following coronal nasal (gn cluster)
    ˈt̪ru.gn̪ɑm → ˈt̪ruŋ.n̪ɑm   (g→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪ruŋ.n̪ɑm → ˈt̪rʊŋ.n̪ɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪rʊŋ.n̪ɑm → ˈt̪roŋ.n̪ɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪roŋ.n̪ɑm → ˈt̪roŋ.n̪ɑ   (m→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈt̪roŋ.n̪ɑ → ˈt̪rũŋ.n̪ɑ   (ˈo→ˈũ)
500: ŋ palatalizes to ɲ before a coronal
    ˈt̪rũŋ.n̪ɑ → ˈt̪rũɲ.n̪ɑ   (ŋ→ɲ)
500: the low vowel fronts by default
    ˈt̪rũɲ.n̪ɑ → ˈt̪rũɲ.n̪a   (ɑ→a)
500: a nasal consonant is lost after ɲ
    ˈt̪rũɲ.n̪a → ˈt̪rũ.ɲa   (n̪→∅)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˈt̪rũ.ɲa → ˈt̪rũː.ɲa   (ˈũ→ˈũː)
600: a vowel shortens before ɲ
    ˈt̪rũː.ɲa → ˈt̪rũ.ɲa   (ˈũː→ˈũ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt̪rũ.ɲa → ˈt̪rũ.ɲə   (a→ə)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪rũ.ɲə → ˈt̪rũɲə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪rũɲə̯ → ˈt̪rũɲ   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈt̪rũɲ → ˈt̪ʀũɲ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ʀũɲ → t̪ʀũɲ   (ˈũ→ũ)
1400: nasal ũ opens to ɔ̃
    t̪ʀũɲ → t̪ʀɔ̃ɲ   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    t̪ʀɔ̃ɲ → t̪ʀɔɲ   (ɔ̃→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪ʀɔɲ → t̪ʁɔɲ   (ʀ→ʁ)
```

## tien

`t̪ˈeum` → `t̪jø`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪e.um → ˈt̪ɛ.ʊm   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪ɛ.ʊm → ˈt̪ɛ.om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɛ.om → ˈt̪ɛ.o   (m→∅)
300: a stressed vowel lengthens before another vowel
    ˈt̪ɛ.o → ˈt̪ɛː.o   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈt̪ɛː.o → ˈt̪i.e̯o   (ˈɛː→ˈie̯)
500: an unstressed back round non-low vowel becomes a glide in hiatus after a stressed vowel
    ˈt̪i.e̯o → ˈt̪ie̯u̯   (o→u̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ie̯u̯ → ˈt̪jeu̯   (ˈi→j, e̯→ˈe)
1000: ew becomes øw
    ˈt̪jeu̯ → ˈt̪jøu̯   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈt̪jøu̯ → ˈt̪jø   (u̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪jø → t̪jø   (ˈø→ø)
```

## outil

`ˌusit̪ˈiːlium` → `u.t̪i`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌu.siˈt̪iː.li.um → ˌʊ.sɪˈt̪iː.lɪ.ʊm   (ˌu→ˌʊ, i→ɪ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌʊ.sɪˈt̪iː.lɪ.ʊm → ˌʊ.sɪˈt̪iː.ljʊm   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˌʊ.sɪˈt̪iː.ljʊm → ˌʊ.sɪˈt̪iː.ɫjʊm   (l→ɫ)
-100: yod strengthens before a vowel
    ˌʊ.sɪˈt̪iː.ɫjʊm → ˌʊ.sɪˈt̪iːɫ.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌʊ.sɪˈt̪iːɫ.ʝʊm → ˌʊ.sɪˈt̪iɫ.ʝʊm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌʊ.sɪˈt̪iɫ.ʝʊm → ˌo.seˈt̪iɫ.ʝom   (ˌʊ→ˌo, ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌo.seˈt̪iɫ.ʝom → ˌo.seˈt̪iɫ.ʝo   (m→∅)
300: l palatalizes to ʎ before yod
    ˌo.seˈt̪iɫ.ʝo → ˌo.seˈt̪i.ʎo   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌo.seˈt̪i.ʎo → ˌo.seˈt̪iː.ʎo   (ˈi→ˈiː)
500: a voiceless fricative voices intervocalically
    ˌo.seˈt̪iː.ʎo → ˌo.zeˈt̪iː.ʎo   (s→z)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌo.zeˈt̪iː.ʎo → ˌo.zəˈt̪iː.ʎə   (e→ə, o→ə)
600: schwa becomes non-syllabic
    ˌo.zəˈt̪iː.ʎə → ˌozə̯ˈt̪iːʎə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌozə̯ˈt̪iːʎə̯ → ˌozˈt̪iːʎ   (ˈə̯t̪iːʎə̯→ˈt̪iːʎ)
750: vowel length resets to short
    ˌozˈt̪iːʎ → ˌozˈt̪iʎ   (ˈiː→ˈi)
1000: a stressed vowel lengthens before z + one consonant + a vowel
    ˌozˈt̪iʎ → ˌoːzˈt̪iʎ   (ˌo→ˌoː)
1000: z is lost before a consonant (preconsonantal effacement)
    ˌoːzˈt̪iʎ → ˌoːˈt̪iʎ   (z→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌoːˈt̪iʎ → ˌuːˈt̪iʎ   (ˌoː→ˌuː)
1400: stress is leveled — no longer distinctive for vowels
    ˌuːˈt̪iʎ → uː.t̪iʎ   (ˌuː→uː, ˈi→i)
1400: distinctive vowel length is lost entirely
    uː.t̪iʎ → u.t̪iʎ   (uː→u)
1400: ʎ becomes j
    u.t̪iʎ → u.t̪ij   (ʎ→j)
1500: outil has a silent final l (no yod), unlike fille
    u.t̪ij → u.t̪i   (j→∅)
```

## vanneau

`wˈɑn̪n̪ˌellum` → `va.n̪o`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwɑn̪ˌn̪el.lum → ˈɣʷɑn̪ˌn̪el.lum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷɑn̪ˌn̪el.lum → ˈɣʷɑn̪ˌn̪ɛl.lʊm   (ˌe→ˌɛ, u→ʊ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɑn̪ˌn̪ɛl.lʊm → ˈβʷɑn̪ˌn̪ɛl.lʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɑn̪ˌn̪ɛl.lʊm → ˈβʷɑn̪ˌn̪ɛl.lom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷɑn̪ˌn̪ɛl.lom → ˈβʷɑn̪ˌn̪ɛl.lo   (m→∅)
500: labialized bilabial fricatives delabialize
    ˈβʷɑn̪ˌn̪ɛl.lo → ˈβɑn̪ˌn̪ɛl.lo   (βʷ→β)
500: the low vowel fronts by default
    ˈβɑn̪ˌn̪ɛl.lo → ˈβan̪ˌn̪ɛl.lo   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβan̪ˌn̪ɛl.lo → ˈβan̪ˌn̪ɛl.lə   (o→ə)
600: schwa becomes non-syllabic
    ˈβan̪ˌn̪ɛl.lə → ˈβan̪ˌn̪ɛllə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈβan̪ˌn̪ɛllə̯ → ˈβan̪ˌn̪ɛll   (ə̯→∅)
600: secondary-stressed ɛ/ɔ raise before a lateral + consonant
    ˈβan̪ˌn̪ɛll → ˈβan̪ˌn̪ɨll   (ˌɛ→ˌɨ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˈβan̪ˌn̪ɨll → ˈβan̪ˌn̪ɛll   (ˌɨ→ˌɛ)
600: the remaining bilabial fricative becomes v
    ˈβan̪ˌn̪ɛll → ˈvan̪ˌn̪ɛll   (β→v)
750: an identical consonant geminate reduces to one (recurrence)
    ˈvan̪ˌn̪ɛll → ˈvaˌn̪ɛl   (ˌn̪ɛl→ˌɛ)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈvaˌn̪ɛl → ˈvãˌn̪ɛl   (ˈa→ˈã)
1000: final l labializes after a short mid vowel
    ˈvãˌn̪ɛl → ˈvãˌn̪ɛɫ   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˈvãˌn̪ɛɫ → ˈvãˌn̪ɛw   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˈvãˌn̪ɛw → ˈvãˌn̪ɛa̯w   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈvãˌn̪ɛa̯w → ˈvãˌn̪e̯aw   (ˌɛ→e̯, a̯→ˌa)
1200: aw becomes long oː
    ˈvãˌn̪e̯aw → ˈvãˌn̪e̯oː   (ˌaw→ˌoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˈvãˌn̪e̯oː → ˈvãˌn̪ə̯oː   (e̯→ə̯)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈvãˌn̪ə̯oː → ˈvãˌn̪oː   (ə̯→∅)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˈvãˌn̪oː → ˈvaˌn̪oː   (ˈã→ˈa)
1400: stress is leveled — no longer distinctive for vowels
    ˈvaˌn̪oː → va.n̪oː   (ˈa→a, ˌoː→oː)
1400: distinctive vowel length is lost entirely
    va.n̪oː → va.n̪o   (oː→o)
```

## vautre

`wˈelt̪rɑgum` → `vjœt̪ʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwel.t̪rɑ.gum → ˈɣʷel.t̪rɑ.gum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷel.t̪rɑ.gum → ˈɣʷɛl.t̪rɑ.gʊm   (ˈe→ˈɛ, u→ʊ)
-100: l darkens before a non-lateral consonant
    ˈɣʷɛl.t̪rɑ.gʊm → ˈɣʷɛɫ.t̪rɑ.gʊm   (l→ɫ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɛɫ.t̪rɑ.gʊm → ˈβʷɛɫ.t̪rɑ.gʊm   (ɣʷ→βʷ)
-100: unstressed g deleted between an unstressed vowel and the following unstressed syllable
    ˈβʷɛɫ.t̪rɑ.gʊm → ˈβʷɛɫ.t̪rʊm   (ɑg→∅)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɛɫ.t̪rʊm → ˈβʷɛɫ.t̪rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷɛɫ.t̪rom → ˈβʷɛɫ.t̪ro   (m→∅)
500: labialized bilabial fricatives delabialize
    ˈβʷɛɫ.t̪ro → ˈβɛɫ.t̪ro   (βʷ→β)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈβɛɫ.t̪ro → ˈβɛɫ.t̪ʲro   (t̪→t̪ʲ)
500: stressed ɛ diphthongizes to ie̯ before a coronal non-nasal consonant + high-front stop
    ˈβɛɫ.t̪ʲro → ˈβie̯ɫ.t̪ʲro   (ˈɛ→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβie̯ɫ.t̪ʲro → ˈβie̯ɫ.t̪ʲrə   (o→ə)
600: schwa becomes non-syllabic
    ˈβie̯ɫ.t̪ʲrə → ˈβie̯ɫt̪ʲrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈβie̯ɫt̪ʲrə̯ → ˈβie̯ɫt̪ʲr   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈβie̯ɫt̪ʲr → ˈβie̯ɫ.t̪ʲrə   (∅→ə)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈβie̯ɫ.t̪ʲrə → ˈβie̯ɫ.t̪ʲrʲə   (r→rʲ)
600: palatalized r depalatalizes
    ˈβie̯ɫ.t̪ʲrʲə → ˈβie̯ɫ.t̪ʲrə   (rʲ→r)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈβie̯ɫ.t̪ʲrə → ˈβie̯ɫj.t̪rə   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈβie̯ɫj.t̪rə → ˈβie̯ɫ.t̪rə   (j→∅)
600: the remaining bilabial fricative becomes v
    ˈβie̯ɫ.t̪rə → ˈvie̯ɫ.t̪rə   (β→v)
1000: back dark-l variants vocalize to w
    ˈvie̯ɫ.t̪rə → ˈvie̯w.t̪rə   (ɫ→w)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈvie̯w.t̪rə → ˈvjew.t̪rə   (ˈi→j, e̯→ˈe)
1000: ew becomes øw
    ˈvjew.t̪rə → ˈvjøw.t̪rə   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈvjøw.t̪rə → ˈvjø.t̪rə   (w→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈvjø.t̪rə → ˈvjøt̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈvjøt̪rə̯ → ˈvjøt̪r   (ə̯→∅)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈvjøt̪r → ˈvjœt̪r   (ˈø→ˈœ)
1400: r becomes uvular ʀ
    ˈvjœt̪r → ˈvjœt̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈvjœt̪ʀ → vjœt̪ʀ   (ˈœ→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    vjœt̪ʀ → vjœt̪ʁ   (ʀ→ʁ)
```

## vermeil

`wˌermˈikulum` → `vɛ.ʁmɛj`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌwerˈmi.ku.lum → ˌɣʷerˈmi.ku.lum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɣʷerˈmi.ku.lum → ˌɣʷɛrˈmɪ.kʊ.lʊm   (ˌe→ˌɛ, ˈi→ˈɪ, u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˌɣʷɛrˈmɪ.kʊ.lʊm → ˌɣʷɛrˈmɪ.klʊm   (ʊ→∅)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɣʷɛrˈmɪ.klʊm → ˌβʷɛrˈmɪ.klʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˌβʷɛrˈmɪ.klʊm → ˌβʷɛrˈme.klom   (ˈɪ→ˈe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌβʷɛrˈme.klom → ˌβʷɛrˈme.klo   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˌβʷɛrˈme.klo → ˌβʷɛrˈmeː.klo   (ˈe→ˈeː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˌβʷɛrˈmeː.klo → ˌβʷɛrˈmeː.xlo   (k→x)
500: a vowel shortens before a consonant cluster
    ˌβʷɛrˈmeː.xlo → ˌβʷɛrˈme.xlo   (ˈeː→ˈe)
500: labialized bilabial fricatives delabialize
    ˌβʷɛrˈme.xlo → ˌβɛrˈme.xlo   (βʷ→β)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌβɛrˈme.xlo → ˌβɛrˈme.çlo   (x→ç)
500: a lateral palatalizes after a high-front consonant
    ˌβɛrˈme.çlo → ˌβɛrˈme.çʎo   (l→ʎ)
600: yod lost before ʎ or palatalized r
    ˌβɛrˈme.çʎo → ˌβɛrˈme.ʎo   (ç→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌβɛrˈme.ʎo → ˌβɛrˈme.ʎə   (o→ə)
600: schwa becomes non-syllabic
    ˌβɛrˈme.ʎə → ˌβɛrˈmeʎə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌβɛrˈmeʎə̯ → ˌβɛrˈmeʎ   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌβɛrˈmeʎ → ˌβerˈmeʎ   (ˌɛ→ˌe)
600: the remaining bilabial fricative becomes v
    ˌβerˈmeʎ → ˌverˈmeʎ   (β→v)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌverˈmeʎ → ˌvɛrˈmeʎ   (ˌe→ˌɛ)
1400: e lowers to ɛ before a lateral
    ˌvɛrˈmeʎ → ˌvɛrˈmɛʎ   (ˈe→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌvɛrˈmɛʎ → ˌvɛɹˈmɛʎ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌvɛɹˈmɛʎ → ˌvɛrˈmɛʎ   (ɹ→r)
1400: r becomes uvular ʀ
    ˌvɛrˈmɛʎ → ˌvɛʀˈmɛʎ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌvɛʀˈmɛʎ → vɛʀ.mɛʎ   (ˌɛ→ɛ, ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    vɛʀ.mɛʎ → vɛ.ʁmɛʎ   (ʀ→ʁ)
1400: ʎ becomes j
    vɛ.ʁmɛʎ → vɛ.ʁmɛj   (ʎ→j)
```

## vieux

`wˈet̪ulus` → `vjø`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwe.t̪u.lus → ˈɣʷe.t̪u.lus   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷe.t̪u.lus → ˈɣʷɛ.t̪ʊ.lʊs   (ˈe→ˈɛ, u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈɣʷɛ.t̪ʊ.lʊs → ˈɣʷɛ.t̪lʊs   (ʊ→∅)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɛ.t̪lʊs → ˈβʷɛ.t̪lʊs   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɛ.t̪lʊs → ˈβʷɛ.t̪los   (ʊ→o)
-100: t becomes k before a lateral
    ˈβʷɛ.t̪los → ˈβʷɛ.klos   (t̪→k)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈβʷɛ.klos → ˈβʷɛː.klos   (ˈɛ→ˈɛː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˈβʷɛː.klos → ˈβʷɛː.xlos   (k→x)
500: a vowel shortens before a consonant cluster
    ˈβʷɛː.xlos → ˈβʷɛ.xlos   (ˈɛː→ˈɛ)
500: labialized bilabial fricatives delabialize
    ˈβʷɛ.xlos → ˈβɛ.xlos   (βʷ→β)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈβɛ.xlos → ˈβɛ.çlos   (x→ç)
500: a lateral palatalizes after a high-front consonant
    ˈβɛ.çlos → ˈβɛ.çʎos   (l→ʎ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈβɛ.çʎos → ˈβie̯.çʎos   (ˈɛ→ˈie̯)
600: yod lost before ʎ or palatalized r
    ˈβie̯.çʎos → ˈβie̯.ʎos   (ç→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβie̯.ʎos → ˈβie̯.ʎəs   (o→ə)
600: schwa becomes non-syllabic
    ˈβie̯.ʎəs → ˈβie̯ʎə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈβie̯ʎə̯s → ˈβie̯ʎs   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈβie̯ʎs → ˈβie̯ʎsʲ   (s→sʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈβie̯ʎsʲ → ˈβie̯ʎjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈβie̯ʎjs → ˈβie̯ʎs   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈβie̯ʎs → ˈβie̯ʎt͡sʲ   (s→t͡sʲ)
600: the remaining bilabial fricative becomes v
    ˈβie̯ʎt͡sʲ → ˈvie̯ʎt͡sʲ   (β→v)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈvie̯ʎt͡sʲ → ˈvie̯ɫt͡sʲ   (ʎ→ɫ)
1000: back dark-l variants vocalize to w
    ˈvie̯ɫt͡sʲ → ˈvie̯wt͡sʲ   (ɫ→w)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈvie̯wt͡sʲ → ˈvjewt͡sʲ   (ˈi→j, e̯→ˈe)
1000: ew becomes øw
    ˈvjewt͡sʲ → ˈvjøwt͡sʲ   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈvjøwt͡sʲ → ˈvjøt͡sʲ   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˈvjøt͡sʲ → ˈvjøsʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈvjøsʲ → ˈvjøs   (sʲ→s)
1400: final obstruents are lost
    ˈvjøs → ˈvjø   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈvjø → vjø   (ˈø→ø)
```

## ville

`wˈiːllɑm` → `vil`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwiːl.lɑm → ˈɣʷiːl.lɑm   (w→ɣʷ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷiːl.lɑm → ˈβʷiːl.lɑm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˈβʷiːl.lɑm → ˈβʷil.lɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷil.lɑm → ˈβʷil.lɑ   (m→∅)
500: labialized bilabial fricatives delabialize
    ˈβʷil.lɑ → ˈβil.lɑ   (βʷ→β)
500: the low vowel fronts by default
    ˈβil.lɑ → ˈβil.la   (ɑ→a)
600: the remaining bilabial fricative becomes v
    ˈβil.la → ˈvil.la   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈvil.la → ˈvil.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈvil.lə → ˈvi.lə   (l→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈvi.lə → ˈvilə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈvilə̯ → ˈvil   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈvil → vil   (ˈi→i)
```

## verge

`wˈirgɑm` → `vɛʁʒ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwir.gɑm → ˈɣʷir.gɑm   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷir.gɑm → ˈɣʷɪr.gɑm   (ˈi→ˈɪ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɪr.gɑm → ˈβʷɪr.gɑm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɪr.gɑm → ˈβʷer.gɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷer.gɑm → ˈβʷer.gɑ   (m→∅)
500: labialized bilabial fricatives delabialize
    ˈβʷer.gɑ → ˈβer.gɑ   (βʷ→β)
500: the low vowel fronts by default
    ˈβer.gɑ → ˈβer.ga   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈβer.ga → ˈβer.gʲa   (g→gʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈβer.gʲa → ˈβer.ɟa   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈβer.ɟa → ˈβer.d͡ʒa   (ɟ→d͡ʒ)
600: the remaining bilabial fricative becomes v
    ˈβer.d͡ʒa → ˈver.d͡ʒa   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈver.d͡ʒa → ˈver.d͡ʒə   (a→ə)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˈver.d͡ʒə → ˈvɛr.d͡ʒə   (ˈe→ˈɛ)
1000: all affricates become sibilants (deaffrication)
    ˈvɛr.d͡ʒə → ˈvɛr.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈvɛr.ʒə → ˈvɛrʒə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈvɛrʒə̯ → ˈvɛɹʒə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈvɛɹʒə̯ → ˈvɛɹʒ   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈvɛɹʒ → ˈvɛrʒ   (ɹ→r)
1400: r becomes uvular ʀ
    ˈvɛrʒ → ˈvɛʀʒ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈvɛʀʒ → vɛʀʒ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    vɛʀʒ → vɛʁʒ   (ʀ→ʁ)
```

## abbesse

`ˌɑbbɑːt̪ˈissɑm` → `a.bɛs`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑb.bɑːˈt̪is.sɑm → ˌɑb.bɑːˈt̪ɪs.sɑm   (ˈi→ˈɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑb.bɑːˈt̪ɪs.sɑm → ˌɑb.bɑˈt̪ɪs.sɑm   (ɑː→ɑ)
-100: lax high vowels lower to tense mid vowels
    ˌɑb.bɑˈt̪ɪs.sɑm → ˌɑb.bɑˈt̪es.sɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑb.bɑˈt̪es.sɑm → ˌɑb.bɑˈt̪es.sɑ   (m→∅)
500: the low vowel fronts by default
    ˌɑb.bɑˈt̪es.sɑ → ˌab.baˈt̪es.sa   (ˌɑ→ˌa, ɑ→a, ɑ→a)
600: a voiceless consonant voices intervocalically
    ˌab.baˈt̪es.sa → ˌab.baˈd̪es.sa   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌab.baˈd̪es.sa → ˌab.baˈðes.sa   (d̪→ð)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌab.baˈðes.sa → ˌab.bəˈðes.sə   (a→ə, a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˌab.bəˈðes.sə → ˌa.bəˈðe.sə   (bəˈðes→əˈðe)
1000: stressed e laxes to ɛ before a consonant + vowel
    ˌa.bəˈðe.sə → ˌa.bəˈðɛ.sə   (ˈe→ˈɛ)
1000: the interdental fricatives (plain and palatalized) efface
    ˌa.bəˈðɛ.sə → ˌa.bəˈɛ.sə   (ð→∅)
1000: a front unrounded vowel lengthens before s + final schwa
    ˌa.bəˈɛ.sə → ˌa.bəˈɛː.sə   (ˈɛ→ˈɛː)
1200: a stressless schwa desyllabifies before another vowel
    ˌa.bəˈɛː.sə → ˌaˈbə̯ɛː.sə   (ə→ə̯)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌaˈbə̯ɛː.sə → ˌaˈbɛː.sə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌaˈbɛː.sə → ˌaˈbɛːsə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌaˈbɛːsə̯ → ˌaˈbɛːs   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈbɛːs → a.bɛːs   (ˌa→a, ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    a.bɛːs → a.bɛs   (ɛː→ɛ)
```

## arceau

`ˌɑrkˈellum` → `aʁ.so`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑrˈkel.lum → ˌɑrˈkɛl.lʊm   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˌɑrˈkɛl.lʊm → ˌɑrˈkɛl.lom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑrˈkɛl.lom → ˌɑrˈkɛl.lo   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌɑrˈkɛl.lo → ˌɑrˈkʲɛl.lo   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌɑrˈkʲɛl.lo → ˌɑrˈcɛl.lo   (kʲ→c)
500: a palatal stop affricates
    ˌɑrˈcɛl.lo → ˌɑrˈt͡sʲɛl.lo   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌɑrˈt͡sʲɛl.lo → ˌarˈt͡sʲɛl.lo   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌarˈt͡sʲɛl.lo → ˌarˈt͡sʲɛl.lə   (o→ə)
600: schwa becomes non-syllabic
    ˌarˈt͡sʲɛl.lə → ˌarˈt͡sʲɛllə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌarˈt͡sʲɛllə̯ → ˌarˈt͡sʲɛll   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˌarˈt͡sʲɛll → ˌarˈt͡sʲɛl   (l→∅)
1000: final l labializes after a short mid vowel
    ˌarˈt͡sʲɛl → ˌarˈt͡sʲɛɫ   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˌarˈt͡sʲɛɫ → ˌarˈt͡sʲɛw   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌarˈt͡sʲɛw → ˌarˈt͡sʲɛa̯w   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌarˈt͡sʲɛa̯w → ˌarˈt͡sʲe̯aw   (ˈɛ→e̯, a̯→ˈa)
1000: all affricates become sibilants (deaffrication)
    ˌarˈt͡sʲe̯aw → ˌarˈsʲe̯aw   (t͡sʲ→sʲ)
1200: aw becomes long oː
    ˌarˈsʲe̯aw → ˌarˈsʲe̯oː   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌarˈsʲe̯oː → ˌarˈsʲə̯oː   (e̯→ə̯)
1200: the remaining anterior palatalized consonants depalatalize
    ˌarˈsʲə̯oː → ˌarˈsə̯oː   (sʲ→s)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌarˈsə̯oː → ˌarˈsoː   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌarˈsoː → ˌaɹˈsoː   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌaɹˈsoː → ˌarˈsoː   (ɹ→r)
1400: r becomes uvular ʀ
    ˌarˈsoː → ˌaʀˈsoː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌaʀˈsoː → aʀ.soː   (ˌa→a, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    aʀ.soː → aʀ.so   (oː→o)
1400: the uvular trill ʀ becomes a fricative ʁ
    aʀ.so → aʁ.so   (ʀ→ʁ)
```

## bourgeon

`bˌurriˈoːn̪em` → `buʁ.ʒɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌbur.riˈoː.n̪em → ˌbʊr.rɪˈoː.n̪ɛm   (ˌu→ˌʊ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌbʊr.rɪˈoː.n̪ɛm → ˌbʊrˈrjoː.n̪ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌbʊrˈrjoː.n̪ɛm → ˌbʊrrˈʝoː.n̪ɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌbʊrrˈʝoː.n̪ɛm → ˌbʊrrˈʝo.n̪ɛm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ˌbʊrrˈʝo.n̪ɛm → ˌborrˈʝo.n̪ɛm   (ˌʊ→ˌo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌborrˈʝo.n̪ɛm → ˌborrˈʝo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌborrˈʝo.n̪ɛ → ˌborrˈʝoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌborrˈʝoː.n̪ɛ → ˌborrˈʝũː.n̪ɛ   (ˈoː→ˈũː)
500: yod hardens to ɟ after geminate r
    ˌborrˈʝũː.n̪ɛ → ˌborrˈɟũː.n̪ɛ   (ʝ→ɟ)
500: a palatal stop affricates
    ˌborrˈɟũː.n̪ɛ → ˌborrˈd͡ʒũː.n̪ɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌborrˈd͡ʒũː.n̪ɛ → ˌborrˈd͡ʒũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌborrˈd͡ʒũː.n̪ə → ˌborrˈd͡ʒũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌborrˈd͡ʒũːn̪ə̯ → ˌborrˈd͡ʒũːn̪   (ə̯→∅)
600: an identical consonant geminate reduces to one, before an obstruent or nasal
    ˌborrˈd͡ʒũːn̪ → ˌborˈd͡ʒũːn̪   (r→∅)
750: vowel length resets to short
    ˌborˈd͡ʒũːn̪ → ˌborˈd͡ʒũn̪   (ˈũː→ˈũ)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌborˈd͡ʒũn̪ → ˌburˈd͡ʒũn̪   (ˌo→ˌu)
1000: all affricates become sibilants (deaffrication)
    ˌburˈd͡ʒũn̪ → ˌburˈʒũn̪   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌburˈʒũn̪ → ˌburˈʒũː   (ˈũn̪→ˈũː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌburˈʒũː → ˌbuɹˈʒũː   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌbuɹˈʒũː → ˌburˈʒũː   (ɹ→r)
1400: r becomes uvular ʀ
    ˌburˈʒũː → ˌbuʀˈʒũː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌbuʀˈʒũː → buʀ.ʒũː   (ˌu→u, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    buʀ.ʒũː → buʀ.ʒũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    buʀ.ʒũ → buʀ.ʒɔ̃   (ũ→ɔ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    buʀ.ʒɔ̃ → buʁ.ʒɔ̃   (ʀ→ʁ)
```

## fou

`fˈɑgum` → `fu`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfɑ.gum → ˈfɑ.gʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈfɑ.gʊm → ˈfɑ.gom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɑ.gom → ˈfɑ.go   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈfɑ.go → ˈfɑ.ɣo   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfɑ.ɣo → ˈfɑː.ɣo   (ˈɑ→ˈɑː)
500: the early Gallo-Roman velar fricative is lost before a tense round vowel
    ˈfɑː.ɣo → ˈfɑː.o   (ɣ→∅)
500: the low vowel fronts by default
    ˈfɑː.o → ˈfaː.o   (ˈɑː→ˈaː)
500: an unstressed back round non-low vowel becomes a glide in hiatus after a stressed vowel
    ˈfaː.o → ˈfaːu̯   (o→u̯)
500: a vowel shortens before the high back round glide (w)
    ˈfaːu̯ → ˈfau̯   (ˈaː→ˈa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈfau̯ → ˈfɔu̯   (ˈa→ˈɔ)
1200: the ow diphthong monophthongizes to u
    ˈfɔu̯ → ˈfu   (ˈɔu̯→ˈu)
1400: stress is leveled — no longer distinctive for vowels
    ˈfu → fu   (ˈu→u)
```

## joie

`gˈɑwd̪iɑm` → `ʒɔʒ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgɑw.d̪i.ɑm → ˈgɑw.d̪ɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈgɑw.d̪ɪ.ɑm → ˈgɑw.d̪jɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈgɑw.d̪jɑm → ˈgɑw.d̪ʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgɑw.d̪ʝɑm → ˈgɑw.d̪ʝɑ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈgɑw.d̪ʝɑ → ˈgɑw.ɟʝɑ   (d̪→ɟ)
300: yod absorbed into a preceding palatalized consonant
    ˈgɑw.ɟʝɑ → ˈgɑw.ɟɑ   (ʝ→∅)
500: a palatal stop affricates
    ˈgɑw.ɟɑ → ˈgɑw.d͡ʒɑ   (ɟ→d͡ʒ)
500: the low vowel fronts by default
    ˈgɑw.d͡ʒɑ → ˈgaw.d͡ʒa   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈgaw.d͡ʒa → ˈgʲaw.d͡ʒa   (g→gʲ)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈgʲaw.d͡ʒa → ˈgʲɔw.d͡ʒa   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈgʲɔw.d͡ʒa → ˈɟɔw.d͡ʒa   (gʲ→ɟ)
600: a voiced stop spirantizes intervocalically or before r
    ˈɟɔw.d͡ʒa → ˈɟɔw.ʒa   (d͡ʒ→ʒ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟɔw.ʒa → ˈd͡ʒɔw.ʒa   (ɟ→d͡ʒ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈd͡ʒɔw.ʒa → ˈd͡ʒɔ.ʒa   (w→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd͡ʒɔ.ʒa → ˈd͡ʒɔ.ʒə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒɔ.ʒə → ˈʒɔ.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈʒɔ.ʒə → ˈʒɔʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʒɔʒə̯ → ˈʒɔʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒɔʒ → ʒɔʒ   (ˈɔ→ɔ)
```

## juin

`iˈuːn̪ium` → `ʒɥɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    iˈuː.n̪i.um → ɪˈuː.n̪ɪ.ʊm   (i→ɪ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ɪˈuː.n̪ɪ.ʊm → ˈjuː.n̪jʊm   (ɪ→j, ɪ→j)
-100: yod strengthens before a vowel
    ˈjuː.n̪jʊm → ˈʝuːn̪.ʝʊm   (j→ʝ, j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈʝuːn̪.ʝʊm → ˈʝun̪.ʝʊm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˈʝun̪.ʝʊm → ˈʝun̪.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈʝun̪.ʝom → ˈʝun̪.ʝo   (m→∅)
300: the coronal nasal palatalizes before yod
    ˈʝun̪.ʝo → ˈʝu.ɲo   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈʝu.ɲo → ˈʝuː.ɲo   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈʝuː.ɲo → ˈʝʉː.ɲo   (ˈuː→ˈʉː)
600: yod hardens to ɟ word-initially before a vowel
    ˈʝʉː.ɲo → ˈɟʉː.ɲo   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟʉː.ɲo → ˈd͡ʒʉː.ɲo   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd͡ʒʉː.ɲo → ˈd͡ʒʉː.ɲə   (o→ə)
600: schwa becomes non-syllabic
    ˈd͡ʒʉː.ɲə → ˈd͡ʒʉːɲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd͡ʒʉːɲə̯ → ˈd͡ʒʉːɲ   (ə̯→∅)
600: a vowel shortens before ɲ
    ˈd͡ʒʉːɲ → ˈd͡ʒʉɲ   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈd͡ʒʉɲ → ˈd͡ʒyɲ   (ˈʉ→ˈy)
1000: word-final ɲ ejects a nasalized j after a tense vowel
    ˈd͡ʒyɲ → ˈd͡ʒyj̃ɲ   (∅→j̃)
1000: the nasal diphthong ũj̃ becomes wĩ (syllabicity swap before a nasal)
    ˈd͡ʒyj̃ɲ → d͡ʒɥj̩̃ɲ   (ˈy→ɥ, j̃→j̩̃)
1000: all affricates become sibilants (deaffrication)
    d͡ʒɥj̩̃ɲ → ʒɥj̩̃ɲ   (d͡ʒ→ʒ)
1200: final ɲ becomes n
    ʒɥj̩̃ɲ → ʒɥj̩̃n̪   (ɲ→n̪)
1200: nasalized ĩ lowers to ẽ
    ʒɥj̩̃n̪ → ʒɥj̩̃n̪   (j̩̃→j̩̃)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ʒɥj̩̃n̪ → ʒɥj̩̃ː   (j̩̃n̪→j̩̃ː)
1400: nasalized ẽ lowers to ɛ̃
    ʒɥj̩̃ː → ʒɥɛ̃ː   (j̩̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    ʒɥɛ̃ː → ʒɥɛ̃   (ɛ̃ː→ɛ̃)
```

## certe

`kˈert̪ɑm` → `sɛʁt̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈker.t̪ɑm → ˈkɛr.t̪ɑm   (ˈe→ˈɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɛr.t̪ɑm → ˈkɛr.t̪ɑ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈkɛr.t̪ɑ → ˈkʲɛr.t̪ɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkʲɛr.t̪ɑ → ˈcɛr.t̪ɑ   (kʲ→c)
500: a palatal stop affricates
    ˈcɛr.t̪ɑ → ˈt͡sʲɛr.t̪ɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˈt͡sʲɛr.t̪ɑ → ˈt͡sʲɛr.t̪a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡sʲɛr.t̪a → ˈt͡sʲɛr.t̪ə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲɛr.t̪ə → ˈsʲɛr.t̪ə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲɛr.t̪ə → ˈsɛr.t̪ə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈsɛr.t̪ə → ˈsɛrt̪ə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsɛrt̪ə̯ → ˈsɛɹt̪ə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈsɛɹt̪ə̯ → ˈsɛɹt̪   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsɛɹt̪ → ˈsɛrt̪   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsɛrt̪ → ˈsɛʀt̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛʀt̪ → sɛʀt̪   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɛʀt̪ → sɛʁt̪   (ʀ→ʁ)
```

## culs

`kˈuːloːs` → `ky`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈkuː.loːs → ˈku.los   (ˈuː→ˈu, oː→o)
300: a stressed vowel lengthens before a single consonant + glide
    ˈku.los → ˈkuː.los   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈkuː.los → ˈkʉː.los   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkʉː.los → ˈkʉː.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˈkʉː.ləs → ˈkʉːlə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkʉːlə̯s → ˈkʉːls   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈkʉːls → ˈkʉls   (ˈʉː→ˈʉ)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈkʉls → ˈkʉɫs   (l→ɫ)
1000: high round back vowels front (completion of u-fronting)
    ˈkʉɫs → ˈkyɫs   (ˈʉ→ˈy)
1000: back dark-l variants vocalize to w
    ˈkyɫs → ˈkyws   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˈkyws → ˈkys   (w→∅)
1000: a primary-stressed vowel lengthens before word-final s
    ˈkys → ˈkyːs   (ˈy→ˈyː)
1400: final obstruents are lost
    ˈkyːs → ˈkyː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkyː → kyː   (ˈyː→yː)
1400: distinctive vowel length is lost entirely
    kyː → ky   (yː→y)
```

## lie

`lˈiːgɑm` → `li`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈliː.gɑm → ˈli.gɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈli.gɑm → ˈli.gɑ   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈli.gɑ → ˈli.ɣɑ   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈli.ɣɑ → ˈliː.ɣɑ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˈliː.ɣɑ → ˈliː.ɣa   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈliː.ɣa → ˈliː.ɣʲa   (ɣ→ɣʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈliː.ɣʲa → ˈliː.ʝa   (ɣʲ→ʝ)
600: ʝ weakens to j unconditionally
    ˈliː.ʝa → ˈliː.ja   (ʝ→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈliː.ja → ˈliː.jə   (a→ə)
750: vowel length resets to short
    ˈliː.jə → ˈli.jə   (ˈiː→ˈi)
750: j deletes after a high front tense vowel
    ˈli.jə → ˈli.ə   (j→∅)
1200: schwa desyllabifies after another vowel
    ˈli.ə → ˈliə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈliə̯ → ˈliː   (ˈiə̯→ˈiː)
1400: stress is leveled — no longer distinctive for vowels
    ˈliː → liː   (ˈiː→iː)
1400: distinctive vowel length is lost entirely
    liː → li   (iː→i)
```

## maille

`mˌed̪ˈɑːliɑ` → `mɑj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmeˈd̪ɑː.li.ɑ → ˌmɛˈd̪ɑː.lɪ.ɑ   (ˌe→ˌɛ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɛˈd̪ɑː.lɪ.ɑ → ˌmɛˈd̪ɑː.ljɑ   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˌmɛˈd̪ɑː.ljɑ → ˌmɛˈd̪ɑː.ɫjɑ   (l→ɫ)
-100: yod strengthens before a vowel
    ˌmɛˈd̪ɑː.ɫjɑ → ˌmɛˈd̪ɑːɫ.ʝɑ   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɛˈd̪ɑːɫ.ʝɑ → ˌmɛˈd̪ɑɫ.ʝɑ   (ˈɑː→ˈɑ)
300: l palatalizes to ʎ before yod
    ˌmɛˈd̪ɑɫ.ʝɑ → ˌmɛˈd̪ɑ.ʎɑ   (ɫʝ→ʎ)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌmɛˈd̪ɑ.ʎɑ → ˌmɛˈðɑ.ʎɑ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɛˈðɑ.ʎɑ → ˌmɛˈðɑː.ʎɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌmɛˈðɑː.ʎɑ → ˌmɛˈðaː.ʎa   (ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˌmɛˈðaː.ʎa → ˌmɛˈðae̯.ʎa   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˌmɛˈðae̯.ʎa → ˌmɛˈða.ʎa   (e̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌmɛˈða.ʎa → ˌmeˈða.ʎa   (ˌɛ→ˌe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌmeˈða.ʎa → ˌmeˈða.ʎə   (a→ə)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌmeˈða.ʎə → ˌməˈða.ʎə   (ˌe→ˌə)
1000: the interdental fricatives (plain and palatalized) efface
    ˌməˈða.ʎə → ˌməˈa.ʎə   (ð→∅)
1200: a stressless schwa desyllabifies before another vowel
    ˌməˈa.ʎə → ˈmə̯a.ʎə   (ˌə→ə̯)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˈmə̯a.ʎə → ˈmə̯aː.ʎə   (ˈa→ˈaː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈmə̯aː.ʎə → ˈmaː.ʎə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈmaː.ʎə → ˈmaːʎə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈmaːʎə̯ → ˈmɑːʎə̯   (ˈaː→ˈɑː)
1400: the final off-glide schwa is deleted elsewhere
    ˈmɑːʎə̯ → ˈmɑːʎ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɑːʎ → mɑːʎ   (ˈɑː→ɑː)
1400: distinctive vowel length is lost entirely
    mɑːʎ → mɑʎ   (ɑː→ɑ)
1400: ʎ becomes j
    mɑʎ → mɑj   (ʎ→j)
```

## nacelle

`n̪ˌɑwikˈellɑm` → `n̪o.zɛl`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌn̪ɑ.wiˈkel.lɑm → ˌn̪ɑ.ɣʷiˈkel.lɑm   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌn̪ɑ.ɣʷiˈkel.lɑm → ˌn̪ɑ.ɣʷɪˈkɛl.lɑm   (i→ɪ, ˈe→ˈɛ)
-100: ɪ lost between the labiovelar approximant and k
    ˌn̪ɑ.ɣʷɪˈkɛl.lɑm → ˌn̪ɑɣʷˈkɛl.lɑm   (ɪ→∅)
-100: the labiovelar approximant simplifies to w before a consonant
    ˌn̪ɑɣʷˈkɛl.lɑm → ˌn̪ɑwˈkɛl.lɑm   (ɣʷ→w)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌn̪ɑwˈkɛl.lɑm → ˌn̪ɑwˈkɛl.lɑ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌn̪ɑwˈkɛl.lɑ → ˌn̪ɑwˈkʲɛl.lɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌn̪ɑwˈkʲɛl.lɑ → ˌn̪ɑwˈcɛl.lɑ   (kʲ→c)
500: a palatal stop affricates
    ˌn̪ɑwˈcɛl.lɑ → ˌn̪ɑwˈt͡sʲɛl.lɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌn̪ɑwˈt͡sʲɛl.lɑ → ˌn̪awˈt͡sʲɛl.la   (ˌɑ→ˌa, ɑ→a)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌn̪awˈt͡sʲɛl.la → ˌn̪ɔwˈt͡sʲɛl.la   (ˌa→ˌɔ)
600: a voiceless consonant voices intervocalically
    ˌn̪ɔwˈt͡sʲɛl.la → ˌn̪ɔwˈd͡zʲɛl.la   (t͡sʲ→d͡zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌn̪ɔwˈd͡zʲɛl.la → ˌn̪ɔwjˈd͡zɛl.la   (d͡zʲ→jd͡z)
600: j is lost after j or a consonant, before a consonant
    ˌn̪ɔwjˈd͡zɛl.la → ˌn̪ɔwˈd͡zɛl.la   (j→∅)
600: secondary-stressed ɔ raises to ɯ before w
    ˌn̪ɔwˈd͡zɛl.la → ˌn̪ɯwˈd͡zɛl.la   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌn̪ɯwˈd͡zɛl.la → ˌn̪ɔwˈd͡zɛl.la   (ˌɯ→ˌɔ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌn̪ɔwˈd͡zɛl.la → ˌn̪ɔˈd͡zɛl.la   (w→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌn̪ɔˈd͡zɛl.la → ˌn̪ɔˈd͡zɛl.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˌn̪ɔˈd͡zɛl.lə → ˌn̪ɔˈd͡zɛ.lə   (l→∅)
1000: all affricates become sibilants (deaffrication)
    ˌn̪ɔˈd͡zɛ.lə → ˌn̪ɔˈzɛ.lə   (d͡z→z)
1200: lax back mid o lengthens before z or v
    ˌn̪ɔˈzɛ.lə → ˌn̪ɔːˈzɛ.lə   (ˌɔ→ˌɔː)
1200: a long back mid o tenses to oː
    ˌn̪ɔːˈzɛ.lə → ˌn̪oːˈzɛ.lə   (ˌɔː→ˌoː)
1400: final ə becomes a non-syllabic off-glide
    ˌn̪oːˈzɛ.lə → ˌn̪oːˈzɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌn̪oːˈzɛlə̯ → ˌn̪oːˈzɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌn̪oːˈzɛl → n̪oː.zɛl   (ˌoː→oː, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    n̪oː.zɛl → n̪o.zɛl   (oː→o)
```

## parenté

`pˌɑren̪t̪ˈɑːt̪um` → `pa.ʁɑ̃.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpɑ.ren̪ˈt̪ɑː.t̪um → ˌpɑ.rɛn̪ˈt̪ɑː.t̪ʊm   (e→ɛ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɑ.rɛn̪ˈt̪ɑː.t̪ʊm → ˌpɑ.rɛn̪ˈt̪ɑ.t̪ʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌpɑ.rɛn̪ˈt̪ɑ.t̪ʊm → ˌpɑ.rɛn̪ˈt̪ɑ.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɑ.rɛn̪ˈt̪ɑ.t̪om → ˌpɑ.rɛn̪ˈt̪ɑ.t̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpɑ.rɛn̪ˈt̪ɑ.t̪o → ˌpɑ.rɛn̪ˈt̪ɑː.t̪o   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌpɑ.rɛn̪ˈt̪ɑː.t̪o → ˌpa.rɛn̪ˈt̪aː.t̪o   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + a primary-stressed low vowel
    ˌpa.rɛn̪ˈt̪aː.t̪o → ˌpa.rən̪ˈt̪aː.t̪o   (ɛ→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpa.rən̪ˈt̪aː.t̪o → ˌpa.rən̪ˈt̪aː.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌpa.rən̪ˈt̪aː.t̪ə → ˌparə̯n̪ˈt̪aːt̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores before a nasal consonant + obstruent
    ˌparə̯n̪ˈt̪aːt̪ə̯ → ˌpa.rən̪ˈt̪aːt̪ə̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˌpa.rən̪ˈt̪aːt̪ə̯ → ˌpa.rən̪ˈt̪aːt̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌpa.rən̪ˈt̪aːt̪ → ˌpa.rən̪ˈt̪ae̯t̪   (ˈaː→ˈae̯)
750: a word-final stop re-opens to a fricative after a vowel
    ˌpa.rən̪ˈt̪ae̯t̪ → ˌpa.rən̪ˈt̪ae̯θ   (t̪→θ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌpa.rən̪ˈt̪ae̯θ → ˌpa.rən̪ˈt̪eːθ   (ˈae̯→ˈeː)
1000: schwa becomes e in a closed nasal syllable, when not word-final
    ˌpa.rən̪ˈt̪eːθ → ˌpa.ren̪ˈt̪eːθ   (ə→e)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌpa.ren̪ˈt̪eːθ → ˌpa.rẽn̪ˈt̪eːθ   (e→ẽ)
1000: vowel length resets to short
    ˌpa.rẽn̪ˈt̪eːθ → ˌpa.rẽn̪ˈt̪eθ   (ˈeː→ˈe)
1000: nasalized front mid vowels begin to lower
    ˌpa.rẽn̪ˈt̪eθ → ˌpa.rɛ̃n̪ˈt̪eθ   (ẽ→ɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌpa.rɛ̃n̪ˈt̪eθ → ˌpa.rãn̪ˈt̪eθ   (ɛ̃→ã)
1000: the interdental fricatives (plain and palatalized) efface
    ˌpa.rãn̪ˈt̪eθ → ˌpa.rãn̪ˈt̪e   (θ→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌpa.rãn̪ˈt̪e → ˌpa.rãːˈt̪e   (ãn̪→ãː)
1400: long a becomes back ɑː
    ˌpa.rãːˈt̪e → ˌpa.rɑ̃ːˈt̪e   (ãː→ɑ̃ː)
1400: r becomes uvular ʀ
    ˌpa.rɑ̃ːˈt̪e → ˌpa.ʀɑ̃ːˈt̪e   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpa.ʀɑ̃ːˈt̪e → pa.ʀɑ̃ː.t̪e   (ˌa→a, ˈe→e)
1400: distinctive vowel length is lost entirely
    pa.ʀɑ̃ː.t̪e → pa.ʀɑ̃.t̪e   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    pa.ʀɑ̃.t̪e → pa.ʁɑ̃.t̪e   (ʀ→ʁ)
```

## pin

`pˈiːn̪um` → `pɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpiː.n̪um → ˈpiː.n̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpiː.n̪ʊm → ˈpi.n̪ʊm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˈpi.n̪ʊm → ˈpi.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpi.n̪om → ˈpi.n̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpi.n̪o → ˈpiː.n̪o   (ˈi→ˈiː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpiː.n̪o → ˈpiː.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈpiː.n̪ə → ˈpiːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpiːn̪ə̯ → ˈpiːn̪   (ə̯→∅)
750: vowel length resets to short
    ˈpiːn̪ → ˈpin̪   (ˈiː→ˈi)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈpin̪ → ˈpĩn̪   (ˈi→ˈĩ)
1200: nasalized ĩ lowers to ẽ
    ˈpĩn̪ → ˈpẽn̪   (ˈĩ→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈpẽn̪ → ˈpẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈpẽː → ˈpɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɛ̃ː → pɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    pɛ̃ː → pɛ̃   (ɛ̃ː→ɛ̃)
```

## puce

`pˈuːlikem` → `pys`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpuː.li.kem → ˈpuː.lɪ.kɛm   (i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpuː.lɪ.kɛm → ˈpu.lɪ.kɛm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˈpu.lɪ.kɛm → ˈpu.le.kɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpu.le.kɛm → ˈpu.le.kɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈpu.le.kɛ → ˈpu.le.kʲɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈpu.le.kʲɛ → ˈpu.le.cɛ   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpu.le.cɛ → ˈpuː.le.cɛ   (ˈu→ˈuː)
500: a palatal stop affricates
    ˈpuː.le.cɛ → ˈpuː.le.t͡sʲɛ   (c→t͡sʲ)
500: a high tense round non-nasal vowel centralizes
    ˈpuː.le.t͡sʲɛ → ˈpʉː.le.t͡sʲɛ   (ˈuː→ˈʉː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈpʉː.le.t͡sʲɛ → ˈpʉː.lə.t͡sʲɛ   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpʉː.lə.t͡sʲɛ → ˈpʉː.lə.t͡sʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpʉː.lə.t͡sʲə → ˈpʉːlə̯t͡sʲə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈpʉːlə̯t͡sʲə̯ → ˈpʉːlə̯.t͡sʲə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈpʉːlə̯.t͡sʲə → ˈpʉːl.t͡sʲə   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈpʉːl.t͡sʲə → ˈpʉl.t͡sʲə   (ˈʉː→ˈʉ)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈpʉl.t͡sʲə → ˈpʉɫ.t͡sʲə   (l→ɫ)
1000: high round back vowels front (completion of u-fronting)
    ˈpʉɫ.t͡sʲə → ˈpyɫ.t͡sʲə   (ˈʉ→ˈy)
1000: back dark-l variants vocalize to w
    ˈpyɫ.t͡sʲə → ˈpyw.t͡sʲə   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˈpyw.t͡sʲə → ˈpy.t͡sʲə   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˈpy.t͡sʲə → ˈpy.sʲə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈpy.sʲə → ˈpy.sə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈpy.sə → ˈpysə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpysə̯ → ˈpys   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpys → pys   (ˈy→y)
```

## salut

`sˌɑlˈuːt̪em` → `sa.ly`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑˈluː.t̪em → ˌsɑˈluː.t̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑˈluː.t̪ɛm → ˌsɑˈlu.t̪ɛm   (ˈuː→ˈu)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɑˈlu.t̪ɛm → ˌsɑˈlu.t̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɑˈlu.t̪ɛ → ˌsɑˈluː.t̪ɛ   (ˈu→ˈuː)
500: the low vowel fronts by default
    ˌsɑˈluː.t̪ɛ → ˌsaˈluː.t̪ɛ   (ˌɑ→ˌa)
500: a high tense round non-nasal vowel centralizes
    ˌsaˈluː.t̪ɛ → ˌsaˈlʉː.t̪ɛ   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsaˈlʉː.t̪ɛ → ˌsaˈlʉː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsaˈlʉː.t̪ə → ˌsaˈlʉːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsaˈlʉːt̪ə̯ → ˌsaˈlʉːt̪   (ə̯→∅)
750: a word-final stop re-opens to a fricative after a vowel
    ˌsaˈlʉːt̪ → ˌsaˈlʉːθ   (t̪→θ)
750: vowel length resets to short
    ˌsaˈlʉːθ → ˌsaˈlʉθ   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˌsaˈlʉθ → ˌsaˈlyθ   (ˈʉ→ˈy)
1000: the interdental fricatives (plain and palatalized) efface
    ˌsaˈlyθ → ˌsaˈly   (θ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsaˈly → sa.ly   (ˌa→a, ˈy→y)
```

## sort

`sˈort̪em` → `sɔʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsor.t̪em → ˈsɔr.t̪ɛm   (ˈo→ˈɔ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsɔr.t̪ɛm → ˈsɔr.t̪ɛ   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsɔr.t̪ɛ → ˈsɔr.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈsɔr.t̪ə → ˈsɔrt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsɔrt̪ə̯ → ˈsɔrt̪   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsɔrt̪ → ˈsɔɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈsɔɹt̪ → ˈsɔɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsɔɹ → ˈsɔr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsɔr → ˈsɔʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɔʀ → sɔʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɔʀ → sɔʁ   (ʀ→ʁ)
```

## tierce

`t̪ˈert̪iɑm` → `t̪jɛʁs`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪er.t̪i.ɑm → ˈt̪ɛr.t̪ɪ.ɑm   (ˈe→ˈɛ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈt̪ɛr.t̪ɪ.ɑm → ˈt̪ɛr.t̪jɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈt̪ɛr.t̪jɑm → ˈt̪ɛr.t̪ʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɛr.t̪ʝɑm → ˈt̪ɛr.t̪ʝɑ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈt̪ɛr.t̪ʝɑ → ˈt̪ɛrt͡sʲ.ʝɑ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˈt̪ɛrt͡sʲ.ʝɑ → ˈt̪ɛr.t͡sʲɑ   (ʝ→∅)
500: the low vowel fronts by default
    ˈt̪ɛr.t͡sʲɑ → ˈt̪ɛr.t͡sʲa   (ɑ→a)
500: stressed ɛ diphthongizes to ie̯ before a coronal non-nasal consonant + high-front stop
    ˈt̪ɛr.t͡sʲa → ˈt̪ie̯r.t͡sʲa   (ˈɛ→ˈie̯)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt̪ie̯r.t͡sʲa → ˈt̪ie̯r.t͡sʲə   (a→ə)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ie̯r.t͡sʲə → ˈt̪jer.t͡sʲə   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈt̪jer.t͡sʲə → ˈt̪jer.sʲə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈt̪jer.sʲə → ˈt̪jer.sə   (sʲ→s)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈt̪jer.sə → ˈt̪jɛr.sə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪jɛr.sə → ˈt̪jɛrsə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈt̪jɛrsə̯ → ˈt̪jɛɹsə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪jɛɹsə̯ → ˈt̪jɛɹs   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈt̪jɛɹs → ˈt̪jɛrs   (ɹ→r)
1400: r becomes uvular ʀ
    ˈt̪jɛrs → ˈt̪jɛʀs   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪jɛʀs → t̪jɛʀs   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪jɛʀs → t̪jɛʁs   (ʀ→ʁ)
```

## vaine

`wˈɑːn̪ɑm` → `vɛn̪`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwɑː.n̪ɑm → ˈɣʷɑː.n̪ɑm   (w→ɣʷ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɑː.n̪ɑm → ˈβʷɑː.n̪ɑm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˈβʷɑː.n̪ɑm → ˈβʷɑ.n̪ɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷɑ.n̪ɑm → ˈβʷɑ.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈβʷɑ.n̪ɑ → ˈβʷɑː.n̪ɑ   (ˈɑ→ˈɑː)
500: labialized bilabial fricatives delabialize
    ˈβʷɑː.n̪ɑ → ˈβɑː.n̪ɑ   (βʷ→β)
500: the low vowel fronts by default
    ˈβɑː.n̪ɑ → ˈβaː.n̪a   (ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˈβaː.n̪a → ˈβae̯.n̪a   (ˈaː→ˈae̯)
600: the remaining bilabial fricative becomes v
    ˈβae̯.n̪a → ˈvae̯.n̪a   (β→v)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˈvae̯.n̪a → ˈvaj.n̪a   (e̯→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈvaj.n̪a → ˈvaj.n̪ə   (a→ə)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˈvaj.n̪ə → ˈvaj̃.n̪ə   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈvaj̃.n̪ə → ˈvãj̃.n̪ə   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈvãj̃.n̪ə → ˈvɛ̃j̃.n̪ə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈvɛ̃j̃.n̪ə → ˈvɛ̃.n̪ə   (j̃→∅)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈvɛ̃.n̪ə → ˈvɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈvɛ.n̪ə → ˈvɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈvɛn̪ə̯ → ˈvɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈvɛn̪ → vɛn̪   (ˈɛ→ɛ)
```

## avancer

`ˌɑbˌɑn̪t̪iˈɑːre` → `a.vɑ̃.se`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑˌbɑn̪.t̪iˈɑː.re → ˌɑˌbɑn̪.t̪ɪˈɑː.rɛ   (i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɑˌbɑn̪.t̪ɪˈɑː.rɛ → ˌɑˌbɑn̪ˈt̪jɑː.rɛ   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɑˌbɑn̪ˈt̪jɑː.rɛ → ˌɑˌbɑn̪ˈt̪ʝɑː.rɛ   (j→ʝ)
-100: b lenites to β intervocalically / before a sonorant
    ˌɑˌbɑn̪ˈt̪ʝɑː.rɛ → ˌɑˌβɑn̪ˈt̪ʝɑː.rɛ   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑˌβɑn̪ˈt̪ʝɑː.rɛ → ˌɑˌβɑn̪ˈt̪ʝɑ.rɛ   (ˈɑː→ˈɑ)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌɑˌβɑn̪ˈt̪ʝɑ.rɛ → ˌɑˌβɑn̪t͡sʲˈʝɑ.rɛ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌɑˌβɑn̪t͡sʲˈʝɑ.rɛ → ˌɑˌβɑn̪ˈt͡sʲɑ.rɛ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑˌβɑn̪ˈt͡sʲɑ.rɛ → ˌɑˌβɑn̪ˈt͡sʲɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌɑˌβɑn̪ˈt͡sʲɑː.rɛ → ˌaˌβan̪ˈt͡sʲaː.rɛ   (ˌɑ→ˌa, ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌaˌβan̪ˈt͡sʲaː.rɛ → ˌaˌβan̪ˈt͡sʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌaˌβan̪ˈt͡sʲaː.rə → ˌaˌβan̪ˈt͡sʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌaˌβan̪ˈt͡sʲaːrə̯ → ˌaˌβan̪ˈt͡sʲaːr   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌaˌβan̪ˈt͡sʲaːr → ˌaˌβan̪ˈt͡sʲɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌaˌβan̪ˈt͡sʲɛːr → ˌaˌβan̪ˈt͡sʲie̯r   (ˈɛː→ˈie̯)
600: the remaining bilabial fricative becomes v
    ˌaˌβan̪ˈt͡sʲie̯r → ˌaˌvan̪ˈt͡sʲie̯r   (β→v)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌaˌvan̪ˈt͡sʲie̯r → ˌaˌvãn̪ˈt͡sʲie̯r   (ˌa→ˌã)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌaˌvãn̪ˈt͡sʲie̯r → ˌaˌvãn̪ˈt͡sʲjer   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌaˌvãn̪ˈt͡sʲjer → ˌaˌvãn̪ˈsʲjer   (t͡sʲ→sʲ)
1200: je becomes e after a palatal consonant
    ˌaˌvãn̪ˈsʲjer → ˌaˌvãn̪ˈsʲer   (j→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌaˌvãn̪ˈsʲer → ˌaˌvãn̪ˈser   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌaˌvãn̪ˈser → ˌaˌvãːˈser   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌaˌvãːˈser → ˌaˌvɑ̃ːˈser   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌaˌvɑ̃ːˈser → ˌaˌvɑ̃ːˈseɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌaˌvɑ̃ːˈseɹ → ˌaˌvɑ̃ːˈse   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˌvɑ̃ːˈse → a.vɑ̃ː.se   (ˌa→a, ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    a.vɑ̃ː.se → a.vɑ̃.se   (ɑ̃ː→ɑ̃)
```

## agneaux

`ˌɑgn̪ˈelloːs` → `a.ɲo`

```
-100: g assimilates to a following coronal nasal (gn cluster)
    ˌɑˈgn̪el.loːs → ˌɑŋˈn̪el.loːs   (g→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑŋˈn̪el.loːs → ˌɑŋˈn̪ɛl.loːs   (ˈe→ˈɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑŋˈn̪ɛl.loːs → ˌɑŋˈn̪ɛl.los   (oː→o)
500: ŋ palatalizes to ɲ before a coronal
    ˌɑŋˈn̪ɛl.los → ˌɑɲˈn̪ɛl.los   (ŋ→ɲ)
500: the low vowel fronts by default
    ˌɑɲˈn̪ɛl.los → ˌaɲˈn̪ɛl.los   (ˌɑ→ˌa)
500: a nasal consonant is lost after ɲ
    ˌaɲˈn̪ɛl.los → ˌaˈɲɛl.los   (n̪→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌaˈɲɛl.los → ˌaˈɲɛl.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˌaˈɲɛl.ləs → ˌaˈɲɛllə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌaˈɲɛllə̯s → ˌaˈɲɛlls   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˌaˈɲɛlls → ˌaˈɲɛls   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌaˈɲɛls → ˌaˈɲɛɫs   (l→ɫ)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌaˈɲɛɫs → ˌãˈɲɛɫs   (ˌa→ˌã)
1000: back dark-l variants vocalize to w
    ˌãˈɲɛɫs → ˌãˈɲɛws   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌãˈɲɛws → ˌãˈɲɛa̯ws   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌãˈɲɛa̯ws → ˌãˈɲe̯aws   (ˈɛ→e̯, a̯→ˈa)
1200: aw becomes long oː
    ˌãˈɲe̯aws → ˌãˈɲe̯oːs   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌãˈɲe̯oːs → ˌãˈɲə̯oːs   (e̯→ə̯)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌãˈɲə̯oːs → ˌãˈɲoːs   (ə̯→∅)
1400: final obstruents are lost
    ˌãˈɲoːs → ˌãˈɲoː   (s→∅)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˌãˈɲoː → ˌaˈɲoː   (ˌã→ˌa)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈɲoː → a.ɲoː   (ˌa→a, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    a.ɲoː → a.ɲo   (oː→o)
```

## amis

`ˌɑmˈiːkoːs` → `a.mi`

```
-100: the length feature is dropped now that quality carries the contrast
    ˌɑˈmiː.koːs → ˌɑˈmi.kos   (ˈiː→ˈi, oː→o)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑˈmi.kos → ˌɑˈmiː.kos   (ˈi→ˈiː)
500: k voices to g intervocalically
    ˌɑˈmiː.kos → ˌɑˈmiː.gos   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˌɑˈmiː.gos → ˌɑˈmiː.ɣos   (g→ɣ)
500: the low vowel fronts by default
    ˌɑˈmiː.ɣos → ˌaˈmiː.ɣos   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌaˈmiː.ɣos → ˌaˈmiː.ɣəs   (o→ə)
600: schwa becomes non-syllabic
    ˌaˈmiː.ɣəs → ˌaˈmiːɣə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌaˈmiːɣə̯s → ˌaˈmiːɣs   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˌaˈmiːɣs → ˌaˈmiɣs   (ˈiː→ˈi)
750: ɣ devoices to x before a voiceless segment or word-finally
    ˌaˈmiɣs → ˌaˈmixs   (ɣ→x)
750: remaining x/ɣ front
    ˌaˈmixs → ˌaˈmiçs   (x→ç)
750: ç merges into ʝ
    ˌaˈmiçs → ˌaˈmiʝs   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌaˈmiʝs → ˌaˈmijs   (ʝ→j)
750: j deletes after a high front tense vowel
    ˌaˈmijs → ˌaˈmis   (j→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌaˈmis → ˌãˈmis   (ˌa→ˌã)
1000: a primary-stressed vowel lengthens before word-final s
    ˌãˈmis → ˌãˈmiːs   (ˈi→ˈiː)
1400: final obstruents are lost
    ˌãˈmiːs → ˌãˈmiː   (s→∅)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˌãˈmiː → ˌaˈmiː   (ˌã→ˌa)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈmiː → a.miː   (ˌa→a, ˈiː→iː)
1400: distinctive vowel length is lost entirely
    a.miː → a.mi   (iː→i)
```

## armure

`ˌɑrmɑːt̪ˈuːrɑm` → `a.ʁmyʁ`

```
-100: the length feature is dropped now that quality carries the contrast
    ˌɑr.mɑːˈt̪uː.rɑm → ˌɑr.mɑˈt̪u.rɑm   (ɑː→ɑ, ˈuː→ˈu)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑr.mɑˈt̪u.rɑm → ˌɑr.mɑˈt̪u.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑr.mɑˈt̪u.rɑ → ˌɑr.mɑˈt̪uː.rɑ   (ˈu→ˈuː)
500: the low vowel fronts by default
    ˌɑr.mɑˈt̪uː.rɑ → ˌar.maˈt̪uː.ra   (ˌɑ→ˌa, ɑ→a, ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˌar.maˈt̪uː.ra → ˌar.maˈt̪ʉː.ra   (ˈuː→ˈʉː)
600: a voiceless consonant voices intervocalically
    ˌar.maˈt̪ʉː.ra → ˌar.maˈd̪ʉː.ra   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌar.maˈd̪ʉː.ra → ˌar.maˈðʉː.ra   (d̪→ð)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌar.maˈðʉː.ra → ˌar.məˈðʉː.rə   (a→ə, a→ə)
750: vowel length resets to short
    ˌar.məˈðʉː.rə → ˌar.məˈðʉ.rə   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˌar.məˈðʉ.rə → ˌar.məˈðy.rə   (ˈʉ→ˈy)
1000: the interdental fricatives (plain and palatalized) efface
    ˌar.məˈðy.rə → ˌar.məˈy.rə   (ð→∅)
1200: a stressless schwa desyllabifies before another vowel
    ˌar.məˈy.rə → ˌarˈmə̯y.rə   (ə→ə̯)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˌarˈmə̯y.rə → ˌarˈmə̯yː.rə   (ˈy→ˈyː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌarˈmə̯yː.rə → ˌarˈmyː.rə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌarˈmyː.rə → ˌarˈmyːrə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌarˈmyːrə̯ → ˌaɹˈmyːrə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˌaɹˈmyːrə̯ → ˌaɹˈmyːr   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌaɹˈmyːr → ˌarˈmyːr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌarˈmyːr → ˌaʀˈmyːʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌaʀˈmyːʀ → aʀ.myːʀ   (ˌa→a, ˈyː→yː)
1400: distinctive vowel length is lost entirely
    aʀ.myːʀ → aʀ.myʀ   (yː→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    aʀ.myʀ → a.ʁmyʁ   (ʀ→ʁ, ʀ→ʁ)
```

## baiser

`bˌɑsiˈɑːre` → `bɛ.ze`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌbɑ.siˈɑː.re → ˌbɑ.sɪˈɑː.rɛ   (i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌbɑ.sɪˈɑː.rɛ → ˌbɑˈsjɑː.rɛ   (ɪ→j)
-100: yod strengthens before a vowel
    ˌbɑˈsjɑː.rɛ → ˌbɑsˈʝɑː.rɛ   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌbɑsˈʝɑː.rɛ → ˌbɑsˈʝɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌbɑsˈʝɑ.rɛ → ˌbɑsˈʝɑː.rɛ   (ˈɑ→ˈɑː)
500: a voiceless fricative voices before yod + a non-consonantal segment
    ˌbɑsˈʝɑː.rɛ → ˌbɑzˈʝɑː.rɛ   (s→z)
500: z + yod becomes palatalized z
    ˌbɑzˈʝɑː.rɛ → ˌbɑˈzʲɑː.rɛ   (zʝ→zʲ)
500: the low vowel fronts by default
    ˌbɑˈzʲɑː.rɛ → ˌbaˈzʲaː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌbaˈzʲaː.rɛ → ˌbaˈzʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌbaˈzʲaː.rə → ˌbaˈzʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌbaˈzʲaːrə̯ → ˌbaˈzʲaːr   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌbaˈzʲaːr → ˌbaˈzʲɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌbaˈzʲɛːr → ˌbaˈzʲie̯r   (ˈɛː→ˈie̯)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌbaˈzʲie̯r → ˌbajˈzie̯r   (zʲ→jz)
600: a coronal palatalizes between two high-front segments
    ˌbajˈzie̯r → ˌbajˈzʲie̯r   (z→zʲ)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌbajˈzʲie̯r → ˌbajˈzʲjer   (ˈi→j, e̯→ˈe)
1200: je becomes e after a palatal consonant
    ˌbajˈzʲjer → ˌbajˈzʲer   (j→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌbajˈzʲer → ˌbajˈzer   (zʲ→z)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌbajˈzer → ˌbɛːˈzer   (ˌaj→ˌɛː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌbɛːˈzer → ˌbɛːˈzeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌbɛːˈzeɹ → ˌbɛːˈze   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌbɛːˈze → bɛː.ze   (ˌɛː→ɛː, ˈe→e)
1400: distinctive vowel length is lost entirely
    bɛː.ze → bɛ.ze   (ɛː→ɛ)
```

## blancs

`blˈɑn̪koːs` → `blɑ̃`

```
-100: n assimilates to a following velar stop
    ˈblɑn̪.koːs → ˈblɑŋ.koːs   (n̪→ŋ)
-100: the length feature is dropped now that quality carries the contrast
    ˈblɑŋ.koːs → ˈblɑŋ.kos   (oː→o)
500: the low vowel fronts by default
    ˈblɑŋ.kos → ˈblaŋ.kos   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈblaŋ.kos → ˈblaŋ.kəs   (o→ə)
600: schwa becomes non-syllabic
    ˈblaŋ.kəs → ˈblaŋkə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈblaŋkə̯s → ˈblaŋks   (ə̯→∅)
750: k is lost before word-final s
    ˈblaŋks → ˈblaŋs   (k→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈblaŋs → ˈblãŋs   (ˈa→ˈã)
1000: ŋ simplifies to n before a non-velar segment
    ˈblãŋs → ˈblãn̪s   (ŋ→n̪)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈblãn̪s → ˈblãːs   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈblãːs → ˈblɑ̃ːs   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈblɑ̃ːs → ˈblɑ̃ː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈblɑ̃ː → blɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    blɑ̃ː → blɑ̃   (ɑ̃ː→ɑ̃)
```

## bouger

`bˌullikˈɑːre` → `bu.ʒe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌbul.liˈkɑː.re → ˌbʊl.lɪˈkɑː.rɛ   (ˌu→ˌʊ, i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌbʊl.lɪˈkɑː.rɛ → ˌbʊl.lɪˈkɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌbʊl.lɪˈkɑ.rɛ → ˌbol.leˈkɑ.rɛ   (ˌʊ→ˌo, ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˌbol.leˈkɑ.rɛ → ˌbol.leˈkɑː.rɛ   (ˈɑ→ˈɑː)
500: k voices to g intervocalically
    ˌbol.leˈkɑː.rɛ → ˌbol.leˈgɑː.rɛ   (k→g)
500: e lost in -ica- endings before the now-voiced g + low vowel
    ˌbol.leˈgɑː.rɛ → ˌbollˈgɑː.rɛ   (e→∅)
500: the low vowel fronts by default
    ˌbollˈgɑː.rɛ → ˌbollˈgaː.rɛ   (ˈɑː→ˈaː)
500: the high back consonant w fronts before a front vowel
    ˌbollˈgaː.rɛ → ˌbollˈgʲaː.rɛ   (g→gʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌbollˈgʲaː.rɛ → ˌbollˈɟaː.rɛ   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˌbollˈɟaː.rɛ → ˌbollˈd͡ʒaː.rɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌbollˈd͡ʒaː.rɛ → ˌbollˈd͡ʒaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌbollˈd͡ʒaː.rə → ˌbollˈd͡ʒaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌbollˈd͡ʒaːrə̯ → ˌbollˈd͡ʒaːr   (ə̯→∅)
600: an identical consonant geminate reduces to one, before an obstruent or nasal
    ˌbollˈd͡ʒaːr → ˌbolˈd͡ʒaːr   (l→∅)
600: long stressed vowels diphthongize
    ˌbolˈd͡ʒaːr → ˌbolˈd͡ʒae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌbolˈd͡ʒae̯r → ˌbolˈd͡ʒeːr   (ˈae̯→ˈeː)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌbolˈd͡ʒeːr → ˌboɫˈd͡ʒeːr   (l→ɫ)
1000: vowel length resets to short
    ˌboɫˈd͡ʒeːr → ˌboɫˈd͡ʒer   (ˈeː→ˈe)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌboɫˈd͡ʒer → ˌbuɫˈd͡ʒer   (ˌo→ˌu)
1000: back dark-l variants vocalize to w
    ˌbuɫˈd͡ʒer → ˌbuwˈd͡ʒer   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˌbuwˈd͡ʒer → ˌbuˈd͡ʒer   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˌbuˈd͡ʒer → ˌbuˈʒer   (d͡ʒ→ʒ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌbuˈʒer → ˌbuˈʒeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌbuˈʒeɹ → ˌbuˈʒe   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌbuˈʒe → bu.ʒe   (ˌu→u, ˈe→e)
```

## doigt

`d̪ˈigit̪um` → `d̪wa`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪i.gi.t̪um → ˈd̪ɪ.gɪ.t̪ʊm   (ˈi→ˈɪ, i→ɪ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈd̪ɪ.gɪ.t̪ʊm → ˈd̪e.ge.t̪om   (ˈɪ→ˈe, ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪e.ge.t̪om → ˈd̪e.ge.t̪o   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈd̪e.ge.t̪o → ˈd̪e.gʲe.t̪o   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˈd̪e.gʲe.t̪o → ˈd̪e.ɟe.t̪o   (gʲ→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈd̪e.ɟe.t̪o → ˈd̪e.ʝe.t̪o   (ɟ→ʝ)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈd̪e.ʝe.t̪o → ˈd̪eʝ.t̪o   (e→∅)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈd̪eʝ.t̪o → ˈd̪eʝ.t̪ʲo   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪eʝ.t̪ʲo → ˈd̪eʝ.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈd̪eʝ.t̪ʲə → ˈd̪eʝt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd̪eʝt̪ʲə̯ → ˈd̪eʝt̪ʲ   (ə̯→∅)
600: ʝ weakens to j before optional consonants + word end
    ˈd̪eʝt̪ʲ → ˈd̪ejt̪ʲ   (ʝ→j)
600: a stressed vowel lengthens before j + optional consonants + a high-front coronal
    ˈd̪ejt̪ʲ → ˈd̪eːjt̪ʲ   (ˈe→ˈeː)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈd̪eːjt̪ʲ → ˈd̪eːjjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈd̪eːjjt̪ → ˈd̪eːjt̪   (j→∅)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˈd̪eːjt̪ → ˈd̪ejt̪   (ˈeː→ˈe)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈd̪ejt̪ → ˈd̪ojt̪   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈd̪ojt̪ → ˈd̪ujt̪   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈd̪ujt̪ → ˈd̪uɛ̯t̪   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈd̪uɛ̯t̪ → ˈd̪wɛt̪   (ˈu→w, ɛ̯→ˈɛ)
1400: final obstruents are lost
    ˈd̪wɛt̪ → ˈd̪wɛ   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪wɛ → d̪wɛ   (ˈɛ→ɛ)
1400: wɛ becomes wa
    d̪wɛ → d̪wa   (ɛ→a)
```

## dures

`d̪ˈuːrɑːs` → `d̪yʁ`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪uː.rɑːs → ˈd̪u.rɑs   (ˈuː→ˈu, ɑː→ɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪u.rɑs → ˈd̪uː.rɑs   (ˈu→ˈuː)
500: the low vowel fronts by default
    ˈd̪uː.rɑs → ˈd̪uː.ras   (ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˈd̪uː.ras → ˈd̪ʉː.ras   (ˈuː→ˈʉː)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd̪ʉː.ras → ˈd̪ʉː.rəs   (a→ə)
750: vowel length resets to short
    ˈd̪ʉː.rəs → ˈd̪ʉ.rəs   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈd̪ʉ.rəs → ˈd̪y.rəs   (ˈʉ→ˈy)
1200: a single final consonant effaces after schwa
    ˈd̪y.rəs → ˈd̪y.rə   (s→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈd̪y.rə → ˈd̪yrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈd̪yrə̯ → ˈd̪yr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈd̪yr → ˈd̪yʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪yʀ → d̪yʀ   (ˈy→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    d̪yʀ → d̪yʁ   (ʀ→ʁ)
```

## fausse

`fˈɑlsɑm` → `fos`

```
-100: l darkens before a non-lateral consonant
    ˈfɑl.sɑm → ˈfɑɫ.sɑm   (l→ɫ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɑɫ.sɑm → ˈfɑɫ.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈfɑɫ.sɑ → ˈfaɫ.sa   (ˈɑ→ˈa, ɑ→a)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈfaɫ.sa → ˈfaɫ.sʲa   (s→sʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈfaɫ.sʲa → ˈfaɫj.sa   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈfaɫj.sa → ˈfaɫ.sa   (j→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfaɫ.sa → ˈfaɫ.sə   (a→ə)
1000: back dark-l variants vocalize to w
    ˈfaɫ.sə → ˈfaw.sə   (ɫ→w)
1200: aw becomes long oː
    ˈfaw.sə → ˈfoː.sə   (ˈaw→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˈfoː.sə → ˈfoːsə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈfoːsə̯ → ˈfoːs   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfoːs → foːs   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    foːs → fos   (oː→o)
```

## fille

`fˈiːliɑm` → `fij`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfiː.li.ɑm → ˈfiː.lɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈfiː.lɪ.ɑm → ˈfiː.ljɑm   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˈfiː.ljɑm → ˈfiː.ɫjɑm   (l→ɫ)
-100: yod strengthens before a vowel
    ˈfiː.ɫjɑm → ˈfiːɫ.ʝɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈfiːɫ.ʝɑm → ˈfiɫ.ʝɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfiɫ.ʝɑm → ˈfiɫ.ʝɑ   (m→∅)
300: l palatalizes to ʎ before yod
    ˈfiɫ.ʝɑ → ˈfi.ʎɑ   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfi.ʎɑ → ˈfiː.ʎɑ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˈfiː.ʎɑ → ˈfiː.ʎa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfiː.ʎa → ˈfiː.ʎə   (a→ə)
750: vowel length resets to short
    ˈfiː.ʎə → ˈfi.ʎə   (ˈiː→ˈi)
1400: final ə becomes a non-syllabic off-glide
    ˈfi.ʎə → ˈfiʎə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈfiʎə̯ → ˈfiʎ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfiʎ → fiʎ   (ˈi→i)
1400: ʎ becomes j
    fiʎ → fij   (ʎ→j)
```

## forêt

`fˌorˈest̪em` → `fɔ.ʁɛ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfoˈres.t̪em → ˌfɔˈrɛs.t̪ɛm   (ˌo→ˌɔ, ˈe→ˈɛ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌfɔˈrɛs.t̪ɛm → ˌfɔˈrɛs.t̪ɛ   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌfɔˈrɛs.t̪ɛ → ˌfɔˈrɛs.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌfɔˈrɛs.t̪ə → ˌfɔˈrɛst̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌfɔˈrɛst̪ə̯ → ˌfɔˈrɛst̪   (ə̯→∅)
600: secondary-stressed ɔ raises to o unconditionally
    ˌfɔˈrɛst̪ → ˌfoˈrɛst̪   (ˌɔ→ˌo)
1000: secondary-stressed o opens to ɔ before r or l, then stressed a or ɛ
    ˌfoˈrɛst̪ → ˌfɔˈrɛst̪   (ˌo→ˌɔ)
1000: s becomes x after a vowel, before any consonant
    ˌfɔˈrɛst̪ → ˌfɔˈrɛxt̪   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌfɔˈrɛxt̪ → ˌfɔˈrɛːt̪   (ˈɛx→ˈɛː)
1400: final obstruents are lost
    ˌfɔˈrɛːt̪ → ˌfɔˈrɛː   (t̪→∅)
1400: r becomes uvular ʀ
    ˌfɔˈrɛː → ˌfɔˈʀɛː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌfɔˈʀɛː → fɔ.ʀɛː   (ˌɔ→ɔ, ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    fɔ.ʀɛː → fɔ.ʀɛ   (ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    fɔ.ʀɛ → fɔ.ʁɛ   (ʀ→ʁ)
```

## fonds

`fˈun̪d̪us` → `fɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfun̪.d̪us → ˈfʊn̪.d̪ʊs   (ˈu→ˈʊ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈfʊn̪.d̪ʊs → ˈfon̪.d̪os   (ˈʊ→ˈo, ʊ→o)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈfon̪.d̪os → ˈfũn̪.d̪os   (ˈo→ˈũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfũn̪.d̪os → ˈfũn̪.d̪əs   (o→ə)
600: schwa becomes non-syllabic
    ˈfũn̪.d̪əs → ˈfũn̪d̪ə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfũn̪d̪ə̯s → ˈfũn̪d̪s   (ə̯→∅)
600: a dental fricative + s becomes the affricate ts word-finally
    ˈfũn̪d̪s → ˈfũn̪t͡s   (d̪s→t͡s)
1000: all affricates become sibilants (deaffrication)
    ˈfũn̪t͡s → ˈfũn̪s   (t͡s→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈfũn̪s → ˈfũːs   (ˈũn̪→ˈũː)
1400: final obstruents are lost
    ˈfũːs → ˈfũː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfũː → fũː   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    fũː → fũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    fũ → fɔ̃   (ũ→ɔ̃)
```

## gros

`grˈossum` → `gʁo`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgros.sum → ˈgrɔs.sʊm   (ˈo→ˈɔ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈgrɔs.sʊm → ˈgrɔs.som   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgrɔs.som → ˈgrɔs.so   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈgrɔs.so → ˈgrɔs.sə   (o→ə)
600: schwa becomes non-syllabic
    ˈgrɔs.sə → ˈgrɔssə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈgrɔssə̯ → ˈgrɔss   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˈgrɔss → ˈgrɔs   (s→∅)
1000: a primary-stressed vowel lengthens before word-final s
    ˈgrɔs → ˈgrɔːs   (ˈɔ→ˈɔː)
1200: a long back mid o tenses to oː
    ˈgrɔːs → ˈgroːs   (ˈɔː→ˈoː)
1400: final obstruents are lost
    ˈgroːs → ˈgroː   (s→∅)
1400: r becomes uvular ʀ
    ˈgroː → ˈgʀoː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈgʀoː → gʀoː   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    gʀoː → gʀo   (oː→o)
1400: the uvular trill ʀ becomes a fricative ʁ
    gʀo → gʁo   (ʀ→ʁ)
```

## janvier

`iˌɑːn̪uˈɑːrium` → `ʒɑ̃.vje`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    iˌɑː.n̪uˈɑː.ri.um → ɪˌɑː.n̪ʊˈɑː.rɪ.ʊm   (i→ɪ, u→ʊ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ɪˌɑː.n̪ʊˈɑː.rɪ.ʊm → ˌjɑːˈn̪wɑː.rjʊm   (ɪ→j, ʊ→w, ɪ→j)
-100: yod strengthens before a vowel
    ˌjɑːˈn̪wɑː.rjʊm → ˌʝɑːˈn̪wɑːr.ʝʊm   (j→ʝ, j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌʝɑːˈn̪wɑːr.ʝʊm → ˌʝɑˈn̪wɑr.ʝʊm   (ˌɑː→ˌɑ, ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌʝɑˈn̪wɑr.ʝʊm → ˌʝɑˈn̪wɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌʝɑˈn̪wɑr.ʝom → ˌʝɑˈn̪wɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌʝɑˈn̪wɑr.ʝo → ˌʝɑˈn̪wɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌʝɑˈn̪wɑ.rʲo → ˌʝaˈn̪wa.rʲo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: w becomes the bilabial fricative between vowels, after n(n)
    ˌʝaˈn̪wa.rʲo → ˌʝan̪ˈβa.rʲo   (w→β)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌʝan̪ˈβa.rʲo → ˌʝan̪ˈβaː.rʲo   (ˈa→ˈaː)
600: yod hardens to ɟ word-initially before a vowel
    ˌʝan̪ˈβaː.rʲo → ˌɟan̪ˈβaː.rʲo   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˌɟan̪ˈβaː.rʲo → ˌd͡ʒan̪ˈβaː.rʲo   (ɟ→d͡ʒ)
600: aːrʲ metathesizes to jɛːr
    ˌd͡ʒan̪ˈβaː.rʲo → ˌd͡ʒan̪ˈβjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌd͡ʒan̪ˈβjɛː.ro → ˌd͡ʒan̪ˈβjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌd͡ʒan̪ˈβjɛː.rə → ˌd͡ʒan̪ˈβjɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌd͡ʒan̪ˈβjɛːrə̯ → ˌd͡ʒan̪ˈβjɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌd͡ʒan̪ˈβjɛːr → ˌd͡ʒan̪ˈβjie̯r   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌd͡ʒan̪ˈβjie̯r → ˌd͡ʒan̪ˈβie̯r   (j→∅)
600: the remaining bilabial fricative becomes v
    ˌd͡ʒan̪ˈβie̯r → ˌd͡ʒan̪ˈvie̯r   (β→v)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌd͡ʒan̪ˈvie̯r → ˌd͡ʒãn̪ˈvie̯r   (ˌa→ˌã)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌd͡ʒãn̪ˈvie̯r → ˌd͡ʒãn̪ˈvjer   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌd͡ʒãn̪ˈvjer → ˌʒãn̪ˈvjer   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌʒãn̪ˈvjer → ˌʒãːˈvjer   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌʒãːˈvjer → ˌʒɑ̃ːˈvjer   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌʒɑ̃ːˈvjer → ˌʒɑ̃ːˈvjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌʒɑ̃ːˈvjeɹ → ˌʒɑ̃ːˈvje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌʒɑ̃ːˈvje → ʒɑ̃ː.vje   (ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    ʒɑ̃ː.vje → ʒɑ̃.vje   (ɑ̃ː→ɑ̃)
```

## jeudi

`iˈowisd̪ˈiːem` → `ʒø.d̪i`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    iˈo.wisˈd̪iː.em → iˈo.ɣʷisˈd̪iː.em   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    iˈo.ɣʷisˈd̪iː.em → ɪˈɔ.ɣʷɪsˈd̪iː.ɛm   (i→ɪ, ˈo→ˈɔ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ɪˈɔ.ɣʷɪsˈd̪iː.ɛm → ˈjɔ.ɣʷɪsˈd̪iː.ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈjɔ.ɣʷɪsˈd̪iː.ɛm → ˈʝɔ.ɣʷɪsˈd̪iː.ɛm   (j→ʝ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈʝɔ.ɣʷɪsˈd̪iː.ɛm → ˈʝɔ.βʷɪsˈd̪iː.ɛm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˈʝɔ.βʷɪsˈd̪iː.ɛm → ˈʝɔ.βʷɪsˈd̪i.ɛm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˈʝɔ.βʷɪsˈd̪i.ɛm → ˈʝɔ.βʷesˈd̪i.ɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈʝɔ.βʷesˈd̪i.ɛm → ˈʝɔ.βʷesˈd̪i.ɛ   (m→∅)
300: a stressed vowel lengthens before another vowel
    ˈʝɔ.βʷesˈd̪i.ɛ → ˈʝɔ.βʷesˈd̪iː.ɛ   (ˈi→ˈiː)
300: a stressed vowel lengthens before a single consonant + glide
    ˈʝɔ.βʷesˈd̪iː.ɛ → ˈʝɔː.βʷesˈd̪iː.ɛ   (ˈɔ→ˈɔː)
500: labialized bilabial fricatives delabialize
    ˈʝɔː.βʷesˈd̪iː.ɛ → ˈʝɔː.βesˈd̪iː.ɛ   (βʷ→β)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈʝɔː.βesˈd̪iː.ɛ → ˈʝuo̯.βesˈd̪iː.ɛ   (ˈɔː→ˈuo̯)
500: a high tense round non-nasal vowel centralizes
    ˈʝuo̯.βesˈd̪iː.ɛ → ˈʝʉo̯.βesˈd̪iː.ɛ   (ˈu→ˈʉ)
500: an unstressed front non-low vowel becomes a glide in hiatus after a stressed vowel
    ˈʝʉo̯.βesˈd̪iː.ɛ → ˈʝʉo̯.βesˈd̪iːɪ̯   (ɛ→ɪ̯)
600: yod hardens to ɟ word-initially before a vowel
    ˈʝʉo̯.βesˈd̪iːɪ̯ → ˈɟʉo̯.βesˈd̪iːɪ̯   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟʉo̯.βesˈd̪iːɪ̯ → ˈd͡ʒʉo̯.βesˈd̪iːɪ̯   (ɟ→d͡ʒ)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈd͡ʒʉo̯.βesˈd̪iːɪ̯ → ˈd͡ʒʉo̯.βəsˈd̪iːɪ̯   (e→ə)
600: schwa becomes non-syllabic
    ˈd͡ʒʉo̯.βəsˈd̪iːɪ̯ → ˈd͡ʒʉo̯βə̯sˈd̪iːɪ̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd͡ʒʉo̯βə̯sˈd̪iːɪ̯ → ˈd͡ʒʉo̯βsˈd̪iːɪ̯   (ə̯→∅)
600: a labial consonant becomes s before s
    ˈd͡ʒʉo̯βsˈd̪iːɪ̯ → ˈd͡ʒʉo̯ssˈd̪iːɪ̯   (β→s)
600: an identical consonant geminate reduces to one, before an obstruent or nasal
    ˈd͡ʒʉo̯ssˈd̪iːɪ̯ → ˈd͡ʒʉo̯sˈd̪iːɪ̯   (s→∅)
750: vowel length resets to short
    ˈd͡ʒʉo̯sˈd̪iːɪ̯ → ˈd͡ʒʉo̯sˈd̪iɪ̯   (ˈiː→ˈi)
750: s voices to z after a vowel, before a voiced consonant
    ˈd͡ʒʉo̯sˈd̪iɪ̯ → ˈd͡ʒʉo̯zˈd̪iɪ̯   (s→z)
1000: high round back vowels front (completion of u-fronting)
    ˈd͡ʒʉo̯zˈd̪iɪ̯ → ˈd͡ʒyo̯zˈd̪iɪ̯   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈd͡ʒyo̯zˈd̪iɪ̯ → ˈd͡ʒye̯zˈd̪iɪ̯   (o̯→e̯)
1000: a high non-round glide deletes after stressed i
    ˈd͡ʒye̯zˈd̪iɪ̯ → ˈd͡ʒye̯zˈd̪i   (ɪ̯→∅)
1000: z is lost before d
    ˈd͡ʒye̯zˈd̪i → ˈd͡ʒye̯ˈd̪i   (z→∅)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈd͡ʒye̯ˈd̪i → ˈd͡ʒøˈd̪i   (ˈye̯→ˈø)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒøˈd̪i → ˈʒøˈd̪i   (d͡ʒ→ʒ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒøˈd̪i → ʒø.d̪i   (ˈø→ø, ˈi→i)
```

## chamois

`kˌɑmˈoːxsum` → `ʃa.mwa`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkɑˈmoːx.sum → ˌkɑˈmoːx.sʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkɑˈmoːx.sʊm → ˌkɑˈmox.sʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ˌkɑˈmox.sʊm → ˌkɑˈmox.som   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkɑˈmox.som → ˌkɑˈmox.so   (m→∅)
500: the low vowel fronts by default
    ˌkɑˈmox.so → ˌkaˈmox.so   (ˌɑ→ˌa)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌkaˈmox.so → ˌkaˈmoç.so   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌkaˈmoç.so → ˌkaˈmoç.sʲo   (s→sʲ)
500: the high back consonant w fronts before a front vowel
    ˌkaˈmoç.sʲo → ˌkʲaˈmoç.sʲo   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌkʲaˈmoç.sʲo → ˌcaˈmoç.sʲo   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˌcaˈmoç.sʲo → ˌt͡ʃaˈmoç.sʲo   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt͡ʃaˈmoç.sʲo → ˌt͡ʃaˈmoç.sʲə   (o→ə)
600: schwa becomes non-syllabic
    ˌt͡ʃaˈmoç.sʲə → ˌt͡ʃaˈmoçsʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt͡ʃaˈmoçsʲə̯ → ˌt͡ʃaˈmoçsʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌt͡ʃaˈmoçsʲ → ˌt͡ʃaˈmoçjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˌt͡ʃaˈmoçjs → ˌt͡ʃaˈmoçs   (j→∅)
750: ç merges into ʝ
    ˌt͡ʃaˈmoçs → ˌt͡ʃaˈmoʝs   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌt͡ʃaˈmoʝs → ˌt͡ʃaˈmojs   (ʝ→j)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌt͡ʃaˈmojs → ˌt͡ʃãˈmojs   (ˌa→ˌã)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌt͡ʃãˈmojs → ˌt͡ʃãˈmujs   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌt͡ʃãˈmujs → ˌt͡ʃãˈmuɛ̯s   (j→ɛ̯)
1000: all affricates become sibilants (deaffrication)
    ˌt͡ʃãˈmuɛ̯s → ˌʃãˈmuɛ̯s   (t͡ʃ→ʃ)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌʃãˈmuɛ̯s → ˌʃãˈmwɛs   (ˈu→w, ɛ̯→ˈɛ)
1400: final obstruents are lost
    ˌʃãˈmwɛs → ˌʃãˈmwɛ   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌʃãˈmwɛ → ʃã.mwɛ   (ˌã→ã, ˈɛ→ɛ)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    ʃã.mwɛ → ʃa.mwɛ   (ã→a)
1400: wɛ becomes wa
    ʃa.mwɛ → ʃa.mwa   (ɛ→a)
```

## chère

`kˈɑːrɑm` → `ʃɛʁ`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈkɑː.rɑm → ˈkɑ.rɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑ.rɑm → ˈkɑ.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkɑ.rɑ → ˈkɑː.rɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈkɑː.rɑ → ˈkaː.ra   (ˈɑː→ˈaː, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈkaː.ra → ˈkʲaː.ra   (k→kʲ)
500: long stressed aː becomes ɛː word-initially after a front consonant
    ˈkʲaː.ra → ˈkʲɛː.ra   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˈkʲɛː.ra → ˈkʲie̯.ra   (ˈɛː→ˈie̯)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲie̯.ra → ˈcie̯.ra   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcie̯.ra → ˈt͡ʃie̯.ra   (c→t͡ʃ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡ʃie̯.ra → ˈt͡ʃie̯.rə   (a→ə)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt͡ʃie̯.rə → ˈt͡ʃje.rə   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃje.rə → ˈʃje.rə   (t͡ʃ→ʃ)
1200: je becomes e after a palatal consonant
    ˈʃje.rə → ˈʃe.rə   (j→∅)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈʃe.rə → ˈʃɛ.rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈʃɛ.rə → ˈʃɛrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃɛrə̯ → ˈʃɛr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈʃɛr → ˈʃɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃɛʀ → ʃɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃɛʀ → ʃɛʁ   (ʀ→ʁ)
```

## sangle

`kˈin̪gulɑ` → `sɑ̃gl`

```
-100: n assimilates to a following velar stop
    ˈkin̪.gu.lɑ → ˈkiŋ.gu.lɑ   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkiŋ.gu.lɑ → ˈkɪŋ.gʊ.lɑ   (ˈi→ˈɪ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈkɪŋ.gʊ.lɑ → ˈkɪŋ.glɑ   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈkɪŋ.glɑ → ˈkeŋ.glɑ   (ˈɪ→ˈe)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈkeŋ.glɑ → ˈkʲeŋ.glɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkʲeŋ.glɑ → ˈceŋ.glɑ   (kʲ→c)
500: a palatal stop affricates
    ˈceŋ.glɑ → ˈt͡sʲeŋ.glɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˈt͡sʲeŋ.glɑ → ˈt͡sʲeŋ.gla   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡sʲeŋ.gla → ˈt͡sʲeŋ.glə   (a→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈt͡sʲeŋ.glə → ˈt͡sʲẽŋ.glə   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈt͡sʲẽŋ.glə → ˈt͡sʲɛ̃ŋ.glə   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈt͡sʲɛ̃ŋ.glə → ˈt͡sʲãŋ.glə   (ˈɛ̃→ˈã)
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲãŋ.glə → ˈsʲãŋ.glə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲãŋ.glə → ˈsãŋ.glə   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈsãŋ.glə → ˈsãː.glə   (ˈãŋ→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈsãː.glə → ˈsãːglə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈsãːglə̯ → ˈsɑ̃ːglə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈsɑ̃ːglə̯ → ˈsɑ̃ːgl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɑ̃ːgl → sɑ̃ːgl   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    sɑ̃ːgl → sɑ̃gl   (ɑ̃ː→ɑ̃)
```

## coq

`kˈokkum` → `kɔk`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkok.kum → ˈkɔk.kʊm   (ˈo→ˈɔ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkɔk.kʊm → ˈkɔk.kom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɔk.kom → ˈkɔk.ko   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkɔk.ko → ˈkɔk.kə   (o→ə)
600: schwa becomes non-syllabic
    ˈkɔk.kə → ˈkɔkkə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkɔkkə̯ → ˈkɔkk   (ə̯→∅)
1200: geminates simplify to single consonants
    ˈkɔkk → ˈkɔk   (k→∅)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈkɔk → ˈkɔkə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkɔkə̯ → ˈkɔk   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkɔk → kɔk   (ˈɔ→ɔ)
```

## graisse

`krˈɑssiɑ` → `gʁɛs`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkrɑs.si.ɑ → ˈkrɑs.sɪ.ɑ   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈkrɑs.sɪ.ɑ → ˈkrɑs.sjɑ   (ɪ→j)
-100: yod strengthens before a vowel
    ˈkrɑs.sjɑ → ˈkrɑss.ʝɑ   (j→ʝ)
500: s + high-front consonant becomes geminate palatalized s
    ˈkrɑss.ʝɑ → ˈkrɑssʲ.sʲɑ   (s→sʲ, ʝ→sʲ)
500: s + high-front consonant becomes geminate palatalized s (recurrence)
    ˈkrɑssʲ.sʲɑ → ˈkrɑsʲsʲ.sʲɑ   (s→sʲ)
500: palatalized s lost before a geminate palatalized s (prevents a triple geminate)
    ˈkrɑsʲsʲ.sʲɑ → ˈkrɑsʲ.sʲɑ   (sʲ→∅)
500: the low vowel fronts by default
    ˈkrɑsʲ.sʲɑ → ˈkrasʲ.sʲa   (ˈɑ→ˈa, ɑ→a)
600: geminate palatalized s degeminates
    ˈkrasʲ.sʲa → ˈkra.sʲa   (sʲ→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈkra.sʲa → ˈkraj.sa   (sʲ→js)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈkraj.sa → ˈkraj.sə   (a→ə)
1000: word-initial k voices before r/l + a
    ˈkraj.sə → ˈgraj.sə   (k→g)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈgraj.sə → ˈgrɛː.sə   (ˈaj→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˈgrɛː.sə → ˈgrɛːsə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈgrɛːsə̯ → ˈgrɛːs   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈgrɛːs → ˈgʀɛːs   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈgʀɛːs → gʀɛːs   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    gʀɛːs → gʀɛs   (ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    gʀɛs → gʁɛs   (ʀ→ʁ)
```

## coffin

`kˈupulɑm` → `kubl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈku.pu.lɑm → ˈkʊ.pʊ.lɑm   (ˈu→ˈʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈkʊ.pʊ.lɑm → ˈkʊ.plɑm   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈkʊ.plɑm → ˈko.plɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈko.plɑm → ˈko.plɑ   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈko.plɑ → ˈkoː.plɑ   (ˈo→ˈoː)
500: a vowel shortens before a consonant cluster
    ˈkoː.plɑ → ˈko.plɑ   (ˈoː→ˈo)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant
    ˈko.plɑ → ˈkoː.plɑ   (ˈo→ˈoː)
500: the low vowel fronts by default
    ˈkoː.plɑ → ˈkoː.pla   (ɑ→a)
500: a vowel shortens before a consonant cluster (recurrence)
    ˈkoː.pla → ˈko.pla   (ˈoː→ˈo)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant (recurrence)
    ˈko.pla → ˈkoː.pla   (ˈo→ˈoː)
600: a voiceless anterior consonant voices before a coronal sonorant non-nasal consonant
    ˈkoː.pla → ˈkoː.bla   (p→b)
600: long stressed vowels diphthongize
    ˈkoː.bla → ˈkow.bla   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈkow.bla → ˈko.bla   (w→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈko.bla → ˈko.blə   (a→ə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈko.blə → ˈku.blə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈku.blə → ˈkublə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkublə̯ → ˈkubl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkubl → kubl   (ˈu→u)
```

## lai

`lˈɑːikum` → `laj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlɑː.i.kum → ˈlɑː.ɪ.kʊm   (i→ɪ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈlɑː.ɪ.kʊm → ˈlɑ.ɪ.kʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˈlɑ.ɪ.kʊm → ˈlɑ.e.kom   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɑ.e.kom → ˈlɑ.e.ko   (m→∅)
300: a stressed vowel lengthens before another vowel
    ˈlɑ.e.ko → ˈlɑː.e.ko   (ˈɑ→ˈɑː)
500: k voices to g intervocalically
    ˈlɑː.e.ko → ˈlɑː.e.go   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˈlɑː.e.go → ˈlɑː.e.ɣo   (g→ɣ)
500: the low vowel fronts by default
    ˈlɑː.e.ɣo → ˈlaː.e.ɣo   (ˈɑː→ˈaː)
500: an unstressed front non-low vowel becomes a glide in hiatus after a stressed vowel
    ˈlaː.e.ɣo → ˈlaːi̯.ɣo   (e→i̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈlaːi̯.ɣo → ˈlaːi̯.ɣə   (o→ə)
600: schwa becomes non-syllabic
    ˈlaːi̯.ɣə → ˈlaːi̯ɣə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈlaːi̯ɣə̯ → ˈlaːi̯ɣ   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈlaːi̯ɣ → ˈlai̯ɣ   (ˈaː→ˈa)
750: all final obstruents devoice
    ˈlai̯ɣ → ˈlai̯x   (ɣ→x)
750: remaining x/ɣ front
    ˈlai̯x → ˈlai̯ç   (x→ç)
750: ç merges into ʝ
    ˈlai̯ç → ˈlai̯ʝ   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈlai̯ʝ → ˈlai̯j   (ʝ→j)
1400: stress is leveled — no longer distinctive for vowels
    ˈlai̯j → lai̯j   (ˈa→a)
1400: a high front vowel after another vowel is absorbed into a following j
    lai̯j → laj   (i̯→∅)
```

## loche

`lˈɑwkkɑm` → `lɔʃ`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɑwk.kɑm → ˈlɑwk.kɑ   (m→∅)
500: the low vowel fronts by default
    ˈlɑwk.kɑ → ˈlawk.ka   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈlawk.ka → ˈlawk.kʲa   (k→kʲ)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈlawk.kʲa → ˈlɔwk.kʲa   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈlɔwk.kʲa → ˈlɔwk.ca   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈlɔwk.ca → ˈlɔw.kt͡ʃa   (c→t͡ʃ)
600: a stop assimilates place to a following affricate (k/tʃ, g/dʒ)
    ˈlɔw.kt͡ʃa → ˈlɔw.t̪t͡ʃa   (k→t̪)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlɔw.t̪t͡ʃa → ˈlɔw.t̪t͡ʃə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈlɔw.t̪t͡ʃə → ˈlɔw.t͡ʃə   (t̪→∅)
1000: ow simplifies to o before a strident consonant, not word-finally
    ˈlɔw.t͡ʃə → ˈlɔ.t͡ʃə   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˈlɔ.t͡ʃə → ˈlɔ.ʃə   (t͡ʃ→ʃ)
1400: final ə becomes a non-syllabic off-glide
    ˈlɔ.ʃə → ˈlɔʃə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlɔʃə̯ → ˈlɔʃ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlɔʃ → lɔʃ   (ˈɔ→ɔ)
```

## ligne

`lˈiːn̪eɑm` → `liɲ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈliː.n̪e.ɑm → ˈliː.n̪ɛ.ɑm   (e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈliː.n̪ɛ.ɑm → ˈliː.n̪jɑm   (ɛ→j)
-100: yod strengthens before a vowel
    ˈliː.n̪jɑm → ˈliːn̪.ʝɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈliːn̪.ʝɑm → ˈlin̪.ʝɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlin̪.ʝɑm → ˈlin̪.ʝɑ   (m→∅)
300: the coronal nasal palatalizes before yod
    ˈlin̪.ʝɑ → ˈli.ɲɑ   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈli.ɲɑ → ˈliː.ɲɑ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˈliː.ɲɑ → ˈliː.ɲa   (ɑ→a)
600: a vowel shortens before ɲ
    ˈliː.ɲa → ˈli.ɲa   (ˈiː→ˈi)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈli.ɲa → ˈli.ɲə   (a→ə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈli.ɲə → ˈlĩ.ɲə   (ˈi→ˈĩ)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˈlĩ.ɲə → ˈli.ɲə   (ˈĩ→ˈi)
1400: final ə becomes a non-syllabic off-glide
    ˈli.ɲə → ˈliɲə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈliɲə̯ → ˈliɲ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈliɲ → liɲ   (ˈi→i)
```

## maie

`mˈɑgid̪em` → `mɛ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmɑ.gi.d̪em → ˈmɑ.gɪ.d̪ɛm   (i→ɪ, e→ɛ)
-100: unstressed front vowel lost between a back stop and a coronal (type a)
    ˈmɑ.gɪ.d̪ɛm → ˈmɑg.d̪ɛm   (ɪ→∅)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmɑg.d̪ɛm → ˈmɑg.d̪ɛ   (m→∅)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˈmɑg.d̪ɛ → ˈmɑɣ.d̪ɛ   (g→ɣ)
500: the low vowel fronts by default
    ˈmɑɣ.d̪ɛ → ˈmaɣ.d̪ɛ   (ˈɑ→ˈa)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈmaɣ.d̪ɛ → ˈmaʝ.d̪ɛ   (ɣ→ʝ)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈmaʝ.d̪ɛ → ˈmaʝ.d̪ʲɛ   (d̪→d̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmaʝ.d̪ʲɛ → ˈmaʝ.d̪ʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈmaʝ.d̪ʲə → ˈmaʝd̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmaʝd̪ʲə̯ → ˈmaʝd̪ʲ   (ə̯→∅)
600: ʝ weakens to j before optional consonants + word end
    ˈmaʝd̪ʲ → ˈmajd̪ʲ   (ʝ→j)
600: a stressed vowel lengthens before j + optional consonants + a high-front coronal
    ˈmajd̪ʲ → ˈmaːjd̪ʲ   (ˈa→ˈaː)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈmaːjd̪ʲ → ˈmaːjjd̪   (d̪ʲ→jd̪)
600: j is lost after j or a consonant, before a consonant
    ˈmaːjjd̪ → ˈmaːjd̪   (j→∅)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˈmaːjd̪ → ˈmajd̪   (ˈaː→ˈa)
750: all final obstruents devoice
    ˈmajd̪ → ˈmajt̪   (d̪→t̪)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈmajt̪ → ˈmɛːt̪   (ˈaj→ˈɛː)
1400: final obstruents are lost
    ˈmɛːt̪ → ˈmɛː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɛː → mɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    mɛː → mɛ   (ɛː→ɛ)
```

## mari

`mˌɑrˈiːt̪um` → `ma.ʁi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmɑˈriː.t̪um → ˌmɑˈriː.t̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɑˈriː.t̪ʊm → ˌmɑˈri.t̪ʊm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌmɑˈri.t̪ʊm → ˌmɑˈri.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɑˈri.t̪om → ˌmɑˈri.t̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɑˈri.t̪o → ˌmɑˈriː.t̪o   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˌmɑˈriː.t̪o → ˌmaˈriː.t̪o   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmaˈriː.t̪o → ˌmaˈriː.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌmaˈriː.t̪ə → ˌmaˈriːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmaˈriːt̪ə̯ → ˌmaˈriːt̪   (ə̯→∅)
750: a word-final stop re-opens to a fricative after a vowel
    ˌmaˈriːt̪ → ˌmaˈriːθ   (t̪→θ)
750: vowel length resets to short
    ˌmaˈriːθ → ˌmaˈriθ   (ˈiː→ˈi)
1000: the interdental fricatives (plain and palatalized) efface
    ˌmaˈriθ → ˌmaˈri   (θ→∅)
1400: r becomes uvular ʀ
    ˌmaˈri → ˌmaˈʀi   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌmaˈʀi → ma.ʀi   (ˌa→a, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ma.ʀi → ma.ʁi   (ʀ→ʁ)
```

## moyenne

`mˌed̪iˈɑːn̪ɑm` → `mwa.jɛn̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌme.d̪iˈɑː.n̪ɑm → ˌmɛ.d̪ɪˈɑː.n̪ɑm   (ˌe→ˌɛ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɛ.d̪ɪˈɑː.n̪ɑm → ˌmɛˈd̪jɑː.n̪ɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌmɛˈd̪jɑː.n̪ɑm → ˌmɛˈd̪ʝɑː.n̪ɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɛˈd̪ʝɑː.n̪ɑm → ˌmɛˈd̪ʝɑ.n̪ɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɛˈd̪ʝɑ.n̪ɑm → ˌmɛˈd̪ʝɑ.n̪ɑ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌmɛˈd̪ʝɑ.n̪ɑ → ˌmɛˈɟʝɑ.n̪ɑ   (d̪→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌmɛˈɟʝɑ.n̪ɑ → ˌmɛʝˈʝɑ.n̪ɑ   (ɟ→ʝ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɛʝˈʝɑ.n̪ɑ → ˌmɛʝˈʝɑː.n̪ɑ   (ˈɑ→ˈɑː)
500: secondary-stressed ɛ/ɔ become tense before geminate yod
    ˌmɛʝˈʝɑː.n̪ɑ → ˌmeʝˈʝɑː.n̪ɑ   (ˌɛ→ˌe)
500: yod degeminates (lost before another yod)
    ˌmeʝˈʝɑː.n̪ɑ → ˌmeˈʝɑː.n̪ɑ   (ʝ→∅)
500: the low vowel fronts by default
    ˌmeˈʝɑː.n̪ɑ → ˌmeˈʝaː.n̪a   (ˈɑː→ˈaː, ɑ→a)
600: a stressed low vowel becomes front non-tense after a front glide, before a consonant + non-consonantal
    ˌmeˈʝaː.n̪a → ˌmeˈʝɛː.n̪a   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌmeˈʝɛː.n̪a → ˌmeˈʝie̯.n̪a   (ˈɛː→ˈie̯)
600: ʝ weakens to j unconditionally
    ˌmeˈʝie̯.n̪a → ˌmeˈjie̯.n̪a   (ʝ→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌmeˈjie̯.n̪a → ˌmeˈjie̯.n̪ə   (a→ə)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌmeˈjie̯.n̪ə → ˌməˈjie̯.n̪ə   (ˌe→ˌə)
1000: secondary-stressed schwa reverts to e before a palatal consonant
    ˌməˈjie̯.n̪ə → ˌmeˈjie̯.n̪ə   (ˌə→ˌe)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌmeˈjie̯.n̪ə → ˌmoˈjie̯.n̪ə   (ˌe→ˌo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌmoˈjie̯.n̪ə → ˌmuˈjie̯.n̪ə   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌmuˈjie̯.n̪ə → ˌmuˈɛ̯ie̯.n̪ə   (j→ɛ̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌmuˈɛ̯ie̯.n̪ə → ˌmuɛ̯ˈje.n̪ə   (ˈi→j, e̯→ˈe)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˌmuɛ̯ˈje.n̪ə → ˌmuɛ̯ˈjẽ.n̪ə   (ˈe→ˈẽ)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌmuɛ̯ˈjẽ.n̪ə → ˌmwɛˈjẽ.n̪ə   (ˌu→w, ɛ̯→ˌɛ)
1400: nasalized ẽ lowers to ɛ̃
    ˌmwɛˈjẽ.n̪ə → ˌmwɛˈjɛ̃.n̪ə   (ˈẽ→ˈɛ̃)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˌmwɛˈjɛ̃.n̪ə → ˌmwɛˈjɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌmwɛˈjɛ.n̪ə → ˌmwɛˈjɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌmwɛˈjɛn̪ə̯ → ˌmwɛˈjɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmwɛˈjɛn̪ → mwɛ.jɛn̪   (ˌɛ→ɛ, ˈɛ→ɛ)
1400: wɛ becomes wa
    mwɛ.jɛn̪ → mwa.jɛn̪   (ɛ→a)
```

## mèche

`mˈikkɑm` → `mɛʃ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmik.kɑm → ˈmɪk.kɑm   (ˈi→ˈɪ)
-100: lax high vowels lower to tense mid vowels
    ˈmɪk.kɑm → ˈmek.kɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmek.kɑm → ˈmek.kɑ   (m→∅)
500: the low vowel fronts by default
    ˈmek.kɑ → ˈmek.ka   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈmek.ka → ˈmek.kʲa   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈmek.kʲa → ˈmek.ca   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈmek.ca → ˈme.kt͡ʃa   (c→t͡ʃ)
600: a stop assimilates place to a following affricate (k/tʃ, g/dʒ)
    ˈme.kt͡ʃa → ˈme.t̪t͡ʃa   (k→t̪)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈme.t̪t͡ʃa → ˈme.t̪t͡ʃə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈme.t̪t͡ʃə → ˈme.t͡ʃə   (t̪→∅)
1000: stressed e laxes to ɛ before a consonant + vowel
    ˈme.t͡ʃə → ˈmɛ.t͡ʃə   (ˈe→ˈɛ)
1000: all affricates become sibilants (deaffrication)
    ˈmɛ.t͡ʃə → ˈmɛ.ʃə   (t͡ʃ→ʃ)
1400: final ə becomes a non-syllabic off-glide
    ˈmɛ.ʃə → ˈmɛʃə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈmɛʃə̯ → ˈmɛʃ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɛʃ → mɛʃ   (ˈɛ→ɛ)
```

## mordre

`mˈord̪ere` → `mɔʁd̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmor.d̪e.re → ˈmɔr.d̪ɛ.rɛ   (ˈo→ˈɔ, e→ɛ, e→ɛ)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈmɔr.d̪ɛ.rɛ → ˈmɔr.d̪rɛ   (ɛ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmɔr.d̪rɛ → ˈmɔr.d̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈmɔr.d̪rə → ˈmɔrd̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmɔrd̪rə̯ → ˈmɔrd̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈmɔrd̪r → ˈmɔr.d̪rə   (∅→ə)
1400: final ə becomes a non-syllabic off-glide
    ˈmɔr.d̪rə → ˈmɔrd̪rə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈmɔrd̪rə̯ → ˈmɔɹd̪rə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈmɔɹd̪rə̯ → ˈmɔɹd̪r   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈmɔɹd̪r → ˈmɔrd̪r   (ɹ→r)
1400: r becomes uvular ʀ
    ˈmɔrd̪r → ˈmɔʀd̪ʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɔʀd̪ʀ → mɔʀd̪ʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    mɔʀd̪ʀ → mɔʁd̪ʁ   (ʀ→ʁ, ʀ→ʁ)
```

## nef

`n̪ˈɑːwem` → `n̪ɛf`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈn̪ɑː.wem → ˈn̪ɑː.ɣʷem   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪ɑː.ɣʷem → ˈn̪ɑː.ɣʷɛm   (e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈn̪ɑː.ɣʷɛm → ˈn̪ɑː.βʷɛm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˈn̪ɑː.βʷɛm → ˈn̪ɑ.βʷɛm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪ɑ.βʷɛm → ˈn̪ɑ.βʷɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈn̪ɑ.βʷɛ → ˈn̪ɑː.βʷɛ   (ˈɑ→ˈɑː)
500: labialized bilabial fricatives delabialize
    ˈn̪ɑː.βʷɛ → ˈn̪ɑː.βɛ   (βʷ→β)
500: the low vowel fronts by default
    ˈn̪ɑː.βɛ → ˈn̪aː.βɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪aː.βɛ → ˈn̪aː.βə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈn̪aː.βə → ˈn̪aːβə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪aːβə̯ → ˈn̪aːβ   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈn̪aːβ → ˈn̪ae̯β   (ˈaː→ˈae̯)
600: the remaining bilabial fricative becomes v
    ˈn̪ae̯β → ˈn̪ae̯v   (β→v)
750: all final obstruents devoice
    ˈn̪ae̯v → ˈn̪ae̯f   (v→f)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈn̪ae̯f → ˈn̪eːf   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈn̪eːf → ˈn̪ef   (ˈeː→ˈe)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈn̪ef → ˈn̪ɛf   (ˈe→ˈɛ)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈn̪ɛf → ˈn̪ɛfə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈn̪ɛfə̯ → ˈn̪ɛf   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪ɛf → n̪ɛf   (ˈɛ→ɛ)
```

## nouvelle

`n̪ˌowˈellɑm` → `n̪u.vɛl`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌn̪oˈwel.lɑm → ˌn̪oˈɣʷel.lɑm   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌn̪oˈɣʷel.lɑm → ˌn̪ɔˈɣʷɛl.lɑm   (ˌo→ˌɔ, ˈe→ˈɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌn̪ɔˈɣʷɛl.lɑm → ˌn̪ɔˈβʷɛl.lɑm   (ɣʷ→βʷ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌn̪ɔˈβʷɛl.lɑm → ˌn̪ɔˈβʷɛl.lɑ   (m→∅)
500: labialized bilabial fricatives delabialize
    ˌn̪ɔˈβʷɛl.lɑ → ˌn̪ɔˈβɛl.lɑ   (βʷ→β)
500: the low vowel fronts by default
    ˌn̪ɔˈβɛl.lɑ → ˌn̪ɔˈβɛl.la   (ɑ→a)
600: secondary-stressed ɔ raises to o unconditionally
    ˌn̪ɔˈβɛl.la → ˌn̪oˈβɛl.la   (ˌɔ→ˌo)
600: the remaining bilabial fricative becomes v
    ˌn̪oˈβɛl.la → ˌn̪oˈvɛl.la   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌn̪oˈvɛl.la → ˌn̪oˈvɛl.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˌn̪oˈvɛl.lə → ˌn̪oˈvɛ.lə   (l→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌn̪oˈvɛ.lə → ˌn̪uˈvɛ.lə   (ˌo→ˌu)
1400: final ə becomes a non-syllabic off-glide
    ˌn̪uˈvɛ.lə → ˌn̪uˈvɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌn̪uˈvɛlə̯ → ˌn̪uˈvɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌn̪uˈvɛl → n̪u.vɛl   (ˌu→u, ˈɛ→ɛ)
```

## œuf

`ˈowum` → `œf`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈo.wum → ˈo.ɣʷum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈo.ɣʷum → ˈɔ.ɣʷʊm   (ˈo→ˈɔ, u→ʊ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɔ.ɣʷʊm → ˈɔ.βʷʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈɔ.βʷʊm → ˈɔ.βʷom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɔ.βʷom → ˈɔ.βʷo   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈɔ.βʷo → ˈɔː.βʷo   (ˈɔ→ˈɔː)
500: labialized bilabial fricatives delabialize
    ˈɔː.βʷo → ˈɔː.βo   (βʷ→β)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈɔː.βo → ˈuo̯.βo   (ˈɔː→ˈuo̯)
500: a high tense round non-nasal vowel centralizes
    ˈuo̯.βo → ˈʉo̯.βo   (ˈu→ˈʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈʉo̯.βo → ˈʉo̯.βə   (o→ə)
600: schwa becomes non-syllabic
    ˈʉo̯.βə → ˈʉo̯βə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈʉo̯βə̯ → ˈʉo̯β   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˈʉo̯β → ˈʉo̯v   (β→v)
750: all final obstruents devoice
    ˈʉo̯v → ˈʉo̯f   (v→f)
1000: high round back vowels front (completion of u-fronting)
    ˈʉo̯f → ˈyo̯f   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈyo̯f → ˈye̯f   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈye̯f → ˈøf   (ˈye̯→ˈø)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈøf → ˈøfə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈøfə̯ → ˈøf   (ə̯→∅)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈøf → ˈœf   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˈœf → œf   (ˈœ→œ)
```

## part

`pˈɑrt̪em` → `paʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpɑr.t̪em → ˈpɑr.t̪ɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpɑr.t̪ɛm → ˈpɑr.t̪ɛ   (m→∅)
500: the low vowel fronts by default
    ˈpɑr.t̪ɛ → ˈpar.t̪ɛ   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpar.t̪ɛ → ˈpar.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpar.t̪ə → ˈpart̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpart̪ə̯ → ˈpart̪   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈpart̪ → ˈpaɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈpaɹt̪ → ˈpaɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈpaɹ → ˈpar   (ɹ→r)
1400: r becomes uvular ʀ
    ˈpar → ˈpaʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpaʀ → paʀ   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    paʀ → paʁ   (ʀ→ʁ)
```

## poêle

`pˈeːn̪silem` → `pwal`

```
-100: n lost after a long vowel before s (compensatory lengthening already applied)
    ˈpeːn̪.si.lem → ˈpeː.si.lem   (n̪→∅)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpeː.si.lem → ˈpeː.sɪ.lɛm   (i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpeː.sɪ.lɛm → ˈpe.sɪ.lɛm   (ˈeː→ˈe)
-100: lax high vowels lower to tense mid vowels
    ˈpe.sɪ.lɛm → ˈpe.se.lɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpe.se.lɛm → ˈpe.se.lɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpe.se.lɛ → ˈpeː.se.lɛ   (ˈe→ˈeː)
500: a voiceless fricative voices intervocalically
    ˈpeː.se.lɛ → ˈpeː.ze.lɛ   (s→z)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈpeː.ze.lɛ → ˈpeː.zə.lɛ   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpeː.zə.lɛ → ˈpeː.zə.lə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpeː.zə.lə → ˈpeːzə̯lə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈpeːzə̯lə̯ → ˈpeːzə̯.lə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈpeːzə̯.lə → ˈpeː.zlə   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈpeː.zlə → ˈpej.zlə   (ˈeː→ˈej)
1000: z is lost before a consonant (preconsonantal effacement)
    ˈpej.zlə → ˈpej.lə   (z→∅)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈpej.lə → ˈpoj.lə   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈpoj.lə → ˈpuj.lə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈpuj.lə → ˈpuɛ̯.lə   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈpuɛ̯.lə → ˈpwɛ.lə   (ˈu→w, ɛ̯→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈpwɛ.lə → ˈpwɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpwɛlə̯ → ˈpwɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpwɛl → pwɛl   (ˈɛ→ɛ)
1400: wɛ becomes wa
    pwɛl → pwal   (ɛ→a)
```

## poix

`pˈikem` → `pwa`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpi.kem → ˈpɪ.kɛm   (ˈi→ˈɪ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈpɪ.kɛm → ˈpe.kɛm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpe.kɛm → ˈpe.kɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈpe.kɛ → ˈpe.kʲɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈpe.kʲɛ → ˈpe.cɛ   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpe.cɛ → ˈpeː.cɛ   (ˈe→ˈeː)
500: a palatal stop affricates
    ˈpeː.cɛ → ˈpeː.t͡sʲɛ   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpeː.t͡sʲɛ → ˈpeː.t͡sʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpeː.t͡sʲə → ˈpeːt͡sʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpeːt͡sʲə̯ → ˈpeːt͡sʲ   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈpeːt͡sʲ → ˈpejt͡sʲ   (ˈeː→ˈej)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈpejt͡sʲ → ˈpojt͡sʲ   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈpojt͡sʲ → ˈpujt͡sʲ   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈpujt͡sʲ → ˈpuɛ̯t͡sʲ   (j→ɛ̯)
1000: all affricates become sibilants (deaffrication)
    ˈpuɛ̯t͡sʲ → ˈpuɛ̯sʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈpuɛ̯sʲ → ˈpuɛ̯s   (sʲ→s)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈpuɛ̯s → ˈpwɛs   (ˈu→w, ɛ̯→ˈɛ)
1400: final obstruents are lost
    ˈpwɛs → ˈpwɛ   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpwɛ → pwɛ   (ˈɛ→ɛ)
1400: wɛ becomes wa
    pwɛ → pwa   (ɛ→a)
```

## plats

`plˈɑt̪t̪oːs` → `pla`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈplɑt̪.t̪oːs → ˈplɑt̪.t̪os   (oː→o)
500: the low vowel fronts by default
    ˈplɑt̪.t̪os → ˈplat̪.t̪os   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈplat̪.t̪os → ˈplat̪.t̪əs   (o→ə)
600: schwa becomes non-syllabic
    ˈplat̪.t̪əs → ˈplat̪t̪ə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈplat̪t̪ə̯s → ˈplat̪t̪s   (ə̯→∅)
600: a dental fricative + s becomes the affricate ts word-finally
    ˈplat̪t̪s → ˈplat̪t͡s   (t̪s→t͡s)
750: a dental stop deletes before another coronal stop
    ˈplat̪t͡s → ˈplat͡s   (t̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈplat͡s → ˈplas   (t͡s→s)
1400: final obstruents are lost
    ˈplas → ˈpla   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpla → pla   (ˈa→a)
```

## porcs

`pˈorkoːs` → `pɔʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpor.koːs → ˈpɔr.koːs   (ˈo→ˈɔ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpɔr.koːs → ˈpɔr.kos   (oː→o)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpɔr.kos → ˈpɔr.kəs   (o→ə)
600: schwa becomes non-syllabic
    ˈpɔr.kəs → ˈpɔrkə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpɔrkə̯s → ˈpɔrks   (ə̯→∅)
750: k is lost before word-final s
    ˈpɔrks → ˈpɔrs   (k→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈpɔrs → ˈpɔɹs   (r→ɹ)
1400: final obstruents are lost
    ˈpɔɹs → ˈpɔɹ   (s→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈpɔɹ → ˈpɔr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈpɔr → ˈpɔʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɔʀ → pɔʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɔʀ → pɔʁ   (ʀ→ʁ)
```

## priser

`prˌet̪iˈɑːre` → `pʁi.ze`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpre.t̪iˈɑː.re → ˌprɛ.t̪ɪˈɑː.rɛ   (ˌe→ˌɛ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌprɛ.t̪ɪˈɑː.rɛ → ˌprɛˈt̪jɑː.rɛ   (ɪ→j)
-100: yod strengthens before a vowel
    ˌprɛˈt̪jɑː.rɛ → ˌprɛˈt̪ʝɑː.rɛ   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌprɛˈt̪ʝɑː.rɛ → ˌprɛˈt̪ʝɑ.rɛ   (ˈɑː→ˈɑ)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌprɛˈt̪ʝɑ.rɛ → ˌprɛt͡sʲˈʝɑ.rɛ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌprɛt͡sʲˈʝɑ.rɛ → ˌprɛˈt͡sʲɑ.rɛ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌprɛˈt͡sʲɑ.rɛ → ˌprɛˈt͡sʲɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌprɛˈt͡sʲɑː.rɛ → ˌprɛˈt͡sʲaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌprɛˈt͡sʲaː.rɛ → ˌprɛˈt͡sʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌprɛˈt͡sʲaː.rə → ˌprɛˈt͡sʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌprɛˈt͡sʲaːrə̯ → ˌprɛˈt͡sʲaːr   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌprɛˈt͡sʲaːr → ˌprɛˈd͡zʲaːr   (t͡sʲ→d͡zʲ)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌprɛˈd͡zʲaːr → ˌprɛˈd͡zʲɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌprɛˈd͡zʲɛːr → ˌprɛˈd͡zʲie̯r   (ˈɛː→ˈie̯)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌprɛˈd͡zʲie̯r → ˌprɛˈzʲie̯r   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌprɛˈzʲie̯r → ˌprɛjˈzie̯r   (zʲ→jz)
600: secondary-stressed ɛj becomes i before a coronal
    ˌprɛjˈzie̯r → ˌpriˈzie̯r   (ˌɛj→ˌi)
600: a coronal palatalizes between two high-front segments
    ˌpriˈzie̯r → ˌpriˈzʲie̯r   (z→zʲ)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌpriˈzʲie̯r → ˌpriˈzʲjer   (ˈi→j, e̯→ˈe)
1200: je becomes e after a palatal consonant
    ˌpriˈzʲjer → ˌpriˈzʲer   (j→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌpriˈzʲer → ˌpriˈzer   (zʲ→z)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌpriˈzer → ˌpriˈzeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌpriˈzeɹ → ˌpriˈze   (ɹ→∅)
1400: r becomes uvular ʀ
    ˌpriˈze → ˌpʀiˈze   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpʀiˈze → pʀi.ze   (ˌi→i, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀi.ze → pʁi.ze   (ʀ→ʁ)
```

## poinçon

`pˌun̪kt̪iˈoːn̪em` → `pwɛ̃.sɔ̃`

```
-100: n assimilates to a following velar stop
    ˌpun̪k.t̪iˈoː.n̪em → ˌpuŋk.t̪iˈoː.n̪em   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpuŋk.t̪iˈoː.n̪em → ˌpʊŋk.t̪ɪˈoː.n̪ɛm   (ˌu→ˌʊ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌpʊŋk.t̪ɪˈoː.n̪ɛm → ˌpʊŋkˈt̪joː.n̪ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌpʊŋkˈt̪joː.n̪ɛm → ˌpʊŋkˈt̪ʝoː.n̪ɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpʊŋkˈt̪ʝoː.n̪ɛm → ˌpʊŋkˈt̪ʝo.n̪ɛm   (ˈoː→ˈo)
-100: k lost after ŋ before a voiceless coronal
    ˌpʊŋkˈt̪ʝo.n̪ɛm → ˌpʊŋˈt̪ʝo.n̪ɛm   (k→∅)
-100: lax high vowels lower to tense mid vowels
    ˌpʊŋˈt̪ʝo.n̪ɛm → ˌpoŋˈt̪ʝo.n̪ɛm   (ˌʊ→ˌo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpoŋˈt̪ʝo.n̪ɛm → ˌpoŋˈt̪ʝo.n̪ɛ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌpoŋˈt̪ʝo.n̪ɛ → ˌpoŋt͡sʲˈʝo.n̪ɛ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌpoŋt͡sʲˈʝo.n̪ɛ → ˌpoŋˈt͡sʲo.n̪ɛ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpoŋˈt͡sʲo.n̪ɛ → ˌpoŋˈt͡sʲoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌpoŋˈt͡sʲoː.n̪ɛ → ˌpũŋˈt͡sʲũː.n̪ɛ   (ˌo→ˌũ, ˈoː→ˈũː)
500: ŋ palatalizes to ɲ before a coronal
    ˌpũŋˈt͡sʲũː.n̪ɛ → ˌpũɲˈt͡sʲũː.n̪ɛ   (ŋ→ɲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpũɲˈt͡sʲũː.n̪ɛ → ˌpũɲˈt͡sʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌpũɲˈt͡sʲũː.n̪ə → ˌpũɲˈt͡sʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpũɲˈt͡sʲũːn̪ə̯ → ˌpũɲˈt͡sʲũːn̪   (ə̯→∅)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˌpũɲˈt͡sʲũːn̪ → ˌpũj̃n̪ˈt͡sʲũːn̪   (ɲ→j̃n̪)
750: vowel length resets to short
    ˌpũj̃n̪ˈt͡sʲũːn̪ → ˌpũj̃n̪ˈt͡sʲũn̪   (ˈũː→ˈũ)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌpũj̃n̪ˈt͡sʲũn̪ → ˌpũj̃ˈt͡sʲũn̪   (n̪→∅)
1000: the nasal diphthong ũj̃ becomes wĩ (syllabicity swap before a nasal)
    ˌpũj̃ˈt͡sʲũn̪ → pwj̩̃ˈt͡sʲũn̪   (ˌũ→w, j̃→j̩̃)
1000: all affricates become sibilants (deaffrication)
    pwj̩̃ˈt͡sʲũn̪ → pwj̩̃ˈsʲũn̪   (t͡sʲ→sʲ)
1200: nasalized ĩ lowers after w
    pwj̩̃ˈsʲũn̪ → pwj̩̃ˈsʲũn̪   (j̩̃→j̩̃)
1200: the remaining anterior palatalized consonants depalatalize
    pwj̩̃ˈsʲũn̪ → pwj̩̃ˈsũn̪   (sʲ→s)
1200: a front unrounded non-low vowel laxes and lowers after w
    pwj̩̃ˈsũn̪ → pwɛ̃ˈsũn̪   (j̩̃→ɛ̃)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    pwɛ̃ˈsũn̪ → pwɛ̃ˈsũː   (ˈũn̪→ˈũː)
1400: stress is leveled — no longer distinctive for vowels
    pwɛ̃ˈsũː → pwɛ̃.sũː   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    pwɛ̃.sũː → pwɛ̃.sũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    pwɛ̃.sũ → pwɛ̃.sɔ̃   (ũ→ɔ̃)
```

## rez

`rˈɑːsum` → `ʁe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈrɑː.sum → ˈrɑː.sʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈrɑː.sʊm → ˈrɑ.sʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˈrɑ.sʊm → ˈrɑ.som   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈrɑ.som → ˈrɑ.so   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈrɑ.so → ˈrɑː.so   (ˈɑ→ˈɑː)
500: a voiceless fricative voices intervocalically
    ˈrɑː.so → ˈrɑː.zo   (s→z)
500: the low vowel fronts by default
    ˈrɑː.zo → ˈraː.zo   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈraː.zo → ˈraː.zə   (o→ə)
600: schwa becomes non-syllabic
    ˈraː.zə → ˈraːzə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈraːzə̯ → ˈraːz   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈraːz → ˈrae̯z   (ˈaː→ˈae̯)
750: all final obstruents devoice
    ˈrae̯z → ˈrae̯s   (z→s)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈrae̯s → ˈreːs   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈreːs → ˈres   (ˈeː→ˈe)
1000: a primary-stressed vowel lengthens before word-final s
    ˈres → ˈreːs   (ˈe→ˈeː)
1400: final obstruents are lost
    ˈreːs → ˈreː   (s→∅)
1400: r becomes uvular ʀ
    ˈreː → ˈʀeː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀeː → ʀeː   (ˈeː→eː)
1400: distinctive vowel length is lost entirely
    ʀeː → ʀe   (eː→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀe → ʁe   (ʀ→ʁ)
```

## rumeur

`rˌuːmˈoːrem` → `ʁy.mœʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌruːˈmoː.rem → ˌruːˈmoː.rɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌruːˈmoː.rɛm → ˌruˈmo.rɛm   (ˌuː→ˌu, ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌruˈmo.rɛm → ˌruˈmo.rɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌruˈmo.rɛ → ˌruˈmoː.rɛ   (ˈo→ˈoː)
500: a high tense round non-nasal vowel centralizes
    ˌruˈmoː.rɛ → ˌrʉˈmoː.rɛ   (ˌu→ˌʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌrʉˈmoː.rɛ → ˌrʉˈmoː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌrʉˈmoː.rə → ˌrʉˈmoːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌrʉˈmoːrə̯ → ˌrʉˈmoːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌrʉˈmoːr → ˌrʉˈmowr   (ˈoː→ˈow)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˌrʉˈmowr → ˌrʉˈmør   (ˈow→ˈø)
1000: high round back vowels front (completion of u-fronting)
    ˌrʉˈmør → ˌryˈmør   (ˌʉ→ˌy)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌryˈmør → ˌrỹˈmør   (ˌy→ˌỹ)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌrỹˈmør → ˌryˈmør   (ˌỹ→ˌy)
1400: e/ø lax before an r that closes the syllable
    ˌryˈmør → ˌryˈmœr   (ˈø→ˈœ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌryˈmœr → ˌryˈmœɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌryˈmœɹ → ˌryˈmœr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌryˈmœr → ˌʀyˈmœʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʀyˈmœʀ → ʀy.mœʀ   (ˌy→y, ˈœ→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀy.mœʀ → ʁy.mœʁ   (ʀ→ʁ, ʀ→ʁ)
```

## sautier

`sˌɑlt̪uˈɑːrium` → `so.p̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑl.t̪uˈɑː.ri.um → ˌsɑl.t̪ʊˈɑː.rɪ.ʊm   (u→ʊ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌsɑl.t̪ʊˈɑː.rɪ.ʊm → ˌsɑlˈt̪wɑː.rjʊm   (ʊ→w, ɪ→j)
-100: l darkens before a non-lateral consonant
    ˌsɑlˈt̪wɑː.rjʊm → ˌsɑɫˈt̪wɑː.rjʊm   (l→ɫ)
-100: yod strengthens before a vowel
    ˌsɑɫˈt̪wɑː.rjʊm → ˌsɑɫˈt̪wɑːr.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑɫˈt̪wɑːr.ʝʊm → ˌsɑɫˈt̪wɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌsɑɫˈt̪wɑr.ʝʊm → ˌsɑɫˈt̪wɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɑɫˈt̪wɑr.ʝom → ˌsɑɫˈt̪wɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌsɑɫˈt̪wɑr.ʝo → ˌsɑɫˈt̪wɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌsɑɫˈt̪wɑ.rʲo → ˌsaɫˈt̪wa.rʲo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: w lost after a non-back consonant
    ˌsaɫˈt̪wa.rʲo → ˌsaɫˈt̪a.rʲo   (w→∅)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌsaɫˈt̪a.rʲo → ˌsaɫˈt̪ʲa.rʲo   (t̪→t̪ʲ)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌsaɫˈt̪ʲa.rʲo → ˌsaɫˈt̪ʲaː.rʲo   (ˈa→ˈaː)
600: aːrʲ metathesizes to jɛːr
    ˌsaɫˈt̪ʲaː.rʲo → ˌsaɫˈt̪ʲjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsaɫˈt̪ʲjɛː.ro → ˌsaɫˈt̪ʲjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌsaɫˈt̪ʲjɛː.rə → ˌsaɫˈt̪ʲjɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsaɫˈt̪ʲjɛːrə̯ → ˌsaɫˈt̪ʲjɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌsaɫˈt̪ʲjɛːr → ˌsaɫˈt̪ʲjie̯r   (ˈɛː→ˈie̯)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌsaɫˈt̪ʲjie̯r → ˌsaɫjˈt̪jie̯r   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌsaɫjˈt̪jie̯r → ˌsaɫˈt̪jie̯r   (j→∅)
600: a coronal palatalizes between two high-front segments
    ˌsaɫˈt̪jie̯r → ˌsaɫˈt̪ʲjie̯r   (t̪→t̪ʲ)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌsaɫˈt̪ʲjie̯r → ˌsaɫˈt̪ʲie̯r   (j→∅)
1000: back dark-l variants vocalize to w
    ˌsaɫˈt̪ʲie̯r → ˌsawˈt̪ʲie̯r   (ɫ→w)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌsawˈt̪ʲie̯r → ˌsawˈt̪ʲjer   (ˈi→j, e̯→ˈe)
1200: aw becomes long oː
    ˌsawˈt̪ʲjer → ˌsoːˈt̪ʲjer   (ˌaw→ˌoː)
1200: je becomes e after a palatal consonant
    ˌsoːˈt̪ʲjer → ˌsoːˈt̪ʲer   (j→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌsoːˈt̪ʲer → ˌsoːˈp̪er   (t̪ʲ→p̪)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsoːˈp̪er → ˌsoːˈp̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌsoːˈp̪eɹ → ˌsoːˈp̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsoːˈp̪e → soː.p̪e   (ˌoː→oː, ˈe→e)
1400: distinctive vowel length is lost entirely
    soː.p̪e → so.p̪e   (oː→o)
```

## saison

`sˌɑt̪iˈoːn̪em` → `sɛ.zɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑ.t̪iˈoː.n̪em → ˌsɑ.t̪ɪˈoː.n̪ɛm   (i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌsɑ.t̪ɪˈoː.n̪ɛm → ˌsɑˈt̪joː.n̪ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌsɑˈt̪joː.n̪ɛm → ˌsɑˈt̪ʝoː.n̪ɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑˈt̪ʝoː.n̪ɛm → ˌsɑˈt̪ʝo.n̪ɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɑˈt̪ʝo.n̪ɛm → ˌsɑˈt̪ʝo.n̪ɛ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌsɑˈt̪ʝo.n̪ɛ → ˌsɑt͡sʲˈʝo.n̪ɛ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌsɑt͡sʲˈʝo.n̪ɛ → ˌsɑˈt͡sʲo.n̪ɛ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɑˈt͡sʲo.n̪ɛ → ˌsɑˈt͡sʲoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌsɑˈt͡sʲoː.n̪ɛ → ˌsɑˈt͡sʲũː.n̪ɛ   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˌsɑˈt͡sʲũː.n̪ɛ → ˌsaˈt͡sʲũː.n̪ɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsaˈt͡sʲũː.n̪ɛ → ˌsaˈt͡sʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsaˈt͡sʲũː.n̪ə → ˌsaˈt͡sʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsaˈt͡sʲũːn̪ə̯ → ˌsaˈt͡sʲũːn̪   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌsaˈt͡sʲũːn̪ → ˌsaˈd͡zʲũːn̪   (t͡sʲ→d͡zʲ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌsaˈd͡zʲũːn̪ → ˌsaˈzʲũːn̪   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌsaˈzʲũːn̪ → ˌsajˈzũːn̪   (zʲ→jz)
750: vowel length resets to short
    ˌsajˈzũːn̪ → ˌsajˈzũn̪   (ˈũː→ˈũ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsajˈzũn̪ → ˌsajˈzũː   (ˈũn̪→ˈũː)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌsajˈzũː → ˌsɛːˈzũː   (ˌaj→ˌɛː)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɛːˈzũː → sɛː.zũː   (ˌɛː→ɛː, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    sɛː.zũː → sɛ.zũ   (ɛː→ɛ, ũː→ũ)
1400: nasal ũ opens to ɔ̃
    sɛ.zũ → sɛ.zɔ̃   (ũ→ɔ̃)
```

## serpent

`sˌerpˈen̪t̪em` → `sɛʁ.pɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌserˈpen̪.t̪em → ˌsɛrˈpɛn̪.t̪ɛm   (ˌe→ˌɛ, ˈe→ˈɛ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɛrˈpɛn̪.t̪ɛm → ˌsɛrˈpɛn̪.t̪ɛ   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsɛrˈpɛn̪.t̪ɛ → ˌsɛrˈpɛn̪.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsɛrˈpɛn̪.t̪ə → ˌsɛrˈpɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsɛrˈpɛn̪t̪ə̯ → ˌsɛrˈpɛn̪t̪   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌsɛrˈpɛn̪t̪ → ˌserˈpɛn̪t̪   (ˌɛ→ˌe)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌserˈpɛn̪t̪ → ˌserˈpɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌserˈpɛ̃n̪t̪ → ˌsɛrˈpɛ̃n̪t̪   (ˌe→ˌɛ)
1000: nasalized front mid vowels become nasalized a
    ˌsɛrˈpɛ̃n̪t̪ → ˌsɛrˈpãn̪t̪   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsɛrˈpãn̪t̪ → ˌsɛrˈpãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˌsɛrˈpãːt̪ → ˌsɛrˈpɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsɛrˈpɑ̃ːt̪ → ˌsɛɹˈpɑ̃ːt̪   (r→ɹ)
1400: final obstruents are lost
    ˌsɛɹˈpɑ̃ːt̪ → ˌsɛɹˈpɑ̃ː   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌsɛɹˈpɑ̃ː → ˌsɛrˈpɑ̃ː   (ɹ→r)
1400: r becomes uvular ʀ
    ˌsɛrˈpɑ̃ː → ˌsɛʀˈpɑ̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɛʀˈpɑ̃ː → sɛʀ.pɑ̃ː   (ˌɛ→ɛ, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    sɛʀ.pɑ̃ː → sɛʀ.pɑ̃   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɛʀ.pɑ̃ → sɛʁ.pɑ̃   (ʀ→ʁ)
```

## écuyer

`skˌuːt̪ˈɑːrium` → `e.kɥi.je`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌskuːˈt̪ɑː.ri.um → ˌskuːˈt̪ɑː.rɪ.ʊm   (i→ɪ, u→ʊ)
-100: i-prosthesis before word-initial s + consonant
    ˌskuːˈt̪ɑː.rɪ.ʊm → ˌɪsˌkuːˈt̪ɑː.rɪ.ʊm   (∅→ˌɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɪsˌkuːˈt̪ɑː.rɪ.ʊm → ˌɪsˌkuːˈt̪ɑː.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɪsˌkuːˈt̪ɑː.rjʊm → ˌɪsˌkuːˈt̪ɑːr.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɪsˌkuːˈt̪ɑːr.ʝʊm → ˌɪsˌkuˈt̪ɑr.ʝʊm   (ˌuː→ˌu, ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌɪsˌkuˈt̪ɑr.ʝʊm → ˌesˌkuˈt̪ɑr.ʝom   (ˌɪ→ˌe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌesˌkuˈt̪ɑr.ʝom → ˌesˌkuˈt̪ɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌesˌkuˈt̪ɑr.ʝo → ˌesˌkuˈt̪ɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌesˌkuˈt̪ɑ.rʲo → ˌesˌkuˈt̪a.rʲo   (ˈɑ→ˈa)
500: a high tense round non-nasal vowel centralizes
    ˌesˌkuˈt̪a.rʲo → ˌesˌkʉˈt̪a.rʲo   (ˌu→ˌʉ)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌesˌkʉˈt̪a.rʲo → ˌesˌkʉˈt̪aː.rʲo   (ˈa→ˈaː)
600: aːrʲ metathesizes to jɛːr
    ˌesˌkʉˈt̪aː.rʲo → ˌesˌkʉˈt̪jɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌesˌkʉˈt̪jɛː.ro → ˌesˌkʉˈt̪jɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌesˌkʉˈt̪jɛː.rə → ˌesˌkʉˈt̪jɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌesˌkʉˈt̪jɛːrə̯ → ˌesˌkʉˈt̪jɛːr   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌesˌkʉˈt̪jɛːr → ˌesˌkʉˈd̪jɛːr   (t̪→d̪)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌesˌkʉˈd̪jɛːr → ˌesˌkʉˈd̪jie̯r   (ˈɛː→ˈie̯)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌesˌkʉˈd̪jie̯r → ˌesˌkʉˈðjie̯r   (d̪→ð)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌesˌkʉˈðjie̯r → ˌesˌkʉˈðie̯r   (j→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌesˌkʉˈðie̯r → ˌesˌkyˈðie̯r   (ˌʉ→ˌy)
1000: s becomes x after a vowel, before any consonant
    ˌesˌkyˈðie̯r → ˌexˌkyˈðie̯r   (s→x)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌexˌkyˈðie̯r → ˌexˌkyˈðjer   (ˈi→j, e̯→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌexˌkyˈðjer → ˌexˌkyˈjer   (ð→∅)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌexˌkyˈjer → ˌeːˌkyˈjer   (ˌex→ˌeː)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˌeːˌkyˈjer → ˌeːˌkɥiˈer   (ˌy→ɥ, j→ˌi)
1400: j is inserted between a back-conditioned ɥi and a following vowel
    ˌeːˌkɥiˈer → ˌeːˌkɥiˈjer   (∅→j)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌeːˌkɥiˈjer → ˌeːˌkɥiˈjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌeːˌkɥiˈjeɹ → ˌeːˌkɥiˈje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌeːˌkɥiˈje → eː.kɥi.je   (ˌeː→eː, ˌi→i, ˈe→e)
1400: distinctive vowel length is lost entirely
    eː.kɥi.je → e.kɥi.je   (eː→e)
```

## étaim

`st̪ˈɑːmen̪` → `e.t̪ɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈst̪ɑː.men̪ → ˈst̪ɑː.mɛn̪   (e→ɛ)
-100: i-prosthesis before word-initial s + consonant
    ˈst̪ɑː.mɛn̪ → ˌɪsˈt̪ɑː.mɛn̪   (∅→ˌɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɪsˈt̪ɑː.mɛn̪ → ˌɪsˈt̪ɑ.mɛn̪   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌɪsˈt̪ɑ.mɛn̪ → ˌesˈt̪ɑ.mɛn̪   (ˌɪ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌesˈt̪ɑ.mɛn̪ → ˌesˈt̪ɑ.mɛ   (n̪→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌesˈt̪ɑ.mɛ → ˌesˈt̪ɑː.mɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌesˈt̪ɑː.mɛ → ˌesˈt̪aː.mɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌesˈt̪aː.mɛ → ˌesˈt̪aː.mə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌesˈt̪aː.mə → ˌesˈt̪aːmə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌesˈt̪aːmə̯ → ˌesˈt̪aːm   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌesˈt̪aːm → ˌesˈt̪ae̯m   (ˈaː→ˈae̯)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˌesˈt̪ae̯m → ˌesˈt̪ajm   (e̯→j)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˌesˈt̪ajm → ˌesˈt̪aj̃m   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌesˈt̪aj̃m → ˌesˈt̪ãj̃m   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌesˈt̪ãj̃m → ˌesˈt̪ɛ̃j̃m   (ˈã→ˈɛ̃)
1000: s becomes x after a vowel, before any consonant
    ˌesˈt̪ɛ̃j̃m → ˌexˈt̪ɛ̃j̃m   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌexˈt̪ɛ̃j̃m → ˌeːˈt̪ɛ̃j̃m   (ˌex→ˌeː)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌeːˈt̪ɛ̃j̃m → ˌeːˈt̪ɛ̃m   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌeːˈt̪ɛ̃m → ˌeːˈt̪ɛ̃ː   (ˈɛ̃m→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌeːˈt̪ɛ̃ː → eː.t̪ɛ̃ː   (ˌeː→eː, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    eː.t̪ɛ̃ː → e.t̪ɛ̃   (eː→e, ɛ̃ː→ɛ̃)
```

## sourde

`sˈurd̪ɑm` → `suʁd̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsur.d̪ɑm → ˈsʊr.d̪ɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈsʊr.d̪ɑm → ˈsor.d̪ɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsor.d̪ɑm → ˈsor.d̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈsor.d̪ɑ → ˈsor.d̪a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈsor.d̪a → ˈsor.d̪ə   (a→ə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈsor.d̪ə → ˈsur.d̪ə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈsur.d̪ə → ˈsurd̪ə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsurd̪ə̯ → ˈsuɹd̪ə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈsuɹd̪ə̯ → ˈsuɹd̪   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsuɹd̪ → ˈsurd̪   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsurd̪ → ˈsuʀd̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsuʀd̪ → suʀd̪   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    suʀd̪ → suʁd̪   (ʀ→ʁ)
```

## tarde

`t̪ˈɑrd̪ɑm` → `t̪aʁd̪`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɑr.d̪ɑm → ˈt̪ɑr.d̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈt̪ɑr.d̪ɑ → ˈt̪ar.d̪a   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt̪ar.d̪a → ˈt̪ar.d̪ə   (a→ə)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪ar.d̪ə → ˈt̪ard̪ə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈt̪ard̪ə̯ → ˈt̪aɹd̪ə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪aɹd̪ə̯ → ˈt̪aɹd̪   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈt̪aɹd̪ → ˈt̪ard̪   (ɹ→r)
1400: r becomes uvular ʀ
    ˈt̪ard̪ → ˈt̪aʀd̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪aʀd̪ → t̪aʀd̪   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪aʀd̪ → t̪aʁd̪   (ʀ→ʁ)
```

## timon

`t̪ˌiːmˈoːn̪em` → `t̪i.mɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪iːˈmoː.n̪em → ˌt̪iːˈmoː.n̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌt̪iːˈmoː.n̪ɛm → ˌt̪iˈmo.n̪ɛm   (ˌiː→ˌi, ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌt̪iˈmo.n̪ɛm → ˌt̪iˈmo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌt̪iˈmo.n̪ɛ → ˌt̪iˈmoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌt̪iˈmoː.n̪ɛ → ˌt̪iˈmũː.n̪ɛ   (ˈoː→ˈũː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪iˈmũː.n̪ɛ → ˌt̪iˈmũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt̪iˈmũː.n̪ə → ˌt̪iˈmũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪iˈmũːn̪ə̯ → ˌt̪iˈmũːn̪   (ə̯→∅)
750: vowel length resets to short
    ˌt̪iˈmũːn̪ → ˌt̪iˈmũn̪   (ˈũː→ˈũ)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌt̪iˈmũn̪ → ˌt̪ĩˈmũn̪   (ˌi→ˌĩ)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌt̪ĩˈmũn̪ → ˌt̪iˈmũn̪   (ˌĩ→ˌi)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪iˈmũn̪ → ˌt̪iˈmũː   (ˈũn̪→ˈũː)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪iˈmũː → t̪i.mũː   (ˌi→i, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    t̪i.mũː → t̪i.mũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    t̪i.mũ → t̪i.mɔ̃   (ũ→ɔ̃)
```

## trou

`t̪rˈɑwkum` → `t̪ʁjø`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪rɑw.kum → ˈt̪rɑw.kʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪rɑw.kʊm → ˈt̪rɑw.kom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪rɑw.kom → ˈt̪rɑw.ko   (m→∅)
500: k voices to g intervocalically
    ˈt̪rɑw.ko → ˈt̪rɑw.go   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˈt̪rɑw.go → ˈt̪rɑw.ɣo   (g→ɣ)
500: the velar fricative is lost after a rounded non-syllabic glide before an unstressed tense round vowel
    ˈt̪rɑw.ɣo → ˈt̪rɑ.wo   (ɣ→∅)
500: the low vowel fronts by default
    ˈt̪rɑ.wo → ˈt̪ra.wo   (ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˈt̪ra.wo → ˈt̪raː.wo   (ˈa→ˈaː)
500: a vowel shortens before the high back round glide (w)
    ˈt̪raː.wo → ˈt̪ra.wo   (ˈaː→ˈa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈt̪ra.wo → ˈt̪rɔ.wo   (ˈa→ˈɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪rɔ.wo → ˈt̪rɔ.wə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪rɔ.wə → ˈt̪rɔwə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪rɔwə̯ → ˈt̪rɔw   (ə̯→∅)
600: a stressed vowel lengthens in a monosyllable before a final consonant
    ˈt̪rɔw → ˈt̪rɔːw   (ˈɔ→ˈɔː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˈt̪rɔːw → ˈt̪ruo̯w   (ˈɔː→ˈuo̯)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈt̪ruo̯w → ˈt̪rʉo̯w   (ˈu→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈt̪rʉo̯w → ˈt̪ryo̯w   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈt̪ryo̯w → ˈt̪rye̯w   (o̯→e̯)
1000: the e-glide rounds to ø before a back sonorant (or ɫ)
    ˈt̪rye̯w → ˈt̪ryø̯w   (e̯→ø̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ryø̯w → ˈt̪rɥøw   (ˈy→ɥ, ø̯→ˈø)
1000: ɥ delabializes to j before a front rounded mid vowel (ɥø > jø)
    ˈt̪rɥøw → ˈt̪rjøw   (ɥ→j)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈt̪rjøw → ˈt̪rjø   (w→∅)
1400: r becomes uvular ʀ
    ˈt̪rjø → ˈt̪ʀjø   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ʀjø → t̪ʀjø   (ˈø→ø)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪ʀjø → t̪ʁjø   (ʀ→ʁ)
```

## ton

`t̪uˌum` → `t̪ɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    t̪uˌum → t̪ʊˌʊm   (u→ʊ, ˌu→ˌʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    t̪ʊˌʊm → ˌt̪wʊm   (ʊ→w)
-100: lax high vowels lower to tense mid vowels
    ˌt̪wʊm → ˌt̪wom   (ˌʊ→ˌo)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌt̪wom → ˌt̪wũm   (ˌo→ˌũ)
500: w lost after a non-back consonant
    ˌt̪wũm → ˌt̪ũm   (w→∅)
1000: final m dentalizes after a vowel
    ˌt̪ũm → ˌt̪ũn̪   (m→n̪)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪ũn̪ → ˌt̪ũː   (ˌũn̪→ˌũː)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪ũː → t̪ũː   (ˌũː→ũː)
1400: distinctive vowel length is lost entirely
    t̪ũː → t̪ũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    t̪ũ → t̪ɔ̃   (ũ→ɔ̃)
```

## vanter

`wˌɑːn̪it̪ˈɑːre` → `vɑ̃.t̪e`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌwɑː.n̪iˈt̪ɑː.re → ˌɣʷɑː.n̪iˈt̪ɑː.re   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɣʷɑː.n̪iˈt̪ɑː.re → ˌɣʷɑː.n̪ɪˈt̪ɑː.rɛ   (i→ɪ, e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɣʷɑː.n̪ɪˈt̪ɑː.rɛ → ˌβʷɑː.n̪ɪˈt̪ɑː.rɛ   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌβʷɑː.n̪ɪˈt̪ɑː.rɛ → ˌβʷɑ.n̪ɪˈt̪ɑ.rɛ   (ˌɑː→ˌɑ, ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌβʷɑ.n̪ɪˈt̪ɑ.rɛ → ˌβʷɑ.n̪eˈt̪ɑ.rɛ   (ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˌβʷɑ.n̪eˈt̪ɑ.rɛ → ˌβʷɑ.n̪eˈt̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: labialized bilabial fricatives delabialize
    ˌβʷɑ.n̪eˈt̪ɑː.rɛ → ˌβɑ.n̪eˈt̪ɑː.rɛ   (βʷ→β)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌβɑ.n̪eˈt̪ɑː.rɛ → ˌβɑn̪ˈt̪ɑː.rɛ   (e→∅)
500: the low vowel fronts by default
    ˌβɑn̪ˈt̪ɑː.rɛ → ˌβan̪ˈt̪aː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌβan̪ˈt̪aː.rɛ → ˌβan̪ˈt̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌβan̪ˈt̪aː.rə → ˌβan̪ˈt̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌβan̪ˈt̪aːrə̯ → ˌβan̪ˈt̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌβan̪ˈt̪aːr → ˌβan̪ˈt̪ae̯r   (ˈaː→ˈae̯)
600: the remaining bilabial fricative becomes v
    ˌβan̪ˈt̪ae̯r → ˌvan̪ˈt̪ae̯r   (β→v)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌvan̪ˈt̪ae̯r → ˌvan̪ˈt̪eːr   (ˈae̯→ˈeː)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌvan̪ˈt̪eːr → ˌvãn̪ˈt̪eːr   (ˌa→ˌã)
1000: vowel length resets to short
    ˌvãn̪ˈt̪eːr → ˌvãn̪ˈt̪er   (ˈeː→ˈe)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌvãn̪ˈt̪er → ˌvãːˈt̪er   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌvãːˈt̪er → ˌvɑ̃ːˈt̪er   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌvɑ̃ːˈt̪er → ˌvɑ̃ːˈt̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌvɑ̃ːˈt̪eɹ → ˌvɑ̃ːˈt̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌvɑ̃ːˈt̪e → vɑ̃ː.t̪e   (ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    vɑ̃ː.t̪e → vɑ̃.t̪e   (ɑ̃ː→ɑ̃)
```

## vergogne

`wˌereːkˈun̪d̪iɑm` → `vɛʁ.gɔɲ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌwe.reːˈkun̪.d̪i.ɑm → ˌɣʷe.reːˈkun̪.d̪i.ɑm   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɣʷe.reːˈkun̪.d̪i.ɑm → ˌɣʷɛ.reːˈkʊn̪.d̪ɪ.ɑm   (ˌe→ˌɛ, ˈu→ˈʊ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɣʷɛ.reːˈkʊn̪.d̪ɪ.ɑm → ˌɣʷɛ.reːˈkʊn̪.d̪jɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɣʷɛ.reːˈkʊn̪.d̪jɑm → ˌɣʷɛ.reːˈkʊn̪.d̪ʝɑm   (j→ʝ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɣʷɛ.reːˈkʊn̪.d̪ʝɑm → ˌβʷɛ.reːˈkʊn̪.d̪ʝɑm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌβʷɛ.reːˈkʊn̪.d̪ʝɑm → ˌβʷɛ.reˈkʊn̪.d̪ʝɑm   (eː→e)
-100: lax high vowels lower to tense mid vowels
    ˌβʷɛ.reˈkʊn̪.d̪ʝɑm → ˌβʷɛ.reˈkon̪.d̪ʝɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌβʷɛ.reˈkon̪.d̪ʝɑm → ˌβʷɛ.reˈkon̪.d̪ʝɑ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌβʷɛ.reˈkon̪.d̪ʝɑ → ˌβʷɛ.reˈkon̪.ɟʝɑ   (d̪→ɟ)
300: yod absorbed into a preceding palatalized consonant
    ˌβʷɛ.reˈkon̪.ɟʝɑ → ˌβʷɛ.reˈkon̪.ɟɑ   (ʝ→∅)
500: k voices to g intervocalically
    ˌβʷɛ.reˈkon̪.ɟɑ → ˌβʷɛ.reˈgon̪.ɟɑ   (k→g)
500: unstressed mid front vowel syncopates between (front vowel + r) and (consonant + back stressed vowel)
    ˌβʷɛ.reˈgon̪.ɟɑ → ˌβʷɛrˈgon̪.ɟɑ   (e→∅)
500: labialized bilabial fricatives delabialize
    ˌβʷɛrˈgon̪.ɟɑ → ˌβɛrˈgon̪.ɟɑ   (βʷ→β)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌβɛrˈgon̪.ɟɑ → ˌβɛrˈgũn̪.ɟɑ   (ˈo→ˈũ)
500: a non-labial nasal palatalizes before a voiced high-front non-nasal consonant
    ˌβɛrˈgũn̪.ɟɑ → ˌβɛrˈgũɲ.ɟɑ   (n̪→ɲ)
500: a high-front glide is lost after a high-front nasal sonorant consonant (ɲ)
    ˌβɛrˈgũɲ.ɟɑ → ˌβɛrˈgũ.ɲɑ   (ɟ→∅)
500: the low vowel fronts by default
    ˌβɛrˈgũ.ɲɑ → ˌβɛrˈgũ.ɲa   (ɑ→a)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌβɛrˈgũ.ɲa → ˌβɛrˈgũː.ɲa   (ˈũ→ˈũː)
600: a vowel shortens before ɲ
    ˌβɛrˈgũː.ɲa → ˌβɛrˈgũ.ɲa   (ˈũː→ˈũ)
600: secondary-stressed ɛ raises to e before any two segments
    ˌβɛrˈgũ.ɲa → ˌβerˈgũ.ɲa   (ˌɛ→ˌe)
600: the remaining bilabial fricative becomes v
    ˌβerˈgũ.ɲa → ˌverˈgũ.ɲa   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌverˈgũ.ɲa → ˌverˈgũ.ɲə   (a→ə)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌverˈgũ.ɲə → ˌvɛrˈgũ.ɲə   (ˌe→ˌɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌvɛrˈgũ.ɲə → ˌvɛrˈgũɲə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌvɛrˈgũɲə̯ → ˌvɛɹˈgũɲə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˌvɛɹˈgũɲə̯ → ˌvɛɹˈgũɲ   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌvɛɹˈgũɲ → ˌvɛrˈgũɲ   (ɹ→r)
1400: r becomes uvular ʀ
    ˌvɛrˈgũɲ → ˌvɛʀˈgũɲ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌvɛʀˈgũɲ → vɛʀ.gũɲ   (ˌɛ→ɛ, ˈũ→ũ)
1400: nasal ũ opens to ɔ̃
    vɛʀ.gũɲ → vɛʀ.gɔ̃ɲ   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    vɛʀ.gɔ̃ɲ → vɛʀ.gɔɲ   (ɔ̃→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    vɛʀ.gɔɲ → vɛʁ.gɔɲ   (ʀ→ʁ)
```

## vendange

`wˌin̪d̪ˈeːmiɑm` → `vɑ̃.d̪ɑ̃ʒ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌwin̪ˈd̪eː.mi.ɑm → ˌɣʷin̪ˈd̪eː.mi.ɑm   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɣʷin̪ˈd̪eː.mi.ɑm → ˌɣʷɪn̪ˈd̪eː.mɪ.ɑm   (ˌi→ˌɪ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɣʷɪn̪ˈd̪eː.mɪ.ɑm → ˌɣʷɪn̪ˈd̪eː.mjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɣʷɪn̪ˈd̪eː.mjɑm → ˌɣʷɪn̪ˈd̪eːm.ʝɑm   (j→ʝ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɣʷɪn̪ˈd̪eːm.ʝɑm → ˌβʷɪn̪ˈd̪eːm.ʝɑm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌβʷɪn̪ˈd̪eːm.ʝɑm → ˌβʷɪn̪ˈd̪em.ʝɑm   (ˈeː→ˈe)
-100: lax high vowels lower to tense mid vowels
    ˌβʷɪn̪ˈd̪em.ʝɑm → ˌβʷen̪ˈd̪em.ʝɑm   (ˌɪ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌβʷen̪ˈd̪em.ʝɑm → ˌβʷen̪ˈd̪em.ʝɑ   (m→∅)
500: labialized bilabial fricatives delabialize
    ˌβʷen̪ˈd̪em.ʝɑ → ˌβen̪ˈd̪em.ʝɑ   (βʷ→β)
500: the low vowel fronts by default
    ˌβen̪ˈd̪em.ʝɑ → ˌβen̪ˈd̪em.ʝa   (ɑ→a)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˌβen̪ˈd̪em.ʝa → ˌβen̪ˈd̪em.ɟa   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˌβen̪ˈd̪em.ɟa → ˌβen̪ˈd̪em.d͡ʒa   (ɟ→d͡ʒ)
600: m becomes n before dʒ
    ˌβen̪ˈd̪em.d͡ʒa → ˌβen̪ˈd̪en̪.d͡ʒa   (m→n̪)
600: the remaining bilabial fricative becomes v
    ˌβen̪ˈd̪en̪.d͡ʒa → ˌven̪ˈd̪en̪.d͡ʒa   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌven̪ˈd̪en̪.d͡ʒa → ˌven̪ˈd̪en̪.d͡ʒə   (a→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌven̪ˈd̪en̪.d͡ʒə → ˌvẽn̪ˈd̪ẽn̪.d͡ʒə   (ˌe→ˌẽ, ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˌvẽn̪ˈd̪ẽn̪.d͡ʒə → ˌvɛ̃n̪ˈd̪ɛ̃n̪.d͡ʒə   (ˌẽ→ˌɛ̃, ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌvɛ̃n̪ˈd̪ɛ̃n̪.d͡ʒə → ˌvãn̪ˈd̪ãn̪.d͡ʒə   (ˌɛ̃→ˌã, ˈɛ̃→ˈã)
1000: all affricates become sibilants (deaffrication)
    ˌvãn̪ˈd̪ãn̪.d͡ʒə → ˌvãn̪ˈd̪ãn̪.ʒə   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌvãn̪ˈd̪ãn̪.ʒə → ˌvãːˈd̪ãː.ʒə   (ˌãn̪ˈd̪ãn̪→ˌãːˈd̪ãː)
1400: final ə becomes a non-syllabic off-glide
    ˌvãːˈd̪ãː.ʒə → ˌvãːˈd̪ãːʒə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌvãːˈd̪ãːʒə̯ → ˌvɑ̃ːˈd̪ɑ̃ːʒə̯   (ˌãː→ˌɑ̃ː, ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˌvɑ̃ːˈd̪ɑ̃ːʒə̯ → ˌvɑ̃ːˈd̪ɑ̃ːʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌvɑ̃ːˈd̪ɑ̃ːʒ → vɑ̃ː.d̪ɑ̃ːʒ   (ˌɑ̃ː→ɑ̃ː, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    vɑ̃ː.d̪ɑ̃ːʒ → vɑ̃.d̪ɑ̃ʒ   (ɑ̃ː→ɑ̃, ɑ̃ː→ɑ̃)
```

## abbé

`ˌɑbbˈɑːt̪em` → `a.be`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑbˈbɑː.t̪em → ˌɑbˈbɑː.t̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑbˈbɑː.t̪ɛm → ˌɑbˈbɑ.t̪ɛm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑbˈbɑ.t̪ɛm → ˌɑbˈbɑ.t̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑbˈbɑ.t̪ɛ → ˌɑbˈbɑː.t̪ɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌɑbˈbɑː.t̪ɛ → ˌabˈbaː.t̪ɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌabˈbaː.t̪ɛ → ˌabˈbaː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌabˈbaː.t̪ə → ˌabˈbaːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌabˈbaːt̪ə̯ → ˌabˈbaːt̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌabˈbaːt̪ → ˌabˈbae̯t̪   (ˈaː→ˈae̯)
750: a word-final stop re-opens to a fricative after a vowel
    ˌabˈbae̯t̪ → ˌabˈbae̯θ   (t̪→θ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌabˈbae̯θ → ˌabˈbeːθ   (ˈae̯→ˈeː)
750: an identical consonant geminate reduces to one (recurrence)
    ˌabˈbeːθ → ˌaˈbeːθ   (b→∅)
1000: vowel length resets to short
    ˌaˈbeːθ → ˌaˈbeθ   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌaˈbeθ → ˌaˈbe   (θ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈbe → a.be   (ˌa→a, ˈe→e)
```

## ai

`hˈɑbeo` → `aʒ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈhɑ.be.o → ˈhɑ.bɛ.ɔ   (e→ɛ, o→ɔ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈhɑ.bɛ.ɔ → ˈhɑ.bjɔ   (ɛ→j)
-100: yod strengthens before a vowel
    ˈhɑ.bjɔ → ˈhɑ.bʝɔ   (j→ʝ)
500: h lost unconditionally (any remaining h)
    ˈhɑ.bʝɔ → ˈɑ.bʝɔ   (h→∅)
500: the low vowel fronts by default
    ˈɑ.bʝɔ → ˈa.bʝɔ   (ˈɑ→ˈa)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˈa.bʝɔ → ˈab.ɟɔ   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈab.ɟɔ → ˈa.bd͡ʒɔ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈa.bd͡ʒɔ → ˈa.bd͡ʒə   (ɔ→ə)
600: schwa becomes non-syllabic
    ˈa.bd͡ʒə → ˈabd͡ʒə̯   (ə→ə̯)
600: non-syllabic schwa restores after a postalveolar affricate
    ˈabd͡ʒə̯ → ˈa.bd͡ʒə   (ə̯→ə)
600: a labial consonant becomes d before a voiced coronal stop
    ˈa.bd͡ʒə → ˈa.d̪d͡ʒə   (b→d̪)
750: a dental stop deletes before another coronal stop
    ˈa.d̪d͡ʒə → ˈa.d͡ʒə   (d̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈa.d͡ʒə → ˈa.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈa.ʒə → ˈaʒə̯   (ə→ə̯)
1400: a lengthens in the ending aʒə̯
    ˈaʒə̯ → ˈaːʒə̯   (ˈa→ˈaː)
1400: the final off-glide schwa is deleted elsewhere
    ˈaːʒə̯ → ˈaːʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈaːʒ → aːʒ   (ˈaː→aː)
1400: distinctive vowel length is lost entirely
    aːʒ → aʒ   (aː→a)
```

## ais

`ˈɑksem` → `ɛ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑ.ksem → ˈɑ.ksɛm   (e→ɛ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈɑ.ksɛm → ˈɑx.sɛm   (k→x)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑx.sɛm → ˈɑx.sɛ   (m→∅)
500: the low vowel fronts by default
    ˈɑx.sɛ → ˈax.sɛ   (ˈɑ→ˈa)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈax.sɛ → ˈaç.sɛ   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈaç.sɛ → ˈaç.sʲɛ   (s→sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaç.sʲɛ → ˈaç.sʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈaç.sʲə → ˈaçsʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈaçsʲə̯ → ˈaçsʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈaçsʲ → ˈaçjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈaçjs → ˈaçs   (j→∅)
750: ç merges into ʝ
    ˈaçs → ˈaʝs   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈaʝs → ˈajs   (ʝ→j)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈajs → ˈɛːs   (ˈaj→ˈɛː)
1400: final obstruents are lost
    ˈɛːs → ˈɛː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛː → ɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    ɛː → ɛ   (ɛː→ɛ)
```

## année

`ˌɑn̪n̪ˈɑːt̪ɑm` → `a.n̪e`

```
-100: the length feature is dropped now that quality carries the contrast
    ˌɑn̪ˈn̪ɑː.t̪ɑm → ˌɑn̪ˈn̪ɑ.t̪ɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɑn̪ˈn̪ɑ.t̪ɑm → ˌɑn̪ˈn̪ɑ.t̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑn̪ˈn̪ɑ.t̪ɑ → ˌɑn̪ˈn̪ɑː.t̪ɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌɑn̪ˈn̪ɑː.t̪ɑ → ˌan̪ˈn̪aː.t̪a   (ˌɑ→ˌa, ˈɑː→ˈaː, ɑ→a)
600: a voiceless consonant voices intervocalically
    ˌan̪ˈn̪aː.t̪a → ˌan̪ˈn̪aː.d̪a   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌan̪ˈn̪aː.d̪a → ˌan̪ˈn̪aː.ða   (d̪→ð)
600: long stressed vowels diphthongize
    ˌan̪ˈn̪aː.ða → ˌan̪ˈn̪ae̯.ða   (ˈaː→ˈae̯)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌan̪ˈn̪ae̯.ða → ˌan̪ˈn̪ae̯.ðə   (a→ə)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌan̪ˈn̪ae̯.ðə → ˌan̪ˈn̪eː.ðə   (ˈae̯→ˈeː)
750: an identical consonant geminate reduces to one (recurrence)
    ˌan̪ˈn̪eː.ðə → ˌaˈn̪eː.ðə   (n̪→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌaˈn̪eː.ðə → ˌãˈn̪eː.ðə   (ˌa→ˌã)
1000: vowel length resets to short
    ˌãˈn̪eː.ðə → ˌãˈn̪e.ðə   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌãˈn̪e.ðə → ˌãˈn̪e.ə   (ð→∅)
1200: schwa desyllabifies after another vowel
    ˌãˈn̪e.ə → ˌãˈn̪eə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˌãˈn̪eə̯ → ˌãˈn̪eː   (ˈeə̯→ˈeː)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˌãˈn̪eː → ˌaˈn̪eː   (ˌã→ˌa)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈn̪eː → a.n̪eː   (ˌa→a, ˈeː→eː)
1400: distinctive vowel length is lost entirely
    a.n̪eː → a.n̪e   (eː→e)
```

## ans

`ˈɑn̪n̪oːs` → `ɑ̃`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈɑn̪.n̪oːs → ˈɑn̪.n̪os   (oː→o)
500: the low vowel fronts by default
    ˈɑn̪.n̪os → ˈan̪.n̪os   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈan̪.n̪os → ˈan̪.n̪əs   (o→ə)
600: schwa becomes non-syllabic
    ˈan̪.n̪əs → ˈan̪n̪ə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈan̪n̪ə̯s → ˈan̪n̪s   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˈan̪n̪s → ˈan̪s   (n̪→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈan̪s → ˈãn̪s   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈãn̪s → ˈãːs   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈãːs → ˈɑ̃ːs   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈɑ̃ːs → ˈɑ̃ː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɑ̃ː → ɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ɑ̃ː → ɑ̃   (ɑ̃ː→ɑ̃)
```

## assez

`ˌɑd̪sˈɑt̪is` → `a.se`

```
-100: d totally assimilates to a following obstruent
    ˌɑˈd̪sɑ.t̪is → ˌɑsˈsɑ.t̪is   (d̪→s)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑsˈsɑ.t̪is → ˌɑsˈsɑ.t̪ɪs   (i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˌɑsˈsɑ.t̪ɪs → ˌɑsˈsɑ.t̪es   (ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɑsˈsɑ.t̪es → ˌɑsˈsɑː.t̪es   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌɑsˈsɑː.t̪es → ˌasˈsaː.t̪es   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌasˈsaː.t̪es → ˌasˈsaː.t̪əs   (e→ə)
600: schwa becomes non-syllabic
    ˌasˈsaː.t̪əs → ˌasˈsaːt̪ə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌasˈsaːt̪ə̯s → ˌasˈsaːt̪s   (ə̯→∅)
600: a dental fricative + s becomes the affricate ts word-finally
    ˌasˈsaːt̪s → ˌasˈsaːt͡s   (t̪s→t͡s)
600: long stressed vowels diphthongize
    ˌasˈsaːt͡s → ˌasˈsae̯t͡s   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌasˈsae̯t͡s → ˌasˈseːt͡s   (ˈae̯→ˈeː)
750: an identical consonant geminate reduces to one (recurrence)
    ˌasˈseːt͡s → ˌaˈseːt͡s   (s→∅)
1000: vowel length resets to short
    ˌaˈseːt͡s → ˌaˈset͡s   (ˈeː→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌaˈset͡s → ˌaˈses   (t͡s→s)
1400: final obstruents are lost
    ˌaˈses → ˌaˈse   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈse → a.se   (ˌa→a, ˈe→e)
```

## aulx

`ˈɑllioːs` → `o`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑl.li.oːs → ˈɑl.lɪ.oːs   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈɑl.lɪ.oːs → ˈɑl.ljoːs   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˈɑl.ljoːs → ˈɑl.ɫjoːs   (l→ɫ)
-100: yod strengthens before a vowel
    ˈɑl.ɫjoːs → ˈɑlɫ.ʝoːs   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈɑlɫ.ʝoːs → ˈɑlɫ.ʝos   (oː→o)
300: ll palatalizes to ʎ before yod
    ˈɑlɫ.ʝos → ˈɑ.ʎos   (lɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.ʎos → ˈɑː.ʎos   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑː.ʎos → ˈaː.ʎos   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaː.ʎos → ˈaː.ʎəs   (o→ə)
600: schwa becomes non-syllabic
    ˈaː.ʎəs → ˈaːʎə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈaːʎə̯s → ˈaːʎs   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈaːʎs → ˈaːʎsʲ   (s→sʲ)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈaːʎsʲ → ˈaʎsʲ   (ˈaː→ˈa)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈaʎsʲ → ˈaʎjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈaʎjs → ˈaʎs   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈaʎs → ˈaʎt͡sʲ   (s→t͡sʲ)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈaʎt͡sʲ → ˈaɫt͡sʲ   (ʎ→ɫ)
1000: back dark-l variants vocalize to w
    ˈaɫt͡sʲ → ˈawt͡sʲ   (ɫ→w)
1000: all affricates become sibilants (deaffrication)
    ˈawt͡sʲ → ˈawsʲ   (t͡sʲ→sʲ)
1200: aw becomes long oː
    ˈawsʲ → ˈoːsʲ   (ˈaw→ˈoː)
1200: the remaining anterior palatalized consonants depalatalize
    ˈoːsʲ → ˈoːs   (sʲ→s)
1400: final obstruents are lost
    ˈoːs → ˈoː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈoː → oː   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    oː → o   (oː→o)
```

## autre

`ˈɑlt̪erum` → `ɔt̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑl.t̪e.rum → ˈɑl.t̪ɛ.rʊm   (e→ɛ, u→ʊ)
-100: l darkens before a non-lateral consonant
    ˈɑl.t̪ɛ.rʊm → ˈɑɫ.t̪ɛ.rʊm   (l→ɫ)
-100: lax high vowels lower to tense mid vowels
    ˈɑɫ.t̪ɛ.rʊm → ˈɑɫ.t̪ɛ.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑɫ.t̪ɛ.rom → ˈɑɫ.t̪ɛ.ro   (m→∅)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈɑɫ.t̪ɛ.ro → ˈɑɫ.t̪ro   (ɛ→∅)
500: the low vowel fronts by default
    ˈɑɫ.t̪ro → ˈaɫ.t̪ro   (ˈɑ→ˈa)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈaɫ.t̪ro → ˈaɫ.t̪ʲro   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaɫ.t̪ʲro → ˈaɫ.t̪ʲrə   (o→ə)
600: schwa becomes non-syllabic
    ˈaɫ.t̪ʲrə → ˈaɫt̪ʲrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈaɫt̪ʲrə̯ → ˈaɫt̪ʲr   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈaɫt̪ʲr → ˈaɫ.t̪ʲrə   (∅→ə)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈaɫ.t̪ʲrə → ˈaɫ.t̪ʲrʲə   (r→rʲ)
600: palatalized r depalatalizes
    ˈaɫ.t̪ʲrʲə → ˈaɫ.t̪ʲrə   (rʲ→r)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈaɫ.t̪ʲrə → ˈaɫj.t̪rə   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈaɫj.t̪rə → ˈaɫ.t̪rə   (j→∅)
1000: back dark-l variants vocalize to w
    ˈaɫ.t̪rə → ˈaw.t̪rə   (ɫ→w)
1200: aw becomes long oː
    ˈaw.t̪rə → ˈoː.t̪rə   (ˈaw→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˈoː.t̪rə → ˈoːt̪rə̯   (ə→ə̯)
1400: back mid o opens before a consonant cluster
    ˈoːt̪rə̯ → ˈɔːt̪rə̯   (ˈoː→ˈɔː)
1400: the final off-glide schwa is deleted elsewhere
    ˈɔːt̪rə̯ → ˈɔːt̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈɔːt̪r → ˈɔːt̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈɔːt̪ʀ → ɔːt̪ʀ   (ˈɔː→ɔː)
1400: distinctive vowel length is lost entirely
    ɔːt̪ʀ → ɔt̪ʀ   (ɔː→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ɔt̪ʀ → ɔt̪ʁ   (ʀ→ʁ)
```

## baie

`bˈɑkɑm` → `bɛ`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɑ.kɑm → ˈbɑ.kɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈbɑ.kɑ → ˈbɑː.kɑ   (ˈɑ→ˈɑː)
500: k voices to g intervocalically
    ˈbɑː.kɑ → ˈbɑː.gɑ   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˈbɑː.gɑ → ˈbɑː.ɣɑ   (g→ɣ)
500: the low vowel fronts by default
    ˈbɑː.ɣɑ → ˈbaː.ɣa   (ˈɑː→ˈaː, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈbaː.ɣa → ˈbaː.ɣʲa   (ɣ→ɣʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈbaː.ɣʲa → ˈbaː.ʝa   (ɣʲ→ʝ)
600: ʝ weakens to j unconditionally
    ˈbaː.ʝa → ˈbaː.ja   (ʝ→j)
600: long stressed vowels diphthongize
    ˈbaː.ja → ˈbae̯.ja   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˈbae̯.ja → ˈba.ja   (e̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈba.ja → ˈba.jə   (a→ə)
1200: schwa desyllabifies after another vowel
    ˈba.jə → ˈbajə̯   (ə→ə̯)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈbajə̯ → ˈbɛːə̯   (ˈaj→ˈɛː)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈbɛːə̯ → ˈbɛː   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈbɛː → bɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    bɛː → bɛ   (ɛː→ɛ)
```

## bain

`bˈɑln̪eum` → `bɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbɑl.n̪e.um → ˈbɑl.n̪ɛ.ʊm   (e→ɛ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈbɑl.n̪ɛ.ʊm → ˈbɑl.n̪jʊm   (ɛ→j)
-100: l darkens before a non-lateral consonant
    ˈbɑl.n̪jʊm → ˈbɑɫ.n̪jʊm   (l→ɫ)
-100: yod strengthens before a vowel
    ˈbɑɫ.n̪jʊm → ˈbɑɫn̪.ʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈbɑɫn̪.ʝʊm → ˈbɑɫn̪.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɑɫn̪.ʝom → ˈbɑɫn̪.ʝo   (m→∅)
-100: a lateral is lost before a nasal + yod
    ˈbɑɫn̪.ʝo → ˈbɑn̪.ʝo   (ɫ→∅)
300: the coronal nasal palatalizes before yod
    ˈbɑn̪.ʝo → ˈbɑ.ɲo   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈbɑ.ɲo → ˈbɑː.ɲo   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈbɑː.ɲo → ˈbaː.ɲo   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbaː.ɲo → ˈbaː.ɲə   (o→ə)
600: schwa becomes non-syllabic
    ˈbaː.ɲə → ˈbaːɲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbaːɲə̯ → ˈbaːɲ   (ə̯→∅)
600: a vowel shortens before ɲ
    ˈbaːɲ → ˈbaɲ   (ˈaː→ˈa)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈbaɲ → ˈbãɲ   (ˈa→ˈã)
1000: word-final ɲ ejects a nasalized j after a tense vowel
    ˈbãɲ → ˈbãj̃ɲ   (∅→j̃)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈbãj̃ɲ → ˈbɛ̃j̃ɲ   (ˈã→ˈɛ̃)
1200: final ɲ becomes n
    ˈbɛ̃j̃ɲ → ˈbɛ̃j̃n̪   (ɲ→n̪)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈbɛ̃j̃n̪ → ˈbɛ̃n̪   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈbɛ̃n̪ → ˈbɛ̃ː   (ˈɛ̃n̪→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈbɛ̃ː → bɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    bɛ̃ː → bɛ̃   (ɛ̃ː→ɛ̃)
```

## bains

`bˈɑln̪eoːs` → `bɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbɑl.n̪e.oːs → ˈbɑl.n̪ɛ.oːs   (e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈbɑl.n̪ɛ.oːs → ˈbɑl.n̪joːs   (ɛ→j)
-100: l darkens before a non-lateral consonant
    ˈbɑl.n̪joːs → ˈbɑɫ.n̪joːs   (l→ɫ)
-100: yod strengthens before a vowel
    ˈbɑɫ.n̪joːs → ˈbɑɫn̪.ʝoːs   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈbɑɫn̪.ʝoːs → ˈbɑɫn̪.ʝos   (oː→o)
-100: a lateral is lost before a nasal + yod
    ˈbɑɫn̪.ʝos → ˈbɑn̪.ʝos   (ɫ→∅)
300: the coronal nasal palatalizes before yod
    ˈbɑn̪.ʝos → ˈbɑ.ɲos   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈbɑ.ɲos → ˈbɑː.ɲos   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈbɑː.ɲos → ˈbaː.ɲos   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbaː.ɲos → ˈbaː.ɲəs   (o→ə)
600: schwa becomes non-syllabic
    ˈbaː.ɲəs → ˈbaːɲə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbaːɲə̯s → ˈbaːɲs   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈbaːɲs → ˈbaːɲsʲ   (s→sʲ)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈbaːɲsʲ → ˈbaɲsʲ   (ˈaː→ˈa)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈbaɲsʲ → ˈbaɲjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈbaɲjs → ˈbaɲs   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈbaɲs → ˈbaɲt͡sʲ   (s→t͡sʲ)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˈbaɲt͡sʲ → ˈbaj̃n̪t͡sʲ   (ɲ→j̃n̪)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈbaj̃n̪t͡sʲ → ˈbaj̃t͡sʲ   (n̪→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈbaj̃t͡sʲ → ˈbãj̃t͡sʲ   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈbãj̃t͡sʲ → ˈbɛ̃j̃t͡sʲ   (ˈã→ˈɛ̃)
1000: all affricates become sibilants (deaffrication)
    ˈbɛ̃j̃t͡sʲ → ˈbɛ̃j̃sʲ   (t͡sʲ→sʲ)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈbɛ̃j̃sʲ → ˈbɛ̃sʲ   (j̃→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˈbɛ̃sʲ → ˈbɛ̃s   (sʲ→s)
1400: final obstruents are lost
    ˈbɛ̃s → ˈbɛ̃   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈbɛ̃ → bɛ̃   (ˈɛ̃→ɛ̃)
```

## barbe

`bˈɑrbɑm` → `baʁb`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɑr.bɑm → ˈbɑr.bɑ   (m→∅)
500: the low vowel fronts by default
    ˈbɑr.bɑ → ˈbar.ba   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈbar.ba → ˈbar.bə   (a→ə)
1400: final ə becomes a non-syllabic off-glide
    ˈbar.bə → ˈbarbə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈbarbə̯ → ˈbaɹbə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈbaɹbə̯ → ˈbaɹb   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈbaɹb → ˈbarb   (ɹ→r)
1400: r becomes uvular ʀ
    ˈbarb → ˈbaʀb   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈbaʀb → baʀb   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    baʀb → baʁb   (ʀ→ʁ)
```

## bas

`bˈɑssum` → `bɑ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbɑs.sum → ˈbɑs.sʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈbɑs.sʊm → ˈbɑs.som   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɑs.som → ˈbɑs.so   (m→∅)
500: the low vowel fronts by default
    ˈbɑs.so → ˈbas.so   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbas.so → ˈbas.sə   (o→ə)
600: schwa becomes non-syllabic
    ˈbas.sə → ˈbassə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbassə̯ → ˈbass   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˈbass → ˈbas   (s→∅)
1000: a primary-stressed vowel lengthens before word-final s
    ˈbas → ˈbaːs   (ˈa→ˈaː)
1400: long a becomes back ɑː
    ˈbaːs → ˈbɑːs   (ˈaː→ˈɑː)
1400: final obstruents are lost
    ˈbɑːs → ˈbɑː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈbɑː → bɑː   (ˈɑː→ɑː)
1400: distinctive vowel length is lost entirely
    bɑː → bɑ   (ɑː→ɑ)
```

## beauté

`bˌellit̪ˈɑːt̪em` → `bo.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌbel.liˈt̪ɑː.t̪em → ˌbɛl.lɪˈt̪ɑː.t̪ɛm   (ˌe→ˌɛ, i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌbɛl.lɪˈt̪ɑː.t̪ɛm → ˌbɛl.lɪˈt̪ɑ.t̪ɛm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌbɛl.lɪˈt̪ɑ.t̪ɛm → ˌbɛl.leˈt̪ɑ.t̪ɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌbɛl.leˈt̪ɑ.t̪ɛm → ˌbɛl.leˈt̪ɑ.t̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌbɛl.leˈt̪ɑ.t̪ɛ → ˌbɛl.leˈt̪ɑː.t̪ɛ   (ˈɑ→ˈɑː)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌbɛl.leˈt̪ɑː.t̪ɛ → ˌbɛllˈt̪ɑː.t̪ɛ   (e→∅)
500: the low vowel fronts by default
    ˌbɛllˈt̪ɑː.t̪ɛ → ˌbɛllˈt̪aː.t̪ɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌbɛllˈt̪aː.t̪ɛ → ˌbɛllˈt̪aː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌbɛllˈt̪aː.t̪ə → ˌbɛllˈt̪aːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌbɛllˈt̪aːt̪ə̯ → ˌbɛllˈt̪aːt̪   (ə̯→∅)
600: an identical consonant geminate reduces to one, before an obstruent or nasal
    ˌbɛllˈt̪aːt̪ → ˌbɛlˈt̪aːt̪   (l→∅)
600: long stressed vowels diphthongize
    ˌbɛlˈt̪aːt̪ → ˌbɛlˈt̪ae̯t̪   (ˈaː→ˈae̯)
600: secondary-stressed ɛ/ɔ raise before a lateral + consonant
    ˌbɛlˈt̪ae̯t̪ → ˌbɨlˈt̪ae̯t̪   (ˌɛ→ˌɨ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌbɨlˈt̪ae̯t̪ → ˌbɛlˈt̪ae̯t̪   (ˌɨ→ˌɛ)
750: a word-final stop re-opens to a fricative after a vowel
    ˌbɛlˈt̪ae̯t̪ → ˌbɛlˈt̪ae̯θ   (t̪→θ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌbɛlˈt̪ae̯θ → ˌbɛlˈt̪eːθ   (ˈae̯→ˈeː)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌbɛlˈt̪eːθ → ˌbɛɫˈt̪eːθ   (l→ɫ)
1000: vowel length resets to short
    ˌbɛɫˈt̪eːθ → ˌbɛɫˈt̪eθ   (ˈeː→ˈe)
1000: back dark-l variants vocalize to w
    ˌbɛɫˈt̪eθ → ˌbɛwˈt̪eθ   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌbɛwˈt̪eθ → ˌbɛa̯wˈt̪eθ   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌbɛa̯wˈt̪eθ → ˌbe̯awˈt̪eθ   (ˌɛ→e̯, a̯→ˌa)
1000: the interdental fricatives (plain and palatalized) efface
    ˌbe̯awˈt̪eθ → ˌbe̯awˈt̪e   (θ→∅)
1200: aw becomes long oː
    ˌbe̯awˈt̪e → ˌbe̯oːˈt̪e   (ˌaw→ˌoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌbe̯oːˈt̪e → ˌbə̯oːˈt̪e   (e̯→ə̯)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌbə̯oːˈt̪e → ˌboːˈt̪e   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌboːˈt̪e → boː.t̪e   (ˌoː→oː, ˈe→e)
1400: distinctive vowel length is lost entirely
    boː.t̪e → bo.t̪e   (oː→o)
```

## beaux

`bˈellus` → `bo`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbel.lus → ˈbɛl.lʊs   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈbɛl.lʊs → ˈbɛl.los   (ʊ→o)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbɛl.los → ˈbɛl.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˈbɛl.ləs → ˈbɛllə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbɛllə̯s → ˈbɛlls   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˈbɛlls → ˈbɛls   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈbɛls → ˈbɛɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˈbɛɫs → ˈbɛws   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˈbɛws → ˈbɛa̯ws   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈbɛa̯ws → ˈbe̯aws   (ˈɛ→e̯, a̯→ˈa)
1200: aw becomes long oː
    ˈbe̯aws → ˈbe̯oːs   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˈbe̯oːs → ˈbə̯oːs   (e̯→ə̯)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈbə̯oːs → ˈboːs   (ə̯→∅)
1400: final obstruents are lost
    ˈboːs → ˈboː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈboː → boː   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    boː → bo   (oː→o)
```

## bien

`bˈen̪e` → `bjɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbe.n̪e → ˈbɛ.n̪ɛ   (ˈe→ˈɛ, e→ɛ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈbɛ.n̪ɛ → ˈbɛː.n̪ɛ   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈbɛː.n̪ɛ → ˈbie̯.n̪ɛ   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbie̯.n̪ɛ → ˈbie̯.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈbie̯.n̪ə → ˈbie̯n̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbie̯n̪ə̯ → ˈbie̯n̪   (ə̯→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈbie̯n̪ → ˈbjen̪   (ˈi→j, e̯→ˈe)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈbjen̪ → ˈbjẽn̪   (ˈe→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈbjẽn̪ → ˈbjẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈbjẽː → ˈbjɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈbjɛ̃ː → bjɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    bjɛ̃ː → bjɛ̃   (ɛ̃ː→ɛ̃)
```

## bouillant

`bˌulliˈen̪t̪em` → `bu.jɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌbul.liˈen̪.t̪em → ˌbʊl.lɪˈɛn̪.t̪ɛm   (ˌu→ˌʊ, i→ɪ, ˈe→ˈɛ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌbʊl.lɪˈɛn̪.t̪ɛm → ˌbʊlˈljɛn̪.t̪ɛm   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˌbʊlˈljɛn̪.t̪ɛm → ˌbʊlˈɫjɛn̪.t̪ɛm   (l→ɫ)
-100: yod strengthens before a vowel
    ˌbʊlˈɫjɛn̪.t̪ɛm → ˌbʊlɫˈʝɛn̪.t̪ɛm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˌbʊlɫˈʝɛn̪.t̪ɛm → ˌbolɫˈʝɛn̪.t̪ɛm   (ˌʊ→ˌo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌbolɫˈʝɛn̪.t̪ɛm → ˌbolɫˈʝɛn̪.t̪ɛ   (m→∅)
300: ll palatalizes to ʎ before yod
    ˌbolɫˈʝɛn̪.t̪ɛ → ˌboˈʎɛn̪.t̪ɛ   (lɫʝ→ʎ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌboˈʎɛn̪.t̪ɛ → ˌboˈʎɛn̪.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌboˈʎɛn̪.t̪ə → ˌboˈʎɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌboˈʎɛn̪t̪ə̯ → ˌboˈʎɛn̪t̪   (ə̯→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌboˈʎɛn̪t̪ → ˌboˈʎɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌboˈʎɛ̃n̪t̪ → ˌbuˈʎɛ̃n̪t̪   (ˌo→ˌu)
1000: nasalized front mid vowels become nasalized a
    ˌbuˈʎɛ̃n̪t̪ → ˌbuˈʎãn̪t̪   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌbuˈʎãn̪t̪ → ˌbuˈʎãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˌbuˈʎãːt̪ → ˌbuˈʎɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˌbuˈʎɑ̃ːt̪ → ˌbuˈʎɑ̃ː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌbuˈʎɑ̃ː → bu.ʎɑ̃ː   (ˌu→u, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    bu.ʎɑ̃ː → bu.ʎɑ̃   (ɑ̃ː→ɑ̃)
1400: ʎ becomes j
    bu.ʎɑ̃ → bu.jɑ̃   (ʎ→j)
```

## bras

`brˈɑkkʰium` → `bʁa`

```
-100: aspiration lost on Greek loanwords (2nd century)
    ˈbrɑk.kʰi.um → ˈbrɑk.ki.um   (kʰ→k)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbrɑk.ki.um → ˈbrɑk.kɪ.ʊm   (i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈbrɑk.kɪ.ʊm → ˈbrɑk.kjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈbrɑk.kjʊm → ˈbrɑk.kʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈbrɑk.kʝʊm → ˈbrɑk.kʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbrɑk.kʝom → ˈbrɑk.kʝo   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈbrɑk.kʝo → ˈbrɑk.kʲʝo   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈbrɑk.kʲʝo → ˈbrɑk.cʝo   (kʲ→c)
-100: k assimilates to a following palatal c
    ˈbrɑk.cʝo → ˈbrɑc.cʝo   (k→c)
300: yod absorbed into a preceding palatalized consonant
    ˈbrɑc.cʝo → ˈbrɑc.co   (ʝ→∅)
500: geminate palatal stop cc becomes t + tsʲ
    ˈbrɑc.co → ˈbrɑ.t̪t͡sʲo   (c→t̪, c→t͡sʲ)
500: the low vowel fronts by default
    ˈbrɑ.t̪t͡sʲo → ˈbra.t̪t͡sʲo   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbra.t̪t͡sʲo → ˈbra.t̪t͡sʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈbra.t̪t͡sʲə → ˈbrat̪t͡sʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbrat̪t͡sʲə̯ → ˈbrat̪t͡sʲ   (ə̯→∅)
750: a dental stop deletes before another coronal stop
    ˈbrat̪t͡sʲ → ˈbrat͡sʲ   (t̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈbrat͡sʲ → ˈbrasʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈbrasʲ → ˈbras   (sʲ→s)
1400: final obstruents are lost
    ˈbras → ˈbra   (s→∅)
1400: r becomes uvular ʀ
    ˈbra → ˈbʀa   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈbʀa → bʀa   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    bʀa → bʁa   (ʀ→ʁ)
```

## bâtir

`bˌɑst̪ˈiːre` → `bɑ.t̪iʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌbɑsˈt̪iː.re → ˌbɑsˈt̪iː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌbɑsˈt̪iː.rɛ → ˌbɑsˈt̪i.rɛ   (ˈiː→ˈi)
300: a stressed vowel lengthens before a single consonant + glide
    ˌbɑsˈt̪i.rɛ → ˌbɑsˈt̪iː.rɛ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˌbɑsˈt̪iː.rɛ → ˌbasˈt̪iː.rɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌbasˈt̪iː.rɛ → ˌbasˈt̪iː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌbasˈt̪iː.rə → ˌbasˈt̪iːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌbasˈt̪iːrə̯ → ˌbasˈt̪iːr   (ə̯→∅)
750: vowel length resets to short
    ˌbasˈt̪iːr → ˌbasˈt̪ir   (ˈiː→ˈi)
1000: s becomes x after a vowel, before any consonant
    ˌbasˈt̪ir → ˌbaxˈt̪ir   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌbaxˈt̪ir → ˌbaːˈt̪ir   (ˌax→ˌaː)
1400: long a becomes back ɑː
    ˌbaːˈt̪ir → ˌbɑːˈt̪ir   (ˌaː→ˌɑː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌbɑːˈt̪ir → ˌbɑːˈt̪iɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌbɑːˈt̪iɹ → ˌbɑːˈt̪ir   (ɹ→r)
1400: r becomes uvular ʀ
    ˌbɑːˈt̪ir → ˌbɑːˈt̪iʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌbɑːˈt̪iʀ → bɑː.t̪iʀ   (ˌɑː→ɑː, ˈi→i)
1400: distinctive vowel length is lost entirely
    bɑː.t̪iʀ → bɑ.t̪iʀ   (ɑː→ɑ)
1400: the uvular trill ʀ becomes a fricative ʁ
    bɑ.t̪iʀ → bɑ.t̪iʁ   (ʀ→ʁ)
```

## bœuf

`bˈowem` → `bœf`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈbo.wem → ˈbo.ɣʷem   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbo.ɣʷem → ˈbɔ.ɣʷɛm   (ˈo→ˈɔ, e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈbɔ.ɣʷɛm → ˈbɔ.βʷɛm   (ɣʷ→βʷ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɔ.βʷɛm → ˈbɔ.βʷɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈbɔ.βʷɛ → ˈbɔː.βʷɛ   (ˈɔ→ˈɔː)
500: labialized bilabial fricatives delabialize
    ˈbɔː.βʷɛ → ˈbɔː.βɛ   (βʷ→β)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈbɔː.βɛ → ˈbuo̯.βɛ   (ˈɔː→ˈuo̯)
500: a high tense round non-nasal vowel centralizes
    ˈbuo̯.βɛ → ˈbʉo̯.βɛ   (ˈu→ˈʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbʉo̯.βɛ → ˈbʉo̯.βə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈbʉo̯.βə → ˈbʉo̯βə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbʉo̯βə̯ → ˈbʉo̯β   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˈbʉo̯β → ˈbʉo̯v   (β→v)
750: all final obstruents devoice
    ˈbʉo̯v → ˈbʉo̯f   (v→f)
1000: high round back vowels front (completion of u-fronting)
    ˈbʉo̯f → ˈbyo̯f   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈbyo̯f → ˈbye̯f   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈbye̯f → ˈbøf   (ˈye̯→ˈø)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈbøf → ˈbøfə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈbøfə̯ → ˈbøf   (ə̯→∅)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈbøf → ˈbœf   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˈbœf → bœf   (ˈœ→œ)
```

## bœufs

`bˈowes` → `bø`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈbo.wes → ˈbo.ɣʷes   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbo.ɣʷes → ˈbɔ.ɣʷɛs   (ˈo→ˈɔ, e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈbɔ.ɣʷɛs → ˈbɔ.βʷɛs   (ɣʷ→βʷ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈbɔ.βʷɛs → ˈbɔː.βʷɛs   (ˈɔ→ˈɔː)
500: labialized bilabial fricatives delabialize
    ˈbɔː.βʷɛs → ˈbɔː.βɛs   (βʷ→β)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈbɔː.βɛs → ˈbuo̯.βɛs   (ˈɔː→ˈuo̯)
500: a high tense round non-nasal vowel centralizes
    ˈbuo̯.βɛs → ˈbʉo̯.βɛs   (ˈu→ˈʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈbʉo̯.βɛs → ˈbʉo̯.βəs   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈbʉo̯.βəs → ˈbʉo̯βə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈbʉo̯βə̯s → ˈbʉo̯βs   (ə̯→∅)
600: a labial consonant becomes s before s
    ˈbʉo̯βs → ˈbʉo̯ss   (β→s)
750: an identical consonant geminate reduces to one (recurrence)
    ˈbʉo̯ss → ˈbʉo̯s   (s→∅)
1000: high round back vowels front (completion of u-fronting)
    ˈbʉo̯s → ˈbyo̯s   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈbyo̯s → ˈbye̯s   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈbye̯s → ˈbøs   (ˈye̯→ˈø)
1000: a primary-stressed vowel lengthens before word-final s
    ˈbøs → ˈbøːs   (ˈø→ˈøː)
1400: final obstruents are lost
    ˈbøːs → ˈbøː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈbøː → bøː   (ˈøː→øː)
1400: distinctive vowel length is lost entirely
    bøː → bø   (øː→ø)
```

## cage

`kˈɑweɑm` → `ʃi`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈkɑ.we.ɑm → ˈkɑ.ɣʷe.ɑm   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑ.ɣʷe.ɑm → ˈkɑ.ɣʷɛ.ɑm   (e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈkɑ.ɣʷɛ.ɑm → ˈkɑ.ɣʷjɑm   (ɛ→j)
-100: yod strengthens before a vowel
    ˈkɑ.ɣʷjɑm → ˈkɑɣʷ.ʝɑm   (j→ʝ)
-100: the rounded glide is lost before the strengthened yod
    ˈkɑɣʷ.ʝɑm → ˈkɑ.ʝɑm   (ɣʷ→∅)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑ.ʝɑm → ˈkɑ.ʝɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkɑ.ʝɑ → ˈkɑː.ʝɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈkɑː.ʝɑ → ˈkaː.ʝa   (ˈɑː→ˈaː, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈkaː.ʝa → ˈkʲaː.ʝa   (k→kʲ)
500: long stressed aː becomes ɛː word-initially after a front consonant
    ˈkʲaː.ʝa → ˈkʲɛː.ʝa   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˈkʲɛː.ʝa → ˈkʲie̯.ʝa   (ˈɛː→ˈie̯)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲie̯.ʝa → ˈcie̯.ʝa   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcie̯.ʝa → ˈt͡ʃie̯.ʝa   (c→t͡ʃ)
600: ʝ weakens to j unconditionally
    ˈt͡ʃie̯.ʝa → ˈt͡ʃie̯.ja   (ʝ→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡ʃie̯.ja → ˈt͡ʃie̯.jə   (a→ə)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈt͡ʃie̯.jə → ˈt͡ʃi.jə   (e̯→∅)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃi.jə → ˈʃi.jə   (t͡ʃ→ʃ)
1200: schwa desyllabifies after another vowel
    ˈʃi.jə → ˈʃijə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃijə̯ → ˈʃij   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃij → ʃij   (ˈi→i)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    ʃij → ʃi   (j→∅)
```

## cent

`kˈen̪t̪um` → `sɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈken̪.t̪um → ˈkɛn̪.t̪ʊm   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkɛn̪.t̪ʊm → ˈkɛn̪.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɛn̪.t̪om → ˈkɛn̪.t̪o   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈkɛn̪.t̪o → ˈkʲɛn̪.t̪o   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkʲɛn̪.t̪o → ˈcɛn̪.t̪o   (kʲ→c)
500: a palatal stop affricates
    ˈcɛn̪.t̪o → ˈt͡sʲɛn̪.t̪o   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡sʲɛn̪.t̪o → ˈt͡sʲɛn̪.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡sʲɛn̪.t̪ə → ˈt͡sʲɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡sʲɛn̪t̪ə̯ → ˈt͡sʲɛn̪t̪   (ə̯→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈt͡sʲɛn̪t̪ → ˈt͡sʲɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈt͡sʲɛ̃n̪t̪ → ˈt͡sʲãn̪t̪   (ˈɛ̃→ˈã)
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲãn̪t̪ → ˈsʲãn̪t̪   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲãn̪t̪ → ˈsãn̪t̪   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈsãn̪t̪ → ˈsãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈsãːt̪ → ˈsɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈsɑ̃ːt̪ → ˈsɑ̃ː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɑ̃ː → sɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    sɑ̃ː → sɑ̃   (ɑ̃ː→ɑ̃)
```

## cercle

`kˈirkulum` → `sɛʁkl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkir.ku.lum → ˈkɪr.kʊ.lʊm   (ˈi→ˈɪ, u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈkɪr.kʊ.lʊm → ˈkɪr.klʊm   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈkɪr.klʊm → ˈker.klom   (ˈɪ→ˈe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈker.klom → ˈker.klo   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈker.klo → ˈkʲer.klo   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkʲer.klo → ˈcer.klo   (kʲ→c)
500: a palatal stop affricates
    ˈcer.klo → ˈt͡sʲer.klo   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡sʲer.klo → ˈt͡sʲer.klə   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡sʲer.klə → ˈt͡sʲerklə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈt͡sʲerklə̯ → ˈt͡sʲer.klə   (ə̯→ə)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˈt͡sʲer.klə → ˈt͡sʲɛr.klə   (ˈe→ˈɛ)
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲɛr.klə → ˈsʲɛr.klə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲɛr.klə → ˈsɛr.klə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈsɛr.klə → ˈsɛrklə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsɛrklə̯ → ˈsɛɹklə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈsɛɹklə̯ → ˈsɛɹkl   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsɛɹkl → ˈsɛrkl   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsɛrkl → ˈsɛʀkl   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛʀkl → sɛʀkl   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɛʀkl → sɛʁkl   (ʀ→ʁ)
```

## chaloir

`kˌɑlˈeːre` → `ʃa.lwaʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkɑˈleː.re → ˌkɑˈleː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkɑˈleː.rɛ → ˌkɑˈle.rɛ   (ˈeː→ˈe)
300: a stressed vowel lengthens before a single consonant + glide
    ˌkɑˈle.rɛ → ˌkɑˈleː.rɛ   (ˈe→ˈeː)
500: the low vowel fronts by default
    ˌkɑˈleː.rɛ → ˌkaˈleː.rɛ   (ˌɑ→ˌa)
500: the high back consonant w fronts before a front vowel
    ˌkaˈleː.rɛ → ˌkʲaˈleː.rɛ   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌkʲaˈleː.rɛ → ˌcaˈleː.rɛ   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˌcaˈleː.rɛ → ˌt͡ʃaˈleː.rɛ   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt͡ʃaˈleː.rɛ → ˌt͡ʃaˈleː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt͡ʃaˈleː.rə → ˌt͡ʃaˈleːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt͡ʃaˈleːrə̯ → ˌt͡ʃaˈleːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌt͡ʃaˈleːr → ˌt͡ʃaˈlejr   (ˈeː→ˈej)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌt͡ʃaˈlejr → ˌt͡ʃaˈlojr   (ˈe→ˈo)
1000: j lowers to ɛ̯ before r, in a back round diphthong
    ˌt͡ʃaˈlojr → ˌt͡ʃaˈloɛ̯r   (j→ɛ̯)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌt͡ʃaˈloɛ̯r → ˌt͡ʃaˈluɛ̯r   (ˈo→ˈu)
1000: all affricates become sibilants (deaffrication)
    ˌt͡ʃaˈluɛ̯r → ˌʃaˈluɛ̯r   (t͡ʃ→ʃ)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌʃaˈluɛ̯r → ˌʃaˈlwɛr   (ˈu→w, ɛ̯→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌʃaˈlwɛr → ˌʃaˈlwɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌʃaˈlwɛɹ → ˌʃaˈlwɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌʃaˈlwɛr → ˌʃaˈlwɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʃaˈlwɛʀ → ʃa.lwɛʀ   (ˌa→a, ˈɛ→ɛ)
1400: wɛ becomes wa
    ʃa.lwɛʀ → ʃa.lwaʀ   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃa.lwaʀ → ʃa.lwaʁ   (ʀ→ʁ)
```

## chambre

`kˈɑmerɑm` → `ʃɑ̃bʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑ.me.rɑm → ˈkɑ.mɛ.rɑm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑ.mɛ.rɑm → ˈkɑ.mɛ.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkɑ.mɛ.rɑ → ˈkɑː.mɛ.rɑ   (ˈɑ→ˈɑː)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈkɑː.mɛ.rɑ → ˈkɑː.mrɑ   (ɛ→∅)
500: b epenthesized between m and a coronal non-nasal sonorant glide
    ˈkɑː.mrɑ → ˈkɑːm.brɑ   (∅→b)
500: a vowel shortens before a consonant cluster
    ˈkɑːm.brɑ → ˈkɑm.brɑ   (ˈɑː→ˈɑ)
500: the low vowel fronts by default
    ˈkɑm.brɑ → ˈkam.bra   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈkam.bra → ˈkʲam.bra   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲam.bra → ˈcam.bra   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcam.bra → ˈt͡ʃam.bra   (c→t͡ʃ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡ʃam.bra → ˈt͡ʃam.brə   (a→ə)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈt͡ʃam.brə → ˈt͡ʃãm.brə   (ˈa→ˈã)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃãm.brə → ˈʃãm.brə   (t͡ʃ→ʃ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈʃãm.brə → ˈʃãː.brə   (ˈãm→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈʃãː.brə → ˈʃãːbrə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈʃãːbrə̯ → ˈʃɑ̃ːbrə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃɑ̃ːbrə̯ → ˈʃɑ̃ːbr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈʃɑ̃ːbr → ˈʃɑ̃ːbʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃɑ̃ːbʀ → ʃɑ̃ːbʀ   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ʃɑ̃ːbʀ → ʃɑ̃bʀ   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃɑ̃bʀ → ʃɑ̃bʁ   (ʀ→ʁ)
```

## champ

`kˈɑmpum` → `ʃɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑm.pum → ˈkɑm.pʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkɑm.pʊm → ˈkɑm.pom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑm.pom → ˈkɑm.po   (m→∅)
500: the low vowel fronts by default
    ˈkɑm.po → ˈkam.po   (ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˈkam.po → ˈkʲam.po   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲam.po → ˈcam.po   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcam.po → ˈt͡ʃam.po   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃam.po → ˈt͡ʃam.pə   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃam.pə → ˈt͡ʃampə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃampə̯ → ˈt͡ʃamp   (ə̯→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈt͡ʃamp → ˈt͡ʃãmp   (ˈa→ˈã)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃãmp → ˈʃãmp   (t͡ʃ→ʃ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈʃãmp → ˈʃãːp   (ˈãm→ˈãː)
1400: long a becomes back ɑː
    ˈʃãːp → ˈʃɑ̃ːp   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈʃɑ̃ːp → ˈʃɑ̃ː   (p→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃɑ̃ː → ʃɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ʃɑ̃ː → ʃɑ̃   (ɑ̃ː→ɑ̃)
```

## char

`kˈɑrrum` → `ʃaʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑr.rum → ˈkɑr.rʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkɑr.rʊm → ˈkɑr.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑr.rom → ˈkɑr.ro   (m→∅)
500: the low vowel fronts by default
    ˈkɑr.ro → ˈkar.ro   (ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˈkar.ro → ˈkʲar.ro   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲar.ro → ˈcar.ro   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcar.ro → ˈt͡ʃar.ro   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃar.ro → ˈt͡ʃar.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃar.rə → ˈt͡ʃarrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃarrə̯ → ˈt͡ʃarr   (ə̯→∅)
750: a word-final rr degeminates
    ˈt͡ʃarr → ˈt͡ʃar   (r→∅)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃar → ˈʃar   (t͡ʃ→ʃ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈʃar → ˈʃaɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈʃaɹ → ˈʃar   (ɹ→r)
1400: r becomes uvular ʀ
    ˈʃar → ˈʃaʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃaʀ → ʃaʀ   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃaʀ → ʃaʁ   (ʀ→ʁ)
```

## chef

`kˈɑpum` → `ʃɛf`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑ.pum → ˈkɑ.pʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkɑ.pʊm → ˈkɑ.pom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑ.pom → ˈkɑ.po   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkɑ.po → ˈkɑː.po   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈkɑː.po → ˈkaː.po   (ˈɑː→ˈaː)
500: the high back consonant w fronts before a front vowel
    ˈkaː.po → ˈkʲaː.po   (k→kʲ)
500: long stressed aː becomes ɛː word-initially after a front consonant
    ˈkʲaː.po → ˈkʲɛː.po   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˈkʲɛː.po → ˈkʲie̯.po   (ˈɛː→ˈie̯)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲie̯.po → ˈcie̯.po   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcie̯.po → ˈt͡ʃie̯.po   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃie̯.po → ˈt͡ʃie̯.pə   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃie̯.pə → ˈt͡ʃie̯pə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃie̯pə̯ → ˈt͡ʃie̯p   (ə̯→∅)
750: a word-final stop re-opens to a fricative after a vowel
    ˈt͡ʃie̯p → ˈt͡ʃie̯ɸ   (p→ɸ)
750: the voiceless bilabial fricative becomes labiodental f
    ˈt͡ʃie̯ɸ → ˈt͡ʃie̯f   (ɸ→f)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt͡ʃie̯f → ˈt͡ʃjef   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃjef → ˈʃjef   (t͡ʃ→ʃ)
1200: je becomes e after a palatal consonant
    ˈʃjef → ˈʃef   (j→∅)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈʃef → ˈʃɛf   (ˈe→ˈɛ)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈʃɛf → ˈʃɛfə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃɛfə̯ → ˈʃɛf   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃɛf → ʃɛf   (ˈɛ→ɛ)
```

## cher

`kˈɑːrum` → `ʃɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑː.rum → ˈkɑː.rʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈkɑː.rʊm → ˈkɑ.rʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˈkɑ.rʊm → ˈkɑ.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑ.rom → ˈkɑ.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkɑ.ro → ˈkɑː.ro   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈkɑː.ro → ˈkaː.ro   (ˈɑː→ˈaː)
500: the high back consonant w fronts before a front vowel
    ˈkaː.ro → ˈkʲaː.ro   (k→kʲ)
500: long stressed aː becomes ɛː word-initially after a front consonant
    ˈkʲaː.ro → ˈkʲɛː.ro   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˈkʲɛː.ro → ˈkʲie̯.ro   (ˈɛː→ˈie̯)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲie̯.ro → ˈcie̯.ro   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcie̯.ro → ˈt͡ʃie̯.ro   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃie̯.ro → ˈt͡ʃie̯.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃie̯.rə → ˈt͡ʃie̯rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃie̯rə̯ → ˈt͡ʃie̯r   (ə̯→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt͡ʃie̯r → ˈt͡ʃjer   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃjer → ˈʃjer   (t͡ʃ→ʃ)
1200: je becomes e after a palatal consonant
    ˈʃjer → ˈʃer   (j→∅)
1400: e/ø lax before an r that closes the syllable
    ˈʃer → ˈʃɛr   (ˈe→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈʃɛr → ˈʃɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈʃɛɹ → ˈʃɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈʃɛr → ˈʃɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃɛʀ → ʃɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃɛʀ → ʃɛʁ   (ʀ→ʁ)
```

## cheval

`kˌɑbˈɑllum` → `ʃə.val`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkɑˈbɑl.lum → ˌkɑˈbɑl.lʊm   (u→ʊ)
-100: b lenites to β intervocalically / before a sonorant
    ˌkɑˈbɑl.lʊm → ˌkɑˈβɑl.lʊm   (b→β)
-100: lax high vowels lower to tense mid vowels
    ˌkɑˈβɑl.lʊm → ˌkɑˈβɑl.lom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkɑˈβɑl.lom → ˌkɑˈβɑl.lo   (m→∅)
500: the low vowel fronts by default
    ˌkɑˈβɑl.lo → ˌkaˈβal.lo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˌkaˈβal.lo → ˌkʲaˈβal.lo   (k→kʲ)
500: secondary-stressed a becomes ɛ after a front consonant, before a non-coronal non-consonantal segment
    ˌkʲaˈβal.lo → ˌkʲɛˈβal.lo   (ˌa→ˌɛ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌkʲɛˈβal.lo → ˌcɛˈβal.lo   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˌcɛˈβal.lo → ˌt͡ʃɛˈβal.lo   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt͡ʃɛˈβal.lo → ˌt͡ʃɛˈβal.lə   (o→ə)
600: schwa becomes non-syllabic
    ˌt͡ʃɛˈβal.lə → ˌt͡ʃɛˈβallə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt͡ʃɛˈβallə̯ → ˌt͡ʃɛˈβall   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌt͡ʃɛˈβall → ˌt͡ʃeˈβall   (ˌɛ→ˌe)
600: the remaining bilabial fricative becomes v
    ˌt͡ʃeˈβall → ˌt͡ʃeˈvall   (β→v)
750: an identical consonant geminate reduces to one (recurrence)
    ˌt͡ʃeˈvall → ˌt͡ʃeˈval   (l→∅)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌt͡ʃeˈval → ˌt͡ʃəˈval   (ˌe→ˌə)
1000: all affricates become sibilants (deaffrication)
    ˌt͡ʃəˈval → ˌʃəˈval   (t͡ʃ→ʃ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʃəˈval → ʃə.val   (ˌə→ə, ˈa→a)
```

## chien

`kˈɑn̪em` → `ʃjɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkɑ.n̪em → ˈkɑ.n̪ɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑ.n̪ɛm → ˈkɑ.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkɑ.n̪ɛ → ˈkɑː.n̪ɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈkɑː.n̪ɛ → ˈkaː.n̪ɛ   (ˈɑː→ˈaː)
500: the high back consonant w fronts before a front vowel
    ˈkaː.n̪ɛ → ˈkʲaː.n̪ɛ   (k→kʲ)
500: long stressed aː becomes ɛː word-initially after a front consonant
    ˈkʲaː.n̪ɛ → ˈkʲɛː.n̪ɛ   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˈkʲɛː.n̪ɛ → ˈkʲie̯.n̪ɛ   (ˈɛː→ˈie̯)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲie̯.n̪ɛ → ˈcie̯.n̪ɛ   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcie̯.n̪ɛ → ˈt͡ʃie̯.n̪ɛ   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃie̯.n̪ɛ → ˈt͡ʃie̯.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃie̯.n̪ə → ˈt͡ʃie̯n̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃie̯n̪ə̯ → ˈt͡ʃie̯n̪   (ə̯→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt͡ʃie̯n̪ → ˈt͡ʃjen̪   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃjen̪ → ˈʃjen̪   (t͡ʃ→ʃ)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈʃjen̪ → ˈʃjẽn̪   (ˈe→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈʃjẽn̪ → ˈʃjẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈʃjẽː → ˈʃjɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃjɛ̃ː → ʃjɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    ʃjɛ̃ː → ʃjɛ̃   (ɛ̃ː→ɛ̃)
```

## chose

`kˈɑwsɑm` → `ʃoz`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkɑw.sɑm → ˈkɑw.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈkɑw.sɑ → ˈkaw.sa   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈkaw.sa → ˈkʲaw.sa   (k→kʲ)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈkʲaw.sa → ˈkʲɔw.sa   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲɔw.sa → ˈcɔw.sa   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcɔw.sa → ˈt͡ʃɔw.sa   (c→t͡ʃ)
600: a voiceless consonant voices intervocalically
    ˈt͡ʃɔw.sa → ˈt͡ʃɔw.za   (s→z)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈt͡ʃɔw.za → ˈt͡ʃɔ.za   (w→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡ʃɔ.za → ˈt͡ʃɔ.zə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃɔ.zə → ˈʃɔ.zə   (t͡ʃ→ʃ)
1200: lax back mid o lengthens before z or v
    ˈʃɔ.zə → ˈʃɔː.zə   (ˈɔ→ˈɔː)
1200: a long back mid o tenses to oː
    ˈʃɔː.zə → ˈʃoː.zə   (ˈɔː→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˈʃoː.zə → ˈʃoːzə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʃoːzə̯ → ˈʃoːz   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃoːz → ʃoːz   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    ʃoːz → ʃoz   (oː→o)
```

## cinquante

`kwˈiːn̪kwˈɑːn̪t̪ɑm` → `sɛ̃.kɑ̃t̪`

```
-100: n assimilates to a following velar stop
    ˈkwiːn̪ˈkwɑːn̪.t̪ɑm → ˈkwiːŋˈkwɑːn̪.t̪ɑm   (n̪→ŋ)
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈkwiːŋˈkwɑːn̪.t̪ɑm → ˈkɣʷiːŋˈkɣʷɑːn̪.t̪ɑm   (w→ɣʷ, w→ɣʷ)
-100: the labiovelar approximant simplifies to w after a velar consonant
    ˈkɣʷiːŋˈkɣʷɑːn̪.t̪ɑm → ˈkwiːŋˈkwɑːn̪.t̪ɑm   (ɣʷ→w, ɣʷ→w)
-100: the old primary stress demotes when a new one has been placed (type 2)
    ˈkwiːŋˈkwɑːn̪.t̪ɑm → ˌkwiːŋˈkwɑːn̪.t̪ɑm   (ˈiː→ˌiː)
-100: the length feature is dropped now that quality carries the contrast
    ˌkwiːŋˈkwɑːn̪.t̪ɑm → ˌkwiŋˈkwɑn̪.t̪ɑm   (ˌiː→ˌi, ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkwiŋˈkwɑn̪.t̪ɑm → ˌkwiŋˈkwɑn̪.t̪ɑ   (m→∅)
-100: w dissimilates between two kw sequences
    ˌkwiŋˈkwɑn̪.t̪ɑ → ˌkiŋˈkwɑn̪.t̪ɑ   (w→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌkiŋˈkwɑn̪.t̪ɑ → ˌkʲiŋˈkwɑn̪.t̪ɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌkʲiŋˈkwɑn̪.t̪ɑ → ˌciŋˈkwɑn̪.t̪ɑ   (kʲ→c)
500: a palatal stop affricates
    ˌciŋˈkwɑn̪.t̪ɑ → ˌt͡sʲiŋˈkwɑn̪.t̪ɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌt͡sʲiŋˈkwɑn̪.t̪ɑ → ˌt͡sʲiŋˈkwan̪.t̪a   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˌt͡sʲiŋˈkwan̪.t̪a → ˌt͡sʲiŋˈkwʲan̪.t̪a   (w→wʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌt͡sʲiŋˈkwʲan̪.t̪a → ˌt͡sʲiŋˈkɥan̪.t̪a   (wʲ→ɥ)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌt͡sʲiŋˈkɥan̪.t̪a → ˌt͡sʲiŋˈkɥɛn̪.t̪a   (ˈa→ˈɛ)
600: w is lost after k before a front non-low vowel
    ˌt͡sʲiŋˈkɥɛn̪.t̪a → ˌt͡sʲiŋˈkɛn̪.t̪a   (ɥ→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌt͡sʲiŋˈkɛn̪.t̪a → ˌt͡sʲiŋˈkɛn̪.t̪ə   (a→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌt͡sʲiŋˈkɛn̪.t̪ə → ˌt͡sʲiŋˈkɛ̃n̪.t̪ə   (ˈɛ→ˈɛ̃)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌt͡sʲiŋˈkɛ̃n̪.t̪ə → ˌt͡sʲĩŋˈkɛ̃n̪.t̪ə   (ˌi→ˌĩ)
1000: nasalized front mid vowels become nasalized a
    ˌt͡sʲĩŋˈkɛ̃n̪.t̪ə → ˌt͡sʲĩŋˈkãn̪.t̪ə   (ˈɛ̃→ˈã)
1000: all affricates become sibilants (deaffrication)
    ˌt͡sʲĩŋˈkãn̪.t̪ə → ˌsʲĩŋˈkãn̪.t̪ə   (t͡sʲ→sʲ)
1200: nasalized ĩ lowers to ẽ
    ˌsʲĩŋˈkãn̪.t̪ə → ˌsʲẽŋˈkãn̪.t̪ə   (ˌĩ→ˌẽ)
1200: the remaining anterior palatalized consonants depalatalize
    ˌsʲẽŋˈkãn̪.t̪ə → ˌsẽŋˈkãn̪.t̪ə   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsẽŋˈkãn̪.t̪ə → ˌsẽːˈkãː.t̪ə   (ˌẽŋˈkãn̪→ˌẽːˈkãː)
1400: nasalized ẽ lowers to ɛ̃
    ˌsẽːˈkãː.t̪ə → ˌsɛ̃ːˈkãː.t̪ə   (ˌẽː→ˌɛ̃ː)
1400: final ə becomes a non-syllabic off-glide
    ˌsɛ̃ːˈkãː.t̪ə → ˌsɛ̃ːˈkãːt̪ə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌsɛ̃ːˈkãːt̪ə̯ → ˌsɛ̃ːˈkɑ̃ːt̪ə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˌsɛ̃ːˈkɑ̃ːt̪ə̯ → ˌsɛ̃ːˈkɑ̃ːt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɛ̃ːˈkɑ̃ːt̪ → sɛ̃ː.kɑ̃ːt̪   (ˌɛ̃ː→ɛ̃ː, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    sɛ̃ː.kɑ̃ːt̪ → sɛ̃.kɑ̃t̪   (ɛ̃ː→ɛ̃, ɑ̃ː→ɑ̃)
```

## cire

`kˈeːrɑm` → `siʁ`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈkeː.rɑm → ˈke.rɑm   (ˈeː→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈke.rɑm → ˈke.rɑ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈke.rɑ → ˈkʲe.rɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈkʲe.rɑ → ˈce.rɑ   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˈce.rɑ → ˈceː.rɑ   (ˈe→ˈeː)
500: stressed eː raises to iː after a high-front consonant
    ˈceː.rɑ → ˈciː.rɑ   (ˈeː→ˈiː)
500: a palatal stop affricates
    ˈciː.rɑ → ˈt͡sʲiː.rɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˈt͡sʲiː.rɑ → ˈt͡sʲiː.ra   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡sʲiː.ra → ˈt͡sʲiː.rə   (a→ə)
750: vowel length resets to short
    ˈt͡sʲiː.rə → ˈt͡sʲi.rə   (ˈiː→ˈi)
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲi.rə → ˈsʲi.rə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲi.rə → ˈsi.rə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈsi.rə → ˈsirə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsirə̯ → ˈsir   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈsir → ˈsiʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsiʀ → siʀ   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    siʀ → siʁ   (ʀ→ʁ)
```

## cité

`kˌiːwit̪ˈɑːt̪em` → `si.t̪e`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌkiː.wiˈt̪ɑː.t̪em → ˌkiː.ɣʷiˈt̪ɑː.t̪em   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkiː.ɣʷiˈt̪ɑː.t̪em → ˌkiː.ɣʷɪˈt̪ɑː.t̪ɛm   (i→ɪ, e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌkiː.ɣʷɪˈt̪ɑː.t̪ɛm → ˌkiː.βʷɪˈt̪ɑː.t̪ɛm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkiː.βʷɪˈt̪ɑː.t̪ɛm → ˌki.βʷɪˈt̪ɑ.t̪ɛm   (ˌiː→ˌi, ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌki.βʷɪˈt̪ɑ.t̪ɛm → ˌki.βʷeˈt̪ɑ.t̪ɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌki.βʷeˈt̪ɑ.t̪ɛm → ˌki.βʷeˈt̪ɑ.t̪ɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌki.βʷeˈt̪ɑ.t̪ɛ → ˌkʲi.βʷeˈt̪ɑ.t̪ɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌkʲi.βʷeˈt̪ɑ.t̪ɛ → ˌci.βʷeˈt̪ɑ.t̪ɛ   (kʲ→c)
300: unstressed vowels deleted between the labiovelar fricative and a coronal stop
    ˌci.βʷeˈt̪ɑ.t̪ɛ → ˌciβʷˈt̪ɑ.t̪ɛ   (e→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌciβʷˈt̪ɑ.t̪ɛ → ˌciβʷˈt̪ɑː.t̪ɛ   (ˈɑ→ˈɑː)
500: labialized bilabial fricatives delabialize
    ˌciβʷˈt̪ɑː.t̪ɛ → ˌciβˈt̪ɑː.t̪ɛ   (βʷ→β)
500: a palatal stop affricates
    ˌciβˈt̪ɑː.t̪ɛ → ˌt͡sʲiβˈt̪ɑː.t̪ɛ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌt͡sʲiβˈt̪ɑː.t̪ɛ → ˌt͡sʲiβˈt̪aː.t̪ɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt͡sʲiβˈt̪aː.t̪ɛ → ˌt͡sʲiβˈt̪aː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt͡sʲiβˈt̪aː.t̪ə → ˌt͡sʲiβˈt̪aːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt͡sʲiβˈt̪aːt̪ə̯ → ˌt͡sʲiβˈt̪aːt̪   (ə̯→∅)
600: a labial consonant becomes t before a voiceless coronal stop
    ˌt͡sʲiβˈt̪aːt̪ → ˌt͡sʲit̪ˈt̪aːt̪   (β→t̪)
600: long stressed vowels diphthongize
    ˌt͡sʲit̪ˈt̪aːt̪ → ˌt͡sʲit̪ˈt̪ae̯t̪   (ˈaː→ˈae̯)
750: a word-final stop re-opens to a fricative after a vowel
    ˌt͡sʲit̪ˈt̪ae̯t̪ → ˌt͡sʲit̪ˈt̪ae̯θ   (t̪→θ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌt͡sʲit̪ˈt̪ae̯θ → ˌt͡sʲit̪ˈt̪eːθ   (ˈae̯→ˈeː)
750: a dental stop deletes before another coronal stop
    ˌt͡sʲit̪ˈt̪eːθ → ˌt͡sʲiˈt̪eːθ   (t̪→∅)
1000: vowel length resets to short
    ˌt͡sʲiˈt̪eːθ → ˌt͡sʲiˈt̪eθ   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌt͡sʲiˈt̪eθ → ˌt͡sʲiˈt̪e   (θ→∅)
1000: all affricates become sibilants (deaffrication)
    ˌt͡sʲiˈt̪e → ˌsʲiˈt̪e   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˌsʲiˈt̪e → ˌsiˈt̪e   (sʲ→s)
1400: stress is leveled — no longer distinctive for vowels
    ˌsiˈt̪e → si.t̪e   (ˌi→i, ˈe→e)
```

## cognée

`kˌun̪eˈɑːt̪ɑm` → `kɔ.ɲe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌku.n̪eˈɑː.t̪ɑm → ˌkʊ.n̪ɛˈɑː.t̪ɑm   (ˌu→ˌʊ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌkʊ.n̪ɛˈɑː.t̪ɑm → ˌkʊˈn̪jɑː.t̪ɑm   (ɛ→j)
-100: yod strengthens before a vowel
    ˌkʊˈn̪jɑː.t̪ɑm → ˌkʊn̪ˈʝɑː.t̪ɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkʊn̪ˈʝɑː.t̪ɑm → ˌkʊn̪ˈʝɑ.t̪ɑm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌkʊn̪ˈʝɑ.t̪ɑm → ˌkon̪ˈʝɑ.t̪ɑm   (ˌʊ→ˌo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkon̪ˈʝɑ.t̪ɑm → ˌkon̪ˈʝɑ.t̪ɑ   (m→∅)
300: the coronal nasal palatalizes before yod
    ˌkon̪ˈʝɑ.t̪ɑ → ˌkoˈɲɑ.t̪ɑ   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌkoˈɲɑ.t̪ɑ → ˌkoˈɲɑː.t̪ɑ   (ˈɑ→ˈɑː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌkoˈɲɑː.t̪ɑ → ˌkũˈɲɑː.t̪ɑ   (ˌo→ˌũ)
500: the low vowel fronts by default
    ˌkũˈɲɑː.t̪ɑ → ˌkũˈɲaː.t̪a   (ˈɑː→ˈaː, ɑ→a)
600: a voiceless consonant voices intervocalically
    ˌkũˈɲaː.t̪a → ˌkũˈɲaː.d̪a   (t̪→d̪)
600: a stressed low vowel becomes front non-tense after a front glide, before a consonant + non-consonantal
    ˌkũˈɲaː.d̪a → ˌkũˈɲɛː.d̪a   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌkũˈɲɛː.d̪a → ˌkũˈɲie̯.d̪a   (ˈɛː→ˈie̯)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌkũˈɲie̯.d̪a → ˌkũˈɲie̯.ða   (d̪→ð)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌkũˈɲie̯.ða → ˌkũˈɲie̯.ðə   (a→ə)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌkũˈɲie̯.ðə → ˌkũˈɲje.ðə   (ˈi→j, e̯→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌkũˈɲje.ðə → ˌkũˈɲje.ə   (ð→∅)
1200: schwa desyllabifies after another vowel
    ˌkũˈɲje.ə → ˌkũˈɲjeə̯   (ə→ə̯)
1200: je becomes e after a palatal consonant
    ˌkũˈɲjeə̯ → ˌkũˈɲeə̯   (j→∅)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˌkũˈɲeə̯ → ˌkũˈɲeː   (ˈeə̯→ˈeː)
1400: stress is leveled — no longer distinctive for vowels
    ˌkũˈɲeː → kũ.ɲeː   (ˌũ→ũ, ˈeː→eː)
1400: distinctive vowel length is lost entirely
    kũ.ɲeː → kũ.ɲe   (eː→e)
1400: nasal ũ opens to ɔ̃
    kũ.ɲe → kɔ̃.ɲe   (ũ→ɔ̃)
1400: ɔ̃ (and œ̃) denasalizes in an open syllable before a nasal consonant
    kɔ̃.ɲe → kɔ.ɲe   (ɔ̃→ɔ)
```

## comble

`kˈumulum` → `kɔ̃bl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈku.mu.lum → ˈkʊ.mʊ.lʊm   (ˈu→ˈʊ, u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈkʊ.mʊ.lʊm → ˈkʊ.mlʊm   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈkʊ.mlʊm → ˈko.mlom   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈko.mlom → ˈko.mlo   (m→∅)
500: b epenthesized between m and a coronal non-nasal sonorant glide
    ˈko.mlo → ˈkom.blo   (∅→b)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈkom.blo → ˈkũm.blo   (ˈo→ˈũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkũm.blo → ˈkũm.blə   (o→ə)
600: schwa becomes non-syllabic
    ˈkũm.blə → ˈkũmblə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈkũmblə̯ → ˈkũm.blə   (ə̯→ə)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈkũm.blə → ˈkũː.blə   (ˈũm→ˈũː)
1400: final ə becomes a non-syllabic off-glide
    ˈkũː.blə → ˈkũːblə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkũːblə̯ → ˈkũːbl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkũːbl → kũːbl   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    kũːbl → kũbl   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    kũbl → kɔ̃bl   (ũ→ɔ̃)
```

## connaître

`kˌon̪n̪ˈoːskere` → `kɔ.n̪wat̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkon̪ˈn̪oːs.ke.re → ˌkɔn̪ˈn̪oːs.kɛ.rɛ   (ˌo→ˌɔ, e→ɛ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌkɔn̪ˈn̪oːs.kɛ.rɛ → ˌkɔn̪ˈn̪os.kɛ.rɛ   (ˈoː→ˈo)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌkɔn̪ˈn̪os.kɛ.rɛ → ˌkɔn̪ˈn̪os.kʲɛ.rɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌkɔn̪ˈn̪os.kʲɛ.rɛ → ˌkɔn̪ˈn̪os.cɛ.rɛ   (kʲ→c)
500: ŋ/ɫ/s palatalize before a complex palatal-triggering sequence
    ˌkɔn̪ˈn̪os.cɛ.rɛ → ˌkɔn̪ˈn̪osʲ.cɛ.rɛ   (s→sʲ)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˌkɔn̪ˈn̪osʲ.cɛ.rɛ → ˌkɔn̪ˈn̪osʲ.crɛ   (ɛ→∅)
500: a palatal stop becomes a dental fricative before a non-front consonant
    ˌkɔn̪ˈn̪osʲ.crɛ → ˌkɔn̪ˈn̪osʲ.t̪rɛ   (c→t̪)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌkɔn̪ˈn̪osʲ.t̪rɛ → ˌkũn̪ˈn̪osʲ.t̪rɛ   (ˌɔ→ˌũ)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌkũn̪ˈn̪osʲ.t̪rɛ → ˌkũn̪ˈn̪osʲ.t̪ʲrɛ   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌkũn̪ˈn̪osʲ.t̪ʲrɛ → ˌkũn̪ˈn̪osʲ.t̪ʲrə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌkũn̪ˈn̪osʲ.t̪ʲrə → ˌkũn̪ˈn̪osʲt̪ʲrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌkũn̪ˈn̪osʲt̪ʲrə̯ → ˌkũn̪ˈn̪osʲt̪ʲr   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˌkũn̪ˈn̪osʲt̪ʲr → ˌkũn̪ˈn̪osʲ.t̪ʲrə   (∅→ə)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˌkũn̪ˈn̪osʲ.t̪ʲrə → ˌkũn̪ˈn̪osʲ.t̪ʲrʲə   (r→rʲ)
600: palatalized r depalatalizes
    ˌkũn̪ˈn̪osʲ.t̪ʲrʲə → ˌkũn̪ˈn̪osʲ.t̪ʲrə   (rʲ→r)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌkũn̪ˈn̪osʲ.t̪ʲrə → ˌkũn̪ˈn̪ojsj.t̪rə   (sʲt̪ʲ→jsjt̪)
600: j is lost after j or a consonant, before a consonant
    ˌkũn̪ˈn̪ojsj.t̪rə → ˌkũn̪ˈn̪ojs.t̪rə   (j→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˌkũn̪ˈn̪ojs.t̪rə → ˌkũˈn̪ojs.t̪rə   (n̪→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌkũˈn̪ojs.t̪rə → ˌkũˈn̪ujs.t̪rə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌkũˈn̪ujs.t̪rə → ˌkũˈn̪uɛ̯s.t̪rə   (j→ɛ̯)
1000: s becomes x after a vowel, before any consonant
    ˌkũˈn̪uɛ̯s.t̪rə → ˌkũˈn̪uɛ̯x.t̪rə   (s→x)
1000: the velar fricative x is lost
    ˌkũˈn̪uɛ̯x.t̪rə → ˌkũˈn̪uɛ̯.t̪rə   (x→∅)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌkũˈn̪uɛ̯.t̪rə → ˌkũˈn̪wɛ.t̪rə   (ˈu→w, ɛ̯→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌkũˈn̪wɛ.t̪rə → ˌkũˈn̪wɛt̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌkũˈn̪wɛt̪rə̯ → ˌkũˈn̪wɛt̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌkũˈn̪wɛt̪r → ˌkũˈn̪wɛt̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌkũˈn̪wɛt̪ʀ → kũ.n̪wɛt̪ʀ   (ˌũ→ũ, ˈɛ→ɛ)
1400: nasal ũ opens to ɔ̃
    kũ.n̪wɛt̪ʀ → kɔ̃.n̪wɛt̪ʀ   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    kɔ̃.n̪wɛt̪ʀ → kɔ.n̪wɛt̪ʀ   (ɔ̃→ɔ)
1400: wɛ becomes wa
    kɔ.n̪wɛt̪ʀ → kɔ.n̪wat̪ʀ   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    kɔ.n̪wat̪ʀ → kɔ.n̪wat̪ʁ   (ʀ→ʁ)
```

## corps

`kˈorpus` → `kɔʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkor.pus → ˈkɔr.pʊs   (ˈo→ˈɔ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkɔr.pʊs → ˈkɔr.pos   (ʊ→o)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkɔr.pos → ˈkɔr.pəs   (o→ə)
600: schwa becomes non-syllabic
    ˈkɔr.pəs → ˈkɔrpə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkɔrpə̯s → ˈkɔrps   (ə̯→∅)
600: a labial consonant becomes s before s
    ˈkɔrps → ˈkɔrss   (p→s)
600: an identical consonant geminate reduces to one, after a consonant or word start
    ˈkɔrss → ˈkɔrs   (s→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈkɔrs → ˈkɔɹs   (r→ɹ)
1400: final obstruents are lost
    ˈkɔɹs → ˈkɔɹ   (s→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈkɔɹ → ˈkɔr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈkɔr → ˈkɔʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkɔʀ → kɔʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    kɔʀ → kɔʁ   (ʀ→ʁ)
```

## coude

`kˈubit̪um` → `kut̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈku.bi.t̪um → ˈkʊ.bɪ.t̪ʊm   (ˈu→ˈʊ, i→ɪ, u→ʊ)
-100: b lenites to β intervocalically / before a sonorant
    ˈkʊ.bɪ.t̪ʊm → ˈkʊ.βɪ.t̪ʊm   (b→β)
-100: lax high vowels lower to tense mid vowels
    ˈkʊ.βɪ.t̪ʊm → ˈko.βe.t̪om   (ˈʊ→ˈo, ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈko.βe.t̪om → ˈko.βe.t̪o   (m→∅)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈko.βe.t̪o → ˈkoβ.t̪o   (e→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkoβ.t̪o → ˈkoβ.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈkoβ.t̪ə → ˈkoβt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkoβt̪ə̯ → ˈkoβt̪   (ə̯→∅)
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈkoβt̪ → ˈkoβ.t̪ə   (∅→ə)
600: a labial consonant becomes t before a voiceless coronal stop
    ˈkoβ.t̪ə → ˈkot̪.t̪ə   (β→t̪)
750: a dental stop deletes before another coronal stop
    ˈkot̪.t̪ə → ˈko.t̪ə   (t̪→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈko.t̪ə → ˈku.t̪ə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈku.t̪ə → ˈkut̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkut̪ə̯ → ˈkut̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkut̪ → kut̪   (ˈu→u)
```

## couille

`kˈoːleɑm` → `kuj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkoː.le.ɑm → ˈkoː.lɛ.ɑm   (e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈkoː.lɛ.ɑm → ˈkoː.ljɑm   (ɛ→j)
-100: l darkens before a non-lateral consonant
    ˈkoː.ljɑm → ˈkoː.ɫjɑm   (l→ɫ)
-100: yod strengthens before a vowel
    ˈkoː.ɫjɑm → ˈkoːɫ.ʝɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈkoːɫ.ʝɑm → ˈkoɫ.ʝɑm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkoɫ.ʝɑm → ˈkoɫ.ʝɑ   (m→∅)
300: l palatalizes to ʎ before yod
    ˈkoɫ.ʝɑ → ˈko.ʎɑ   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈko.ʎɑ → ˈkoː.ʎɑ   (ˈo→ˈoː)
500: the low vowel fronts by default
    ˈkoː.ʎɑ → ˈkoː.ʎa   (ɑ→a)
500: a non-high tense vowel shortens before ʎ/ɲ
    ˈkoː.ʎa → ˈko.ʎa   (ˈoː→ˈo)
600: a stressed vowel lengthens before a consonant + vowel
    ˈko.ʎa → ˈkoː.ʎa   (ˈo→ˈoː)
600: a non-high tense vowel shortens before ʎ/ɲ
    ˈkoː.ʎa → ˈko.ʎa   (ˈoː→ˈo)
600: a stressed vowel lengthens before a consonant + vowel (recurrence)
    ˈko.ʎa → ˈkoː.ʎa   (ˈo→ˈoː)
600: a non-high tense vowel shortens before ʎ/ɲ (recurrence)
    ˈkoː.ʎa → ˈko.ʎa   (ˈoː→ˈo)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈko.ʎa → ˈko.ʎə   (a→ə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈko.ʎə → ˈku.ʎə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈku.ʎə → ˈkuʎə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkuʎə̯ → ˈkuʎ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkuʎ → kuʎ   (ˈu→u)
1400: ʎ becomes j
    kuʎ → kuj   (ʎ→j)
```

## coupable

`kˌulpˈɑːbilem` → `ku.pabl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkulˈpɑː.bi.lem → ˌkʊlˈpɑː.bɪ.lɛm   (ˌu→ˌʊ, i→ɪ, e→ɛ)
-100: l darkens before a non-lateral consonant
    ˌkʊlˈpɑː.bɪ.lɛm → ˌkʊɫˈpɑː.bɪ.lɛm   (l→ɫ)
-100: b lenites to β intervocalically / before a sonorant
    ˌkʊɫˈpɑː.bɪ.lɛm → ˌkʊɫˈpɑː.βɪ.lɛm   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌkʊɫˈpɑː.βɪ.lɛm → ˌkʊɫˈpɑ.βɪ.lɛm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌkʊɫˈpɑ.βɪ.lɛm → ˌkoɫˈpɑ.βe.lɛm   (ˌʊ→ˌo, ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌkoɫˈpɑ.βe.lɛm → ˌkoɫˈpɑ.βe.lɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌkoɫˈpɑ.βe.lɛ → ˌkoɫˈpɑː.βe.lɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌkoɫˈpɑː.βe.lɛ → ˌkoɫˈpaː.βe.lɛ   (ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˌkoɫˈpaː.βe.lɛ → ˌkoɫˈpaː.βə.lɛ   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌkoɫˈpaː.βə.lɛ → ˌkoɫˈpaː.βə.lə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌkoɫˈpaː.βə.lə → ˌkoɫˈpaːβə̯lə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˌkoɫˈpaːβə̯lə̯ → ˌkoɫˈpaːβə̯.lə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˌkoɫˈpaːβə̯.lə → ˌkoɫˈpaː.βlə   (ə̯→∅)
600: the bilabial fricative hardens to b before a lateral
    ˌkoɫˈpaː.βlə → ˌkoɫˈpaː.blə   (β→b)
600: a non-round vowel shortens before a stop + l
    ˌkoɫˈpaː.blə → ˌkoɫˈpa.blə   (ˈaː→ˈa)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌkoɫˈpa.blə → ˌkuɫˈpa.blə   (ˌo→ˌu)
1000: back dark-l variants vocalize to w
    ˌkuɫˈpa.blə → ˌkuwˈpa.blə   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˌkuwˈpa.blə → ˌkuˈpa.blə   (w→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌkuˈpa.blə → ˌkuˈpablə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌkuˈpablə̯ → ˌkuˈpabl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌkuˈpabl → ku.pabl   (ˌu→u, ˈa→a)
```

## coupe

`kˈuppɑm` → `kup`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkup.pɑm → ˈkʊp.pɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkʊp.pɑm → ˈkop.pɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkop.pɑm → ˈkop.pɑ   (m→∅)
500: the low vowel fronts by default
    ˈkop.pɑ → ˈkop.pa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈkop.pa → ˈkop.pə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈkop.pə → ˈko.pə   (p→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈko.pə → ˈku.pə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈku.pə → ˈkupə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkupə̯ → ˈkup   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkup → kup   (ˈu→u)
```

## cours

`kˈursum` → `kuʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkur.sum → ˈkʊr.sʊm   (ˈu→ˈʊ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈkʊr.sʊm → ˈkor.som   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkor.som → ˈkor.so   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkor.so → ˈkor.sə   (o→ə)
600: schwa becomes non-syllabic
    ˈkor.sə → ˈkorsə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkorsə̯ → ˈkors   (ə̯→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈkors → ˈkurs   (ˈo→ˈu)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈkurs → ˈkuɹs   (r→ɹ)
1400: final obstruents are lost
    ˈkuɹs → ˈkuɹ   (s→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈkuɹ → ˈkur   (ɹ→r)
1400: r becomes uvular ʀ
    ˈkur → ˈkuʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkuʀ → kuʀ   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    kuʀ → kuʁ   (ʀ→ʁ)
```

## court

`kˌohˈort̪em` → `kuʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌkoˈhor.t̪em → ˌkɔˈhɔr.t̪ɛm   (ˌo→ˌɔ, ˈo→ˈɔ, e→ɛ)
-100: h lost word-internally (word-initial h survives at this stage)
    ˌkɔˈhɔr.t̪ɛm → ˌkɔˈɔr.t̪ɛm   (h→∅)
-100: o + o contracts to a long stressed o when stress is on the second vowel
    ˌkɔˈɔr.t̪ɛm → ˈkoːr.t̪ɛm   (ˌɔˈɔ→ˈoː)
-100: the length feature is dropped now that quality carries the contrast
    ˈkoːr.t̪ɛm → ˈkor.t̪ɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkor.t̪ɛm → ˈkor.t̪ɛ   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkor.t̪ɛ → ˈkor.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈkor.t̪ə → ˈkort̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkort̪ə̯ → ˈkort̪   (ə̯→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈkort̪ → ˈkurt̪   (ˈo→ˈu)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈkurt̪ → ˈkuɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈkuɹt̪ → ˈkuɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈkuɹ → ˈkur   (ɹ→r)
1400: r becomes uvular ʀ
    ˈkur → ˈkuʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkuʀ → kuʀ   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    kuʀ → kuʁ   (ʀ→ʁ)
```

## craie

`krˈeːt̪ɑm` → `kʁwa`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈkreː.t̪ɑm → ˈkre.t̪ɑm   (ˈeː→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈkre.t̪ɑm → ˈkre.t̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈkre.t̪ɑ → ˈkreː.t̪ɑ   (ˈe→ˈeː)
500: the low vowel fronts by default
    ˈkreː.t̪ɑ → ˈkreː.t̪a   (ɑ→a)
600: a voiceless consonant voices intervocalically
    ˈkreː.t̪a → ˈkreː.d̪a   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈkreː.d̪a → ˈkreː.ða   (d̪→ð)
600: long stressed vowels diphthongize
    ˈkreː.ða → ˈkrej.ða   (ˈeː→ˈej)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈkrej.ða → ˈkrej.ðə   (a→ə)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈkrej.ðə → ˈkroj.ðə   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈkroj.ðə → ˈkruj.ðə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈkruj.ðə → ˈkruɛ̯.ðə   (j→ɛ̯)
1000: the interdental fricatives (plain and palatalized) efface
    ˈkruɛ̯.ðə → ˈkru.ɛ̯ə   (ð→∅)
1200: schwa desyllabifies after another vowel
    ˈkru.ɛ̯ə → ˈkruɛ̯ə̯   (ə→ə̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈkruɛ̯ə̯ → ˈkrwɛə̯   (ˈu→w, ɛ̯→ˈɛ)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈkrwɛə̯ → ˈkrwɛː   (ˈɛə̯→ˈɛː)
1400: r becomes uvular ʀ
    ˈkrwɛː → ˈkʀwɛː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkʀwɛː → kʀwɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    kʀwɛː → kʀwɛ   (ɛː→ɛ)
1400: wɛ becomes wa
    kʀwɛ → kʀwa   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    kʀwa → kʁwa   (ʀ→ʁ)
```

## dette

`d̪ˈeːbit̪ɑm` → `d̪ɛt̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪eː.bi.t̪ɑm → ˈd̪eː.bɪ.t̪ɑm   (i→ɪ)
-100: b lenites to β intervocalically / before a sonorant
    ˈd̪eː.bɪ.t̪ɑm → ˈd̪eː.βɪ.t̪ɑm   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪eː.βɪ.t̪ɑm → ˈd̪e.βɪ.t̪ɑm   (ˈeː→ˈe)
-100: lax high vowels lower to tense mid vowels
    ˈd̪e.βɪ.t̪ɑm → ˈd̪e.βe.t̪ɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪e.βe.t̪ɑm → ˈd̪e.βe.t̪ɑ   (m→∅)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈd̪e.βe.t̪ɑ → ˈd̪eβ.t̪ɑ   (e→∅)
500: the low vowel fronts by default
    ˈd̪eβ.t̪ɑ → ˈd̪eβ.t̪a   (ɑ→a)
600: a labial consonant becomes t before a voiceless coronal stop
    ˈd̪eβ.t̪a → ˈd̪et̪.t̪a   (β→t̪)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd̪et̪.t̪a → ˈd̪et̪.t̪ə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈd̪et̪.t̪ə → ˈd̪e.t̪ə   (t̪→∅)
1000: stressed e laxes to ɛ before a consonant + vowel
    ˈd̪e.t̪ə → ˈd̪ɛ.t̪ə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈd̪ɛ.t̪ə → ˈd̪ɛt̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈd̪ɛt̪ə̯ → ˈd̪ɛt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪ɛt̪ → d̪ɛt̪   (ˈɛ→ɛ)
```

## devoir

`d̪ˌeːbˈeːre` → `d̪ə.vwaʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌd̪eːˈbeː.re → ˌd̪eːˈbeː.rɛ   (e→ɛ)
-100: b lenites to β intervocalically / before a sonorant
    ˌd̪eːˈbeː.rɛ → ˌd̪eːˈβeː.rɛ   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌd̪eːˈβeː.rɛ → ˌd̪eˈβe.rɛ   (ˌeː→ˌe, ˈeː→ˈe)
300: a stressed vowel lengthens before a single consonant + glide
    ˌd̪eˈβe.rɛ → ˌd̪eˈβeː.rɛ   (ˈe→ˈeː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌd̪eˈβeː.rɛ → ˌd̪eˈβeː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌd̪eˈβeː.rə → ˌd̪eˈβeːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌd̪eˈβeːrə̯ → ˌd̪eˈβeːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌd̪eˈβeːr → ˌd̪eˈβejr   (ˈeː→ˈej)
600: the remaining bilabial fricative becomes v
    ˌd̪eˈβejr → ˌd̪eˈvejr   (β→v)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌd̪eˈvejr → ˌd̪əˈvejr   (ˌe→ˌə)
1000: stressed e rounds early to o before j, after a voiced labial consonant
    ˌd̪əˈvejr → ˌd̪əˈvojr   (ˈe→ˈo)
1000: j lowers to ɛ̯ before r, in a back round diphthong
    ˌd̪əˈvojr → ˌd̪əˈvoɛ̯r   (j→ɛ̯)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌd̪əˈvoɛ̯r → ˌd̪əˈvuɛ̯r   (ˈo→ˈu)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌd̪əˈvuɛ̯r → ˌd̪əˈvwɛr   (ˈu→w, ɛ̯→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌd̪əˈvwɛr → ˌd̪əˈvwɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌd̪əˈvwɛɹ → ˌd̪əˈvwɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌd̪əˈvwɛr → ˌd̪əˈvwɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌd̪əˈvwɛʀ → d̪ə.vwɛʀ   (ˌə→ə, ˈɛ→ɛ)
1400: wɛ becomes wa
    d̪ə.vwɛʀ → d̪ə.vwaʀ   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    d̪ə.vwaʀ → d̪ə.vwaʁ   (ʀ→ʁ)
```

## don

`d̪ˈoːn̪um` → `d̪ɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪oː.n̪um → ˈd̪oː.n̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪oː.n̪ʊm → ˈd̪o.n̪ʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ˈd̪o.n̪ʊm → ˈd̪o.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪o.n̪om → ˈd̪o.n̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪o.n̪o → ˈd̪oː.n̪o   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈd̪oː.n̪o → ˈd̪ũː.n̪o   (ˈoː→ˈũː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪ũː.n̪o → ˈd̪ũː.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈd̪ũː.n̪ə → ˈd̪ũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd̪ũːn̪ə̯ → ˈd̪ũːn̪   (ə̯→∅)
750: vowel length resets to short
    ˈd̪ũːn̪ → ˈd̪ũn̪   (ˈũː→ˈũ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈd̪ũn̪ → ˈd̪ũː   (ˈũn̪→ˈũː)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪ũː → d̪ũː   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    d̪ũː → d̪ũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    d̪ũ → d̪ɔ̃   (ũ→ɔ̃)
```

## donne

`d̪ˈoːn̪ɑt̪` → `d̪ɔn̪`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪oː.n̪ɑt̪ → ˈd̪o.n̪ɑt̪   (ˈoː→ˈo)
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪o.n̪ɑt̪ → ˈd̪oː.n̪ɑt̪   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈd̪oː.n̪ɑt̪ → ˈd̪ũː.n̪ɑt̪   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˈd̪ũː.n̪ɑt̪ → ˈd̪ũː.n̪at̪   (ɑ→a)
600: t/d spirantize word-finally after a vowel
    ˈd̪ũː.n̪at̪ → ˈd̪ũː.n̪aθ   (t̪→θ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd̪ũː.n̪aθ → ˈd̪ũː.n̪əθ   (a→ə)
750: vowel length resets to short
    ˈd̪ũː.n̪əθ → ˈd̪ũ.n̪əθ   (ˈũː→ˈũ)
1000: the interdental fricatives (plain and palatalized) efface
    ˈd̪ũ.n̪əθ → ˈd̪ũ.n̪ə   (θ→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈd̪ũ.n̪ə → ˈd̪ũn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈd̪ũn̪ə̯ → ˈd̪ũn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪ũn̪ → d̪ũn̪   (ˈũ→ũ)
1400: nasal ũ opens to ɔ̃
    d̪ũn̪ → d̪ɔ̃n̪   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    d̪ɔ̃n̪ → d̪ɔn̪   (ɔ̃→ɔ)
```

## donner

`d̪ˌoːn̪ˈɑːre` → `d̪ɔ.n̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌd̪oːˈn̪ɑː.re → ˌd̪oːˈn̪ɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌd̪oːˈn̪ɑː.rɛ → ˌd̪oˈn̪ɑ.rɛ   (ˌoː→ˌo, ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌd̪oˈn̪ɑ.rɛ → ˌd̪oˈn̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌd̪oˈn̪ɑː.rɛ → ˌd̪ũˈn̪ɑː.rɛ   (ˌo→ˌũ)
500: the low vowel fronts by default
    ˌd̪ũˈn̪ɑː.rɛ → ˌd̪ũˈn̪aː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌd̪ũˈn̪aː.rɛ → ˌd̪ũˈn̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌd̪ũˈn̪aː.rə → ˌd̪ũˈn̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌd̪ũˈn̪aːrə̯ → ˌd̪ũˈn̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌd̪ũˈn̪aːr → ˌd̪ũˈn̪ae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌd̪ũˈn̪ae̯r → ˌd̪ũˈn̪eːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌd̪ũˈn̪eːr → ˌd̪ũˈn̪er   (ˈeː→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌd̪ũˈn̪er → ˌd̪ũˈn̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌd̪ũˈn̪eɹ → ˌd̪ũˈn̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌd̪ũˈn̪e → d̪ũ.n̪e   (ˌũ→ũ, ˈe→e)
1400: nasal ũ opens to ɔ̃
    d̪ũ.n̪e → d̪ɔ̃.n̪e   (ũ→ɔ̃)
1400: ɔ̃ (and œ̃) denasalizes in an open syllable before a nasal consonant
    d̪ɔ̃.n̪e → d̪ɔ.n̪e   (ɔ̃→ɔ)
```

## double

`d̪ˈuplum` → `d̪ubl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪u.plum → ˈd̪ʊ.plʊm   (ˈu→ˈʊ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈd̪ʊ.plʊm → ˈd̪o.plom   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪o.plom → ˈd̪o.plo   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈd̪o.plo → ˈd̪oː.plo   (ˈo→ˈoː)
500: a vowel shortens before a consonant cluster
    ˈd̪oː.plo → ˈd̪o.plo   (ˈoː→ˈo)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant
    ˈd̪o.plo → ˈd̪oː.plo   (ˈo→ˈoː)
500: a vowel shortens before a consonant cluster (recurrence)
    ˈd̪oː.plo → ˈd̪o.plo   (ˈoː→ˈo)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant (recurrence)
    ˈd̪o.plo → ˈd̪oː.plo   (ˈo→ˈoː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪oː.plo → ˈd̪oː.plə   (o→ə)
600: schwa becomes non-syllabic
    ˈd̪oː.plə → ˈd̪oːplə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈd̪oːplə̯ → ˈd̪oː.plə   (ə̯→ə)
600: a voiceless anterior consonant voices before a coronal sonorant non-nasal consonant
    ˈd̪oː.plə → ˈd̪oː.blə   (p→b)
600: long stressed vowels diphthongize
    ˈd̪oː.blə → ˈd̪ow.blə   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈd̪ow.blə → ˈd̪o.blə   (w→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈd̪o.blə → ˈd̪u.blə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈd̪u.blə → ˈd̪ublə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈd̪ublə̯ → ˈd̪ubl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪ubl → d̪ubl   (ˈu→u)
```

## douter

`d̪ˌubit̪ˈɑːre` → `d̪u.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌd̪u.biˈt̪ɑː.re → ˌd̪ʊ.bɪˈt̪ɑː.rɛ   (ˌu→ˌʊ, i→ɪ, e→ɛ)
-100: b lenites to β intervocalically / before a sonorant
    ˌd̪ʊ.bɪˈt̪ɑː.rɛ → ˌd̪ʊ.βɪˈt̪ɑː.rɛ   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌd̪ʊ.βɪˈt̪ɑː.rɛ → ˌd̪ʊ.βɪˈt̪ɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌd̪ʊ.βɪˈt̪ɑ.rɛ → ˌd̪o.βeˈt̪ɑ.rɛ   (ˌʊ→ˌo, ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˌd̪o.βeˈt̪ɑ.rɛ → ˌd̪o.βeˈt̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌd̪o.βeˈt̪ɑː.rɛ → ˌd̪oβˈt̪ɑː.rɛ   (e→∅)
500: the low vowel fronts by default
    ˌd̪oβˈt̪ɑː.rɛ → ˌd̪oβˈt̪aː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌd̪oβˈt̪aː.rɛ → ˌd̪oβˈt̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌd̪oβˈt̪aː.rə → ˌd̪oβˈt̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌd̪oβˈt̪aːrə̯ → ˌd̪oβˈt̪aːr   (ə̯→∅)
600: a labial consonant becomes t before a voiceless coronal stop
    ˌd̪oβˈt̪aːr → ˌd̪ot̪ˈt̪aːr   (β→t̪)
600: long stressed vowels diphthongize
    ˌd̪ot̪ˈt̪aːr → ˌd̪ot̪ˈt̪ae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌd̪ot̪ˈt̪ae̯r → ˌd̪ot̪ˈt̪eːr   (ˈae̯→ˈeː)
750: a dental stop deletes before another coronal stop
    ˌd̪ot̪ˈt̪eːr → ˌd̪oˈt̪eːr   (t̪→∅)
1000: vowel length resets to short
    ˌd̪oˈt̪eːr → ˌd̪oˈt̪er   (ˈeː→ˈe)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌd̪oˈt̪er → ˌd̪uˈt̪er   (ˌo→ˌu)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌd̪uˈt̪er → ˌd̪uˈt̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌd̪uˈt̪eɹ → ˌd̪uˈt̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌd̪uˈt̪e → d̪u.t̪e   (ˌu→u, ˈe→e)
```

## douve

`d̪ˈoːgɑm` → `d̪uv`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪oː.gɑm → ˈd̪o.gɑm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪o.gɑm → ˈd̪o.gɑ   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈd̪o.gɑ → ˈd̪o.ɣɑ   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪o.ɣɑ → ˈd̪oː.ɣɑ   (ˈo→ˈoː)
500: the velar fricative becomes a labialized bilabial fricative between o and a low vowel
    ˈd̪oː.ɣɑ → ˈd̪oː.βʷɑ   (ɣ→βʷ)
500: labialized bilabial fricatives delabialize
    ˈd̪oː.βʷɑ → ˈd̪oː.βɑ   (βʷ→β)
500: the low vowel fronts by default
    ˈd̪oː.βɑ → ˈd̪oː.βa   (ɑ→a)
600: long stressed vowels diphthongize
    ˈd̪oː.βa → ˈd̪ow.βa   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈd̪ow.βa → ˈd̪o.βa   (w→∅)
600: the remaining bilabial fricative becomes v
    ˈd̪o.βa → ˈd̪o.va   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd̪o.va → ˈd̪o.və   (a→ə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈd̪o.və → ˈd̪u.və   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈd̪u.və → ˈd̪uvə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈd̪uvə̯ → ˈd̪uv   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪uv → d̪uv   (ˈu→u)
```

## drap

`d̪rˈɑppum` → `d̪ʁa`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪rɑp.pum → ˈd̪rɑp.pʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈd̪rɑp.pʊm → ˈd̪rɑp.pom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪rɑp.pom → ˈd̪rɑp.po   (m→∅)
500: the low vowel fronts by default
    ˈd̪rɑp.po → ˈd̪rap.po   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪rap.po → ˈd̪rap.pə   (o→ə)
600: schwa becomes non-syllabic
    ˈd̪rap.pə → ˈd̪rappə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd̪rappə̯ → ˈd̪rapp   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˈd̪rapp → ˈd̪rap   (p→∅)
1400: final obstruents are lost
    ˈd̪rap → ˈd̪ra   (p→∅)
1400: r becomes uvular ʀ
    ˈd̪ra → ˈd̪ʀa   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪ʀa → d̪ʀa   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    d̪ʀa → d̪ʁa   (ʀ→ʁ)
```

## dur

`d̪ˈuːrum` → `d̪yʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈd̪uː.rum → ˈd̪uː.rʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈd̪uː.rʊm → ˈd̪u.rʊm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˈd̪u.rʊm → ˈd̪u.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪u.rom → ˈd̪u.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪u.ro → ˈd̪uː.ro   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈd̪uː.ro → ˈd̪ʉː.ro   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪ʉː.ro → ˈd̪ʉː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈd̪ʉː.rə → ˈd̪ʉːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd̪ʉːrə̯ → ˈd̪ʉːr   (ə̯→∅)
750: vowel length resets to short
    ˈd̪ʉːr → ˈd̪ʉr   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈd̪ʉr → ˈd̪yr   (ˈʉ→ˈy)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈd̪yr → ˈd̪yɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈd̪yɹ → ˈd̪yr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈd̪yr → ˈd̪yʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪yʀ → d̪yʀ   (ˈy→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    d̪yʀ → d̪yʁ   (ʀ→ʁ)
```

## défaire

`d̪ˌisfˈɑkere` → `d̪e.fɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌd̪isˈfɑ.ke.re → ˌd̪ɪsˈfɑ.kɛ.rɛ   (ˌi→ˌɪ, e→ɛ, e→ɛ)
-100: unstressed front vowel lost between a back stop and a coronal (type a)
    ˌd̪ɪsˈfɑ.kɛ.rɛ → ˌd̪ɪsˈfɑ.krɛ   (ɛ→∅)
-100: lax high vowels lower to tense mid vowels
    ˌd̪ɪsˈfɑ.krɛ → ˌd̪esˈfɑ.krɛ   (ˌɪ→ˌe)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˌd̪esˈfɑ.krɛ → ˌd̪esˈfɑː.krɛ   (ˈɑ→ˈɑː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˌd̪esˈfɑː.krɛ → ˌd̪esˈfɑː.xrɛ   (k→x)
500: a vowel shortens before a consonant cluster
    ˌd̪esˈfɑː.xrɛ → ˌd̪esˈfɑ.xrɛ   (ˈɑː→ˈɑ)
500: the low vowel fronts by default
    ˌd̪esˈfɑ.xrɛ → ˌd̪esˈfa.xrɛ   (ˈɑ→ˈa)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌd̪esˈfa.xrɛ → ˌd̪esˈfa.çrɛ   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌd̪esˈfa.çrɛ → ˌd̪esˈfa.çrʲɛ   (r→rʲ)
600: yod lost before ʎ or palatalized r
    ˌd̪esˈfa.çrʲɛ → ˌd̪esˈfa.rʲɛ   (ç→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌd̪esˈfa.rʲɛ → ˌd̪esˈfa.rʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌd̪esˈfa.rʲə → ˌd̪esˈfarʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌd̪esˈfarʲə̯ → ˌd̪esˈfarʲ   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˌd̪esˈfarʲ → ˌd̪esˈfajrʲ   (∅→j)
600: a stressed vowel lengthens before j + optional consonants + a high-front coronal
    ˌd̪esˈfajrʲ → ˌd̪esˈfaːjrʲ   (ˈa→ˈaː)
600: palatalized r depalatalizes
    ˌd̪esˈfaːjrʲ → ˌd̪esˈfaːjr   (rʲ→r)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˌd̪esˈfaːjr → ˌd̪esˈfajr   (ˈaː→ˈa)
750: s voices to z before a non-coronal continuant consonant (e.g. f)
    ˌd̪esˈfajr → ˌd̪ezˈfajr   (s→z)
750: schwa is epenthesized word-finally after a low vowel + j + r
    ˌd̪ezˈfajr → ˌd̪ezˈfaj.rə   (∅→ə)
1000: a stressed vowel lengthens before z + one consonant + a vowel
    ˌd̪ezˈfaj.rə → ˌd̪eːzˈfaj.rə   (ˌe→ˌeː)
1000: z is lost before a consonant (preconsonantal effacement)
    ˌd̪eːzˈfaj.rə → ˌd̪eːˈfaj.rə   (z→∅)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌd̪eːˈfaj.rə → ˌd̪eːˈfɛː.rə   (ˈaj→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˌd̪eːˈfɛː.rə → ˌd̪eːˈfɛːrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌd̪eːˈfɛːrə̯ → ˌd̪eːˈfɛːr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌd̪eːˈfɛːr → ˌd̪eːˈfɛːʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌd̪eːˈfɛːʀ → d̪eː.fɛːʀ   (ˌeː→eː, ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    d̪eː.fɛːʀ → d̪e.fɛʀ   (eː→e, ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    d̪e.fɛʀ → d̪e.fɛʁ   (ʀ→ʁ)
```

## effriter

`ˌeksfrˌuːkt̪ˈɑːre` → `ef.ʁɥi.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌeksˌfruːkˈt̪ɑː.re → ˌɛksˌfruːkˈt̪ɑː.rɛ   (ˌe→ˌɛ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɛksˌfruːkˈt̪ɑː.rɛ → ˌɛksˌfrukˈt̪ɑ.rɛ   (ˌuː→ˌu, ˈɑː→ˈɑ)
-100: k lost before s + consonant
    ˌɛksˌfrukˈt̪ɑ.rɛ → ˌɛsˌfrukˈt̪ɑ.rɛ   (k→∅)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˌɛsˌfrukˈt̪ɑ.rɛ → ˌɛsˌfruxˈt̪ɑ.rɛ   (k→x)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɛsˌfruxˈt̪ɑ.rɛ → ˌɛsˌfruxˈt̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌɛsˌfruxˈt̪ɑː.rɛ → ˌɛsˌfruxˈt̪aː.rɛ   (ˈɑː→ˈaː)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌɛsˌfruxˈt̪aː.rɛ → ˌɛsˌfruçˈt̪aː.rɛ   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌɛsˌfruçˈt̪aː.rɛ → ˌɛsˌfruçˈt̪ʲaː.rɛ   (t̪→t̪ʲ)
500: a high tense round non-nasal vowel centralizes
    ˌɛsˌfruçˈt̪ʲaː.rɛ → ˌɛsˌfrʉçˈt̪ʲaː.rɛ   (ˌu→ˌʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɛsˌfrʉçˈt̪ʲaː.rɛ → ˌɛsˌfrʉçˈt̪ʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌɛsˌfrʉçˈt̪ʲaː.rə → ˌɛsˌfrʉçˈt̪ʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌɛsˌfrʉçˈt̪ʲaːrə̯ → ˌɛsˌfrʉçˈt̪ʲaːr   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌɛsˌfrʉçˈt̪ʲaːr → ˌɛsˌfrʉçjˈt̪aːr   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌɛsˌfrʉçjˈt̪aːr → ˌɛsˌfrʉçˈt̪aːr   (j→∅)
600: long stressed vowels diphthongize
    ˌɛsˌfrʉçˈt̪aːr → ˌɛsˌfrʉçˈt̪ae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɛ raises to e word-initially before a coronal continuant
    ˌɛsˌfrʉçˈt̪ae̯r → ˌesˌfrʉçˈt̪ae̯r   (ˌɛ→ˌe)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌesˌfrʉçˈt̪ae̯r → ˌesˌfrʉçˈt̪eːr   (ˈae̯→ˈeː)
750: ç merges into ʝ
    ˌesˌfrʉçˈt̪eːr → ˌesˌfrʉʝˈt̪eːr   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌesˌfrʉʝˈt̪eːr → ˌesˌfrʉjˈt̪eːr   (ʝ→j)
750: s voices to z before a non-coronal continuant consonant (e.g. f)
    ˌesˌfrʉjˈt̪eːr → ˌezˌfrʉjˈt̪eːr   (s→z)
1000: high round back vowels front (completion of u-fronting)
    ˌezˌfrʉjˈt̪eːr → ˌezˌfryjˈt̪eːr   (ˌʉ→ˌy)
1000: vowel length resets to short
    ˌezˌfryjˈt̪eːr → ˌezˌfryjˈt̪er   (ˈeː→ˈe)
1000: z is lost before a consonant (preconsonantal effacement)
    ˌezˌfryjˈt̪er → ˌeˌfryjˈt̪er   (z→∅)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˌeˌfryjˈt̪er → ˌeˌfrɥiˈt̪er   (ˌy→ɥ, j→ˌi)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌeˌfrɥiˈt̪er → ˌeˌfrɥiˈt̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌeˌfrɥiˈt̪eɹ → ˌeˌfrɥiˈt̪e   (ɹ→∅)
1400: r becomes uvular ʀ
    ˌeˌfrɥiˈt̪e → ˌeˌfʀɥiˈt̪e   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌeˌfʀɥiˈt̪e → e.fʀɥi.t̪e   (ˌe→e, ˌi→i, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    e.fʀɥi.t̪e → ef.ʁɥi.t̪e   (ʀ→ʁ)
```

## elle

`ˈillɑm` → `ɛl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈil.lɑm → ˈɪl.lɑm   (ˈi→ˈɪ)
-100: lax high vowels lower to tense mid vowels
    ˈɪl.lɑm → ˈel.lɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈel.lɑm → ˈel.lɑ   (m→∅)
500: the low vowel fronts by default
    ˈel.lɑ → ˈel.la   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈel.la → ˈel.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈel.lə → ˈe.lə   (l→∅)
1000: stressed e laxes to ɛ before a consonant + vowel
    ˈe.lə → ˈɛ.lə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈɛ.lə → ˈɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈɛlə̯ → ˈɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛl → ɛl   (ˈɛ→ɛ)
```

## engins

`ˌin̪gˈen̪ioːs` → `ɛ.jɛ̃`

```
-100: n assimilates to a following velar stop
    ˌin̪ˈge.n̪i.oːs → ˌiŋˈge.n̪i.oːs   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌiŋˈge.n̪i.oːs → ˌɪŋˈgɛ.n̪ɪ.oːs   (ˌi→ˌɪ, ˈe→ˈɛ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɪŋˈgɛ.n̪ɪ.oːs → ˌɪŋˈgɛ.n̪joːs   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɪŋˈgɛ.n̪joːs → ˌɪŋˈgɛn̪.ʝoːs   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɪŋˈgɛn̪.ʝoːs → ˌɪŋˈgɛn̪.ʝos   (oː→o)
-100: lax high vowels lower to tense mid vowels
    ˌɪŋˈgɛn̪.ʝos → ˌeŋˈgɛn̪.ʝos   (ˌɪ→ˌe)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌeŋˈgɛn̪.ʝos → ˌeŋˈgʲɛn̪.ʝos   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˌeŋˈgʲɛn̪.ʝos → ˌeŋˈɟɛn̪.ʝos   (gʲ→ɟ)
300: the coronal nasal palatalizes before yod
    ˌeŋˈɟɛn̪.ʝos → ˌeŋˈɟɛ.ɲos   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌeŋˈɟɛ.ɲos → ˌeŋˈɟɛː.ɲos   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˌeŋˈɟɛː.ɲos → ˌeŋˈɟie̯.ɲos   (ˈɛː→ˈie̯)
500: a non-labial nasal palatalizes before a voiced high-front non-nasal consonant
    ˌeŋˈɟie̯.ɲos → ˌeɲˈɟie̯.ɲos   (ŋ→ɲ)
500: a high-front glide is lost after a high-front nasal sonorant consonant (ɲ)
    ˌeɲˈɟie̯.ɲos → ˌeˈɲie̯.ɲos   (ɟ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌeˈɲie̯.ɲos → ˌeˈɲie̯.ɲəs   (o→ə)
600: schwa becomes non-syllabic
    ˌeˈɲie̯.ɲəs → ˌeˈɲie̯ɲə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌeˈɲie̯ɲə̯s → ˌeˈɲie̯ɲs   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˌeˈɲie̯ɲs → ˌeˈɲie̯ɲsʲ   (s→sʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌeˈɲie̯ɲsʲ → ˌeˈɲie̯ɲjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˌeˈɲie̯ɲjs → ˌeˈɲie̯ɲs   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˌeˈɲie̯ɲs → ˌeˈɲie̯ɲt͡sʲ   (s→t͡sʲ)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˌeˈɲie̯ɲt͡sʲ → ˌeˈɲie̯j̃n̪t͡sʲ   (ɲ→j̃n̪)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌeˈɲie̯j̃n̪t͡sʲ → ˌeˈɲie̯j̃t͡sʲ   (n̪→∅)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌeˈɲie̯j̃t͡sʲ → ˌəˈɲie̯j̃t͡sʲ   (ˌe→ˌə)
1000: secondary-stressed schwa reverts to e before a palatal consonant
    ˌəˈɲie̯j̃t͡sʲ → ˌeˈɲie̯j̃t͡sʲ   (ˌə→ˌe)
1000: a glide develops between a stressed mid front vowel and intervocalic ɲ
    ˌeˈɲie̯j̃t͡sʲ → ˌej̃ˈɲie̯j̃t͡sʲ   (∅→j̃)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌej̃ˈɲie̯j̃t͡sʲ → ˌẽj̃ˈɲie̯j̃t͡sʲ   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌẽj̃ˈɲie̯j̃t͡sʲ → ˌɛ̃j̃ˈɲie̯j̃t͡sʲ   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌɛ̃j̃ˈɲie̯j̃t͡sʲ → ˌãj̃ˈɲie̯j̃t͡sʲ   (ˌɛ̃→ˌã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌãj̃ˈɲie̯j̃t͡sʲ → ˌɛ̃j̃ˈɲie̯j̃t͡sʲ   (ˌã→ˌɛ̃)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌɛ̃j̃ˈɲie̯j̃t͡sʲ → ˌɛ̃j̃ˈɲjej̃t͡sʲ   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌɛ̃j̃ˈɲjej̃t͡sʲ → ˌɛ̃j̃ˈɲjej̃sʲ   (t͡sʲ→sʲ)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˌɛ̃j̃ˈɲjej̃sʲ → ˌɛ̃j̃ˈɲjẽj̃sʲ   (ˈe→ˈẽ)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌɛ̃j̃ˈɲjẽj̃sʲ → ˌɛ̃ˈɲjẽj̃sʲ   (j̃→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌɛ̃ˈɲjẽj̃sʲ → ˌɛ̃ˈɲjẽj̃s   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌɛ̃ˈɲjẽj̃s → ˌɛ̃ˈɲjẽːs   (ˈẽj̃→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˌɛ̃ˈɲjẽːs → ˌɛ̃ˈɲjɛ̃ːs   (ˈẽː→ˈɛ̃ː)
1400: final obstruents are lost
    ˌɛ̃ˈɲjɛ̃ːs → ˌɛ̃ˈɲjɛ̃ː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌɛ̃ˈɲjɛ̃ː → ɛ̃.ɲjɛ̃ː   (ˌɛ̃→ɛ̃, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    ɛ̃.ɲjɛ̃ː → ɛ̃.ɲjɛ̃   (ɛ̃ː→ɛ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    ɛ̃.ɲjɛ̃ → ɛ.ɲjɛ̃   (ɛ̃→ɛ)
1400: a high front vowel after another vowel is absorbed into a following j
    ɛ.ɲjɛ̃ → ɛ.jɛ̃   (ɲ→∅)
```

## enseigne

`ˌin̪sˈign̪iɑm` → `ɑ̃.sɛɲ`

```
-100: g assimilates to a following coronal nasal (gn cluster)
    ˌin̪ˈsi.gn̪i.ɑm → ˌin̪ˈsiŋ.n̪i.ɑm   (g→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌin̪ˈsiŋ.n̪i.ɑm → ˌɪn̪ˈsɪŋ.n̪ɪ.ɑm   (ˌi→ˌɪ, ˈi→ˈɪ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɪn̪ˈsɪŋ.n̪ɪ.ɑm → ˌɪn̪ˈsɪŋ.n̪jɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɪn̪ˈsɪŋ.n̪jɑm → ˌɪn̪ˈsɪŋn̪.ʝɑm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˌɪn̪ˈsɪŋn̪.ʝɑm → ˌen̪ˈseŋn̪.ʝɑm   (ˌɪ→ˌe, ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌen̪ˈseŋn̪.ʝɑm → ˌen̪ˈseŋn̪.ʝɑ   (m→∅)
300: the coronal nasal palatalizes before yod
    ˌen̪ˈseŋn̪.ʝɑ → ˌen̪ˈseŋ.ɲɑ   (n̪ʝ→ɲ)
500: ŋ palatalizes to ɲ before a coronal
    ˌen̪ˈseŋ.ɲɑ → ˌen̪ˈseɲ.ɲɑ   (ŋ→ɲ)
500: the low vowel fronts by default
    ˌen̪ˈseɲ.ɲɑ → ˌen̪ˈseɲ.ɲa   (ɑ→a)
500: a nasal consonant is lost after ɲ
    ˌen̪ˈseɲ.ɲa → ˌen̪ˈse.ɲa   (ɲ→∅)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌen̪ˈse.ɲa → ˌen̪ˈseː.ɲa   (ˈe→ˈeː)
500: a non-high tense vowel shortens before ʎ/ɲ
    ˌen̪ˈseː.ɲa → ˌen̪ˈse.ɲa   (ˈeː→ˈe)
600: a stressed vowel lengthens before a consonant + vowel
    ˌen̪ˈse.ɲa → ˌen̪ˈseː.ɲa   (ˈe→ˈeː)
600: a non-high tense vowel shortens before ʎ/ɲ
    ˌen̪ˈseː.ɲa → ˌen̪ˈse.ɲa   (ˈeː→ˈe)
600: a stressed vowel lengthens before a consonant + vowel (recurrence)
    ˌen̪ˈse.ɲa → ˌen̪ˈseː.ɲa   (ˈe→ˈeː)
600: a non-high tense vowel shortens before ʎ/ɲ (recurrence)
    ˌen̪ˈseː.ɲa → ˌen̪ˈse.ɲa   (ˈeː→ˈe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌen̪ˈse.ɲa → ˌen̪ˈse.ɲə   (a→ə)
1000: a glide develops between a stressed mid front vowel and intervocalic ɲ
    ˌen̪ˈse.ɲə → ˌen̪ˈsej̃.ɲə   (∅→j̃)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌen̪ˈsej̃.ɲə → ˌẽn̪ˈsẽj̃.ɲə   (ˌe→ˌẽ, ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˌẽn̪ˈsẽj̃.ɲə → ˌɛ̃n̪ˈsɛ̃j̃.ɲə   (ˌẽ→ˌɛ̃, ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌɛ̃n̪ˈsɛ̃j̃.ɲə → ˌãn̪ˈsãj̃.ɲə   (ˌɛ̃→ˌã, ˈɛ̃→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌãn̪ˈsãj̃.ɲə → ˌãn̪ˈsɛ̃j̃.ɲə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌãn̪ˈsɛ̃j̃.ɲə → ˌãn̪ˈsɛ̃.ɲə   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌãn̪ˈsɛ̃.ɲə → ˌãːˈsɛ̃.ɲə   (ˌãn̪→ˌãː)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˌãːˈsɛ̃.ɲə → ˌãːˈsɛ.ɲə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌãːˈsɛ.ɲə → ˌãːˈsɛɲə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌãːˈsɛɲə̯ → ˌɑ̃ːˈsɛɲə̯   (ˌãː→ˌɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˌɑ̃ːˈsɛɲə̯ → ˌɑ̃ːˈsɛɲ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌɑ̃ːˈsɛɲ → ɑ̃ː.sɛɲ   (ˌɑ̃ː→ɑ̃ː, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    ɑ̃ː.sɛɲ → ɑ̃.sɛɲ   (ɑ̃ː→ɑ̃)
```

## essai

`ˌeksˈɑgium` → `e.sɛ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌeˈksɑ.gi.um → ˌɛˈksɑ.gɪ.ʊm   (ˌe→ˌɛ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɛˈksɑ.gɪ.ʊm → ˌɛˈksɑ.gjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɛˈksɑ.gjʊm → ˌɛˈksɑ.gʝʊm   (j→ʝ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˌɛˈksɑ.gʝʊm → ˌɛxˈsɑ.gʝʊm   (k→x)
-100: lax high vowels lower to tense mid vowels
    ˌɛxˈsɑ.gʝʊm → ˌɛxˈsɑ.gʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɛxˈsɑ.gʝom → ˌɛxˈsɑ.gʝo   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌɛxˈsɑ.gʝo → ˌɛxˈsɑ.gʲʝo   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˌɛxˈsɑ.gʲʝo → ˌɛxˈsɑ.ɟʝo   (gʲ→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌɛxˈsɑ.ɟʝo → ˌɛxˈsɑʝ.ʝo   (ɟ→ʝ)
500: yod degeminates (lost before another yod)
    ˌɛxˈsɑʝ.ʝo → ˌɛxˈsɑ.ʝo   (ʝ→∅)
500: the low vowel fronts by default
    ˌɛxˈsɑ.ʝo → ˌɛxˈsa.ʝo   (ˈɑ→ˈa)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌɛxˈsa.ʝo → ˌɛçˈsa.ʝo   (x→ç)
500: ç becomes s word-initially after secondary-stressed ɛ, before s
    ˌɛçˈsa.ʝo → ˌɛsˈsa.ʝo   (ç→s)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌɛsˈsa.ʝo → ˌɛsˈsaː.ʝo   (ˈa→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɛsˈsaː.ʝo → ˌɛsˈsaː.ʝə   (o→ə)
600: schwa becomes non-syllabic
    ˌɛsˈsaː.ʝə → ˌɛsˈsaːʝə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌɛsˈsaːʝə̯ → ˌɛsˈsaːʝ   (ə̯→∅)
600: ʝ weakens to j before optional consonants + word end
    ˌɛsˈsaːʝ → ˌɛsˈsaːj   (ʝ→j)
600: long stressed vowels diphthongize
    ˌɛsˈsaːj → ˌɛsˈsae̯j   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˌɛsˈsae̯j → ˌɛsˈsaj   (e̯→∅)
600: secondary-stressed ɛ raises to e word-initially before a coronal continuant
    ˌɛsˈsaj → ˌesˈsaj   (ˌɛ→ˌe)
750: an identical consonant geminate reduces to one (recurrence)
    ˌesˈsaj → ˌeˈsaj   (s→∅)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌeˈsaj → ˌəˈsaj   (ˌe→ˌə)
1000: word-initial secondary-stressed schwa becomes e before a strident
    ˌəˈsaj → ˌeˈsaj   (ˌə→ˌe)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌeˈsaj → ˌeˈsɛː   (ˈaj→ˈɛː)
1400: stress is leveled — no longer distinctive for vowels
    ˌeˈsɛː → e.sɛː   (ˌe→e, ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    e.sɛː → e.sɛ   (ɛː→ɛ)
```

## eux

`ˈilloːs` → `ø`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈil.loːs → ˈɪl.loːs   (ˈi→ˈɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˈɪl.loːs → ˈɪl.los   (oː→o)
-100: lax high vowels lower to tense mid vowels
    ˈɪl.los → ˈel.los   (ˈɪ→ˈe)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈel.los → ˈel.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˈel.ləs → ˈellə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈellə̯s → ˈells   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˈells → ˈels   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈels → ˈeɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˈeɫs → ˈews   (ɫ→w)
1000: ew becomes øw
    ˈews → ˈøws   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈøws → ˈøs   (w→∅)
1000: a primary-stressed vowel lengthens before word-final s
    ˈøs → ˈøːs   (ˈø→ˈøː)
1400: final obstruents are lost
    ˈøːs → ˈøː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈøː → øː   (ˈøː→øː)
1400: distinctive vowel length is lost entirely
    øː → ø   (øː→ø)
```

## faim

`fˈɑmem` → `fɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfɑ.mem → ˈfɑ.mɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɑ.mɛm → ˈfɑ.mɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfɑ.mɛ → ˈfɑː.mɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈfɑː.mɛ → ˈfaː.mɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfaː.mɛ → ˈfaː.mə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈfaː.mə → ˈfaːmə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfaːmə̯ → ˈfaːm   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈfaːm → ˈfae̯m   (ˈaː→ˈae̯)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˈfae̯m → ˈfajm   (e̯→j)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˈfajm → ˈfaj̃m   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈfaj̃m → ˈfãj̃m   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈfãj̃m → ˈfɛ̃j̃m   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈfɛ̃j̃m → ˈfɛ̃m   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈfɛ̃m → ˈfɛ̃ː   (ˈɛ̃m→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɛ̃ː → fɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    fɛ̃ː → fɛ̃   (ɛ̃ː→ɛ̃)
```

## faner

`fˌen̪ˈɑːre` → `fə.n̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfeˈn̪ɑː.re → ˌfɛˈn̪ɑː.rɛ   (ˌe→ˌɛ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfɛˈn̪ɑː.rɛ → ˌfɛˈn̪ɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌfɛˈn̪ɑ.rɛ → ˌfɛˈn̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌfɛˈn̪ɑː.rɛ → ˌfɛˈn̪aː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌfɛˈn̪aː.rɛ → ˌfɛˈn̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌfɛˈn̪aː.rə → ˌfɛˈn̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌfɛˈn̪aːrə̯ → ˌfɛˈn̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌfɛˈn̪aːr → ˌfɛˈn̪ae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɛ raises to e before any two segments
    ˌfɛˈn̪ae̯r → ˌfeˈn̪ae̯r   (ˌɛ→ˌe)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌfeˈn̪ae̯r → ˌfeˈn̪eːr   (ˈae̯→ˈeː)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌfeˈn̪eːr → ˌfəˈn̪eːr   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌfəˈn̪eːr → ˌfə̃ˈn̪eːr   (ˌə→ˌə̃)
1000: vowel length resets to short
    ˌfə̃ˈn̪eːr → ˌfə̃ˈn̪er   (ˈeː→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌfə̃ˈn̪er → ˌfə̃ˈn̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌfə̃ˈn̪eɹ → ˌfə̃ˈn̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌfə̃ˈn̪e → fə̃.n̪e   (ˌə̃→ə̃, ˈe→e)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    fə̃.n̪e → fə.n̪e   (ə̃→ə)
```

## fasse

`fˈɑkiɑm` → `fas`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfɑ.ki.ɑm → ˈfɑ.kɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈfɑ.kɪ.ɑm → ˈfɑ.kjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈfɑ.kjɑm → ˈfɑ.kʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɑ.kʝɑm → ˈfɑ.kʝɑ   (m→∅)
-100: k geminates (as palatal cc) intervocalically before yod + vowel
    ˈfɑ.kʝɑ → ˈfɑc.cʝɑ   (k→cc)
300: yod absorbed into a preceding palatalized consonant
    ˈfɑc.cʝɑ → ˈfɑc.cɑ   (ʝ→∅)
500: geminate palatal stop cc becomes t + tsʲ
    ˈfɑc.cɑ → ˈfɑ.t̪t͡sʲɑ   (c→t̪, c→t͡sʲ)
500: the low vowel fronts by default
    ˈfɑ.t̪t͡sʲɑ → ˈfa.t̪t͡sʲa   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfa.t̪t͡sʲa → ˈfa.t̪t͡sʲə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈfa.t̪t͡sʲə → ˈfa.t͡sʲə   (t̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈfa.t͡sʲə → ˈfa.sʲə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈfa.sʲə → ˈfa.sə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈfa.sə → ˈfasə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈfasə̯ → ˈfas   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfas → fas   (ˈa→a)
```

## feint

`fˈin̪kt̪um` → `fɛ̃`

```
-100: n assimilates to a following velar stop
    ˈfin̪k.t̪um → ˈfiŋk.t̪um   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfiŋk.t̪um → ˈfɪŋk.t̪ʊm   (ˈi→ˈɪ, u→ʊ)
-100: k lost after ŋ before a voiceless coronal
    ˈfɪŋk.t̪ʊm → ˈfɪŋ.t̪ʊm   (k→∅)
-100: lax high vowels lower to tense mid vowels
    ˈfɪŋ.t̪ʊm → ˈfeŋ.t̪om   (ˈɪ→ˈe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfeŋ.t̪om → ˈfeŋ.t̪o   (m→∅)
500: ŋ palatalizes to ɲ before a coronal
    ˈfeŋ.t̪o → ˈfeɲ.t̪o   (ŋ→ɲ)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈfeɲ.t̪o → ˈfeɲ.t̪ʲo   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfeɲ.t̪ʲo → ˈfeɲ.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈfeɲ.t̪ʲə → ˈfeɲt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfeɲt̪ʲə̯ → ˈfeɲt̪ʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈfeɲt̪ʲ → ˈfeɲjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈfeɲjt̪ → ˈfeɲt̪   (j→∅)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˈfeɲt̪ → ˈfej̃n̪t̪   (ɲ→j̃n̪)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈfej̃n̪t̪ → ˈfej̃t̪   (n̪→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈfej̃t̪ → ˈfẽj̃t̪   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈfẽj̃t̪ → ˈfɛ̃j̃t̪   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈfɛ̃j̃t̪ → ˈfãj̃t̪   (ˈɛ̃→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈfãj̃t̪ → ˈfɛ̃j̃t̪   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈfɛ̃j̃t̪ → ˈfɛ̃t̪   (j̃→∅)
1400: final obstruents are lost
    ˈfɛ̃t̪ → ˈfɛ̃   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɛ̃ → fɛ̃   (ˈɛ̃→ɛ̃)
```

## femme

`fˈeːmin̪ɑm` → `fam`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfeː.mi.n̪ɑm → ˈfeː.mɪ.n̪ɑm   (i→ɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˈfeː.mɪ.n̪ɑm → ˈfe.mɪ.n̪ɑm   (ˈeː→ˈe)
-100: lax high vowels lower to tense mid vowels
    ˈfe.mɪ.n̪ɑm → ˈfe.me.n̪ɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfe.me.n̪ɑm → ˈfe.me.n̪ɑ   (m→∅)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈfe.me.n̪ɑ → ˈfem.n̪ɑ   (e→∅)
500: the low vowel fronts by default
    ˈfem.n̪ɑ → ˈfem.n̪a   (ɑ→a)
600: n becomes m before m (recurrence)
    ˈfem.n̪a → ˈfem.ma   (n̪→m)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfem.ma → ˈfem.mə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈfem.mə → ˈfe.mə   (m→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈfe.mə → ˈfẽ.mə   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈfẽ.mə → ˈfɛ̃.mə   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈfɛ̃.mə → ˈfã.mə   (ˈɛ̃→ˈã)
1400: final ə becomes a non-syllabic off-glide
    ˈfã.mə → ˈfãmə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈfãmə̯ → ˈfãm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfãm → fãm   (ˈã→ã)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    fãm → fam   (ã→a)
```

## fer

`fˈerrum` → `fɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfer.rum → ˈfɛr.rʊm   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈfɛr.rʊm → ˈfɛr.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɛr.rom → ˈfɛr.ro   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfɛr.ro → ˈfɛr.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈfɛr.rə → ˈfɛrrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfɛrrə̯ → ˈfɛrr   (ə̯→∅)
750: a word-final rr degeminates
    ˈfɛrr → ˈfɛr   (r→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈfɛr → ˈfɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈfɛɹ → ˈfɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈfɛr → ˈfɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɛʀ → fɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    fɛʀ → fɛʁ   (ʀ→ʁ)
```

## fermer

`fˌirmˈɑːre` → `fɛ.ʁme`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfirˈmɑː.re → ˌfɪrˈmɑː.rɛ   (ˌi→ˌɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfɪrˈmɑː.rɛ → ˌfɪrˈmɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌfɪrˈmɑ.rɛ → ˌferˈmɑ.rɛ   (ˌɪ→ˌe)
300: a stressed vowel lengthens before a single consonant + glide
    ˌferˈmɑ.rɛ → ˌferˈmɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌferˈmɑː.rɛ → ˌferˈmaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌferˈmaː.rɛ → ˌferˈmaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌferˈmaː.rə → ˌferˈmaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌferˈmaːrə̯ → ˌferˈmaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌferˈmaːr → ˌferˈmae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌferˈmae̯r → ˌferˈmeːr   (ˈae̯→ˈeː)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌferˈmeːr → ˌfɛrˈmeːr   (ˌe→ˌɛ)
1000: vowel length resets to short
    ˌfɛrˈmeːr → ˌfɛrˈmer   (ˈeː→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌfɛrˈmer → ˌfɛɹˈmeɹ   (r→ɹ, r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌfɛɹˈmeɹ → ˌfɛɹˈme   (ɹ→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌfɛɹˈme → ˌfɛrˈme   (ɹ→r)
1400: r becomes uvular ʀ
    ˌfɛrˈme → ˌfɛʀˈme   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌfɛʀˈme → fɛʀ.me   (ˌɛ→ɛ, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    fɛʀ.me → fɛ.ʁme   (ʀ→ʁ)
```

## feutrer

`fˌilt̪rˈɑːre` → `fø.t̪ʁe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfilˈt̪rɑː.re → ˌfɪlˈt̪rɑː.rɛ   (ˌi→ˌɪ, e→ɛ)
-100: l darkens before a non-lateral consonant
    ˌfɪlˈt̪rɑː.rɛ → ˌfɪɫˈt̪rɑː.rɛ   (l→ɫ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfɪɫˈt̪rɑː.rɛ → ˌfɪɫˈt̪rɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌfɪɫˈt̪rɑ.rɛ → ˌfeɫˈt̪rɑ.rɛ   (ˌɪ→ˌe)
300: a stressed vowel lengthens before a single consonant + glide
    ˌfeɫˈt̪rɑ.rɛ → ˌfeɫˈt̪rɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌfeɫˈt̪rɑː.rɛ → ˌfeɫˈt̪raː.rɛ   (ˈɑː→ˈaː)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌfeɫˈt̪raː.rɛ → ˌfeɫˈt̪ʲraː.rɛ   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌfeɫˈt̪ʲraː.rɛ → ˌfeɫˈt̪ʲraː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌfeɫˈt̪ʲraː.rə → ˌfeɫˈt̪ʲraːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌfeɫˈt̪ʲraːrə̯ → ˌfeɫˈt̪ʲraːr   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˌfeɫˈt̪ʲraːr → ˌfeɫˈt̪ʲrʲaːr   (r→rʲ)
600: palatalized r depalatalizes
    ˌfeɫˈt̪ʲrʲaːr → ˌfeɫˈt̪ʲraːr   (rʲ→r)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌfeɫˈt̪ʲraːr → ˌfeɫjˈt̪raːr   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌfeɫjˈt̪raːr → ˌfeɫˈt̪raːr   (j→∅)
600: long stressed vowels diphthongize
    ˌfeɫˈt̪raːr → ˌfeɫˈt̪rae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌfeɫˈt̪rae̯r → ˌfeɫˈt̪reːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌfeɫˈt̪reːr → ˌfeɫˈt̪rer   (ˈeː→ˈe)
1000: back dark-l variants vocalize to w
    ˌfeɫˈt̪rer → ˌfewˈt̪rer   (ɫ→w)
1000: ew becomes øw
    ˌfewˈt̪rer → ˌføwˈt̪rer   (ˌe→ˌø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˌføwˈt̪rer → ˌføˈt̪rer   (w→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌføˈt̪rer → ˌføˈt̪reɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌføˈt̪reɹ → ˌføˈt̪re   (ɹ→∅)
1400: r becomes uvular ʀ
    ˌføˈt̪re → ˌføˈt̪ʀe   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌføˈt̪ʀe → fø.t̪ʀe   (ˌø→ø, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    fø.t̪ʀe → fø.t̪ʁe   (ʀ→ʁ)
```

## ficelle

`fˌiːlikˈellɑm` → `fi.sɛl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfiː.liˈkel.lɑm → ˌfiː.lɪˈkɛl.lɑm   (i→ɪ, ˈe→ˈɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfiː.lɪˈkɛl.lɑm → ˌfi.lɪˈkɛl.lɑm   (ˌiː→ˌi)
-100: lax high vowels lower to tense mid vowels
    ˌfi.lɪˈkɛl.lɑm → ˌfi.leˈkɛl.lɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌfi.leˈkɛl.lɑm → ˌfi.leˈkɛl.lɑ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌfi.leˈkɛl.lɑ → ˌfi.leˈkʲɛl.lɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌfi.leˈkʲɛl.lɑ → ˌfi.leˈcɛl.lɑ   (kʲ→c)
500: a palatal stop affricates
    ˌfi.leˈcɛl.lɑ → ˌfi.leˈt͡sʲɛl.lɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌfi.leˈt͡sʲɛl.lɑ → ˌfi.leˈt͡sʲɛl.la   (ɑ→a)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌfi.leˈt͡sʲɛl.la → ˌfi.ləˈt͡sʲɛl.la   (e→ə)
600: schwa becomes non-syllabic
    ˌfi.ləˈt͡sʲɛl.la → ˌfilə̯ˈt͡sʲɛl.la   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌfilə̯ˈt͡sʲɛl.la → ˌfilˈt͡sʲɛl.la   (ə̯→∅)
600: a coronal palatalizes between two high-front segments
    ˌfilˈt͡sʲɛl.la → ˌfilʲˈt͡sʲɛl.la   (l→lʲ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌfilʲˈt͡sʲɛl.la → ˌfilʲˈt͡sʲɛl.lə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˌfilʲˈt͡sʲɛl.lə → ˌfilʲˈt͡sʲɛ.lə   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌfilʲˈt͡sʲɛ.lə → ˌfiɫˈt͡sʲɛ.lə   (lʲ→ɫ)
1000: dark l becomes ʎ after a front unrounded high vowel
    ˌfiɫˈt͡sʲɛ.lə → ˌfiʎˈt͡sʲɛ.lə   (ɫ→ʎ)
1000: ʎ effaces between an i-variant and a consonant
    ˌfiʎˈt͡sʲɛ.lə → ˌfiˈt͡sʲɛ.lə   (ʎ→∅)
1000: all affricates become sibilants (deaffrication)
    ˌfiˈt͡sʲɛ.lə → ˌfiˈsʲɛ.lə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˌfiˈsʲɛ.lə → ˌfiˈsɛ.lə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˌfiˈsɛ.lə → ˌfiˈsɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌfiˈsɛlə̯ → ˌfiˈsɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌfiˈsɛl → fi.sɛl   (ˌi→i, ˈɛ→ɛ)
```

## fils

`fˈiːlius` → `fi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfiː.li.us → ˈfiː.lɪ.ʊs   (i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈfiː.lɪ.ʊs → ˈfiː.ljʊs   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˈfiː.ljʊs → ˈfiː.ɫjʊs   (l→ɫ)
-100: yod strengthens before a vowel
    ˈfiː.ɫjʊs → ˈfiːɫ.ʝʊs   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈfiːɫ.ʝʊs → ˈfiɫ.ʝʊs   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˈfiɫ.ʝʊs → ˈfiɫ.ʝos   (ʊ→o)
300: l palatalizes to ʎ before yod
    ˈfiɫ.ʝos → ˈfi.ʎos   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfi.ʎos → ˈfiː.ʎos   (ˈi→ˈiː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfiː.ʎos → ˈfiː.ʎəs   (o→ə)
600: schwa becomes non-syllabic
    ˈfiː.ʎəs → ˈfiːʎə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfiːʎə̯s → ˈfiːʎs   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈfiːʎs → ˈfiːʎsʲ   (s→sʲ)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈfiːʎsʲ → ˈfiʎsʲ   (ˈiː→ˈi)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈfiʎsʲ → ˈfiʎjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈfiʎjs → ˈfiʎs   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈfiʎs → ˈfiʎt͡sʲ   (s→t͡sʲ)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈfiʎt͡sʲ → ˈfiɫt͡sʲ   (ʎ→ɫ)
1000: dark l becomes ʎ after a front unrounded high vowel
    ˈfiɫt͡sʲ → ˈfiʎt͡sʲ   (ɫ→ʎ)
1000: ʎ effaces between an i-variant and a consonant
    ˈfiʎt͡sʲ → ˈfit͡sʲ   (ʎ→∅)
1000: all affricates become sibilants (deaffrication)
    ˈfit͡sʲ → ˈfisʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈfisʲ → ˈfis   (sʲ→s)
1400: final obstruents are lost
    ˈfis → ˈfi   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfi → fi   (ˈi→i)
```

## fin

`fˈiːn̪em` → `fɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfiː.n̪em → ˈfiː.n̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˈfiː.n̪ɛm → ˈfi.n̪ɛm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfi.n̪ɛm → ˈfi.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfi.n̪ɛ → ˈfiː.n̪ɛ   (ˈi→ˈiː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfiː.n̪ɛ → ˈfiː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈfiː.n̪ə → ˈfiːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfiːn̪ə̯ → ˈfiːn̪   (ə̯→∅)
750: vowel length resets to short
    ˈfiːn̪ → ˈfin̪   (ˈiː→ˈi)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈfin̪ → ˈfĩn̪   (ˈi→ˈĩ)
1200: nasalized ĩ lowers to ẽ
    ˈfĩn̪ → ˈfẽn̪   (ˈĩ→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈfẽn̪ → ˈfẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈfẽː → ˈfɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɛ̃ː → fɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    fɛ̃ː → fɛ̃   (ɛ̃ː→ɛ̃)
```

## fléaux

`flˌɑgˈelloːs` → `fle.o`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌflɑˈgel.loːs → ˌflɑˈgɛl.loːs   (ˈe→ˈɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌflɑˈgɛl.loːs → ˌflɑˈgɛl.los   (oː→o)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌflɑˈgɛl.los → ˌflɑˈgʲɛl.los   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˌflɑˈgʲɛl.los → ˌflɑˈɟɛl.los   (gʲ→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌflɑˈɟɛl.los → ˌflɑˈʝɛl.los   (ɟ→ʝ)
500: the low vowel fronts by default
    ˌflɑˈʝɛl.los → ˌflaˈʝɛl.los   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌflaˈʝɛl.los → ˌflaˈʝɛl.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˌflaˈʝɛl.ləs → ˌflaˈʝɛllə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌflaˈʝɛllə̯s → ˌflaˈʝɛlls   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˌflaˈʝɛlls → ˌflaˈʝɛls   (l→∅)
600: ʝ weakens to j unconditionally
    ˌflaˈʝɛls → ˌflaˈjɛls   (ʝ→j)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌflaˈjɛls → ˌflaˈjɛɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˌflaˈjɛɫs → ˌflaˈjɛws   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌflaˈjɛws → ˌflaˈjɛa̯ws   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌflaˈjɛa̯ws → ˌflaˈje̯aws   (ˈɛ→e̯, a̯→ˈa)
1200: aw becomes long oː
    ˌflaˈje̯aws → ˌflaˈje̯oːs   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌflaˈje̯oːs → ˌflaˈjə̯oːs   (e̯→ə̯)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌflaˈjə̯oːs → ˌflaˈjoːs   (ə̯→∅)
1400: final obstruents are lost
    ˌflaˈjoːs → ˌflaˈjoː   (s→∅)
1400: aj becomes e before a tense tonic vowel
    ˌflaˈjoː → ˌflɛˈoː   (ˌaj→ˌɛ)
1400: countertonic ə/ɛ becomes ˌe after a labial + l
    ˌflɛˈoː → ˌfleˈoː   (ˌɛ→ˌe)
1400: stress is leveled — no longer distinctive for vowels
    ˌfleˈoː → fle.oː   (ˌe→e, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    fle.oː → fle.o   (oː→o)
```

## foi

`fˈid̪em` → `fwa`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfi.d̪em → ˈfɪ.d̪ɛm   (ˈi→ˈɪ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈfɪ.d̪ɛm → ˈfe.d̪ɛm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfe.d̪ɛm → ˈfe.d̪ɛ   (m→∅)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈfe.d̪ɛ → ˈfe.ðɛ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈfe.ðɛ → ˈfeː.ðɛ   (ˈe→ˈeː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfeː.ðɛ → ˈfeː.ðə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈfeː.ðə → ˈfeːðə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfeːðə̯ → ˈfeːð   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈfeːð → ˈfejð   (ˈeː→ˈej)
750: all final obstruents devoice
    ˈfejð → ˈfejθ   (ð→θ)
750: a supported non-strident fricative closes to a stop word-finally
    ˈfejθ → ˈfejt̪   (θ→t̪)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈfejt̪ → ˈfojt̪   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈfojt̪ → ˈfujt̪   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈfujt̪ → ˈfuɛ̯t̪   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈfuɛ̯t̪ → ˈfwɛt̪   (ˈu→w, ɛ̯→ˈɛ)
1400: final obstruents are lost
    ˈfwɛt̪ → ˈfwɛ   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfwɛ → fwɛ   (ˈɛ→ɛ)
1400: wɛ becomes wa
    fwɛ → fwa   (ɛ→a)
```

## fonder

`fˌun̪d̪ˈɑːre` → `fɔ̃.d̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfun̪ˈd̪ɑː.re → ˌfʊn̪ˈd̪ɑː.rɛ   (ˌu→ˌʊ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfʊn̪ˈd̪ɑː.rɛ → ˌfʊn̪ˈd̪ɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌfʊn̪ˈd̪ɑ.rɛ → ˌfon̪ˈd̪ɑ.rɛ   (ˌʊ→ˌo)
300: a stressed vowel lengthens before a single consonant + glide
    ˌfon̪ˈd̪ɑ.rɛ → ˌfon̪ˈd̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌfon̪ˈd̪ɑː.rɛ → ˌfũn̪ˈd̪ɑː.rɛ   (ˌo→ˌũ)
500: the low vowel fronts by default
    ˌfũn̪ˈd̪ɑː.rɛ → ˌfũn̪ˈd̪aː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌfũn̪ˈd̪aː.rɛ → ˌfũn̪ˈd̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌfũn̪ˈd̪aː.rə → ˌfũn̪ˈd̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌfũn̪ˈd̪aːrə̯ → ˌfũn̪ˈd̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌfũn̪ˈd̪aːr → ˌfũn̪ˈd̪ae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌfũn̪ˈd̪ae̯r → ˌfũn̪ˈd̪eːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌfũn̪ˈd̪eːr → ˌfũn̪ˈd̪er   (ˈeː→ˈe)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌfũn̪ˈd̪er → ˌfũːˈd̪er   (ˌũn̪→ˌũː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌfũːˈd̪er → ˌfũːˈd̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌfũːˈd̪eɹ → ˌfũːˈd̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌfũːˈd̪e → fũː.d̪e   (ˌũː→ũː, ˈe→e)
1400: distinctive vowel length is lost entirely
    fũː.d̪e → fũ.d̪e   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    fũ.d̪e → fɔ̃.d̪e   (ũ→ɔ̃)
```

## fontaine

`fˌon̪t̪ˈɑːn̪ɑm` → `fɔ̃.t̪ɛn̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfon̪ˈt̪ɑː.n̪ɑm → ˌfɔn̪ˈt̪ɑː.n̪ɑm   (ˌo→ˌɔ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfɔn̪ˈt̪ɑː.n̪ɑm → ˌfɔn̪ˈt̪ɑ.n̪ɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌfɔn̪ˈt̪ɑ.n̪ɑm → ˌfɔn̪ˈt̪ɑ.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌfɔn̪ˈt̪ɑ.n̪ɑ → ˌfɔn̪ˈt̪ɑː.n̪ɑ   (ˈɑ→ˈɑː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌfɔn̪ˈt̪ɑː.n̪ɑ → ˌfũn̪ˈt̪ɑː.n̪ɑ   (ˌɔ→ˌũ)
500: the low vowel fronts by default
    ˌfũn̪ˈt̪ɑː.n̪ɑ → ˌfũn̪ˈt̪aː.n̪a   (ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˌfũn̪ˈt̪aː.n̪a → ˌfũn̪ˈt̪ae̯.n̪a   (ˈaː→ˈae̯)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˌfũn̪ˈt̪ae̯.n̪a → ˌfũn̪ˈt̪aj.n̪a   (e̯→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌfũn̪ˈt̪aj.n̪a → ˌfũn̪ˈt̪aj.n̪ə   (a→ə)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˌfũn̪ˈt̪aj.n̪ə → ˌfũn̪ˈt̪aj̃.n̪ə   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌfũn̪ˈt̪aj̃.n̪ə → ˌfũn̪ˈt̪ãj̃.n̪ə   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌfũn̪ˈt̪ãj̃.n̪ə → ˌfũn̪ˈt̪ɛ̃j̃.n̪ə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌfũn̪ˈt̪ɛ̃j̃.n̪ə → ˌfũn̪ˈt̪ɛ̃.n̪ə   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌfũn̪ˈt̪ɛ̃.n̪ə → ˌfũːˈt̪ɛ̃.n̪ə   (ˌũn̪→ˌũː)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˌfũːˈt̪ɛ̃.n̪ə → ˌfũːˈt̪ɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌfũːˈt̪ɛ.n̪ə → ˌfũːˈt̪ɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌfũːˈt̪ɛn̪ə̯ → ˌfũːˈt̪ɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌfũːˈt̪ɛn̪ → fũː.t̪ɛn̪   (ˌũː→ũː, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    fũː.t̪ɛn̪ → fũ.t̪ɛn̪   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    fũ.t̪ɛn̪ → fɔ̃.t̪ɛn̪   (ũ→ɔ̃)
```

## force

`fˈort̪iɑm` → `fɔʁs`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfor.t̪i.ɑm → ˈfɔr.t̪ɪ.ɑm   (ˈo→ˈɔ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈfɔr.t̪ɪ.ɑm → ˈfɔr.t̪jɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈfɔr.t̪jɑm → ˈfɔr.t̪ʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɔr.t̪ʝɑm → ˈfɔr.t̪ʝɑ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈfɔr.t̪ʝɑ → ˈfɔrt͡sʲ.ʝɑ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˈfɔrt͡sʲ.ʝɑ → ˈfɔr.t͡sʲɑ   (ʝ→∅)
500: the low vowel fronts by default
    ˈfɔr.t͡sʲɑ → ˈfɔr.t͡sʲa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfɔr.t͡sʲa → ˈfɔr.t͡sʲə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈfɔr.t͡sʲə → ˈfɔr.sʲə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈfɔr.sʲə → ˈfɔr.sə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˈfɔr.sə → ˈfɔrsə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈfɔrsə̯ → ˈfɔɹsə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈfɔɹsə̯ → ˈfɔɹs   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈfɔɹs → ˈfɔrs   (ɹ→r)
1400: r becomes uvular ʀ
    ˈfɔrs → ˈfɔʀs   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɔʀs → fɔʀs   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    fɔʀs → fɔʁs   (ʀ→ʁ)
```

## fort

`fˈort̪em` → `fɔʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfor.t̪em → ˈfɔr.t̪ɛm   (ˈo→ˈɔ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɔr.t̪ɛm → ˈfɔr.t̪ɛ   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfɔr.t̪ɛ → ˈfɔr.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈfɔr.t̪ə → ˈfɔrt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfɔrt̪ə̯ → ˈfɔrt̪   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈfɔrt̪ → ˈfɔɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈfɔɹt̪ → ˈfɔɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈfɔɹ → ˈfɔr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈfɔr → ˈfɔʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɔʀ → fɔʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    fɔʀ → fɔʁ   (ʀ→ʁ)
```

## foudre

`fˈulgerem` → `fud̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈful.ge.rem → ˈfʊl.gɛ.rɛm   (ˈu→ˈʊ, e→ɛ, e→ɛ)
-100: l darkens before a non-lateral consonant
    ˈfʊl.gɛ.rɛm → ˈfʊɫ.gɛ.rɛm   (l→ɫ)
-100: lax high vowels lower to tense mid vowels
    ˈfʊɫ.gɛ.rɛm → ˈfoɫ.gɛ.rɛm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfoɫ.gɛ.rɛm → ˈfoɫ.gɛ.rɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈfoɫ.gɛ.rɛ → ˈfoɫ.gʲɛ.rɛ   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˈfoɫ.gʲɛ.rɛ → ˈfoɫ.ɟɛ.rɛ   (gʲ→ɟ)
500: ŋ/ɫ/s palatalize before a complex palatal-triggering sequence
    ˈfoɫ.ɟɛ.rɛ → ˈfolʲ.ɟɛ.rɛ   (ɫ→lʲ)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈfolʲ.ɟɛ.rɛ → ˈfolʲ.ɟrɛ   (ɛ→∅)
500: a palatal stop becomes a dental fricative before a non-front consonant
    ˈfolʲ.ɟrɛ → ˈfolʲ.d̪rɛ   (ɟ→d̪)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈfolʲ.d̪rɛ → ˈfolʲ.d̪ʲrɛ   (d̪→d̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfolʲ.d̪ʲrɛ → ˈfolʲ.d̪ʲrə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈfolʲ.d̪ʲrə → ˈfolʲd̪ʲrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfolʲd̪ʲrə̯ → ˈfolʲd̪ʲr   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈfolʲd̪ʲr → ˈfolʲ.d̪ʲrə   (∅→ə)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈfolʲ.d̪ʲrə → ˈfolʲ.d̪ʲrʲə   (r→rʲ)
600: palatalized r depalatalizes
    ˈfolʲ.d̪ʲrʲə → ˈfolʲ.d̪ʲrə   (rʲ→r)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈfolʲ.d̪ʲrə → ˈfolʲj.d̪rə   (d̪ʲ→jd̪)
600: j is lost after j or a consonant, before a consonant
    ˈfolʲj.d̪rə → ˈfolʲ.d̪rə   (j→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈfolʲ.d̪rə → ˈfoɫ.d̪rə   (lʲ→ɫ)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈfoɫ.d̪rə → ˈfuɫ.d̪rə   (ˈo→ˈu)
1000: back dark-l variants vocalize to w
    ˈfuɫ.d̪rə → ˈfuw.d̪rə   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˈfuw.d̪rə → ˈfu.d̪rə   (w→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈfu.d̪rə → ˈfud̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈfud̪rə̯ → ˈfud̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈfud̪r → ˈfud̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈfud̪ʀ → fud̪ʀ   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    fud̪ʀ → fud̪ʁ   (ʀ→ʁ)
```

## fous

`fˈolleːs` → `fu`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfol.leːs → ˈfɔl.leːs   (ˈo→ˈɔ)
-100: the length feature is dropped now that quality carries the contrast
    ˈfɔl.leːs → ˈfɔl.les   (eː→e)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfɔl.les → ˈfɔl.ləs   (e→ə)
600: schwa becomes non-syllabic
    ˈfɔl.ləs → ˈfɔllə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfɔllə̯s → ˈfɔlls   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˈfɔlls → ˈfɔls   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈfɔls → ˈfɔɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˈfɔɫs → ˈfɔws   (ɫ→w)
1200: the ow diphthong monophthongizes to u
    ˈfɔws → ˈfus   (ˈɔw→ˈu)
1400: final obstruents are lost
    ˈfus → ˈfu   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfu → fu   (ˈu→u)
```

## frayer

`frˌikˈɑːre` → `ʒɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfriˈkɑː.re → ˌfrɪˈkɑː.rɛ   (ˌi→ˌɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfrɪˈkɑː.rɛ → ˌfrɪˈkɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌfrɪˈkɑ.rɛ → ˌfreˈkɑ.rɛ   (ˌɪ→ˌe)
300: a stressed vowel lengthens before a single consonant + glide
    ˌfreˈkɑ.rɛ → ˌfreˈkɑː.rɛ   (ˈɑ→ˈɑː)
500: k voices to g intervocalically
    ˌfreˈkɑː.rɛ → ˌfreˈgɑː.rɛ   (k→g)
500: e lost in -ica- endings before the now-voiced g + low vowel
    ˌfreˈgɑː.rɛ → ˈfrgɑː.rɛ   (ˌe→∅)
500: the low vowel fronts by default
    ˈfrgɑː.rɛ → ˈfrgaː.rɛ   (ˈɑː→ˈaː)
500: the high back consonant w fronts before a front vowel
    ˈfrgaː.rɛ → ˈfrgʲaː.rɛ   (g→gʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈfrgʲaː.rɛ → ˈfrɟaː.rɛ   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈfrɟaː.rɛ → ˈfrd͡ʒaː.rɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈfrd͡ʒaː.rɛ → ˈfrd͡ʒaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈfrd͡ʒaː.rə → ˈfrd͡ʒaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈfrd͡ʒaːrə̯ → ˈfrd͡ʒaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈfrd͡ʒaːr → ˈfrd͡ʒae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈfrd͡ʒae̯r → ˈfrd͡ʒeːr   (ˈae̯→ˈeː)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈfrd͡ʒeːr → ˈfd͡ʒeːr   (r→∅)
750: a non-nasal non-round labial assimilates to a following voiced coronal stop
    ˈfd͡ʒeːr → ˈd̪d͡ʒeːr   (f→d̪)
750: a dental stop deletes before another coronal stop
    ˈd̪d͡ʒeːr → ˈd͡ʒeːr   (d̪→∅)
1000: vowel length resets to short
    ˈd͡ʒeːr → ˈd͡ʒer   (ˈeː→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒer → ˈʒer   (d͡ʒ→ʒ)
1400: e/ø lax before an r that closes the syllable
    ˈʒer → ˈʒɛr   (ˈe→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈʒɛr → ˈʒɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈʒɛɹ → ˈʒɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈʒɛr → ˈʒɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒɛʀ → ʒɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʒɛʀ → ʒɛʁ   (ʀ→ʁ)
```

## fumer

`fˌuːmˈɑːre` → `fy.me`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfuːˈmɑː.re → ˌfuːˈmɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfuːˈmɑː.rɛ → ˌfuˈmɑ.rɛ   (ˌuː→ˌu, ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌfuˈmɑ.rɛ → ˌfuˈmɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌfuˈmɑː.rɛ → ˌfuˈmaː.rɛ   (ˈɑː→ˈaː)
500: a high tense round non-nasal vowel centralizes
    ˌfuˈmaː.rɛ → ˌfʉˈmaː.rɛ   (ˌu→ˌʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌfʉˈmaː.rɛ → ˌfʉˈmaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌfʉˈmaː.rə → ˌfʉˈmaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌfʉˈmaːrə̯ → ˌfʉˈmaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌfʉˈmaːr → ˌfʉˈmae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌfʉˈmae̯r → ˌfʉˈmeːr   (ˈae̯→ˈeː)
1000: high round back vowels front (completion of u-fronting)
    ˌfʉˈmeːr → ˌfyˈmeːr   (ˌʉ→ˌy)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌfyˈmeːr → ˌfỹˈmeːr   (ˌy→ˌỹ)
1000: vowel length resets to short
    ˌfỹˈmeːr → ˌfỹˈmer   (ˈeː→ˈe)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌfỹˈmer → ˌfyˈmer   (ˌỹ→ˌy)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌfyˈmer → ˌfyˈmeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌfyˈmeɹ → ˌfyˈme   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌfyˈme → fy.me   (ˌy→y, ˈe→e)
```

## fumier

`fˌimˈɑːrium` → `fə.mje`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌfiˈmɑː.ri.um → ˌfɪˈmɑː.rɪ.ʊm   (ˌi→ˌɪ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌfɪˈmɑː.rɪ.ʊm → ˌfɪˈmɑː.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌfɪˈmɑː.rjʊm → ˌfɪˈmɑːr.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌfɪˈmɑːr.ʝʊm → ˌfɪˈmɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌfɪˈmɑr.ʝʊm → ˌfeˈmɑr.ʝom   (ˌɪ→ˌe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌfeˈmɑr.ʝom → ˌfeˈmɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌfeˈmɑr.ʝo → ˌfeˈmɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌfeˈmɑ.rʲo → ˌfeˈma.rʲo   (ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌfeˈma.rʲo → ˌfeˈmaː.rʲo   (ˈa→ˈaː)
600: aːrʲ metathesizes to jɛːr
    ˌfeˈmaː.rʲo → ˌfeˈmjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌfeˈmjɛː.ro → ˌfeˈmjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌfeˈmjɛː.rə → ˌfeˈmjɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌfeˈmjɛːrə̯ → ˌfeˈmjɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌfeˈmjɛːr → ˌfeˈmjie̯r   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌfeˈmjie̯r → ˌfeˈmie̯r   (j→∅)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌfeˈmie̯r → ˌfəˈmie̯r   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌfəˈmie̯r → ˌfə̃ˈmie̯r   (ˌə→ˌə̃)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌfə̃ˈmie̯r → ˌfə̃ˈmjer   (ˈi→j, e̯→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌfə̃ˈmjer → ˌfə̃ˈmjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌfə̃ˈmjeɹ → ˌfə̃ˈmje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌfə̃ˈmje → fə̃.mje   (ˌə̃→ə̃, ˈe→e)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    fə̃.mje → fə.mje   (ə̃→ə)
```

## fête

`fˈest̪ɑm` → `fɛt̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈfes.t̪ɑm → ˈfɛs.t̪ɑm   (ˈe→ˈɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈfɛs.t̪ɑm → ˈfɛs.t̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈfɛs.t̪ɑ → ˈfɛs.t̪a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfɛs.t̪a → ˈfɛs.t̪ə   (a→ə)
1000: s becomes x after a vowel, before any consonant
    ˈfɛs.t̪ə → ˈfɛx.t̪ə   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈfɛx.t̪ə → ˈfɛː.t̪ə   (ˈɛx→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˈfɛː.t̪ə → ˈfɛːt̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈfɛːt̪ə̯ → ˈfɛːt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈfɛːt̪ → fɛːt̪   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    fɛːt̪ → fɛt̪   (ɛː→ɛ)
```

## gent

`gˈen̪t̪em` → `ʒɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgen̪.t̪em → ˈgɛn̪.t̪ɛm   (ˈe→ˈɛ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgɛn̪.t̪ɛm → ˈgɛn̪.t̪ɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈgɛn̪.t̪ɛ → ˈgʲɛn̪.t̪ɛ   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˈgʲɛn̪.t̪ɛ → ˈɟɛn̪.t̪ɛ   (gʲ→ɟ)
500: a palatal stop affricates
    ˈɟɛn̪.t̪ɛ → ˈd͡ʒɛn̪.t̪ɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd͡ʒɛn̪.t̪ɛ → ˈd͡ʒɛn̪.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈd͡ʒɛn̪.t̪ə → ˈd͡ʒɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd͡ʒɛn̪t̪ə̯ → ˈd͡ʒɛn̪t̪   (ə̯→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈd͡ʒɛn̪t̪ → ˈd͡ʒɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈd͡ʒɛ̃n̪t̪ → ˈd͡ʒãn̪t̪   (ˈɛ̃→ˈã)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒãn̪t̪ → ˈʒãn̪t̪   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈʒãn̪t̪ → ˈʒãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈʒãːt̪ → ˈʒɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈʒɑ̃ːt̪ → ˈʒɑ̃ː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒɑ̃ː → ʒɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ʒɑ̃ː → ʒɑ̃   (ɑ̃ː→ɑ̃)
```

## git

`iˈɑket̪` → `ʒis`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    iˈɑ.ket̪ → ɪˈɑ.kɛt̪   (i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ɪˈɑ.kɛt̪ → ˈjɑ.kɛt̪   (ɪ→j)
-100: yod strengthens before a vowel
    ˈjɑ.kɛt̪ → ˈʝɑ.kɛt̪   (j→ʝ)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈʝɑ.kɛt̪ → ˈʝɑ.kʲɛt̪   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈʝɑ.kʲɛt̪ → ˈʝɑ.cɛt̪   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˈʝɑ.cɛt̪ → ˈʝɑː.cɛt̪   (ˈɑ→ˈɑː)
500: a palatal stop affricates
    ˈʝɑː.cɛt̪ → ˈʝɑː.t͡sʲɛt̪   (c→t͡sʲ)
500: the low vowel fronts by default
    ˈʝɑː.t͡sʲɛt̪ → ˈʝaː.t͡sʲɛt̪   (ˈɑː→ˈaː)
500: long stressed aː becomes ɛː word-initially after a front consonant
    ˈʝaː.t͡sʲɛt̪ → ˈʝɛː.t͡sʲɛt̪   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˈʝɛː.t͡sʲɛt̪ → ˈʝie̯.t͡sʲɛt̪   (ˈɛː→ˈie̯)
600: t/d spirantize word-finally after a vowel
    ˈʝie̯.t͡sʲɛt̪ → ˈʝie̯.t͡sʲɛθ   (t̪→θ)
600: yod hardens to ɟ word-initially before a vowel
    ˈʝie̯.t͡sʲɛθ → ˈɟie̯.t͡sʲɛθ   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟie̯.t͡sʲɛθ → ˈd͡ʒie̯.t͡sʲɛθ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd͡ʒie̯.t͡sʲɛθ → ˈd͡ʒie̯.t͡sʲəθ   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈd͡ʒie̯.t͡sʲəθ → ˈd͡ʒie̯t͡sʲə̯θ   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd͡ʒie̯t͡sʲə̯θ → ˈd͡ʒie̯t͡sʲθ   (ə̯→∅)
600: a dental fricative hardens to a stop after a consonant, word-finally
    ˈd͡ʒie̯t͡sʲθ → ˈd͡ʒie̯t͡sʲt̪   (θ→t̪)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈd͡ʒie̯t͡sʲt̪ → ˈd͡ʒie̯t͡sʲt̪ʲ   (t̪→t̪ʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈd͡ʒie̯t͡sʲt̪ʲ → ˈd͡ʒie̯t͡sʲjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈd͡ʒie̯t͡sʲjt̪ → ˈd͡ʒie̯t͡sʲt̪   (j→∅)
600: j epenthesized after the e-glide before tsʲ
    ˈd͡ʒie̯t͡sʲt̪ → ˈd͡ʒie̯jt͡sʲt̪   (∅→j)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈd͡ʒie̯jt͡sʲt̪ → ˈd͡ʒijt͡sʲt̪   (e̯→∅)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒijt͡sʲt̪ → ˈʒijsʲt̪   (d͡ʒ→ʒ, t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈʒijsʲt̪ → ˈʒijst̪   (sʲ→s)
1400: final obstruents are lost
    ˈʒijst̪ → ˈʒijs   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒijs → ʒijs   (ˈi→i)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    ʒijs → ʒis   (j→∅)
```

## goutte

`gˈut̪t̪ɑm` → `gut̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgut̪.t̪ɑm → ˈgʊt̪.t̪ɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈgʊt̪.t̪ɑm → ˈgot̪.t̪ɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgot̪.t̪ɑm → ˈgot̪.t̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈgot̪.t̪ɑ → ˈgot̪.t̪a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈgot̪.t̪a → ˈgot̪.t̪ə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈgot̪.t̪ə → ˈgo.t̪ə   (t̪→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈgo.t̪ə → ˈgu.t̪ə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈgu.t̪ə → ˈgut̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈgut̪ə̯ → ˈgut̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈgut̪ → gut̪   (ˈu→u)
```

## goût

`gˈust̪um` → `gu`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgus.t̪um → ˈgʊs.t̪ʊm   (ˈu→ˈʊ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈgʊs.t̪ʊm → ˈgos.t̪om   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgos.t̪om → ˈgos.t̪o   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈgos.t̪o → ˈgos.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈgos.t̪ə → ˈgost̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈgost̪ə̯ → ˈgost̪   (ə̯→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈgost̪ → ˈgust̪   (ˈo→ˈu)
1000: s becomes x after a vowel, before any consonant
    ˈgust̪ → ˈguxt̪   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈguxt̪ → ˈguːt̪   (ˈux→ˈuː)
1400: final obstruents are lost
    ˈguːt̪ → ˈguː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈguː → guː   (ˈuː→uː)
1400: distinctive vowel length is lost entirely
    guː → gu   (uː→u)
```

## gré

`grˈɑːt̪um` → `gʁe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgrɑː.t̪um → ˈgrɑː.t̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈgrɑː.t̪ʊm → ˈgrɑ.t̪ʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˈgrɑ.t̪ʊm → ˈgrɑ.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgrɑ.t̪om → ˈgrɑ.t̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈgrɑ.t̪o → ˈgrɑː.t̪o   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈgrɑː.t̪o → ˈgraː.t̪o   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈgraː.t̪o → ˈgraː.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈgraː.t̪ə → ˈgraːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈgraːt̪ə̯ → ˈgraːt̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈgraːt̪ → ˈgrae̯t̪   (ˈaː→ˈae̯)
750: a word-final stop re-opens to a fricative after a vowel
    ˈgrae̯t̪ → ˈgrae̯θ   (t̪→θ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈgrae̯θ → ˈgreːθ   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈgreːθ → ˈgreθ   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˈgreθ → ˈgre   (θ→∅)
1400: r becomes uvular ʀ
    ˈgre → ˈgʀe   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈgʀe → gʀe   (ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    gʀe → gʁe   (ʀ→ʁ)
```

## hier

`hˈeri` → `jɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈhe.ri → ˈhɛ.rɪ   (ˈe→ˈɛ, i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈhɛ.rɪ → ˈhɛ.re   (ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˈhɛ.re → ˈhɛː.re   (ˈɛ→ˈɛː)
500: h lost unconditionally (any remaining h)
    ˈhɛː.re → ˈɛː.re   (h→∅)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈɛː.re → ˈie̯.re   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈie̯.re → ˈie̯.rə   (e→ə)
600: schwa becomes non-syllabic
    ˈie̯.rə → ˈie̯rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈie̯rə̯ → ˈie̯r   (ə̯→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈie̯r → ˈjer   (ˈi→j, e̯→ˈe)
1400: e/ø lax before an r that closes the syllable
    ˈjer → ˈjɛr   (ˈe→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈjɛr → ˈjɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈjɛɹ → ˈjɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈjɛr → ˈjɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈjɛʀ → jɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    jɛʀ → jɛʁ   (ʀ→ʁ)
```

## hiver

`hˌiːbˈern̪um` → `i.vɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌhiːˈber.n̪um → ˌhiːˈbɛr.n̪ʊm   (ˈe→ˈɛ, u→ʊ)
-100: b lenites to β intervocalically / before a sonorant
    ˌhiːˈbɛr.n̪ʊm → ˌhiːˈβɛr.n̪ʊm   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌhiːˈβɛr.n̪ʊm → ˌhiˈβɛr.n̪ʊm   (ˌiː→ˌi)
-100: lax high vowels lower to tense mid vowels
    ˌhiˈβɛr.n̪ʊm → ˌhiˈβɛr.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌhiˈβɛr.n̪om → ˌhiˈβɛr.n̪o   (m→∅)
500: h lost unconditionally (any remaining h)
    ˌhiˈβɛr.n̪o → ˌiˈβɛr.n̪o   (h→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌiˈβɛr.n̪o → ˌiˈβɛr.n̪ə   (o→ə)
600: n becomes a tap between r(+schwa) and schwa
    ˌiˈβɛr.n̪ə → ˌiˈβɛr.ɾə   (n̪→ɾ)
600: schwa becomes non-syllabic
    ˌiˈβɛr.ɾə → ˌiˈβɛrɾə̯   (ə→ə̯)
600: tap + non-syllabic schwa becomes r after a front non-low vowel (+ optional r)
    ˌiˈβɛrɾə̯ → ˌiˈβɛrr   (ɾə̯→r)
600: the remaining bilabial fricative becomes v
    ˌiˈβɛrr → ˌiˈvɛrr   (β→v)
750: a word-final rr degeminates
    ˌiˈvɛrr → ˌiˈvɛr   (r→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌiˈvɛr → ˌiˈvɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌiˈvɛɹ → ˌiˈvɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌiˈvɛr → ˌiˈvɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌiˈvɛʀ → i.vɛʀ   (ˌi→i, ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    i.vɛʀ → i.vɛʁ   (ʀ→ʁ)
```

## honneur

`hˌon̪ˈoːrem` → `ɔ.n̪œʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌhoˈn̪oː.rem → ˌhɔˈn̪oː.rɛm   (ˌo→ˌɔ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌhɔˈn̪oː.rɛm → ˌhɔˈn̪o.rɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌhɔˈn̪o.rɛm → ˌhɔˈn̪o.rɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌhɔˈn̪o.rɛ → ˌhɔˈn̪oː.rɛ   (ˈo→ˈoː)
500: h lost unconditionally (any remaining h)
    ˌhɔˈn̪oː.rɛ → ˌɔˈn̪oː.rɛ   (h→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌɔˈn̪oː.rɛ → ˌũˈn̪oː.rɛ   (ˌɔ→ˌũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌũˈn̪oː.rɛ → ˌũˈn̪oː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌũˈn̪oː.rə → ˌũˈn̪oːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌũˈn̪oːrə̯ → ˌũˈn̪oːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌũˈn̪oːr → ˌũˈn̪owr   (ˈoː→ˈow)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˌũˈn̪owr → ˌũˈn̪ør   (ˈow→ˈø)
1400: e/ø lax before an r that closes the syllable
    ˌũˈn̪ør → ˌũˈn̪œr   (ˈø→ˈœ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌũˈn̪œr → ˌũˈn̪œɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌũˈn̪œɹ → ˌũˈn̪œr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌũˈn̪œr → ˌũˈn̪œʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌũˈn̪œʀ → ũ.n̪œʀ   (ˌũ→ũ, ˈœ→œ)
1400: nasal ũ opens to ɔ̃
    ũ.n̪œʀ → ɔ̃.n̪œʀ   (ũ→ɔ̃)
1400: ɔ̃ (and œ̃) denasalizes in an open syllable before a nasal consonant
    ɔ̃.n̪œʀ → ɔ.n̪œʀ   (ɔ̃→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ɔ.n̪œʀ → ɔ.n̪œʁ   (ʀ→ʁ)
```

## hui

`hˈod̪ieː` → `ɥi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈho.d̪i.eː → ˈhɔ.d̪ɪ.eː   (ˈo→ˈɔ, i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈhɔ.d̪ɪ.eː → ˈhɔ.d̪jeː   (ɪ→j)
-100: yod strengthens before a vowel
    ˈhɔ.d̪jeː → ˈhɔ.d̪ʝeː   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈhɔ.d̪ʝeː → ˈhɔ.d̪ʝe   (eː→e)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈhɔ.d̪ʝe → ˈhɔ.ɟʝe   (d̪→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈhɔ.ɟʝe → ˈhɔʝ.ʝe   (ɟ→ʝ)
500: h lost unconditionally (any remaining h)
    ˈhɔʝ.ʝe → ˈɔʝ.ʝe   (h→∅)
500: yod degeminates (lost before another yod)
    ˈɔʝ.ʝe → ˈɔ.ʝe   (ʝ→∅)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˈɔ.ʝe → ˈɔː.ʝe   (ˈɔ→ˈɔː)
500: long stressed ɛː/ɔː diphthongize (recurrence)
    ˈɔː.ʝe → ˈuo̯.ʝe   (ˈɔː→ˈuo̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈuo̯.ʝe → ˈuo̯.ʝə   (e→ə)
600: schwa becomes non-syllabic
    ˈuo̯.ʝə → ˈuo̯ʝə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈuo̯ʝə̯ → ˈuo̯ʝ   (ə̯→∅)
600: ʝ weakens to j before optional consonants + word end
    ˈuo̯ʝ → ˈuo̯j   (ʝ→j)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈuo̯j → ˈʉo̯j   (ˈu→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈʉo̯j → ˈyo̯j   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈyo̯j → ˈye̯j   (o̯→e̯)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈye̯j → ˈyj   (e̯→∅)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˈyj → ˈɥi   (ˈy→ɥ, j→ˈi)
1400: stress is leveled — no longer distinctive for vowels
    ˈɥi → ɥi   (ˈi→i)
```

## huisser

`ˌuːst̪iˈɑːrium` → `ɥi.se`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌuːs.t̪iˈɑː.ri.um → ˌuːs.t̪ɪˈɑː.rɪ.ʊm   (i→ɪ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌuːs.t̪ɪˈɑː.rɪ.ʊm → ˌuːsˈt̪jɑː.rjʊm   (ɪ→j, ɪ→j)
-100: yod strengthens before a vowel
    ˌuːsˈt̪jɑː.rjʊm → ˌuːsˈt̪ʝɑːr.ʝʊm   (j→ʝ, j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌuːsˈt̪ʝɑːr.ʝʊm → ˌusˈt̪ʝɑr.ʝʊm   (ˌuː→ˌu, ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌusˈt̪ʝɑr.ʝʊm → ˌusˈt̪ʝɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌusˈt̪ʝɑr.ʝom → ˌusˈt̪ʝɑr.ʝo   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌusˈt̪ʝɑr.ʝo → ˌust͡sʲˈʝɑr.ʝo   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌust͡sʲˈʝɑr.ʝo → ˌusˈt͡sʲɑr.ʝo   (ʝ→∅)
500: r + yod becomes palatalized r
    ˌusˈt͡sʲɑr.ʝo → ˌusˈt͡sʲɑ.rʲo   (rʝ→rʲ)
500: s + high-front consonant becomes geminate palatalized s
    ˌusˈt͡sʲɑ.rʲo → ˌusʲˈsʲɑ.rʲo   (s→sʲ, t͡sʲ→sʲ)
500: the low vowel fronts by default
    ˌusʲˈsʲɑ.rʲo → ˌusʲˈsʲa.rʲo   (ˈɑ→ˈa)
500: a high tense round non-nasal vowel centralizes
    ˌusʲˈsʲa.rʲo → ˌʉsʲˈsʲa.rʲo   (ˌu→ˌʉ)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌʉsʲˈsʲa.rʲo → ˌʉsʲˈsʲaː.rʲo   (ˈa→ˈaː)
600: aːrʲ metathesizes to jɛːr
    ˌʉsʲˈsʲaː.rʲo → ˌʉsʲˈsʲjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌʉsʲˈsʲjɛː.ro → ˌʉsʲˈsʲjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌʉsʲˈsʲjɛː.rə → ˌʉsʲˈsʲjɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌʉsʲˈsʲjɛːrə̯ → ˌʉsʲˈsʲjɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌʉsʲˈsʲjɛːr → ˌʉsʲˈsʲjie̯r   (ˈɛː→ˈie̯)
600: geminate palatalized s degeminates
    ˌʉsʲˈsʲjie̯r → ˌʉˈsʲjie̯r   (sʲ→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌʉˈsʲjie̯r → ˌʉjˈsjie̯r   (sʲ→js)
600: a coronal palatalizes between two high-front segments
    ˌʉjˈsjie̯r → ˌʉjˈsʲjie̯r   (s→sʲ)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌʉjˈsʲjie̯r → ˌʉjˈsʲie̯r   (j→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌʉjˈsʲie̯r → ˌyjˈsʲie̯r   (ˌʉ→ˌy)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌyjˈsʲie̯r → ˌyjˈsʲjer   (ˈi→j, e̯→ˈe)
1200: je becomes e after a palatal consonant
    ˌyjˈsʲjer → ˌyjˈsʲer   (j→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌyjˈsʲer → ˌyjˈser   (sʲ→s)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˌyjˈser → ˌɥiˈser   (ˌy→ɥ, j→ˌi)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌɥiˈser → ˌɥiˈseɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌɥiˈseɹ → ˌɥiˈse   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌɥiˈse → ɥi.se   (ˌi→i, ˈe→e)
```

## ja

`iˈɑm` → `ʒjɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    iˈɑm → ɪˈɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ɪˈɑm → ˈjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈjɑm → ˈʝɑm   (j→ʝ)
300: a stressed vowel lengthens in a monosyllable before a final consonant
    ˈʝɑm → ˈʝɑːm   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈʝɑːm → ˈʝaːm   (ˈɑː→ˈaː)
500: long stressed aː becomes ɛː word-initially after a front consonant
    ˈʝaːm → ˈʝɛːm   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˈʝɛːm → ˈʝie̯m   (ˈɛː→ˈie̯)
600: yod hardens to ɟ word-initially before a vowel
    ˈʝie̯m → ˈɟie̯m   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟie̯m → ˈd͡ʒie̯m   (ɟ→d͡ʒ)
1000: final m dentalizes after a vowel
    ˈd͡ʒie̯m → ˈd͡ʒie̯n̪   (m→n̪)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈd͡ʒie̯n̪ → ˈd͡ʒjen̪   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒjen̪ → ˈʒjen̪   (d͡ʒ→ʒ)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈʒjen̪ → ˈʒjẽn̪   (ˈe→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈʒjẽn̪ → ˈʒjẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈʒjẽː → ˈʒjɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒjɛ̃ː → ʒjɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    ʒjɛ̃ː → ʒjɛ̃   (ɛ̃ː→ɛ̃)
```

## jaune

`gˈɑlbin̪um` → `ʒon̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈgɑl.bi.n̪um → ˈgɑl.bɪ.n̪ʊm   (i→ɪ, u→ʊ)
-100: l darkens before a non-lateral consonant
    ˈgɑl.bɪ.n̪ʊm → ˈgɑɫ.bɪ.n̪ʊm   (l→ɫ)
-100: lax high vowels lower to tense mid vowels
    ˈgɑɫ.bɪ.n̪ʊm → ˈgɑɫ.be.n̪om   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈgɑɫ.be.n̪om → ˈgɑɫ.be.n̪o   (m→∅)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈgɑɫ.be.n̪o → ˈgɑɫ.bn̪o   (e→∅)
500: the low vowel fronts by default
    ˈgɑɫ.bn̪o → ˈgaɫ.bn̪o   (ˈɑ→ˈa)
500: the high back consonant w fronts before a front vowel
    ˈgaɫ.bn̪o → ˈgʲaɫ.bn̪o   (g→gʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈgʲaɫ.bn̪o → ˈɟaɫ.bn̪o   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟaɫ.bn̪o → ˈd͡ʒaɫ.bn̪o   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd͡ʒaɫ.bn̪o → ˈd͡ʒaɫ.bn̪ə   (o→ə)
600: a labial consonant is lost between a consonant and a nasal consonant
    ˈd͡ʒaɫ.bn̪ə → ˈd͡ʒaɫ.n̪ə   (b→∅)
600: schwa becomes non-syllabic
    ˈd͡ʒaɫ.n̪ə → ˈd͡ʒaɫn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd͡ʒaɫn̪ə̯ → ˈd͡ʒaɫn̪   (ə̯→∅)
600: schwa epenthesized after a non-nasal consonant + nasal consonant, word-finally
    ˈd͡ʒaɫn̪ → ˈd͡ʒaɫ.n̪ə   (∅→ə)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈd͡ʒaɫ.n̪ə → ˈd͡ʒaɫ.n̪ʲə   (n̪→n̪ʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈd͡ʒaɫ.n̪ʲə → ˈd͡ʒaɫj.n̪ə   (n̪ʲ→jn̪)
600: j is lost after j or a consonant, before a consonant
    ˈd͡ʒaɫj.n̪ə → ˈd͡ʒaɫ.n̪ə   (j→∅)
1000: back dark-l variants vocalize to w
    ˈd͡ʒaɫ.n̪ə → ˈd͡ʒaw.n̪ə   (ɫ→w)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒaw.n̪ə → ˈʒaw.n̪ə   (d͡ʒ→ʒ)
1200: aw becomes long oː
    ˈʒaw.n̪ə → ˈʒoː.n̪ə   (ˈaw→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˈʒoː.n̪ə → ˈʒoːn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʒoːn̪ə̯ → ˈʒoːn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒoːn̪ → ʒoːn̪   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    ʒoːn̪ → ʒon̪   (oː→o)
```

## jour

`d̪iˈurn̪um` → `ʒuʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    d̪iˈur.n̪um → d̪ɪˈʊr.n̪ʊm   (i→ɪ, ˈu→ˈʊ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    d̪ɪˈʊr.n̪ʊm → ˈd̪jʊr.n̪ʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈd̪jʊr.n̪ʊm → ˈd̪ʝʊr.n̪ʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈd̪ʝʊr.n̪ʊm → ˈd̪ʝor.n̪om   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈd̪ʝor.n̪om → ˈd̪ʝor.n̪o   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈd̪ʝor.n̪o → ˈɟʝor.n̪o   (d̪→ɟ)
300: yod absorbed into a preceding palatalized consonant
    ˈɟʝor.n̪o → ˈɟor.n̪o   (ʝ→∅)
500: a palatal stop affricates
    ˈɟor.n̪o → ˈd͡ʒor.n̪o   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd͡ʒor.n̪o → ˈd͡ʒor.n̪ə   (o→ə)
600: n becomes a tap between r(+schwa) and schwa
    ˈd͡ʒor.n̪ə → ˈd͡ʒor.ɾə   (n̪→ɾ)
600: schwa becomes non-syllabic
    ˈd͡ʒor.ɾə → ˈd͡ʒorɾə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈd͡ʒorɾə̯ → ˈd͡ʒorɾ   (ə̯→∅)
600: a tap hardens to the trill
    ˈd͡ʒorɾ → ˈd͡ʒorr   (ɾ→r)
750: a word-final rr degeminates
    ˈd͡ʒorr → ˈd͡ʒor   (r→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈd͡ʒor → ˈd͡ʒur   (ˈo→ˈu)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒur → ˈʒur   (d͡ʒ→ʒ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈʒur → ˈʒuɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈʒuɹ → ˈʒur   (ɹ→r)
1400: r becomes uvular ʀ
    ˈʒur → ˈʒuʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒuʀ → ʒuʀ   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʒuʀ → ʒuʁ   (ʀ→ʁ)
```

## laisser

`lˌɑksˈɑːre` → `lɛ.se`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌlɑˈksɑː.re → ˌlɑˈksɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌlɑˈksɑː.rɛ → ˌlɑˈksɑ.rɛ   (ˈɑː→ˈɑ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˌlɑˈksɑ.rɛ → ˌlɑxˈsɑ.rɛ   (k→x)
300: a stressed vowel lengthens before a single consonant + glide
    ˌlɑxˈsɑ.rɛ → ˌlɑxˈsɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌlɑxˈsɑː.rɛ → ˌlaxˈsaː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌlaxˈsaː.rɛ → ˌlaçˈsaː.rɛ   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌlaçˈsaː.rɛ → ˌlaçˈsʲaː.rɛ   (s→sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌlaçˈsʲaː.rɛ → ˌlaçˈsʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌlaçˈsʲaː.rə → ˌlaçˈsʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌlaçˈsʲaːrə̯ → ˌlaçˈsʲaːr   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌlaçˈsʲaːr → ˌlaçˈsʲɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌlaçˈsʲɛːr → ˌlaçˈsʲie̯r   (ˈɛː→ˈie̯)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌlaçˈsʲie̯r → ˌlaçjˈsie̯r   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˌlaçjˈsie̯r → ˌlaçˈsie̯r   (j→∅)
600: a coronal palatalizes between two high-front segments
    ˌlaçˈsie̯r → ˌlaçˈsʲie̯r   (s→sʲ)
750: ç merges into ʝ
    ˌlaçˈsʲie̯r → ˌlaʝˈsʲie̯r   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌlaʝˈsʲie̯r → ˌlajˈsʲie̯r   (ʝ→j)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌlajˈsʲie̯r → ˌlajˈsʲjer   (ˈi→j, e̯→ˈe)
1200: je becomes e after a palatal consonant
    ˌlajˈsʲjer → ˌlajˈsʲer   (j→∅)
1200: the remaining anterior palatalized consonants depalatalize
    ˌlajˈsʲer → ˌlajˈser   (sʲ→s)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌlajˈser → ˌlɛːˈser   (ˌaj→ˌɛː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌlɛːˈser → ˌlɛːˈseɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌlɛːˈseɹ → ˌlɛːˈse   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌlɛːˈse → lɛː.se   (ˌɛː→ɛː, ˈe→e)
1400: distinctive vowel length is lost entirely
    lɛː.se → lɛ.se   (ɛː→ɛ)
```

## lame

`lˈɑmin̪ɑm` → `lam`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlɑ.mi.n̪ɑm → ˈlɑ.mɪ.n̪ɑm   (i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈlɑ.mɪ.n̪ɑm → ˈlɑ.me.n̪ɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɑ.me.n̪ɑm → ˈlɑ.me.n̪ɑ   (m→∅)
300: e deleted after a non-nasal + non-syllabic sequence, before a distributed consonant + non-primary-stressed vowel
    ˈlɑ.me.n̪ɑ → ˈlɑm.n̪ɑ   (e→∅)
500: the low vowel fronts by default
    ˈlɑm.n̪ɑ → ˈlam.n̪a   (ˈɑ→ˈa, ɑ→a)
600: n becomes m before m (recurrence)
    ˈlam.n̪a → ˈlam.ma   (n̪→m)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlam.ma → ˈlam.mə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈlam.mə → ˈla.mə   (m→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈla.mə → ˈlã.mə   (ˈa→ˈã)
1400: final ə becomes a non-syllabic off-glide
    ˈlã.mə → ˈlãmə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlãmə̯ → ˈlãm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlãm → lãm   (ˈã→ã)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    lãm → lam   (ã→a)
```

## larme

`lˈɑkrimɑm` → `lɛm`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlɑ.kri.mɑm → ˈlɑ.krɪ.mɑm   (i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈlɑ.krɪ.mɑm → ˈlɑ.kre.mɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɑ.kre.mɑm → ˈlɑ.kre.mɑ   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈlɑ.kre.mɑ → ˈlɑː.kre.mɑ   (ˈɑ→ˈɑː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˈlɑː.kre.mɑ → ˈlɑː.xre.mɑ   (k→x)
500: a vowel shortens before a consonant cluster
    ˈlɑː.xre.mɑ → ˈlɑ.xre.mɑ   (ˈɑː→ˈɑ)
500: the low vowel fronts by default
    ˈlɑ.xre.mɑ → ˈla.xre.ma   (ˈɑ→ˈa, ɑ→a)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈla.xre.ma → ˈla.çre.ma   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈla.çre.ma → ˈla.çrʲe.ma   (r→rʲ)
600: yod lost before ʎ or palatalized r
    ˈla.çrʲe.ma → ˈla.rʲe.ma   (ç→∅)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈla.rʲe.ma → ˈla.rʲə.ma   (e→ə)
600: schwa becomes non-syllabic
    ˈla.rʲə.ma → ˈlarʲə̯.ma   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈlarʲə̯.ma → ˈlarʲ.ma   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˈlarʲ.ma → ˈlajrʲ.ma   (∅→j)
600: a stressed vowel lengthens before j + optional consonants + a high-front coronal
    ˈlajrʲ.ma → ˈlaːjrʲ.ma   (ˈa→ˈaː)
600: palatalized r depalatalizes
    ˈlaːjrʲ.ma → ˈlaːjr.ma   (rʲ→r)
600: long stressed vowels diphthongize
    ˈlaːjr.ma → ˈlae̯jr.ma   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˈlae̯jr.ma → ˈlajr.ma   (e̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlajr.ma → ˈlajr.mə   (a→ə)
750: a medial consonant/glide is lost between two consonants, before a nasal
    ˈlajr.mə → ˈlaj.mə   (r→∅)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˈlaj.mə → ˈlaj̃.mə   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈlaj̃.mə → ˈlãj̃.mə   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈlãj̃.mə → ˈlɛ̃j̃.mə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈlɛ̃j̃.mə → ˈlɛ̃.mə   (j̃→∅)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈlɛ̃.mə → ˈlɛ.mə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈlɛ.mə → ˈlɛmə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlɛmə̯ → ˈlɛm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlɛm → lɛm   (ˈɛ→ɛ)
```

## laver

`lˌɑwˈɑːrɛ` → `la.ve`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌlɑˈwɑː.rɛ → ˌlɑˈɣʷɑː.rɛ   (w→ɣʷ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌlɑˈɣʷɑː.rɛ → ˌlɑˈβʷɑː.rɛ   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌlɑˈβʷɑː.rɛ → ˌlɑˈβʷɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌlɑˈβʷɑ.rɛ → ˌlɑˈβʷɑː.rɛ   (ˈɑ→ˈɑː)
500: labialized bilabial fricatives delabialize
    ˌlɑˈβʷɑː.rɛ → ˌlɑˈβɑː.rɛ   (βʷ→β)
500: the low vowel fronts by default
    ˌlɑˈβɑː.rɛ → ˌlaˈβaː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌlaˈβaː.rɛ → ˌlaˈβaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌlaˈβaː.rə → ˌlaˈβaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌlaˈβaːrə̯ → ˌlaˈβaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌlaˈβaːr → ˌlaˈβae̯r   (ˈaː→ˈae̯)
600: the remaining bilabial fricative becomes v
    ˌlaˈβae̯r → ˌlaˈvae̯r   (β→v)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌlaˈvae̯r → ˌlaˈveːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌlaˈveːr → ˌlaˈver   (ˈeː→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌlaˈver → ˌlaˈveɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌlaˈveɹ → ˌlaˈve   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌlaˈve → la.ve   (ˌa→a, ˈe→e)
```

## leur

`illˈoːrum` → `lœʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ilˈloː.rum → ɪlˈloː.rʊm   (i→ɪ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ɪlˈloː.rʊm → ɪlˈlo.rʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ɪlˈlo.rʊm → elˈlo.rom   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    elˈlo.rom → elˈlo.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    elˈlo.ro → elˈloː.ro   (ˈo→ˈoː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    elˈloː.ro → əlˈloː.rə   (e→ə, o→ə)
600: schwa becomes non-syllabic
    əlˈloː.rə → ˈə̯lloːrə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈə̯lloːrə̯ → ˈlloːr   (ˈə̯lloːrə̯→ˈlloːr)
600: an identical consonant geminate reduces to one, after a consonant or word start
    ˈlloːr → ˈloːr   (l→∅)
600: long stressed vowels diphthongize
    ˈloːr → ˈlowr   (ˈoː→ˈow)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˈlowr → ˈlør   (ˈow→ˈø)
1400: e/ø lax before an r that closes the syllable
    ˈlør → ˈlœr   (ˈø→ˈœ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈlœr → ˈlœɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈlœɹ → ˈlœr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈlœr → ˈlœʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈlœʀ → lœʀ   (ˈœ→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    lœʀ → lœʁ   (ʀ→ʁ)
```

## lignée

`lˌiːn̪eˈɑːt̪ɑm` → `lɛ.ɲe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌliː.n̪eˈɑː.t̪ɑm → ˌliː.n̪ɛˈɑː.t̪ɑm   (e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌliː.n̪ɛˈɑː.t̪ɑm → ˌliːˈn̪jɑː.t̪ɑm   (ɛ→j)
-100: yod strengthens before a vowel
    ˌliːˈn̪jɑː.t̪ɑm → ˌliːn̪ˈʝɑː.t̪ɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌliːn̪ˈʝɑː.t̪ɑm → ˌlin̪ˈʝɑ.t̪ɑm   (ˌiː→ˌi, ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌlin̪ˈʝɑ.t̪ɑm → ˌlin̪ˈʝɑ.t̪ɑ   (m→∅)
300: the coronal nasal palatalizes before yod
    ˌlin̪ˈʝɑ.t̪ɑ → ˌliˈɲɑ.t̪ɑ   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌliˈɲɑ.t̪ɑ → ˌliˈɲɑː.t̪ɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌliˈɲɑː.t̪ɑ → ˌliˈɲaː.t̪a   (ˈɑː→ˈaː, ɑ→a)
600: a voiceless consonant voices intervocalically
    ˌliˈɲaː.t̪a → ˌliˈɲaː.d̪a   (t̪→d̪)
600: a stressed low vowel becomes front non-tense after a front glide, before a consonant + non-consonantal
    ˌliˈɲaː.d̪a → ˌliˈɲɛː.d̪a   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌliˈɲɛː.d̪a → ˌliˈɲie̯.d̪a   (ˈɛː→ˈie̯)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌliˈɲie̯.d̪a → ˌliˈɲie̯.ða   (d̪→ð)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌliˈɲie̯.ða → ˌliˈɲie̯.ðə   (a→ə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌliˈɲie̯.ðə → ˌlĩˈɲie̯.ðə   (ˌi→ˌĩ)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌlĩˈɲie̯.ðə → ˌlĩˈɲje.ðə   (ˈi→j, e̯→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌlĩˈɲje.ðə → ˌlĩˈɲje.ə   (ð→∅)
1200: schwa desyllabifies after another vowel
    ˌlĩˈɲje.ə → ˌlĩˈɲjeə̯   (ə→ə̯)
1200: nasalized ĩ lowers to ẽ
    ˌlĩˈɲjeə̯ → ˌlẽˈɲjeə̯   (ˌĩ→ˌẽ)
1200: je becomes e after a palatal consonant
    ˌlẽˈɲjeə̯ → ˌlẽˈɲeə̯   (j→∅)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˌlẽˈɲeə̯ → ˌlẽˈɲeː   (ˈeə̯→ˈeː)
1400: nasalized ẽ lowers to ɛ̃
    ˌlẽˈɲeː → ˌlɛ̃ˈɲeː   (ˌẽ→ˌɛ̃)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˌlɛ̃ˈɲeː → ˌlɛˈɲeː   (ˌɛ̃→ˌɛ)
1400: stress is leveled — no longer distinctive for vowels
    ˌlɛˈɲeː → lɛ.ɲeː   (ˌɛ→ɛ, ˈeː→eː)
1400: distinctive vowel length is lost entirely
    lɛ.ɲeː → lɛ.ɲe   (eː→e)
```

## limer

`lˌiːmˈɑːre` → `li.me`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌliːˈmɑː.re → ˌliːˈmɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌliːˈmɑː.rɛ → ˌliˈmɑ.rɛ   (ˌiː→ˌi, ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌliˈmɑ.rɛ → ˌliˈmɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌliˈmɑː.rɛ → ˌliˈmaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌliˈmaː.rɛ → ˌliˈmaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌliˈmaː.rə → ˌliˈmaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌliˈmaːrə̯ → ˌliˈmaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌliˈmaːr → ˌliˈmae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌliˈmae̯r → ˌliˈmeːr   (ˈae̯→ˈeː)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌliˈmeːr → ˌlĩˈmeːr   (ˌi→ˌĩ)
1000: vowel length resets to short
    ˌlĩˈmeːr → ˌlĩˈmer   (ˈeː→ˈe)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌlĩˈmer → ˌliˈmer   (ˌĩ→ˌi)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌliˈmer → ˌliˈmeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌliˈmeɹ → ˌliˈme   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌliˈme → li.me   (ˌi→i, ˈe→e)
```

## livre

`lˈiːbrɑm` → `livʁ`

```
-100: b lenites to β intervocalically / before a sonorant
    ˈliː.brɑm → ˈliː.βrɑm   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˈliː.βrɑm → ˈli.βrɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈli.βrɑm → ˈli.βrɑ   (m→∅)
300: a stressed vowel lengthens before a voiced labial + r + vowel + word end
    ˈli.βrɑ → ˈliː.βrɑ   (ˈi→ˈiː)
500: a vowel shortens before a consonant cluster
    ˈliː.βrɑ → ˈli.βrɑ   (ˈiː→ˈi)
500: a stressed vowel lengthens before a voiced labial + r + vowel + word end
    ˈli.βrɑ → ˈliː.βrɑ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˈliː.βrɑ → ˈliː.βra   (ɑ→a)
500: a vowel shortens before a consonant cluster (recurrence)
    ˈliː.βra → ˈli.βra   (ˈiː→ˈi)
500: a stressed vowel lengthens before a voiced labial + r + vowel (recurrence)
    ˈli.βra → ˈliː.βra   (ˈi→ˈiː)
600: the bilabial fricative becomes v after a non-low front vowel before r
    ˈliː.βra → ˈliː.vra   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈliː.vra → ˈliː.vrə   (a→ə)
750: vowel length resets to short
    ˈliː.vrə → ˈli.vrə   (ˈiː→ˈi)
1400: final ə becomes a non-syllabic off-glide
    ˈli.vrə → ˈlivrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlivrə̯ → ˈlivr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈlivr → ˈlivʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈlivʀ → livʀ   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    livʀ → livʁ   (ʀ→ʁ)
```

## lièvre

`lˈeporem` → `ljɛvʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈle.po.rem → ˈlɛ.pɔ.rɛm   (ˈe→ˈɛ, o→ɔ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɛ.pɔ.rɛm → ˈlɛ.pɔ.rɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈlɛ.pɔ.rɛ → ˈlɛː.pɔ.rɛ   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈlɛː.pɔ.rɛ → ˈlie̯.pɔ.rɛ   (ˈɛː→ˈie̯)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈlie̯.pɔ.rɛ → ˈlie̯.pə.rɛ   (ɔ→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈlie̯.pə.rɛ → ˈlie̯.pə.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈlie̯.pə.rə → ˈlie̯pə̯rə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈlie̯pə̯rə̯ → ˈlie̯pə̯.rə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈlie̯pə̯.rə → ˈlie̯.prə   (ə̯→∅)
600: a voiceless anterior consonant voices before a coronal sonorant non-nasal consonant
    ˈlie̯.prə → ˈlie̯.brə   (p→b)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈlie̯.brə → ˈlie̯.βrə   (b→β)
600: the remaining bilabial fricative becomes v
    ˈlie̯.βrə → ˈlie̯.vrə   (β→v)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈlie̯.vrə → ˈlje.vrə   (ˈi→j, e̯→ˈe)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈlje.vrə → ˈljɛ.vrə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈljɛ.vrə → ˈljɛvrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈljɛvrə̯ → ˈljɛvr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈljɛvr → ˈljɛvʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈljɛvʀ → ljɛvʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ljɛvʀ → ljɛvʁ   (ʀ→ʁ)
```

## longs

`lˈon̪goːs` → `lɔ̃`

```
-100: n assimilates to a following velar stop
    ˈlon̪.goːs → ˈloŋ.goːs   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈloŋ.goːs → ˈlɔŋ.goːs   (ˈo→ˈɔ)
-100: the length feature is dropped now that quality carries the contrast
    ˈlɔŋ.goːs → ˈlɔŋ.gos   (oː→o)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈlɔŋ.gos → ˈlũŋ.gos   (ˈɔ→ˈũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈlũŋ.gos → ˈlũŋ.gəs   (o→ə)
600: schwa becomes non-syllabic
    ˈlũŋ.gəs → ˈlũŋgə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈlũŋgə̯s → ˈlũŋgs   (ə̯→∅)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈlũŋgs → ˈlũŋs   (g→∅)
1000: ŋ simplifies to n before a non-velar segment
    ˈlũŋs → ˈlũn̪s   (ŋ→n̪)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈlũn̪s → ˈlũːs   (ˈũn̪→ˈũː)
1400: final obstruents are lost
    ˈlũːs → ˈlũː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlũː → lũː   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    lũː → lũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    lũ → lɔ̃   (ũ→ɔ̃)
```

## lorier

`lˌɑwrˈɑːrium` → `lɔ.ʁje`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌlɑwˈrɑː.ri.um → ˌlɑwˈrɑː.rɪ.ʊm   (i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌlɑwˈrɑː.rɪ.ʊm → ˌlɑwˈrɑː.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌlɑwˈrɑː.rjʊm → ˌlɑwˈrɑːr.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌlɑwˈrɑːr.ʝʊm → ˌlɑwˈrɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌlɑwˈrɑr.ʝʊm → ˌlɑwˈrɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌlɑwˈrɑr.ʝom → ˌlɑwˈrɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌlɑwˈrɑr.ʝo → ˌlɑwˈrɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌlɑwˈrɑ.rʲo → ˌlawˈra.rʲo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌlawˈra.rʲo → ˌlawˈraː.rʲo   (ˈa→ˈaː)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌlawˈraː.rʲo → ˌlɔwˈraː.rʲo   (ˌa→ˌɔ)
600: aːrʲ metathesizes to jɛːr
    ˌlɔwˈraː.rʲo → ˌlɔwˈrjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌlɔwˈrjɛː.ro → ˌlɔwˈrjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌlɔwˈrjɛː.rə → ˌlɔwˈrjɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌlɔwˈrjɛːrə̯ → ˌlɔwˈrjɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌlɔwˈrjɛːr → ˌlɔwˈrjie̯r   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌlɔwˈrjie̯r → ˌlɔwˈrie̯r   (j→∅)
600: secondary-stressed ɔ raises to ɯ before w
    ˌlɔwˈrie̯r → ˌlɯwˈrie̯r   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌlɯwˈrie̯r → ˌlɔwˈrie̯r   (ˌɯ→ˌɔ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌlɔwˈrie̯r → ˌlɔˈrie̯r   (w→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌlɔˈrie̯r → ˌlɔˈrjer   (ˈi→j, e̯→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌlɔˈrjer → ˌlɔˈɹjeɹ   (r→ɹ, r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌlɔˈɹjeɹ → ˌlɔˈɹje   (ɹ→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌlɔˈɹje → ˌlɔˈrje   (ɹ→r)
1400: r becomes uvular ʀ
    ˌlɔˈrje → ˌlɔˈʀje   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌlɔˈʀje → lɔ.ʀje   (ˌɔ→ɔ, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    lɔ.ʀje → lɔ.ʁje   (ʀ→ʁ)
```

## louer

`lˌokˈɑːre` → `lu̯e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌloˈkɑː.re → ˌlɔˈkɑː.rɛ   (ˌo→ˌɔ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌlɔˈkɑː.rɛ → ˌlɔˈkɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌlɔˈkɑ.rɛ → ˌlɔˈkɑː.rɛ   (ˈɑ→ˈɑː)
500: k voices to g intervocalically
    ˌlɔˈkɑː.rɛ → ˌlɔˈgɑː.rɛ   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˌlɔˈgɑː.rɛ → ˌlɔˈɣɑː.rɛ   (g→ɣ)
500: the velar fricative is lost after a rounded non-consonantal segment before a low vowel
    ˌlɔˈɣɑː.rɛ → ˌlɔˈɑː.rɛ   (ɣ→∅)
500: the low vowel fronts by default
    ˌlɔˈɑː.rɛ → ˌlɔˈaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌlɔˈaː.rɛ → ˌlɔˈaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌlɔˈaː.rə → ˌlɔˈaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌlɔˈaːrə̯ → ˌlɔˈaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌlɔˈaːr → ˌlɔˈae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɔ raises to o unconditionally
    ˌlɔˈae̯r → ˌloˈae̯r   (ˌɔ→ˌo)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌloˈae̯r → ˌloˈeːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌloˈeːr → ˌloˈer   (ˈeː→ˈe)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌloˈer → ˌluˈer   (ˌo→ˌu)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌluˈer → ˌluˈeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌluˈeɹ → ˌluˈe   (ɹ→∅)
1400: a countertonic high vowel consonantalizes before a lower vowel, ceding stress
    ˌluˈe → ˌlu̯e   (ˌu→u̯, ˈe→ˌe)
1400: stress is leveled — no longer distinctive for vowels
    ˌlu̯e → lu̯e   (ˌe→e)
```

## louve

`lˈupɑm` → `luv`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈlu.pɑm → ˈlʊ.pɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈlʊ.pɑm → ˈlo.pɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlo.pɑm → ˈlo.pɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈlo.pɑ → ˈloː.pɑ   (ˈo→ˈoː)
500: the low vowel fronts by default
    ˈloː.pɑ → ˈloː.pa   (ɑ→a)
600: a voiceless consonant voices intervocalically
    ˈloː.pa → ˈloː.ba   (p→b)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈloː.ba → ˈloː.βa   (b→β)
600: long stressed vowels diphthongize
    ˈloː.βa → ˈlow.βa   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈlow.βa → ˈlo.βa   (w→∅)
600: the remaining bilabial fricative becomes v
    ˈlo.βa → ˈlo.va   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlo.va → ˈlo.və   (a→ə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈlo.və → ˈlu.və   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈlu.və → ˈluvə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈluvə̯ → ˈluv   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈluv → luv   (ˈu→u)
```

## lune

`lˈuːn̪ɑm` → `lyn̪`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈluː.n̪ɑm → ˈlu.n̪ɑm   (ˈuː→ˈu)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlu.n̪ɑm → ˈlu.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈlu.n̪ɑ → ˈluː.n̪ɑ   (ˈu→ˈuː)
500: the low vowel fronts by default
    ˈluː.n̪ɑ → ˈluː.n̪a   (ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˈluː.n̪a → ˈlʉː.n̪a   (ˈuː→ˈʉː)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlʉː.n̪a → ˈlʉː.n̪ə   (a→ə)
750: vowel length resets to short
    ˈlʉː.n̪ə → ˈlʉ.n̪ə   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈlʉ.n̪ə → ˈly.n̪ə   (ˈʉ→ˈy)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈly.n̪ə → ˈlỹ.n̪ə   (ˈy→ˈỹ)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˈlỹ.n̪ə → ˈly.n̪ə   (ˈỹ→ˈy)
1400: final ə becomes a non-syllabic off-glide
    ˈly.n̪ə → ˈlyn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlyn̪ə̯ → ˈlyn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlyn̪ → lyn̪   (ˈy→y)
```

## léger

`lˌewiˈɑːrium` → `li.je`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌle.wiˈɑː.ri.um → ˌle.ɣʷiˈɑː.ri.um   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌle.ɣʷiˈɑː.ri.um → ˌlɛ.ɣʷɪˈɑː.rɪ.ʊm   (ˌe→ˌɛ, i→ɪ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌlɛ.ɣʷɪˈɑː.rɪ.ʊm → ˌlɛˈɣʷjɑː.rjʊm   (ɪ→j, ɪ→j)
-100: yod strengthens before a vowel
    ˌlɛˈɣʷjɑː.rjʊm → ˌlɛɣʷˈʝɑːr.ʝʊm   (j→ʝ, j→ʝ)
-100: the rounded glide is lost before the strengthened yod
    ˌlɛɣʷˈʝɑːr.ʝʊm → ˌlɛˈʝɑːr.ʝʊm   (ɣʷ→∅)
-100: the length feature is dropped now that quality carries the contrast
    ˌlɛˈʝɑːr.ʝʊm → ˌlɛˈʝɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌlɛˈʝɑr.ʝʊm → ˌlɛˈʝɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌlɛˈʝɑr.ʝom → ˌlɛˈʝɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌlɛˈʝɑr.ʝo → ˌlɛˈʝɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌlɛˈʝɑ.rʲo → ˌlɛˈʝa.rʲo   (ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌlɛˈʝa.rʲo → ˌlɛˈʝaː.rʲo   (ˈa→ˈaː)
500: long stressed aː becomes ɛː after a front consonant, before palatalized r
    ˌlɛˈʝaː.rʲo → ˌlɛˈʝɛː.rʲo   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˌlɛˈʝɛː.rʲo → ˌlɛˈʝie̯.rʲo   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌlɛˈʝie̯.rʲo → ˌlɛˈʝie̯.rʲə   (o→ə)
600: schwa becomes non-syllabic
    ˌlɛˈʝie̯.rʲə → ˌlɛˈʝie̯rʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌlɛˈʝie̯rʲə̯ → ˌlɛˈʝie̯rʲ   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˌlɛˈʝie̯rʲ → ˌlɛˈʝie̯jrʲ   (∅→j)
600: j lost after a vowel + optional consonants + stressed ie̯, before palatalized r
    ˌlɛˈʝie̯jrʲ → ˌlɛˈʝie̯rʲ   (j→∅)
600: ʝ weakens to j unconditionally
    ˌlɛˈʝie̯rʲ → ˌlɛˈjie̯rʲ   (ʝ→j)
600: palatalized r depalatalizes
    ˌlɛˈjie̯rʲ → ˌlɛˈjie̯r   (rʲ→r)
600: secondary-stressed ɛj becomes i before a coronal
    ˌlɛˈjie̯r → ˌliˈie̯r   (ˌɛj→ˌi)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌliˈie̯r → ˌliˈjer   (ˈi→j, e̯→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌliˈjer → ˌliˈjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌliˈjeɹ → ˌliˈje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌliˈje → li.je   (ˌi→i, ˈe→e)
```

## mai

`mˈɑjum` → `mɛ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈmɑ.jum → ˈmɑ.ʝum   (j→ʝ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmɑ.ʝum → ˈmɑ.ʝʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈmɑ.ʝʊm → ˈmɑ.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmɑ.ʝom → ˈmɑ.ʝo   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈmɑ.ʝo → ˈmɑː.ʝo   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈmɑː.ʝo → ˈmaː.ʝo   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmaː.ʝo → ˈmaː.ʝə   (o→ə)
600: schwa becomes non-syllabic
    ˈmaː.ʝə → ˈmaːʝə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmaːʝə̯ → ˈmaːʝ   (ə̯→∅)
600: ʝ weakens to j before optional consonants + word end
    ˈmaːʝ → ˈmaːj   (ʝ→j)
600: long stressed vowels diphthongize
    ˈmaːj → ˈmae̯j   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˈmae̯j → ˈmaj   (e̯→∅)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈmaj → ˈmɛː   (ˈaj→ˈɛː)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɛː → mɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    mɛː → mɛ   (ɛː→ɛ)
```

## main

`mˈɑn̪u` → `mɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmɑ.n̪u → ˈmɑ.n̪ʊ   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈmɑ.n̪ʊ → ˈmɑ.n̪o   (ʊ→o)
300: a stressed vowel lengthens before a single consonant + glide
    ˈmɑ.n̪o → ˈmɑː.n̪o   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈmɑː.n̪o → ˈmaː.n̪o   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmaː.n̪o → ˈmaː.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈmaː.n̪ə → ˈmaːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmaːn̪ə̯ → ˈmaːn̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈmaːn̪ → ˈmae̯n̪   (ˈaː→ˈae̯)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˈmae̯n̪ → ˈmajn̪   (e̯→j)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˈmajn̪ → ˈmaj̃n̪   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈmaj̃n̪ → ˈmãj̃n̪   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈmãj̃n̪ → ˈmɛ̃j̃n̪   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈmɛ̃j̃n̪ → ˈmɛ̃n̪   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈmɛ̃n̪ → ˈmɛ̃ː   (ˈɛ̃n̪→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɛ̃ː → mɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    mɛ̃ː → mɛ̃   (ɛ̃ː→ɛ̃)
```

## mais

`mˈɑgis` → `mɛ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmɑ.gis → ˈmɑ.gɪs   (i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈmɑ.gɪs → ˈmɑ.ges   (ɪ→e)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈmɑ.ges → ˈmɑ.gʲes   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˈmɑ.gʲes → ˈmɑ.ɟes   (gʲ→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈmɑ.ɟes → ˈmɑ.ʝes   (ɟ→ʝ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈmɑ.ʝes → ˈmɑː.ʝes   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈmɑː.ʝes → ˈmaː.ʝes   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmaː.ʝes → ˈmaː.ʝəs   (e→ə)
600: schwa becomes non-syllabic
    ˈmaː.ʝəs → ˈmaːʝə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmaːʝə̯s → ˈmaːʝs   (ə̯→∅)
600: ʝ weakens to j before optional consonants + word end
    ˈmaːʝs → ˈmaːjs   (ʝ→j)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈmaːjs → ˈmaːjsʲ   (s→sʲ)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈmaːjsʲ → ˈmajsʲ   (ˈaː→ˈa)
600: a stressed vowel lengthens before j + optional consonants + a high-front coronal
    ˈmajsʲ → ˈmaːjsʲ   (ˈa→ˈaː)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈmaːjsʲ → ˈmaːjjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈmaːjjs → ˈmaːjs   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈmaːjs → ˈmaːjt͡sʲ   (s→t͡sʲ)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˈmaːjt͡sʲ → ˈmajt͡sʲ   (ˈaː→ˈa)
1000: all affricates become sibilants (deaffrication)
    ˈmajt͡sʲ → ˈmajsʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈmajsʲ → ˈmajs   (sʲ→s)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈmajs → ˈmɛːs   (ˈaj→ˈɛː)
1400: final obstruents are lost
    ˈmɛːs → ˈmɛː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɛː → mɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    mɛː → mɛ   (ɛː→ɛ)
```

## maison

`mˌɑn̪siˈoːn̪em` → `mɛ.zɔ̃`

```
-100: vowel lengthens before ns when the next syllable is unstressed
    ˌmɑn̪.siˈoː.n̪em → ˌmɑːn̪.siˈoː.n̪em   (ˌɑ→ˌɑː)
-100: n lost after a long vowel before s (compensatory lengthening already applied)
    ˌmɑːn̪.siˈoː.n̪em → ˌmɑː.siˈoː.n̪em   (n̪→∅)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmɑː.siˈoː.n̪em → ˌmɑː.sɪˈoː.n̪ɛm   (i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɑː.sɪˈoː.n̪ɛm → ˌmɑːˈsjoː.n̪ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌmɑːˈsjoː.n̪ɛm → ˌmɑːsˈʝoː.n̪ɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɑːsˈʝoː.n̪ɛm → ˌmɑsˈʝo.n̪ɛm   (ˌɑː→ˌɑ, ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɑsˈʝo.n̪ɛm → ˌmɑsˈʝo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɑsˈʝo.n̪ɛ → ˌmɑsˈʝoː.n̪ɛ   (ˈo→ˈoː)
500: a voiceless fricative voices before yod + a non-consonantal segment
    ˌmɑsˈʝoː.n̪ɛ → ˌmɑzˈʝoː.n̪ɛ   (s→z)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌmɑzˈʝoː.n̪ɛ → ˌmɑzˈʝũː.n̪ɛ   (ˈoː→ˈũː)
500: z + yod becomes palatalized z
    ˌmɑzˈʝũː.n̪ɛ → ˌmɑˈzʲũː.n̪ɛ   (zʝ→zʲ)
500: the low vowel fronts by default
    ˌmɑˈzʲũː.n̪ɛ → ˌmaˈzʲũː.n̪ɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmaˈzʲũː.n̪ɛ → ˌmaˈzʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌmaˈzʲũː.n̪ə → ˌmaˈzʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmaˈzʲũːn̪ə̯ → ˌmaˈzʲũːn̪   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌmaˈzʲũːn̪ → ˌmajˈzũːn̪   (zʲ→jz)
750: vowel length resets to short
    ˌmajˈzũːn̪ → ˌmajˈzũn̪   (ˈũː→ˈũ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmajˈzũn̪ → ˌmajˈzũː   (ˈũn̪→ˈũː)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌmajˈzũː → ˌmɛːˈzũː   (ˌaj→ˌɛː)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɛːˈzũː → mɛː.zũː   (ˌɛː→ɛː, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    mɛː.zũː → mɛ.zũ   (ɛː→ɛ, ũː→ũ)
1400: nasal ũ opens to ɔ̃
    mɛ.zũ → mɛ.zɔ̃   (ũ→ɔ̃)
```

## mal

`mˌɑlum` → `mal`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmɑ.lum → ˌmɑ.lʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˌmɑ.lʊm → ˌmɑ.lom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɑ.lom → ˌmɑ.lo   (m→∅)
500: the low vowel fronts by default
    ˌmɑ.lo → ˌma.lo   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌma.lo → ˌma.lə   (o→ə)
600: schwa becomes non-syllabic
    ˌma.lə → ˌmalə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmalə̯ → ˌmal   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmal → mal   (ˌa→a)
```

## mander

`mˈɑn̪d̪ˈɑːre` → `mɑ̃.d̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmɑn̪ˈd̪ɑː.re → ˈmɑn̪ˈd̪ɑː.rɛ   (e→ɛ)
-100: the old primary stress demotes when a new one has been placed (type 2)
    ˈmɑn̪ˈd̪ɑː.rɛ → ˌmɑn̪ˈd̪ɑː.rɛ   (ˈɑ→ˌɑ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɑn̪ˈd̪ɑː.rɛ → ˌmɑn̪ˈd̪ɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɑn̪ˈd̪ɑ.rɛ → ˌmɑn̪ˈd̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌmɑn̪ˈd̪ɑː.rɛ → ˌman̪ˈd̪aː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌman̪ˈd̪aː.rɛ → ˌman̪ˈd̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌman̪ˈd̪aː.rə → ˌman̪ˈd̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌman̪ˈd̪aːrə̯ → ˌman̪ˈd̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌman̪ˈd̪aːr → ˌman̪ˈd̪ae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌman̪ˈd̪ae̯r → ˌman̪ˈd̪eːr   (ˈae̯→ˈeː)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌman̪ˈd̪eːr → ˌmãn̪ˈd̪eːr   (ˌa→ˌã)
1000: vowel length resets to short
    ˌmãn̪ˈd̪eːr → ˌmãn̪ˈd̪er   (ˈeː→ˈe)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmãn̪ˈd̪er → ˌmãːˈd̪er   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌmãːˈd̪er → ˌmɑ̃ːˈd̪er   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmɑ̃ːˈd̪er → ˌmɑ̃ːˈd̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌmɑ̃ːˈd̪eɹ → ˌmɑ̃ːˈd̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɑ̃ːˈd̪e → mɑ̃ː.d̪e   (ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    mɑ̃ː.d̪e → mɑ̃.d̪e   (ɑ̃ː→ɑ̃)
```

## manger

`mˌɑn̪d̪uːkˈɑːre` → `mɑ̃.ʒe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmɑn̪.d̪uːˈkɑː.re → ˌmɑn̪.d̪uːˈkɑː.rɛ   (e→ɛ)
-100: unstressed long u becomes a mid central vowel (sonus medius), not word-finally
    ˌmɑn̪.d̪uːˈkɑː.rɛ → ˌmɑn̪.d̪ɪˈkɑː.rɛ   (uː→ɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɑn̪.d̪ɪˈkɑː.rɛ → ˌmɑn̪.d̪ɪˈkɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌmɑn̪.d̪ɪˈkɑ.rɛ → ˌmɑn̪.d̪eˈkɑ.rɛ   (ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɑn̪.d̪eˈkɑ.rɛ → ˌmɑn̪.d̪eˈkɑː.rɛ   (ˈɑ→ˈɑː)
500: k voices to g intervocalically
    ˌmɑn̪.d̪eˈkɑː.rɛ → ˌmɑn̪.d̪eˈgɑː.rɛ   (k→g)
500: e lost in -ica- endings before the now-voiced g + low vowel
    ˌmɑn̪.d̪eˈgɑː.rɛ → ˌmɑn̪d̪ˈgɑː.rɛ   (e→∅)
500: the low vowel fronts by default
    ˌmɑn̪d̪ˈgɑː.rɛ → ˌman̪d̪ˈgaː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
500: the high back consonant w fronts before a front vowel
    ˌman̪d̪ˈgaː.rɛ → ˌman̪d̪ˈgʲaː.rɛ   (g→gʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌman̪d̪ˈgʲaː.rɛ → ˌman̪d̪ˈɟaː.rɛ   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˌman̪d̪ˈɟaː.rɛ → ˌman̪ˈd̪d͡ʒaː.rɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌman̪ˈd̪d͡ʒaː.rɛ → ˌman̪ˈd̪d͡ʒaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌman̪ˈd̪d͡ʒaː.rə → ˌman̪ˈd̪d͡ʒaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌman̪ˈd̪d͡ʒaːrə̯ → ˌman̪ˈd̪d͡ʒaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌman̪ˈd̪d͡ʒaːr → ˌman̪ˈd̪d͡ʒae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌman̪ˈd̪d͡ʒae̯r → ˌman̪ˈd̪d͡ʒeːr   (ˈae̯→ˈeː)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌman̪ˈd̪d͡ʒeːr → ˌman̪ˈd͡ʒeːr   (d̪→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌman̪ˈd͡ʒeːr → ˌmãn̪ˈd͡ʒeːr   (ˌa→ˌã)
1000: vowel length resets to short
    ˌmãn̪ˈd͡ʒeːr → ˌmãn̪ˈd͡ʒer   (ˈeː→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌmãn̪ˈd͡ʒer → ˌmãn̪ˈʒer   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmãn̪ˈʒer → ˌmãːˈʒer   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌmãːˈʒer → ˌmɑ̃ːˈʒer   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmɑ̃ːˈʒer → ˌmɑ̃ːˈʒeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌmɑ̃ːˈʒeɹ → ˌmɑ̃ːˈʒe   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɑ̃ːˈʒe → mɑ̃ː.ʒe   (ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    mɑ̃ː.ʒe → mɑ̃.ʒe   (ɑ̃ː→ɑ̃)
```

## meilleur

`mˌeliˈoːrem` → `me.jœʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌme.liˈoː.rem → ˌmɛ.lɪˈoː.rɛm   (ˌe→ˌɛ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɛ.lɪˈoː.rɛm → ˌmɛˈljoː.rɛm   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˌmɛˈljoː.rɛm → ˌmɛˈɫjoː.rɛm   (l→ɫ)
-100: yod strengthens before a vowel
    ˌmɛˈɫjoː.rɛm → ˌmɛɫˈʝoː.rɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɛɫˈʝoː.rɛm → ˌmɛɫˈʝo.rɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɛɫˈʝo.rɛm → ˌmɛɫˈʝo.rɛ   (m→∅)
300: l palatalizes to ʎ before yod
    ˌmɛɫˈʝo.rɛ → ˌmɛˈʎo.rɛ   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɛˈʎo.rɛ → ˌmɛˈʎoː.rɛ   (ˈo→ˈoː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmɛˈʎoː.rɛ → ˌmɛˈʎoː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌmɛˈʎoː.rə → ˌmɛˈʎoːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmɛˈʎoːrə̯ → ˌmɛˈʎoːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌmɛˈʎoːr → ˌmɛˈʎowr   (ˈoː→ˈow)
600: secondary-stressed ɛ raises to e before any two segments
    ˌmɛˈʎowr → ˌmeˈʎowr   (ˌɛ→ˌe)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˌmeˈʎowr → ˌmeˈʎør   (ˈow→ˈø)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌmeˈʎør → ˌməˈʎør   (ˌe→ˌə)
1000: secondary-stressed schwa reverts to e before a palatal consonant
    ˌməˈʎør → ˌmeˈʎør   (ˌə→ˌe)
1000: a glide develops between a stressed mid front unrounded vowel and intervocalic ʎ
    ˌmeˈʎør → ˌmejˈʎør   (∅→j)
1400: e/ø lax before an r that closes the syllable
    ˌmejˈʎør → ˌmejˈʎœr   (ˈø→ˈœ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmejˈʎœr → ˌmejˈʎœɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌmejˈʎœɹ → ˌmejˈʎœr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌmejˈʎœr → ˌmejˈʎœʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌmejˈʎœʀ → mej.ʎœʀ   (ˌe→e, ˈœ→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    mej.ʎœʀ → mej.ʎœʁ   (ʀ→ʁ)
1400: ʎ becomes j
    mej.ʎœʁ → mej.jœʁ   (ʎ→j)
1400: a high front vowel after another vowel is absorbed into a following j
    mej.jœʁ → me.jœʁ   (j→∅)
```

## membre

`mˈembrum` → `mɑ̃bʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmem.brum → ˈmɛm.brʊm   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈmɛm.brʊm → ˈmɛm.brom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmɛm.brom → ˈmɛm.bro   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmɛm.bro → ˈmɛm.brə   (o→ə)
600: schwa becomes non-syllabic
    ˈmɛm.brə → ˈmɛmbrə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈmɛmbrə̯ → ˈmɛm.brə   (ə̯→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈmɛm.brə → ˈmɛ̃m.brə   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈmɛ̃m.brə → ˈmãm.brə   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈmãm.brə → ˈmãː.brə   (ˈãm→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈmãː.brə → ˈmãːbrə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈmãːbrə̯ → ˈmɑ̃ːbrə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈmɑ̃ːbrə̯ → ˈmɑ̃ːbr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈmɑ̃ːbr → ˈmɑ̃ːbʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɑ̃ːbʀ → mɑ̃ːbʀ   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    mɑ̃ːbʀ → mɑ̃bʀ   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    mɑ̃bʀ → mɑ̃bʁ   (ʀ→ʁ)
```

## mener

`mˌin̪ˈɑːri` → `mə.n̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmiˈn̪ɑː.ri → ˌmɪˈn̪ɑː.rɪ   (ˌi→ˌɪ, i→ɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɪˈn̪ɑː.rɪ → ˌmɪˈn̪ɑ.rɪ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌmɪˈn̪ɑ.rɪ → ˌmeˈn̪ɑ.re   (ˌɪ→ˌe, ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmeˈn̪ɑ.re → ˌmeˈn̪ɑː.re   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌmeˈn̪ɑː.re → ˌmeˈn̪aː.re   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmeˈn̪aː.re → ˌmeˈn̪aː.rə   (e→ə)
600: schwa becomes non-syllabic
    ˌmeˈn̪aː.rə → ˌmeˈn̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmeˈn̪aːrə̯ → ˌmeˈn̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌmeˈn̪aːr → ˌmeˈn̪ae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌmeˈn̪ae̯r → ˌmeˈn̪eːr   (ˈae̯→ˈeː)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌmeˈn̪eːr → ˌməˈn̪eːr   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌməˈn̪eːr → ˌmə̃ˈn̪eːr   (ˌə→ˌə̃)
1000: vowel length resets to short
    ˌmə̃ˈn̪eːr → ˌmə̃ˈn̪er   (ˈeː→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmə̃ˈn̪er → ˌmə̃ˈn̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌmə̃ˈn̪eɹ → ˌmə̃ˈn̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmə̃ˈn̪e → mə̃.n̪e   (ˌə̃→ə̃, ˈe→e)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    mə̃.n̪e → mə.n̪e   (ə̃→ə)
```

## mer

`mˈɑre` → `mɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmɑ.re → ˈmɑ.rɛ   (e→ɛ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈmɑ.rɛ → ˈmɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈmɑː.rɛ → ˈmaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmaː.rɛ → ˈmaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈmaː.rə → ˈmaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmaːrə̯ → ˈmaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈmaːr → ˈmae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈmae̯r → ˈmeːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈmeːr → ˈmer   (ˈeː→ˈe)
1400: e/ø lax before an r that closes the syllable
    ˈmer → ˈmɛr   (ˈe→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈmɛr → ˈmɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈmɛɹ → ˈmɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈmɛr → ˈmɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɛʀ → mɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    mɛʀ → mɛʁ   (ʀ→ʁ)
```

## mie

`mˈiːkɑm` → `mi`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈmiː.kɑm → ˈmi.kɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmi.kɑm → ˈmi.kɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈmi.kɑ → ˈmiː.kɑ   (ˈi→ˈiː)
500: k voices to g intervocalically
    ˈmiː.kɑ → ˈmiː.gɑ   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˈmiː.gɑ → ˈmiː.ɣɑ   (g→ɣ)
500: the low vowel fronts by default
    ˈmiː.ɣɑ → ˈmiː.ɣa   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈmiː.ɣa → ˈmiː.ɣʲa   (ɣ→ɣʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈmiː.ɣʲa → ˈmiː.ʝa   (ɣʲ→ʝ)
600: ʝ weakens to j unconditionally
    ˈmiː.ʝa → ˈmiː.ja   (ʝ→j)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈmiː.ja → ˈmiː.jə   (a→ə)
750: vowel length resets to short
    ˈmiː.jə → ˈmi.jə   (ˈiː→ˈi)
750: j deletes after a high front tense vowel
    ˈmi.jə → ˈmi.ə   (j→∅)
1200: schwa desyllabifies after another vowel
    ˈmi.ə → ˈmiə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈmiə̯ → ˈmiː   (ˈiə̯→ˈiː)
1400: stress is leveled — no longer distinctive for vowels
    ˈmiː → miː   (ˈiː→iː)
1400: distinctive vowel length is lost entirely
    miː → mi   (iː→i)
```

## mille

`mˈiːllem` → `mil`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmiːl.lem → ˈmiːl.lɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˈmiːl.lɛm → ˈmil.lɛm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmil.lɛm → ˈmil.lɛ   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmil.lɛ → ˈmil.lə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈmil.lə → ˈmillə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmillə̯ → ˈmill   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˈmill → ˈmil   (l→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmil → mil   (ˈi→i)
```

## moisson

`mˌessiˈoːn̪em` → `mwa.sɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmes.siˈoː.n̪em → ˌmɛs.sɪˈoː.n̪ɛm   (ˌe→ˌɛ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɛs.sɪˈoː.n̪ɛm → ˌmɛsˈsjoː.n̪ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌmɛsˈsjoː.n̪ɛm → ˌmɛssˈʝoː.n̪ɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɛssˈʝoː.n̪ɛm → ˌmɛssˈʝo.n̪ɛm   (ˈoː→ˈo)
-100: secondary-stressed ɛ raises to e before ssʝ
    ˌmɛssˈʝo.n̪ɛm → ˌmessˈʝo.n̪ɛm   (ˌɛ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmessˈʝo.n̪ɛm → ˌmessˈʝo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmessˈʝo.n̪ɛ → ˌmessˈʝoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌmessˈʝoː.n̪ɛ → ˌmessˈʝũː.n̪ɛ   (ˈoː→ˈũː)
500: s + high-front consonant becomes geminate palatalized s
    ˌmessˈʝũː.n̪ɛ → ˌmessʲˈsʲũː.n̪ɛ   (s→sʲ, ʝ→sʲ)
500: s + high-front consonant becomes geminate palatalized s (recurrence)
    ˌmessʲˈsʲũː.n̪ɛ → ˌmesʲsʲˈsʲũː.n̪ɛ   (s→sʲ)
500: palatalized s lost before a geminate palatalized s (prevents a triple geminate)
    ˌmesʲsʲˈsʲũː.n̪ɛ → ˌmesʲˈsʲũː.n̪ɛ   (sʲ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmesʲˈsʲũː.n̪ɛ → ˌmesʲˈsʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌmesʲˈsʲũː.n̪ə → ˌmesʲˈsʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmesʲˈsʲũːn̪ə̯ → ˌmesʲˈsʲũːn̪   (ə̯→∅)
600: geminate palatalized s degeminates
    ˌmesʲˈsʲũːn̪ → ˌmeˈsʲũːn̪   (sʲ→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌmeˈsʲũːn̪ → ˌmejˈsũːn̪   (sʲ→js)
750: vowel length resets to short
    ˌmejˈsũːn̪ → ˌmejˈsũn̪   (ˈũː→ˈũ)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌmejˈsũn̪ → ˌmojˈsũn̪   (ˌe→ˌo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌmojˈsũn̪ → ˌmujˈsũn̪   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌmujˈsũn̪ → ˌmuɛ̯ˈsũn̪   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌmuɛ̯ˈsũn̪ → ˌmwɛˈsũn̪   (ˌu→w, ɛ̯→ˌɛ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmwɛˈsũn̪ → ˌmwɛˈsũː   (ˈũn̪→ˈũː)
1400: stress is leveled — no longer distinctive for vowels
    ˌmwɛˈsũː → mwɛ.sũː   (ˌɛ→ɛ, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    mwɛ.sũː → mwɛ.sũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    mwɛ.sũ → mwɛ.sɔ̃   (ũ→ɔ̃)
1400: wɛ becomes wa
    mwɛ.sɔ̃ → mwa.sɔ̃   (ɛ→a)
```

## montagne

`mˌon̪t̪ˈɑːn̪eɑm` → `mɔ̃.t̪aɲ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmon̪ˈt̪ɑː.n̪e.ɑm → ˌmɔn̪ˈt̪ɑː.n̪ɛ.ɑm   (ˌo→ˌɔ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɔn̪ˈt̪ɑː.n̪ɛ.ɑm → ˌmɔn̪ˈt̪ɑː.n̪jɑm   (ɛ→j)
-100: yod strengthens before a vowel
    ˌmɔn̪ˈt̪ɑː.n̪jɑm → ˌmɔn̪ˈt̪ɑːn̪.ʝɑm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɔn̪ˈt̪ɑːn̪.ʝɑm → ˌmɔn̪ˈt̪ɑn̪.ʝɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɔn̪ˈt̪ɑn̪.ʝɑm → ˌmɔn̪ˈt̪ɑn̪.ʝɑ   (m→∅)
300: the coronal nasal palatalizes before yod
    ˌmɔn̪ˈt̪ɑn̪.ʝɑ → ˌmɔn̪ˈt̪ɑ.ɲɑ   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɔn̪ˈt̪ɑ.ɲɑ → ˌmɔn̪ˈt̪ɑː.ɲɑ   (ˈɑ→ˈɑː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌmɔn̪ˈt̪ɑː.ɲɑ → ˌmũn̪ˈt̪ɑː.ɲɑ   (ˌɔ→ˌũ)
500: the low vowel fronts by default
    ˌmũn̪ˈt̪ɑː.ɲɑ → ˌmũn̪ˈt̪aː.ɲa   (ˈɑː→ˈaː, ɑ→a)
600: a vowel shortens before ɲ
    ˌmũn̪ˈt̪aː.ɲa → ˌmũn̪ˈt̪a.ɲa   (ˈaː→ˈa)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌmũn̪ˈt̪a.ɲa → ˌmũn̪ˈt̪a.ɲə   (a→ə)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌmũn̪ˈt̪a.ɲə → ˌmũn̪ˈt̪ã.ɲə   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmũn̪ˈt̪ã.ɲə → ˌmũːˈt̪ã.ɲə   (ˌũn̪→ˌũː)
1400: final ə becomes a non-syllabic off-glide
    ˌmũːˈt̪ã.ɲə → ˌmũːˈt̪ãɲə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌmũːˈt̪ãɲə̯ → ˌmũːˈt̪ãɲ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmũːˈt̪ãɲ → mũː.t̪ãɲ   (ˌũː→ũː, ˈã→ã)
1400: distinctive vowel length is lost entirely
    mũː.t̪ãɲ → mũ.t̪ãɲ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    mũ.t̪ãɲ → mɔ̃.t̪ãɲ   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    mɔ̃.t̪ãɲ → mɔ̃.t̪aɲ   (ã→a)
```

## mourir

`mˌorˈiːri` → `mu.ʁiʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmoˈriː.ri → ˌmɔˈriː.rɪ   (ˌo→ˌɔ, i→ɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɔˈriː.rɪ → ˌmɔˈri.rɪ   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌmɔˈri.rɪ → ˌmɔˈri.re   (ɪ→e)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɔˈri.re → ˌmɔˈriː.re   (ˈi→ˈiː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmɔˈriː.re → ˌmɔˈriː.rə   (e→ə)
600: schwa becomes non-syllabic
    ˌmɔˈriː.rə → ˌmɔˈriːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmɔˈriːrə̯ → ˌmɔˈriːr   (ə̯→∅)
600: secondary-stressed ɔ raises to o unconditionally
    ˌmɔˈriːr → ˌmoˈriːr   (ˌɔ→ˌo)
750: vowel length resets to short
    ˌmoˈriːr → ˌmoˈrir   (ˈiː→ˈi)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌmoˈrir → ˌmuˈrir   (ˌo→ˌu)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmuˈrir → ˌmuˈriɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌmuˈriɹ → ˌmuˈrir   (ɹ→r)
1400: r becomes uvular ʀ
    ˌmuˈrir → ˌmuˈʀiʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌmuˈʀiʀ → mu.ʀiʀ   (ˌu→u, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    mu.ʀiʀ → mu.ʁiʁ   (ʀ→ʁ, ʀ→ʁ)
```

## moyen

`mˌed̪iˈɑːn̪um` → `mwa.jɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌme.d̪iˈɑː.n̪um → ˌmɛ.d̪ɪˈɑː.n̪ʊm   (ˌe→ˌɛ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɛ.d̪ɪˈɑː.n̪ʊm → ˌmɛˈd̪jɑː.n̪ʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌmɛˈd̪jɑː.n̪ʊm → ˌmɛˈd̪ʝɑː.n̪ʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɛˈd̪ʝɑː.n̪ʊm → ˌmɛˈd̪ʝɑ.n̪ʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌmɛˈd̪ʝɑ.n̪ʊm → ˌmɛˈd̪ʝɑ.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɛˈd̪ʝɑ.n̪om → ˌmɛˈd̪ʝɑ.n̪o   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌmɛˈd̪ʝɑ.n̪o → ˌmɛˈɟʝɑ.n̪o   (d̪→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌmɛˈɟʝɑ.n̪o → ˌmɛʝˈʝɑ.n̪o   (ɟ→ʝ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɛʝˈʝɑ.n̪o → ˌmɛʝˈʝɑː.n̪o   (ˈɑ→ˈɑː)
500: secondary-stressed ɛ/ɔ become tense before geminate yod
    ˌmɛʝˈʝɑː.n̪o → ˌmeʝˈʝɑː.n̪o   (ˌɛ→ˌe)
500: yod degeminates (lost before another yod)
    ˌmeʝˈʝɑː.n̪o → ˌmeˈʝɑː.n̪o   (ʝ→∅)
500: the low vowel fronts by default
    ˌmeˈʝɑː.n̪o → ˌmeˈʝaː.n̪o   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmeˈʝaː.n̪o → ˌmeˈʝaː.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌmeˈʝaː.n̪ə → ˌmeˈʝaːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmeˈʝaːn̪ə̯ → ˌmeˈʝaːn̪   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌmeˈʝaːn̪ → ˌmeˈʝɛːn̪   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌmeˈʝɛːn̪ → ˌmeˈʝie̯n̪   (ˈɛː→ˈie̯)
600: ʝ weakens to j unconditionally
    ˌmeˈʝie̯n̪ → ˌmeˈjie̯n̪   (ʝ→j)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌmeˈjie̯n̪ → ˌməˈjie̯n̪   (ˌe→ˌə)
1000: secondary-stressed schwa reverts to e before a palatal consonant
    ˌməˈjie̯n̪ → ˌmeˈjie̯n̪   (ˌə→ˌe)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌmeˈjie̯n̪ → ˌmoˈjie̯n̪   (ˌe→ˌo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌmoˈjie̯n̪ → ˌmuˈjie̯n̪   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌmuˈjie̯n̪ → ˌmuˈɛ̯ie̯n̪   (j→ɛ̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌmuˈɛ̯ie̯n̪ → ˌmuɛ̯ˈjen̪   (ˈi→j, e̯→ˈe)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˌmuɛ̯ˈjen̪ → ˌmuɛ̯ˈjẽn̪   (ˈe→ˈẽ)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌmuɛ̯ˈjẽn̪ → ˌmwɛˈjẽn̪   (ˌu→w, ɛ̯→ˌɛ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmwɛˈjẽn̪ → ˌmwɛˈjẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˌmwɛˈjẽː → ˌmwɛˈjɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌmwɛˈjɛ̃ː → mwɛ.jɛ̃ː   (ˌɛ→ɛ, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    mwɛ.jɛ̃ː → mwɛ.jɛ̃   (ɛ̃ː→ɛ̃)
1400: wɛ becomes wa
    mwɛ.jɛ̃ → mwa.jɛ̃   (ɛ→a)
```

## moyeu

`mˌod̪iˈolum` → `mwa.œl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmo.d̪iˈo.lum → ˌmɔ.d̪ɪˈɔ.lʊm   (ˌo→ˌɔ, i→ɪ, ˈo→ˈɔ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmɔ.d̪ɪˈɔ.lʊm → ˌmɔˈd̪jɔ.lʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌmɔˈd̪jɔ.lʊm → ˌmɔˈd̪ʝɔ.lʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˌmɔˈd̪ʝɔ.lʊm → ˌmɔˈd̪ʝɔ.lom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌmɔˈd̪ʝɔ.lom → ˌmɔˈd̪ʝɔ.lo   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌmɔˈd̪ʝɔ.lo → ˌmɔˈɟʝɔ.lo   (d̪→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌmɔˈɟʝɔ.lo → ˌmɔʝˈʝɔ.lo   (ɟ→ʝ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɔʝˈʝɔ.lo → ˌmɔʝˈʝɔː.lo   (ˈɔ→ˈɔː)
500: secondary-stressed ɛ/ɔ become tense before geminate yod
    ˌmɔʝˈʝɔː.lo → ˌmoʝˈʝɔː.lo   (ˌɔ→ˌo)
500: yod degeminates (lost before another yod)
    ˌmoʝˈʝɔː.lo → ˌmoˈʝɔː.lo   (ʝ→∅)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˌmoˈʝɔː.lo → ˌmoˈʝuo̯.lo   (ˈɔː→ˈuo̯)
500: a high tense round non-nasal vowel centralizes
    ˌmoˈʝuo̯.lo → ˌmoˈʝʉo̯.lo   (ˈu→ˈʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmoˈʝʉo̯.lo → ˌmoˈʝʉo̯.lə   (o→ə)
600: schwa becomes non-syllabic
    ˌmoˈʝʉo̯.lə → ˌmoˈʝʉo̯lə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmoˈʝʉo̯lə̯ → ˌmoˈʝʉo̯l   (ə̯→∅)
600: ʝ weakens to j unconditionally
    ˌmoˈʝʉo̯l → ˌmoˈjʉo̯l   (ʝ→j)
1000: high round back vowels front (completion of u-fronting)
    ˌmoˈjʉo̯l → ˌmoˈjyo̯l   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˌmoˈjyo̯l → ˌmoˈjye̯l   (o̯→e̯)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌmoˈjye̯l → ˌmuˈjye̯l   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌmuˈjye̯l → ˌmuˈɛ̯ye̯l   (j→ɛ̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˌmuˈɛ̯ye̯l → ˌmuˈɛ̯øl   (ˈye̯→ˈø)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌmuˈɛ̯øl → ˌmwɛˈøl   (ˌu→w, ɛ̯→ˌɛ)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˌmwɛˈøl → ˌmwɛˈœl   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˌmwɛˈœl → mwɛ.œl   (ˌɛ→ɛ, ˈœ→œ)
1400: wɛ becomes wa
    mwɛ.œl → mwa.œl   (ɛ→a)
```

## mur

`mˈuːrum` → `myʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmuː.rum → ˈmuː.rʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈmuː.rʊm → ˈmu.rʊm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˈmu.rʊm → ˈmu.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmu.rom → ˈmu.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈmu.ro → ˈmuː.ro   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈmuː.ro → ˈmʉː.ro   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmʉː.ro → ˈmʉː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈmʉː.rə → ˈmʉːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmʉːrə̯ → ˈmʉːr   (ə̯→∅)
750: vowel length resets to short
    ˈmʉːr → ˈmʉr   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈmʉr → ˈmyr   (ˈʉ→ˈy)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈmyr → ˈmyɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈmyɹ → ˈmyr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈmyr → ˈmyʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈmyʀ → myʀ   (ˈy→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    myʀ → myʁ   (ʀ→ʁ)
```

## muraille

`mˌuːrˈɑːliɑ` → `my.ʁɑj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmuːˈrɑː.li.ɑ → ˌmuːˈrɑː.lɪ.ɑ   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌmuːˈrɑː.lɪ.ɑ → ˌmuːˈrɑː.ljɑ   (ɪ→j)
-100: l darkens before a non-lateral consonant
    ˌmuːˈrɑː.ljɑ → ˌmuːˈrɑː.ɫjɑ   (l→ɫ)
-100: yod strengthens before a vowel
    ˌmuːˈrɑː.ɫjɑ → ˌmuːˈrɑːɫ.ʝɑ   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmuːˈrɑːɫ.ʝɑ → ˌmuˈrɑɫ.ʝɑ   (ˌuː→ˌu, ˈɑː→ˈɑ)
300: l palatalizes to ʎ before yod
    ˌmuˈrɑɫ.ʝɑ → ˌmuˈrɑ.ʎɑ   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmuˈrɑ.ʎɑ → ˌmuˈrɑː.ʎɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌmuˈrɑː.ʎɑ → ˌmuˈraː.ʎa   (ˈɑː→ˈaː, ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˌmuˈraː.ʎa → ˌmʉˈraː.ʎa   (ˌu→ˌʉ)
600: long stressed vowels diphthongize
    ˌmʉˈraː.ʎa → ˌmʉˈrae̯.ʎa   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˌmʉˈrae̯.ʎa → ˌmʉˈra.ʎa   (e̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌmʉˈra.ʎa → ˌmʉˈra.ʎə   (a→ə)
1000: high round back vowels front (completion of u-fronting)
    ˌmʉˈra.ʎə → ˌmyˈra.ʎə   (ˌʉ→ˌy)
1400: a lengthens before final ʎə
    ˌmyˈra.ʎə → ˌmyˈraː.ʎə   (ˈa→ˈaː)
1400: final ə becomes a non-syllabic off-glide
    ˌmyˈraː.ʎə → ˌmyˈraːʎə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌmyˈraːʎə̯ → ˌmyˈrɑːʎə̯   (ˈaː→ˈɑː)
1400: the final off-glide schwa is deleted elsewhere
    ˌmyˈrɑːʎə̯ → ˌmyˈrɑːʎ   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌmyˈrɑːʎ → ˌmyˈʀɑːʎ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌmyˈʀɑːʎ → my.ʀɑːʎ   (ˌy→y, ˈɑː→ɑː)
1400: distinctive vowel length is lost entirely
    my.ʀɑːʎ → my.ʀɑʎ   (ɑː→ɑ)
1400: the uvular trill ʀ becomes a fricative ʁ
    my.ʀɑʎ → my.ʁɑʎ   (ʀ→ʁ)
1400: ʎ becomes j
    my.ʁɑʎ → my.ʁɑj   (ʎ→j)
```

## mère

`mˈɑt̪rem` → `mɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈmɑ.t̪rem → ˈmɑ.t̪rɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈmɑ.t̪rɛm → ˈmɑ.t̪rɛ   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈmɑ.t̪rɛ → ˈmɑː.t̪rɛ   (ˈɑ→ˈɑː)
500: a vowel shortens before a consonant cluster
    ˈmɑː.t̪rɛ → ˈmɑ.t̪rɛ   (ˈɑː→ˈɑ)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant
    ˈmɑ.t̪rɛ → ˈmɑː.t̪rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈmɑː.t̪rɛ → ˈmaː.t̪rɛ   (ˈɑː→ˈaː)
500: a vowel shortens before a consonant cluster (recurrence)
    ˈmaː.t̪rɛ → ˈma.t̪rɛ   (ˈaː→ˈa)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant (recurrence)
    ˈma.t̪rɛ → ˈmaː.t̪rɛ   (ˈa→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈmaː.t̪rɛ → ˈmaː.t̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈmaː.t̪rə → ˈmaːt̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈmaːt̪rə̯ → ˈmaːt̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈmaːt̪r → ˈmaː.t̪rə   (∅→ə)
600: a voiceless anterior consonant voices before a coronal sonorant non-nasal consonant
    ˈmaː.t̪rə → ˈmaː.d̪rə   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈmaː.d̪rə → ˈmaː.ðrə   (d̪→ð)
600: long stressed vowels diphthongize
    ˈmaː.ðrə → ˈmae̯.ðrə   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈmae̯.ðrə → ˈmeː.ðrə   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈmeː.ðrə → ˈme.ðrə   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˈme.ðrə → ˈme.rə   (ð→∅)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈme.rə → ˈmɛ.rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈmɛ.rə → ˈmɛrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈmɛrə̯ → ˈmɛr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈmɛr → ˈmɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈmɛʀ → mɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    mɛʀ → mɛʁ   (ʀ→ʁ)
```

## mêler

`mˌiskulˈɑːre` → `mɛ.le`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmis.kuˈlɑː.re → ˌmɪs.kʊˈlɑː.rɛ   (ˌi→ˌɪ, u→ʊ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌmɪs.kʊˈlɑː.rɛ → ˌmɪs.kʊˈlɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌmɪs.kʊˈlɑ.rɛ → ˌmes.koˈlɑ.rɛ   (ˌɪ→ˌe, ʊ→o)
300: a stressed vowel lengthens before a single consonant + glide
    ˌmes.koˈlɑ.rɛ → ˌmes.koˈlɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌmes.koˈlɑː.rɛ → ˌmes.koˈlaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + a primary-stressed low vowel
    ˌmes.koˈlaː.rɛ → ˌmes.kəˈlaː.rɛ   (o→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmes.kəˈlaː.rɛ → ˌmes.kəˈlaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌmes.kəˈlaː.rə → ˌmeskə̯ˈlaːrə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmeskə̯ˈlaːrə̯ → ˌmesˈklaːr   (ˈə̯laːrə̯→ˈlaːr)
600: long stressed vowels diphthongize
    ˌmesˈklaːr → ˌmesˈklae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌmesˈklae̯r → ˌmesˈkleːr   (ˈae̯→ˈeː)
750: the s-velar-l cluster (skl) loses its velar and voices the s, intervocalically
    ˌmesˈkleːr → ˌmeˈzleːr   (sk→z)
1000: vowel length resets to short
    ˌmeˈzleːr → ˌmeˈzler   (ˈeː→ˈe)
1000: a stressed vowel lengthens before z + one consonant + a vowel
    ˌmeˈzler → ˌmeːˈzler   (ˌe→ˌeː)
1000: z is lost before a consonant (preconsonantal effacement)
    ˌmeːˈzler → ˌmeːˈler   (z→∅)
1400: e lowers to ɛ before a lateral
    ˌmeːˈler → ˌmɛːˈler   (ˌeː→ˌɛː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmɛːˈler → ˌmɛːˈleɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌmɛːˈleɹ → ˌmɛːˈle   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɛːˈle → mɛː.le   (ˌɛː→ɛː, ˈe→e)
1400: distinctive vowel length is lost entirely
    mɛː.le → mɛ.le   (ɛː→ɛ)
```

## neveu

`n̪ˌepˈoːt̪em` → `n̪ə.vø`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌn̪eˈpoː.t̪em → ˌn̪ɛˈpoː.t̪ɛm   (ˌe→ˌɛ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌn̪ɛˈpoː.t̪ɛm → ˌn̪ɛˈpo.t̪ɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌn̪ɛˈpo.t̪ɛm → ˌn̪ɛˈpo.t̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌn̪ɛˈpo.t̪ɛ → ˌn̪ɛˈpoː.t̪ɛ   (ˈo→ˈoː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌn̪ɛˈpoː.t̪ɛ → ˌn̪ɛˈpoː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌn̪ɛˈpoː.t̪ə → ˌn̪ɛˈpoːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌn̪ɛˈpoːt̪ə̯ → ˌn̪ɛˈpoːt̪   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌn̪ɛˈpoːt̪ → ˌn̪ɛˈboːt̪   (p→b)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌn̪ɛˈboːt̪ → ˌn̪ɛˈβoːt̪   (b→β)
600: long stressed vowels diphthongize
    ˌn̪ɛˈβoːt̪ → ˌn̪ɛˈβowt̪   (ˈoː→ˈow)
600: secondary-stressed ɛ raises to e before any two segments
    ˌn̪ɛˈβowt̪ → ˌn̪eˈβowt̪   (ˌɛ→ˌe)
600: the remaining bilabial fricative becomes v
    ˌn̪eˈβowt̪ → ˌn̪eˈvowt̪   (β→v)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌn̪eˈvowt̪ → ˌn̪əˈvowt̪   (ˌe→ˌə)
1000: stressed o becomes e before a high back round glide
    ˌn̪əˈvowt̪ → ˌn̪əˈvewt̪   (ˈo→ˈe)
1000: ew becomes øw
    ˌn̪əˈvewt̪ → ˌn̪əˈvøwt̪   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˌn̪əˈvøwt̪ → ˌn̪əˈvøt̪   (w→∅)
1400: final obstruents are lost
    ˌn̪əˈvøt̪ → ˌn̪əˈvø   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌn̪əˈvø → n̪ə.vø   (ˌə→ə, ˈø→ø)
```

## nez

`n̪ˈɑːsum` → `n̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪ɑː.sum → ˈn̪ɑː.sʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈn̪ɑː.sʊm → ˈn̪ɑ.sʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˈn̪ɑ.sʊm → ˈn̪ɑ.som   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪ɑ.som → ˈn̪ɑ.so   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈn̪ɑ.so → ˈn̪ɑː.so   (ˈɑ→ˈɑː)
500: a voiceless fricative voices intervocalically
    ˈn̪ɑː.so → ˈn̪ɑː.zo   (s→z)
500: the low vowel fronts by default
    ˈn̪ɑː.zo → ˈn̪aː.zo   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪aː.zo → ˈn̪aː.zə   (o→ə)
600: schwa becomes non-syllabic
    ˈn̪aː.zə → ˈn̪aːzə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪aːzə̯ → ˈn̪aːz   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈn̪aːz → ˈn̪ae̯z   (ˈaː→ˈae̯)
750: all final obstruents devoice
    ˈn̪ae̯z → ˈn̪ae̯s   (z→s)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈn̪ae̯s → ˈn̪eːs   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈn̪eːs → ˈn̪es   (ˈeː→ˈe)
1000: a primary-stressed vowel lengthens before word-final s
    ˈn̪es → ˈn̪eːs   (ˈe→ˈeː)
1400: final obstruents are lost
    ˈn̪eːs → ˈn̪eː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪eː → n̪eː   (ˈeː→eː)
1400: distinctive vowel length is lost entirely
    n̪eː → n̪e   (eː→e)
```

## noir

`n̪ˈigrum` → `n̪waʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪i.grum → ˈn̪ɪ.grʊm   (ˈi→ˈɪ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈn̪ɪ.grʊm → ˈn̪e.grom   (ˈɪ→ˈe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪e.grom → ˈn̪e.gro   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈn̪e.gro → ˈn̪e.ɣro   (g→ɣ)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈn̪e.ɣro → ˈn̪e.ʝro   (ɣ→ʝ)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈn̪e.ʝro → ˈn̪e.ʝrʲo   (r→rʲ)
600: yod lost before ʎ or palatalized r
    ˈn̪e.ʝrʲo → ˈn̪e.rʲo   (ʝ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪e.rʲo → ˈn̪e.rʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈn̪e.rʲə → ˈn̪erʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪erʲə̯ → ˈn̪erʲ   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˈn̪erʲ → ˈn̪ejrʲ   (∅→j)
600: a stressed vowel lengthens before j + optional consonants + a high-front coronal
    ˈn̪ejrʲ → ˈn̪eːjrʲ   (ˈe→ˈeː)
600: palatalized r depalatalizes
    ˈn̪eːjrʲ → ˈn̪eːjr   (rʲ→r)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˈn̪eːjr → ˈn̪ejr   (ˈeː→ˈe)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈn̪ejr → ˈn̪ojr   (ˈe→ˈo)
1000: j lowers to ɛ̯ before r, in a back round diphthong
    ˈn̪ojr → ˈn̪oɛ̯r   (j→ɛ̯)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈn̪oɛ̯r → ˈn̪uɛ̯r   (ˈo→ˈu)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈn̪uɛ̯r → ˈn̪wɛr   (ˈu→w, ɛ̯→ˈɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈn̪wɛr → ˈn̪wɛɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈn̪wɛɹ → ˈn̪wɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈn̪wɛr → ˈn̪wɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪wɛʀ → n̪wɛʀ   (ˈɛ→ɛ)
1400: wɛ becomes wa
    n̪wɛʀ → n̪waʀ   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    n̪waʀ → n̪waʁ   (ʀ→ʁ)
```

## noix

`n̪ˈukem` → `n̪wa`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪u.kem → ˈn̪ʊ.kɛm   (ˈu→ˈʊ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈn̪ʊ.kɛm → ˈn̪o.kɛm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪o.kɛm → ˈn̪o.kɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈn̪o.kɛ → ˈn̪o.kʲɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈn̪o.kʲɛ → ˈn̪o.cɛ   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˈn̪o.cɛ → ˈn̪oː.cɛ   (ˈo→ˈoː)
500: a palatal stop affricates
    ˈn̪oː.cɛ → ˈn̪oː.t͡sʲɛ   (c→t͡sʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪oː.t͡sʲɛ → ˈn̪oː.t͡sʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈn̪oː.t͡sʲə → ˈn̪oːt͡sʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪oːt͡sʲə̯ → ˈn̪oːt͡sʲ   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈn̪oːt͡sʲ → ˈn̪owt͡sʲ   (ˈoː→ˈow)
600: w becomes j after a round vowel before tsʲ
    ˈn̪owt͡sʲ → ˈn̪ojt͡sʲ   (w→j)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈn̪ojt͡sʲ → ˈn̪ujt͡sʲ   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈn̪ujt͡sʲ → ˈn̪uɛ̯t͡sʲ   (j→ɛ̯)
1000: all affricates become sibilants (deaffrication)
    ˈn̪uɛ̯t͡sʲ → ˈn̪uɛ̯sʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈn̪uɛ̯sʲ → ˈn̪uɛ̯s   (sʲ→s)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈn̪uɛ̯s → ˈn̪wɛs   (ˈu→w, ɛ̯→ˈɛ)
1400: final obstruents are lost
    ˈn̪wɛs → ˈn̪wɛ   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪wɛ → n̪wɛ   (ˈɛ→ɛ)
1400: wɛ becomes wa
    n̪wɛ → n̪wa   (ɛ→a)
```

## nu

`n̪ˈuːd̪um` → `n̪y`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪uː.d̪um → ˈn̪uː.d̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈn̪uː.d̪ʊm → ˈn̪u.d̪ʊm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˈn̪u.d̪ʊm → ˈn̪u.d̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪u.d̪om → ˈn̪u.d̪o   (m→∅)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈn̪u.d̪o → ˈn̪u.ðo   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈn̪u.ðo → ˈn̪uː.ðo   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈn̪uː.ðo → ˈn̪ʉː.ðo   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪ʉː.ðo → ˈn̪ʉː.ðə   (o→ə)
600: schwa becomes non-syllabic
    ˈn̪ʉː.ðə → ˈn̪ʉːðə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪ʉːðə̯ → ˈn̪ʉːð   (ə̯→∅)
750: all final obstruents devoice
    ˈn̪ʉːð → ˈn̪ʉːθ   (ð→θ)
750: vowel length resets to short
    ˈn̪ʉːθ → ˈn̪ʉθ   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈn̪ʉθ → ˈn̪yθ   (ˈʉ→ˈy)
1000: the interdental fricatives (plain and palatalized) efface
    ˈn̪yθ → ˈn̪y   (θ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪y → n̪y   (ˈy→y)
```

## nue

`n̪ˈuːd̪ɑm` → `n̪y`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈn̪uː.d̪ɑm → ˈn̪u.d̪ɑm   (ˈuː→ˈu)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪u.d̪ɑm → ˈn̪u.d̪ɑ   (m→∅)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈn̪u.d̪ɑ → ˈn̪u.ðɑ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈn̪u.ðɑ → ˈn̪uː.ðɑ   (ˈu→ˈuː)
500: the low vowel fronts by default
    ˈn̪uː.ðɑ → ˈn̪uː.ða   (ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˈn̪uː.ða → ˈn̪ʉː.ða   (ˈuː→ˈʉː)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈn̪ʉː.ða → ˈn̪ʉː.ðə   (a→ə)
750: vowel length resets to short
    ˈn̪ʉː.ðə → ˈn̪ʉ.ðə   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈn̪ʉ.ðə → ˈn̪y.ðə   (ˈʉ→ˈy)
1000: the interdental fricatives (plain and palatalized) efface
    ˈn̪y.ðə → ˈn̪y.ə   (ð→∅)
1200: schwa desyllabifies after another vowel
    ˈn̪y.ə → ˈn̪yə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈn̪yə̯ → ˈn̪yː   (ˈyə̯→ˈyː)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪yː → n̪yː   (ˈyː→yː)
1400: distinctive vowel length is lost entirely
    n̪yː → n̪y   (yː→y)
```

## nuit

`n̪ˈokt̪em` → `n̪ɥi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪ok.t̪em → ˈn̪ɔk.t̪ɛm   (ˈo→ˈɔ, e→ɛ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈn̪ɔk.t̪ɛm → ˈn̪ɔx.t̪ɛm   (k→x)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪ɔx.t̪ɛm → ˈn̪ɔx.t̪ɛ   (m→∅)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈn̪ɔx.t̪ɛ → ˈn̪ɔç.t̪ɛ   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈn̪ɔç.t̪ɛ → ˈn̪ɔç.t̪ʲɛ   (t̪→t̪ʲ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈn̪ɔç.t̪ʲɛ → ˈn̪uo̯ç.t̪ʲɛ   (ˈɔ→ˈuo̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪uo̯ç.t̪ʲɛ → ˈn̪uo̯ç.t̪ʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈn̪uo̯ç.t̪ʲə → ˈn̪uo̯çt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪uo̯çt̪ʲə̯ → ˈn̪uo̯çt̪ʲ   (ə̯→∅)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈn̪uo̯çt̪ʲ → ˈn̪ʉo̯çt̪ʲ   (ˈu→ˈʉ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈn̪ʉo̯çt̪ʲ → ˈn̪ʉo̯çjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈn̪ʉo̯çjt̪ → ˈn̪ʉo̯çt̪   (j→∅)
750: ç merges into ʝ
    ˈn̪ʉo̯çt̪ → ˈn̪ʉo̯ʝt̪   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈn̪ʉo̯ʝt̪ → ˈn̪ʉo̯jt̪   (ʝ→j)
1000: high round back vowels front (completion of u-fronting)
    ˈn̪ʉo̯jt̪ → ˈn̪yo̯jt̪   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈn̪yo̯jt̪ → ˈn̪ye̯jt̪   (o̯→e̯)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈn̪ye̯jt̪ → ˈn̪yjt̪   (e̯→∅)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˈn̪yjt̪ → ˈn̪ɥit̪   (ˈy→ɥ, j→ˈi)
1400: final obstruents are lost
    ˈn̪ɥit̪ → ˈn̪ɥi   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪ɥi → n̪ɥi   (ˈi→i)
```

## nul

`n̪ˈuːllum` → `n̪yl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪uːl.lum → ˈn̪uːl.lʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈn̪uːl.lʊm → ˈn̪ul.lʊm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˈn̪ul.lʊm → ˈn̪ul.lom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪ul.lom → ˈn̪ul.lo   (m→∅)
500: a high tense round non-nasal vowel centralizes
    ˈn̪ul.lo → ˈn̪ʉl.lo   (ˈu→ˈʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪ʉl.lo → ˈn̪ʉl.lə   (o→ə)
600: schwa becomes non-syllabic
    ˈn̪ʉl.lə → ˈn̪ʉllə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪ʉllə̯ → ˈn̪ʉll   (ə̯→∅)
750: an identical consonant geminate reduces to one (recurrence)
    ˈn̪ʉll → ˈn̪ʉl   (l→∅)
1000: high round back vowels front (completion of u-fronting)
    ˈn̪ʉl → ˈn̪yl   (ˈʉ→ˈy)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪yl → n̪yl   (ˈy→y)
```

## nœud

`n̪ˈoːd̪um` → `n̪ø`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈn̪oː.d̪um → ˈn̪oː.d̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈn̪oː.d̪ʊm → ˈn̪o.d̪ʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ˈn̪o.d̪ʊm → ˈn̪o.d̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈn̪o.d̪om → ˈn̪o.d̪o   (m→∅)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈn̪o.d̪o → ˈn̪o.ðo   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈn̪o.ðo → ˈn̪oː.ðo   (ˈo→ˈoː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈn̪oː.ðo → ˈn̪oː.ðə   (o→ə)
600: schwa becomes non-syllabic
    ˈn̪oː.ðə → ˈn̪oːðə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈn̪oːðə̯ → ˈn̪oːð   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈn̪oːð → ˈn̪owð   (ˈoː→ˈow)
750: all final obstruents devoice
    ˈn̪owð → ˈn̪owθ   (ð→θ)
750: a supported non-strident fricative closes to a stop word-finally
    ˈn̪owθ → ˈn̪owt̪   (θ→t̪)
1000: stressed o becomes e before a high back round glide
    ˈn̪owt̪ → ˈn̪ewt̪   (ˈo→ˈe)
1000: ew becomes øw
    ˈn̪ewt̪ → ˈn̪øwt̪   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈn̪øwt̪ → ˈn̪øt̪   (w→∅)
1400: final obstruents are lost
    ˈn̪øt̪ → ˈn̪ø   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪ø → n̪ø   (ˈø→ø)
```

## oiseaux

`ˌɑwikˈelloːs` → `o.zo`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌɑ.wiˈkel.loːs → ˌɑ.ɣʷiˈkel.loːs   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑ.ɣʷiˈkel.loːs → ˌɑ.ɣʷɪˈkɛl.loːs   (i→ɪ, ˈe→ˈɛ)
-100: ɪ lost between the labiovelar approximant and k
    ˌɑ.ɣʷɪˈkɛl.loːs → ˌɑɣʷˈkɛl.loːs   (ɪ→∅)
-100: the labiovelar approximant simplifies to w before a consonant
    ˌɑɣʷˈkɛl.loːs → ˌɑwˈkɛl.loːs   (ɣʷ→w)
-100: the length feature is dropped now that quality carries the contrast
    ˌɑwˈkɛl.loːs → ˌɑwˈkɛl.los   (oː→o)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌɑwˈkɛl.los → ˌɑwˈkʲɛl.los   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌɑwˈkʲɛl.los → ˌɑwˈcɛl.los   (kʲ→c)
500: a palatal stop affricates
    ˌɑwˈcɛl.los → ˌɑwˈt͡sʲɛl.los   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌɑwˈt͡sʲɛl.los → ˌawˈt͡sʲɛl.los   (ˌɑ→ˌa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌawˈt͡sʲɛl.los → ˌɔwˈt͡sʲɛl.los   (ˌa→ˌɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɔwˈt͡sʲɛl.los → ˌɔwˈt͡sʲɛl.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˌɔwˈt͡sʲɛl.ləs → ˌɔwˈt͡sʲɛllə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌɔwˈt͡sʲɛllə̯s → ˌɔwˈt͡sʲɛlls   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˌɔwˈt͡sʲɛlls → ˌɔwˈt͡sʲɛls   (l→∅)
600: a voiceless consonant voices intervocalically
    ˌɔwˈt͡sʲɛls → ˌɔwˈd͡zʲɛls   (t͡sʲ→d͡zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌɔwˈd͡zʲɛls → ˌɔwjˈd͡zɛls   (d͡zʲ→jd͡z)
600: j is lost after j or a consonant, before a consonant
    ˌɔwjˈd͡zɛls → ˌɔwˈd͡zɛls   (j→∅)
600: secondary-stressed ɔ raises to ɯ before w
    ˌɔwˈd͡zɛls → ˌɯwˈd͡zɛls   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌɯwˈd͡zɛls → ˌɔwˈd͡zɛls   (ˌɯ→ˌɔ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌɔwˈd͡zɛls → ˌɔˈd͡zɛls   (w→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌɔˈd͡zɛls → ˌɔˈd͡zɛɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˌɔˈd͡zɛɫs → ˌɔˈd͡zɛws   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌɔˈd͡zɛws → ˌɔˈd͡zɛa̯ws   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌɔˈd͡zɛa̯ws → ˌɔˈd͡ze̯aws   (ˈɛ→e̯, a̯→ˈa)
1000: all affricates become sibilants (deaffrication)
    ˌɔˈd͡ze̯aws → ˌɔˈze̯aws   (d͡z→z)
1200: aw becomes long oː
    ˌɔˈze̯aws → ˌɔˈze̯oːs   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌɔˈze̯oːs → ˌɔˈzə̯oːs   (e̯→ə̯)
1200: lax back mid o lengthens before z or v
    ˌɔˈzə̯oːs → ˌɔːˈzə̯oːs   (ˌɔ→ˌɔː)
1200: a long back mid o tenses to oː
    ˌɔːˈzə̯oːs → ˌoːˈzə̯oːs   (ˌɔː→ˌoː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌoːˈzə̯oːs → ˌoːˈzoːs   (ə̯→∅)
1400: final obstruents are lost
    ˌoːˈzoːs → ˌoːˈzoː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌoːˈzoː → oː.zoː   (ˌoː→oː, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    oː.zoː → o.zo   (oː→o, oː→o)
```

## ongle

`ˈun̪gulɑm` → `ɔ̃gl`

```
-100: n assimilates to a following velar stop
    ˈun̪.gu.lɑm → ˈuŋ.gu.lɑm   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈuŋ.gu.lɑm → ˈʊŋ.gʊ.lɑm   (ˈu→ˈʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈʊŋ.gʊ.lɑm → ˈʊŋ.glɑm   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈʊŋ.glɑm → ˈoŋ.glɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈoŋ.glɑm → ˈoŋ.glɑ   (m→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈoŋ.glɑ → ˈũŋ.glɑ   (ˈo→ˈũ)
500: the low vowel fronts by default
    ˈũŋ.glɑ → ˈũŋ.gla   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈũŋ.gla → ˈũŋ.glə   (a→ə)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈũŋ.glə → ˈũː.glə   (ˈũŋ→ˈũː)
1400: final ə becomes a non-syllabic off-glide
    ˈũː.glə → ˈũːglə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈũːglə̯ → ˈũːgl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈũːgl → ũːgl   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    ũːgl → ũgl   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    ũgl → ɔ̃gl   (ũ→ɔ̃)
```

## ourse

`ˈursɑm` → `uʁs`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈur.sɑm → ˈʊr.sɑm   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈʊr.sɑm → ˈor.sɑm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈor.sɑm → ˈor.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈor.sɑ → ˈor.sa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈor.sa → ˈor.sə   (a→ə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈor.sə → ˈur.sə   (ˈo→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈur.sə → ˈursə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈursə̯ → ˈuɹsə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˈuɹsə̯ → ˈuɹs   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈuɹs → ˈurs   (ɹ→r)
1400: r becomes uvular ʀ
    ˈurs → ˈuʀs   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈuʀs → uʀs   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    uʀs → uʁs   (ʀ→ʁ)
```

## ouvrier

`ˌoperˈɑːrium` → `uv.ʁi.je`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌo.peˈrɑː.ri.um → ˌɔ.pɛˈrɑː.rɪ.ʊm   (ˌo→ˌɔ, e→ɛ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌɔ.pɛˈrɑː.rɪ.ʊm → ˌɔ.pɛˈrɑː.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌɔ.pɛˈrɑː.rjʊm → ˌɔ.pɛˈrɑːr.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɔ.pɛˈrɑːr.ʝʊm → ˌɔ.pɛˈrɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌɔ.pɛˈrɑr.ʝʊm → ˌɔ.pɛˈrɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɔ.pɛˈrɑr.ʝom → ˌɔ.pɛˈrɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌɔ.pɛˈrɑr.ʝo → ˌɔ.pɛˈrɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌɔ.pɛˈrɑ.rʲo → ˌɔ.pɛˈra.rʲo   (ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌɔ.pɛˈra.rʲo → ˌɔ.pɛˈraː.rʲo   (ˈa→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + a primary-stressed low vowel
    ˌɔ.pɛˈraː.rʲo → ˌɔ.pəˈraː.rʲo   (ɛ→ə)
600: aːrʲ metathesizes to jɛːr
    ˌɔ.pəˈraː.rʲo → ˌɔ.pəˈrjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɔ.pəˈrjɛː.ro → ˌɔ.pəˈrjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌɔ.pəˈrjɛː.rə → ˌɔpə̯ˈrjɛːrə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌɔpə̯ˈrjɛːrə̯ → ˌɔˈprjɛːr   (ˈə̯rjɛːrə̯→ˈrjɛːr)
600: a voiceless anterior consonant voices before a coronal sonorant non-nasal consonant
    ˌɔˈprjɛːr → ˌɔˈbrjɛːr   (p→b)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌɔˈbrjɛːr → ˌɔˈbrjie̯r   (ˈɛː→ˈie̯)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌɔˈbrjie̯r → ˌɔˈβrjie̯r   (b→β)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌɔˈβrjie̯r → ˌɔˈβrie̯r   (j→∅)
600: secondary-stressed ɔ raises to o unconditionally
    ˌɔˈβrie̯r → ˌoˈβrie̯r   (ˌɔ→ˌo)
600: the remaining bilabial fricative becomes v
    ˌoˈβrie̯r → ˌoˈvrie̯r   (β→v)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌoˈvrie̯r → ˌuˈvrie̯r   (ˌo→ˌu)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌuˈvrie̯r → ˌuˈvrjer   (ˈi→j, e̯→ˈe)
1400: je becomes ije (diaeresis) after a consonant + liquid
    ˌuˈvrjer → ˌu.vriˈjer   (∅→i)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌu.vriˈjer → ˌu.vriˈjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌu.vriˈjeɹ → ˌu.vriˈje   (ɹ→∅)
1400: r becomes uvular ʀ
    ˌu.vriˈje → ˌu.vʀiˈje   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌu.vʀiˈje → u.vʀi.je   (ˌu→u, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    u.vʀi.je → uv.ʁi.je   (ʀ→ʁ)
```

## paille

`pˈɑleɑm` → `pɑj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpɑ.le.ɑm → ˈpɑ.lɛ.ɑm   (e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈpɑ.lɛ.ɑm → ˈpɑ.ljɑm   (ɛ→j)
-100: l darkens before a non-lateral consonant
    ˈpɑ.ljɑm → ˈpɑ.ɫjɑm   (l→ɫ)
-100: yod strengthens before a vowel
    ˈpɑ.ɫjɑm → ˈpɑɫ.ʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpɑɫ.ʝɑm → ˈpɑɫ.ʝɑ   (m→∅)
300: l palatalizes to ʎ before yod
    ˈpɑɫ.ʝɑ → ˈpɑ.ʎɑ   (ɫʝ→ʎ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpɑ.ʎɑ → ˈpɑː.ʎɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈpɑː.ʎɑ → ˈpaː.ʎa   (ˈɑː→ˈaː, ɑ→a)
600: long stressed vowels diphthongize
    ˈpaː.ʎa → ˈpae̯.ʎa   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˈpae̯.ʎa → ˈpa.ʎa   (e̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpa.ʎa → ˈpa.ʎə   (a→ə)
1400: a lengthens before final ʎə
    ˈpa.ʎə → ˈpaː.ʎə   (ˈa→ˈaː)
1400: final ə becomes a non-syllabic off-glide
    ˈpaː.ʎə → ˈpaːʎə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈpaːʎə̯ → ˈpɑːʎə̯   (ˈaː→ˈɑː)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɑːʎə̯ → ˈpɑːʎ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɑːʎ → pɑːʎ   (ˈɑː→ɑː)
1400: distinctive vowel length is lost entirely
    pɑːʎ → pɑʎ   (ɑː→ɑ)
1400: ʎ becomes j
    pɑʎ → pɑj   (ʎ→j)
```

## pailler

`pˌɑleˈɑːrium` → `pa.je`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpɑ.leˈɑː.ri.um → ˌpɑ.lɛˈɑː.rɪ.ʊm   (e→ɛ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌpɑ.lɛˈɑː.rɪ.ʊm → ˌpɑˈljɑː.rjʊm   (ɛ→j, ɪ→j)
-100: l darkens before a non-lateral consonant
    ˌpɑˈljɑː.rjʊm → ˌpɑˈɫjɑː.rjʊm   (l→ɫ)
-100: yod strengthens before a vowel
    ˌpɑˈɫjɑː.rjʊm → ˌpɑɫˈʝɑːr.ʝʊm   (j→ʝ, j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɑɫˈʝɑːr.ʝʊm → ˌpɑɫˈʝɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌpɑɫˈʝɑr.ʝʊm → ˌpɑɫˈʝɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɑɫˈʝɑr.ʝom → ˌpɑɫˈʝɑr.ʝo   (m→∅)
300: l palatalizes to ʎ before yod
    ˌpɑɫˈʝɑr.ʝo → ˌpɑˈʎɑr.ʝo   (ɫʝ→ʎ)
500: r + yod becomes palatalized r
    ˌpɑˈʎɑr.ʝo → ˌpɑˈʎɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌpɑˈʎɑ.rʲo → ˌpaˈʎa.rʲo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌpaˈʎa.rʲo → ˌpaˈʎaː.rʲo   (ˈa→ˈaː)
500: long stressed aː becomes ɛː after a front consonant, before palatalized r
    ˌpaˈʎaː.rʲo → ˌpaˈʎɛː.rʲo   (ˈaː→ˈɛː)
500: long stressed ɛː/ɔː diphthongize (final recurrence)
    ˌpaˈʎɛː.rʲo → ˌpaˈʎie̯.rʲo   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpaˈʎie̯.rʲo → ˌpaˈʎie̯.rʲə   (o→ə)
600: schwa becomes non-syllabic
    ˌpaˈʎie̯.rʲə → ˌpaˈʎie̯rʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpaˈʎie̯rʲə̯ → ˌpaˈʎie̯rʲ   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˌpaˈʎie̯rʲ → ˌpaˈʎie̯jrʲ   (∅→j)
600: j lost after a vowel + optional consonants + stressed ie̯, before palatalized r
    ˌpaˈʎie̯jrʲ → ˌpaˈʎie̯rʲ   (j→∅)
600: palatalized r depalatalizes
    ˌpaˈʎie̯rʲ → ˌpaˈʎie̯r   (rʲ→r)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌpaˈʎie̯r → ˌpaˈʎjer   (ˈi→j, e̯→ˈe)
1200: je becomes e after a palatal consonant
    ˌpaˈʎjer → ˌpaˈʎer   (j→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌpaˈʎer → ˌpaˈʎeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌpaˈʎeɹ → ˌpaˈʎe   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌpaˈʎe → pa.ʎe   (ˌa→a, ˈe→e)
1400: ʎ becomes j
    pa.ʎe → pa.je   (ʎ→j)
```

## pareil

`pˌɑrˈikulum` → `pa.ʁɛj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpɑˈri.ku.lum → ˌpɑˈrɪ.kʊ.lʊm   (ˈi→ˈɪ, u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˌpɑˈrɪ.kʊ.lʊm → ˌpɑˈrɪ.klʊm   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˌpɑˈrɪ.klʊm → ˌpɑˈre.klom   (ˈɪ→ˈe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɑˈre.klom → ˌpɑˈre.klo   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˌpɑˈre.klo → ˌpɑˈreː.klo   (ˈe→ˈeː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˌpɑˈreː.klo → ˌpɑˈreː.xlo   (k→x)
500: a vowel shortens before a consonant cluster
    ˌpɑˈreː.xlo → ˌpɑˈre.xlo   (ˈeː→ˈe)
500: the low vowel fronts by default
    ˌpɑˈre.xlo → ˌpaˈre.xlo   (ˌɑ→ˌa)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌpaˈre.xlo → ˌpaˈre.çlo   (x→ç)
500: a lateral palatalizes after a high-front consonant
    ˌpaˈre.çlo → ˌpaˈre.çʎo   (l→ʎ)
600: yod lost before ʎ or palatalized r
    ˌpaˈre.çʎo → ˌpaˈre.ʎo   (ç→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpaˈre.ʎo → ˌpaˈre.ʎə   (o→ə)
600: schwa becomes non-syllabic
    ˌpaˈre.ʎə → ˌpaˈreʎə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpaˈreʎə̯ → ˌpaˈreʎ   (ə̯→∅)
1400: e lowers to ɛ before a lateral
    ˌpaˈreʎ → ˌpaˈrɛʎ   (ˈe→ˈɛ)
1400: r becomes uvular ʀ
    ˌpaˈrɛʎ → ˌpaˈʀɛʎ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpaˈʀɛʎ → pa.ʀɛʎ   (ˌa→a, ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pa.ʀɛʎ → pa.ʁɛʎ   (ʀ→ʁ)
1400: ʎ becomes j
    pa.ʁɛʎ → pa.ʁɛj   (ʎ→j)
```

## pauvre

`pˈɑwper` → `pɔpʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpɑw.per → ˈpɑw.pɛr   (e→ɛ)
500: the low vowel fronts by default
    ˈpɑw.pɛr → ˈpaw.pɛr   (ˈɑ→ˈa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈpaw.pɛr → ˈpɔw.pɛr   (ˈa→ˈɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpɔw.pɛr → ˈpɔw.pər   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpɔw.pər → ˈpɔwpə̯r   (ə→ə̯)
600: non-syllabic schwa + r/tap metathesizes word-finally
    ˈpɔwpə̯r → ˈpɔwprə̯   (ə̯→r, r→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈpɔwprə̯ → ˈpɔw.prə   (ə̯→ə)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈpɔw.prə → ˈpɔ.prə   (w→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈpɔ.prə → ˈpɔprə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɔprə̯ → ˈpɔpr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈpɔpr → ˈpɔpʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɔpʀ → pɔpʀ   (ˈɔ→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɔpʀ → pɔpʁ   (ʀ→ʁ)
```

## peinture

`pˌin̪kt̪ˈuːrɑm` → `pɛ̃.t̪yʁ`

```
-100: n assimilates to a following velar stop
    ˌpin̪kˈt̪uː.rɑm → ˌpiŋkˈt̪uː.rɑm   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpiŋkˈt̪uː.rɑm → ˌpɪŋkˈt̪uː.rɑm   (ˌi→ˌɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɪŋkˈt̪uː.rɑm → ˌpɪŋkˈt̪u.rɑm   (ˈuː→ˈu)
-100: k lost after ŋ before a voiceless coronal
    ˌpɪŋkˈt̪u.rɑm → ˌpɪŋˈt̪u.rɑm   (k→∅)
-100: lax high vowels lower to tense mid vowels
    ˌpɪŋˈt̪u.rɑm → ˌpeŋˈt̪u.rɑm   (ˌɪ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpeŋˈt̪u.rɑm → ˌpeŋˈt̪u.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpeŋˈt̪u.rɑ → ˌpeŋˈt̪uː.rɑ   (ˈu→ˈuː)
500: ŋ palatalizes to ɲ before a coronal
    ˌpeŋˈt̪uː.rɑ → ˌpeɲˈt̪uː.rɑ   (ŋ→ɲ)
500: the low vowel fronts by default
    ˌpeɲˈt̪uː.rɑ → ˌpeɲˈt̪uː.ra   (ɑ→a)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌpeɲˈt̪uː.ra → ˌpeɲˈt̪ʲuː.ra   (t̪→t̪ʲ)
500: a high tense round non-nasal vowel centralizes
    ˌpeɲˈt̪ʲuː.ra → ˌpeɲˈt̪ʲʉː.ra   (ˈuː→ˈʉː)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌpeɲˈt̪ʲʉː.ra → ˌpeɲjˈt̪ʉː.ra   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌpeɲjˈt̪ʉː.ra → ˌpeɲˈt̪ʉː.ra   (j→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpeɲˈt̪ʉː.ra → ˌpeɲˈt̪ʉː.rə   (a→ə)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˌpeɲˈt̪ʉː.rə → ˌpej̃n̪ˈt̪ʉː.rə   (ɲ→j̃n̪)
750: vowel length resets to short
    ˌpej̃n̪ˈt̪ʉː.rə → ˌpej̃n̪ˈt̪ʉ.rə   (ˈʉː→ˈʉ)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌpej̃n̪ˈt̪ʉ.rə → ˌpej̃ˈt̪ʉ.rə   (n̪→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌpej̃ˈt̪ʉ.rə → ˌpej̃ˈt̪y.rə   (ˈʉ→ˈy)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌpej̃ˈt̪y.rə → ˌpẽj̃ˈt̪y.rə   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌpẽj̃ˈt̪y.rə → ˌpɛ̃j̃ˈt̪y.rə   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌpɛ̃j̃ˈt̪y.rə → ˌpãj̃ˈt̪y.rə   (ˌɛ̃→ˌã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌpãj̃ˈt̪y.rə → ˌpɛ̃j̃ˈt̪y.rə   (ˌã→ˌɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌpɛ̃j̃ˈt̪y.rə → ˌpɛ̃ˈt̪y.rə   (j̃→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌpɛ̃ˈt̪y.rə → ˌpɛ̃ˈt̪yrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌpɛ̃ˈt̪yrə̯ → ˌpɛ̃ˈt̪yr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌpɛ̃ˈt̪yr → ˌpɛ̃ˈt̪yʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpɛ̃ˈt̪yʀ → pɛ̃.t̪yʀ   (ˌɛ̃→ɛ̃, ˈy→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɛ̃.t̪yʀ → pɛ̃.t̪yʁ   (ʀ→ʁ)
```

## pelerin

`pˌeregrˈiːn̪um` → `pe.ʁɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpe.reˈgriː.n̪um → ˌpɛ.rɛˈgriː.n̪ʊm   (ˌe→ˌɛ, e→ɛ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɛ.rɛˈgriː.n̪ʊm → ˌpɛ.rɛˈgri.n̪ʊm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌpɛ.rɛˈgri.n̪ʊm → ˌpɛ.rɛˈgri.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɛ.rɛˈgri.n̪om → ˌpɛ.rɛˈgri.n̪o   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌpɛ.rɛˈgri.n̪o → ˌpɛ.rɛˈɣri.n̪o   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpɛ.rɛˈɣri.n̪o → ˌpɛ.rɛˈɣriː.n̪o   (ˈi→ˈiː)
500: the velar fricative is lost between a front-mid vowel and stressed r
    ˌpɛ.rɛˈɣriː.n̪o → ˌpɛ.rɛˈriː.n̪o   (ɣ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpɛ.rɛˈriː.n̪o → ˌpɛ.rəˈriː.n̪ə   (ɛ→ə, o→ə)
600: schwa becomes non-syllabic
    ˌpɛ.rəˈriː.n̪ə → ˌpɛrə̯ˈriːn̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpɛrə̯ˈriːn̪ə̯ → ˌpɛrˈriːn̪   (ˈə̯riːn̪ə̯→ˈriːn̪)
600: secondary-stressed ɛ raises to e before rr
    ˌpɛrˈriːn̪ → ˌperˈriːn̪   (ˌɛ→ˌe)
750: vowel length resets to short
    ˌperˈriːn̪ → ˌperˈrin̪   (ˈiː→ˈi)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌperˈrin̪ → ˌperˈrĩn̪   (ˈi→ˈĩ)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌperˈrĩn̪ → ˌpɛrˈrĩn̪   (ˌe→ˌɛ)
1000: the geminate rr degeminates
    ˌpɛrˈrĩn̪ → ˌpɛˈrĩn̪   (r→∅)
1000: secondary-stressed ɛ becomes e before r, z, or v, then a vowel
    ˌpɛˈrĩn̪ → ˌpeˈrĩn̪   (ˌɛ→ˌe)
1200: nasalized ĩ lowers to ẽ
    ˌpeˈrĩn̪ → ˌpeˈrẽn̪   (ˈĩ→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌpeˈrẽn̪ → ˌpeˈrẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˌpeˈrẽː → ˌpeˈrɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: r becomes uvular ʀ
    ˌpeˈrɛ̃ː → ˌpeˈʀɛ̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpeˈʀɛ̃ː → pe.ʀɛ̃ː   (ˌe→e, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    pe.ʀɛ̃ː → pe.ʀɛ̃   (ɛ̃ː→ɛ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    pe.ʀɛ̃ → pe.ʁɛ̃   (ʀ→ʁ)
```

## personne

`pˌersˈoːn̪ɑm` → `pɛʁ.sɔn̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌperˈsoː.n̪ɑm → ˌpɛrˈsoː.n̪ɑm   (ˌe→ˌɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɛrˈsoː.n̪ɑm → ˌpɛrˈso.n̪ɑm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɛrˈso.n̪ɑm → ˌpɛrˈso.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpɛrˈso.n̪ɑ → ˌpɛrˈsoː.n̪ɑ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌpɛrˈsoː.n̪ɑ → ˌpɛrˈsũː.n̪ɑ   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˌpɛrˈsũː.n̪ɑ → ˌpɛrˈsũː.n̪a   (ɑ→a)
600: secondary-stressed ɛ raises to e before any two segments
    ˌpɛrˈsũː.n̪a → ˌperˈsũː.n̪a   (ˌɛ→ˌe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌperˈsũː.n̪a → ˌperˈsũː.n̪ə   (a→ə)
750: vowel length resets to short
    ˌperˈsũː.n̪ə → ˌperˈsũ.n̪ə   (ˈũː→ˈũ)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌperˈsũ.n̪ə → ˌpɛrˈsũ.n̪ə   (ˌe→ˌɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌpɛrˈsũ.n̪ə → ˌpɛrˈsũn̪ə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌpɛrˈsũn̪ə̯ → ˌpɛɹˈsũn̪ə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˌpɛɹˈsũn̪ə̯ → ˌpɛɹˈsũn̪   (ə̯→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌpɛɹˈsũn̪ → ˌpɛrˈsũn̪   (ɹ→r)
1400: r becomes uvular ʀ
    ˌpɛrˈsũn̪ → ˌpɛʀˈsũn̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpɛʀˈsũn̪ → pɛʀ.sũn̪   (ˌɛ→ɛ, ˈũ→ũ)
1400: nasal ũ opens to ɔ̃
    pɛʀ.sũn̪ → pɛʀ.sɔ̃n̪   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    pɛʀ.sɔ̃n̪ → pɛʀ.sɔn̪   (ɔ̃→ɔ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɛʀ.sɔn̪ → pɛʁ.sɔn̪   (ʀ→ʁ)
```

## peur

`pˌɑwˈoːrem` → `pœʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌpɑˈwoː.rem → ˌpɑˈɣʷoː.rem   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpɑˈɣʷoː.rem → ˌpɑˈɣʷoː.rɛm   (e→ɛ)
-100: the labiovelar approximant is lost between a low vowel and a rounded vowel
    ˌpɑˈɣʷoː.rɛm → ˌpɑˈoː.rɛm   (ɣʷ→∅)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɑˈoː.rɛm → ˌpɑˈo.rɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɑˈo.rɛm → ˌpɑˈo.rɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpɑˈo.rɛ → ˌpɑˈoː.rɛ   (ˈo→ˈoː)
500: the low vowel fronts by default
    ˌpɑˈoː.rɛ → ˌpaˈoː.rɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpaˈoː.rɛ → ˌpaˈoː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌpaˈoː.rə → ˌpaˈoːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpaˈoːrə̯ → ˌpaˈoːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌpaˈoːr → ˌpaˈowr   (ˈoː→ˈow)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˌpaˈowr → ˌpaˈør   (ˈow→ˈø)
1000: secondary-stressed a raises to e before a front round vowel
    ˌpaˈør → ˌpeˈør   (ˌa→ˌe)
1000: secondary-stressed e reduces to schwa in an open syllable (recurrence)
    ˌpeˈør → ˌpəˈør   (ˌe→ˌə)
1200: a stressless schwa desyllabifies before another vowel
    ˌpəˈør → ˈpə̯ør   (ˌə→ə̯)
1400: e/ø lax before an r that closes the syllable
    ˈpə̯ør → ˈpə̯œr   (ˈø→ˈœ)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˈpə̯œr → ˈpə̯œːr   (ˈœ→ˈœː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈpə̯œːr → ˈpœːr   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈpœːr → ˈpœːɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈpœːɹ → ˈpœːr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈpœːr → ˈpœːʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpœːʀ → pœːʀ   (ˈœː→œː)
1400: distinctive vowel length is lost entirely
    pœːʀ → pœʀ   (œː→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pœʀ → pœʁ   (ʀ→ʁ)
```

## peut

`pˈot̪et̪` → `pø`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpo.t̪et̪ → ˈpɔ.t̪ɛt̪   (ˈo→ˈɔ, e→ɛ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpɔ.t̪ɛt̪ → ˈpɔː.t̪ɛt̪   (ˈɔ→ˈɔː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈpɔː.t̪ɛt̪ → ˈpuo̯.t̪ɛt̪   (ˈɔː→ˈuo̯)
500: a high tense round non-nasal vowel centralizes
    ˈpuo̯.t̪ɛt̪ → ˈpʉo̯.t̪ɛt̪   (ˈu→ˈʉ)
600: t/d spirantize word-finally after a vowel
    ˈpʉo̯.t̪ɛt̪ → ˈpʉo̯.t̪ɛθ   (t̪→θ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpʉo̯.t̪ɛθ → ˈpʉo̯.t̪əθ   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpʉo̯.t̪əθ → ˈpʉo̯t̪ə̯θ   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpʉo̯t̪ə̯θ → ˈpʉo̯t̪θ   (ə̯→∅)
600: a dental fricative hardens to a stop after a consonant, word-finally
    ˈpʉo̯t̪θ → ˈpʉo̯t̪t̪   (θ→t̪)
750: a dental stop deletes before another coronal stop
    ˈpʉo̯t̪t̪ → ˈpʉo̯t̪   (t̪→∅)
1000: high round back vowels front (completion of u-fronting)
    ˈpʉo̯t̪ → ˈpyo̯t̪   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈpyo̯t̪ → ˈpye̯t̪   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈpye̯t̪ → ˈpøt̪   (ˈye̯→ˈø)
1400: final obstruents are lost
    ˈpøt̪ → ˈpø   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpø → pø   (ˈø→ø)
```

## pied

`pˈed̪em` → `pje`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpe.d̪em → ˈpɛ.d̪ɛm   (ˈe→ˈɛ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpɛ.d̪ɛm → ˈpɛ.d̪ɛ   (m→∅)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈpɛ.d̪ɛ → ˈpɛ.ðɛ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpɛ.ðɛ → ˈpɛː.ðɛ   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈpɛː.ðɛ → ˈpie̯.ðɛ   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpie̯.ðɛ → ˈpie̯.ðə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpie̯.ðə → ˈpie̯ðə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpie̯ðə̯ → ˈpie̯ð   (ə̯→∅)
750: all final obstruents devoice
    ˈpie̯ð → ˈpie̯θ   (ð→θ)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈpie̯θ → ˈpjeθ   (ˈi→j, e̯→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˈpjeθ → ˈpje   (θ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpje → pje   (ˈe→e)
```

## pieds

`pˈed̪es` → `pje`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpe.d̪es → ˈpɛ.d̪ɛs   (ˈe→ˈɛ, e→ɛ)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈpɛ.d̪ɛs → ˈpɛ.ðɛs   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpɛ.ðɛs → ˈpɛː.ðɛs   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈpɛː.ðɛs → ˈpie̯.ðɛs   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpie̯.ðɛs → ˈpie̯.ðəs   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpie̯.ðəs → ˈpie̯ðə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpie̯ðə̯s → ˈpie̯ðs   (ə̯→∅)
600: a dental fricative + s becomes the affricate ts word-finally
    ˈpie̯ðs → ˈpie̯t͡s   (ðs→t͡s)
750: a word-final stop re-opens to a fricative after a vowel
    ˈpie̯t͡s → ˈpie̯s   (t͡s→s)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈpie̯s → ˈpjes   (ˈi→j, e̯→ˈe)
1000: a primary-stressed vowel lengthens before word-final s
    ˈpjes → ˈpjeːs   (ˈe→ˈeː)
1400: final obstruents are lost
    ˈpjeːs → ˈpjeː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpjeː → pjeː   (ˈeː→eː)
1400: distinctive vowel length is lost entirely
    pjeː → pje   (eː→e)
```

## pieux

`pˈɑːloːs` → `po`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈpɑː.loːs → ˈpɑ.los   (ˈɑː→ˈɑ, oː→o)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpɑ.los → ˈpɑː.los   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈpɑː.los → ˈpaː.los   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpaː.los → ˈpaː.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˈpaː.ləs → ˈpaːlə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpaːlə̯s → ˈpaːls   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈpaːls → ˈpals   (ˈaː→ˈa)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈpals → ˈpaɫs   (l→ɫ)
1000: back dark-l variants vocalize to w
    ˈpaɫs → ˈpaws   (ɫ→w)
1200: aw becomes long oː
    ˈpaws → ˈpoːs   (ˈaw→ˈoː)
1400: final obstruents are lost
    ˈpoːs → ˈpoː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpoː → poː   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    poː → po   (oː→o)
```

## pis

`pˈejus` → `pi`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈpe.jus → ˈpe.ʝus   (j→ʝ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpe.ʝus → ˈpɛ.ʝʊs   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈpɛ.ʝʊs → ˈpɛ.ʝos   (ʊ→o)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpɛ.ʝos → ˈpɛː.ʝos   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈpɛː.ʝos → ˈpie̯.ʝos   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpie̯.ʝos → ˈpie̯.ʝəs   (o→ə)
600: schwa becomes non-syllabic
    ˈpie̯.ʝəs → ˈpie̯ʝə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpie̯ʝə̯s → ˈpie̯ʝs   (ə̯→∅)
600: ʝ weakens to j before optional consonants + word end
    ˈpie̯ʝs → ˈpie̯js   (ʝ→j)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈpie̯js → ˈpie̯jsʲ   (s→sʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈpie̯jsʲ → ˈpie̯jjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈpie̯jjs → ˈpie̯js   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈpie̯js → ˈpie̯jt͡sʲ   (s→t͡sʲ)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈpie̯jt͡sʲ → ˈpijt͡sʲ   (e̯→∅)
1000: all affricates become sibilants (deaffrication)
    ˈpijt͡sʲ → ˈpijsʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈpijsʲ → ˈpijs   (sʲ→s)
1400: final obstruents are lost
    ˈpijs → ˈpij   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpij → pij   (ˈi→i)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    pij → pi   (j→∅)
```

## pitié

`pˌiet̪ˈɑːt̪em` → `pi.t̪e`

```
-100: stressed i + e becomes iːx (pietatem-type lexemes)
    ˌpi.eˈt̪ɑː.t̪em → ˌpiːxˈt̪ɑː.t̪em   (ˌi→ˌiː, e→x)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpiːxˈt̪ɑː.t̪em → ˌpiːxˈt̪ɑː.t̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpiːxˈt̪ɑː.t̪ɛm → ˌpixˈt̪ɑ.t̪ɛm   (ˌiː→ˌi, ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpixˈt̪ɑ.t̪ɛm → ˌpixˈt̪ɑ.t̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpixˈt̪ɑ.t̪ɛ → ˌpixˈt̪ɑː.t̪ɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌpixˈt̪ɑː.t̪ɛ → ˌpixˈt̪aː.t̪ɛ   (ˈɑː→ˈaː)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌpixˈt̪aː.t̪ɛ → ˌpiçˈt̪aː.t̪ɛ   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌpiçˈt̪aː.t̪ɛ → ˌpiçˈt̪ʲaː.t̪ɛ   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpiçˈt̪ʲaː.t̪ɛ → ˌpiçˈt̪ʲaː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌpiçˈt̪ʲaː.t̪ə → ˌpiçˈt̪ʲaːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpiçˈt̪ʲaːt̪ə̯ → ˌpiçˈt̪ʲaːt̪   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌpiçˈt̪ʲaːt̪ → ˌpiçjˈt̪aːt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌpiçjˈt̪aːt̪ → ˌpiçˈt̪aːt̪   (j→∅)
600: long stressed vowels diphthongize
    ˌpiçˈt̪aːt̪ → ˌpiçˈt̪ae̯t̪   (ˈaː→ˈae̯)
750: a word-final stop re-opens to a fricative after a vowel
    ˌpiçˈt̪ae̯t̪ → ˌpiçˈt̪ae̯θ   (t̪→θ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌpiçˈt̪ae̯θ → ˌpiçˈt̪eːθ   (ˈae̯→ˈeː)
750: ç merges into ʝ
    ˌpiçˈt̪eːθ → ˌpiʝˈt̪eːθ   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌpiʝˈt̪eːθ → ˌpijˈt̪eːθ   (ʝ→j)
750: j deletes after a high front tense vowel
    ˌpijˈt̪eːθ → ˌpiˈt̪eːθ   (j→∅)
1000: vowel length resets to short
    ˌpiˈt̪eːθ → ˌpiˈt̪eθ   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌpiˈt̪eθ → ˌpiˈt̪e   (θ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌpiˈt̪e → pi.t̪e   (ˌi→i, ˈe→e)
```

## plaie

`plˈɑːgɑm` → `plɛ`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈplɑː.gɑm → ˈplɑ.gɑm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈplɑ.gɑm → ˈplɑ.gɑ   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈplɑ.gɑ → ˈplɑ.ɣɑ   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈplɑ.ɣɑ → ˈplɑː.ɣɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈplɑː.ɣɑ → ˈplaː.ɣa   (ˈɑː→ˈaː, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈplaː.ɣa → ˈplaː.ɣʲa   (ɣ→ɣʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈplaː.ɣʲa → ˈplaː.ʝa   (ɣʲ→ʝ)
600: ʝ weakens to j unconditionally
    ˈplaː.ʝa → ˈplaː.ja   (ʝ→j)
600: long stressed vowels diphthongize
    ˈplaː.ja → ˈplae̯.ja   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˈplae̯.ja → ˈpla.ja   (e̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpla.ja → ˈpla.jə   (a→ə)
1200: schwa desyllabifies after another vowel
    ˈpla.jə → ˈplajə̯   (ə→ə̯)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈplajə̯ → ˈplɛːə̯   (ˈaj→ˈɛː)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈplɛːə̯ → ˈplɛː   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈplɛː → plɛː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    plɛː → plɛ   (ɛː→ɛ)
```

## plaindre

`plˈɑn̪gere` → `plɛ̃d̪ʁ`

```
-100: n assimilates to a following velar stop
    ˈplɑn̪.ge.re → ˈplɑŋ.ge.re   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈplɑŋ.ge.re → ˈplɑŋ.gɛ.rɛ   (e→ɛ, e→ɛ)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈplɑŋ.gɛ.rɛ → ˈplɑŋ.gʲɛ.rɛ   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˈplɑŋ.gʲɛ.rɛ → ˈplɑŋ.ɟɛ.rɛ   (gʲ→ɟ)
500: ŋ/ɫ/s palatalize before a complex palatal-triggering sequence
    ˈplɑŋ.ɟɛ.rɛ → ˈplɑɲ.ɟɛ.rɛ   (ŋ→ɲ)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈplɑɲ.ɟɛ.rɛ → ˈplɑɲ.ɟrɛ   (ɛ→∅)
500: a palatal stop becomes a dental fricative before a non-front consonant
    ˈplɑɲ.ɟrɛ → ˈplɑɲ.d̪rɛ   (ɟ→d̪)
500: the low vowel fronts by default
    ˈplɑɲ.d̪rɛ → ˈplaɲ.d̪rɛ   (ˈɑ→ˈa)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈplaɲ.d̪rɛ → ˈplaɲ.d̪ʲrɛ   (d̪→d̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈplaɲ.d̪ʲrɛ → ˈplaɲ.d̪ʲrə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈplaɲ.d̪ʲrə → ˈplaɲd̪ʲrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈplaɲd̪ʲrə̯ → ˈplaɲd̪ʲr   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈplaɲd̪ʲr → ˈplaɲ.d̪ʲrə   (∅→ə)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈplaɲ.d̪ʲrə → ˈplaɲ.d̪ʲrʲə   (r→rʲ)
600: palatalized r depalatalizes
    ˈplaɲ.d̪ʲrʲə → ˈplaɲ.d̪ʲrə   (rʲ→r)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈplaɲ.d̪ʲrə → ˈplaɲj.d̪rə   (d̪ʲ→jd̪)
600: j is lost after j or a consonant, before a consonant
    ˈplaɲj.d̪rə → ˈplaɲ.d̪rə   (j→∅)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˈplaɲ.d̪rə → ˈplaj̃n̪.d̪rə   (ɲ→j̃n̪)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈplaj̃n̪.d̪rə → ˈplaj̃.d̪rə   (n̪→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈplaj̃.d̪rə → ˈplãj̃.d̪rə   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈplãj̃.d̪rə → ˈplɛ̃j̃.d̪rə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈplɛ̃j̃.d̪rə → ˈplɛ̃.d̪rə   (j̃→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈplɛ̃.d̪rə → ˈplɛ̃d̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈplɛ̃d̪rə̯ → ˈplɛ̃d̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈplɛ̃d̪r → ˈplɛ̃d̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈplɛ̃d̪ʀ → plɛ̃d̪ʀ   (ˈɛ̃→ɛ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    plɛ̃d̪ʀ → plɛ̃d̪ʁ   (ʀ→ʁ)
```

## plein

`plˈeːn̪um` → `plɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpleː.n̪um → ˈpleː.n̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpleː.n̪ʊm → ˈple.n̪ʊm   (ˈeː→ˈe)
-100: lax high vowels lower to tense mid vowels
    ˈple.n̪ʊm → ˈple.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈple.n̪om → ˈple.n̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈple.n̪o → ˈpleː.n̪o   (ˈe→ˈeː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpleː.n̪o → ˈpleː.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈpleː.n̪ə → ˈpleːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpleːn̪ə̯ → ˈpleːn̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈpleːn̪ → ˈplejn̪   (ˈeː→ˈej)
1000: j nasalizes after a mid front vowel, before a nasal (second nasalization)
    ˈplejn̪ → ˈplej̃n̪   (j→j̃)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈplej̃n̪ → ˈplẽj̃n̪   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈplẽj̃n̪ → ˈplɛ̃j̃n̪   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈplɛ̃j̃n̪ → ˈplãj̃n̪   (ˈɛ̃→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈplãj̃n̪ → ˈplɛ̃j̃n̪   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈplɛ̃j̃n̪ → ˈplɛ̃n̪   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈplɛ̃n̪ → ˈplɛ̃ː   (ˈɛ̃n̪→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈplɛ̃ː → plɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    plɛ̃ː → plɛ̃   (ɛ̃ː→ɛ̃)
```

## pleine

`plˈeːn̪ɑm` → `plɛn̪`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈpleː.n̪ɑm → ˈple.n̪ɑm   (ˈeː→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈple.n̪ɑm → ˈple.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈple.n̪ɑ → ˈpleː.n̪ɑ   (ˈe→ˈeː)
500: the low vowel fronts by default
    ˈpleː.n̪ɑ → ˈpleː.n̪a   (ɑ→a)
600: long stressed vowels diphthongize
    ˈpleː.n̪a → ˈplej.n̪a   (ˈeː→ˈej)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈplej.n̪a → ˈplej.n̪ə   (a→ə)
1000: j nasalizes after a mid front vowel, before a nasal (second nasalization)
    ˈplej.n̪ə → ˈplej̃.n̪ə   (j→j̃)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈplej̃.n̪ə → ˈplẽj̃.n̪ə   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈplẽj̃.n̪ə → ˈplɛ̃j̃.n̪ə   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈplɛ̃j̃.n̪ə → ˈplãj̃.n̪ə   (ˈɛ̃→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈplãj̃.n̪ə → ˈplɛ̃j̃.n̪ə   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈplɛ̃j̃.n̪ə → ˈplɛ̃.n̪ə   (j̃→∅)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈplɛ̃.n̪ə → ˈplɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈplɛ.n̪ə → ˈplɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈplɛn̪ə̯ → ˈplɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈplɛn̪ → plɛn̪   (ˈɛ→ɛ)
```

## ploie

`plˈikɑt̪` → `plɛj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpli.kɑt̪ → ˈplɪ.kɑt̪   (ˈi→ˈɪ)
-100: lax high vowels lower to tense mid vowels
    ˈplɪ.kɑt̪ → ˈple.kɑt̪   (ˈɪ→ˈe)
300: a stressed vowel lengthens before a single consonant + glide
    ˈple.kɑt̪ → ˈpleː.kɑt̪   (ˈe→ˈeː)
500: k voices to g intervocalically
    ˈpleː.kɑt̪ → ˈpleː.gɑt̪   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˈpleː.gɑt̪ → ˈpleː.ɣɑt̪   (g→ɣ)
500: the low vowel fronts by default
    ˈpleː.ɣɑt̪ → ˈpleː.ɣat̪   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈpleː.ɣat̪ → ˈpleː.ɣʲat̪   (ɣ→ɣʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈpleː.ɣʲat̪ → ˈpleː.ʝat̪   (ɣʲ→ʝ)
600: t/d spirantize word-finally after a vowel
    ˈpleː.ʝat̪ → ˈpleː.ʝaθ   (t̪→θ)
600: ʝ weakens to j unconditionally
    ˈpleː.ʝaθ → ˈpleː.jaθ   (ʝ→j)
600: eːj/eːʝ shortens to ej
    ˈpleː.jaθ → ˈple.jaθ   (ˈeː→ˈe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈple.jaθ → ˈple.jəθ   (a→ə)
1000: stressed e laxes to ɛ before a consonant + vowel
    ˈple.jəθ → ˈplɛ.jəθ   (ˈe→ˈɛ)
1000: the interdental fricatives (plain and palatalized) efface
    ˈplɛ.jəθ → ˈplɛ.jə   (θ→∅)
1200: schwa desyllabifies after another vowel
    ˈplɛ.jə → ˈplɛjə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈplɛjə̯ → ˈplɛj   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈplɛj → plɛj   (ˈɛ→ɛ)
```

## point

`pˈun̪kt̪um` → `pwɛ̃`

```
-100: n assimilates to a following velar stop
    ˈpun̪k.t̪um → ˈpuŋk.t̪um   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpuŋk.t̪um → ˈpʊŋk.t̪ʊm   (ˈu→ˈʊ, u→ʊ)
-100: k lost after ŋ before a voiceless coronal
    ˈpʊŋk.t̪ʊm → ˈpʊŋ.t̪ʊm   (k→∅)
-100: lax high vowels lower to tense mid vowels
    ˈpʊŋ.t̪ʊm → ˈpoŋ.t̪om   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpoŋ.t̪om → ˈpoŋ.t̪o   (m→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈpoŋ.t̪o → ˈpũŋ.t̪o   (ˈo→ˈũ)
500: ŋ palatalizes to ɲ before a coronal
    ˈpũŋ.t̪o → ˈpũɲ.t̪o   (ŋ→ɲ)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈpũɲ.t̪o → ˈpũɲ.t̪ʲo   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpũɲ.t̪ʲo → ˈpũɲ.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈpũɲ.t̪ʲə → ˈpũɲt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpũɲt̪ʲə̯ → ˈpũɲt̪ʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈpũɲt̪ʲ → ˈpũɲjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈpũɲjt̪ → ˈpũɲt̪   (j→∅)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˈpũɲt̪ → ˈpũj̃n̪t̪   (ɲ→j̃n̪)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈpũj̃n̪t̪ → ˈpũj̃t̪   (n̪→∅)
1000: the nasal diphthong ũj̃ becomes wĩ (syllabicity swap before a nasal)
    ˈpũj̃t̪ → pwj̩̃t̪   (ˈũ→w, j̃→j̩̃)
1200: nasalized ĩ lowers after w
    pwj̩̃t̪ → pwj̩̃t̪   (j̩̃→j̩̃)
1200: a front unrounded non-low vowel laxes and lowers after w
    pwj̩̃t̪ → pwɛ̃t̪   (j̩̃→ɛ̃)
1400: final obstruents are lost
    pwɛ̃t̪ → pwɛ̃   (t̪→∅)
```

## pomme

`pˈoːmɑm` → `pɔm`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈpoː.mɑm → ˈpo.mɑm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpo.mɑm → ˈpo.mɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpo.mɑ → ˈpoː.mɑ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈpoː.mɑ → ˈpũː.mɑ   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˈpũː.mɑ → ˈpũː.ma   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpũː.ma → ˈpũː.mə   (a→ə)
750: vowel length resets to short
    ˈpũː.mə → ˈpũ.mə   (ˈũː→ˈũ)
1400: final ə becomes a non-syllabic off-glide
    ˈpũ.mə → ˈpũmə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpũmə̯ → ˈpũm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpũm → pũm   (ˈũ→ũ)
1400: nasal ũ opens to ɔ̃
    pũm → pɔ̃m   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    pɔ̃m → pɔm   (ɔ̃→ɔ)
```

## pondre

`pˈon̪ere` → `pɔ̃d̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpo.n̪e.re → ˈpɔ.n̪ɛ.rɛ   (ˈo→ˈɔ, e→ɛ, e→ɛ)
-100: posttonic non-low vowel syncopates between n and r + vowel
    ˈpɔ.n̪ɛ.rɛ → ˈpɔ.n̪rɛ   (ɛ→∅)
500: d epenthesized between n and r
    ˈpɔ.n̪rɛ → ˈpɔn̪.d̪rɛ   (∅→d̪)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈpɔn̪.d̪rɛ → ˈpũn̪.d̪rɛ   (ˈɔ→ˈũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpũn̪.d̪rɛ → ˈpũn̪.d̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpũn̪.d̪rə → ˈpũn̪d̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpũn̪d̪rə̯ → ˈpũn̪d̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈpũn̪d̪r → ˈpũn̪.d̪rə   (∅→ə)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈpũn̪.d̪rə → ˈpũː.d̪rə   (ˈũn̪→ˈũː)
1400: final ə becomes a non-syllabic off-glide
    ˈpũː.d̪rə → ˈpũːd̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpũːd̪rə̯ → ˈpũːd̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈpũːd̪r → ˈpũːd̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpũːd̪ʀ → pũːd̪ʀ   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    pũːd̪ʀ → pũd̪ʀ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    pũd̪ʀ → pɔ̃d̪ʀ   (ũ→ɔ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɔ̃d̪ʀ → pɔ̃d̪ʁ   (ʀ→ʁ)
```

## pont

`pˈoːn̪t̪em` → `pɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpoːn̪.t̪em → ˈpoːn̪.t̪ɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpoːn̪.t̪ɛm → ˈpon̪.t̪ɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpon̪.t̪ɛm → ˈpon̪.t̪ɛ   (m→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈpon̪.t̪ɛ → ˈpũn̪.t̪ɛ   (ˈo→ˈũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpũn̪.t̪ɛ → ˈpũn̪.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpũn̪.t̪ə → ˈpũn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpũn̪t̪ə̯ → ˈpũn̪t̪   (ə̯→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈpũn̪t̪ → ˈpũːt̪   (ˈũn̪→ˈũː)
1400: final obstruents are lost
    ˈpũːt̪ → ˈpũː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpũː → pũː   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    pũː → pũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    pũ → pɔ̃   (ũ→ɔ̃)
```

## porter

`pˌort̪ˈɑːre` → `pɔʁ.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌporˈt̪ɑː.re → ˌpɔrˈt̪ɑː.rɛ   (ˌo→ˌɔ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɔrˈt̪ɑː.rɛ → ˌpɔrˈt̪ɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpɔrˈt̪ɑ.rɛ → ˌpɔrˈt̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌpɔrˈt̪ɑː.rɛ → ˌpɔrˈt̪aː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpɔrˈt̪aː.rɛ → ˌpɔrˈt̪aː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌpɔrˈt̪aː.rə → ˌpɔrˈt̪aːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpɔrˈt̪aːrə̯ → ˌpɔrˈt̪aːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌpɔrˈt̪aːr → ˌpɔrˈt̪ae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɔ raises to o unconditionally
    ˌpɔrˈt̪ae̯r → ˌporˈt̪ae̯r   (ˌɔ→ˌo)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌporˈt̪ae̯r → ˌporˈt̪eːr   (ˈae̯→ˈeː)
1000: secondary-stressed o opens to ɔ before r + an anterior non-labial stop + a vowel
    ˌporˈt̪eːr → ˌpɔrˈt̪eːr   (ˌo→ˌɔ)
1000: vowel length resets to short
    ˌpɔrˈt̪eːr → ˌpɔrˈt̪er   (ˈeː→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌpɔrˈt̪er → ˌpɔɹˈt̪eɹ   (r→ɹ, r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌpɔɹˈt̪eɹ → ˌpɔɹˈt̪e   (ɹ→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌpɔɹˈt̪e → ˌpɔrˈt̪e   (ɹ→r)
1400: r becomes uvular ʀ
    ˌpɔrˈt̪e → ˌpɔʀˈt̪e   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpɔʀˈt̪e → pɔʀ.t̪e   (ˌɔ→ɔ, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɔʀ.t̪e → pɔʁ.t̪e   (ʀ→ʁ)
```

## porteur

`pˌort̪ɑt̪ˈoːrem` → `pɔʁ.t̪œʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpor.t̪ɑˈt̪oː.rem → ˌpɔr.t̪ɑˈt̪oː.rɛm   (ˌo→ˌɔ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpɔr.t̪ɑˈt̪oː.rɛm → ˌpɔr.t̪ɑˈt̪o.rɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌpɔr.t̪ɑˈt̪o.rɛm → ˌpɔr.t̪ɑˈt̪o.rɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpɔr.t̪ɑˈt̪o.rɛ → ˌpɔr.t̪ɑˈt̪oː.rɛ   (ˈo→ˈoː)
500: the low vowel fronts by default
    ˌpɔr.t̪ɑˈt̪oː.rɛ → ˌpɔr.t̪aˈt̪oː.rɛ   (ɑ→a)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpɔr.t̪aˈt̪oː.rɛ → ˌpɔr.t̪aˈt̪oː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌpɔr.t̪aˈt̪oː.rə → ˌpɔr.t̪aˈt̪oːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpɔr.t̪aˈt̪oːrə̯ → ˌpɔr.t̪aˈt̪oːr   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌpɔr.t̪aˈt̪oːr → ˌpɔr.t̪aˈd̪oːr   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌpɔr.t̪aˈd̪oːr → ˌpɔr.t̪aˈðoːr   (d̪→ð)
600: long stressed vowels diphthongize
    ˌpɔr.t̪aˈðoːr → ˌpɔr.t̪aˈðowr   (ˈoː→ˈow)
600: secondary-stressed ɔ raises to o unconditionally
    ˌpɔr.t̪aˈðowr → ˌpor.t̪aˈðowr   (ˌɔ→ˌo)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˌpor.t̪aˈðowr → ˌpor.t̪aˈðør   (ˈow→ˈø)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpor.t̪aˈðør → ˌpor.t̪əˈðør   (a→ə)
1000: secondary-stressed o opens to ɔ before r + an anterior non-labial stop + a vowel
    ˌpor.t̪əˈðør → ˌpɔr.t̪əˈðør   (ˌo→ˌɔ)
1000: the interdental fricatives (plain and palatalized) efface
    ˌpɔr.t̪əˈðør → ˌpɔr.t̪əˈør   (ð→∅)
1200: a stressless schwa desyllabifies before another vowel
    ˌpɔr.t̪əˈør → ˌpɔrˈt̪ə̯ør   (ə→ə̯)
1400: e/ø lax before an r that closes the syllable
    ˌpɔrˈt̪ə̯ør → ˌpɔrˈt̪ə̯œr   (ˈø→ˈœ)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˌpɔrˈt̪ə̯œr → ˌpɔrˈt̪ə̯œːr   (ˈœ→ˈœː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌpɔrˈt̪ə̯œːr → ˌpɔrˈt̪œːr   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌpɔrˈt̪œːr → ˌpɔɹˈt̪œːɹ   (r→ɹ, r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌpɔɹˈt̪œːɹ → ˌpɔrˈt̪œːr   (ɹ→r, ɹ→r)
1400: r becomes uvular ʀ
    ˌpɔrˈt̪œːr → ˌpɔʀˈt̪œːʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpɔʀˈt̪œːʀ → pɔʀ.t̪œːʀ   (ˌɔ→ɔ, ˈœː→œː)
1400: distinctive vowel length is lost entirely
    pɔʀ.t̪œːʀ → pɔʀ.t̪œʀ   (œː→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɔʀ.t̪œʀ → pɔʁ.t̪œʁ   (ʀ→ʁ, ʀ→ʁ)
```

## poudre

`pˈulwerem` → `pud̪ʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈpu.lwe.rem → ˈpul.ɣʷe.rem   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpul.ɣʷe.rem → ˈpʊl.ɣʷɛ.rɛm   (ˈu→ˈʊ, e→ɛ, e→ɛ)
-100: l darkens before a non-lateral consonant
    ˈpʊl.ɣʷɛ.rɛm → ˈpʊɫ.ɣʷɛ.rɛm   (l→ɫ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈpʊɫ.ɣʷɛ.rɛm → ˈpʊɫ.βʷɛ.rɛm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈpʊɫ.βʷɛ.rɛm → ˈpoɫ.βʷɛ.rɛm   (ˈʊ→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpoɫ.βʷɛ.rɛm → ˈpoɫ.βʷɛ.rɛ   (m→∅)
500: lw becomes ll after a rounded vowel/glide, before a non-consonantal segment
    ˈpoɫ.βʷɛ.rɛ → ˈpol.lɛ.rɛ   (ɫ→l, βʷ→l)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈpol.lɛ.rɛ → ˈpol.lrɛ   (ɛ→∅)
500: d epenthesized between a lateral and r
    ˈpol.lrɛ → ˈpoll.d̪rɛ   (∅→d̪)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpoll.d̪rɛ → ˈpoll.d̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpoll.d̪rə → ˈpolld̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpolld̪rə̯ → ˈpolld̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈpolld̪r → ˈpoll.d̪rə   (∅→ə)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˈpoll.d̪rə → ˈpol.d̪rə   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈpol.d̪rə → ˈpoɫ.d̪rə   (l→ɫ)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈpoɫ.d̪rə → ˈpuɫ.d̪rə   (ˈo→ˈu)
1000: back dark-l variants vocalize to w
    ˈpuɫ.d̪rə → ˈpuw.d̪rə   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˈpuw.d̪rə → ˈpu.d̪rə   (w→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈpu.d̪rə → ˈpud̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpud̪rə̯ → ˈpud̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈpud̪r → ˈpud̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpud̪ʀ → pud̪ʀ   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    pud̪ʀ → pud̪ʁ   (ʀ→ʁ)
```

## prendre

`prˌehˈen̪d̪ere` → `pʁɑ̃d̪ʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpreˈhen̪.d̪e.re → ˌprɛˈhɛn̪.d̪ɛ.rɛ   (ˌe→ˌɛ, ˈe→ˈɛ, e→ɛ, e→ɛ)
-100: h lost word-internally (word-initial h survives at this stage)
    ˌprɛˈhɛn̪.d̪ɛ.rɛ → ˌprɛˈɛn̪.d̪ɛ.rɛ   (h→∅)
-100: e + e contracts to a long stressed e when stress is on the second vowel
    ˌprɛˈɛn̪.d̪ɛ.rɛ → ˈpreːn̪.d̪ɛ.rɛ   (ˌɛˈɛ→ˈeː)
-100: the length feature is dropped now that quality carries the contrast
    ˈpreːn̪.d̪ɛ.rɛ → ˈpren̪.d̪ɛ.rɛ   (ˈeː→ˈe)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈpren̪.d̪ɛ.rɛ → ˈpren̪.d̪rɛ   (ɛ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpren̪.d̪rɛ → ˈpren̪.d̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpren̪.d̪rə → ˈpren̪d̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpren̪d̪rə̯ → ˈpren̪d̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈpren̪d̪r → ˈpren̪.d̪rə   (∅→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈpren̪.d̪rə → ˈprẽn̪.d̪rə   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈprẽn̪.d̪rə → ˈprɛ̃n̪.d̪rə   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈprɛ̃n̪.d̪rə → ˈprãn̪.d̪rə   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈprãn̪.d̪rə → ˈprãː.d̪rə   (ˈãn̪→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈprãː.d̪rə → ˈprãːd̪rə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈprãːd̪rə̯ → ˈprɑ̃ːd̪rə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈprɑ̃ːd̪rə̯ → ˈprɑ̃ːd̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈprɑ̃ːd̪r → ˈpʀɑ̃ːd̪ʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpʀɑ̃ːd̪ʀ → pʀɑ̃ːd̪ʀ   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    pʀɑ̃ːd̪ʀ → pʀɑ̃d̪ʀ   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀɑ̃d̪ʀ → pʁɑ̃d̪ʁ   (ʀ→ʁ, ʀ→ʁ)
```

## presse

`prˈessɑm` → `pʁɛs`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpres.sɑm → ˈprɛs.sɑm   (ˈe→ˈɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈprɛs.sɑm → ˈprɛs.sɑ   (m→∅)
500: the low vowel fronts by default
    ˈprɛs.sɑ → ˈprɛs.sa   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈprɛs.sa → ˈprɛs.sə   (a→ə)
750: an identical consonant geminate reduces to one (recurrence)
    ˈprɛs.sə → ˈprɛ.sə   (s→∅)
1000: a front unrounded vowel lengthens before s + final schwa
    ˈprɛ.sə → ˈprɛː.sə   (ˈɛ→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˈprɛː.sə → ˈprɛːsə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈprɛːsə̯ → ˈprɛːs   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈprɛːs → ˈpʀɛːs   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpʀɛːs → pʀɛːs   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    pʀɛːs → pʀɛs   (ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀɛs → pʁɛs   (ʀ→ʁ)
```

## prix

`prˈet̪ium` → `pʁi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpre.t̪i.um → ˈprɛ.t̪ɪ.ʊm   (ˈe→ˈɛ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈprɛ.t̪ɪ.ʊm → ˈprɛ.t̪jʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈprɛ.t̪jʊm → ˈprɛ.t̪ʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈprɛ.t̪ʝʊm → ˈprɛ.t̪ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈprɛ.t̪ʝom → ˈprɛ.t̪ʝo   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˈprɛ.t̪ʝo → ˈprɛt͡sʲ.ʝo   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˈprɛt͡sʲ.ʝo → ˈprɛ.t͡sʲo   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈprɛ.t͡sʲo → ˈprɛː.t͡sʲo   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈprɛː.t͡sʲo → ˈprie̯.t͡sʲo   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈprie̯.t͡sʲo → ˈprie̯.t͡sʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈprie̯.t͡sʲə → ˈprie̯t͡sʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈprie̯t͡sʲə̯ → ˈprie̯t͡sʲ   (ə̯→∅)
600: j epenthesized after the e-glide before tsʲ
    ˈprie̯t͡sʲ → ˈprie̯jt͡sʲ   (∅→j)
1000: the e-glide deletes after a stressed high front tense vowel, before a high non-round glide
    ˈprie̯jt͡sʲ → ˈprijt͡sʲ   (e̯→∅)
1000: all affricates become sibilants (deaffrication)
    ˈprijt͡sʲ → ˈprijsʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈprijsʲ → ˈprijs   (sʲ→s)
1400: final obstruents are lost
    ˈprijs → ˈprij   (s→∅)
1400: r becomes uvular ʀ
    ˈprij → ˈpʀij   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpʀij → pʀij   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀij → pʁij   (ʀ→ʁ)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    pʁij → pʁi   (j→∅)
```

## prêtre

`prˈesbyt̪er` → `pʁɛt̪ʁ`

```
-100: Greek y unrounds to i
    ˈpres.by.t̪er → ˈpres.bi.t̪er   (y→i)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpres.bi.t̪er → ˈprɛs.bɪ.t̪ɛr   (ˈe→ˈɛ, i→ɪ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈprɛs.bɪ.t̪ɛr → ˈprɛs.be.t̪ɛr   (ɪ→e)
300: e becomes a schwa-glide between an unrounded labial and a distributed obstruent + non-low vowel
    ˈprɛs.be.t̪ɛr → ˈprɛsbə̯.t̪ɛr   (e→ə̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈprɛsbə̯.t̪ɛr → ˈprɛsbə̯.t̪ər   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈprɛsbə̯.t̪ər → ˈprɛsbə̯t̪ə̯r   (ə→ə̯)
600: non-syllabic schwa + r/tap metathesizes word-finally
    ˈprɛsbə̯t̪ə̯r → ˈprɛsbə̯t̪rə̯   (ə̯→r, r→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈprɛsbə̯t̪rə̯ → ˈprɛsbə̯.t̪rə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈprɛsbə̯.t̪rə → ˈprɛsb.t̪rə   (ə̯→∅)
600: a labial consonant becomes t before a voiceless coronal stop
    ˈprɛsb.t̪rə → ˈprɛst̪.t̪rə   (b→t̪)
600: an identical consonant geminate reduces to one, after a consonant or word start
    ˈprɛst̪.t̪rə → ˈprɛs.t̪rə   (t̪→∅)
1000: s becomes x after a vowel, before any consonant
    ˈprɛs.t̪rə → ˈprɛx.t̪rə   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈprɛx.t̪rə → ˈprɛː.t̪rə   (ˈɛx→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˈprɛː.t̪rə → ˈprɛːt̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈprɛːt̪rə̯ → ˈprɛːt̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈprɛːt̪r → ˈpʀɛːt̪ʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpʀɛːt̪ʀ → pʀɛːt̪ʀ   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    pʀɛːt̪ʀ → pʀɛt̪ʀ   (ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀɛt̪ʀ → pʁɛt̪ʁ   (ʀ→ʁ, ʀ→ʁ)
```

## pur

`pˈuːrum` → `pyʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpuː.rum → ˈpuː.rʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈpuː.rʊm → ˈpu.rʊm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˈpu.rʊm → ˈpu.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpu.rom → ˈpu.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈpu.ro → ˈpuː.ro   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈpuː.ro → ˈpʉː.ro   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpʉː.ro → ˈpʉː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˈpʉː.rə → ˈpʉːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpʉːrə̯ → ˈpʉːr   (ə̯→∅)
750: vowel length resets to short
    ˈpʉːr → ˈpʉr   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈpʉr → ˈpyr   (ˈʉ→ˈy)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈpyr → ˈpyɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈpyɹ → ˈpyr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈpyr → ˈpyʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpyʀ → pyʀ   (ˈy→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    pyʀ → pyʁ   (ʀ→ʁ)
```

## purger

`pˌuːrgˈɑːre` → `pyʁ.ʒe`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌpuːrˈgɑː.re → ˌpuːrˈgɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌpuːrˈgɑː.rɛ → ˌpurˈgɑ.rɛ   (ˌuː→ˌu, ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌpurˈgɑ.rɛ → ˌpurˈgɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌpurˈgɑː.rɛ → ˌpurˈgaː.rɛ   (ˈɑː→ˈaː)
500: a high tense round non-nasal vowel centralizes
    ˌpurˈgaː.rɛ → ˌpʉrˈgaː.rɛ   (ˌu→ˌʉ)
500: the high back consonant w fronts before a front vowel
    ˌpʉrˈgaː.rɛ → ˌpʉrˈgʲaː.rɛ   (g→gʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌpʉrˈgʲaː.rɛ → ˌpʉrˈɟaː.rɛ   (gʲ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˌpʉrˈɟaː.rɛ → ˌpʉrˈd͡ʒaː.rɛ   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌpʉrˈd͡ʒaː.rɛ → ˌpʉrˈd͡ʒaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌpʉrˈd͡ʒaː.rə → ˌpʉrˈd͡ʒaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌpʉrˈd͡ʒaːrə̯ → ˌpʉrˈd͡ʒaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌpʉrˈd͡ʒaːr → ˌpʉrˈd͡ʒae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌpʉrˈd͡ʒae̯r → ˌpʉrˈd͡ʒeːr   (ˈae̯→ˈeː)
1000: high round back vowels front (completion of u-fronting)
    ˌpʉrˈd͡ʒeːr → ˌpyrˈd͡ʒeːr   (ˌʉ→ˌy)
1000: vowel length resets to short
    ˌpyrˈd͡ʒeːr → ˌpyrˈd͡ʒer   (ˈeː→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌpyrˈd͡ʒer → ˌpyrˈʒer   (d͡ʒ→ʒ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌpyrˈʒer → ˌpyɹˈʒeɹ   (r→ɹ, r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌpyɹˈʒeɹ → ˌpyɹˈʒe   (ɹ→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌpyɹˈʒe → ˌpyrˈʒe   (ɹ→r)
1400: r becomes uvular ʀ
    ˌpyrˈʒe → ˌpyʀˈʒe   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpyʀˈʒe → pyʀ.ʒe   (ˌy→y, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    pyʀ.ʒe → pyʁ.ʒe   (ʀ→ʁ)
```

## pâte

`pˈɑst̪ɑm` → `pɑt̪`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpɑs.t̪ɑm → ˈpɑs.t̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˈpɑs.t̪ɑ → ˈpas.t̪a   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpas.t̪a → ˈpas.t̪ə   (a→ə)
1000: s becomes x after a vowel, before any consonant
    ˈpas.t̪ə → ˈpax.t̪ə   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈpax.t̪ə → ˈpaː.t̪ə   (ˈax→ˈaː)
1400: final ə becomes a non-syllabic off-glide
    ˈpaː.t̪ə → ˈpaːt̪ə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈpaːt̪ə̯ → ˈpɑːt̪ə̯   (ˈaː→ˈɑː)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɑːt̪ə̯ → ˈpɑːt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɑːt̪ → pɑːt̪   (ˈɑː→ɑː)
1400: distinctive vowel length is lost entirely
    pɑːt̪ → pɑt̪   (ɑː→ɑ)
```

## père

`pˈɑt̪rem` → `pɛʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈpɑ.t̪rem → ˈpɑ.t̪rɛm   (e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈpɑ.t̪rɛm → ˈpɑ.t̪rɛ   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈpɑ.t̪rɛ → ˈpɑː.t̪rɛ   (ˈɑ→ˈɑː)
500: a vowel shortens before a consonant cluster
    ˈpɑː.t̪rɛ → ˈpɑ.t̪rɛ   (ˈɑː→ˈɑ)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant
    ˈpɑ.t̪rɛ → ˈpɑː.t̪rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈpɑː.t̪rɛ → ˈpaː.t̪rɛ   (ˈɑː→ˈaː)
500: a vowel shortens before a consonant cluster (recurrence)
    ˈpaː.t̪rɛ → ˈpa.t̪rɛ   (ˈaː→ˈa)
500: a stressed vowel lengthens before a plosive + non-nasal sonorant (recurrence)
    ˈpa.t̪rɛ → ˈpaː.t̪rɛ   (ˈa→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈpaː.t̪rɛ → ˈpaː.t̪rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈpaː.t̪rə → ˈpaːt̪rə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈpaːt̪rə̯ → ˈpaːt̪r   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈpaːt̪r → ˈpaː.t̪rə   (∅→ə)
600: a voiceless anterior consonant voices before a coronal sonorant non-nasal consonant
    ˈpaː.t̪rə → ˈpaː.d̪rə   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈpaː.d̪rə → ˈpaː.ðrə   (d̪→ð)
600: long stressed vowels diphthongize
    ˈpaː.ðrə → ˈpae̯.ðrə   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈpae̯.ðrə → ˈpeː.ðrə   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈpeː.ðrə → ˈpe.ðrə   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˈpe.ðrə → ˈpe.rə   (ð→∅)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈpe.rə → ˈpɛ.rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈpɛ.rə → ˈpɛrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɛrə̯ → ˈpɛr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈpɛr → ˈpɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɛʀ → pɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɛʀ → pɛʁ   (ʀ→ʁ)
```

## racine

`rˌɑːd̪iːkˈiːn̪ɑm` → `ʁa.sin̪`

```
-100: the length feature is dropped now that quality carries the contrast
    ˌrɑː.d̪iːˈkiː.n̪ɑm → ˌrɑ.d̪iˈki.n̪ɑm   (ˌɑː→ˌɑ, iː→i, ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌrɑ.d̪iˈki.n̪ɑm → ˌrɑ.d̪iˈki.n̪ɑ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌrɑ.d̪iˈki.n̪ɑ → ˌrɑ.d̪iˈkʲi.n̪ɑ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌrɑ.d̪iˈkʲi.n̪ɑ → ˌrɑ.d̪iˈci.n̪ɑ   (kʲ→c)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌrɑ.d̪iˈci.n̪ɑ → ˌrɑ.ðiˈci.n̪ɑ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˌrɑ.ðiˈci.n̪ɑ → ˌrɑ.ðiˈciː.n̪ɑ   (ˈi→ˈiː)
500: a palatal stop affricates
    ˌrɑ.ðiˈciː.n̪ɑ → ˌrɑ.ðiˈt͡sʲiː.n̪ɑ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌrɑ.ðiˈt͡sʲiː.n̪ɑ → ˌra.ðiˈt͡sʲiː.n̪a   (ˌɑ→ˌa, ɑ→a)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌra.ðiˈt͡sʲiː.n̪a → ˌra.ðəˈt͡sʲiː.n̪a   (i→ə)
600: schwa becomes non-syllabic
    ˌra.ðəˈt͡sʲiː.n̪a → ˌraðə̯ˈt͡sʲiː.n̪a   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌraðə̯ˈt͡sʲiː.n̪a → ˌraðˈt͡sʲiː.n̪a   (ə̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌraðˈt͡sʲiː.n̪a → ˌraðˈt͡sʲiː.n̪ə   (a→ə)
750: vowel length resets to short
    ˌraðˈt͡sʲiː.n̪ə → ˌraðˈt͡sʲi.n̪ə   (ˈiː→ˈi)
750: ð deletes before a stop
    ˌraðˈt͡sʲi.n̪ə → ˌraˈt͡sʲi.n̪ə   (ð→∅)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌraˈt͡sʲi.n̪ə → ˌraˈt͡sʲĩ.n̪ə   (ˈi→ˈĩ)
1000: all affricates become sibilants (deaffrication)
    ˌraˈt͡sʲĩ.n̪ə → ˌraˈsʲĩ.n̪ə   (t͡sʲ→sʲ)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌraˈsʲĩ.n̪ə → ˌraˈsʲi.n̪ə   (ˈĩ→ˈi)
1200: the remaining anterior palatalized consonants depalatalize
    ˌraˈsʲi.n̪ə → ˌraˈsi.n̪ə   (sʲ→s)
1400: final ə becomes a non-syllabic off-glide
    ˌraˈsi.n̪ə → ˌraˈsin̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌraˈsin̪ə̯ → ˌraˈsin̪   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌraˈsin̪ → ˌʀaˈsin̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʀaˈsin̪ → ʀa.sin̪   (ˌa→a, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀa.sin̪ → ʁa.sin̪   (ʀ→ʁ)
```

## raide

`rˈigid̪ɑm` → `ʁwad̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈri.gi.d̪ɑm → ˈrɪ.gɪ.d̪ɑm   (ˈi→ˈɪ, i→ɪ)
-100: unstressed front vowel lost between g and a voiced coronal
    ˈrɪ.gɪ.d̪ɑm → ˈrɪg.d̪ɑm   (ɪ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈrɪg.d̪ɑm → ˈreg.d̪ɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈreg.d̪ɑm → ˈreg.d̪ɑ   (m→∅)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˈreg.d̪ɑ → ˈreɣ.d̪ɑ   (g→ɣ)
500: the low vowel fronts by default
    ˈreɣ.d̪ɑ → ˈreɣ.d̪a   (ɑ→a)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈreɣ.d̪a → ˈreʝ.d̪a   (ɣ→ʝ)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈreʝ.d̪a → ˈreʝ.d̪ʲa   (d̪→d̪ʲ)
600: ʝ weakens to j unconditionally
    ˈreʝ.d̪ʲa → ˈrej.d̪ʲa   (ʝ→j)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈrej.d̪ʲa → ˈrejj.d̪a   (d̪ʲ→jd̪)
600: j is lost after j or a consonant, before a consonant
    ˈrejj.d̪a → ˈrej.d̪a   (j→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈrej.d̪a → ˈrej.d̪ə   (a→ə)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈrej.d̪ə → ˈroj.d̪ə   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈroj.d̪ə → ˈruj.d̪ə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈruj.d̪ə → ˈruɛ̯.d̪ə   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈruɛ̯.d̪ə → ˈrwɛ.d̪ə   (ˈu→w, ɛ̯→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈrwɛ.d̪ə → ˈrwɛd̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrwɛd̪ə̯ → ˈrwɛd̪   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrwɛd̪ → ˈʀwɛd̪   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀwɛd̪ → ʀwɛd̪   (ˈɛ→ɛ)
1400: wɛ becomes wa
    ʀwɛd̪ → ʀwad̪   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀwad̪ → ʁwad̪   (ʀ→ʁ)
```

## raie

`rˈigɑm` → `ʁɛj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈri.gɑm → ˈrɪ.gɑm   (ˈi→ˈɪ)
-100: lax high vowels lower to tense mid vowels
    ˈrɪ.gɑm → ˈre.gɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈre.gɑm → ˈre.gɑ   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈre.gɑ → ˈre.ɣɑ   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈre.ɣɑ → ˈreː.ɣɑ   (ˈe→ˈeː)
500: the low vowel fronts by default
    ˈreː.ɣɑ → ˈreː.ɣa   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈreː.ɣa → ˈreː.ɣʲa   (ɣ→ɣʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈreː.ɣʲa → ˈreː.ʝa   (ɣʲ→ʝ)
600: ʝ weakens to j unconditionally
    ˈreː.ʝa → ˈreː.ja   (ʝ→j)
600: eːj/eːʝ shortens to ej
    ˈreː.ja → ˈre.ja   (ˈeː→ˈe)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈre.ja → ˈre.jə   (a→ə)
1000: stressed e laxes to ɛ before a consonant + vowel
    ˈre.jə → ˈrɛ.jə   (ˈe→ˈɛ)
1200: schwa desyllabifies after another vowel
    ˈrɛ.jə → ˈrɛjə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrɛjə̯ → ˈrɛj   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrɛj → ˈʀɛj   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀɛj → ʀɛj   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀɛj → ʁɛj   (ʀ→ʁ)
```

## raisin

`rˌɑkˈeːmum` → `ʁɛ.zɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌrɑˈkeː.mum → ˌrɑˈkeː.mʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌrɑˈkeː.mʊm → ˌrɑˈke.mʊm   (ˈeː→ˈe)
-100: lax high vowels lower to tense mid vowels
    ˌrɑˈke.mʊm → ˌrɑˈke.mom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌrɑˈke.mom → ˌrɑˈke.mo   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌrɑˈke.mo → ˌrɑˈkʲe.mo   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˌrɑˈkʲe.mo → ˌrɑˈce.mo   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˌrɑˈce.mo → ˌrɑˈceː.mo   (ˈe→ˈeː)
500: stressed eː raises to iː after a high-front consonant
    ˌrɑˈceː.mo → ˌrɑˈciː.mo   (ˈeː→ˈiː)
500: a palatal stop affricates
    ˌrɑˈciː.mo → ˌrɑˈt͡sʲiː.mo   (c→t͡sʲ)
500: the low vowel fronts by default
    ˌrɑˈt͡sʲiː.mo → ˌraˈt͡sʲiː.mo   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌraˈt͡sʲiː.mo → ˌraˈt͡sʲiː.mə   (o→ə)
600: schwa becomes non-syllabic
    ˌraˈt͡sʲiː.mə → ˌraˈt͡sʲiːmə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌraˈt͡sʲiːmə̯ → ˌraˈt͡sʲiːm   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌraˈt͡sʲiːm → ˌraˈd͡zʲiːm   (t͡sʲ→d͡zʲ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌraˈd͡zʲiːm → ˌraˈzʲiːm   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌraˈzʲiːm → ˌrajˈziːm   (zʲ→jz)
600: a coronal palatalizes between two high-front segments
    ˌrajˈziːm → ˌrajˈzʲiːm   (z→zʲ)
750: vowel length resets to short
    ˌrajˈzʲiːm → ˌrajˈzʲim   (ˈiː→ˈi)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌrajˈzʲim → ˌrajˈzʲĩm   (ˈi→ˈĩ)
1000: final m dentalizes after a vowel
    ˌrajˈzʲĩm → ˌrajˈzʲĩn̪   (m→n̪)
1200: nasalized ĩ lowers to ẽ
    ˌrajˈzʲĩn̪ → ˌrajˈzʲẽn̪   (ˈĩ→ˈẽ)
1200: the remaining anterior palatalized consonants depalatalize
    ˌrajˈzʲẽn̪ → ˌrajˈzẽn̪   (zʲ→z)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌrajˈzẽn̪ → ˌrajˈzẽː   (ˈẽn̪→ˈẽː)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌrajˈzẽː → ˌrɛːˈzẽː   (ˌaj→ˌɛː)
1400: nasalized ẽ lowers to ɛ̃
    ˌrɛːˈzẽː → ˌrɛːˈzɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: r becomes uvular ʀ
    ˌrɛːˈzɛ̃ː → ˌʀɛːˈzɛ̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʀɛːˈzɛ̃ː → ʀɛː.zɛ̃ː   (ˌɛː→ɛː, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    ʀɛː.zɛ̃ː → ʀɛ.zɛ̃   (ɛː→ɛ, ɛ̃ː→ɛ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀɛ.zɛ̃ → ʁɛ.zɛ̃   (ʀ→ʁ)
```

## raison

`rˌɑt̪iˈoːn̪em` → `ʁɛ.zɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌrɑ.t̪iˈoː.n̪em → ˌrɑ.t̪ɪˈoː.n̪ɛm   (i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌrɑ.t̪ɪˈoː.n̪ɛm → ˌrɑˈt̪joː.n̪ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌrɑˈt̪joː.n̪ɛm → ˌrɑˈt̪ʝoː.n̪ɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌrɑˈt̪ʝoː.n̪ɛm → ˌrɑˈt̪ʝo.n̪ɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌrɑˈt̪ʝo.n̪ɛm → ˌrɑˈt̪ʝo.n̪ɛ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌrɑˈt̪ʝo.n̪ɛ → ˌrɑt͡sʲˈʝo.n̪ɛ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌrɑt͡sʲˈʝo.n̪ɛ → ˌrɑˈt͡sʲo.n̪ɛ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌrɑˈt͡sʲo.n̪ɛ → ˌrɑˈt͡sʲoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌrɑˈt͡sʲoː.n̪ɛ → ˌrɑˈt͡sʲũː.n̪ɛ   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˌrɑˈt͡sʲũː.n̪ɛ → ˌraˈt͡sʲũː.n̪ɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌraˈt͡sʲũː.n̪ɛ → ˌraˈt͡sʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌraˈt͡sʲũː.n̪ə → ˌraˈt͡sʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌraˈt͡sʲũːn̪ə̯ → ˌraˈt͡sʲũːn̪   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌraˈt͡sʲũːn̪ → ˌraˈd͡zʲũːn̪   (t͡sʲ→d͡zʲ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌraˈd͡zʲũːn̪ → ˌraˈzʲũːn̪   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌraˈzʲũːn̪ → ˌrajˈzũːn̪   (zʲ→jz)
750: vowel length resets to short
    ˌrajˈzũːn̪ → ˌrajˈzũn̪   (ˈũː→ˈũ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌrajˈzũn̪ → ˌrajˈzũː   (ˈũn̪→ˈũː)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌrajˈzũː → ˌrɛːˈzũː   (ˌaj→ˌɛː)
1400: r becomes uvular ʀ
    ˌrɛːˈzũː → ˌʀɛːˈzũː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʀɛːˈzũː → ʀɛː.zũː   (ˌɛː→ɛː, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    ʀɛː.zũː → ʀɛ.zũ   (ɛː→ɛ, ũː→ũ)
1400: nasal ũ opens to ɔ̃
    ʀɛ.zũ → ʀɛ.zɔ̃   (ũ→ɔ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀɛ.zɔ̃ → ʁɛ.zɔ̃   (ʀ→ʁ)
```

## rire

`rˈiːd̪ere` → `ʁiʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈriː.d̪e.re → ˈriː.d̪ɛ.rɛ   (e→ɛ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˈriː.d̪ɛ.rɛ → ˈri.d̪ɛ.rɛ   (ˈiː→ˈi)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈri.d̪ɛ.rɛ → ˈri.ðɛ.rɛ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈri.ðɛ.rɛ → ˈriː.ðɛ.rɛ   (ˈi→ˈiː)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈriː.ðɛ.rɛ → ˈriː.ðrɛ   (ɛ→∅)
500: a vowel shortens before a consonant cluster
    ˈriː.ðrɛ → ˈri.ðrɛ   (ˈiː→ˈi)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈri.ðrɛ → ˈri.ðrə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈri.ðrə → ˈriðrə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈriðrə̯ → ˈri.ðrə   (ə̯→ə)
1000: the interdental fricatives (plain and palatalized) efface
    ˈri.ðrə → ˈri.rə   (ð→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈri.rə → ˈrirə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrirə̯ → ˈrir   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrir → ˈʀiʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀiʀ → ʀiʀ   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀiʀ → ʁiʁ   (ʀ→ʁ, ʀ→ʁ)
```

## ris

`rˈiːsum` → `ʁi`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈriː.sum → ˈriː.sʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈriː.sʊm → ˈri.sʊm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˈri.sʊm → ˈri.som   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈri.som → ˈri.so   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈri.so → ˈriː.so   (ˈi→ˈiː)
500: a voiceless fricative voices intervocalically
    ˈriː.so → ˈriː.zo   (s→z)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈriː.zo → ˈriː.zə   (o→ə)
600: schwa becomes non-syllabic
    ˈriː.zə → ˈriːzə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈriːzə̯ → ˈriːz   (ə̯→∅)
750: all final obstruents devoice
    ˈriːz → ˈriːs   (z→s)
750: vowel length resets to short
    ˈriːs → ˈris   (ˈiː→ˈi)
1000: a primary-stressed vowel lengthens before word-final s
    ˈris → ˈriːs   (ˈi→ˈiː)
1400: final obstruents are lost
    ˈriːs → ˈriː   (s→∅)
1400: r becomes uvular ʀ
    ˈriː → ˈʀiː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀiː → ʀiː   (ˈiː→iː)
1400: distinctive vowel length is lost entirely
    ʀiː → ʀi   (iː→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀi → ʁi   (ʀ→ʁ)
```

## rive

`rˈiːpɑm` → `ʁiv`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈriː.pɑm → ˈri.pɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈri.pɑm → ˈri.pɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈri.pɑ → ˈriː.pɑ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˈriː.pɑ → ˈriː.pa   (ɑ→a)
600: a voiceless consonant voices intervocalically
    ˈriː.pa → ˈriː.ba   (p→b)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈriː.ba → ˈriː.βa   (b→β)
600: the remaining bilabial fricative becomes v
    ˈriː.βa → ˈriː.va   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈriː.va → ˈriː.və   (a→ə)
750: vowel length resets to short
    ˈriː.və → ˈri.və   (ˈiː→ˈi)
1400: final ə becomes a non-syllabic off-glide
    ˈri.və → ˈrivə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrivə̯ → ˈriv   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈriv → ˈʀiv   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀiv → ʀiv   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀiv → ʁiv   (ʀ→ʁ)
```

## rompre

`rˈumpere` → `ʁɔ̃pʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈrum.pe.re → ˈrʊm.pɛ.rɛ   (ˈu→ˈʊ, e→ɛ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈrʊm.pɛ.rɛ → ˈrom.pɛ.rɛ   (ˈʊ→ˈo)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈrom.pɛ.rɛ → ˈrom.prɛ   (ɛ→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈrom.prɛ → ˈrũm.prɛ   (ˈo→ˈũ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈrũm.prɛ → ˈrũm.prə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈrũm.prə → ˈrũmprə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈrũmprə̯ → ˈrũm.prə   (ə̯→ə)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈrũm.prə → ˈrũː.prə   (ˈũm→ˈũː)
1400: final ə becomes a non-syllabic off-glide
    ˈrũː.prə → ˈrũːprə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrũːprə̯ → ˈrũːpr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrũːpr → ˈʀũːpʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀũːpʀ → ʀũːpʀ   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    ʀũːpʀ → ʀũpʀ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    ʀũpʀ → ʀɔ̃pʀ   (ũ→ɔ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀɔ̃pʀ → ʁɔ̃pʁ   (ʀ→ʁ, ʀ→ʁ)
```

## ronce

`rˈumikem` → `ʁɔ̃s`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈru.mi.kem → ˈrʊ.mɪ.kɛm   (ˈu→ˈʊ, i→ɪ, e→ɛ)
-100: lax high vowels lower to tense mid vowels
    ˈrʊ.mɪ.kɛm → ˈro.me.kɛm   (ˈʊ→ˈo, ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈro.me.kɛm → ˈro.me.kɛ   (m→∅)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˈro.me.kɛ → ˈro.me.kʲɛ   (k→kʲ)
-100: a segment marked both back and front loses the back specification
    ˈro.me.kʲɛ → ˈro.me.cɛ   (kʲ→c)
300: a stressed vowel lengthens before a single consonant + glide
    ˈro.me.cɛ → ˈroː.me.cɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈroː.me.cɛ → ˈrũː.me.cɛ   (ˈoː→ˈũː)
500: a palatal stop affricates
    ˈrũː.me.cɛ → ˈrũː.me.t͡sʲɛ   (c→t͡sʲ)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈrũː.me.t͡sʲɛ → ˈrũː.mə.t͡sʲɛ   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈrũː.mə.t͡sʲɛ → ˈrũː.mə.t͡sʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈrũː.mə.t͡sʲə → ˈrũːmə̯t͡sʲə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈrũːmə̯t͡sʲə̯ → ˈrũːmə̯.t͡sʲə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈrũːmə̯.t͡sʲə → ˈrũːm.t͡sʲə   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈrũːm.t͡sʲə → ˈrũm.t͡sʲə   (ˈũː→ˈũ)
1000: all affricates become sibilants (deaffrication)
    ˈrũm.t͡sʲə → ˈrũm.sʲə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈrũm.sʲə → ˈrũm.sə   (sʲ→s)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈrũm.sə → ˈrũː.sə   (ˈũm→ˈũː)
1400: final ə becomes a non-syllabic off-glide
    ˈrũː.sə → ˈrũːsə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈrũːsə̯ → ˈrũːs   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈrũːs → ˈʀũːs   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀũːs → ʀũːs   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    ʀũːs → ʀũs   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    ʀũs → ʀɔ̃s   (ũ→ɔ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀɔ̃s → ʁɔ̃s   (ʀ→ʁ)
```

## rouge

`rˈubeum` → `ʁuʒ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈru.be.um → ˈrʊ.bɛ.ʊm   (ˈu→ˈʊ, e→ɛ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈrʊ.bɛ.ʊm → ˈrʊ.bjʊm   (ɛ→j)
-100: yod strengthens before a vowel
    ˈrʊ.bjʊm → ˈrʊ.bʝʊm   (j→ʝ)
-100: lax high vowels lower to tense mid vowels
    ˈrʊ.bʝʊm → ˈro.bʝom   (ˈʊ→ˈo, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈro.bʝom → ˈro.bʝo   (m→∅)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˈro.bʝo → ˈrob.ɟo   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈrob.ɟo → ˈro.bd͡ʒo   (ɟ→d͡ʒ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈro.bd͡ʒo → ˈro.bd͡ʒə   (o→ə)
600: schwa becomes non-syllabic
    ˈro.bd͡ʒə → ˈrobd͡ʒə̯   (ə→ə̯)
600: non-syllabic schwa restores after a postalveolar affricate
    ˈrobd͡ʒə̯ → ˈro.bd͡ʒə   (ə̯→ə)
600: a labial consonant becomes d before a voiced coronal stop
    ˈro.bd͡ʒə → ˈro.d̪d͡ʒə   (b→d̪)
750: a dental stop deletes before another coronal stop
    ˈro.d̪d͡ʒə → ˈro.d͡ʒə   (d̪→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈro.d͡ʒə → ˈru.d͡ʒə   (ˈo→ˈu)
1000: all affricates become sibilants (deaffrication)
    ˈru.d͡ʒə → ˈru.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈru.ʒə → ˈruʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈruʒə̯ → ˈruʒ   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈruʒ → ˈʀuʒ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀuʒ → ʀuʒ   (ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀuʒ → ʁuʒ   (ʀ→ʁ)
```

## rue

`rˈuːgɑm` → `ʁy`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈruː.gɑm → ˈru.gɑm   (ˈuː→ˈu)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈru.gɑm → ˈru.gɑ   (m→∅)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˈru.gɑ → ˈru.ɣɑ   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈru.ɣɑ → ˈruː.ɣɑ   (ˈu→ˈuː)
500: the velar fricative is lost between a high round vowel and a low vowel
    ˈruː.ɣɑ → ˈruː.ɑ   (ɣ→∅)
500: the low vowel fronts by default
    ˈruː.ɑ → ˈruː.a   (ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˈruː.a → ˈrʉː.a   (ˈuː→ˈʉː)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈrʉː.a → ˈrʉː.ə   (a→ə)
750: vowel length resets to short
    ˈrʉː.ə → ˈrʉ.ə   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈrʉ.ə → ˈry.ə   (ˈʉ→ˈy)
1200: schwa desyllabifies after another vowel
    ˈry.ə → ˈryə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈryə̯ → ˈryː   (ˈyə̯→ˈyː)
1400: r becomes uvular ʀ
    ˈryː → ˈʀyː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀyː → ʀyː   (ˈyː→yː)
1400: distinctive vowel length is lost entirely
    ʀyː → ʀy   (yː→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀy → ʁy   (ʀ→ʁ)
```

## sache

`sˈɑpiɑm` → `saʃ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsɑ.pi.ɑm → ˈsɑ.pɪ.ɑm   (i→ɪ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈsɑ.pɪ.ɑm → ˈsɑ.pjɑm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈsɑ.pjɑm → ˈsɑ.pʝɑm   (j→ʝ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsɑ.pʝɑm → ˈsɑ.pʝɑ   (m→∅)
500: the low vowel fronts by default
    ˈsɑ.pʝɑ → ˈsa.pʝa   (ˈɑ→ˈa, ɑ→a)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˈsa.pʝa → ˈsap.ɟa   (ʝ→ɟ)
600: ɟ devoices to c after a voiceless segment
    ˈsap.ɟa → ˈsap.ca   (ɟ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈsap.ca → ˈsa.pt͡ʃa   (c→t͡ʃ)
600: a labial consonant becomes t before a voiceless coronal stop
    ˈsa.pt͡ʃa → ˈsa.t̪t͡ʃa   (p→t̪)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈsa.t̪t͡ʃa → ˈsa.t̪t͡ʃə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈsa.t̪t͡ʃə → ˈsa.t͡ʃə   (t̪→∅)
1000: all affricates become sibilants (deaffrication)
    ˈsa.t͡ʃə → ˈsa.ʃə   (t͡ʃ→ʃ)
1400: final ə becomes a non-syllabic off-glide
    ˈsa.ʃə → ˈsaʃə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsaʃə̯ → ˈsaʃ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsaʃ → saʃ   (ˈa→a)
```

## saint

`sˈɑn̪kt̪um` → `sɛ̃`

```
-100: n assimilates to a following velar stop
    ˈsɑn̪k.t̪um → ˈsɑŋk.t̪um   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsɑŋk.t̪um → ˈsɑŋk.t̪ʊm   (u→ʊ)
-100: k lost after ŋ before a voiceless coronal
    ˈsɑŋk.t̪ʊm → ˈsɑŋ.t̪ʊm   (k→∅)
-100: lax high vowels lower to tense mid vowels
    ˈsɑŋ.t̪ʊm → ˈsɑŋ.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsɑŋ.t̪om → ˈsɑŋ.t̪o   (m→∅)
500: ŋ palatalizes to ɲ before a coronal
    ˈsɑŋ.t̪o → ˈsɑɲ.t̪o   (ŋ→ɲ)
500: the low vowel fronts by default
    ˈsɑɲ.t̪o → ˈsaɲ.t̪o   (ˈɑ→ˈa)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈsaɲ.t̪o → ˈsaɲ.t̪ʲo   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsaɲ.t̪ʲo → ˈsaɲ.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈsaɲ.t̪ʲə → ˈsaɲt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsaɲt̪ʲə̯ → ˈsaɲt̪ʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈsaɲt̪ʲ → ˈsaɲjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈsaɲjt̪ → ˈsaɲt̪   (j→∅)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˈsaɲt̪ → ˈsaj̃n̪t̪   (ɲ→j̃n̪)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈsaj̃n̪t̪ → ˈsaj̃t̪   (n̪→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈsaj̃t̪ → ˈsãj̃t̪   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˈsãj̃t̪ → ˈsɛ̃j̃t̪   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˈsɛ̃j̃t̪ → ˈsɛ̃t̪   (j̃→∅)
1400: final obstruents are lost
    ˈsɛ̃t̪ → ˈsɛ̃   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛ̃ → sɛ̃   (ˈɛ̃→ɛ̃)
```

## sainteté

`sˌɑn̪kt̪it̪ˈɑːt̪em` → `sɛ̃.t̪e`

```
-100: n assimilates to a following velar stop
    ˌsɑn̪k.t̪iˈt̪ɑː.t̪em → ˌsɑŋk.t̪iˈt̪ɑː.t̪em   (n̪→ŋ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑŋk.t̪iˈt̪ɑː.t̪em → ˌsɑŋk.t̪ɪˈt̪ɑː.t̪ɛm   (i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑŋk.t̪ɪˈt̪ɑː.t̪ɛm → ˌsɑŋk.t̪ɪˈt̪ɑ.t̪ɛm   (ˈɑː→ˈɑ)
-100: k lost after ŋ before a voiceless coronal
    ˌsɑŋk.t̪ɪˈt̪ɑ.t̪ɛm → ˌsɑŋ.t̪ɪˈt̪ɑ.t̪ɛm   (k→∅)
-100: lax high vowels lower to tense mid vowels
    ˌsɑŋ.t̪ɪˈt̪ɑ.t̪ɛm → ˌsɑŋ.t̪eˈt̪ɑ.t̪ɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɑŋ.t̪eˈt̪ɑ.t̪ɛm → ˌsɑŋ.t̪eˈt̪ɑ.t̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɑŋ.t̪eˈt̪ɑ.t̪ɛ → ˌsɑŋ.t̪eˈt̪ɑː.t̪ɛ   (ˈɑ→ˈɑː)
500: ŋ palatalizes to ɲ before a coronal
    ˌsɑŋ.t̪eˈt̪ɑː.t̪ɛ → ˌsɑɲ.t̪eˈt̪ɑː.t̪ɛ   (ŋ→ɲ)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌsɑɲ.t̪eˈt̪ɑː.t̪ɛ → ˌsɑɲt̪ˈt̪ɑː.t̪ɛ   (e→∅)
500: the low vowel fronts by default
    ˌsɑɲt̪ˈt̪ɑː.t̪ɛ → ˌsaɲt̪ˈt̪aː.t̪ɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
500: geminate t degeminates after a consonant
    ˌsaɲt̪ˈt̪aː.t̪ɛ → ˌsaɲˈt̪aː.t̪ɛ   (t̪→∅)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌsaɲˈt̪aː.t̪ɛ → ˌsaɲˈt̪ʲaː.t̪ɛ   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsaɲˈt̪ʲaː.t̪ɛ → ˌsaɲˈt̪ʲaː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsaɲˈt̪ʲaː.t̪ə → ˌsaɲˈt̪ʲaːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsaɲˈt̪ʲaːt̪ə̯ → ˌsaɲˈt̪ʲaːt̪   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌsaɲˈt̪ʲaːt̪ → ˌsaɲjˈt̪aːt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌsaɲjˈt̪aːt̪ → ˌsaɲˈt̪aːt̪   (j→∅)
600: long stressed vowels diphthongize
    ˌsaɲˈt̪aːt̪ → ˌsaɲˈt̪ae̯t̪   (ˈaː→ˈae̯)
750: a word-final stop re-opens to a fricative after a vowel
    ˌsaɲˈt̪ae̯t̪ → ˌsaɲˈt̪ae̯θ   (t̪→θ)
750: pre-consonantal ɲ resolves to a nasalized j + dental n
    ˌsaɲˈt̪ae̯θ → ˌsaj̃n̪ˈt̪ae̯θ   (ɲ→j̃n̪)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌsaj̃n̪ˈt̪ae̯θ → ˌsaj̃n̪ˈt̪eːθ   (ˈae̯→ˈeː)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌsaj̃n̪ˈt̪eːθ → ˌsaj̃ˈt̪eːθ   (n̪→∅)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌsaj̃ˈt̪eːθ → ˌsãj̃ˈt̪eːθ   (ˌa→ˌã)
1000: vowel length resets to short
    ˌsãj̃ˈt̪eːθ → ˌsãj̃ˈt̪eθ   (ˈeː→ˈe)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌsãj̃ˈt̪eθ → ˌsɛ̃j̃ˈt̪eθ   (ˌã→ˌɛ̃)
1000: the interdental fricatives (plain and palatalized) efface
    ˌsɛ̃j̃ˈt̪eθ → ˌsɛ̃j̃ˈt̪e   (θ→∅)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌsɛ̃j̃ˈt̪e → ˌsɛ̃ˈt̪e   (j̃→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɛ̃ˈt̪e → sɛ̃.t̪e   (ˌɛ̃→ɛ̃, ˈe→e)
```

## santé

`sˌɑːn̪it̪ˈɑːt̪em` → `sɑ̃.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑː.n̪iˈt̪ɑː.t̪em → ˌsɑː.n̪ɪˈt̪ɑː.t̪ɛm   (i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑː.n̪ɪˈt̪ɑː.t̪ɛm → ˌsɑ.n̪ɪˈt̪ɑ.t̪ɛm   (ˌɑː→ˌɑ, ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌsɑ.n̪ɪˈt̪ɑ.t̪ɛm → ˌsɑ.n̪eˈt̪ɑ.t̪ɛm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɑ.n̪eˈt̪ɑ.t̪ɛm → ˌsɑ.n̪eˈt̪ɑ.t̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɑ.n̪eˈt̪ɑ.t̪ɛ → ˌsɑ.n̪eˈt̪ɑː.t̪ɛ   (ˈɑ→ˈɑː)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌsɑ.n̪eˈt̪ɑː.t̪ɛ → ˌsɑn̪ˈt̪ɑː.t̪ɛ   (e→∅)
500: the low vowel fronts by default
    ˌsɑn̪ˈt̪ɑː.t̪ɛ → ˌsan̪ˈt̪aː.t̪ɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsan̪ˈt̪aː.t̪ɛ → ˌsan̪ˈt̪aː.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsan̪ˈt̪aː.t̪ə → ˌsan̪ˈt̪aːt̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsan̪ˈt̪aːt̪ə̯ → ˌsan̪ˈt̪aːt̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌsan̪ˈt̪aːt̪ → ˌsan̪ˈt̪ae̯t̪   (ˈaː→ˈae̯)
750: a word-final stop re-opens to a fricative after a vowel
    ˌsan̪ˈt̪ae̯t̪ → ˌsan̪ˈt̪ae̯θ   (t̪→θ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌsan̪ˈt̪ae̯θ → ˌsan̪ˈt̪eːθ   (ˈae̯→ˈeː)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌsan̪ˈt̪eːθ → ˌsãn̪ˈt̪eːθ   (ˌa→ˌã)
1000: vowel length resets to short
    ˌsãn̪ˈt̪eːθ → ˌsãn̪ˈt̪eθ   (ˈeː→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˌsãn̪ˈt̪eθ → ˌsãn̪ˈt̪e   (θ→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsãn̪ˈt̪e → ˌsãːˈt̪e   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌsãːˈt̪e → ˌsɑ̃ːˈt̪e   (ˌãː→ˌɑ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɑ̃ːˈt̪e → sɑ̃ː.t̪e   (ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    sɑ̃ː.t̪e → sɑ̃.t̪e   (ɑ̃ː→ɑ̃)
```

## sauter

`sˌɑlt̪ˈɑːre` → `so.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑlˈt̪ɑː.re → ˌsɑlˈt̪ɑː.rɛ   (e→ɛ)
-100: l darkens before a non-lateral consonant
    ˌsɑlˈt̪ɑː.rɛ → ˌsɑɫˈt̪ɑː.rɛ   (l→ɫ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑɫˈt̪ɑː.rɛ → ˌsɑɫˈt̪ɑ.rɛ   (ˈɑː→ˈɑ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɑɫˈt̪ɑ.rɛ → ˌsɑɫˈt̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌsɑɫˈt̪ɑː.rɛ → ˌsaɫˈt̪aː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌsaɫˈt̪aː.rɛ → ˌsaɫˈt̪ʲaː.rɛ   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsaɫˈt̪ʲaː.rɛ → ˌsaɫˈt̪ʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsaɫˈt̪ʲaː.rə → ˌsaɫˈt̪ʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsaɫˈt̪ʲaːrə̯ → ˌsaɫˈt̪ʲaːr   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌsaɫˈt̪ʲaːr → ˌsaɫjˈt̪aːr   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌsaɫjˈt̪aːr → ˌsaɫˈt̪aːr   (j→∅)
600: long stressed vowels diphthongize
    ˌsaɫˈt̪aːr → ˌsaɫˈt̪ae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌsaɫˈt̪ae̯r → ˌsaɫˈt̪eːr   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌsaɫˈt̪eːr → ˌsaɫˈt̪er   (ˈeː→ˈe)
1000: back dark-l variants vocalize to w
    ˌsaɫˈt̪er → ˌsawˈt̪er   (ɫ→w)
1200: aw becomes long oː
    ˌsawˈt̪er → ˌsoːˈt̪er   (ˌaw→ˌoː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsoːˈt̪er → ˌsoːˈt̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌsoːˈt̪eɹ → ˌsoːˈt̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsoːˈt̪e → soː.t̪e   (ˌoː→oː, ˈe→e)
1400: distinctive vowel length is lost entirely
    soː.t̪e → so.t̪e   (oː→o)
```

## sceau

`sˌigˈelloːs` → `so`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsiˈgel.loːs → ˌsɪˈgɛl.loːs   (ˌi→ˌɪ, ˈe→ˈɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɪˈgɛl.loːs → ˌsɪˈgɛl.los   (oː→o)
-100: lax high vowels lower to tense mid vowels
    ˌsɪˈgɛl.los → ˌseˈgɛl.los   (ˌɪ→ˌe)
-100: a velar stop fronts before a following front non-low continuant (second palatalization trigger)
    ˌseˈgɛl.los → ˌseˈgʲɛl.los   (g→gʲ)
-100: a segment marked both back and front loses the back specification
    ˌseˈgʲɛl.los → ˌseˈɟɛl.los   (gʲ→ɟ)
-100: a voiced high stop/affricate spirantizes after a vowel before a sonorant or yod
    ˌseˈɟɛl.los → ˌseˈʝɛl.los   (ɟ→ʝ)
500: yod lost after secondary-stressed e before a vowel
    ˌseˈʝɛl.los → ˌseˈɛl.los   (ʝ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌseˈɛl.los → ˌseˈɛl.ləs   (o→ə)
600: schwa becomes non-syllabic
    ˌseˈɛl.ləs → ˌseˈɛllə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌseˈɛllə̯s → ˌseˈɛlls   (ə̯→∅)
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˌseˈɛlls → ˌseˈɛls   (l→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌseˈɛls → ˌseˈɛɫs   (l→ɫ)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌseˈɛɫs → ˌsəˈɛɫs   (ˌe→ˌə)
1000: back dark-l variants vocalize to w
    ˌsəˈɛɫs → ˌsəˈɛws   (ɫ→w)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌsəˈɛws → ˌsəˈɛa̯ws   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌsəˈɛa̯ws → ˌsəˈe̯aws   (ˈɛ→e̯, a̯→ˈa)
1200: a stressless schwa desyllabifies before another vowel
    ˌsəˈe̯aws → ˈsə̯e̯aws   (ˌə→ə̯)
1200: aw becomes long oː
    ˈsə̯e̯aws → ˈsə̯e̯oːs   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˈsə̯e̯oːs → ˈsə̯ə̯oːs   (e̯→ə̯)
1200: a non-syllabic schwa effaces after another vowel
    ˈsə̯ə̯oːs → ˈsə̯oːs   (ə̯→∅)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈsə̯oːs → ˈsoːs   (ə̯→∅)
1400: final obstruents are lost
    ˈsoːs → ˈsoː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsoː → soː   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    soː → so   (oː→o)
```

## sec

`sˈikkum` → `sek`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsik.kum → ˈsɪk.kʊm   (ˈi→ˈɪ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈsɪk.kʊm → ˈsek.kom   (ˈɪ→ˈe, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsek.kom → ˈsek.ko   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsek.ko → ˈsek.kə   (o→ə)
600: schwa becomes non-syllabic
    ˈsek.kə → ˈsekkə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsekkə̯ → ˈsekk   (ə̯→∅)
1200: geminates simplify to single consonants
    ˈsekk → ˈsek   (k→∅)
1400: final f/k/s are supported by an epenthetic off-glide (escaping the coming consonant loss)
    ˈsek → ˈsekə̯   (∅→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsekə̯ → ˈsek   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsek → sek   (ˈe→e)
```

## seigneur

`sˌen̪iˈoːrem` → `sɛ.ɲœʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌse.n̪iˈoː.rem → ˌsɛ.n̪ɪˈoː.rɛm   (ˌe→ˌɛ, i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌsɛ.n̪ɪˈoː.rɛm → ˌsɛˈn̪joː.rɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌsɛˈn̪joː.rɛm → ˌsɛn̪ˈʝoː.rɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɛn̪ˈʝoː.rɛm → ˌsɛn̪ˈʝo.rɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɛn̪ˈʝo.rɛm → ˌsɛn̪ˈʝo.rɛ   (m→∅)
300: the coronal nasal palatalizes before yod
    ˌsɛn̪ˈʝo.rɛ → ˌsɛˈɲo.rɛ   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɛˈɲo.rɛ → ˌsɛˈɲoː.rɛ   (ˈo→ˈoː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsɛˈɲoː.rɛ → ˌsɛˈɲoː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsɛˈɲoː.rə → ˌsɛˈɲoːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsɛˈɲoːrə̯ → ˌsɛˈɲoːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌsɛˈɲoːr → ˌsɛˈɲowr   (ˈoː→ˈow)
600: secondary-stressed ɛ raises to e before any two segments
    ˌsɛˈɲowr → ˌseˈɲowr   (ˌɛ→ˌe)
600: the tonic ow diphthong fronts to ø before r (final-accuracy fix, not DiaCLEF)
    ˌseˈɲowr → ˌseˈɲør   (ˈow→ˈø)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌseˈɲør → ˌsəˈɲør   (ˌe→ˌə)
1000: secondary-stressed schwa reverts to e before a palatal consonant
    ˌsəˈɲør → ˌseˈɲør   (ˌə→ˌe)
1000: a glide develops between a stressed mid front vowel and intervocalic ɲ
    ˌseˈɲør → ˌsej̃ˈɲør   (∅→j̃)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌsej̃ˈɲør → ˌsẽj̃ˈɲør   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌsẽj̃ˈɲør → ˌsɛ̃j̃ˈɲør   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌsɛ̃j̃ˈɲør → ˌsãj̃ˈɲør   (ˌɛ̃→ˌã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌsãj̃ˈɲør → ˌsɛ̃j̃ˈɲør   (ˌã→ˌɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌsɛ̃j̃ˈɲør → ˌsɛ̃ˈɲør   (j̃→∅)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˌsɛ̃ˈɲør → ˌsɛˈɲør   (ˌɛ̃→ˌɛ)
1400: e/ø lax before an r that closes the syllable
    ˌsɛˈɲør → ˌsɛˈɲœr   (ˈø→ˈœ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsɛˈɲœr → ˌsɛˈɲœɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌsɛˈɲœɹ → ˌsɛˈɲœr   (ɹ→r)
1400: r becomes uvular ʀ
    ˌsɛˈɲœr → ˌsɛˈɲœʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɛˈɲœʀ → sɛ.ɲœʀ   (ˌɛ→ɛ, ˈœ→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɛ.ɲœʀ → sɛ.ɲœʁ   (ʀ→ʁ)
```

## sept

`sˈept̪em` → `sɛ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsep.t̪em → ˈsɛp.t̪ɛm   (ˈe→ˈɛ, e→ɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsɛp.t̪ɛm → ˈsɛp.t̪ɛ   (m→∅)
500: a labial stop becomes t before a voiceless coronal stop
    ˈsɛp.t̪ɛ → ˈsɛt̪.t̪ɛ   (p→t̪)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsɛt̪.t̪ɛ → ˈsɛt̪.t̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈsɛt̪.t̪ə → ˈsɛt̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsɛt̪t̪ə̯ → ˈsɛt̪t̪   (ə̯→∅)
750: a dental stop deletes before another coronal stop
    ˈsɛt̪t̪ → ˈsɛt̪   (t̪→∅)
1400: final obstruents are lost
    ˈsɛt̪ → ˈsɛ   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛ → sɛ   (ˈɛ→ɛ)
```

## sert

`sˈerwit̪` → `sɛʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈse.rwit̪ → ˈser.ɣʷit̪   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈser.ɣʷit̪ → ˈsɛr.ɣʷɪt̪   (ˈe→ˈɛ, i→ɪ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈsɛr.ɣʷɪt̪ → ˈsɛr.βʷɪt̪   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈsɛr.βʷɪt̪ → ˈsɛr.βʷet̪   (ɪ→e)
500: labialized bilabial fricatives delabialize
    ˈsɛr.βʷet̪ → ˈsɛr.βet̪   (βʷ→β)
600: t/d spirantize word-finally after a vowel
    ˈsɛr.βet̪ → ˈsɛr.βeθ   (t̪→θ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsɛr.βeθ → ˈsɛr.βəθ   (e→ə)
600: schwa becomes non-syllabic
    ˈsɛr.βəθ → ˈsɛrβə̯θ   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsɛrβə̯θ → ˈsɛrβθ   (ə̯→∅)
600: a dental fricative hardens to a stop after a consonant, word-finally
    ˈsɛrβθ → ˈsɛrβt̪   (θ→t̪)
600: a labial consonant becomes t before a voiceless coronal stop
    ˈsɛrβt̪ → ˈsɛrt̪t̪   (β→t̪)
600: an identical consonant geminate reduces to one, after a consonant or word start
    ˈsɛrt̪t̪ → ˈsɛrt̪   (t̪→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsɛrt̪ → ˈsɛɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈsɛɹt̪ → ˈsɛɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsɛɹ → ˈsɛr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsɛr → ˈsɛʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛʀ → sɛʀ   (ˈɛ→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɛʀ → sɛʁ   (ʀ→ʁ)
```

## servir

`sˌerwˈiːre` → `sɛʁ.viʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌseˈrwiː.re → ˌserˈɣʷiː.re   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌserˈɣʷiː.re → ˌsɛrˈɣʷiː.rɛ   (ˌe→ˌɛ, e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌsɛrˈɣʷiː.rɛ → ˌsɛrˈβʷiː.rɛ   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɛrˈβʷiː.rɛ → ˌsɛrˈβʷi.rɛ   (ˈiː→ˈi)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɛrˈβʷi.rɛ → ˌsɛrˈβʷiː.rɛ   (ˈi→ˈiː)
500: labialized bilabial fricatives delabialize
    ˌsɛrˈβʷiː.rɛ → ˌsɛrˈβiː.rɛ   (βʷ→β)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsɛrˈβiː.rɛ → ˌsɛrˈβiː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsɛrˈβiː.rə → ˌsɛrˈβiːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsɛrˈβiːrə̯ → ˌsɛrˈβiːr   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌsɛrˈβiːr → ˌserˈβiːr   (ˌɛ→ˌe)
600: the remaining bilabial fricative becomes v
    ˌserˈβiːr → ˌserˈviːr   (β→v)
750: vowel length resets to short
    ˌserˈviːr → ˌserˈvir   (ˈiː→ˈi)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌserˈvir → ˌsɛrˈvir   (ˌe→ˌɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsɛrˈvir → ˌsɛɹˈviɹ   (r→ɹ, r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌsɛɹˈviɹ → ˌsɛrˈvir   (ɹ→r, ɹ→r)
1400: r becomes uvular ʀ
    ˌsɛrˈvir → ˌsɛʀˈviʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌsɛʀˈviʀ → sɛʀ.viʀ   (ˌɛ→ɛ, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    sɛʀ.viʀ → sɛʁ.viʁ   (ʀ→ʁ, ʀ→ʁ)
```

## singe

`sˈiːmium` → `sɛ̃ʒ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsiː.mi.um → ˈsiː.mɪ.ʊm   (i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈsiː.mɪ.ʊm → ˈsiː.mjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈsiː.mjʊm → ˈsiːm.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˈsiːm.ʝʊm → ˈsim.ʝʊm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˈsim.ʝʊm → ˈsim.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsim.ʝom → ˈsim.ʝo   (m→∅)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˈsim.ʝo → ˈsim.ɟo   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈsim.ɟo → ˈsim.d͡ʒo   (ɟ→d͡ʒ)
600: m becomes n before dʒ
    ˈsim.d͡ʒo → ˈsin̪.d͡ʒo   (m→n̪)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsin̪.d͡ʒo → ˈsin̪.d͡ʒə   (o→ə)
600: schwa becomes non-syllabic
    ˈsin̪.d͡ʒə → ˈsin̪d͡ʒə̯   (ə→ə̯)
600: non-syllabic schwa restores after a postalveolar affricate
    ˈsin̪d͡ʒə̯ → ˈsin̪.d͡ʒə   (ə̯→ə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈsin̪.d͡ʒə → ˈsĩn̪.d͡ʒə   (ˈi→ˈĩ)
1000: all affricates become sibilants (deaffrication)
    ˈsĩn̪.d͡ʒə → ˈsĩn̪.ʒə   (d͡ʒ→ʒ)
1200: nasalized ĩ lowers to ẽ
    ˈsĩn̪.ʒə → ˈsẽn̪.ʒə   (ˈĩ→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈsẽn̪.ʒə → ˈsẽː.ʒə   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈsẽː.ʒə → ˈsɛ̃ː.ʒə   (ˈẽː→ˈɛ̃ː)
1400: final ə becomes a non-syllabic off-glide
    ˈsɛ̃ː.ʒə → ˈsɛ̃ːʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsɛ̃ːʒə̯ → ˈsɛ̃ːʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛ̃ːʒ → sɛ̃ːʒ   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    sɛ̃ːʒ → sɛ̃ʒ   (ɛ̃ː→ɛ̃)
```

## sommier

`sˌɑgmˈɑːrium` → `sɔ.mje`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌsɑˈgmɑː.ri.um → ˌsɑˈgmɑː.rɪ.ʊm   (i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌsɑˈgmɑː.rɪ.ʊm → ˌsɑˈgmɑː.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌsɑˈgmɑː.rjʊm → ˌsɑˈgmɑːr.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɑˈgmɑːr.ʝʊm → ˌsɑˈgmɑr.ʝʊm   (ˈɑː→ˈɑ)
-100: g spirantizes before m
    ˌsɑˈgmɑr.ʝʊm → ˌsɑˈɣmɑr.ʝʊm   (g→ɣ)
-100: the resulting velar fricative becomes w before m
    ˌsɑˈɣmɑr.ʝʊm → ˌsɑwˈmɑr.ʝʊm   (ɣ→w)
-100: lax high vowels lower to tense mid vowels
    ˌsɑwˈmɑr.ʝʊm → ˌsɑwˈmɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɑwˈmɑr.ʝom → ˌsɑwˈmɑr.ʝo   (m→∅)
500: r + yod becomes palatalized r
    ˌsɑwˈmɑr.ʝo → ˌsɑwˈmɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌsɑwˈmɑ.rʲo → ˌsawˈma.rʲo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌsawˈma.rʲo → ˌsawˈmaː.rʲo   (ˈa→ˈaː)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌsawˈmaː.rʲo → ˌsɔwˈmaː.rʲo   (ˌa→ˌɔ)
600: aːrʲ metathesizes to jɛːr
    ˌsɔwˈmaː.rʲo → ˌsɔwˈmjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsɔwˈmjɛː.ro → ˌsɔwˈmjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌsɔwˈmjɛː.rə → ˌsɔwˈmjɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsɔwˈmjɛːrə̯ → ˌsɔwˈmjɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌsɔwˈmjɛːr → ˌsɔwˈmjie̯r   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌsɔwˈmjie̯r → ˌsɔwˈmie̯r   (j→∅)
600: secondary-stressed ɔ raises to ɯ before w
    ˌsɔwˈmie̯r → ˌsɯwˈmie̯r   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌsɯwˈmie̯r → ˌsɔwˈmie̯r   (ˌɯ→ˌɔ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌsɔwˈmie̯r → ˌsɔˈmie̯r   (w→∅)
600: a back round vowel raises to nasalized high tense before a nasal consonant (recurrence)
    ˌsɔˈmie̯r → ˌsũˈmie̯r   (ˌɔ→ˌũ)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌsũˈmie̯r → ˌsũˈmjer   (ˈi→j, e̯→ˈe)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsũˈmjer → ˌsũˈmjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌsũˈmjeɹ → ˌsũˈmje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsũˈmje → sũ.mje   (ˌũ→ũ, ˈe→e)
1400: nasal ũ opens to ɔ̃
    sũ.mje → sɔ̃.mje   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    sɔ̃.mje → sɔ.mje   (ɔ̃→ɔ)
```

## sont

`sˈun̪t̪` → `sɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsun̪t̪ → ˈsʊn̪t̪   (ˈu→ˈʊ)
-100: lax high vowels lower to tense mid vowels
    ˈsʊn̪t̪ → ˈson̪t̪   (ˈʊ→ˈo)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˈson̪t̪ → ˈsũn̪t̪   (ˈo→ˈũ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈsũn̪t̪ → ˈsũːt̪   (ˈũn̪→ˈũː)
1400: final obstruents are lost
    ˈsũːt̪ → ˈsũː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsũː → sũː   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    sũː → sũ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    sũ → sɔ̃   (ũ→ɔ̃)
```

## souder

`sˌolid̪ˈɑːre` → `su.d̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌso.liˈd̪ɑː.re → ˌsɔ.lɪˈd̪ɑː.rɛ   (ˌo→ˌɔ, i→ɪ, e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɔ.lɪˈd̪ɑː.rɛ → ˌsɔ.lɪˈd̪ɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌsɔ.lɪˈd̪ɑ.rɛ → ˌsɔ.leˈd̪ɑ.rɛ   (ɪ→e)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌsɔ.leˈd̪ɑ.rɛ → ˌsɔ.leˈðɑ.rɛ   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɔ.leˈðɑ.rɛ → ˌsɔ.leˈðɑː.rɛ   (ˈɑ→ˈɑː)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌsɔ.leˈðɑː.rɛ → ˌsɔlˈðɑː.rɛ   (e→∅)
500: the low vowel fronts by default
    ˌsɔlˈðɑː.rɛ → ˌsɔlˈðaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsɔlˈðaː.rɛ → ˌsɔlˈðaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsɔlˈðaː.rə → ˌsɔlˈðaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsɔlˈðaːrə̯ → ˌsɔlˈðaːr   (ə̯→∅)
600: ð (plain or palatalized) hardens to d after a lateral
    ˌsɔlˈðaːr → ˌsɔlˈd̪aːr   (ð→d̪)
600: long stressed vowels diphthongize
    ˌsɔlˈd̪aːr → ˌsɔlˈd̪ae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɛ/ɔ raise before a lateral + consonant
    ˌsɔlˈd̪ae̯r → ˌsɯlˈd̪ae̯r   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌsɯlˈd̪ae̯r → ˌsɔlˈd̪ae̯r   (ˌɯ→ˌɔ)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌsɔlˈd̪ae̯r → ˌsɔlˈd̪eːr   (ˈae̯→ˈeː)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌsɔlˈd̪eːr → ˌsɔɫˈd̪eːr   (l→ɫ)
1000: vowel length resets to short
    ˌsɔɫˈd̪eːr → ˌsɔɫˈd̪er   (ˈeː→ˈe)
1000: back dark-l variants vocalize to w
    ˌsɔɫˈd̪er → ˌsɔwˈd̪er   (ɫ→w)
1200: the ow diphthong monophthongizes to u
    ˌsɔwˈd̪er → ˌsuˈd̪er   (ˌɔw→ˌu)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsuˈd̪er → ˌsuˈd̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌsuˈd̪eɹ → ˌsuˈd̪e   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsuˈd̪e → su.d̪e   (ˌu→u, ˈe→e)
```

## sèche

`sˈikkɑm` → `sɛʃ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈsik.kɑm → ˈsɪk.kɑm   (ˈi→ˈɪ)
-100: lax high vowels lower to tense mid vowels
    ˈsɪk.kɑm → ˈsek.kɑm   (ˈɪ→ˈe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈsek.kɑm → ˈsek.kɑ   (m→∅)
500: the low vowel fronts by default
    ˈsek.kɑ → ˈsek.ka   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈsek.ka → ˈsek.kʲa   (k→kʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈsek.kʲa → ˈsek.ca   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈsek.ca → ˈse.kt͡ʃa   (c→t͡ʃ)
600: a stop assimilates place to a following affricate (k/tʃ, g/dʒ)
    ˈse.kt͡ʃa → ˈse.t̪t͡ʃa   (k→t̪)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈse.t̪t͡ʃa → ˈse.t̪t͡ʃə   (a→ə)
750: a dental stop deletes before another coronal stop
    ˈse.t̪t͡ʃə → ˈse.t͡ʃə   (t̪→∅)
1000: stressed e laxes to ɛ before a consonant + vowel
    ˈse.t͡ʃə → ˈsɛ.t͡ʃə   (ˈe→ˈɛ)
1000: all affricates become sibilants (deaffrication)
    ˈsɛ.t͡ʃə → ˈsɛ.ʃə   (t͡ʃ→ʃ)
1400: final ə becomes a non-syllabic off-glide
    ˈsɛ.ʃə → ˈsɛʃə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈsɛʃə̯ → ˈsɛʃ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsɛʃ → sɛʃ   (ˈɛ→ɛ)
```

## sûr

`sˌekˈuːrum` → `syʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌseˈkuː.rum → ˌsɛˈkuː.rʊm   (ˌe→ˌɛ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌsɛˈkuː.rʊm → ˌsɛˈku.rʊm   (ˈuː→ˈu)
-100: lax high vowels lower to tense mid vowels
    ˌsɛˈku.rʊm → ˌsɛˈku.rom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌsɛˈku.rom → ˌsɛˈku.ro   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌsɛˈku.ro → ˌsɛˈkuː.ro   (ˈu→ˈuː)
500: k voices to g intervocalically
    ˌsɛˈkuː.ro → ˌsɛˈguː.ro   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˌsɛˈguː.ro → ˌsɛˈɣuː.ro   (g→ɣ)
500: the velar fricative is lost before a primary-stressed tense round vowel (recurrence)
    ˌsɛˈɣuː.ro → ˌsɛˈuː.ro   (ɣ→∅)
500: a high tense round non-nasal vowel centralizes
    ˌsɛˈuː.ro → ˌsɛˈʉː.ro   (ˈuː→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsɛˈʉː.ro → ˌsɛˈʉː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌsɛˈʉː.rə → ˌsɛˈʉːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsɛˈʉːrə̯ → ˌsɛˈʉːr   (ə̯→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌsɛˈʉːr → ˌseˈʉːr   (ˌɛ→ˌe)
750: vowel length resets to short
    ˌseˈʉːr → ˌseˈʉr   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˌseˈʉr → ˌseˈyr   (ˈʉ→ˈy)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌseˈyr → ˌsəˈyr   (ˌe→ˌə)
1200: a stressless schwa desyllabifies before another vowel
    ˌsəˈyr → ˈsə̯yr   (ˌə→ə̯)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˈsə̯yr → ˈsə̯yːr   (ˈy→ˈyː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈsə̯yːr → ˈsyːr   (ə̯→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsyːr → ˈsyːɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsyːɹ → ˈsyːr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsyːr → ˈsyːʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsyːʀ → syːʀ   (ˈyː→yː)
1400: distinctive vowel length is lost entirely
    syːʀ → syʀ   (yː→y)
1400: the uvular trill ʀ becomes a fricative ʁ
    syʀ → syʁ   (ʀ→ʁ)
```

## sœur

`sˈoror` → `sœʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈso.ror → ˈsɔ.rɔr   (ˈo→ˈɔ, o→ɔ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈsɔ.rɔr → ˈsɔː.rɔr   (ˈɔ→ˈɔː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈsɔː.rɔr → ˈsuo̯.rɔr   (ˈɔː→ˈuo̯)
500: a high tense round non-nasal vowel centralizes
    ˈsuo̯.rɔr → ˈsʉo̯.rɔr   (ˈu→ˈʉ)
500: a stressed vowel lengthens before a voiced labial + r + vowel (recurrence)
    ˈsʉo̯.rɔr → ˈsʉːo̯.rɔr   (ˈʉ→ˈʉː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsʉːo̯.rɔr → ˈsʉːo̯.rər   (ɔ→ə)
600: schwa becomes non-syllabic
    ˈsʉːo̯.rər → ˈsʉːo̯rə̯r   (ə→ə̯)
600: non-syllabic schwa + r/tap metathesizes word-finally
    ˈsʉːo̯rə̯r → ˈsʉːo̯rrə̯   (ə̯→r, r→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsʉːo̯rrə̯ → ˈsʉːo̯rr   (ə̯→∅)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˈsʉːo̯rr → ˈsʉo̯rr   (ˈʉː→ˈʉ)
750: a word-final rr degeminates
    ˈsʉo̯rr → ˈsʉo̯r   (r→∅)
1000: high round back vowels front (completion of u-fronting)
    ˈsʉo̯r → ˈsyo̯r   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈsyo̯r → ˈsye̯r   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈsye̯r → ˈsør   (ˈye̯→ˈø)
1400: e/ø lax before an r that closes the syllable
    ˈsør → ˈsœr   (ˈø→ˈœ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈsœr → ˈsœɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈsœɹ → ˈsœr   (ɹ→r)
1400: r becomes uvular ʀ
    ˈsœr → ˈsœʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈsœʀ → sœʀ   (ˈœ→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    sœʀ → sœʁ   (ʀ→ʁ)
```

## table

`t̪ˈɑbulɑm` → `t̪abl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪ɑ.bu.lɑm → ˈt̪ɑ.bʊ.lɑm   (u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈt̪ɑ.bʊ.lɑm → ˈt̪ɑ.blɑm   (ʊ→∅)
-100: b lenites to β intervocalically / before a sonorant
    ˈt̪ɑ.blɑm → ˈt̪ɑ.βlɑm   (b→β)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɑ.βlɑm → ˈt̪ɑ.βlɑ   (m→∅)
500: the low vowel fronts by default
    ˈt̪ɑ.βlɑ → ˈt̪a.βla   (ˈɑ→ˈa, ɑ→a)
600: the bilabial fricative hardens to b before a lateral
    ˈt̪a.βla → ˈt̪a.bla   (β→b)
600: a stressed vowel lengthens before a plosive + non-nasal sonorant
    ˈt̪a.bla → ˈt̪aː.bla   (ˈa→ˈaː)
600: a non-round vowel shortens before a stop + l
    ˈt̪aː.bla → ˈt̪a.bla   (ˈaː→ˈa)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt̪a.bla → ˈt̪a.blə   (a→ə)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪a.blə → ˈt̪ablə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪ablə̯ → ˈt̪abl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪abl → t̪abl   (ˈa→a)
```

## taon

`t̪ˌɑbˈoːn̪em` → `t̪ɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪ɑˈboː.n̪em → ˌt̪ɑˈboː.n̪ɛm   (e→ɛ)
-100: b lenites to β intervocalically / before a sonorant
    ˌt̪ɑˈboː.n̪ɛm → ˌt̪ɑˈβoː.n̪ɛm   (b→β)
-100: the length feature is dropped now that quality carries the contrast
    ˌt̪ɑˈβoː.n̪ɛm → ˌt̪ɑˈβo.n̪ɛm   (ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌt̪ɑˈβo.n̪ɛm → ˌt̪ɑˈβo.n̪ɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌt̪ɑˈβo.n̪ɛ → ˌt̪ɑˈβoː.n̪ɛ   (ˈo→ˈoː)
500: the bilabial fricative is lost after a (non-initial) low vowel before a labial vowel
    ˌt̪ɑˈβoː.n̪ɛ → ˌt̪ɑˈoː.n̪ɛ   (β→∅)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌt̪ɑˈoː.n̪ɛ → ˌt̪ɑˈũː.n̪ɛ   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˌt̪ɑˈũː.n̪ɛ → ˌt̪aˈũː.n̪ɛ   (ˌɑ→ˌa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪aˈũː.n̪ɛ → ˌt̪aˈũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt̪aˈũː.n̪ə → ˌt̪aˈũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪aˈũːn̪ə̯ → ˌt̪aˈũːn̪   (ə̯→∅)
750: vowel length resets to short
    ˌt̪aˈũːn̪ → ˌt̪aˈũn̪   (ˈũː→ˈũ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪aˈũn̪ → ˌt̪aˈũː   (ˈũn̪→ˈũː)
1200: secondary-stressed a plus a primary-stressed nasalized back vowel becomes a long nasalized a, word-finally
    ˌt̪aˈũː → ˈt̪ãː   (ˌaˈũː→ˈãː)
1400: long a becomes back ɑː
    ˈt̪ãː → ˈt̪ɑ̃ː   (ˈãː→ˈɑ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ɑ̃ː → t̪ɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    t̪ɑ̃ː → t̪ɑ̃   (ɑ̃ː→ɑ̃)
```

## tart

`t̪ˈɑrd̪um` → `t̪aʁ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪ɑr.d̪um → ˈt̪ɑr.d̪ʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪ɑr.d̪ʊm → ˈt̪ɑr.d̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɑr.d̪om → ˈt̪ɑr.d̪o   (m→∅)
500: the low vowel fronts by default
    ˈt̪ɑr.d̪o → ˈt̪ar.d̪o   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ar.d̪o → ˈt̪ar.d̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪ar.d̪ə → ˈt̪ard̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪ard̪ə̯ → ˈt̪ard̪   (ə̯→∅)
750: all final obstruents devoice
    ˈt̪ard̪ → ˈt̪art̪   (d̪→t̪)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈt̪art̪ → ˈt̪aɹt̪   (r→ɹ)
1400: final obstruents are lost
    ˈt̪aɹt̪ → ˈt̪aɹ   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈt̪aɹ → ˈt̪ar   (ɹ→r)
1400: r becomes uvular ʀ
    ˈt̪ar → ˈt̪aʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪aʀ → t̪aʀ   (ˈa→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪aʀ → t̪aʁ   (ʀ→ʁ)
```

## taupe

`t̪ˈɑlpɑm` → `t̪op`

```
-100: l darkens before a non-lateral consonant
    ˈt̪ɑl.pɑm → ˈt̪ɑɫ.pɑm   (l→ɫ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɑɫ.pɑm → ˈt̪ɑɫ.pɑ   (m→∅)
500: the low vowel fronts by default
    ˈt̪ɑɫ.pɑ → ˈt̪aɫ.pa   (ˈɑ→ˈa, ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt̪aɫ.pa → ˈt̪aɫ.pə   (a→ə)
1000: back dark-l variants vocalize to w
    ˈt̪aɫ.pə → ˈt̪aw.pə   (ɫ→w)
1200: aw becomes long oː
    ˈt̪aw.pə → ˈt̪oː.pə   (ˈaw→ˈoː)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪oː.pə → ˈt̪oːpə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪oːpə̯ → ˈt̪oːp   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪oːp → t̪oːp   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    t̪oːp → t̪op   (oː→o)
```

## tel

`t̪ˈɑːlem` → `t̪ɛl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪ɑː.lem → ˈt̪ɑː.lɛm   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˈt̪ɑː.lɛm → ˈt̪ɑ.lɛm   (ˈɑː→ˈɑ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɑ.lɛm → ˈt̪ɑ.lɛ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈt̪ɑ.lɛ → ˈt̪ɑː.lɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈt̪ɑː.lɛ → ˈt̪aː.lɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪aː.lɛ → ˈt̪aː.lə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈt̪aː.lə → ˈt̪aːlə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪aːlə̯ → ˈt̪aːl   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈt̪aːl → ˈt̪ae̯l   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈt̪ae̯l → ˈt̪eːl   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈt̪eːl → ˈt̪el   (ˈeː→ˈe)
1400: e lowers to ɛ before a lateral
    ˈt̪el → ˈt̪ɛl   (ˈe→ˈɛ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ɛl → t̪ɛl   (ˈɛ→ɛ)
```

## temps

`t̪ˈempus` → `t̪ɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪em.pus → ˈt̪ɛm.pʊs   (ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪ɛm.pʊs → ˈt̪ɛm.pos   (ʊ→o)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ɛm.pos → ˈt̪ɛm.pəs   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪ɛm.pəs → ˈt̪ɛmpə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪ɛmpə̯s → ˈt̪ɛmps   (ə̯→∅)
600: a labial consonant becomes s before s
    ˈt̪ɛmps → ˈt̪ɛmss   (p→s)
600: an identical consonant geminate reduces to one, after a consonant or word start
    ˈt̪ɛmss → ˈt̪ɛms   (s→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈt̪ɛms → ˈt̪ɛ̃ms   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈt̪ɛ̃ms → ˈt̪ãms   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈt̪ãms → ˈt̪ãːs   (ˈãm→ˈãː)
1400: long a becomes back ɑː
    ˈt̪ãːs → ˈt̪ɑ̃ːs   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈt̪ɑ̃ːs → ˈt̪ɑ̃ː   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ɑ̃ː → t̪ɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    t̪ɑ̃ː → t̪ɑ̃   (ɑ̃ː→ɑ̃)
```

## tienne

`t̪ˈen̪eɑt̪` → `t̪jɛɲ`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪e.n̪e.ɑt̪ → ˈt̪ɛ.n̪ɛ.ɑt̪   (ˈe→ˈɛ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈt̪ɛ.n̪ɛ.ɑt̪ → ˈt̪ɛ.n̪jɑt̪   (ɛ→j)
-100: yod strengthens before a vowel
    ˈt̪ɛ.n̪jɑt̪ → ˈt̪ɛn̪.ʝɑt̪   (j→ʝ)
300: the coronal nasal palatalizes before yod
    ˈt̪ɛn̪.ʝɑt̪ → ˈt̪ɛ.ɲɑt̪   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈt̪ɛ.ɲɑt̪ → ˈt̪ɛː.ɲɑt̪   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈt̪ɛː.ɲɑt̪ → ˈt̪ie̯.ɲɑt̪   (ˈɛː→ˈie̯)
500: the low vowel fronts by default
    ˈt̪ie̯.ɲɑt̪ → ˈt̪ie̯.ɲat̪   (ɑ→a)
600: t/d spirantize word-finally after a vowel
    ˈt̪ie̯.ɲat̪ → ˈt̪ie̯.ɲaθ   (t̪→θ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt̪ie̯.ɲaθ → ˈt̪ie̯.ɲəθ   (a→ə)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ie̯.ɲəθ → ˈt̪je.ɲəθ   (ˈi→j, e̯→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˈt̪je.ɲəθ → ˈt̪je.ɲə   (θ→∅)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈt̪je.ɲə → ˈt̪jẽ.ɲə   (ˈe→ˈẽ)
1400: nasalized ẽ lowers to ɛ̃
    ˈt̪jẽ.ɲə → ˈt̪jɛ̃.ɲə   (ˈẽ→ˈɛ̃)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈt̪jɛ̃.ɲə → ˈt̪jɛ.ɲə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪jɛ.ɲə → ˈt̪jɛɲə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪jɛɲə̯ → ˈt̪jɛɲ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪jɛɲ → t̪jɛɲ   (ˈɛ→ɛ)
```

## tiennent

`t̪ˈen̪en̪t̪` → `t̪jɛn̪`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪e.n̪en̪t̪ → ˈt̪ɛ.n̪ɛn̪t̪   (ˈe→ˈɛ, e→ɛ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈt̪ɛ.n̪ɛn̪t̪ → ˈt̪ɛː.n̪ɛn̪t̪   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈt̪ɛː.n̪ɛn̪t̪ → ˈt̪ie̯.n̪ɛn̪t̪   (ˈɛː→ˈie̯)
500: unstressed vowel + n becomes a nasalized schwa before word-final t
    ˈt̪ie̯.n̪ɛn̪t̪ → ˈt̪ie̯.n̪ə̃t̪   (ɛn̪→ə̃)
600: t/d spirantize word-finally after a vowel
    ˈt̪ie̯.n̪ə̃t̪ → ˈt̪ie̯.n̪ə̃θ   (t̪→θ)
1000: unstressed nasalized schwa denasalizes
    ˈt̪ie̯.n̪ə̃θ → ˈt̪ie̯.n̪əθ   (ə̃→ə)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ie̯.n̪əθ → ˈt̪je.n̪əθ   (ˈi→j, e̯→ˈe)
1000: the interdental fricatives (plain and palatalized) efface
    ˈt̪je.n̪əθ → ˈt̪je.n̪ə   (θ→∅)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈt̪je.n̪ə → ˈt̪jẽ.n̪ə   (ˈe→ˈẽ)
1400: nasalized ẽ lowers to ɛ̃
    ˈt̪jẽ.n̪ə → ˈt̪jɛ̃.n̪ə   (ˈẽ→ˈɛ̃)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˈt̪jɛ̃.n̪ə → ˈt̪jɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈt̪jɛ.n̪ə → ˈt̪jɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈt̪jɛn̪ə̯ → ˈt̪jɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪jɛn̪ → t̪jɛn̪   (ˈɛ→ɛ)
```

## tiens

`t̪ˈen̪eo` → `t̪jɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪e.n̪e.o → ˈt̪ɛ.n̪ɛ.ɔ   (ˈe→ˈɛ, e→ɛ, o→ɔ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈt̪ɛ.n̪ɛ.ɔ → ˈt̪ɛ.n̪jɔ   (ɛ→j)
-100: yod strengthens before a vowel
    ˈt̪ɛ.n̪jɔ → ˈt̪ɛn̪.ʝɔ   (j→ʝ)
300: the coronal nasal palatalizes before yod
    ˈt̪ɛn̪.ʝɔ → ˈt̪ɛ.ɲɔ   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈt̪ɛ.ɲɔ → ˈt̪ɛː.ɲɔ   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈt̪ɛː.ɲɔ → ˈt̪ie̯.ɲɔ   (ˈɛː→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ie̯.ɲɔ → ˈt̪ie̯.ɲə   (ɔ→ə)
600: schwa becomes non-syllabic
    ˈt̪ie̯.ɲə → ˈt̪ie̯ɲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪ie̯ɲə̯ → ˈt̪ie̯ɲ   (ə̯→∅)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ie̯ɲ → ˈt̪jeɲ   (ˈi→j, e̯→ˈe)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈt̪jeɲ → ˈt̪jẽɲ   (ˈe→ˈẽ)
1200: final ɲ becomes n
    ˈt̪jẽɲ → ˈt̪jẽn̪   (ɲ→n̪)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈt̪jẽn̪ → ˈt̪jẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈt̪jẽː → ˈt̪jɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪jɛ̃ː → t̪jɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    t̪jɛ̃ː → t̪jɛ̃   (ɛ̃ː→ɛ̃)
```

## tient

`t̪ˈen̪et̪` → `t̪jɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪e.n̪et̪ → ˈt̪ɛ.n̪ɛt̪   (ˈe→ˈɛ, e→ɛ)
300: a stressed vowel lengthens before a single consonant + glide
    ˈt̪ɛ.n̪ɛt̪ → ˈt̪ɛː.n̪ɛt̪   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈt̪ɛː.n̪ɛt̪ → ˈt̪ie̯.n̪ɛt̪   (ˈɛː→ˈie̯)
600: t/d spirantize word-finally after a vowel
    ˈt̪ie̯.n̪ɛt̪ → ˈt̪ie̯.n̪ɛθ   (t̪→θ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ie̯.n̪ɛθ → ˈt̪ie̯.n̪əθ   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈt̪ie̯.n̪əθ → ˈt̪ie̯n̪ə̯θ   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪ie̯n̪ə̯θ → ˈt̪ie̯n̪θ   (ə̯→∅)
600: a dental fricative hardens to a stop after a consonant, word-finally
    ˈt̪ie̯n̪θ → ˈt̪ie̯n̪t̪   (θ→t̪)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈt̪ie̯n̪t̪ → ˈt̪jen̪t̪   (ˈi→j, e̯→ˈe)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˈt̪jen̪t̪ → ˈt̪jẽn̪t̪   (ˈe→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈt̪jẽn̪t̪ → ˈt̪jẽːt̪   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˈt̪jẽːt̪ → ˈt̪jɛ̃ːt̪   (ˈẽː→ˈɛ̃ː)
1400: final obstruents are lost
    ˈt̪jɛ̃ːt̪ → ˈt̪jɛ̃ː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪jɛ̃ː → t̪jɛ̃ː   (ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    t̪jɛ̃ː → t̪jɛ̃   (ɛ̃ː→ɛ̃)
```

## tison

`t̪ˌiːt̪iˈoːn̪em` → `t̪i.zɔ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪iː.t̪iˈoː.n̪em → ˌt̪iː.t̪ɪˈoː.n̪ɛm   (i→ɪ, e→ɛ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌt̪iː.t̪ɪˈoː.n̪ɛm → ˌt̪iːˈt̪joː.n̪ɛm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌt̪iːˈt̪joː.n̪ɛm → ˌt̪iːˈt̪ʝoː.n̪ɛm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌt̪iːˈt̪ʝoː.n̪ɛm → ˌt̪iˈt̪ʝo.n̪ɛm   (ˌiː→ˌi, ˈoː→ˈo)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌt̪iˈt̪ʝo.n̪ɛm → ˌt̪iˈt̪ʝo.n̪ɛ   (m→∅)
-100: t/d palatalize before yod (t → tsʲ, d → ɟ)
    ˌt̪iˈt̪ʝo.n̪ɛ → ˌt̪it͡sʲˈʝo.n̪ɛ   (t̪→t͡sʲ)
300: yod absorbed into a preceding palatalized consonant
    ˌt̪it͡sʲˈʝo.n̪ɛ → ˌt̪iˈt͡sʲo.n̪ɛ   (ʝ→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌt̪iˈt͡sʲo.n̪ɛ → ˌt̪iˈt͡sʲoː.n̪ɛ   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌt̪iˈt͡sʲoː.n̪ɛ → ˌt̪iˈt͡sʲũː.n̪ɛ   (ˈoː→ˈũː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪iˈt͡sʲũː.n̪ɛ → ˌt̪iˈt͡sʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt̪iˈt͡sʲũː.n̪ə → ˌt̪iˈt͡sʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪iˈt͡sʲũːn̪ə̯ → ˌt̪iˈt͡sʲũːn̪   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˌt̪iˈt͡sʲũːn̪ → ˌt̪iˈd͡zʲũːn̪   (t͡sʲ→d͡zʲ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌt̪iˈd͡zʲũːn̪ → ˌt̪iˈzʲũːn̪   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌt̪iˈzʲũːn̪ → ˌt̪ijˈzũːn̪   (zʲ→jz)
750: vowel length resets to short
    ˌt̪ijˈzũːn̪ → ˌt̪ijˈzũn̪   (ˈũː→ˈũ)
750: j deletes after a high front tense vowel
    ˌt̪ijˈzũn̪ → ˌt̪iˈzũn̪   (j→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪iˈzũn̪ → ˌt̪iˈzũː   (ˈũn̪→ˈũː)
1400: a vowel lengthens before an intervocalic z
    ˌt̪iˈzũː → ˌt̪iːˈzũː   (ˌi→ˌiː)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪iːˈzũː → t̪iː.zũː   (ˌiː→iː, ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    t̪iː.zũː → t̪i.zũ   (iː→i, ũː→ũ)
1400: nasal ũ opens to ɔ̃
    t̪i.zũ → t̪i.zɔ̃   (ũ→ɔ̃)
```

## toi

`t̪ˈeːkt̪um` → `t̪wa`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪eːk.t̪um → ˈt̪eːk.t̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈt̪eːk.t̪ʊm → ˈt̪ek.t̪ʊm   (ˈeː→ˈe)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˈt̪ek.t̪ʊm → ˈt̪ex.t̪ʊm   (k→x)
-100: lax high vowels lower to tense mid vowels
    ˈt̪ex.t̪ʊm → ˈt̪ex.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ex.t̪om → ˈt̪ex.t̪o   (m→∅)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈt̪ex.t̪o → ˈt̪eç.t̪o   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈt̪eç.t̪o → ˈt̪eç.t̪ʲo   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪eç.t̪ʲo → ˈt̪eç.t̪ʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪eç.t̪ʲə → ˈt̪eçt̪ʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪eçt̪ʲə̯ → ˈt̪eçt̪ʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈt̪eçt̪ʲ → ˈt̪eçjt̪   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈt̪eçjt̪ → ˈt̪eçt̪   (j→∅)
750: ç merges into ʝ
    ˈt̪eçt̪ → ˈt̪eʝt̪   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈt̪eʝt̪ → ˈt̪ejt̪   (ʝ→j)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈt̪ejt̪ → ˈt̪ojt̪   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈt̪ojt̪ → ˈt̪ujt̪   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈt̪ujt̪ → ˈt̪uɛ̯t̪   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈt̪uɛ̯t̪ → ˈt̪wɛt̪   (ˈu→w, ɛ̯→ˈɛ)
1400: final obstruents are lost
    ˈt̪wɛt̪ → ˈt̪wɛ   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪wɛ → t̪wɛ   (ˈɛ→ɛ)
1400: wɛ becomes wa
    t̪wɛ → t̪wa   (ɛ→a)
```

## tourment

`t̪ˌormˈen̪t̪um` → `t̪u.ʁmɑ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪orˈmen̪.t̪um → ˌt̪ɔrˈmɛn̪.t̪ʊm   (ˌo→ˌɔ, ˈe→ˈɛ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˌt̪ɔrˈmɛn̪.t̪ʊm → ˌt̪ɔrˈmɛn̪.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌt̪ɔrˈmɛn̪.t̪om → ˌt̪ɔrˈmɛn̪.t̪o   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪ɔrˈmɛn̪.t̪o → ˌt̪ɔrˈmɛn̪.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌt̪ɔrˈmɛn̪.t̪ə → ˌt̪ɔrˈmɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪ɔrˈmɛn̪t̪ə̯ → ˌt̪ɔrˈmɛn̪t̪   (ə̯→∅)
600: secondary-stressed ɔ raises to o unconditionally
    ˌt̪ɔrˈmɛn̪t̪ → ˌt̪orˈmɛn̪t̪   (ˌɔ→ˌo)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌt̪orˈmɛn̪t̪ → ˌt̪orˈmɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌt̪orˈmɛ̃n̪t̪ → ˌt̪urˈmɛ̃n̪t̪   (ˌo→ˌu)
1000: nasalized front mid vowels become nasalized a
    ˌt̪urˈmɛ̃n̪t̪ → ˌt̪urˈmãn̪t̪   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪urˈmãn̪t̪ → ˌt̪urˈmãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˌt̪urˈmãːt̪ → ˌt̪urˈmɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌt̪urˈmɑ̃ːt̪ → ˌt̪uɹˈmɑ̃ːt̪   (r→ɹ)
1400: final obstruents are lost
    ˌt̪uɹˈmɑ̃ːt̪ → ˌt̪uɹˈmɑ̃ː   (t̪→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌt̪uɹˈmɑ̃ː → ˌt̪urˈmɑ̃ː   (ɹ→r)
1400: r becomes uvular ʀ
    ˌt̪urˈmɑ̃ː → ˌt̪uʀˈmɑ̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪uʀˈmɑ̃ː → t̪uʀ.mɑ̃ː   (ˌu→u, ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    t̪uʀ.mɑ̃ː → t̪uʀ.mɑ̃   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪uʀ.mɑ̃ → t̪u.ʁmɑ̃   (ʀ→ʁ)
```

## tout

`t̪ˈoːt̪t̪um` → `t̪o`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪oːt̪.t̪um → ˈt̪oːt̪.t̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˈt̪oːt̪.t̪ʊm → ˈt̪ot̪.t̪ʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ˈt̪ot̪.t̪ʊm → ˈt̪ot̪.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ot̪.t̪om → ˈt̪ot̪.t̪o   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ot̪.t̪o → ˈt̪ot̪.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪ot̪.t̪ə → ˈt̪ot̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪ot̪t̪ə̯ → ˈt̪ot̪t̪   (ə̯→∅)
750: a dental stop deletes before another coronal stop
    ˈt̪ot̪t̪ → ˈt̪ot̪   (t̪→∅)
1000: primary-stressed o opens to ɔ before a pre-coda stop, word-finally
    ˈt̪ot̪ → ˈt̪ɔt̪   (ˈo→ˈɔ)
1400: final obstruents are lost
    ˈt̪ɔt̪ → ˈt̪ɔ   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ɔ → t̪ɔ   (ˈɔ→ɔ)
1400: word-final ɔ raises to o
    t̪ɔ → t̪o   (ɔ→o)
```

## traiter

`t̪rˌɑkt̪ˈɑːre` → `t̪ʁɛ.t̪e`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪rɑkˈt̪ɑː.re → ˌt̪rɑkˈt̪ɑː.rɛ   (e→ɛ)
-100: the length feature is dropped now that quality carries the contrast
    ˌt̪rɑkˈt̪ɑː.rɛ → ˌt̪rɑkˈt̪ɑ.rɛ   (ˈɑː→ˈɑ)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˌt̪rɑkˈt̪ɑ.rɛ → ˌt̪rɑxˈt̪ɑ.rɛ   (k→x)
300: a stressed vowel lengthens before a single consonant + glide
    ˌt̪rɑxˈt̪ɑ.rɛ → ˌt̪rɑxˈt̪ɑː.rɛ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌt̪rɑxˈt̪ɑː.rɛ → ˌt̪raxˈt̪aː.rɛ   (ˌɑ→ˌa, ˈɑː→ˈaː)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌt̪raxˈt̪aː.rɛ → ˌt̪raçˈt̪aː.rɛ   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌt̪raçˈt̪aː.rɛ → ˌt̪raçˈt̪ʲaː.rɛ   (t̪→t̪ʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪raçˈt̪ʲaː.rɛ → ˌt̪raçˈt̪ʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌt̪raçˈt̪ʲaː.rə → ˌt̪raçˈt̪ʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪raçˈt̪ʲaːrə̯ → ˌt̪raçˈt̪ʲaːr   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌt̪raçˈt̪ʲaːr → ˌt̪raçjˈt̪aːr   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌt̪raçjˈt̪aːr → ˌt̪raçˈt̪aːr   (j→∅)
600: long stressed vowels diphthongize
    ˌt̪raçˈt̪aːr → ˌt̪raçˈt̪ae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌt̪raçˈt̪ae̯r → ˌt̪raçˈt̪eːr   (ˈae̯→ˈeː)
750: ç merges into ʝ
    ˌt̪raçˈt̪eːr → ˌt̪raʝˈt̪eːr   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌt̪raʝˈt̪eːr → ˌt̪rajˈt̪eːr   (ʝ→j)
1000: vowel length resets to short
    ˌt̪rajˈt̪eːr → ˌt̪rajˈt̪er   (ˈeː→ˈe)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌt̪rajˈt̪er → ˌt̪rɛːˈt̪er   (ˌaj→ˌɛː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌt̪rɛːˈt̪er → ˌt̪rɛːˈt̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌt̪rɛːˈt̪eɹ → ˌt̪rɛːˈt̪e   (ɹ→∅)
1400: r becomes uvular ʀ
    ˌt̪rɛːˈt̪e → ˌt̪ʀɛːˈt̪e   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪ʀɛːˈt̪e → t̪ʀɛː.t̪e   (ˌɛː→ɛː, ˈe→e)
1400: distinctive vowel length is lost entirely
    t̪ʀɛː.t̪e → t̪ʀɛ.t̪e   (ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪ʀɛ.t̪e → t̪ʁɛ.t̪e   (ʀ→ʁ)
```

## tu

`t̪ˈuː` → `t̪y`

```
-100: the length feature is dropped now that quality carries the contrast
    ˈt̪uː → ˈt̪u   (ˈuː→ˈu)
300: a stressed vowel lengthens word-finally
    ˈt̪u → ˈt̪uː   (ˈu→ˈuː)
500: a high tense round non-nasal vowel centralizes
    ˈt̪uː → ˈt̪ʉː   (ˈuː→ˈʉː)
750: vowel length resets to short
    ˈt̪ʉː → ˈt̪ʉ   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈt̪ʉ → ˈt̪y   (ˈʉ→ˈy)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪y → t̪y   (ˈy→y)
```

## témoin

`t̪ˌest̪imˈoːn̪ium` → `t̪ɛ.mwɛ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌt̪es.t̪iˈmoː.n̪i.um → ˌt̪ɛs.t̪ɪˈmoː.n̪ɪ.ʊm   (ˌe→ˌɛ, i→ɪ, i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˌt̪ɛs.t̪ɪˈmoː.n̪ɪ.ʊm → ˌt̪ɛs.t̪ɪˈmoː.n̪jʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˌt̪ɛs.t̪ɪˈmoː.n̪jʊm → ˌt̪ɛs.t̪ɪˈmoːn̪.ʝʊm   (j→ʝ)
-100: the length feature is dropped now that quality carries the contrast
    ˌt̪ɛs.t̪ɪˈmoːn̪.ʝʊm → ˌt̪ɛs.t̪ɪˈmon̪.ʝʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ˌt̪ɛs.t̪ɪˈmon̪.ʝʊm → ˌt̪ɛs.t̪eˈmon̪.ʝom   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌt̪ɛs.t̪eˈmon̪.ʝom → ˌt̪ɛs.t̪eˈmon̪.ʝo   (m→∅)
300: the coronal nasal palatalizes before yod
    ˌt̪ɛs.t̪eˈmon̪.ʝo → ˌt̪ɛs.t̪eˈmo.ɲo   (n̪ʝ→ɲ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌt̪ɛs.t̪eˈmo.ɲo → ˌt̪ɛs.t̪eˈmoː.ɲo   (ˈo→ˈoː)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌt̪ɛs.t̪eˈmoː.ɲo → ˌt̪ɛs.t̪eˈmũː.ɲo   (ˈoː→ˈũː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt̪ɛs.t̪eˈmũː.ɲo → ˌt̪ɛs.t̪əˈmũː.ɲə   (e→ə, o→ə)
600: schwa becomes non-syllabic
    ˌt̪ɛs.t̪əˈmũː.ɲə → ˌt̪ɛst̪ə̯ˈmũːɲə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt̪ɛst̪ə̯ˈmũːɲə̯ → ˌt̪ɛsˈt̪mũːɲ   (ˈə̯mũːɲə̯→ˈmũːɲ)
600: t voices to d before a nasal consonant
    ˌt̪ɛsˈt̪mũːɲ → ˌt̪ɛsˈd̪mũːɲ   (t̪→d̪)
600: a vowel shortens before ɲ
    ˌt̪ɛsˈd̪mũːɲ → ˌt̪ɛsˈd̪mũɲ   (ˈũː→ˈũ)
600: secondary-stressed ɛ raises to ɨ before a coronal non-nasal continuant + non-nasal consonant
    ˌt̪ɛsˈd̪mũɲ → ˌt̪ɨsˈd̪mũɲ   (ˌɛ→ˌɨ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌt̪ɨsˈd̪mũɲ → ˌt̪ɛsˈd̪mũɲ   (ˌɨ→ˌɛ)
750: a medial consonant/glide is lost between two consonants, before a nasal
    ˌt̪ɛsˈd̪mũɲ → ˌt̪ɛˈsmũɲ   (d̪→∅)
750: s voices to z after a vowel, before a voiced consonant
    ˌt̪ɛˈsmũɲ → ˌt̪ɛˈzmũɲ   (s→z)
1000: word-final ɲ ejects a nasalized j after a tense vowel
    ˌt̪ɛˈzmũɲ → ˌt̪ɛˈzmũj̃ɲ   (∅→j̃)
1000: the nasal diphthong ũj̃ becomes wĩ (syllabicity swap before a nasal)
    ˌt̪ɛˈzmũj̃ɲ → ˌt̪ɛ.zmwj̩̃ɲ   (ˈũ→w, j̃→j̩̃)
1000: z is lost before a consonant (preconsonantal effacement)
    ˌt̪ɛ.zmwj̩̃ɲ → ˌt̪ɛ.mwj̩̃ɲ   (z→∅)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˌt̪ɛ.mwj̩̃ɲ → ˌt̪ɛ̃.mwj̩̃ɲ   (ˌɛ→ˌɛ̃)
1200: final ɲ becomes n
    ˌt̪ɛ̃.mwj̩̃ɲ → ˌt̪ɛ̃.mwj̩̃n̪   (ɲ→n̪)
1200: nasalized ĩ lowers after w
    ˌt̪ɛ̃.mwj̩̃n̪ → ˌt̪ɛ̃.mwj̩̃n̪   (j̩̃→j̩̃)
1200: a front unrounded non-low vowel laxes and lowers after w
    ˌt̪ɛ̃.mwj̩̃n̪ → ˌt̪ɛ̃.mwɛ̃n̪   (j̩̃→ɛ̃)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪ɛ̃.mwɛ̃n̪ → ˌt̪ɛ̃.mwɛ̃ː   (ɛ̃n̪→ɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪ɛ̃.mwɛ̃ː → t̪ɛ̃.mwɛ̃ː   (ˌɛ̃→ɛ̃)
1400: distinctive vowel length is lost entirely
    t̪ɛ̃.mwɛ̃ː → t̪ɛ̃.mwɛ̃   (ɛ̃ː→ɛ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    t̪ɛ̃.mwɛ̃ → t̪ɛ.mwɛ̃   (ɛ̃→ɛ)
```

## tôt

`t̪ˈost̪um` → `t̪o`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪os.t̪um → ˈt̪ɔs.t̪ʊm   (ˈo→ˈɔ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪ɔs.t̪ʊm → ˈt̪ɔs.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪ɔs.t̪om → ˈt̪ɔs.t̪o   (m→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ɔs.t̪o → ˈt̪ɔs.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪ɔs.t̪ə → ˈt̪ɔst̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪ɔst̪ə̯ → ˈt̪ɔst̪   (ə̯→∅)
1000: s becomes x after a vowel, before any consonant
    ˈt̪ɔst̪ → ˈt̪ɔxt̪   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˈt̪ɔxt̪ → ˈt̪ɔːt̪   (ˈɔx→ˈɔː)
1200: a long back mid o tenses to oː
    ˈt̪ɔːt̪ → ˈt̪oːt̪   (ˈɔː→ˈoː)
1400: final obstruents are lost
    ˈt̪oːt̪ → ˈt̪oː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪oː → t̪oː   (ˈoː→oː)
1400: distinctive vowel length is lost entirely
    t̪oː → t̪o   (oː→o)
```

## un

`ˌuːn̪um` → `œ̃`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌuː.n̪um → ˌuː.n̪ʊm   (u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌuː.n̪ʊm → ˌu.n̪ʊm   (ˌuː→ˌu)
-100: lax high vowels lower to tense mid vowels
    ˌu.n̪ʊm → ˌu.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌu.n̪om → ˌu.n̪o   (m→∅)
500: a high tense round non-nasal vowel centralizes
    ˌu.n̪o → ˌʉ.n̪o   (ˌu→ˌʉ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌʉ.n̪o → ˌʉ.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌʉ.n̪ə → ˌʉn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌʉn̪ə̯ → ˌʉn̪   (ə̯→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌʉn̪ → ˌyn̪   (ˌʉ→ˌy)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌyn̪ → ˌỹn̪   (ˌy→ˌỹ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌỹn̪ → ˌỹː   (ˌỹn̪→ˌỹː)
1400: nasalized front vowels lower (wẽ, jẽ, ø̃ open to wɛ̃, jɛ̃, œ̃)
    ˌỹː → ˌœ̃ː   (ˌỹː→ˌœ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌœ̃ː → œ̃ː   (ˌœ̃ː→œ̃ː)
1400: distinctive vowel length is lost entirely
    œ̃ː → œ̃   (œ̃ː→œ̃)
```

## une

`ˌuːn̪ɑm` → `yn̪`

```
-100: the length feature is dropped now that quality carries the contrast
    ˌuː.n̪ɑm → ˌu.n̪ɑm   (ˌuː→ˌu)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌu.n̪ɑm → ˌu.n̪ɑ   (m→∅)
500: the low vowel fronts by default
    ˌu.n̪ɑ → ˌu.n̪a   (ɑ→a)
500: a high tense round non-nasal vowel centralizes
    ˌu.n̪a → ˌʉ.n̪a   (ˌu→ˌʉ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌʉ.n̪a → ˌʉ.n̪ə   (a→ə)
1000: high round back vowels front (completion of u-fronting)
    ˌʉ.n̪ə → ˌy.n̪ə   (ˌʉ→ˌy)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌy.n̪ə → ˌỹ.n̪ə   (ˌy→ˌỹ)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌỹ.n̪ə → ˌy.n̪ə   (ˌỹ→ˌy)
1400: final ə becomes a non-syllabic off-glide
    ˌy.n̪ə → ˌyn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌyn̪ə̯ → ˌyn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌyn̪ → yn̪   (ˌy→y)
```

## vair

`wˈɑrium` → `vɛʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwɑ.ri.um → ˈɣʷɑ.ri.um   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷɑ.ri.um → ˈɣʷɑ.rɪ.ʊm   (i→ɪ, u→ʊ)
-100: unstressed short non-low vowels glide before another vowel (yod/w formation)
    ˈɣʷɑ.rɪ.ʊm → ˈɣʷɑ.rjʊm   (ɪ→j)
-100: yod strengthens before a vowel
    ˈɣʷɑ.rjʊm → ˈɣʷɑr.ʝʊm   (j→ʝ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɑr.ʝʊm → ˈβʷɑr.ʝʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɑr.ʝʊm → ˈβʷɑr.ʝom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷɑr.ʝom → ˈβʷɑr.ʝo   (m→∅)
500: labialized bilabial fricatives delabialize
    ˈβʷɑr.ʝo → ˈβɑr.ʝo   (βʷ→β)
500: r + yod becomes palatalized r
    ˈβɑr.ʝo → ˈβɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˈβɑ.rʲo → ˈβa.rʲo   (ˈɑ→ˈa)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˈβa.rʲo → ˈβaː.rʲo   (ˈa→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβaː.rʲo → ˈβaː.rʲə   (o→ə)
600: schwa becomes non-syllabic
    ˈβaː.rʲə → ˈβaːrʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈβaːrʲə̯ → ˈβaːrʲ   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˈβaːrʲ → ˈβaːjrʲ   (∅→j)
600: palatalized r depalatalizes
    ˈβaːjrʲ → ˈβaːjr   (rʲ→r)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˈβaːjr → ˈβajr   (ˈaː→ˈa)
600: the remaining bilabial fricative becomes v
    ˈβajr → ˈvajr   (β→v)
750: schwa is epenthesized word-finally after a low vowel + j + r
    ˈvajr → ˈvaj.rə   (∅→ə)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈvaj.rə → ˈvɛː.rə   (ˈaj→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˈvɛː.rə → ˈvɛːrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈvɛːrə̯ → ˈvɛːr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈvɛːr → ˈvɛːʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈvɛːʀ → vɛːʀ   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    vɛːʀ → vɛʀ   (ɛː→ɛ)
1400: the uvular trill ʀ becomes a fricative ʁ
    vɛʀ → vɛʁ   (ʀ→ʁ)
```

## veiller

`wˌigilˈɑːre` → `ve.je`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌwi.giˈlɑː.re → ˌɣʷi.giˈlɑː.re   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɣʷi.giˈlɑː.re → ˌɣʷɪ.gɪˈlɑː.rɛ   (ˌi→ˌɪ, i→ɪ, e→ɛ)
-100: ɪ lost after a non-low vowel + velar stop, before l
    ˌɣʷɪ.gɪˈlɑː.rɛ → ˌɣʷɪˈglɑː.rɛ   (ɪ→∅)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɣʷɪˈglɑː.rɛ → ˌβʷɪˈglɑː.rɛ   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌβʷɪˈglɑː.rɛ → ˌβʷɪˈglɑ.rɛ   (ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌβʷɪˈglɑ.rɛ → ˌβʷeˈglɑ.rɛ   (ˌɪ→ˌe)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌβʷeˈglɑ.rɛ → ˌβʷeˈɣlɑ.rɛ   (g→ɣ)
300: a stressed vowel lengthens before a single consonant + glide
    ˌβʷeˈɣlɑ.rɛ → ˌβʷeˈɣlɑː.rɛ   (ˈɑ→ˈɑː)
500: labialized bilabial fricatives delabialize
    ˌβʷeˈɣlɑː.rɛ → ˌβeˈɣlɑː.rɛ   (βʷ→β)
500: the low vowel fronts by default
    ˌβeˈɣlɑː.rɛ → ˌβeˈɣlaː.rɛ   (ˈɑː→ˈaː)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌβeˈɣlaː.rɛ → ˌβeˈʝlaː.rɛ   (ɣ→ʝ)
500: a lateral palatalizes after a high-front consonant
    ˌβeˈʝlaː.rɛ → ˌβeˈʝʎaː.rɛ   (l→ʎ)
600: yod lost before ʎ or palatalized r
    ˌβeˈʝʎaː.rɛ → ˌβeˈʎaː.rɛ   (ʝ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌβeˈʎaː.rɛ → ˌβeˈʎaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌβeˈʎaː.rə → ˌβeˈʎaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌβeˈʎaːrə̯ → ˌβeˈʎaːr   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌβeˈʎaːr → ˌβeˈʎɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌβeˈʎɛːr → ˌβeˈʎie̯r   (ˈɛː→ˈie̯)
600: the remaining bilabial fricative becomes v
    ˌβeˈʎie̯r → ˌveˈʎie̯r   (β→v)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌveˈʎie̯r → ˌvəˈʎie̯r   (ˌe→ˌə)
1000: secondary-stressed schwa reverts to e before a palatal consonant
    ˌvəˈʎie̯r → ˌveˈʎie̯r   (ˌə→ˌe)
1000: a glide develops between a stressed mid front unrounded vowel and intervocalic ʎ
    ˌveˈʎie̯r → ˌvejˈʎie̯r   (∅→j)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌvejˈʎie̯r → ˌvejˈʎjer   (ˈi→j, e̯→ˈe)
1200: je becomes e after a palatal consonant
    ˌvejˈʎjer → ˌvejˈʎer   (j→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌvejˈʎer → ˌvejˈʎeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌvejˈʎeɹ → ˌvejˈʎe   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌvejˈʎe → vej.ʎe   (ˌe→e, ˈe→e)
1400: ʎ becomes j
    vej.ʎe → vej.je   (ʎ→j)
1400: a high front vowel after another vowel is absorbed into a following j
    vej.je → ve.je   (j→∅)
```

## vent

`wˈen̪t̪um` → `vɑ̃`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwen̪.t̪um → ˈɣʷen̪.t̪um   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷen̪.t̪um → ˈɣʷɛn̪.t̪ʊm   (ˈe→ˈɛ, u→ʊ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɛn̪.t̪ʊm → ˈβʷɛn̪.t̪ʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɛn̪.t̪ʊm → ˈβʷɛn̪.t̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷɛn̪.t̪om → ˈβʷɛn̪.t̪o   (m→∅)
500: labialized bilabial fricatives delabialize
    ˈβʷɛn̪.t̪o → ˈβɛn̪.t̪o   (βʷ→β)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβɛn̪.t̪o → ˈβɛn̪.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈβɛn̪.t̪ə → ˈβɛn̪t̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈβɛn̪t̪ə̯ → ˈβɛn̪t̪   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˈβɛn̪t̪ → ˈvɛn̪t̪   (β→v)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈvɛn̪t̪ → ˈvɛ̃n̪t̪   (ˈɛ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈvɛ̃n̪t̪ → ˈvãn̪t̪   (ˈɛ̃→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈvãn̪t̪ → ˈvãːt̪   (ˈãn̪→ˈãː)
1400: long a becomes back ɑː
    ˈvãːt̪ → ˈvɑ̃ːt̪   (ˈãː→ˈɑ̃ː)
1400: final obstruents are lost
    ˈvɑ̃ːt̪ → ˈvɑ̃ː   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈvɑ̃ː → vɑ̃ː   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    vɑ̃ː → vɑ̃   (ɑ̃ː→ɑ̃)
```

## vie

`wˈiːt̪ɑm` → `vi`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwiː.t̪ɑm → ˈɣʷiː.t̪ɑm   (w→ɣʷ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷiː.t̪ɑm → ˈβʷiː.t̪ɑm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˈβʷiː.t̪ɑm → ˈβʷi.t̪ɑm   (ˈiː→ˈi)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷi.t̪ɑm → ˈβʷi.t̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈβʷi.t̪ɑ → ˈβʷiː.t̪ɑ   (ˈi→ˈiː)
500: labialized bilabial fricatives delabialize
    ˈβʷiː.t̪ɑ → ˈβiː.t̪ɑ   (βʷ→β)
500: the low vowel fronts by default
    ˈβiː.t̪ɑ → ˈβiː.t̪a   (ɑ→a)
600: a voiceless consonant voices intervocalically
    ˈβiː.t̪a → ˈβiː.d̪a   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈβiː.d̪a → ˈβiː.ða   (d̪→ð)
600: the remaining bilabial fricative becomes v
    ˈβiː.ða → ˈviː.ða   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈviː.ða → ˈviː.ðə   (a→ə)
750: vowel length resets to short
    ˈviː.ðə → ˈvi.ðə   (ˈiː→ˈi)
1000: the interdental fricatives (plain and palatalized) efface
    ˈvi.ðə → ˈvi.ə   (ð→∅)
1200: schwa desyllabifies after another vowel
    ˈvi.ə → ˈviə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈviə̯ → ˈviː   (ˈiə̯→ˈiː)
1400: stress is leveled — no longer distinctive for vowels
    ˈviː → viː   (ˈiː→iː)
1400: distinctive vowel length is lost entirely
    viː → vi   (iː→i)
```

## vieil

`wˈet̪ulum` → `vjɛj`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwe.t̪u.lum → ˈɣʷe.t̪u.lum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷe.t̪u.lum → ˈɣʷɛ.t̪ʊ.lʊm   (ˈe→ˈɛ, u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈɣʷɛ.t̪ʊ.lʊm → ˈɣʷɛ.t̪lʊm   (ʊ→∅)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɛ.t̪lʊm → ˈβʷɛ.t̪lʊm   (ɣʷ→βʷ)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɛ.t̪lʊm → ˈβʷɛ.t̪lom   (ʊ→o)
-100: t becomes k before a lateral
    ˈβʷɛ.t̪lom → ˈβʷɛ.klom   (t̪→k)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷɛ.klom → ˈβʷɛ.klo   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈβʷɛ.klo → ˈβʷɛː.klo   (ˈɛ→ˈɛː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˈβʷɛː.klo → ˈβʷɛː.xlo   (k→x)
500: a vowel shortens before a consonant cluster
    ˈβʷɛː.xlo → ˈβʷɛ.xlo   (ˈɛː→ˈɛ)
500: labialized bilabial fricatives delabialize
    ˈβʷɛ.xlo → ˈβɛ.xlo   (βʷ→β)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈβɛ.xlo → ˈβɛ.çlo   (x→ç)
500: a lateral palatalizes after a high-front consonant
    ˈβɛ.çlo → ˈβɛ.çʎo   (l→ʎ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈβɛ.çʎo → ˈβie̯.çʎo   (ˈɛ→ˈie̯)
600: yod lost before ʎ or palatalized r
    ˈβie̯.çʎo → ˈβie̯.ʎo   (ç→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβie̯.ʎo → ˈβie̯.ʎə   (o→ə)
600: schwa becomes non-syllabic
    ˈβie̯.ʎə → ˈβie̯ʎə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈβie̯ʎə̯ → ˈβie̯ʎ   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˈβie̯ʎ → ˈvie̯ʎ   (β→v)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈvie̯ʎ → ˈvjeʎ   (ˈi→j, e̯→ˈe)
1400: e lowers to ɛ before a lateral
    ˈvjeʎ → ˈvjɛʎ   (ˈe→ˈɛ)
1400: stress is leveled — no longer distinctive for vowels
    ˈvjɛʎ → vjɛʎ   (ˈɛ→ɛ)
1400: ʎ becomes j
    vjɛʎ → vjɛj   (ʎ→j)
```

## vilain

`wˌiːllˈɑːn̪um` → `vi.lɛ̃`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌwiːlˈlɑː.n̪um → ˌɣʷiːlˈlɑː.n̪um   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɣʷiːlˈlɑː.n̪um → ˌɣʷiːlˈlɑː.n̪ʊm   (u→ʊ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɣʷiːlˈlɑː.n̪ʊm → ˌβʷiːlˈlɑː.n̪ʊm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌβʷiːlˈlɑː.n̪ʊm → ˌβʷilˈlɑ.n̪ʊm   (ˌiː→ˌi, ˈɑː→ˈɑ)
-100: lax high vowels lower to tense mid vowels
    ˌβʷilˈlɑ.n̪ʊm → ˌβʷilˈlɑ.n̪om   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌβʷilˈlɑ.n̪om → ˌβʷilˈlɑ.n̪o   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌβʷilˈlɑ.n̪o → ˌβʷilˈlɑː.n̪o   (ˈɑ→ˈɑː)
500: labialized bilabial fricatives delabialize
    ˌβʷilˈlɑː.n̪o → ˌβilˈlɑː.n̪o   (βʷ→β)
500: the low vowel fronts by default
    ˌβilˈlɑː.n̪o → ˌβilˈlaː.n̪o   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌβilˈlaː.n̪o → ˌβilˈlaː.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌβilˈlaː.n̪ə → ˌβilˈlaːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌβilˈlaːn̪ə̯ → ˌβilˈlaːn̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌβilˈlaːn̪ → ˌβilˈlae̯n̪   (ˈaː→ˈae̯)
600: the remaining bilabial fricative becomes v
    ˌβilˈlae̯n̪ → ˌvilˈlae̯n̪   (β→v)
750: the ae̯ diphthong's offglide hardens to j before a non-velar/palatal nasal, under stress
    ˌvilˈlae̯n̪ → ˌvilˈlajn̪   (e̯→j)
750: an identical consonant geminate reduces to one (recurrence)
    ˌvilˈlajn̪ → ˌviˈlajn̪   (l→∅)
1000: j nasalizes after a low vowel, before a nasal (first nasalization)
    ˌviˈlajn̪ → ˌviˈlaj̃n̪   (j→j̃)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌviˈlaj̃n̪ → ˌviˈlãj̃n̪   (ˈa→ˈã)
1000: nasalized aj becomes ɛ̃j everywhere
    ˌviˈlãj̃n̪ → ˌviˈlɛ̃j̃n̪   (ˈã→ˈɛ̃)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌviˈlɛ̃j̃n̪ → ˌviˈlɛ̃n̪   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌviˈlɛ̃n̪ → ˌviˈlɛ̃ː   (ˈɛ̃n̪→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌviˈlɛ̃ː → vi.lɛ̃ː   (ˌi→i, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    vi.lɛ̃ː → vi.lɛ̃   (ɛ̃ː→ɛ̃)
```

## vivre

`wˈiːwere` → `vivʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwiː.we.re → ˈɣʷiː.ɣʷe.re   (w→ɣʷ, w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷiː.ɣʷe.re → ˈɣʷiː.ɣʷɛ.rɛ   (e→ɛ, e→ɛ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷiː.ɣʷɛ.rɛ → ˈβʷiː.βʷɛ.rɛ   (ɣʷ→βʷ, ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˈβʷiː.βʷɛ.rɛ → ˈβʷi.βʷɛ.rɛ   (ˈiː→ˈi)
300: a stressed vowel lengthens before a single consonant + glide
    ˈβʷi.βʷɛ.rɛ → ˈβʷiː.βʷɛ.rɛ   (ˈi→ˈiː)
500: ɛ lost before a coronal non-nasal sonorant + vowel, near the end of the word
    ˈβʷiː.βʷɛ.rɛ → ˈβʷiː.βʷrɛ   (ɛ→∅)
500: a vowel shortens before a consonant cluster
    ˈβʷiː.βʷrɛ → ˈβʷi.βʷrɛ   (ˈiː→ˈi)
500: a stressed vowel lengthens before a voiced labial + r + vowel + word end
    ˈβʷi.βʷrɛ → ˈβʷiː.βʷrɛ   (ˈi→ˈiː)
500: labialized bilabial fricatives delabialize
    ˈβʷiː.βʷrɛ → ˈβiː.βrɛ   (βʷ→β, βʷ→β)
500: a vowel shortens before a consonant cluster (recurrence)
    ˈβiː.βrɛ → ˈβi.βrɛ   (ˈiː→ˈi)
500: a stressed vowel lengthens before a voiced labial + r + vowel (recurrence)
    ˈβi.βrɛ → ˈβiː.βrɛ   (ˈi→ˈiː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβiː.βrɛ → ˈβiː.βrə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈβiː.βrə → ˈβiːβrə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈβiːβrə̯ → ˈβiː.βrə   (ə̯→ə)
600: the bilabial fricative becomes v after a non-low front vowel before r
    ˈβiː.βrə → ˈβiː.vrə   (β→v)
600: the remaining bilabial fricative becomes v
    ˈβiː.vrə → ˈviː.vrə   (β→v)
750: vowel length resets to short
    ˈviː.vrə → ˈvi.vrə   (ˈiː→ˈi)
1400: final ə becomes a non-syllabic off-glide
    ˈvi.vrə → ˈvivrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈvivrə̯ → ˈvivr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈvivr → ˈvivʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈvivʀ → vivʀ   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    vivʀ → vivʁ   (ʀ→ʁ)
```

## voiture

`wˌeːkt̪ˈuːrɑm` → `vwa.t̪yʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌweːkˈt̪uː.rɑm → ˌɣʷeːkˈt̪uː.rɑm   (w→ɣʷ)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˌɣʷeːkˈt̪uː.rɑm → ˌβʷeːkˈt̪uː.rɑm   (ɣʷ→βʷ)
-100: the length feature is dropped now that quality carries the contrast
    ˌβʷeːkˈt̪uː.rɑm → ˌβʷekˈt̪u.rɑm   (ˌeː→ˌe, ˈuː→ˈu)
-100: k spirantizes to x after a vowel/glide before a voiceless coronal
    ˌβʷekˈt̪u.rɑm → ˌβʷexˈt̪u.rɑm   (k→x)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌβʷexˈt̪u.rɑm → ˌβʷexˈt̪u.rɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌβʷexˈt̪u.rɑ → ˌβʷexˈt̪uː.rɑ   (ˈu→ˈuː)
500: labialized bilabial fricatives delabialize
    ˌβʷexˈt̪uː.rɑ → ˌβexˈt̪uː.rɑ   (βʷ→β)
500: the low vowel fronts by default
    ˌβexˈt̪uː.rɑ → ˌβexˈt̪uː.ra   (ɑ→a)
500: the back high continuant obstruent (x) fronts before a coronal
    ˌβexˈt̪uː.ra → ˌβeçˈt̪uː.ra   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌβeçˈt̪uː.ra → ˌβeçˈt̪ʲuː.ra   (t̪→t̪ʲ)
500: a high tense round non-nasal vowel centralizes
    ˌβeçˈt̪ʲuː.ra → ˌβeçˈt̪ʲʉː.ra   (ˈuː→ˈʉː)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌβeçˈt̪ʲʉː.ra → ˌβeçjˈt̪ʉː.ra   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌβeçjˈt̪ʉː.ra → ˌβeçˈt̪ʉː.ra   (j→∅)
600: the remaining bilabial fricative becomes v
    ˌβeçˈt̪ʉː.ra → ˌveçˈt̪ʉː.ra   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌveçˈt̪ʉː.ra → ˌveçˈt̪ʉː.rə   (a→ə)
750: vowel length resets to short
    ˌveçˈt̪ʉː.rə → ˌveçˈt̪ʉ.rə   (ˈʉː→ˈʉ)
750: ç merges into ʝ
    ˌveçˈt̪ʉ.rə → ˌveʝˈt̪ʉ.rə   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌveʝˈt̪ʉ.rə → ˌvejˈt̪ʉ.rə   (ʝ→j)
1000: high round back vowels front (completion of u-fronting)
    ˌvejˈt̪ʉ.rə → ˌvejˈt̪y.rə   (ˈʉ→ˈy)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌvejˈt̪y.rə → ˌvojˈt̪y.rə   (ˌe→ˌo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌvojˈt̪y.rə → ˌvujˈt̪y.rə   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌvujˈt̪y.rə → ˌvuɛ̯ˈt̪y.rə   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌvuɛ̯ˈt̪y.rə → ˌvwɛˈt̪y.rə   (ˌu→w, ɛ̯→ˌɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌvwɛˈt̪y.rə → ˌvwɛˈt̪yrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌvwɛˈt̪yrə̯ → ˌvwɛˈt̪yr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌvwɛˈt̪yr → ˌvwɛˈt̪yʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌvwɛˈt̪yʀ → vwɛ.t̪yʀ   (ˌɛ→ɛ, ˈy→y)
1400: wɛ becomes wa
    vwɛ.t̪yʀ → vwa.t̪yʀ   (ɛ→a)
1400: the uvular trill ʀ becomes a fricative ʁ
    vwa.t̪yʀ → vwa.t̪yʁ   (ʀ→ʁ)
```

## yeux

`ˈokuloːs` → `y`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈo.ku.loːs → ˈɔ.kʊ.loːs   (ˈo→ˈɔ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈɔ.kʊ.loːs → ˈɔ.kloːs   (ʊ→∅)
-100: the length feature is dropped now that quality carries the contrast
    ˈɔ.kloːs → ˈɔ.klos   (oː→o)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈɔ.klos → ˈɔː.klos   (ˈɔ→ˈɔː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˈɔː.klos → ˈɔː.xlos   (k→x)
500: a vowel shortens before a consonant cluster
    ˈɔː.xlos → ˈɔ.xlos   (ˈɔː→ˈɔ)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈɔ.xlos → ˈɔ.çlos   (x→ç)
500: a lateral palatalizes after a high-front consonant
    ˈɔ.çlos → ˈɔ.çʎos   (l→ʎ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈɔ.çʎos → ˈuo̯.çʎos   (ˈɔ→ˈuo̯)
600: yod lost before ʎ or palatalized r
    ˈuo̯.çʎos → ˈuo̯.ʎos   (ç→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈuo̯.ʎos → ˈuo̯.ʎəs   (o→ə)
600: schwa becomes non-syllabic
    ˈuo̯.ʎəs → ˈuo̯ʎə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈuo̯ʎə̯s → ˈuo̯ʎs   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈuo̯ʎs → ˈuo̯ʎsʲ   (s→sʲ)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈuo̯ʎsʲ → ˈʉo̯ʎsʲ   (ˈu→ˈʉ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈʉo̯ʎsʲ → ˈʉo̯ʎjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈʉo̯ʎjs → ˈʉo̯ʎs   (j→∅)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈʉo̯ʎs → ˈʉo̯ʎt͡sʲ   (s→t͡sʲ)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈʉo̯ʎt͡sʲ → ˈʉo̯ɫt͡sʲ   (ʎ→ɫ)
1000: high round back vowels front (completion of u-fronting)
    ˈʉo̯ɫt͡sʲ → ˈyo̯ɫt͡sʲ   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈyo̯ɫt͡sʲ → ˈye̯ɫt͡sʲ   (o̯→e̯)
1000: the e-glide deletes after a stressed high front tense vowel, before a +cons yod + consonant
    ˈye̯ɫt͡sʲ → ˈyɫt͡sʲ   (e̯→∅)
1000: back dark-l variants vocalize to w
    ˈyɫt͡sʲ → ˈywt͡sʲ   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˈywt͡sʲ → ˈyt͡sʲ   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˈyt͡sʲ → ˈysʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈysʲ → ˈys   (sʲ→s)
1400: final obstruents are lost
    ˈys → ˈy   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈy → y   (ˈy→y)
```

## âge

`ˌae̯t̪ˈɑːt̪ikum` → `ɑʒ`

```
-100: low vowel backs by default
    ˌae̯ˈt̪ɑː.t̪i.kum → ˌɑe̯ˈt̪ɑː.t̪i.kum   (ˌa→ˌɑ)
-100: low vowel re-fronts before the e-glide
    ˌɑe̯ˈt̪ɑː.t̪i.kum → ˌae̯ˈt̪ɑː.t̪i.kum   (ˌɑ→ˌa)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌae̯ˈt̪ɑː.t̪i.kum → ˌae̯ˈt̪ɑː.t̪ɪ.kʊm   (i→ɪ, u→ʊ)
-100: the length feature is dropped now that quality carries the contrast
    ˌae̯ˈt̪ɑː.t̪ɪ.kʊm → ˌae̯ˈt̪ɑ.t̪ɪ.kʊm   (ˈɑː→ˈɑ)
-100: the ae diphthong monophthongizes to ɛ, preserving any stress mark
    ˌae̯ˈt̪ɑ.t̪ɪ.kʊm → ˌɛˈt̪ɑ.t̪ɪ.kʊm   (ˌae̯→ˌɛ)
-100: lax high vowels lower to tense mid vowels
    ˌɛˈt̪ɑ.t̪ɪ.kʊm → ˌɛˈt̪ɑ.t̪e.kom   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌɛˈt̪ɑ.t̪e.kom → ˌɛˈt̪ɑ.t̪e.ko   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌɛˈt̪ɑ.t̪e.ko → ˌɛˈt̪ɑː.t̪e.ko   (ˈɑ→ˈɑː)
500: k voices to g intervocalically
    ˌɛˈt̪ɑː.t̪e.ko → ˌɛˈt̪ɑː.t̪e.go   (k→g)
500: g spirantizes to ɣ intervocalically (recurrence)
    ˌɛˈt̪ɑː.t̪e.go → ˌɛˈt̪ɑː.t̪e.ɣo   (g→ɣ)
500: the low vowel fronts by default
    ˌɛˈt̪ɑː.t̪e.ɣo → ˌɛˈt̪aː.t̪e.ɣo   (ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˌɛˈt̪aː.t̪e.ɣo → ˌɛˈt̪aː.t̪ə.ɣo   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɛˈt̪aː.t̪ə.ɣo → ˌɛˈt̪aː.t̪ə.ɣə   (o→ə)
600: schwa becomes non-syllabic
    ˌɛˈt̪aː.t̪ə.ɣə → ˌɛˈt̪aːt̪ə̯ɣə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after a non-strident coronal before the velar fricative
    ˌɛˈt̪aːt̪ə̯ɣə̯ → ˌɛˈt̪aː.t̪əɣə̯   (ə̯→ə)
600: non-syllabic schwa restores after a dental fricative + schwa + the velar fricative
    ˌɛˈt̪aː.t̪əɣə̯ → ˌɛˈt̪aː.t̪ə.ɣə   (ə̯→ə)
600: a voiceless consonant voices intervocalically
    ˌɛˈt̪aː.t̪ə.ɣə → ˌɛˈd̪aː.d̪ə.ɣə   (t̪→d̪, t̪→d̪)
600: t/d/ð + schwa + the velar fricative becomes an affricate
    ˌɛˈd̪aː.d̪ə.ɣə → ˌɛˈd̪aː.d̪d͡ʒə   (əɣ→d͡ʒ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌɛˈd̪aː.d̪d͡ʒə → ˌɛˈðaː.d̪d͡ʒə   (d̪→ð)
600: a vowel shortens before a consonant cluster ending in an obstruent (recurrence)
    ˌɛˈðaː.d̪d͡ʒə → ˌɛˈða.d̪d͡ʒə   (ˈaː→ˈa)
600: secondary-stressed ɛ raises to e word-initially before a coronal continuant
    ˌɛˈða.d̪d͡ʒə → ˌeˈða.d̪d͡ʒə   (ˌɛ→ˌe)
750: a dental stop deletes before another coronal stop
    ˌeˈða.d̪d͡ʒə → ˌeˈða.d͡ʒə   (d̪→∅)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌeˈða.d͡ʒə → ˌəˈða.d͡ʒə   (ˌe→ˌə)
1000: the interdental fricatives (plain and palatalized) efface
    ˌəˈða.d͡ʒə → ˌəˈa.d͡ʒə   (ð→∅)
1000: all affricates become sibilants (deaffrication)
    ˌəˈa.d͡ʒə → ˌəˈa.ʒə   (d͡ʒ→ʒ)
1200: a stressless schwa desyllabifies before another vowel
    ˌəˈa.ʒə → ˈə̯a.ʒə   (ˌə→ə̯)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˈə̯a.ʒə → ˈə̯aː.ʒə   (ˈa→ˈaː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈə̯aː.ʒə → ˈaː.ʒə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈaː.ʒə → ˈaːʒə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈaːʒə̯ → ˈɑːʒə̯   (ˈaː→ˈɑː)
1400: the final off-glide schwa is deleted elsewhere
    ˈɑːʒə̯ → ˈɑːʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɑːʒ → ɑːʒ   (ˈɑː→ɑː)
1400: distinctive vowel length is lost entirely
    ɑːʒ → ɑʒ   (ɑː→ɑ)
```

## âme

`ˈɑn̪imɑm` → `ɑm`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɑ.n̪i.mɑm → ˈɑ.n̪ɪ.mɑm   (i→ɪ)
-100: lax high vowels lower to tense mid vowels
    ˈɑ.n̪ɪ.mɑm → ˈɑ.n̪e.mɑm   (ɪ→e)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɑ.n̪e.mɑm → ˈɑ.n̪e.mɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.n̪e.mɑ → ˈɑː.n̪e.mɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈɑː.n̪e.mɑ → ˈaː.n̪e.ma   (ˈɑː→ˈaː, ɑ→a)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈaː.n̪e.ma → ˈaː.n̪ə.ma   (e→ə)
600: schwa becomes non-syllabic
    ˈaː.n̪ə.ma → ˈaːn̪ə̯.ma   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈaːn̪ə̯.ma → ˈaːn̪.ma   (ə̯→∅)
600: a vowel shortens before a consonant cluster ending in a nasal
    ˈaːn̪.ma → ˈan̪.ma   (ˈaː→ˈa)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈan̪.ma → ˈan̪.mə   (a→ə)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈan̪.mə → ˈãn̪.mə   (ˈa→ˈã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈãn̪.mə → ˈãː.mə   (ˈãn̪→ˈãː)
1400: final ə becomes a non-syllabic off-glide
    ˈãː.mə → ˈãːmə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈãːmə̯ → ˈɑ̃ːmə̯   (ˈãː→ˈɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˈɑ̃ːmə̯ → ˈɑ̃ːm   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɑ̃ːm → ɑ̃ːm   (ˈɑ̃ː→ɑ̃ː)
1400: distinctive vowel length is lost entirely
    ɑ̃ːm → ɑ̃m   (ɑ̃ː→ɑ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    ɑ̃m → ɑm   (ɑ̃→ɑ)
```

## épine

`spˈiːn̪ɑm` → `e.pin̪`

```
-100: i-prosthesis before word-initial s + consonant
    ˈspiː.n̪ɑm → ˌɪsˈpiː.n̪ɑm   (∅→ˌɪ)
-100: the length feature is dropped now that quality carries the contrast
    ˌɪsˈpiː.n̪ɑm → ˌɪsˈpi.n̪ɑm   (ˈiː→ˈi)
-100: lax high vowels lower to tense mid vowels
    ˌɪsˈpi.n̪ɑm → ˌesˈpi.n̪ɑm   (ˌɪ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌesˈpi.n̪ɑm → ˌesˈpi.n̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌesˈpi.n̪ɑ → ˌesˈpiː.n̪ɑ   (ˈi→ˈiː)
500: the low vowel fronts by default
    ˌesˈpiː.n̪ɑ → ˌesˈpiː.n̪a   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌesˈpiː.n̪a → ˌesˈpiː.n̪ə   (a→ə)
750: vowel length resets to short
    ˌesˈpiː.n̪ə → ˌesˈpi.n̪ə   (ˈiː→ˈi)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌesˈpi.n̪ə → ˌesˈpĩ.n̪ə   (ˈi→ˈĩ)
1000: s becomes x after a vowel, before any consonant
    ˌesˈpĩ.n̪ə → ˌexˈpĩ.n̪ə   (s→x)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌexˈpĩ.n̪ə → ˌeːˈpĩ.n̪ə   (ˌex→ˌeː)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌeːˈpĩ.n̪ə → ˌeːˈpi.n̪ə   (ˈĩ→ˈi)
1400: final ə becomes a non-syllabic off-glide
    ˌeːˈpi.n̪ə → ˌeːˈpin̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌeːˈpin̪ə̯ → ˌeːˈpin̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌeːˈpin̪ → eː.pin̪   (ˌeː→eː, ˈi→i)
1400: distinctive vowel length is lost entirely
    eː.pin̪ → e.pin̪   (eː→e)
```

## épée

`spˈɑt̪ʰɑm` → `e.pe`

```
-100: aspiration lost on Greek loanwords (2nd century)
    ˈspɑ.t̪ʰɑm → ˈspɑ.t̪ɑm   (t̪ʰ→t̪)
-100: i-prosthesis before word-initial s + consonant
    ˈspɑ.t̪ɑm → ˌɪsˈpɑ.t̪ɑm   (∅→ˌɪ)
-100: lax high vowels lower to tense mid vowels
    ˌɪsˈpɑ.t̪ɑm → ˌesˈpɑ.t̪ɑm   (ˌɪ→ˌe)
-100: word-final nasal consonant lost after an unstressed vowel
    ˌesˈpɑ.t̪ɑm → ˌesˈpɑ.t̪ɑ   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    ˌesˈpɑ.t̪ɑ → ˌesˈpɑː.t̪ɑ   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌesˈpɑː.t̪ɑ → ˌesˈpaː.t̪a   (ˈɑː→ˈaː, ɑ→a)
600: a voiceless consonant voices intervocalically
    ˌesˈpaː.t̪a → ˌesˈpaː.d̪a   (t̪→d̪)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌesˈpaː.d̪a → ˌesˈpaː.ða   (d̪→ð)
600: long stressed vowels diphthongize
    ˌesˈpaː.ða → ˌesˈpae̯.ða   (ˈaː→ˈae̯)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌesˈpae̯.ða → ˌesˈpae̯.ðə   (a→ə)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌesˈpae̯.ðə → ˌesˈpeː.ðə   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˌesˈpeː.ðə → ˌesˈpe.ðə   (ˈeː→ˈe)
1000: s becomes x after a vowel, before any consonant
    ˌesˈpe.ðə → ˌexˈpe.ðə   (s→x)
1000: the interdental fricatives (plain and palatalized) efface
    ˌexˈpe.ðə → ˌexˈpe.ə   (ð→∅)
1000: preconsonantal x is lost after a vowel, which lengthens compensatorily
    ˌexˈpe.ə → ˌeːˈpe.ə   (ˌex→ˌeː)
1200: schwa desyllabifies after another vowel
    ˌeːˈpe.ə → ˌeːˈpeə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˌeːˈpeə̯ → ˌeːˈpeː   (ˈeə̯→ˈeː)
1400: stress is leveled — no longer distinctive for vowels
    ˌeːˈpeː → eː.peː   (ˌeː→eː, ˈeː→eː)
1400: distinctive vowel length is lost entirely
    eː.peː → e.pe   (eː→e, eː→e)
```

## œil

`ˈokulum` → `œj`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈo.ku.lum → ˈɔ.kʊ.lʊm   (ˈo→ˈɔ, u→ʊ, u→ʊ)
-100: posttonic ʊ/o syncopates before l + vowel near the end of the word
    ˈɔ.kʊ.lʊm → ˈɔ.klʊm   (ʊ→∅)
-100: lax high vowels lower to tense mid vowels
    ˈɔ.klʊm → ˈɔ.klom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈɔ.klom → ˈɔ.klo   (m→∅)
300: a stressed vowel lengthens before a plosive + non-nasal sonorant (muta cum liquida)
    ˈɔ.klo → ˈɔː.klo   (ˈɔ→ˈɔː)
500: a velar stop spirantizes after a vowel/glide before a coronal consonant
    ˈɔː.klo → ˈɔː.xlo   (k→x)
500: a vowel shortens before a consonant cluster
    ˈɔː.xlo → ˈɔ.xlo   (ˈɔː→ˈɔ)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈɔ.xlo → ˈɔ.çlo   (x→ç)
500: a lateral palatalizes after a high-front consonant
    ˈɔ.çlo → ˈɔ.çʎo   (l→ʎ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈɔ.çʎo → ˈuo̯.çʎo   (ˈɔ→ˈuo̯)
600: yod lost before ʎ or palatalized r
    ˈuo̯.çʎo → ˈuo̯.ʎo   (ç→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈuo̯.ʎo → ˈuo̯.ʎə   (o→ə)
600: schwa becomes non-syllabic
    ˈuo̯.ʎə → ˈuo̯ʎə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈuo̯ʎə̯ → ˈuo̯ʎ   (ə̯→∅)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈuo̯ʎ → ˈʉo̯ʎ   (ˈu→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈʉo̯ʎ → ˈyo̯ʎ   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈyo̯ʎ → ˈye̯ʎ   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈye̯ʎ → ˈøʎ   (ˈye̯→ˈø)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈøʎ → ˈœʎ   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˈœʎ → œʎ   (ˈœ→œ)
1400: ʎ becomes j
    œʎ → œj   (ʎ→j)
```
