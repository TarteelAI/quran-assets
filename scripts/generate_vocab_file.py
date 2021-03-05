import argparse
from collections import Counter
import json
from pathlib import Path

QURAN_TEXT_JSON = Path(__file__).parent.parent / "text" / "quran-text.json"

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--diacritized", action="store_true", help="Use the diacritized (Uthmani) text to generate the file")
parser.add_argument("-o", "--output", type=str, default="vocabulary.txt", help="Path to output file")
parser.add_argument("--quran-json", type=str, default=QURAN_TEXT_JSON, help="Path to quran-text.json")
args = parser.parse_args()


def main():
    with open(QURAN_TEXT_JSON, "r", encoding="utf-8") as quran_text_fh:
        quran_text = json.load(quran_text_fh)

    sentences = []
    word_counter = Counter()
    for surah_num in quran_text:
        for ayah_num in quran_text[surah_num]:
            if args.diacritized:
                text = quran_text[surah_num][ayah_num]["displayText"]
            else:
                text = quran_text[surah_num][ayah_num]["text"]
            sentences.append(text)
            word_counter.update(text.split())
    
    with open(args.output, "w", encoding="utf-8") as output_fh:
        vocab_str = "\n".join(c for c in sentences)
        output_fh.writelines(vocab_str)


if __name__ == "__main__":
    main()
