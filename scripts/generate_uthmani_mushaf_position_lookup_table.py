import json
from pathlib import Path

QURAN_TEXT_JSON = Path(__file__).parent.parent / "text" / "quran-simple-clean.json"
OUTPUT_FILE_JSON = Path(__file__).parent.parent / "metadata" / "mushaf-translator-index.json"


def main():
    with open(QURAN_TEXT_JSON, "r", encoding="utf-8") as quran_text_fh:
        quran_text = json.load(quran_text_fh)

    translation_index = {}
    surah_count = 0
    ayah_count = 0
    mushaf_word_count = 0
    for surah_num in quran_text:
        translation_index[surah_num] = {}
        surah_count += 1

        for ayah_num in quran_text[surah_num]:
            translation_index[surah_num][ayah_num] = {}
            ayah_count += 1

            text = quran_text[surah_num][ayah_num]
            words = text.split()
            mapped_position = 0
            for idx, word in enumerate(words):
                translation_index[surah_num][ayah_num][str(idx)] = mapped_position
                if not (
                    word == "يا" or  # 350 matches for this case
                    word == "ها" or  # 3:66, 3:119, 4:109, 47:38
                    word == "ويا" or  # 7:19, 11:29, 11:30, 11:44, 11:52, 11:64, 11:85, 11:89, 11:93, 40:32, 40:41
                    word == "إل" or  # 37:130
                    (word == "ابن" and words[idx + 1] == "أم" and surah_num == "20") or  # 20:94
                    (word == "وأن" and words[idx + 1] == "لو")  # 72:16
                ):
                    mapped_position += 1
                    mushaf_word_count += 1

    with open(OUTPUT_FILE_JSON, "w", encoding="utf-8") as output_fh:
        data = json.dumps(translation_index, indent=2, ensure_ascii=False)
        output_fh.write(data)

    print(f"{surah_count} surahs")
    print(f"{ayah_count} ayahs")
    print(f"{mushaf_word_count} mushaf words")


if __name__ == "__main__":
    main()
