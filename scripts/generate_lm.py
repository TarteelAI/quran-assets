import argparse
import os
from pathlib import Path
import subprocess

DEFAULT_VOCAB_FILE = Path(__file__).parent.parent / "text" / "vocab-DI.txt" 

parser = argparse.ArgumentParser()
parser.add_argument("-b", "--bin", type=str, required=True, help="Path to kenlm binaries")
parser.add_argument("-o", "--order", type=int, default=3, help="Order of the LM")
parser.add_argument("--max_arpa_memory", type=int, default=80, help="Max sorting memory")
parser.add_argument("--prune", type=str, default="", help="ARPA pruning parameters. Separate values with '|'")
parser.add_argument("--output", type=str, default=".", help="Path to output directory")
parser.add_argument("--vocab", type=str, default=DEFAULT_VOCAB_FILE, help="Path to the vocabulary file")
args = parser.parse_args()


def main():
    lm_path = Path(args.output) / f"{args.order}-gram{'-pruned' if args.prune else ''}-lm.arpa"
    vocab_file = Path(args.vocab).as_posix()

    subargs = [
        os.path.join(args.bin, "lmplz"),
        "--order",
        str(args.order),
        "--temp_prefix",
        args.output,
        "--memory",
        f"{args.max_arpa_memory}%",
        "--text",
        vocab_file,
        "--arpa",
        lm_path.as_posix()
    ]
    if args.prune:
        subargs += ["--prune", *args.prune.split("|")]

    subprocess.check_call(subargs)


if __name__ == "__main__":
    main()
