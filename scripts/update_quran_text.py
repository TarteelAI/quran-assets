from collections import Counter
import json
from pathlib import Path

QURAN_TEXT_JSON = Path(__file__).parent.parent / "text" / "quran-text.json"
OUTPUT_FILE_JSON = Path(__file__).parent.parent / "text" / "standardized-simple-quran-text.json"


def main():
    with open(QURAN_TEXT_JSON, "r", encoding="utf-8") as quran_text_fh:
        quran_text = json.load(quran_text_fh)

    word_counter = Counter()
    new_text = {}
    surah_count = 0
    ayah_count = 0
    for surah_num in quran_text:
        new_text[surah_num] = {}
        surah_count += 1

        for ayah_num in quran_text[surah_num]:
            ayah_count += 1

            text = quran_text[surah_num][ayah_num]["text"]
            words = text.split()
            modified_words = []
            preceding_string = ""
            for idx, word in enumerate(words):
                if (
                    word == "يا" or  # 350 matches for this case
                    word == "ها" or  # 3:66, 3:119, 4:109, 47:38
                    word == "ويا" or  # 7:19, 11:29, 11:30, 11:44, 11:52, 11:64, 11:85, 11:89, 11:93, 40:32, 40:41
                    word == "إل" or  # 37:130
                    (word == "ابن" and words[idx + 1] == "أم" and surah_num == "20") or  # 20:94
                    (word == "وأن" and words[idx + 1] == "لو")  # 72:16
                ):
                    preceding_string += word
                else:
                    modified_words.append(preceding_string + word)
                    word_counter[preceding_string + word] += 1
                    preceding_string = ""

            new_text[surah_num][ayah_num] = " ".join(modified_words)

    with open(OUTPUT_FILE_JSON, "w", encoding="utf-8") as output_fh:
        data = json.dumps(new_text, indent=2, ensure_ascii=False)
        output_fh.write(data)

    print(f"{surah_count} surahs")
    print(f"{ayah_count} ayahs")
    print(f"{sum(word_counter.values())} words")


if __name__ == "__main__":
    main()
