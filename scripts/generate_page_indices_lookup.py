import io
import json
import os


def main():
    dirname = os.path.dirname(__file__)

    lookup_list = []
    for i in range(1, 605):
        with open(os.path.join(dirname, f'../pages/{i}.json'), "r", encoding="utf-8") as page_info_file:
            page_info = json.load(page_info_file)

        lookup_list.append(
            {
                "juz": page_info["juz"],
                "rub": page_info["hizb"],
                "start": {
                    "surah": page_info["surahs"][0]["surahNum"],
                    "ayah": page_info["surahs"][0]["ayahs"][0]["ayahNum"]
                },
                "end": {
                    "surah": page_info["surahs"][-1]["surahNum"],
                    "ayah": page_info["surahs"][-1]["ayahs"][-1]["ayahNum"]
                }
            }
        )

    with io.open(os.path.join(dirname, '../pages/lookups/page-indices-lookup.json'), 'w', encoding='utf8') as json_file:
        data = json.dumps(lookup_list, indent=2, ensure_ascii=False)
        json_file.write(data)


if __name__ == "__main__":
    main()
