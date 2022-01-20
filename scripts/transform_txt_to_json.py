# Transforms Quran text file into formatted json file
# json file still needs post-processing to remove extra basmallahs

import io
import json
import os


def main():
    dirname = os.path.dirname(__file__)

    with open(os.path.join(dirname, f'../text/quran-simple-clean.txt'), "r", encoding="utf-8") as text_file:
        line_by_line_quran = text_file.readlines()

    quran_json = {}
    quran_list_json = []
    for line in line_by_line_quran:
        split_line = line.split("|")
        if split_line[1] == "1":
            quran_json[split_line[0]] = {}
            quran_list_json.append([])
        ayah_text = split_line[2].strip()
        quran_json[split_line[0]][split_line[1]] = ayah_text
        quran_list_json[-1].append(ayah_text)

        # Stop processing lines before we reach empty lines or license information
        if split_line[0] == "114" and split_line[1] == "6":
            break

    with io.open(os.path.join(dirname, f'../text/quran-simple-clean.json'), 'w', encoding='utf8') as json_file:
        data = json.dumps(quran_json, indent=2, ensure_ascii=False)
        json_file.write(data)

    with io.open(os.path.join(dirname, f'../text/quran-simple-clean-list.json'), 'w', encoding='utf8') as json_file:
        data = json.dumps(quran_list_json, indent=4, ensure_ascii=False)
        json_file.write(data)


if __name__ == "__main__":
    main()
