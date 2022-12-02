import sys

ROCK, PAPER, SCISSORS = range(3)


def translate_first(c):
    return {"A": ROCK, "B": PAPER, "C": SCISSORS}[c]


def translate_second(c):
    return {"X": ROCK, "Y": PAPER, "Z": SCISSORS}[c]


def points(them, me):
    if them == me:
        # Draw
        points = 3
    elif (them + 1) % 3 == me:
        # I win
        points = 6
    else:
        # They win
        points = 0
    return points + me + 1


def solve(lines):
    total = 0
    for line in lines:
        them, me = line.split()
        total += points(
            translate_first(them),
            translate_second(me),
        )
    return total


def main():
    lines = map(str.strip, sys.stdin)
    print("ans1", solve(lines))


if __name__ == "__main__":
    main()
