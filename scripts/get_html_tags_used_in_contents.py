import json
import os
import re

dirname = os.path.dirname(__file__)
tafsir_dir = os.path.join(dirname, '../tafsir')

with open(f'{tafsir_dir}/en-tafsir-ibn-kathir.json', 'r') as quran:
	parsed = json.load(quran)

tag_set = set()
for surah in parsed:
    for ayah in surah:
        tags = re.findall('<.*?>', ayah)
        tag_set.update(tags)

print(tag_set, len(tag_set))
