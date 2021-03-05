import argparse
from collections import Counter
import json
from pathlib import Path

TEXT_DIR = Path(__file__).parent.parent / "text"
QURAN_TEXT_JSON = TEXT_DIR / "quran-text.json"

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--diacritized", action="store_true", help="Use the diacritized (Uthmani) text to generate the file")
parser.add_argument("--json", action="store_true", help="Save the alphabet as JSON list")
parser.add_argument("--quran-json", type=str, default=QURAN_TEXT_JSON, help="Path to quran-text.json")
parser.add_argument("-o", "--output", type=str, default=TEXT_DIR, help="Output directory")
args = parser.parse_args()


def main():
    with open(QURAN_TEXT_JSON, "r", encoding="utf-8") as quran_text_fh:
        quran_text = json.load(quran_text_fh)

    characters = set()

    for surah_num in quran_text:
        for ayah_num in quran_text[surah_num]:
            if args.diacritized:
                text = quran_text[surah_num][ayah_num]["displayText"]
            else:
                text = quran_text[surah_num][ayah_num]["text"]
            characters = characters | set(text)

    characters = list(characters)
    print(f"Found {len(characters)} characters")
    print(characters)

    if args.json:
        filename = TEXT_DIR / "alphabet.json"
        with open(filename, "w", encoding="utf-8") as alphabet_fh:
            json.dump(characters, alphabet_fh, ensure_ascii=False)
    else:
        filename = TEXT_DIR / "alphabet.txt"
        character_str = "\n".join(c for c in characters)
        with open(filename, "w", encoding="utf-8") as alphabet_fh:
            alphabet_fh.writelines(character_str)

if __name__ == "__main__":
    main()
