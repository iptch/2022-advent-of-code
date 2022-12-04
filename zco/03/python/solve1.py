import sys


def split(line, n):
    delta = len(line) // n
    i = 0
    for _ in range(n):
        yield line[i : i + delta]
        i += delta


def points(c: str):
    if c.islower():
        p = ord(c) - ord("a") + 1
    else:
        p = ord(c) - ord("A") + 27
    return p


def solve(lines):
    s = 0
    for line in lines:
        first, second = split(line, 2)
        first = set(first)
        for c in second:
            if c in first:
                s += points(c)
                break
    return s


def main():
    lines = map(str.strip, sys.stdin)
    print("ans1", solve(lines))


if __name__ == "__main__":
    main()
