import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Get byte, line, word, or character counts on specified file or standard input."
    )

    parser.add_argument(
        "-l",
        action="store_true",
        help="Count the number of lines in the specified file.",
    )

    parser.add_argument(
        "-w",
        action="store_true",
        help="Count the number of words in the specified file.",
    )

    parser.add_argument(
        "-c",
        action="store_true",
        help="Count the number of bytes in the specified file.",
    )

    parser.add_argument(
        "-m",
        action="store_true",
        help="Count the number of characters in the specified file.",
    )

    parser.add_argument(
        "filename",
        nargs="?",
        help="The file to count bytes, lines, words, or characters in. Stdin is used if no file is specified.",
    )

    args = parser.parse_args()
    flags = [True, True, True, False]

    if args.l or args.w or args.c or args.m:
        flags = [args.l, args.w, args.c, args.m]
    count = count_operation(flags, args.filename)
    print(count)


def count_operation(flags, filename):
    counts = {}
    with open(filename, "rb") if filename else sys.stdin.buffer as f:
        for line in f:
            if flags[0]:  # Count lines
                counts["lines"] = counts.get("lines", 0) + 1
            if flags[1]:  # Count words
                counts["words"] = counts.get("words", 0) + len(line.split())
            if flags[2]:  # Count bytes
                counts["bytes"] = counts.get("bytes", 0) + len(line)
            if flags[3]:  # Count characters
                counts["characters"] = counts.get("characters", 0) + len(
                    line.decode(errors="ignore")
                )

    result = " ".join(str(v) for v in counts.values()) + (
        f" {filename}" if filename else ""
    )

    return result.strip()


if __name__ == "__main__":
    main()
