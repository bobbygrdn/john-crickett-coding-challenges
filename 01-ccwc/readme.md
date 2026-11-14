# 01-ccwc

A tiny `wc`-like utility written in Python. Counts bytes, lines, words and characters on a file or on standard input.

## Install

From the project root:

```sh
uv tool -e .
```

This installs the console script ccwc from pyproject.toml:

```sh
[project.scripts]
ccwc = "main:main"
```

You can now run ccwc -h anywhere on your PATH.

## Usage

```sh
usage: ccwc [-l] [-w] [-c] [-m] [FILE]

Get byte, line, word, or character counts on specified file or standard input.

options:
  -h, --help  show this help message and exit
  -l          Count the number of lines
  -w          Count the number of words
  -c          Count the number of bytes
  -m          Count the number of characters
  FILE        File to process. If omitted, stdin is used.
If no flags are given the tool currently defaults to lines, words and bytes, matching classic wc behaviour.
```

## Examples

```sh
ccwc file.txt -l -w
# Returns line and word count in file

ccwc -m file.txt
# Returns character count in file

cat file.txt | ccwc -c
# Returns byte count from standard input

ccwc file.txt
# Returns line, word and byte counts in file
```

## Project layout

```sh
01-ccwc/
  main.py          # CLI implementation
  pyproject.toml   # project metadata + console script
  .gitignore
  readme.md
  test.txt         # sample data
```

## Development notes

- Single file implementation with argparse.
- filename is nargs="?" so [FILE] is optional and stdin is used when omitted.
- Files are opened with a context manager; sys.stdin.buffer is used for stdin.
- Build artifacts like *.egg-info/ are ignored via .gitignore.
