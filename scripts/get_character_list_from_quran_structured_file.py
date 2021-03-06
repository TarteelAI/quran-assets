import json
import os

dirname = os.path.dirname(__file__)
translations_dir = os.path.join(dirname, '../translations/tanzil')

with open(f'{translations_dir}/en-asad.json', 'r') as quran:
	parsed = json.load(quran)

char_set = set()
for surah in parsed:
    for ayah in surah:
        for char in ayah:
            char_set.add(char)

print(sorted(list(char_set)))
