import sys


def is_contained(section1, section2):
    return section2[0] <= section1[0] and section1[1] <= section2[1]


def parse_line(line):
    for part in line.split(","):
        yield list(map(int, part.split("-")))


def solve(lines):
    s = 0
    for line in lines:
        section1, section2 = parse_line(line)
        s += int(
            is_contained(section1, section2)
            or is_contained(section2, section1)
        )
    return s


def main():
    lines = map(str.strip, sys.stdin)
    print("ans1", solve(lines))


if __name__ == "__main__":
    main()
