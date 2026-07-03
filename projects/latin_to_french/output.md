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

`ˌɑmˈiːkum` → `a.mi`

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
500: a vowel shortens before a consonant cluster
    ˈɑː.xwɑ → ˈɑ.xwɑ   (ˈɑː→ˈɑ)
500: the low vowel fronts by default
    ˈɑ.xwɑ → ˈa.xwa   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈa.xwa → ˈa.xwʲa   (w→wʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈa.xwʲa → ˈa.xɥa   (wʲ→ɥ)
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈa.xɥa → ˈa.xɥa.ə   (∅→ə)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈa.xɥa.ə → ˈa.xɥə.ə   (a→ə)
750: remaining x/ɣ front
    ˈa.xɥə.ə → ˈa.çɥə.ə   (x→ç)
750: ç merges into ʝ
    ˈa.çɥə.ə → ˈa.ʝɥə.ə   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈa.ʝɥə.ə → ˈaj.ɥə.ə   (ʝ→j)
1200: a stressless schwa desyllabifies before another vowel
    ˈaj.ɥə.ə → ˈaj.ɥə̯ə   (ə→ə̯)
1200: schwa desyllabifies after another vowel
    ˈaj.ɥə̯ə → ˈajɥə̯ə̯   (ə→ə̯)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈajɥə̯ə̯ → ˈɛːɥə̯ə̯   (ˈaj→ˈɛː)
1200: a non-syllabic schwa effaces after another vowel
    ˈɛːɥə̯ə̯ → ˈɛːɥə̯   (ə̯→∅)
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
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈann → ˈãnn   (ˈa→ˈã)
1200: geminates simplify to single consonants
    ˈãnn → ˈãn   (n→∅)
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
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈɔwrə̯ → ˈɔw.rə   (ə̯→ə)
600: a stressed vowel lengthens before a voiced labial + r + vowel + word end
    ˈɔw.rə → ˈɔːw.rə   (ˈɔ→ˈɔː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˈɔːw.rə → ˈuo̯w.rə   (ˈɔː→ˈuo̯)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈuo̯w.rə → ˈʉo̯w.rə   (ˈu→ˈʉ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈʉo̯w.rə → ˈʉo̯.rə   (w→∅)
1000: high round back vowels front (completion of u-fronting)
    ˈʉo̯.rə → ˈyo̯.rə   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈyo̯.rə → ˈye̯.rə   (o̯→e̯)
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈye̯.rə → ˈø.rə   (ˈye̯→ˈø)
1400: final ə becomes a non-syllabic off-glide
    ˈø.rə → ˈørə̯   (ə→ə̯)
1400: the tonic vowel of or is back ɔ (au monophthong), not front œ
    ˈørə̯ → ˈɔrə̯   (ˈø→ˈɔ)
1400: the final off-glide schwa is deleted elsewhere
    ˈɔrə̯ → ˈɔr   (ə̯→∅)
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

`ˌɑmˈɑːrɑm` → `a.mɛʁ`

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
-100: a segment marked both back and front loses the back specification
    ˈɑlɫ.ʝo → ˈɑllʲ.ʝo   (ɫ→lʲ)
500: a lateral palatalizes before a high-front consonant
    ˈɑllʲ.ʝo → ˈɑʎʎ.ʝo   (l→ʎ, lʲ→ʎ)
500: the low vowel fronts by default
    ˈɑʎʎ.ʝo → ˈaʎʎ.ʝo   (ˈɑ→ˈa)
600: a yod is absorbed by a preceding palatal lateral (ʎj > ʎ)
    ˈaʎʎ.ʝo → ˈaʎ.ʎo   (ʝ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaʎ.ʎo → ˈaʎ.ʎə   (o→ə)
600: schwa becomes non-syllabic
    ˈaʎ.ʎə → ˈaʎʎə̯   (ə→ə̯)
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
    ˈaʎʎə̯ → ˈaʎ.ʎə   (ə̯→ə)
1200: geminates simplify to single consonants
    ˈaʎ.ʎə → ˈa.ʎə   (ʎ→∅)
1400: a lengthens before final ʎə
    ˈa.ʎə → ˈaː.ʎə   (ˈa→ˈaː)
1400: final ə becomes a non-syllabic off-glide
    ˈaː.ʎə → ˈaːʎə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˈaːʎə̯ → ˈɑːʎə̯   (ˈaː→ˈɑː)
1400: the long a stays front in words that lexically resisted backing
    ˈɑːʎə̯ → ˈaːʎə̯   (ˈɑː→ˈaː)
1400: the final off-glide schwa is deleted elsewhere
    ˈaːʎə̯ → ˈaːʎ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈaːʎ → aːʎ   (ˈaː→aː)
1400: distinctive vowel length is lost entirely
    aːʎ → aʎ   (aː→a)
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
-100: a segment marked both back and front loses the back specification
    ˈɑɫ.bɑ → ˈɑlʲ.bɑ   (ɫ→lʲ)
500: the low vowel fronts by default
    ˈɑlʲ.bɑ → ˈalʲ.ba   (ˈɑ→ˈa, ɑ→a)
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈalʲ.ba → ˈalʲ.ba.ə   (∅→ə)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈalʲ.ba.ə → ˈalʲ.bə.ə   (a→ə)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈalʲ.bə.ə → ˈaɫ.bə.ə   (lʲ→ɫ)
1000: back dark-l variants vocalize to w
    ˈaɫ.bə.ə → ˈaw.bə.ə   (ɫ→w)
1200: a stressless schwa desyllabifies before another vowel
    ˈaw.bə.ə → ˈaw.bə̯ə   (ə→ə̯)
1200: schwa desyllabifies after another vowel
    ˈaw.bə̯ə → ˈawbə̯ə̯   (ə→ə̯)
1200: aw becomes long oː
    ˈawbə̯ə̯ → ˈoːbə̯ə̯   (ˈaw→ˈoː)
1200: a non-syllabic schwa effaces after another vowel
    ˈoːbə̯ə̯ → ˈoːbə̯   (ə̯→∅)
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

`ˈɑːbilem` → `ɛv`

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
600: non-syllabic schwa restores before a front sonorant consonant
    ˈaːβə̯lə̯ → ˈaː.βələ̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈaː.βələ̯ → ˈaː.βəl   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈaː.βəl → ˈae̯.βəl   (ˈaː→ˈae̯)
600: the remaining bilabial fricative becomes v
    ˈae̯.βəl → ˈae̯.vəl   (β→v)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈae̯.vəl → ˈeː.vəl   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈeː.vəl → ˈe.vəl   (ˈeː→ˈe)
1200: a single final consonant effaces after schwa
    ˈe.vəl → ˈe.və   (l→∅)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˈe.və → ˈɛ.və   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈɛ.və → ˈɛvə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈɛvə̯ → ˈɛv   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛv → ɛv   (ˈɛ→ɛ)
```

## auguste

`ˌɑwˈgustus` → `ɔ.gu`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌɑwˈgus.tus → ˌɑwˈgʊs.tʊs   (ˈu→ˈʊ, u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˌɑwˈgʊs.tʊs → ˌɑwˈgos.tos   (ˈʊ→ˈo, ʊ→o)
500: the low vowel fronts by default
    ˌɑwˈgos.tos → ˌawˈgos.tos   (ˌɑ→ˌa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˌawˈgos.tos → ˌɔwˈgos.tos   (ˌa→ˌɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌɔwˈgos.tos → ˌɔwˈgos.təs   (o→ə)
600: schwa becomes non-syllabic
    ˌɔwˈgos.təs → ˌɔwˈgostə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌɔwˈgostə̯s → ˌɔwˈgosts   (ə̯→∅)
600: secondary-stressed ɔ raises to ɯ before w
    ˌɔwˈgosts → ˌɯwˈgosts   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌɯwˈgosts → ˌɔwˈgosts   (ˌɯ→ˌɔ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌɔwˈgosts → ˌɔˈgosts   (w→∅)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌɔˈgosts → ˌɔˈgoss   (t→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌɔˈgoss → ˌɔˈguss   (ˈo→ˈu)
1000: s becomes x after a vowel, before any consonant
    ˌɔˈguss → ˌɔˈguxs   (s→x)
1000: the velar fricative x is lost
    ˌɔˈguxs → ˌɔˈgus   (x→∅)
1400: final obstruents are lost
    ˌɔˈgus → ˌɔˈgu   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌɔˈgu → ɔ.gu   (ˌɔ→ɔ, ˈu→u)
```

## avers

`ˌɑd̪wˈersum` → `a.vjɛʁ`

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
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌaˈlɔw.sa → ˌaˈlɔ.sa   (w→∅)
750: a voiceless fricative voices intervocalically (recurrence, after the diphthongs resolve)
    ˌaˈlɔ.sa → ˌaˈlɔ.za   (s→z)
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

`ˈɑkin̪um` → `ɛ.zə̃`

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
300: a stressed vowel lengthens before a single consonant + glide
    ˈɑ.ce.n̪o → ˈɑː.ce.n̪o   (ˈɑ→ˈɑː)
500: a palatal stop affricates
    ˈɑː.ce.n̪o → ˈɑː.t͡sʲe.n̪o   (c→t͡sʲ)
500: the low vowel fronts by default
    ˈɑː.t͡sʲe.n̪o → ˈaː.t͡sʲe.n̪o   (ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈaː.t͡sʲe.n̪o → ˈaː.t͡sʲə.n̪o   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈaː.t͡sʲə.n̪o → ˈaː.t͡sʲə.n̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈaː.t͡sʲə.n̪ə → ˈaːt͡sʲə̯n̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores before a front sonorant consonant
    ˈaːt͡sʲə̯n̪ə̯ → ˈaː.t͡sʲən̪ə̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈaː.t͡sʲən̪ə̯ → ˈaː.t͡sʲən̪   (ə̯→∅)
600: a voiceless consonant voices intervocalically
    ˈaː.t͡sʲən̪ → ˈaː.d͡zʲən̪   (t͡sʲ→d͡zʲ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˈaː.d͡zʲən̪ → ˈaː.zʲən̪   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈaː.zʲən̪ → ˈaːj.zən̪   (zʲ→jz)
600: a vowel shortens before a consonant cluster ending in an obstruent (recurrence)
    ˈaːj.zən̪ → ˈaj.zən̪   (ˈaː→ˈa)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈaj.zən̪ → ˈaj.zə̃n̪   (ə→ə̃)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈaj.zə̃n̪ → ˈaj.zə̃ː   (ə̃n̪→ə̃ː)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈaj.zə̃ː → ˈɛː.zə̃ː   (ˈaj→ˈɛː)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛː.zə̃ː → ɛː.zə̃ː   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    ɛː.zə̃ː → ɛ.zə̃   (ɛː→ɛ, ə̃ː→ə̃)
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

`ˌɑrd̪ˈeːsiɑm` → `aʁ.d̪waz`

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

`ˌɑwsˈɑːre` → `o.ze`

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
600: long stressed vowels diphthongize
    ˌɔwˈsaːr → ˌɔwˈsae̯r   (ˈaː→ˈae̯)
600: secondary-stressed ɔ raises to ɯ before w
    ˌɔwˈsae̯r → ˌɯwˈsae̯r   (ˌɔ→ˌɯ)
600: the intermediate central vowels revert to ɛ/ɔ
    ˌɯwˈsae̯r → ˌɔwˈsae̯r   (ˌɯ→ˌɔ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌɔwˈsae̯r → ˌɔˈsae̯r   (w→∅)
750: a voiceless fricative voices intervocalically (recurrence, after the diphthongs resolve)
    ˌɔˈsae̯r → ˌɔˈzae̯r   (s→z)
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

`bˈɑrgɑm` → `baʁʒ`

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

`bˈellɑm` → `bɛl`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈbel.lɑm → ˈbɛl.lɑm   (ˈe→ˈɛ)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈbɛl.lɑm → ˈbɛl.lɑ   (m→∅)
500: the low vowel fronts by default
    ˈbɛl.lɑ → ˈbɛl.la   (ɑ→a)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈbɛl.la → ˈbɛl.lə   (a→ə)
1000: intervocalic geminate ll degeminates to a single l (before l-vocalization)
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
500: the low vowel fronts by default
    ˈbox.se.t̪ɑ → ˈbox.se.t̪a   (ɑ→a)
500: the back high continuant obstruent (x) fronts before a coronal
    ˈbox.se.t̪a → ˈboç.se.t̪a   (x→ç)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈboç.se.t̪a → ˈboç.sʲe.t̪a   (s→sʲ)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈboç.sʲe.t̪a → ˈboç.sʲə.t̪a   (e→ə)
600: schwa becomes non-syllabic
    ˈboç.sʲə.t̪a → ˈboçsʲə̯.t̪a   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈboçsʲə̯.t̪a → ˈboçsʲ.t̪a   (ə̯→∅)
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
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈbojs.t̪ə → ˈboj.t̪ə   (s→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈboj.t̪ə → ˈbuj.t̪ə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈbuj.t̪ə → ˈbuɛ̯.t̪ə   (j→ɛ̯)
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

`d̪ˈeːbet̪` → `d̪ø`

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
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈd̪eːβθ → ˈd̪eːβ.θə   (∅→ə)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈd̪eːβ.θə → ˈd̪eβ.θə   (ˈeː→ˈe)
600: the bilabial fricative becomes w before a non-labial obstruent
    ˈd̪eβ.θə → ˈd̪ew.θə   (β→w)
1000: the interdental fricatives (plain and palatalized) efface
    ˈd̪ew.θə → ˈd̪e.wə   (θ→∅)
1000: ew becomes øw
    ˈd̪e.wə → ˈd̪ø.wə   (ˈe→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈd̪ø.wə → ˈd̪ø.ə   (w→∅)
1200: schwa desyllabifies after another vowel
    ˈd̪ø.ə → ˈd̪øə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after a stressed syllable, lengthening it
    ˈd̪øə̯ → ˈd̪øː   (ˈøə̯→ˈøː)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪øː → d̪øː   (ˈøː→øː)
1400: distinctive vowel length is lost entirely
    d̪øː → d̪ø   (øː→ø)
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
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈd̪ɔrmθ → ˈd̪ɔrm.θə   (∅→ə)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈd̪ɔrm.θə → ˈd̪ɔr.θə   (m→∅)
1000: the interdental fricatives (plain and palatalized) efface
    ˈd̪ɔr.θə → ˈd̪ɔ.rə   (θ→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈd̪ɔ.rə → ˈd̪ɔrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈd̪ɔrə̯ → ˈd̪ɔr   (ə̯→∅)
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

`ˈekwɑ` → `ɛjɥ`

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
500: a vowel shortens before a consonant cluster
    ˈɛː.xwɑ → ˈɛ.xwɑ   (ˈɛː→ˈɛ)
500: the low vowel fronts by default
    ˈɛ.xwɑ → ˈɛ.xwa   (ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈɛ.xwa → ˈɛ.xwʲa   (w→wʲ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈɛ.xwʲa → ˈɛ.xɥa   (wʲ→ɥ)
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈɛ.xɥa → ˈɛ.xɥa.ə   (∅→ə)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈɛ.xɥa.ə → ˈɛ.xɥə.ə   (a→ə)
750: remaining x/ɣ front
    ˈɛ.xɥə.ə → ˈɛ.çɥə.ə   (x→ç)
750: ç merges into ʝ
    ˈɛ.çɥə.ə → ˈɛ.ʝɥə.ə   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈɛ.ʝɥə.ə → ˈɛj.ɥə.ə   (ʝ→j)
1200: a stressless schwa desyllabifies before another vowel
    ˈɛj.ɥə.ə → ˈɛj.ɥə̯ə   (ə→ə̯)
1200: schwa desyllabifies after another vowel
    ˈɛj.ɥə̯ə → ˈɛjɥə̯ə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after another vowel
    ˈɛjɥə̯ə̯ → ˈɛjɥə̯   (ə̯→∅)
1400: the final off-glide schwa is deleted elsewhere
    ˈɛjɥə̯ → ˈɛjɥ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈɛjɥ → ɛjɥ   (ˈɛ→ɛ)
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
-100: a segment marked both back and front loses the back specification
    ˈfɔɫ.ʝɑ → ˈfɔlʲ.ʝɑ   (ɫ→lʲ)
500: a lateral palatalizes before a high-front consonant
    ˈfɔlʲ.ʝɑ → ˈfɔʎ.ʝɑ   (lʲ→ʎ)
500: the low vowel fronts by default
    ˈfɔʎ.ʝɑ → ˈfɔʎ.ʝa   (ɑ→a)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈfɔʎ.ʝa → ˈfuo̯ʎ.ʝa   (ˈɔ→ˈuo̯)
600: a yod is absorbed by a preceding palatal lateral (ʎj > ʎ)
    ˈfuo̯ʎ.ʝa → ˈfuo̯.ʎa   (ʝ→∅)
600: a high tense round non-nasal vowel centralizes (recurrence)
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
1000: s becomes x after a vowel, before any consonant
    ˈfɔs.sə → ˈfɔx.sə   (s→x)
1000: the velar fricative x is lost
    ˈfɔx.sə → ˈfɔ.sə   (x→∅)
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

`gˈɑwt̪ɑ` → `ʒut̪`

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
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd͡ʒɔw.t̪a → ˈd͡ʒɔw.t̪ə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒɔw.t̪ə → ˈʒɔw.t̪ə   (d͡ʒ→ʒ)
1200: the ow diphthong monophthongizes to u
    ˈʒɔw.t̪ə → ˈʒu.t̪ə   (ˈɔw→ˈu)
1400: final ə becomes a non-syllabic off-glide
    ˈʒu.t̪ə → ˈʒut̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈʒut̪ə̯ → ˈʒut̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒut̪ → ʒut̪   (ˈu→u)
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

`ˈjuwen̪em` → `ʒu.və̃`

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
300: a stressed vowel lengthens before a single consonant + glide
    ˈʝo.βʷɛ.n̪ɛ → ˈʝoː.βʷɛ.n̪ɛ   (ˈo→ˈoː)
500: labialized bilabial fricatives delabialize
    ˈʝoː.βʷɛ.n̪ɛ → ˈʝoː.βɛ.n̪ɛ   (βʷ→β)
600: yod hardens to ɟ word-initially before a vowel
    ˈʝoː.βɛ.n̪ɛ → ˈɟoː.βɛ.n̪ɛ   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈɟoː.βɛ.n̪ɛ → ˈd͡ʒoː.βɛ.n̪ɛ   (ɟ→d͡ʒ)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈd͡ʒoː.βɛ.n̪ɛ → ˈd͡ʒoː.βə.n̪ɛ   (ɛ→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd͡ʒoː.βə.n̪ɛ → ˈd͡ʒoː.βə.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈd͡ʒoː.βə.n̪ə → ˈd͡ʒoːβə̯n̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores before a front sonorant consonant
    ˈd͡ʒoːβə̯n̪ə̯ → ˈd͡ʒoː.βən̪ə̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈd͡ʒoː.βən̪ə̯ → ˈd͡ʒoː.βən̪   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈd͡ʒoː.βən̪ → ˈd͡ʒow.βən̪   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈd͡ʒow.βən̪ → ˈd͡ʒo.βən̪   (w→∅)
600: the remaining bilabial fricative becomes v
    ˈd͡ʒo.βən̪ → ˈd͡ʒo.vən̪   (β→v)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈd͡ʒo.vən̪ → ˈd͡ʒo.və̃n̪   (ə→ə̃)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈd͡ʒo.və̃n̪ → ˈd͡ʒu.və̃n̪   (ˈo→ˈu)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒu.və̃n̪ → ˈʒu.və̃n̪   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈʒu.və̃n̪ → ˈʒu.və̃ː   (ə̃n̪→ə̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒu.və̃ː → ʒu.və̃ː   (ˈu→u)
1400: distinctive vowel length is lost entirely
    ʒu.və̃ː → ʒu.və̃   (ə̃ː→ə̃)
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
1000: all affricates become sibilants (deaffrication)
    ˈt͡sʲjøs → ˈsʲjøs   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈsʲjøs → ˈsjøs   (sʲ→s)
1400: final obstruents are lost
    ˈsjøs → ˈsjø   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈsjø → sjø   (ˈø→ø)
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
500: secondary-stressed a becomes ɛ after a front consonant, before a non-coronal non-consonantal segment
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

`kˈɑrkerem` → `ʃaʁ`

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
500: a palatal stop affricates
    ˈkɑr.crɛ → ˈkɑr.t͡sʲrɛ   (c→t͡sʲ)
500: the low vowel fronts by default
    ˈkɑr.t͡sʲrɛ → ˈkar.t͡sʲrɛ   (ˈɑ→ˈa)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈkar.t͡sʲrɛ → ˈkar.t͡sʲrʲɛ   (r→rʲ)
500: the high back consonant w fronts before a front vowel
    ˈkar.t͡sʲrʲɛ → ˈkʲar.t͡sʲrʲɛ   (k→kʲ)
600: yod lost before ʎ or palatalized r
    ˈkʲar.t͡sʲrʲɛ → ˈkʲar.rʲɛ   (t͡sʲ→∅)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲar.rʲɛ → ˈcar.rʲɛ   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcar.rʲɛ → ˈt͡ʃar.rʲɛ   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt͡ʃar.rʲɛ → ˈt͡ʃar.rʲə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈt͡ʃar.rʲə → ˈt͡ʃarrʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃarrʲə̯ → ˈt͡ʃarrʲ   (ə̯→∅)
600: palatalized r depalatalizes
    ˈt͡ʃarrʲ → ˈt͡ʃarr   (rʲ→r)
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

## Chartres

`kˈɑrt̪un̪eːs` → `ʃaʁ.t̪ə̃`

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
600: schwa becomes non-syllabic
    ˈt͡ʃar.t̪ə.n̪əs → ˈt͡ʃart̪ə̯n̪ə̯s   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores before a front sonorant consonant
    ˈt͡ʃart̪ə̯n̪ə̯s → ˈt͡ʃar.t̪ən̪ə̯s   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈt͡ʃar.t̪ən̪ə̯s → ˈt͡ʃar.t̪ən̪s   (ə̯→∅)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈt͡ʃar.t̪ən̪s → ˈt͡ʃar.t̪ə̃n̪s   (ə→ə̃)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃar.t̪ə̃n̪s → ˈʃar.t̪ə̃n̪s   (t͡ʃ→ʃ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈʃar.t̪ə̃n̪s → ˈʃar.t̪ə̃ːs   (ə̃n̪→ə̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˈʃar.t̪ə̃ːs → ˈʃaɹ.t̪ə̃ːs   (r→ɹ)
1400: final obstruents are lost
    ˈʃaɹ.t̪ə̃ːs → ˈʃaɹ.t̪ə̃ː   (s→∅)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˈʃaɹ.t̪ə̃ː → ˈʃar.t̪ə̃ː   (ɹ→r)
1400: r becomes uvular ʀ
    ˈʃar.t̪ə̃ː → ˈʃaʀ.t̪ə̃ː   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʃaʀ.t̪ə̃ː → ʃaʀ.t̪ə̃ː   (ˈa→a)
1400: distinctive vowel length is lost entirely
    ʃaʀ.t̪ə̃ː → ʃaʀ.t̪ə̃   (ə̃ː→ə̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʃaʀ.t̪ə̃ → ʃaʁ.t̪ə̃   (ʀ→ʁ)
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
600: non-syllabic schwa restores after a stressed vowel + optional consonants + a non-anterior consonant or fricative + sonorant
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

`kˈolpoːs` → `kys`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈkol.poːs → ˈkɔl.poːs   (ˈo→ˈɔ)
-100: l darkens before a non-lateral consonant
    ˈkɔl.poːs → ˈkɔɫ.poːs   (l→ɫ)
-100: the length feature is dropped now that quality carries the contrast
    ˈkɔɫ.poːs → ˈkɔɫ.pos   (oː→o)
-100: a segment marked both back and front loses the back specification
    ˈkɔɫ.pos → ˈkɔlʲ.pos   (ɫ→lʲ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈkɔlʲ.pos → ˈkuo̯lʲ.pos   (ˈɔ→ˈuo̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈkuo̯lʲ.pos → ˈkuo̯lʲ.pəs   (o→ə)
600: schwa becomes non-syllabic
    ˈkuo̯lʲ.pəs → ˈkuo̯lʲpə̯s   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈkuo̯lʲpə̯s → ˈkuo̯lʲps   (ə̯→∅)
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈkuo̯lʲps → ˈkuo̯lʲ.psə   (∅→ə)
600: a labial consonant becomes s before s
    ˈkuo̯lʲ.psə → ˈkuo̯lʲs.sə   (p→s)
600: an identical consonant geminate reduces to one, after a consonant or word start
    ˈkuo̯lʲs.sə → ˈkuo̯lʲ.sə   (s→∅)
600: a high tense round non-nasal vowel centralizes (recurrence)
    ˈkuo̯lʲ.sə → ˈkʉo̯lʲ.sə   (ˈu→ˈʉ)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈkʉo̯lʲ.sə → ˈkʉo̯ɫ.sə   (lʲ→ɫ)
1000: high round back vowels front (completion of u-fronting)
    ˈkʉo̯ɫ.sə → ˈkyo̯ɫ.sə   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈkyo̯ɫ.sə → ˈkye̯ɫ.sə   (o̯→e̯)
1000: the e-glide deletes after a stressed high front tense vowel, before a +cons yod + consonant
    ˈkye̯ɫ.sə → ˈkyɫ.sə   (e̯→∅)
1000: back dark-l variants vocalize to w
    ˈkyɫ.sə → ˈkyw.sə   (ɫ→w)
1000: w deletes immediately after a high round vowel (u or y)
    ˈkyw.sə → ˈky.sə   (w→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈky.sə → ˈkysə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkysə̯ → ˈkys   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈkys → kys   (ˈy→y)
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
1000: the e-glide deletes after a stressed high front tense vowel, before a +cons yod + consonant
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
1400: final obstruents are lost
    ˈkrys → ˈkry   (s→∅)
1400: r becomes uvular ʀ
    ˈkry → ˈkʀy   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkʀy → kʀy   (ˈy→y)
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
500: a voiceless fricative voices intervocalically
    ˈlɑː.t͡sʲɑ → ˈlɑː.d͡zʲɑ   (t͡sʲ→d͡zʲ)
500: the low vowel fronts by default
    ˈlɑː.d͡zʲɑ → ˈlaː.d͡zʲa   (ˈɑː→ˈaː, ɑ→a)
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
600: a coronal palatalizes between two high-front segments
    ˈlie̯çt̪ → ˈlii̯çt̪   (e̯→i̯)
750: ç merges into ʝ
    ˈlii̯çt̪ → ˈlii̯ʝt̪   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈlii̯ʝt̪ → ˈlii̯jt̪   (ʝ→j)
1000: a high non-round glide deletes after stressed i
    ˈlii̯jt̪ → ˈlijt̪   (i̯→∅)
1400: final obstruents are lost
    ˈlijt̪ → ˈlij   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlij → lij   (ˈi→i)
1400: a yod is absorbed after a high front vowel (word-finally or before a consonant)
    lij → li   (j→∅)
```

## lien

`lˌigˈɑːmen̪` → `le.jɛ̃`

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
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌleˈjie̯n̪ → ˌlejˈjen̪   (ˈi→j, e̯→ˈe)
1200: geminates simplify to single consonants
    ˌlejˈjen̪ → ˌleˈjen̪   (j→∅)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˌleˈjen̪ → ˌleˈjẽn̪   (ˈe→ˈẽ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌleˈjẽn̪ → ˌleˈjẽː   (ˈẽn̪→ˈẽː)
1400: nasalized ẽ lowers to ɛ̃
    ˌleˈjẽː → ˌleˈjɛ̃ː   (ˈẽː→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌleˈjɛ̃ː → le.jɛ̃ː   (ˌe→e, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    le.jɛ̃ː → le.jɛ̃   (ɛ̃ː→ɛ̃)
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
300: a stressed vowel lengthens before a single consonant + glide
    ˌmɑ.loˈɑ.βe.t̪o → ˌmɑ.loˈɑː.βe.t̪o   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˌmɑ.loˈɑː.βe.t̪o → ˌma.loˈaː.βe.t̪o   (ˌɑ→ˌa, ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˌma.loˈaː.βe.t̪o → ˌma.loˈaː.βə.t̪o   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌma.loˈaː.βə.t̪o → ˌma.loˈaː.βə.t̪ə   (o→ə)
600: an unstressed non-low tense vowel reduces to schwa unconditionally
    ˌma.loˈaː.βə.t̪ə → ˌma.ləˈaː.βə.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˌma.ləˈaː.βə.t̪ə → ˌmaˈlə̯aːβə̯t̪ə̯   (ə→ə̯, ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores to schwa after a lateral, before an optional obstruent (+ optional schwa) + non-nasal coronal sonorant
    ˌmaˈlə̯aːβə̯t̪ə̯ → ˌma.ləˈaːβə̯t̪ə̯   (ə̯→ə)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˌma.ləˈaːβə̯t̪ə̯ → ˌma.ləˈaːβə̯.t̪ə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˌma.ləˈaːβə̯.t̪ə → ˌma.ləˈaːβ.t̪ə   (ə̯→∅)
600: an anterior coronal voices after a non-high voiced labial consonant, before a voiced segment
    ˌma.ləˈaːβ.t̪ə → ˌma.ləˈaːβ.d̪ə   (t̪→d̪)
600: a labial consonant becomes d before a voiced coronal stop
    ˌma.ləˈaːβ.d̪ə → ˌma.ləˈaːd̪.d̪ə   (β→d̪)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˌma.ləˈaːd̪.d̪ə → ˌma.ləˈad̪.d̪ə   (ˈaː→ˈa)
750: a dental stop deletes before another coronal stop
    ˌma.ləˈad̪.d̪ə → ˌma.ləˈa.d̪ə   (d̪→∅)
1200: a stressless schwa desyllabifies before another vowel
    ˌma.ləˈa.d̪ə → ˌmaˈlə̯a.d̪ə   (ə→ə̯)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˌmaˈlə̯a.d̪ə → ˌmaˈlə̯aː.d̪ə   (ˈa→ˈaː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌmaˈlə̯aː.d̪ə → ˌmaˈlaː.d̪ə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌmaˈlaː.d̪ə → ˌmaˈlaːd̪ə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌmaˈlaːd̪ə̯ → ˌmaˈlɑːd̪ə̯   (ˈaː→ˈɑː)
1400: the long a stays front in words that lexically resisted backing
    ˌmaˈlɑːd̪ə̯ → ˌmaˈlaːd̪ə̯   (ˈɑː→ˈaː)
1400: the final off-glide schwa is deleted elsewhere
    ˌmaˈlaːd̪ə̯ → ˌmaˈlaːd̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmaˈlaːd̪ → ma.laːd̪   (ˌa→a, ˈaː→aː)
1400: distinctive vowel length is lost entirely
    ma.laːd̪ → ma.lad̪   (aː→a)
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
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌman̪ˈt̪ɛll → ˌman̪ˈt̪ɛɫl   (l→ɫ)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˌman̪ˈt̪ɛɫl → ˌmãn̪ˈt̪ɛɫl   (ˌa→ˌã)
1000: schwa is epenthesized word-finally after a back glide + lateral
    ˌmãn̪ˈt̪ɛɫl → ˌmãn̪ˈt̪ɛɫ.lə   (∅→ə)
1000: back dark-l variants vocalize to w
    ˌmãn̪ˈt̪ɛɫ.lə → ˌmãn̪ˈt̪ɛw.lə   (ɫ→w)
1000: the second half of a vocalized geminate l is lost
    ˌmãn̪ˈt̪ɛw.lə → ˌmãn̪ˈt̪ɛ.wə   (l→∅)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌmãn̪ˈt̪ɛ.wə → ˌmãn̪ˈt̪ɛa̯.wə   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌmãn̪ˈt̪ɛa̯.wə → ˌmãn̪ˈt̪e̯a.wə   (ˈɛ→e̯, a̯→ˈa)
1200: aw becomes long oː
    ˌmãn̪ˈt̪e̯a.wə → ˌmãn̪ˈt̪e̯oː.ə   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌmãn̪ˈt̪e̯oː.ə → ˌmãn̪ˈt̪ə̯oː.ə   (e̯→ə̯)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmãn̪ˈt̪ə̯oː.ə → ˌmãːˈt̪ə̯oː.ə   (ˌãn̪→ˌãː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌmãːˈt̪ə̯oː.ə → ˌmãːˈt̪oː.ə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌmãːˈt̪oː.ə → ˌmãːˈt̪oːə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌmãːˈt̪oːə̯ → ˌmɑ̃ːˈt̪oːə̯   (ˌãː→ˌɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˌmɑ̃ːˈt̪oːə̯ → ˌmɑ̃ːˈt̪oː   (ə̯→∅)
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
1000: s becomes x after a vowel, before any consonant
    ˈmas.sə → ˈmax.sə   (s→x)
1000: the velar fricative x is lost
    ˈmax.sə → ˈma.sə   (x→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈma.sə → ˈmasə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈmasə̯ → ˈmas   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmas → mas   (ˈa→a)
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
1000: intervocalic geminate ll degeminates to a single l (before l-vocalization)
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

`mˌin̪uːt̪ˈjɑːre` → `mɑ̃.zje`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˌmi.n̪uːˈt̪jɑː.re → ˌmi.n̪uːˈt̪ʝɑː.re   (j→ʝ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˌmi.n̪uːˈt̪ʝɑː.re → ˌmɪ.n̪uːˈt̪ʝɑː.rɛ   (ˌi→ˌɪ, e→ɛ)
-100: unstressed long u becomes a mid central vowel (sonus medius), not word-finally
    ˌmɪ.n̪uːˈt̪ʝɑː.rɛ → ˌmɪ.n̪ɪˈt̪ʝɑː.rɛ   (uː→ɪ)
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
500: a voiceless fricative voices intervocalically
    ˌme.n̪eˈt͡sʲɑː.rɛ → ˌme.n̪eˈd͡zʲɑː.rɛ   (t͡sʲ→d͡zʲ)
500: an unstressed front tense vowel lost before a coronal + long low vowel
    ˌme.n̪eˈd͡zʲɑː.rɛ → ˌmen̪ˈd͡zʲɑː.rɛ   (e→∅)
500: the low vowel fronts by default
    ˌmen̪ˈd͡zʲɑː.rɛ → ˌmen̪ˈd͡zʲaː.rɛ   (ˈɑː→ˈaː)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌmen̪ˈd͡zʲaː.rɛ → ˌmen̪ˈd͡zʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌmen̪ˈd͡zʲaː.rə → ˌmen̪ˈd͡zʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌmen̪ˈd͡zʲaːrə̯ → ˌmen̪ˈd͡zʲaːr   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌmen̪ˈd͡zʲaːr → ˌmen̪ˈd͡zʲɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌmen̪ˈd͡zʲɛːr → ˌmen̪ˈd͡zʲie̯r   (ˈɛː→ˈie̯)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌmen̪ˈd͡zʲie̯r → ˌmen̪jˈd͡zie̯r   (d͡zʲ→jd͡z)
600: j is lost after j or a consonant, before a consonant
    ˌmen̪jˈd͡zie̯r → ˌmen̪ˈd͡zie̯r   (j→∅)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌmen̪ˈd͡zie̯r → ˌmẽn̪ˈd͡zie̯r   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌmẽn̪ˈd͡zie̯r → ˌmɛ̃n̪ˈd͡zie̯r   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌmɛ̃n̪ˈd͡zie̯r → ˌmãn̪ˈd͡zie̯r   (ˌɛ̃→ˌã)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌmãn̪ˈd͡zie̯r → ˌmãn̪ˈd͡zjer   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌmãn̪ˈd͡zjer → ˌmãn̪ˈzjer   (d͡z→z)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌmãn̪ˈzjer → ˌmãːˈzjer   (ˌãn̪→ˌãː)
1400: long a becomes back ɑː
    ˌmãːˈzjer → ˌmɑ̃ːˈzjer   (ˌãː→ˌɑ̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌmɑ̃ːˈzjer → ˌmɑ̃ːˈzjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌmɑ̃ːˈzjeɹ → ˌmɑ̃ːˈzje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmɑ̃ːˈzje → mɑ̃ː.zje   (ˌɑ̃ː→ɑ̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    mɑ̃ː.zje → mɑ̃.zje   (ɑ̃ː→ɑ̃)
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
1000: the velar fricative x is lost
    ˈmuxt̪ → ˈmut̪   (x→∅)
1400: final obstruents are lost
    ˈmut̪ → ˈmu   (t̪→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈmu → mu   (ˈu→u)
```

## noue

`n̪ˈɑwikɑm` → `n̪ɔʒ`

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
500: the low vowel fronts by default
    ˈn̪ɑw.kɑ → ˈn̪aw.ka   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈn̪aw.ka → ˈn̪aw.kʲa   (k→kʲ)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈn̪aw.kʲa → ˈn̪ɔw.kʲa   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈn̪ɔw.kʲa → ˈn̪ɔw.ca   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈn̪ɔw.ca → ˈn̪ɔw.t͡ʃa   (c→t͡ʃ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈn̪ɔw.t͡ʃa → ˈn̪ɔ.t͡ʃa   (w→∅)
750: a voiceless fricative voices intervocalically (recurrence, after the diphthongs resolve)
    ˈn̪ɔ.t͡ʃa → ˈn̪ɔ.d͡ʒa   (t͡ʃ→d͡ʒ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈn̪ɔ.d͡ʒa → ˈn̪ɔ.d͡ʒə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈn̪ɔ.d͡ʒə → ˈn̪ɔ.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈn̪ɔ.ʒə → ˈn̪ɔʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈn̪ɔʒə̯ → ˈn̪ɔʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈn̪ɔʒ → n̪ɔʒ   (ˈɔ→ɔ)
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
1000: the velar fricative x is lost
    ˈn̪ɔx.t̪rə → ˈn̪ɔ.t̪rə   (x→∅)
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
1000: nasalized front mid vowels become nasalized a
    ˈɔr.n̪ə̃ˈmɛ̃n̪t̪ → ˈɔr.n̪ə̃ˈmãn̪t̪   (ˈɛ̃→ˈã)
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
-100: a segment marked both back and front loses the back specification
    ˈpɑɫ.mɑ → ˈpɑlʲ.mɑ   (ɫ→lʲ)
500: the low vowel fronts by default
    ˈpɑlʲ.mɑ → ˈpalʲ.ma   (ˈɑ→ˈa, ɑ→a)
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈpalʲ.ma → ˈpalʲ.ma.ə   (∅→ə)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈpalʲ.ma.ə → ˈpalʲ.mə.ə   (a→ə)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈpalʲ.mə.ə → ˈpaɫ.mə.ə   (lʲ→ɫ)
1000: back dark-l variants vocalize to w
    ˈpaɫ.mə.ə → ˈpaw.mə.ə   (ɫ→w)
1200: a stressless schwa desyllabifies before another vowel
    ˈpaw.mə.ə → ˈpaw.mə̯ə   (ə→ə̯)
1200: schwa desyllabifies after another vowel
    ˈpaw.mə̯ə → ˈpawmə̯ə̯   (ə→ə̯)
1200: aw becomes long oː
    ˈpawmə̯ə̯ → ˈpoːmə̯ə̯   (ˈaw→ˈoː)
1200: a non-syllabic schwa effaces after another vowel
    ˈpoːmə̯ə̯ → ˈpoːmə̯   (ə̯→∅)
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
1000: the velar fricative x is lost
    ˈpax.t̪rə → ˈpa.t̪rə   (x→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈpa.t̪rə → ˈpat̪rə̯   (ə→ə̯)
1400: the a backs to ɑ in words with a historical â (lost preconsonantal s)
    ˈpat̪rə̯ → ˈpɑt̪rə̯   (ˈa→ˈɑ)
1400: the final off-glide schwa is deleted elsewhere
    ˈpɑt̪rə̯ → ˈpɑt̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈpɑt̪r → ˈpɑt̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈpɑt̪ʀ → pɑt̪ʀ   (ˈɑ→ɑ)
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

`pˌeːn̪ikˈellum` → `pwa.so`

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
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˌpejn̪ˈt͡sʲɛll → ˌpejˈt͡sʲɛll   (n̪→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌpejˈt͡sʲɛll → ˌpejˈt͡sʲɛɫl   (l→ɫ)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌpejˈt͡sʲɛɫl → ˌpojˈt͡sʲɛɫl   (ˌe→ˌo)
1000: schwa is epenthesized word-finally after a back glide + lateral
    ˌpojˈt͡sʲɛɫl → ˌpojˈt͡sʲɛɫ.lə   (∅→ə)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌpojˈt͡sʲɛɫ.lə → ˌpujˈt͡sʲɛɫ.lə   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌpujˈt͡sʲɛɫ.lə → ˌpuɛ̯ˈt͡sʲɛɫ.lə   (j→ɛ̯)
1000: back dark-l variants vocalize to w
    ˌpuɛ̯ˈt͡sʲɛɫ.lə → ˌpuɛ̯ˈt͡sʲɛw.lə   (ɫ→w)
1000: the second half of a vocalized geminate l is lost
    ˌpuɛ̯ˈt͡sʲɛw.lə → ˌpuɛ̯ˈt͡sʲɛ.wə   (l→∅)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌpuɛ̯ˈt͡sʲɛ.wə → ˌpuɛ̯ˈt͡sʲɛa̯.wə   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌpuɛ̯ˈt͡sʲɛa̯.wə → ˌpuɛ̯ˈt͡sʲe̯a.wə   (ˈɛ→e̯, a̯→ˈa)
1000: all affricates become sibilants (deaffrication)
    ˌpuɛ̯ˈt͡sʲe̯a.wə → ˌpuɛ̯ˈsʲe̯a.wə   (t͡sʲ→sʲ)
1200: aw becomes long oː
    ˌpuɛ̯ˈsʲe̯a.wə → ˌpuɛ̯ˈsʲe̯oː.ə   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌpuɛ̯ˈsʲe̯oː.ə → ˌpuɛ̯ˈsʲə̯oː.ə   (e̯→ə̯)
1200: the remaining anterior palatalized consonants depalatalize
    ˌpuɛ̯ˈsʲə̯oː.ə → ˌpuɛ̯ˈsə̯oː.ə   (sʲ→s)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌpuɛ̯ˈsə̯oː.ə → ˌpwɛˈsə̯oː.ə   (ˌu→w, ɛ̯→ˌɛ)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌpwɛˈsə̯oː.ə → ˌpwɛˈsoː.ə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌpwɛˈsoː.ə → ˌpwɛˈsoːə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌpwɛˈsoːə̯ → ˌpwɛˈsoː   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌpwɛˈsoː → pwɛ.soː   (ˌɛ→ɛ, ˈoː→oː)
1400: distinctive vowel length is lost entirely
    pwɛ.soː → pwɛ.so   (oː→o)
1400: wɛ becomes wa
    pwɛ.so → pwa.so   (ɛ→a)
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
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˈpen̪.n̪ə → ˈpẽn̪.n̪ə   (ˈe→ˈẽ)
1000: nasalized front mid vowels begin to lower
    ˈpẽn̪.n̪ə → ˈpɛ̃n̪.n̪ə   (ˈẽ→ˈɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˈpɛ̃n̪.n̪ə → ˈpãn̪.n̪ə   (ˈɛ̃→ˈã)
1200: geminates simplify to single consonants
    ˈpãn̪.n̪ə → ˈpã.n̪ə   (n̪→∅)
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
1400: final obstruents are lost
    ˈplys → ˈply   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈply → ply   (ˈy→y)
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
1000: the velar fricative x is lost
    ˌprɛxˈt̪er → ˌprɛˈt̪er   (x→∅)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌprɛˈt̪er → ˌprɛˈt̪eɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌprɛˈt̪eɹ → ˌprɛˈt̪e   (ɹ→∅)
1400: r becomes uvular ʀ
    ˌprɛˈt̪e → ˌpʀɛˈt̪e   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpʀɛˈt̪e → pʀɛ.t̪e   (ˌɛ→ɛ, ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀɛ.t̪e → pʁɛ.t̪e   (ʀ→ʁ)
```

## première

`prˌimˈɑːriɑm` → `pʁɑ̃.bjɛʁ`

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
600: b epenthesized between m and a coronal non-nasal sonorant glide (recurrence)
    ˌpreˈmjɛː.ra → ˌpremˈbjɛː.ra   (∅→b)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌpremˈbjɛː.ra → ˌpremˈbjie̯.ra   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌpremˈbjie̯.ra → ˌpremˈbie̯.ra   (j→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpremˈbie̯.ra → ˌpremˈbie̯.rə   (a→ə)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌpremˈbie̯.rə → ˌprẽmˈbie̯.rə   (ˌe→ˌẽ)
1000: nasalized front mid vowels begin to lower
    ˌprẽmˈbie̯.rə → ˌprɛ̃mˈbie̯.rə   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌprɛ̃mˈbie̯.rə → ˌprãmˈbie̯.rə   (ˌɛ̃→ˌã)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌprãmˈbie̯.rə → ˌprãmˈbje.rə   (ˈi→j, e̯→ˈe)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌprãmˈbje.rə → ˌprãːˈbje.rə   (ˌãm→ˌãː)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˌprãːˈbje.rə → ˌprãːˈbjɛ.rə   (ˈe→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌprãːˈbjɛ.rə → ˌprãːˈbjɛrə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌprãːˈbjɛrə̯ → ˌprɑ̃ːˈbjɛrə̯   (ˌãː→ˌɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˌprɑ̃ːˈbjɛrə̯ → ˌprɑ̃ːˈbjɛr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌprɑ̃ːˈbjɛr → ˌpʀɑ̃ːˈbjɛʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpʀɑ̃ːˈbjɛʀ → pʀɑ̃ː.bjɛʀ   (ˌɑ̃ː→ɑ̃ː, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    pʀɑ̃ː.bjɛʀ → pʀɑ̃.bjɛʀ   (ɑ̃ː→ɑ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀɑ̃.bjɛʀ → pʁɑ̃.bjɛʁ   (ʀ→ʁ, ʀ→ʁ)
```

## pucelle

`pˌuːlikˈellɑm` → `py.lwa.zɛl`

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
600: non-syllabic schwa restores to schwa after a lateral, before an optional obstruent (+ optional schwa) + non-nasal coronal sonorant
    ˌpʉlə̯ˈt͡sʲɛl.la → ˌpʉ.ləˈt͡sʲɛl.la   (ə̯→ə)
600: a voiceless consonant voices intervocalically
    ˌpʉ.ləˈt͡sʲɛl.la → ˌpʉ.ləˈd͡zʲɛl.la   (t͡sʲ→d͡zʲ)
600: a voiced stop spirantizes intervocalically or before a non-nasal non-lateral sonorant
    ˌpʉ.ləˈd͡zʲɛl.la → ˌpʉ.ləˈzʲɛl.la   (d͡zʲ→zʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌpʉ.ləˈzʲɛl.la → ˌpʉ.ləjˈzɛl.la   (zʲ→jz)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpʉ.ləjˈzɛl.la → ˌpʉ.ləjˈzɛl.lə   (a→ə)
1000: unstressed schwa becomes e before a yod-like sonorant (j, ʎ, ɲ)
    ˌpʉ.ləjˈzɛl.lə → ˌpʉ.lejˈzɛl.lə   (ə→e)
1000: intervocalic geminate ll degeminates to a single l (before l-vocalization)
    ˌpʉ.lejˈzɛl.lə → ˌpʉ.lejˈzɛ.lə   (l→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌpʉ.lejˈzɛ.lə → ˌpy.lejˈzɛ.lə   (ˌʉ→ˌy)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˌpy.lejˈzɛ.lə → ˌpy.lojˈzɛ.lə   (e→o)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌpy.lojˈzɛ.lə → ˌpy.lujˈzɛ.lə   (o→u)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌpy.lujˈzɛ.lə → ˌpy.luɛ̯ˈzɛ.lə   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌpy.luɛ̯ˈzɛ.lə → ˌpy.lwɛˈzɛ.lə   (u→w, ɛ̯→ɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌpy.lwɛˈzɛ.lə → ˌpy.lwɛˈzɛlə̯   (ə→ə̯)
1400: a vowel lengthens before an intervocalic z
    ˌpy.lwɛˈzɛlə̯ → ˌpy.lwɛːˈzɛlə̯   (ɛ→ɛː)
1400: the final off-glide schwa is deleted elsewhere
    ˌpy.lwɛːˈzɛlə̯ → ˌpy.lwɛːˈzɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌpy.lwɛːˈzɛl → py.lwɛː.zɛl   (ˌy→y, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    py.lwɛː.zɛl → py.lwɛ.zɛl   (ɛː→ɛ)
1400: wɛ becomes wa
    py.lwɛ.zɛl → py.lwa.zɛl   (ɛ→a)
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

`rˌoːbˈiːkulɑm` → `ʁu.vij`

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
600: a stressed vowel lengthens before a consonant + vowel
    ˌroˈβi.ʎa → ˌroˈβiː.ʎa   (ˈi→ˈiː)
600: the remaining bilabial fricative becomes v
    ˌroˈβiː.ʎa → ˌroˈviː.ʎa   (β→v)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌroˈviː.ʎa → ˌroˈviː.ʎə   (a→ə)
750: vowel length resets to short
    ˌroˈviː.ʎə → ˌroˈvi.ʎə   (ˈiː→ˈi)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌroˈvi.ʎə → ˌruˈvi.ʎə   (ˌo→ˌu)
1400: final ə becomes a non-syllabic off-glide
    ˌruˈvi.ʎə → ˌruˈviʎə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌruˈviʎə̯ → ˌruˈviʎ   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌruˈviʎ → ˌʀuˈviʎ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʀuˈviʎ → ʀu.viʎ   (ˌu→u, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀu.viʎ → ʁu.viʎ   (ʀ→ʁ)
1400: ʎ becomes j
    ʁu.viʎ → ʁu.vij   (ʎ→j)
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
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈros.sə → ˈrus.sə   (ˈo→ˈu)
1000: s becomes x after a vowel, before any consonant
    ˈrus.sə → ˈrux.sə   (s→x)
1000: the velar fricative x is lost
    ˈrux.sə → ˈru.sə   (x→∅)
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

`sˌɑlin̪ˈɑːrium` → `sa.lə̃.je`

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
600: non-syllabic schwa restores before a front sonorant consonant
    ˌsalə̯ˈn̪jɛːrə̯ → ˌsa.ləˈn̪jɛːrə̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˌsa.ləˈn̪jɛːrə̯ → ˌsa.ləˈn̪jɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌsa.ləˈn̪jɛːr → ˌsa.ləˈn̪jie̯r   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌsa.ləˈn̪jie̯r → ˌsa.ləˈn̪ie̯r   (j→∅)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌsa.ləˈn̪ie̯r → ˌsa.lə̃ˈn̪ie̯r   (ə→ə̃)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌsa.lə̃ˈn̪ie̯r → ˌsa.lə̃ˈn̪jer   (ˈi→j, e̯→ˈe)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsa.lə̃ˈn̪jer → ˌsa.lə̃ːˈjer   (ə̃n̪→ə̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌsa.lə̃ːˈjer → ˌsa.lə̃ːˈjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌsa.lə̃ːˈjeɹ → ˌsa.lə̃ːˈje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌsa.lə̃ːˈje → sa.lə̃ː.je   (ˌa→a, ˈe→e)
1400: distinctive vowel length is lost entirely
    sa.lə̃ː.je → sa.lə̃.je   (ə̃ː→ə̃)
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
-100: a segment marked both back and front loses the back specification
    ˈsɑɫ.βʷo → ˈsɑlʲ.βʷo   (ɫ→lʲ)
500: labialized bilabial fricatives delabialize
    ˈsɑlʲ.βʷo → ˈsɑlʲ.βo   (βʷ→β)
500: the low vowel fronts by default
    ˈsɑlʲ.βo → ˈsalʲ.βo   (ˈɑ→ˈa)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsalʲ.βo → ˈsalʲ.βə   (o→ə)
600: schwa becomes non-syllabic
    ˈsalʲ.βə → ˈsalʲβə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈsalʲβə̯ → ˈsalʲβ   (ə̯→∅)
600: the remaining bilabial fricative becomes v
    ˈsalʲβ → ˈsalʲv   (β→v)
750: all final obstruents devoice
    ˈsalʲv → ˈsalʲf   (v→f)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈsalʲf → ˈsaɫf   (lʲ→ɫ)
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
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈsɑ.pe.d̪o → ˈsɑ.pe.ðo   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈsɑ.pe.ðo → ˈsɑː.pe.ðo   (ˈɑ→ˈɑː)
500: the low vowel fronts by default
    ˈsɑː.pe.ðo → ˈsaː.pe.ðo   (ˈɑː→ˈaː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈsaː.pe.ðo → ˈsaː.pə.ðo   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈsaː.pə.ðo → ˈsaː.pə.ðə   (o→ə)
600: schwa becomes non-syllabic
    ˈsaː.pə.ðə → ˈsaːpə̯ðə̯   (ə→ə̯, ə→ə̯)
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
600: a coronal palatalizes between two high-front segments
    ˈsie̯çs → ˈsii̯çs   (e̯→i̯)
750: ç merges into ʝ
    ˈsii̯çs → ˈsii̯ʝs   (ç→ʝ)
750: ʝ becomes j everywhere
    ˈsii̯ʝs → ˈsii̯js   (ʝ→j)
1000: a high non-round glide deletes after stressed i
    ˈsii̯js → ˈsijs   (i̯→∅)
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
600: non-syllabic schwa restores before a front sonorant consonant
    ˌseŋgə̯ˈlaːrə̯ → ˌseŋ.gəˈlaːrə̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˌseŋ.gəˈlaːrə̯ → ˌseŋ.gəˈlaːr   (ə̯→∅)
600: long stressed vowels diphthongize
    ˌseŋ.gəˈlaːr → ˌseŋ.gəˈlae̯r   (ˈaː→ˈae̯)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˌseŋ.gəˈlae̯r → ˌseŋ.gəˈleːr   (ˈae̯→ˈeː)
1000: a mid front vowel nasalizes before a nasal (second nasalization)
    ˌseŋ.gəˈleːr → ˌsẽŋ.gəˈleːr   (ˌe→ˌẽ)
1000: vowel length resets to short
    ˌsẽŋ.gəˈleːr → ˌsẽŋ.gəˈler   (ˈeː→ˈe)
1000: nasalized front mid vowels begin to lower
    ˌsẽŋ.gəˈler → ˌsɛ̃ŋ.gəˈler   (ˌẽ→ˌɛ̃)
1000: nasalized front mid vowels become nasalized a
    ˌsɛ̃ŋ.gəˈler → ˌsãŋ.gəˈler   (ˌɛ̃→ˌã)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌsãŋ.gəˈler → ˌsãː.gəˈler   (ˌãŋ→ˌãː)
1200: intertonic schwa effaces between a stressed consonant and r/l, before a later stressed syllable
    ˌsãː.gəˈler → ˌsãːˈgler   (ə→∅)
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
1000: the velar fricative x is lost
    ˌexˈpus → ˌeˈpus   (x→∅)
1400: final obstruents are lost
    ˌeˈpus → ˌeˈpu   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌeˈpu → e.pu   (ˌe→e, ˈu→u)
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
600: schwa epenthesized after a labial consonant + coronal, word-finally
    ˈsũm.ma → ˈsũm.ma.ə   (∅→ə)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈsũm.ma.ə → ˈsũm.mə.ə   (a→ə)
1200: geminates simplify to single consonants
    ˈsũm.mə.ə → ˈsũ.mə.ə   (m→∅)
1200: a stressless schwa desyllabifies before another vowel
    ˈsũ.mə.ə → ˈsũ.mə̯ə   (ə→ə̯)
1200: schwa desyllabifies after another vowel
    ˈsũ.mə̯ə → ˈsũmə̯ə̯   (ə→ə̯)
1200: a non-syllabic schwa effaces after another vowel
    ˈsũmə̯ə̯ → ˈsũmə̯   (ə̯→∅)
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
1000: the velar fricative x is lost
    ˌt̪ãmˈpɛx.t̪ə → ˌt̪ãmˈpɛ.t̪ə   (x→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌt̪ãmˈpɛ.t̪ə → ˌt̪ãːˈpɛ.t̪ə   (ˌãm→ˌãː)
1400: final ə becomes a non-syllabic off-glide
    ˌt̪ãːˈpɛ.t̪ə → ˌt̪ãːˈpɛt̪ə̯   (ə→ə̯)
1400: long a becomes back ɑː
    ˌt̪ãːˈpɛt̪ə̯ → ˌt̪ɑ̃ːˈpɛt̪ə̯   (ˌãː→ˌɑ̃ː)
1400: the final off-glide schwa is deleted elsewhere
    ˌt̪ɑ̃ːˈpɛt̪ə̯ → ˌt̪ɑ̃ːˈpɛt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌt̪ɑ̃ːˈpɛt̪ → t̪ɑ̃ː.pɛt̪   (ˌɑ̃ː→ɑ̃ː, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    t̪ɑ̃ː.pɛt̪ → t̪ɑ̃.pɛt̪   (ɑ̃ː→ɑ̃)
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
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˈt̪ɛ.pe.d̪o → ˈt̪ɛ.pe.ðo   (d̪→ð)
300: a stressed vowel lengthens before a single consonant + glide
    ˈt̪ɛ.pe.ðo → ˈt̪ɛː.pe.ðo   (ˈɛ→ˈɛː)
500: long stressed ɛː/ɔː diphthongize to ie̯/uo̯
    ˈt̪ɛː.pe.ðo → ˈt̪ie̯.pe.ðo   (ˈɛː→ˈie̯)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈt̪ie̯.pe.ðo → ˈt̪ie̯.pə.ðo   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪ie̯.pə.ðo → ˈt̪ie̯.pə.ðə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪ie̯.pə.ðə → ˈt̪ie̯pə̯ðə̯   (ə→ə̯, ə→ə̯)
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
-100: a segment marked both back and front loses the back specification
    ˌo.seˈt̪iɫ.ʝo → ˌo.seˈt̪ilʲ.ʝo   (ɫ→lʲ)
500: a voiceless fricative voices intervocalically
    ˌo.seˈt̪ilʲ.ʝo → ˌo.zeˈt̪ilʲ.ʝo   (s→z)
500: a lateral palatalizes before a high-front consonant
    ˌo.zeˈt̪ilʲ.ʝo → ˌo.zeˈt̪iʎ.ʝo   (lʲ→ʎ)
600: a yod is absorbed by a preceding palatal lateral (ʎj > ʎ)
    ˌo.zeˈt̪iʎ.ʝo → ˌo.zeˈt̪i.ʎo   (ʝ→∅)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌo.zeˈt̪i.ʎo → ˌo.zəˈt̪i.ʎə   (e→ə, o→ə)
600: schwa becomes non-syllabic
    ˌo.zəˈt̪i.ʎə → ˌozə̯ˈt̪iʎə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌozə̯ˈt̪iʎə̯ → ˌozˈt̪iʎ   (ˈə̯t̪iʎə̯→ˈt̪iʎ)
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
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈvan̪ˌn̪ɛll → ˈvan̪ˌn̪ɛɫl   (l→ɫ)
1000: a low vowel nasalizes before a nasal (first nasalization)
    ˈvan̪ˌn̪ɛɫl → ˈvãn̪ˌn̪ɛɫl   (ˈa→ˈã)
1000: schwa is epenthesized word-finally after a back glide + lateral
    ˈvãn̪ˌn̪ɛɫl → ˈvãn̪ˌn̪ɛɫ.lə   (∅→ə)
1000: back dark-l variants vocalize to w
    ˈvãn̪ˌn̪ɛɫ.lə → ˈvãn̪ˌn̪ɛw.lə   (ɫ→w)
1000: the second half of a vocalized geminate l is lost
    ˈvãn̪ˌn̪ɛw.lə → ˈvãn̪ˌn̪ɛ.wə   (l→∅)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˈvãn̪ˌn̪ɛ.wə → ˈvãn̪ˌn̪ɛa̯.wə   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈvãn̪ˌn̪ɛa̯.wə → ˈvãn̪ˌn̪e̯a.wə   (ˌɛ→e̯, a̯→ˌa)
1200: geminates simplify to single consonants
    ˈvãn̪ˌn̪e̯a.wə → ˈvãˌn̪e̯a.wə   (n̪→∅)
1200: aw becomes long oː
    ˈvãˌn̪e̯a.wə → ˈvãˌn̪e̯oː.ə   (ˌaw→ˌoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˈvãˌn̪e̯oː.ə → ˈvãˌn̪ə̯oː.ə   (e̯→ə̯)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˈvãˌn̪ə̯oː.ə → ˈvãˌn̪oː.ə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈvãˌn̪oː.ə → ˈvãˌn̪oːə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈvãˌn̪oːə̯ → ˈvãˌn̪oː   (ə̯→∅)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˈvãˌn̪oː → ˈvaˌn̪oː   (ˈã→ˈa)
1400: stress is leveled — no longer distinctive for vowels
    ˈvaˌn̪oː → va.n̪oː   (ˈa→a, ˌoː→oː)
1400: distinctive vowel length is lost entirely
    va.n̪oː → va.n̪o   (oː→o)
```

## vautre

`wˈelt̪rɑgum` → `vid̪ʁ`

```
-100: j/w harden to fricative-like consonants before a vowel (not in a falling diphthong)
    ˈwel.t̪rɑ.gum → ˈɣʷel.t̪rɑ.gum   (w→ɣʷ)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈɣʷel.t̪rɑ.gum → ˈɣʷɛl.t̪rɑ.gʊm   (ˈe→ˈɛ, u→ʊ)
-100: l darkens before a non-lateral consonant
    ˈɣʷɛl.t̪rɑ.gʊm → ˈɣʷɛɫ.t̪rɑ.gʊm   (l→ɫ)
-100: posttonic non-low vowel syncopates between l and r + vowel
    ˈɣʷɛɫ.t̪rɑ.gʊm → ˈɣʷɛ.ɫrɑ.gʊm   (t̪→∅)
-100: any remaining labiovelar approximant becomes a labialized voiced bilabial fricative
    ˈɣʷɛ.ɫrɑ.gʊm → ˈβʷɛ.ɫrɑ.gʊm   (ɣʷ→βʷ)
-100: unstressed g deleted between an unstressed vowel and the following unstressed syllable
    ˈβʷɛ.ɫrɑ.gʊm → ˈβʷɛ.ɫrʊm   (ɑg→∅)
-100: lax high vowels lower to tense mid vowels
    ˈβʷɛ.ɫrʊm → ˈβʷɛ.ɫrom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈβʷɛ.ɫrom → ˈβʷɛ.ɫro   (m→∅)
-100: a segment marked both back and front loses the back specification
    ˈβʷɛ.ɫro → ˈβʷɛ.lʲro   (ɫ→lʲ)
500: d epenthesized between a lateral and r
    ˈβʷɛ.lʲro → ˈβʷɛlʲ.d̪ro   (∅→d̪)
500: labialized bilabial fricatives delabialize
    ˈβʷɛlʲ.d̪ro → ˈβɛlʲ.d̪ro   (βʷ→β)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈβɛlʲ.d̪ro → ˈβɛlʲ.d̪ʲro   (d̪→d̪ʲ)
500: short stressed ɛ/ɔ also diphthongize before a high-front consonant
    ˈβɛlʲ.d̪ʲro → ˈβie̯lʲ.d̪ʲro   (ˈɛ→ˈie̯)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈβie̯lʲ.d̪ʲro → ˈβie̯lʲ.d̪ʲrə   (o→ə)
600: schwa becomes non-syllabic
    ˈβie̯lʲ.d̪ʲrə → ˈβie̯lʲd̪ʲrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈβie̯lʲd̪ʲrə̯ → ˈβie̯lʲd̪ʲr   (ə̯→∅)
600: schwa epenthesized after an obstruent + sonorant consonant, before optional consonants + word end
    ˈβie̯lʲd̪ʲr → ˈβie̯lʲ.d̪ʲrə   (∅→ə)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈβie̯lʲ.d̪ʲrə → ˈβie̯lʲ.d̪ʲrʲə   (r→rʲ)
600: palatalized r depalatalizes
    ˈβie̯lʲ.d̪ʲrʲə → ˈβie̯lʲ.d̪ʲrə   (rʲ→r)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈβie̯lʲ.d̪ʲrə → ˈβie̯lʲj.d̪rə   (d̪ʲ→jd̪)
600: j is lost after j or a consonant, before a consonant
    ˈβie̯lʲj.d̪rə → ˈβie̯lʲ.d̪rə   (j→∅)
600: a coronal palatalizes between two high-front segments
    ˈβie̯lʲ.d̪rə → ˈβii̯lʲ.d̪rə   (e̯→i̯)
600: a palatalized consonant depalatalizes after a front tense non-low vowel + a high segment
    ˈβii̯lʲ.d̪rə → ˈβii̯l.d̪rə   (lʲ→l)
600: the remaining bilabial fricative becomes v
    ˈβii̯l.d̪rə → ˈvii̯l.d̪rə   (β→v)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈvii̯l.d̪rə → ˈvii̯ɫ.d̪rə   (l→ɫ)
1000: dark l becomes ʎ after a front unrounded high vowel
    ˈvii̯ɫ.d̪rə → ˈvii̯ʎ.d̪rə   (ɫ→ʎ)
1000: a high non-round glide deletes after stressed i
    ˈvii̯ʎ.d̪rə → ˈviʎ.d̪rə   (i̯→∅)
1000: ʎ effaces between an i-variant and a consonant
    ˈviʎ.d̪rə → ˈvi.d̪rə   (ʎ→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈvi.d̪rə → ˈvid̪rə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈvid̪rə̯ → ˈvid̪r   (ə̯→∅)
1400: r becomes uvular ʀ
    ˈvid̪r → ˈvid̪ʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈvid̪ʀ → vid̪ʀ   (ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    vid̪ʀ → vid̪ʁ   (ʀ→ʁ)
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

`wˈet̪ulus` → `vi`

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
600: a coronal palatalizes between two high-front segments
    ˈβie̯ʎs → ˈβii̯ʎs   (e̯→i̯)
600: s affricates after a high-front sonorant consonant, word-finally
    ˈβii̯ʎs → ˈβii̯ʎt͡sʲ   (s→t͡sʲ)
600: the remaining bilabial fricative becomes v
    ˈβii̯ʎt͡sʲ → ˈvii̯ʎt͡sʲ   (β→v)
1000: a high non-round glide deletes after stressed i
    ˈvii̯ʎt͡sʲ → ˈviʎt͡sʲ   (i̯→∅)
1000: ʎ effaces between an i-variant and a consonant
    ˈviʎt͡sʲ → ˈvit͡sʲ   (ʎ→∅)
1000: all affricates become sibilants (deaffrication)
    ˈvit͡sʲ → ˈvisʲ   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˈvisʲ → ˈvis   (sʲ→s)
1400: final obstruents are lost
    ˈvis → ˈvi   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈvi → vi   (ˈi→i)
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
1000: intervocalic geminate ll degeminates to a single l (before l-vocalization)
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
1000: s becomes x after a vowel, before any consonant
    ˌab.bəˈðes.sə → ˌab.bəˈðex.sə   (s→x)
1000: the interdental fricatives (plain and palatalized) efface
    ˌab.bəˈðex.sə → ˌab.bəˈex.sə   (ð→∅)
1000: the velar fricative x is lost
    ˌab.bəˈex.sə → ˌab.bəˈe.sə   (x→∅)
1200: geminates simplify to single consonants
    ˌab.bəˈe.sə → ˌa.bəˈe.sə   (b→∅)
1200: a stressless schwa desyllabifies before another vowel
    ˌa.bəˈe.sə → ˌaˈbə̯e.sə   (ə→ə̯)
1400: a stressed vowel lengthens after a non-syllabic schwa
    ˌaˈbə̯e.sə → ˌaˈbə̯eː.sə   (ˈe→ˈeː)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌaˈbə̯eː.sə → ˌaˈbeː.sə   (ə̯→∅)
1400: long e:/je: lower to ɛ:/jɛ: before a single consonant + coda (or ə)
    ˌaˈbeː.sə → ˌaˈbɛː.sə   (ˈeː→ˈɛː)
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
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌarˈt͡sʲɛll → ˌarˈt͡sʲɛɫl   (l→ɫ)
1000: schwa is epenthesized word-finally after a back glide + lateral
    ˌarˈt͡sʲɛɫl → ˌarˈt͡sʲɛɫ.lə   (∅→ə)
1000: back dark-l variants vocalize to w
    ˌarˈt͡sʲɛɫ.lə → ˌarˈt͡sʲɛw.lə   (ɫ→w)
1000: the second half of a vocalized geminate l is lost
    ˌarˈt͡sʲɛw.lə → ˌarˈt͡sʲɛ.wə   (l→∅)
1000: a glide develops between a stressed or secondary-stressed lax front mid vowel and w
    ˌarˈt͡sʲɛ.wə → ˌarˈt͡sʲɛa̯.wə   (∅→a̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌarˈt͡sʲɛa̯.wə → ˌarˈt͡sʲe̯a.wə   (ˈɛ→e̯, a̯→ˈa)
1000: all affricates become sibilants (deaffrication)
    ˌarˈt͡sʲe̯a.wə → ˌarˈsʲe̯a.wə   (t͡sʲ→sʲ)
1200: aw becomes long oː
    ˌarˈsʲe̯a.wə → ˌarˈsʲe̯oː.ə   (ˈaw→ˈoː)
1200: the e-glide becomes a schwa-glide before a non-high round back vowel
    ˌarˈsʲe̯oː.ə → ˌarˈsʲə̯oː.ə   (e̯→ə̯)
1200: the remaining anterior palatalized consonants depalatalize
    ˌarˈsʲə̯oː.ə → ˌarˈsə̯oː.ə   (sʲ→s)
1400: a non-syllabic schwa is lost before a vowel/glide
    ˌarˈsə̯oː.ə → ˌarˈsoː.ə   (ə̯→∅)
1400: final ə becomes a non-syllabic off-glide
    ˌarˈsoː.ə → ˌarˈsoːə̯   (ə→ə̯)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌarˈsoːə̯ → ˌaɹˈsoːə̯   (r→ɹ)
1400: the final off-glide schwa is deleted elsewhere
    ˌaɹˈsoːə̯ → ˌaɹˈsoː   (ə̯→∅)
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
600: a palatal stop affricates to a postalveolar affricate
    ˈɟɔw.d͡ʒa → ˈd͡ʒɔw.d͡ʒa   (ɟ→d͡ʒ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈd͡ʒɔw.d͡ʒa → ˈd͡ʒɔ.d͡ʒa   (w→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈd͡ʒɔ.d͡ʒa → ˈd͡ʒɔ.d͡ʒə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒɔ.d͡ʒə → ˈʒɔ.ʒə   (d͡ʒ→ʒ, d͡ʒ→ʒ)
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
1400: final obstruents are lost
    ˈkys → ˈky   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈky → ky   (ˈy→y)
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
500: the back high continuant obstruent (x) fronts before a coronal
    ˈliː.ɣa → ˈliː.ʝa   (ɣ→ʝ)
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
-100: a segment marked both back and front loses the back specification
    ˌmɛˈd̪ɑɫ.ʝɑ → ˌmɛˈd̪ɑlʲ.ʝɑ   (ɫ→lʲ)
300: a voiced stop lenites to a continuant intervocalically or before a non-nasal sonorant
    ˌmɛˈd̪ɑlʲ.ʝɑ → ˌmɛˈðɑlʲ.ʝɑ   (d̪→ð)
500: a lateral palatalizes before a high-front consonant
    ˌmɛˈðɑlʲ.ʝɑ → ˌmɛˈðɑʎ.ʝɑ   (lʲ→ʎ)
500: the low vowel fronts by default
    ˌmɛˈðɑʎ.ʝɑ → ˌmɛˈðaʎ.ʝa   (ˈɑ→ˈa, ɑ→a)
600: a yod is absorbed by a preceding palatal lateral (ʎj > ʎ)
    ˌmɛˈðaʎ.ʝa → ˌmɛˈða.ʎa   (ʝ→∅)
600: a stressed vowel lengthens before a consonant + vowel
    ˌmɛˈða.ʎa → ˌmɛˈðaː.ʎa   (ˈa→ˈaː)
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

`n̪ˌɑwikˈellɑm` → `n̪wa.sɛl`

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
600: w becomes j after a round vowel before tsʲ
    ˌn̪ɔwˈt͡sʲɛl.la → ˌn̪ɔjˈt͡sʲɛl.la   (w→j)
600: secondary-stressed ɔ raises to o unconditionally
    ˌn̪ɔjˈt͡sʲɛl.la → ˌn̪ojˈt͡sʲɛl.la   (ˌɔ→ˌo)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌn̪ojˈt͡sʲɛl.la → ˌn̪ojˈt͡sʲɛl.lə   (a→ə)
1000: intervocalic geminate ll degeminates to a single l (before l-vocalization)
    ˌn̪ojˈt͡sʲɛl.lə → ˌn̪ojˈt͡sʲɛ.lə   (l→∅)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌn̪ojˈt͡sʲɛ.lə → ˌn̪ujˈt͡sʲɛ.lə   (ˌo→ˌu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌn̪ujˈt͡sʲɛ.lə → ˌn̪uɛ̯ˈt͡sʲɛ.lə   (j→ɛ̯)
1000: all affricates become sibilants (deaffrication)
    ˌn̪uɛ̯ˈt͡sʲɛ.lə → ˌn̪uɛ̯ˈsʲɛ.lə   (t͡sʲ→sʲ)
1200: the remaining anterior palatalized consonants depalatalize
    ˌn̪uɛ̯ˈsʲɛ.lə → ˌn̪uɛ̯ˈsɛ.lə   (sʲ→s)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌn̪uɛ̯ˈsɛ.lə → ˌn̪wɛˈsɛ.lə   (ˌu→w, ɛ̯→ˌɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌn̪wɛˈsɛ.lə → ˌn̪wɛˈsɛlə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌn̪wɛˈsɛlə̯ → ˌn̪wɛˈsɛl   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌn̪wɛˈsɛl → n̪wɛ.sɛl   (ˌɛ→ɛ, ˈɛ→ɛ)
1400: wɛ becomes wa
    n̪wɛ.sɛl → n̪wa.sɛl   (ɛ→a)
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
600: non-syllabic schwa restores before a front sonorant consonant
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
1400: final obstruents are lost
    ˌãˈmis → ˌãˈmi   (s→∅)
1400: nasalized ã (and wɛ̃, jɛ̃) denasalizes before a nasal consonant + vowel
    ˌãˈmi → ˌaˈmi   (ˌã→ˌa)
1400: stress is leveled — no longer distinctive for vowels
    ˌaˈmi → a.mi   (ˌa→a, ˈi→i)
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

`d̪ˈigit̪um` → `d̪wat̪`

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
300: a stressed vowel lengthens before a single consonant + glide
    ˈd̪e.ʝe.t̪o → ˈd̪eː.ʝe.t̪o   (ˈe→ˈeː)
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈd̪eː.ʝe.t̪o → ˈd̪eː.ʝə.t̪o   (e→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈd̪eː.ʝə.t̪o → ˈd̪eː.ʝə.t̪ə   (o→ə)
600: schwa becomes non-syllabic
    ˈd̪eː.ʝə.t̪ə → ˈd̪eːʝə̯t̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores after another non-syllabic schwa + optional consonants, word-finally
    ˈd̪eːʝə̯t̪ə̯ → ˈd̪eːʝə̯.t̪ə   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈd̪eːʝə̯.t̪ə → ˈd̪eːʝ.t̪ə   (ə̯→∅)
600: an anterior non-lateral coronal palatalizes after a high-front consonant (recurrence)
    ˈd̪eːʝ.t̪ə → ˈd̪eːʝ.t̪ʲə   (t̪→t̪ʲ)
600: a vowel shortens before a consonant cluster ending in an obstruent
    ˈd̪eːʝ.t̪ʲə → ˈd̪eʝ.t̪ʲə   (ˈeː→ˈe)
600: ʝ weakens to j unconditionally
    ˈd̪eʝ.t̪ʲə → ˈd̪ej.t̪ʲə   (ʝ→j)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈd̪ej.t̪ʲə → ˈd̪ejj.t̪ə   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˈd̪ejj.t̪ə → ˈd̪ej.t̪ə   (j→∅)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈd̪ej.t̪ə → ˈd̪oj.t̪ə   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈd̪oj.t̪ə → ˈd̪uj.t̪ə   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈd̪uj.t̪ə → ˈd̪uɛ̯.t̪ə   (j→ɛ̯)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈd̪uɛ̯.t̪ə → ˈd̪wɛ.t̪ə   (ˈu→w, ɛ̯→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈd̪wɛ.t̪ə → ˈd̪wɛt̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈd̪wɛt̪ə̯ → ˈd̪wɛt̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈd̪wɛt̪ → d̪wɛt̪   (ˈɛ→ɛ)
1400: wɛ becomes wa
    d̪wɛt̪ → d̪wat̪   (ɛ→a)
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
-100: a segment marked both back and front loses the back specification
    ˈfɑɫ.sɑ → ˈfɑlʲ.sɑ   (ɫ→lʲ)
500: the low vowel fronts by default
    ˈfɑlʲ.sɑ → ˈfalʲ.sa   (ˈɑ→ˈa, ɑ→a)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˈfalʲ.sa → ˈfalʲ.sʲa   (s→sʲ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈfalʲ.sʲa → ˈfalʲj.sa   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˈfalʲj.sa → ˈfalʲ.sa   (j→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈfalʲ.sa → ˈfalʲ.sə   (a→ə)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˈfalʲ.sə → ˈfaɫ.sə   (lʲ→ɫ)
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
-100: a segment marked both back and front loses the back specification
    ˈfiɫ.ʝɑ → ˈfilʲ.ʝɑ   (ɫ→lʲ)
500: a lateral palatalizes before a high-front consonant
    ˈfilʲ.ʝɑ → ˈfiʎ.ʝɑ   (lʲ→ʎ)
500: the low vowel fronts by default
    ˈfiʎ.ʝɑ → ˈfiʎ.ʝa   (ɑ→a)
600: a yod is absorbed by a preceding palatal lateral (ʎj > ʎ)
    ˈfiʎ.ʝa → ˈfi.ʎa   (ʝ→∅)
600: a stressed vowel lengthens before a consonant + vowel
    ˈfi.ʎa → ˈfiː.ʎa   (ˈi→ˈiː)
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
1000: the velar fricative x is lost
    ˌfɔˈrɛxt̪ → ˌfɔˈrɛt̪   (x→∅)
1400: final obstruents are lost
    ˌfɔˈrɛt̪ → ˌfɔˈrɛ   (t̪→∅)
1400: r becomes uvular ʀ
    ˌfɔˈrɛ → ˌfɔˈʀɛ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌfɔˈʀɛ → fɔ.ʀɛ   (ˌɔ→ɔ, ˈɛ→ɛ)
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
750: d/t plus s becomes the affricate ts
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
1000: s becomes x after a vowel, before any consonant
    ˈgrɔss → ˈgrɔxs   (s→x)
1000: the velar fricative x is lost
    ˈgrɔxs → ˈgrɔs   (x→∅)
1400: final obstruents are lost
    ˈgrɔs → ˈgrɔ   (s→∅)
1400: r becomes uvular ʀ
    ˈgrɔ → ˈgʀɔ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈgʀɔ → gʀɔ   (ˈɔ→ɔ)
1400: word-final ɔ raises to o
    gʀɔ → gʀo   (ɔ→o)
1400: the uvular trill ʀ becomes a fricative ʁ
    gʀo → gʁo   (ʀ→ʁ)
```

## janvier

`iˌɑːn̪uˈɑːrium` → `ʒə̃.je`

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
500: w lost after a non-back consonant
    ˌʝaˈn̪wa.rʲo → ˌʝaˈn̪a.rʲo   (w→∅)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌʝaˈn̪a.rʲo → ˌʝaˈn̪aː.rʲo   (ˈa→ˈaː)
500: secondary-stressed a becomes ɛ after a front consonant, before a nasal + long vowel
    ˌʝaˈn̪aː.rʲo → ˌʝɛˈn̪aː.rʲo   (ˌa→ˌɛ)
600: yod hardens to ɟ word-initially before a vowel
    ˌʝɛˈn̪aː.rʲo → ˌɟɛˈn̪aː.rʲo   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˌɟɛˈn̪aː.rʲo → ˌd͡ʒɛˈn̪aː.rʲo   (ɟ→d͡ʒ)
600: aːrʲ metathesizes to jɛːr
    ˌd͡ʒɛˈn̪aː.rʲo → ˌd͡ʒɛˈn̪jɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌd͡ʒɛˈn̪jɛː.ro → ˌd͡ʒɛˈn̪jɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌd͡ʒɛˈn̪jɛː.rə → ˌd͡ʒɛˈn̪jɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌd͡ʒɛˈn̪jɛːrə̯ → ˌd͡ʒɛˈn̪jɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌd͡ʒɛˈn̪jɛːr → ˌd͡ʒɛˈn̪jie̯r   (ˈɛː→ˈie̯)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌd͡ʒɛˈn̪jie̯r → ˌd͡ʒɛˈn̪ie̯r   (j→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌd͡ʒɛˈn̪ie̯r → ˌd͡ʒeˈn̪ie̯r   (ˌɛ→ˌe)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌd͡ʒeˈn̪ie̯r → ˌd͡ʒəˈn̪ie̯r   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌd͡ʒəˈn̪ie̯r → ˌd͡ʒə̃ˈn̪ie̯r   (ˌə→ˌə̃)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌd͡ʒə̃ˈn̪ie̯r → ˌd͡ʒə̃ˈn̪jer   (ˈi→j, e̯→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˌd͡ʒə̃ˈn̪jer → ˌʒə̃ˈn̪jer   (d͡ʒ→ʒ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌʒə̃ˈn̪jer → ˌʒə̃ːˈjer   (ˌə̃n̪→ˌə̃ː)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌʒə̃ːˈjer → ˌʒə̃ːˈjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌʒə̃ːˈjeɹ → ˌʒə̃ːˈje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌʒə̃ːˈje → ʒə̃ː.je   (ˌə̃ː→ə̃ː, ˈe→e)
1400: distinctive vowel length is lost entirely
    ʒə̃ː.je → ʒə̃.je   (ə̃ː→ə̃)
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
600: an anterior coronal voices after a non-high voiced labial consonant, before a voiced segment
    ˈd͡ʒʉo̯βsˈd̪iːɪ̯ → ˈd͡ʒʉo̯βzˈd̪iːɪ̯   (s→z)
600: the bilabial fricative becomes w before a non-labial obstruent
    ˈd͡ʒʉo̯βzˈd̪iːɪ̯ → ˈd͡ʒʉo̯wzˈd̪iːɪ̯   (β→w)
750: vowel length resets to short
    ˈd͡ʒʉo̯wzˈd̪iːɪ̯ → ˈd͡ʒʉo̯wzˈd̪iɪ̯   (ˈiː→ˈi)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈd͡ʒʉo̯wzˈd̪iɪ̯ → ˈd͡ʒʉo̯wˈd̪iɪ̯   (z→∅)
1000: high round back vowels front (completion of u-fronting)
    ˈd͡ʒʉo̯wˈd̪iɪ̯ → ˈd͡ʒyo̯wˈd̪iɪ̯   (ˈʉ→ˈy)
1000: the diphthong uo becomes ue
    ˈd͡ʒyo̯wˈd̪iɪ̯ → ˈd͡ʒye̯wˈd̪iɪ̯   (o̯→e̯)
1000: a high non-round glide deletes after stressed i
    ˈd͡ʒye̯wˈd̪iɪ̯ → ˈd͡ʒye̯wˈd̪i   (ɪ̯→∅)
1000: the e-glide rounds to ø before a back sonorant (or ɫ)
    ˈd͡ʒye̯wˈd̪i → ˈd͡ʒyø̯wˈd̪i   (e̯→ø̯)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈd͡ʒyø̯wˈd̪i → ˈd͡ʒɥøwˈd̪i   (ˈy→ɥ, ø̯→ˈø)
1000: ɥ delabializes to j before a front rounded mid vowel (ɥø > jø)
    ˈd͡ʒɥøwˈd̪i → ˈd͡ʒjøwˈd̪i   (ɥ→j)
1000: the yod is lost after d͡ʒ before a front rounded mid vowel
    ˈd͡ʒjøwˈd̪i → ˈd͡ʒøwˈd̪i   (j→∅)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈd͡ʒøwˈd̪i → ˈd͡ʒøˈd̪i   (w→∅)
1000: all affricates become sibilants (deaffrication)
    ˈd͡ʒøˈd̪i → ˈʒøˈd̪i   (d͡ʒ→ʒ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʒøˈd̪i → ʒø.d̪i   (ˈø→ø, ˈi→i)
```

## chamois

`kˌɑmˈoːxsum` → `ʃə̃.wa`

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
500: secondary-stressed a becomes ɛ after a front consonant, before a non-coronal non-consonantal segment
    ˌkʲaˈmoç.sʲo → ˌkʲɛˈmoç.sʲo   (ˌa→ˌɛ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˌkʲɛˈmoç.sʲo → ˌcɛˈmoç.sʲo   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˌcɛˈmoç.sʲo → ˌt͡ʃɛˈmoç.sʲo   (c→t͡ʃ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌt͡ʃɛˈmoç.sʲo → ˌt͡ʃɛˈmoç.sʲə   (o→ə)
600: schwa becomes non-syllabic
    ˌt͡ʃɛˈmoç.sʲə → ˌt͡ʃɛˈmoçsʲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌt͡ʃɛˈmoçsʲə̯ → ˌt͡ʃɛˈmoçsʲ   (ə̯→∅)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌt͡ʃɛˈmoçsʲ → ˌt͡ʃɛˈmoçjs   (sʲ→js)
600: j is lost after j or a consonant, before a consonant
    ˌt͡ʃɛˈmoçjs → ˌt͡ʃɛˈmoçs   (j→∅)
600: secondary-stressed ɛ raises to e before any two segments
    ˌt͡ʃɛˈmoçs → ˌt͡ʃeˈmoçs   (ˌɛ→ˌe)
750: ç merges into ʝ
    ˌt͡ʃeˈmoçs → ˌt͡ʃeˈmoʝs   (ç→ʝ)
750: ʝ becomes j everywhere
    ˌt͡ʃeˈmoʝs → ˌt͡ʃeˈmojs   (ʝ→j)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌt͡ʃeˈmojs → ˌt͡ʃəˈmojs   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌt͡ʃəˈmojs → ˌt͡ʃə̃ˈmojs   (ˌə→ˌə̃)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌt͡ʃə̃ˈmojs → ˌt͡ʃə̃ˈmujs   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˌt͡ʃə̃ˈmujs → ˌt͡ʃə̃ˈmuɛ̯s   (j→ɛ̯)
1000: all affricates become sibilants (deaffrication)
    ˌt͡ʃə̃ˈmuɛ̯s → ˌʃə̃ˈmuɛ̯s   (t͡ʃ→ʃ)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˌʃə̃ˈmuɛ̯s → ˌʃə̃ˈmwɛs   (ˈu→w, ɛ̯→ˈɛ)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌʃə̃ˈmwɛs → ˌʃə̃ːˈwɛs   (ˌə̃m→ˌə̃ː)
1400: final obstruents are lost
    ˌʃə̃ːˈwɛs → ˌʃə̃ːˈwɛ   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌʃə̃ːˈwɛ → ʃə̃ː.wɛ   (ˌə̃ː→ə̃ː, ˈɛ→ɛ)
1400: distinctive vowel length is lost entirely
    ʃə̃ː.wɛ → ʃə̃.wɛ   (ə̃ː→ə̃)
1400: wɛ becomes wa
    ʃə̃.wɛ → ʃə̃.wa   (ɛ→a)
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
600: a segment marked both back and front loses the back specification (recurrence)
    ˈkʲaː.ra → ˈcaː.ra   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈcaː.ra → ˈt͡ʃaː.ra   (c→t͡ʃ)
600: long stressed vowels diphthongize
    ˈt͡ʃaː.ra → ˈt͡ʃae̯.ra   (ˈaː→ˈae̯)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈt͡ʃae̯.ra → ˈt͡ʃae̯.rə   (a→ə)
750: the ae̯ diphthong monophthongizes to a long e, preserving its stress level
    ˈt͡ʃae̯.rə → ˈt͡ʃeː.rə   (ˈae̯→ˈeː)
1000: vowel length resets to short
    ˈt͡ʃeː.rə → ˈt͡ʃe.rə   (ˈeː→ˈe)
1000: all affricates become sibilants (deaffrication)
    ˈt͡ʃe.rə → ˈʃe.rə   (t͡ʃ→ʃ)
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
600: long stressed vowels diphthongize
    ˈkoː.pla → ˈkow.pla   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈkow.pla → ˈko.pla   (w→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈko.pla → ˈko.plə   (a→ə)
750: p voices to b after a vowel, before a continuant non-nasal sonorant
    ˈko.plə → ˈko.blə   (p→b)
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

`lˈɑwkkɑm` → `lɔʒ`

```
-100: word-final nasal consonant lost after an unstressed vowel
    ˈlɑwk.kɑm → ˈlɑwk.kɑ   (m→∅)
300: a stop is deleted internal to a cluster, before a high stop
    ˈlɑwk.kɑ → ˈlɑw.kɑ   (k→∅)
500: the low vowel fronts by default
    ˈlɑw.kɑ → ˈlaw.ka   (ˈɑ→ˈa, ɑ→a)
500: the high back consonant w fronts before a front vowel
    ˈlaw.ka → ˈlaw.kʲa   (k→kʲ)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈlaw.kʲa → ˈlɔw.kʲa   (ˈa→ˈɔ)
600: a segment marked both back and front loses the back specification (recurrence)
    ˈlɔw.kʲa → ˈlɔw.ca   (kʲ→c)
600: a palatal stop affricates to a postalveolar affricate
    ˈlɔw.ca → ˈlɔw.t͡ʃa   (c→t͡ʃ)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈlɔw.t͡ʃa → ˈlɔ.t͡ʃa   (w→∅)
750: a voiceless fricative voices intervocalically (recurrence, after the diphthongs resolve)
    ˈlɔ.t͡ʃa → ˈlɔ.d͡ʒa   (t͡ʃ→d͡ʒ)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlɔ.d͡ʒa → ˈlɔ.d͡ʒə   (a→ə)
1000: all affricates become sibilants (deaffrication)
    ˈlɔ.d͡ʒə → ˈlɔ.ʒə   (d͡ʒ→ʒ)
1400: final ə becomes a non-syllabic off-glide
    ˈlɔ.ʒə → ˈlɔʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlɔʒə̯ → ˈlɔʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlɔʒ → lɔʒ   (ˈɔ→ɔ)
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

`mˌed̪iˈɑːn̪ɑm` → `me.jɛn̪`

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
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˌmeˈjie̯.n̪ə → ˌmejˈje.n̪ə   (ˈi→j, e̯→ˈe)
1200: geminates simplify to single consonants
    ˌmejˈje.n̪ə → ˌmeˈje.n̪ə   (j→∅)
1200: any remaining vowel nasalizes before a nasal consonant (recurrence)
    ˌmeˈje.n̪ə → ˌmeˈjẽ.n̪ə   (ˈe→ˈẽ)
1400: nasalized ẽ lowers to ɛ̃
    ˌmeˈjẽ.n̪ə → ˌmeˈjɛ̃.n̪ə   (ˈẽ→ˈɛ̃)
1400: the open front nasal ɛ̃ (and œ̃) denasalizes before a nasal consonant + vowel
    ˌmeˈjɛ̃.n̪ə → ˌmeˈjɛ.n̪ə   (ˈɛ̃→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˌmeˈjɛ.n̪ə → ˌmeˈjɛn̪ə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌmeˈjɛn̪ə̯ → ˌmeˈjɛn̪   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌmeˈjɛn̪ → me.jɛn̪   (ˌe→e, ˈɛ→ɛ)
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
1000: intervocalic geminate ll degeminates to a single l (before l-vocalization)
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

`pˈeːn̪silem` → `pwaz`

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
600: non-syllabic schwa restores before a front sonorant consonant
    ˈpeːzə̯lə̯ → ˈpeː.zələ̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈpeː.zələ̯ → ˈpeː.zəl   (ə̯→∅)
600: long stressed vowels diphthongize
    ˈpeː.zəl → ˈpej.zəl   (ˈeː→ˈej)
1000: a short tense front mid/high vowel backs and rounds before yod
    ˈpej.zəl → ˈpoj.zəl   (ˈe→ˈo)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈpoj.zəl → ˈpuj.zəl   (ˈo→ˈu)
1000: the yod of a back-round diphthong lowers to ɛ̯ everywhere (oj/uj > oɛ̯/uɛ̯)
    ˈpuj.zəl → ˈpuɛ̯.zəl   (j→ɛ̯)
1200: a single final consonant effaces after schwa
    ˈpuɛ̯.zəl → ˈpuɛ̯.zə   (l→∅)
1200: the diphthong oɛ̯ completes its shift to wɛ
    ˈpuɛ̯.zə → ˈpwɛ.zə   (ˈu→w, ɛ̯→ˈɛ)
1400: final ə becomes a non-syllabic off-glide
    ˈpwɛ.zə → ˈpwɛzə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈpwɛzə̯ → ˈpwɛz   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈpwɛz → pwɛz   (ˈɛ→ɛ)
1400: wɛ becomes wa
    pwɛz → pwaz   (ɛ→a)
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
600: an identical consonant geminate reduces to one, before a consonant + consonant-or-boundary
    ˈplat̪t̪s → ˈplat̪s   (t̪→∅)
750: d/t plus s becomes the affricate ts
    ˈplat̪s → ˈplat͡s   (t̪s→t͡s)
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
500: a voiceless fricative voices intervocalically
    ˌprɛˈt͡sʲɑː.rɛ → ˌprɛˈd͡zʲɑː.rɛ   (t͡sʲ→d͡zʲ)
500: the low vowel fronts by default
    ˌprɛˈd͡zʲɑː.rɛ → ˌprɛˈd͡zʲaː.rɛ   (ˈɑː→ˈaː)
600: a voiced stop spirantizes intervocalically or before r
    ˌprɛˈd͡zʲaː.rɛ → ˌprɛˈzʲaː.rɛ   (d͡zʲ→zʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌprɛˈzʲaː.rɛ → ˌprɛˈzʲaː.rə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌprɛˈzʲaː.rə → ˌprɛˈzʲaːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌprɛˈzʲaːrə̯ → ˌprɛˈzʲaːr   (ə̯→∅)
600: a stressed low vowel becomes front non-tense after a front continuant glide, before a sonorant non-lateral consonant
    ˌprɛˈzʲaːr → ˌprɛˈzʲɛːr   (ˈaː→ˈɛː)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌprɛˈzʲɛːr → ˌprɛˈzʲie̯r   (ˈɛː→ˈie̯)
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
1400: final obstruents are lost
    ˈres → ˈre   (s→∅)
1400: r becomes uvular ʀ
    ˈre → ˈʀe   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈʀe → ʀe   (ˈe→e)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀe → ʁe   (ʀ→ʁ)
```

## rumeur

`rˌuːmˈoːrem` → `ʁy.muʁ`

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
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˌrʉˈmowr → ˌrʉˈmor   (w→∅)
1000: high round back vowels front (completion of u-fronting)
    ˌrʉˈmor → ˌryˈmor   (ˌʉ→ˌy)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌryˈmor → ˌrỹˈmor   (ˌy→ˌỹ)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˌrỹˈmor → ˌrỹˈmur   (ˈo→ˈu)
1200: nasalized high front ĩ denasalizes before a nasal consonant + glide
    ˌrỹˈmur → ˌryˈmur   (ˌỹ→ˌy)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌryˈmur → ˌryˈmuɹ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌryˈmuɹ → ˌryˈmur   (ɹ→r)
1400: r becomes uvular ʀ
    ˌryˈmur → ˌʀyˈmuʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌʀyˈmuʀ → ʀy.muʀ   (ˌy→y, ˈu→u)
1400: the uvular trill ʀ becomes a fricative ʁ
    ʀy.muʀ → ʁy.muʁ   (ʀ→ʁ, ʀ→ʁ)
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
-100: a segment marked both back and front loses the back specification
    ˌsɑɫˈt̪wɑr.ʝo → ˌsɑlʲˈt̪wɑr.ʝo   (ɫ→lʲ)
500: r + yod becomes palatalized r
    ˌsɑlʲˈt̪wɑr.ʝo → ˌsɑlʲˈt̪wɑ.rʲo   (rʝ→rʲ)
500: the low vowel fronts by default
    ˌsɑlʲˈt̪wɑ.rʲo → ˌsalʲˈt̪wa.rʲo   (ˌɑ→ˌa, ˈɑ→ˈa)
500: w lost after a non-back consonant
    ˌsalʲˈt̪wa.rʲo → ˌsalʲˈt̪a.rʲo   (w→∅)
500: an anterior non-lateral coronal palatalizes after a high-front consonant
    ˌsalʲˈt̪a.rʲo → ˌsalʲˈt̪ʲa.rʲo   (t̪→t̪ʲ)
500: a stressed vowel lengthens before an optional consonant + vowel (recurrence)
    ˌsalʲˈt̪ʲa.rʲo → ˌsalʲˈt̪ʲaː.rʲo   (ˈa→ˈaː)
600: aːrʲ metathesizes to jɛːr
    ˌsalʲˈt̪ʲaː.rʲo → ˌsalʲˈt̪ʲjɛː.ro   (ˈaːrʲ→ˈjɛːr)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsalʲˈt̪ʲjɛː.ro → ˌsalʲˈt̪ʲjɛː.rə   (o→ə)
600: schwa becomes non-syllabic
    ˌsalʲˈt̪ʲjɛː.rə → ˌsalʲˈt̪ʲjɛːrə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsalʲˈt̪ʲjɛːrə̯ → ˌsalʲˈt̪ʲjɛːr   (ə̯→∅)
600: long stressed ɛː/ɔː diphthongize (recurrence)
    ˌsalʲˈt̪ʲjɛːr → ˌsalʲˈt̪ʲjie̯r   (ˈɛː→ˈie̯)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˌsalʲˈt̪ʲjie̯r → ˌsalʲjˈt̪jie̯r   (t̪ʲ→jt̪)
600: j is lost after j or a consonant, before a consonant
    ˌsalʲjˈt̪jie̯r → ˌsalʲˈt̪jie̯r   (j→∅)
600: a coronal palatalizes between two high-front segments
    ˌsalʲˈt̪jie̯r → ˌsalʲˈt̪ʲjie̯r   (t̪→t̪ʲ)
600: j lost after a consonant before a high front unrounded sonorant + e-glide
    ˌsalʲˈt̪ʲjie̯r → ˌsalʲˈt̪ʲie̯r   (j→∅)
1000: l darkens before a consonant (beginnings of l-vocalization)
    ˌsalʲˈt̪ʲie̯r → ˌsaɫˈt̪ʲie̯r   (lʲ→ɫ)
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
500: a voiceless fricative voices intervocalically
    ˌsɑˈt͡sʲoː.n̪ɛ → ˌsɑˈd͡zʲoː.n̪ɛ   (t͡sʲ→d͡zʲ)
500: a round non-high vowel becomes tense, high, and nasalized before a nasal
    ˌsɑˈd͡zʲoː.n̪ɛ → ˌsɑˈd͡zʲũː.n̪ɛ   (ˈoː→ˈũː)
500: the low vowel fronts by default
    ˌsɑˈd͡zʲũː.n̪ɛ → ˌsaˈd͡zʲũː.n̪ɛ   (ˌɑ→ˌa)
600: a voiced stop spirantizes intervocalically or before r
    ˌsaˈd͡zʲũː.n̪ɛ → ˌsaˈzʲũː.n̪ɛ   (d͡zʲ→zʲ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsaˈzʲũː.n̪ɛ → ˌsaˈzʲũː.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˌsaˈzʲũː.n̪ə → ˌsaˈzʲũːn̪ə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˌsaˈzʲũːn̪ə̯ → ˌsaˈzʲũːn̪   (ə̯→∅)
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
600: a voiceless anterior consonant voices before a coronal sonorant non-nasal consonant
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
1000: the velar fricative x is lost
    ˌexˌkyˈjer → ˌeˌkyˈjer   (x→∅)
1200: yj becomes ɥi (the y desyllabifies, the yod becomes the nucleus)
    ˌeˌkyˈjer → ˌeˌkɥiˈer   (ˌy→ɥ, j→ˌi)
1400: j is inserted between a back-conditioned ɥi and a following vowel
    ˌeˌkɥiˈer → ˌeˌkɥiˈjer   (∅→j)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌeˌkɥiˈjer → ˌeˌkɥiˈjeɹ   (r→ɹ)
1400: final ɹ effaces after a monosyllabic e(ː) or a we(ː) nucleus
    ˌeˌkɥiˈjeɹ → ˌeˌkɥiˈje   (ɹ→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˌeˌkɥiˈje → e.kɥi.je   (ˌe→e, ˌi→i, ˈe→e)
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
1000: the velar fricative x is lost
    ˌexˈt̪ɛ̃j̃m → ˌeˈt̪ɛ̃j̃m   (x→∅)
1200: j̃ deletes before a nasalized non-tense front vowel
    ˌeˈt̪ɛ̃j̃m → ˌeˈt̪ɛ̃m   (j̃→∅)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌeˈt̪ɛ̃m → ˌeˈt̪ɛ̃ː   (ˈɛ̃m→ˈɛ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˌeˈt̪ɛ̃ː → e.t̪ɛ̃ː   (ˌe→e, ˈɛ̃ː→ɛ̃ː)
1400: distinctive vowel length is lost entirely
    e.t̪ɛ̃ː → e.t̪ɛ̃   (ɛ̃ː→ɛ̃)
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

`t̪rˈɑwkum` → `t̪ʁo`

```
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈt̪rɑw.kum → ˈt̪rɑw.kʊm   (u→ʊ)
-100: lax high vowels lower to tense mid vowels
    ˈt̪rɑw.kʊm → ˈt̪rɑw.kom   (ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    ˈt̪rɑw.kom → ˈt̪rɑw.ko   (m→∅)
500: the low vowel fronts by default
    ˈt̪rɑw.ko → ˈt̪raw.ko   (ˈɑ→ˈa)
500: a becomes ɔ before the high back round glide (w), at any stress level
    ˈt̪raw.ko → ˈt̪rɔw.ko   (ˈa→ˈɔ)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈt̪rɔw.ko → ˈt̪rɔw.kə   (o→ə)
600: schwa becomes non-syllabic
    ˈt̪rɔw.kə → ˈt̪rɔwkə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈt̪rɔwkə̯ → ˈt̪rɔwk   (ə̯→∅)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈt̪rɔwk → ˈt̪rɔk   (w→∅)
750: a word-final stop re-opens to a fricative after a vowel
    ˈt̪rɔk → ˈt̪rɔx   (k→x)
750: x closes to k word-finally after a stressed back vowel
    ˈt̪rɔx → ˈt̪rɔk   (x→k)
1400: final obstruents are lost
    ˈt̪rɔk → ˈt̪rɔ   (k→∅)
1400: r becomes uvular ʀ
    ˈt̪rɔ → ˈt̪ʀɔ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈt̪ʀɔ → t̪ʀɔ   (ˈɔ→ɔ)
1400: word-final ɔ raises to o
    t̪ʀɔ → t̪ʀo   (ɔ→o)
1400: the uvular trill ʀ becomes a fricative ʁ
    t̪ʀo → t̪ʁo   (ʀ→ʁ)
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
