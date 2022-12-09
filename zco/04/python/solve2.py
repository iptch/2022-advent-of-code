import sys


def is_overlapping(section1, section2):
    return not (section2[1] < section1[0] or section1[1] < section2[0])


def parse_line(line):
    for part in line.split(","):
        yield list(map(int, part.split("-")))


def solve(lines):
    s = 0
    for line in lines:
        section1, section2 = parse_line(line)
        s += int(is_overlapping(section1, section2))
    return s


def main():
    lines = map(str.strip, sys.stdin)
    print("ans2", solve(lines))


if __name__ == "__main__":
    main()
