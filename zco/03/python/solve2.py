import sys


def split(lines, n):
    collected = []
    for line in lines:
        collected.append(line)
        if len(collected) == n:
            yield collected
            collected = []


def points(c: str):
    if c.islower():
        p = ord(c) - ord("a") + 1
    else:
        p = ord(c) - ord("A") + 27
    return p


def solve(lines):
    s = 0
    for linegroup in split(lines, 3):
        common_items = set(linegroup[0])
        for line in linegroup:
            common_items &= set(line)
        s += points(*common_items)
    return s


def main():
    lines = map(str.strip, sys.stdin)
    print("ans2", solve(lines))


if __name__ == "__main__":
    main()
