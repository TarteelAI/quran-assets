# This script pulls data from the QDC api to generate standardized data files
# for each page of the Quran


import io
import json
import os
import requests

BASE_API_URL = "https://api.quran.com/api/qdc/verses/by_page/{}?words=true&fields=chapter_id&word_fields=%20text_uthmani,%20text_indopak,%20code_v1&mushaf=2"


def main():
    dirname = os.path.dirname(__file__)

    for i in range(1, 605):
        qdc_page_data = requests.get(BASE_API_URL.format(i)).json()

        custom_page_data = {
            "hizb": qdc_page_data["verses"][0]["hizb_number"],
            "juz": qdc_page_data["verses"][0]["juz_number"],
            "pageNumber": qdc_page_data["verses"][0]["page_number"],
            "rub": qdc_page_data["verses"][0]["rub_number"],
            "surahs": [],
        }

        for verse in qdc_page_data["verses"]:
            surah_number = verse["chapter_id"]
            if len(custom_page_data["surahs"]) == 0 or custom_page_data["surahs"][-1]["surahNum"] != surah_number:
                custom_page_data["surahs"].append({
                    "surahNum": surah_number,
                    "ayahs": []
                })

            custom_page_data["surahs"][-1]["ayahs"].append({
                "ayahNum": verse["verse_number"],
                "words": [],
            })

            for word in verse["words"]:
                custom_page_data["surahs"][-1]["ayahs"][-1]["words"].append({
                    "code": word["code_v1"],
                    "text": None if word["char_type_name"] == "end" else word["text_uthmani"],
                    "indopak": word["text_indopak"],
                    "lineNumber": word["line_number"],
                })

        with io.open(os.path.join(dirname, f'../pages/{i}.json'), 'w', encoding='utf8') as json_file:
            data = json.dumps(custom_page_data, indent=2, ensure_ascii=False)
            json_file.write(data)


if __name__ == "__main__":
    main()
