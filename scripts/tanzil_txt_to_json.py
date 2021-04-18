"""
Convert the source text from Tanzil to JSON for easier and faster parsing.
"""
import argparse
import json


def tanzil_txt_to_json(tanzil_txt_path: str):
    tanzil_json = {}
    with open(tanzil_txt_path, "r") as tanzil_txt_fd:
        lines = tanzil_txt_fd.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            surah_num, ayah_num, text = line.split("|")
            if surah_num not in tanzil_json:
                tanzil_json[surah_num] = {}
            tanzil_json[surah_num][ayah_num] = text
    return tanzil_json


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, help="Path to the Tanzil text file")
    parser.add_argument("-o", "--output", default="./quran-uthmani.json", type=str, help="Path to output file")
    args = parser.parse_args()

    print(f"Generating JSON from {args.input}")
    output_json = tanzil_txt_to_json(args.input)

    print(f"Writing JSON to {args.output}")
    with open(args.output, "w", encoding="utf-8") as tanzil_json_fd:
        json.dump(output_json, tanzil_json_fd, ensure_ascii=False)
