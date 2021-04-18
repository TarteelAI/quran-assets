"""
Convert the source text from Tanzil to JSON for easier and faster parsing.
"""
import argparse
import json


def tanzil_txt_to_json_lists(tanzil_txt_path: str):
    tanzil_list = []
    with open(tanzil_txt_path, "r") as tanzil_txt_fd:
        lines = tanzil_txt_fd.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            surah_num, ayah_num, text = line.split("|")
            surah_num = int(surah_num)
            ayah_num = int(ayah_num)

            if surah_num > 1 and ayah_num == 1:
                text = text.replace("بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ ", "")
                # Missing shadda for a couple ayahs
                text = text.replace("بِّسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ ", "")

            if surah_num > len(tanzil_list):
                tanzil_list.append([])
            tanzil_list[surah_num - 1].append(text)
    return tanzil_list


def tanzil_txt_to_json_objects(tanzil_txt_path: str):
    tanzil_json = {}
    with open(tanzil_txt_path, "r") as tanzil_txt_fd:
        lines = tanzil_txt_fd.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            surah_num, ayah_num, text = line.split("|")
            surah_num = int(surah_num)
            ayah_num = int(ayah_num)

            if surah_num > 1 and ayah_num == 1:
                text = text.replace("بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ ", "")
                # Missing shadda for a couple ayahs
                text = text.replace("بِّسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ ", "")

            if surah_num not in tanzil_json:
                tanzil_json[surah_num] = {}
            tanzil_json[surah_num][ayah_num] = text
    return tanzil_json


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Path to the Tanzil text file")
    parser.add_argument("-o", "--output", default="./quran-uthmani.json", type=str, help="Path to output file")
    parser.add_argument("-f", "--format", default="o", type=str, help="Format Quran as list (l) or object (o)")
    args = parser.parse_args()

    print(f"Generating JSON from {args.input}")
    if args.format == "l":
        output_json = tanzil_txt_to_json_lists(args.input)
    else:
        output_json = tanzil_txt_to_json_objects(args.input)

    print(f"Writing JSON to {args.output}")
    with open(args.output, "w", encoding="utf-8") as tanzil_json_fd:
        json.dump(output_json, tanzil_json_fd, ensure_ascii=False)
