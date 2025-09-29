---
title: Padauk - Font Features
fontversion: 6.000
---

Padauk is an OpenType-enabled font family that supports the Myanmar (Burmese) script. It includes a number of optional features that may be useful or required for particular uses or languages. This document lists all the available features.

These OpenType features are primarily specified using four-letter tags (e.g. 'ss01'). For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features).

*Please note that Graphite support has been removed in the current release, but continues to be available in the version 5.100 fonts. See our [Previous Versions archive](https://software.sil.org/padauk/download/previous-versions).*

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Padauk as a web font see *../web/Padauk-webfont-example.html* in the font package *web* folder. For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

[MyanmarWeb](http://enabling-languages.github.io/myanmarweb/fonts-padauk.html) also documents how to use the fonts on the web.

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Complete feature list

### Language system tags

#### Sgaw <a id="ksw"></a>

<span class='affects'>Affects: U+1037</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>ရ့ ရံ့ ကှ့</span> |
Sgaw | <span class='padauk-R normal' lang='ksw'>ရ့ ရံ့ ကှ့</span> | `lang='ksw'`

#### Khamti <a id="kht"></a>

<span class='affects'>Affects: U+1036 U+1038 U+1087 U+1088 U+1089 U+108A U+109A U+109B U+AA7B U+1086</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>ံ း ႇ ႈ ႉ ႊ ႚ ႛ ꩻ ႆ</span> |
Khamti | <span class='padauk-R normal' lang='kht'>ံ း ႇ ႈ ႉ ႊ ႚ ႛ ꩻ ႆ</span> | `lang='kht'`

#### Kayah <a id="kyu"></a>

<span class='affects'>Affects: U+103E U+102F U+1030 U+1061 U+1066 U+103D</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>ှ ှု ှူ ၡ ၦ တွ ျွ ြွ ွှ</span> |
Kayah | <span class='padauk-R normal' lang='kyu'>ှ ှု ှူ ၡ ၦ တွ ျွ ြွ ွှ</span> | `lang='kyu'`

#### Shan <a id="shn"></a>

<span class='affects'>Affects: U+103D</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>တွ ျွ ြွ ွှ</span> |
Shan | <span class='padauk-R normal' lang='shn'>တွ ျွ ြွ ွှ</span> | `lang='shn'`

#### Asho Chin <a id="csh"></a>

<span class='affects'>Affects: U+106D</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>ကၭ</span> |
Asho Chin | <span class='padauk-R normal' lang='csh'>ကၭ</span> | `lang='csh'`

#### Aiton or Phake <a id="aio"></a><a id="phk"></a>

<span class='affects'>Affects: U+1000 U+1075 U+AA61 U+107A U+1010 U+AA6B U+1078 U+101A U+AA7A U+101C U+AA6D U+1022 U+103C U+AA77 U+1036 U+1038 U+1087 U+1088 U+1089 U+108A U+109A U+109B U+AA7B U+1086</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>က︀ ၵ︀ ꩡ︀ ၺ တ︀ ꩫ︀ ၸ︀ ယ︀ ꩺ လ︀ ꩭ ဢ︀ ြ ꩷︀ ံ း ႇ ႈ ႉ ႊ ႚ ႛ ꩻ ႆ</span> |
Aiton or Phake | <span class='padauk-R normal' lang='aio'>က︀ ၵ︀ ꩡ︀ ၺ တ︀ ꩫ︀ ၸ︀ ယ︀ ꩺ လ︀ ꩭ ဢ︀ ြ ꩷︀ ံ း ႇ ႈ ႉ ႊ ႚ ႛ ꩻ ႆ</span> | `lang='aio'` or `lang='phk'`

#### Tai Laing <a id="tjl"></a>

<span class='affects'>Affects: U+AA6C</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>ꩬ</span> |
Tai Laing | <span class='padauk-R normal' lang='tjl'>ꩬ</span> | `lang='tjl'`

#### Thai Mon <a id="mnw"></a>

<span class='affects'>Affects: U+1003 U+100B U+100C U+100D U+100E U+1012 U+1014 U+101E U+1020 U+1021 U+1023 U+103F U+1049 U+104A U+104B U+104B.kinzi (U+105A, U+103A, U+1039)</span>

Language | Sample | Language setting
------- | ---------------------------- | -------
Default | <span class='padauk-R normal'>ဃ ဋ ဌ ဍ ဎ ဒ န သ ဠ အ ဣ ဿ ၉ ၊ ။ ၚ်္</span> |
Thai Mon | <span class='padauk-R normal' lang='mnw-TH'>ဃ ဋ ဌ ဍ ဎ ဒ န သ ဠ အ ဣ ဿ ၉ ၊ ။ ၚ်္</span> | `lang='mnw-TH'`

### Character and stylistic alternates

#### Filled dots <a id="cv01"></a><a id="ss01"></a>

<span class='affects'>Affects: U+1036 U+1038 U+1087 U+1088 U+1089 U+108A U+109A U+109B U+AA7B</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>ံ း ႇ ႈ ႉ ႊ ႚ ႛ ꩻ</span> | `cv01=0` or `ss01=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv01" 1'>ံ း ႇ ႈ ႉ ႊ ႚ ႛ ꩻ</span> | `cv01=1` or `ss01=1`

#### Tear drop style washwe <a id="cv02"></a><a id="ss02"></a>

<span class='affects'>Affects: U+103D</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>တွ ျွ ြွ ွှ</span> | `cv02=0` or `ss02=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv02" 1'>တွ ျွ ြွ ွှ</span> | `cv02=1` or `ss02=1`

#### Asho Chin variants <a id="cv03"></a><a id="ss03"></a>

<span class='affects'>Affects: U+106D</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>ကၭ</span> | `cv03=0` or `ss03=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv03" 1'>ကၭ</span> | `cv03=1` or `ss03=1`

#### Thai Mon variants <a id="cv04"></a><a id="ss04"></a>

<span class='affects'>Affects: U+1003 U+100B U+100C U+100D U+100E U+1012 U+1014 U+101E U+1020 U+1021 U+1023 U+103F U+1049 U+104A U+104B U+104B kinzi (U+105A, U+103A, U+1039)</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>ဃ ဋ ဌ ဍ ဎ ဒ န သ ဠ အ ဣ ဿ ၉ ၊ ။ ၚ်္</span> | `cv04=0` or `ss04=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv04" 1'>ဃ ဋ ဌ ဍ ဎ ဒ န သ ဠ အ ဣ ဿ ၉ ၊ ။ ၚ်္</span> | `cv04=1` or `ss04=1`

#### Aiton Phake special characters over Khamti <a id="cv05"></a><a id="ss05"></a>

<span class='affects'>Affects: U+1000 U+1075 U+AA61 U+107A U+1010 U+AA6B U+1078 U+101A U+AA7A U+101C U+AA6D U+1022 U+103C U+AA77</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>က︀ ၵ︀ ꩡ︀ ၺ တ︀ ꩫ︀ ၸ︀ ယ︀ ꩺ လ︀ ꩭ ဢ︀ ြ ꩷︀</span> | `cv05=0` or `ss05=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv05" 1'>က︀ ၵ︀ ꩡ︀ ၺ တ︀ ꩫ︀ ၸ︀ ယ︀ ꩺ လ︀ ꩭ ဢ︀ ြ ꩷︀</span> | `cv05=1` or `ss05=1`

#### Khamti variants <a id="cv06"></a><a id="ss06"></a>

<span class='affects'>Affects: U+1086</span>

Also note Variation Selector-1 below.

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>ႆ</span> | `cv06=0` or `ss06=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv06" 1'>ႆ</span> | `cv06=1` or `ss06=1`

#### Slanted hato <a id="cv07"></a>

<span class='affects'>Affects: U+103E U+102F U+1030 U+1061 U+1066</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
Upright | <span class='padauk-R normal'>ှ ှု ှူ ၡ ၦ</span> | `cv07=0`
Sgaw style slanted leg with horizontal foot | <span class='padauk-R normal' style='font-feature-settings: "cv07" 1'>ှ ှု ှူ ၡ ၦ</span> | `cv07=1`
Slanted leg with right angled foot | <span class='padauk-R normal' style='font-feature-settings: "cv07" 2'>ှ ှု ှူ ၡ ၦ</span> | `cv07=2`

#### Tai Laing variant <a id="cv09"></a><a id="ss09"></a>

<span class='affects'>Affects: U+AA6C</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>ꩬ</span> | `cv09=0` or `ss09=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv09" 1'>ꩬ</span> | `cv09=1` or `ss09=1`

#### Tai Laing variants <a id="cv10"></a><a id="ss10"></a>

<span class='affects'>Affects: U+A9E4 U+A9E8</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>ꧤ ꧨ</span> | `cv10=0` or `ss10=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv10" 1'>ꧤ ꧨ</span> | `cv10=1` or `ss10=1`

#### Disable Great nnya <a id="cv11"></a><a id="ss11"></a>

<span class='affects'>Affects: U+1039 U+100A</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
False | <span class='padauk-R normal'>ည္ည</span> | `cv11=0` or `ss11=0`
True | <span class='padauk-R normal' style='font-feature-settings: "cv11" 1'>ည္ည</span> | `cv11=1` or `ss11=1`

#### Variation Selector-1 <a id="vs1"></a>

<span class='affects'>Affects: U+FE00</span>

Note: Used for Khamti, Aiton, and Phake dotted characters. Also see entries for `cv05` and `cv06` above for additional variants.

Feature | Sample | Feature setting
------- | ---------------------------- | -------
Character with no VS1 (U+FE00) following | <span class='padauk-R normal'>က ဂ င တ ထ ပ မ ယ လ ဝ ဢ ေ ၵ ၸ ၺ ႀ ꩠ ꩡ ꩢ ꩣ ꩤ ꩥ ꩦ ꩫ ꩬ ꩯ ꩺ</span> |
Character with VS1 (U+FE00) following | <span class='padauk-R normal'>က︀ ဂ︀ င︀ တ︀ ထ︀ ပ︀ မ︀︀ ယ︀︀ လ︀ ဝ︀︀ ဢ︀︀ ေ︀ ၵ︀ ၸ︀ ၺ︀ ႀ︀ ꩠ︀ ꩡ︀ ꩢ︀ ꩣ︀ ꩤ︀ ꩥ︀ ꩦ︀ ꩫ︀ ꩬ︀ ꩯ︀ ꩺ︀</span> |

<!-- PRODUCT SITE ONLY
[font id='padauk' face='Padauk-Regular' bold='Padauk-Bold' size='150%']
-->
