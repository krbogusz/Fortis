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

`ˈjuwen̪em` → `ju.və̃`

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
600: an unstressed non-low vowel reduces to schwa before consonants + vowel + optional consonants + word end
    ˈʝoː.βɛ.n̪ɛ → ˈʝoː.βə.n̪ɛ   (ɛ→ə)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈʝoː.βə.n̪ɛ → ˈʝoː.βə.n̪ə   (ɛ→ə)
600: schwa becomes non-syllabic
    ˈʝoː.βə.n̪ə → ˈʝoːβə̯n̪ə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores before a front sonorant consonant
    ˈʝoːβə̯n̪ə̯ → ˈʝoː.βən̪ə̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˈʝoː.βən̪ə̯ → ˈʝoː.βən̪   (ə̯→∅)
600: ʝ weakens to j unconditionally
    ˈʝoː.βən̪ → ˈjoː.βən̪   (ʝ→j)
600: long stressed vowels diphthongize
    ˈjoː.βən̪ → ˈjow.βən̪   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈjow.βən̪ → ˈjo.βən̪   (w→∅)
600: the remaining bilabial fricative becomes v
    ˈjo.βən̪ → ˈjo.vən̪   (β→v)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈjo.vən̪ → ˈjo.və̃n̪   (ə→ə̃)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈjo.və̃n̪ → ˈju.və̃n̪   (ˈo→ˈu)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈju.və̃n̪ → ˈju.və̃ː   (ə̃n̪→ə̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈju.və̃ː → ju.və̃ː   (ˈu→u)
1400: distinctive vowel length is lost entirely
    ju.və̃ː → ju.və̃   (ə̃ː→ə̃)
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

`kˈolpoːs` → `kɥœs`

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
1000: the e-glide rounds to ø before a back sonorant (or ɫ)
    ˈkye̯ɫ.sə → ˈkyø̯ɫ.sə   (e̯→ø̯)
1000: back dark-l variants vocalize to w
    ˈkyø̯ɫ.sə → ˈkyø̯w.sə   (ɫ→w)
1000: diphthongs shift their stress onto the second element (ie̯ > je, ɛa̯ > e̯a, yø̯ > ɥø)
    ˈkyø̯w.sə → ˈkɥøw.sə   (ˈy→ɥ, ø̯→ˈø)
1000: øw becomes ø (the back-round glide is absorbed after ø)
    ˈkɥøw.sə → ˈkɥø.sə   (w→∅)
1400: final ə becomes a non-syllabic off-glide
    ˈkɥø.sə → ˈkɥøsə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈkɥøsə̯ → ˈkɥøs   (ə̯→∅)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈkɥøs → ˈkɥœs   (ˈø→ˈœ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkɥœs → kɥœs   (ˈœ→œ)
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

`kˈorium` → `kœjʁ`

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
1000: the stressed diphthong ye̯ (from ue̯) monophthongizes to ø
    ˈkye̯jr → ˈkøjr   (ˈye̯→ˈø)
1400: front round ø opens to œ before a coda consonant in the final syllable
    ˈkøjr → ˈkœjr   (ˈø→ˈœ)
1400: r becomes uvular ʀ
    ˈkœjr → ˈkœjʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˈkœjʀ → kœjʀ   (ˈœ→œ)
1400: the uvular trill ʀ becomes a fricative ʁ
    kœjʀ → kœjʁ   (ʀ→ʁ)
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

`kˈun̪eum` → `kɔn̪`

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
1200: final ɲ becomes n
    ˈkũj̃ɲ → ˈkũj̃n̪   (ɲ→n̪)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈkũj̃n̪ → ˈkũːn̪   (ˈũj̃→ˈũː)
1400: stress is leveled — no longer distinctive for vowels
    ˈkũːn̪ → kũːn̪   (ˈũː→ũː)
1400: distinctive vowel length is lost entirely
    kũːn̪ → kũn̪   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    kũn̪ → kɔ̃n̪   (ũ→ɔ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    kɔ̃n̪ → kɔn̪   (ɔ̃→ɔ)
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

`lˈɑt̪iɑm` → `lɛʒ`

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
500: a voiceless fricative voices before yod + a non-consonantal segment
    ˈlɑt͡sʲ.ʝɑ → ˈlɑd͡zʲ.ʝɑ   (t͡sʲ→d͡zʲ)
500: the low vowel fronts by default
    ˈlɑd͡zʲ.ʝɑ → ˈlad͡zʲ.ʝa   (ˈɑ→ˈa, ɑ→a)
600: yod hardens to ɟ word-medially after one or more consonants, before a vowel
    ˈlad͡zʲ.ʝa → ˈlad͡zʲ.ɟa   (ʝ→ɟ)
600: a palatal stop affricates to a postalveolar affricate
    ˈlad͡zʲ.ɟa → ˈlad͡zʲ.d͡ʒa   (ɟ→d͡ʒ)
600: a palatalized consonant moves its palatalization onto a preceding j
    ˈlad͡zʲ.d͡ʒa → ˈlajd͡z.d͡ʒa   (d͡zʲ→jd͡z)
750: an unstressed a reduces to schwa, word-medially or finally
    ˈlajd͡z.d͡ʒa → ˈlajd͡z.d͡ʒə   (a→ə)
750: a medial consonant/glide is lost between two consonants, before an obstruent (not l/r)
    ˈlajd͡z.d͡ʒə → ˈlaj.d͡ʒə   (d͡z→∅)
1000: all affricates become sibilants (deaffrication)
    ˈlaj.d͡ʒə → ˈlaj.ʒə   (d͡ʒ→ʒ)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˈlaj.ʒə → ˈlɛː.ʒə   (ˈaj→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˈlɛː.ʒə → ˈlɛːʒə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˈlɛːʒə̯ → ˈlɛːʒ   (ə̯→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈlɛːʒ → lɛːʒ   (ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    lɛːʒ → lɛʒ   (ɛː→ɛ)
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
1400: a yod is absorbed after a high front vowel word-finally or before a consonant
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
    ˌn̪uˈe → n̪u̯e   (ˌu→u̯, ˈe→e)
1400: stress is leveled — no longer distinctive for vowels
    n̪u̯e → n̪u̯e   (e→e)
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

`prˌimˈɑːriɑm` → `pʁə.mɛʁ`

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
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˌpreˈmaː.rʲa → ˌpreˈmaːj.rʲa   (∅→j)
600: palatalized r depalatalizes
    ˌpreˈmaːj.rʲa → ˌpreˈmaːj.ra   (rʲ→r)
600: long stressed vowels diphthongize
    ˌpreˈmaːj.ra → ˌpreˈmae̯j.ra   (ˈaː→ˈae̯)
600: the e-glide is lost after stressed a before a front sonorant glide
    ˌpreˈmae̯j.ra → ˌpreˈmaj.ra   (e̯→∅)
750: an unstressed a reduces to schwa, word-medially or finally
    ˌpreˈmaj.ra → ˌpreˈmaj.rə   (a→ə)
1000: secondary-stressed e reduces to schwa in an open syllable
    ˌpreˈmaj.rə → ˌprəˈmaj.rə   (ˌe→ˌə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌprəˈmaj.rə → ˌprə̃ˈmaj.rə   (ˌə→ˌə̃)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌprə̃ˈmaj.rə → ˌprə̃ˈmɛː.rə   (ˈaj→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˌprə̃ˈmɛː.rə → ˌprə̃ˈmɛːrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌprə̃ˈmɛːrə̯ → ˌprə̃ˈmɛːr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌprə̃ˈmɛːr → ˌpʀə̃ˈmɛːʀ   (r→ʀ, r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpʀə̃ˈmɛːʀ → pʀə̃.mɛːʀ   (ˌə̃→ə̃, ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    pʀə̃.mɛːʀ → pʀə̃.mɛʀ   (ɛː→ɛ)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    pʀə̃.mɛʀ → pʀə.mɛʀ   (ə̃→ə)
1400: the uvular trill ʀ becomes a fricative ʁ
    pʀə.mɛʀ → pʁə.mɛʁ   (ʀ→ʁ, ʀ→ʁ)
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

`pˌun̪kt̪ˈuːrɑm` → `pɔ̃.t̪yʁ`

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
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˌpũj̃ˈt̪y.rə → ˌpũːˈt̪y.rə   (ˌũj̃→ˌũː)
1400: final ə becomes a non-syllabic off-glide
    ˌpũːˈt̪y.rə → ˌpũːˈt̪yrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌpũːˈt̪yrə̯ → ˌpũːˈt̪yr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌpũːˈt̪yr → ˌpũːˈt̪yʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌpũːˈt̪yʀ → pũː.t̪yʀ   (ˌũː→ũː, ˈy→y)
1400: distinctive vowel length is lost entirely
    pũː.t̪yʀ → pũ.t̪yʀ   (ũː→ũ)
1400: nasal ũ opens to ɔ̃
    pũ.t̪yʀ → pɔ̃.t̪yʀ   (ũ→ɔ̃)
1400: the uvular trill ʀ becomes a fricative ʁ
    pɔ̃.t̪yʀ → pɔ̃.t̪yʁ   (ʀ→ʁ)
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

`rˌoːbˈiːkulɑm` → `ʁu.vi`

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
1400: a yod is absorbed after a high front vowel word-finally or before a consonant
    ʁu.vij → ʁu.vi   (j→∅)
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

`sˌɑlin̪ˈɑːrium` → `sa.lə.n̪ɛʁ`

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
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˌsa.ləˈn̪aː.rʲo → ˌsa.ləˈn̪aː.rʲə   (o→ə)
600: schwa becomes non-syllabic
    ˌsa.ləˈn̪aː.rʲə → ˌsalə̯ˈn̪aːrʲə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa restores before a front sonorant consonant
    ˌsalə̯ˈn̪aːrʲə̯ → ˌsa.ləˈn̪aːrʲə̯   (ə̯→ə)
600: non-syllabic schwa is lost elsewhere
    ˌsa.ləˈn̪aːrʲə̯ → ˌsa.ləˈn̪aːrʲ   (ə̯→∅)
600: j epenthesized after a non-consonantal segment directly before palatalized r
    ˌsa.ləˈn̪aːrʲ → ˌsa.ləˈn̪aːjrʲ   (∅→j)
600: palatalized r depalatalizes
    ˌsa.ləˈn̪aːjrʲ → ˌsa.ləˈn̪aːjr   (rʲ→r)
600: a vowel shortens before two or more non-syllabic segments + word end (recurrence)
    ˌsa.ləˈn̪aːjr → ˌsa.ləˈn̪ajr   (ˈaː→ˈa)
750: schwa is epenthesized word-finally after a low vowel + j + r
    ˌsa.ləˈn̪ajr → ˌsa.ləˈn̪aj.rə   (∅→ə)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˌsa.ləˈn̪aj.rə → ˌsa.lə̃ˈn̪aj.rə   (ə→ə̃)
1200: final ajə (and aj before a consonant) becomes long ɛː
    ˌsa.lə̃ˈn̪aj.rə → ˌsa.lə̃ˈn̪ɛː.rə   (ˈaj→ˈɛː)
1400: final ə becomes a non-syllabic off-glide
    ˌsa.lə̃ˈn̪ɛː.rə → ˌsa.lə̃ˈn̪ɛːrə̯   (ə→ə̯)
1400: the final off-glide schwa is deleted elsewhere
    ˌsa.lə̃ˈn̪ɛːrə̯ → ˌsa.lə̃ˈn̪ɛːr   (ə̯→∅)
1400: r becomes uvular ʀ
    ˌsa.lə̃ˈn̪ɛːr → ˌsa.lə̃ˈn̪ɛːʀ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌsa.lə̃ˈn̪ɛːʀ → sa.lə̃.n̪ɛːʀ   (ˌa→a, ˈɛː→ɛː)
1400: distinctive vowel length is lost entirely
    sa.lə̃.n̪ɛːʀ → sa.lə̃.n̪ɛʀ   (ɛː→ɛ)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    sa.lə̃.n̪ɛʀ → sa.lə.n̪ɛʀ   (ə̃→ə)
1400: the uvular trill ʀ becomes a fricative ʁ
    sa.lə.n̪ɛʀ → sa.lə.n̪ɛʁ   (ʀ→ʁ)
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
1400: a yod is absorbed after a high front vowel word-finally or before a consonant
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

`spˈon̪sum` → `spu`

```
-100: vowel lengthens before ns when the next syllable is unstressed
    ˈspon̪.sum → ˈspoːn̪.sum   (ˈo→ˈoː)
-100: n lost after a long vowel before s (compensatory lengthening already applied)
    ˈspoːn̪.sum → ˈspoː.sum   (n̪→∅)
-100: Classical Latin length distinction becomes a quality (tense) distinction, first pass
    ˈspoː.sum → ˈspoː.sʊm   (u→ʊ)
-100: i-prosthesis before word-initial s + consonant
    ˈspoː.sʊm → ɪsˈpoː.sʊm   (∅→ɪ)
-100: the length feature is dropped now that quality carries the contrast
    ɪsˈpoː.sʊm → ɪsˈpo.sʊm   (ˈoː→ˈo)
-100: lax high vowels lower to tense mid vowels
    ɪsˈpo.sʊm → esˈpo.som   (ɪ→e, ʊ→o)
-100: word-final nasal consonant lost after an unstressed vowel
    esˈpo.som → esˈpo.so   (m→∅)
300: a stressed vowel lengthens before a single consonant + glide
    esˈpo.so → esˈpoː.so   (ˈo→ˈoː)
500: a voiceless fricative voices intervocalically
    esˈpoː.so → esˈpoː.zo   (s→z)
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    esˈpoː.zo → əsˈpoː.zə   (e→ə, o→ə)
600: schwa becomes non-syllabic
    əsˈpoː.zə → ˈə̯spoːzə̯   (ə→ə̯, ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈə̯spoːzə̯ → ˈspoːz   (ˈə̯spoːzə̯→ˈspoːz)
600: long stressed vowels diphthongize
    ˈspoːz → ˈspowz   (ˈoː→ˈow)
600: the high back round glide is lost after a lax round vowel, before a non-front non-syllabic segment, a strident, or a non-syllabic sonorant
    ˈspowz → ˈspoz   (w→∅)
750: all final obstruents devoice
    ˈspoz → ˈspos   (z→s)
1000: round tense back vowels raise to u (o > u, oi > ui)
    ˈspos → ˈspus   (ˈo→ˈu)
1400: final obstruents are lost
    ˈspus → ˈspu   (s→∅)
1400: stress is leveled — no longer distinctive for vowels
    ˈspu → spu   (ˈu→u)
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
1400: a yod is absorbed after a high front vowel word-finally or before a consonant
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

`wˌermˈikulum` → `vɛ.ʁmi`

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
1000: intertonic e raises to i before a palatal consonant (ɲ, ʎ)
    ˌverˈmeʎ → ˌverˈmiʎ   (ˈe→ˈi)
1000: a stressed mid unrounded vowel laxes and fronts before r + consonant
    ˌverˈmiʎ → ˌvɛrˈmiʎ   (ˌe→ˌɛ)
1400: r loses its trill and becomes the approximant ɹ intervocalically/preconsonantally
    ˌvɛrˈmiʎ → ˌvɛɹˈmiʎ   (r→ɹ)
1400: the approximant ɹ reasserts as a trill r wherever it was not deleted
    ˌvɛɹˈmiʎ → ˌvɛrˈmiʎ   (ɹ→r)
1400: r becomes uvular ʀ
    ˌvɛrˈmiʎ → ˌvɛʀˈmiʎ   (r→ʀ)
1400: stress is leveled — no longer distinctive for vowels
    ˌvɛʀˈmiʎ → vɛʀ.miʎ   (ˌɛ→ɛ, ˈi→i)
1400: the uvular trill ʀ becomes a fricative ʁ
    vɛʀ.miʎ → vɛ.ʁmiʎ   (ʀ→ʁ)
1400: ʎ becomes j
    vɛ.ʁmiʎ → vɛ.ʁmij   (ʎ→j)
1400: a yod is absorbed after a high front vowel word-finally or before a consonant
    vɛ.ʁmij → vɛ.ʁmi   (j→∅)
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

`iˈuːn̪ium` → `jœn̪`

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
600: an unstressed non-low non-nasalized vowel reduces to schwa before a consonant or word end
    ˈʝʉː.ɲo → ˈʝʉː.ɲə   (o→ə)
600: schwa becomes non-syllabic
    ˈʝʉː.ɲə → ˈʝʉːɲə̯   (ə→ə̯)
600: non-syllabic schwa is lost elsewhere
    ˈʝʉːɲə̯ → ˈʝʉːɲ   (ə̯→∅)
600: ʝ weakens to j unconditionally
    ˈʝʉːɲ → ˈjʉːɲ   (ʝ→j)
600: a vowel shortens before ɲ
    ˈjʉːɲ → ˈjʉɲ   (ˈʉː→ˈʉ)
1000: high round back vowels front (completion of u-fronting)
    ˈjʉɲ → ˈjyɲ   (ˈʉ→ˈy)
1000: word-final ɲ ejects a nasalized j after a tense vowel
    ˈjyɲ → ˈjyj̃ɲ   (∅→j̃)
1000: any remaining vowel nasalizes before a nasal consonant (general nasalization)
    ˈjyj̃ɲ → ˈjỹj̃ɲ   (ˈy→ˈỹ)
1200: final ɲ becomes n
    ˈjỹj̃ɲ → ˈjỹj̃n̪   (ɲ→n̪)
1200: a nasal consonant effaces praeconsonantally (or finally) after a nasal vowel, lengthening it
    ˈjỹj̃n̪ → ˈjỹːn̪   (ˈỹj̃→ˈỹː)
1400: nasalized front vowels lower (wẽ, jẽ, ø̃ open to wɛ̃, jɛ̃, œ̃)
    ˈjỹːn̪ → ˈjœ̃ːn̪   (ˈỹː→ˈœ̃ː)
1400: stress is leveled — no longer distinctive for vowels
    ˈjœ̃ːn̪ → jœ̃ːn̪   (ˈœ̃ː→œ̃ː)
1400: distinctive vowel length is lost entirely
    jœ̃ːn̪ → jœ̃n̪   (œ̃ː→œ̃)
1400: a nasal vowel denasalizes before a surviving nasal consonant
    jœ̃n̪ → jœn̪   (œ̃→œ)
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
