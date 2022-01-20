# This script pulls data from sqlite db files obtained from QDC as well as the
# existing page files to update the words of each page to align with the
# standardized words

import json
import os


def main():
    dirname = os.path.dirname(__file__)

    hash_list = []
    for i in range(1, 605):
        with open(os.path.join(dirname, f'../pages/{i}.json'), "r", encoding="utf-8") as page_info_file:
            page_info = json.load(page_info_file)

        latest_index = ""
        for surah in page_info["surahs"]:
            for ayah in surah["ayahs"]:
                for idx, word in enumerate(ayah["words"]):
                    if word["text"] is not None:
                        latest_index = f"{surah['surahNum']}-{ayah['ayahNum']}-{idx}"

        hash_list.append(latest_index)
    print(hash_list)


if __name__ == "__main__":
    main()
