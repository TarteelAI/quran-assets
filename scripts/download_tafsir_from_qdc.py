import copy
import io
import json
import os
import requests

TAFSIR_LIST_URL = 'https://api.quran.com/api/v4/resources/tafsirs'
SINGLE_TAFSIR_URL = 'https://api.quran.com/api/v4/quran/tafsirs/'


def main():
    dirname = os.path.dirname(__file__)

    with open(os.path.join(dirname, '../metadata/ayah-count-per-surah-map.json'), "r", encoding="utf-8") as ayah_count_per_surah_file:
        AYAH_COUNT_PER_SURAH_MAP = json.load(ayah_count_per_surah_file)
        JSON_BASE_STRUCTURE = [[""] * val for val in AYAH_COUNT_PER_SURAH_MAP.values()]

    tafsir_dir = os.path.join(dirname, '../tafsir')
    os.makedirs(tafsir_dir, exist_ok=True)

    r = requests.get(TAFSIR_LIST_URL)
    r.encoding = 'utf-8'
    tafsir_list = r.json()['tafsirs']

    for tafsir in tafsir_list:
        id = tafsir['id']
        name = tafsir['name']

        print(f'Downloading {name}')
        url = f'{SINGLE_TAFSIR_URL}{id}?fields=text,verse_number,chapter_id'
        r = requests.get(url)
        r.encoding = 'utf-8'
        tafsir_data = r.json()['tafsirs']

        formatted_data = copy.deepcopy(JSON_BASE_STRUCTURE)
        for entry in tafsir_data:
            formatted_data[entry['chapter_id'] - 1][entry['verse_number'] - 1] = entry['text']

        with io.open(f'{tafsir_dir}/{name}.json', 'w', encoding='utf8') as json_file:
            data = json.dumps(formatted_data, indent=4, ensure_ascii=False)
            json_file.write(data)


if __name__ == "__main__":
    main()
