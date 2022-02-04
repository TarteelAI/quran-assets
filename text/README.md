# Text

## Shortcodes

* DI: Diacritized
* UD: Undiacritized

## Vocabulary

`vocab-<shortcode>.txt`: All sentences in the Quran.

Generated from [`scripts/generate_vocab_file.py`](../scripts/generate_vocab_file.py).

## Words

`words-<shortcode>.txt`: All words in the Quran.
`words-<shortcode>-filtered.txt`: All words in the Quran.

Generated using 

```sh
for word in $(cat vocab-<shortcode>.txt); do echo "$word" >> words-<shortcode>.txt; done
sort words-<shortcode>.txt | uniq -u > words-<shortcode>-filtered.txt
```

## Alphabets

`alphabet-<shortcode>.<extension>`: Unique characters in the Quran (i.e. Arabic)

Generated from [`scripts/generate_alphabet.py`](../scripts/generate_alphabet.py).

## Files

* `quran-uthmani.txt`: Quran "Uthmani" text with pause, sajdah, rub, and tatweel from tanzil.net. Version 1.1 released February 12, 2021.
* `quran-simple-clean.txt`: Quran "Imlaei" text without pause, sajdah, rub, tashkil, or tatweel from tanzil.net. Version 1.1 released February 12, 2021.

## Licenses

### Tanzil

#### Quran Uthmani

```
# PLEASE DO NOT REMOVE OR CHANGE THIS COPYRIGHT BLOCK
#====================================================================
#
#  Tanzil Quran Text (Uthmani, Version 1.1)
#  Copyright (C) 2007-2021 Tanzil Project
#  License: Creative Commons Attribution 3.0
#
#  This copy of the Quran text is carefully produced, highly
#  verified and continuously monitored by a group of specialists
#  at Tanzil Project.
#
#  TERMS OF USE:
#
#  - Permission is granted to copy and distribute verbatim copies
#    of this text, but CHANGING IT IS NOT ALLOWED.
#
#  - This Quran text can be used in any website or application,
#    provided that its source (Tanzil Project) is clearly indicated,
#    and a link is made to tanzil.net to enable users to keep
#    track of changes.
#
#  - This copyright notice shall be included in all verbatim copies
#    of the text, and shall be reproduced appropriately in all files
#    derived from or containing substantial portion of this text.
#
#  Please check updates at: https://tanzil.net/updates/
#
#====================================================================
```
