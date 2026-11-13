import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Get byte, line, or word counts on specified files."
    )

    parser.add_argument(
        "-c",
        action="store_true",
        help="Count the number of bytes in the specified file.",
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
        "filenames",
        nargs="+",
        help="The path(s) to the file(s) to count bytes, lines, or words in.",
    )

    args = parser.parse_args()

    if args.c or args.l or args.w:
        flags = [args.c, args.l, args.w]
        for filename in args.filenames:
            try:
                count = count_operation(flags, filename)
                print(f"{count} {filename}")
            except FileNotFoundError:
                print(f"File not found: {filename}")
    else:
        print(
            "No operation specified. Use -c, -l, or -w to count bytes, lines, or words."
        )


def count_operation(flags, filename):
    try:
        with open(filename, "rb") as f:
            data = f.read()
        text = data.decode("utf-8", errors="ignore")
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filename}")

    results = []
    if flags[0]:  # Count bytes
        results.append(str(len(data)))
    if flags[1]:  # Count lines
        results.append(str(len(text.splitlines())))
    if flags[2]:  # Count words
        results.append(str(len(text.split())))

    return " ".join(results)


if __name__ == "__main__":
    main()
