import io
import json
import os
import requests

BASE_API_URL = "https://api.quran.com/api/v4/verses/by_page/{}?audio=7&per_page=30"


def main():
    dirname = os.path.dirname(__file__)
    manifest = []
    for page_number in range(1, 605):
        source_data = requests.get(BASE_API_URL.format(page_number)).json()

        for ayah in source_data["verses"]:
            surah_number = int(ayah["verse_key"].split(":")[0])
            if surah_number > len(manifest):
                manifest.append([])
            ayah_number = ayah["verse_number"]
            if ayah_number > len(manifest[surah_number - 1]):
                manifest[surah_number - 1].append([])
            for s in ayah["audio"]["segments"]:
                if s[1] != s[0] + 1:
                    print(page_number, ayah["verse_key"], s)
                try:
                    manifest[surah_number - 1][ayah_number - 1].append([s[1], s[2], s[3]])
                except:
                    print(ayah["verse_key"], s)


    with io.open(os.path.join(dirname, '../audio/alafasy-ayah-manifest.json'), 'w', encoding='utf8') as json_file:
        data = json.dumps(manifest, ensure_ascii=False)
        json_file.write(data)


if __name__ == "__main__":
    main()
