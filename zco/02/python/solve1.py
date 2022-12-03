import sys

ROCK, PAPER, SCISSORS = range(3)


def translate_first(c):
    # return {"A": ROCK, "B": PAPER, "C": SCISSORS}[c]
    return ord(c) - ord("A")


def translate_second(c):
    # return {"X": ROCK, "Y": PAPER, "Z": SCISSORS}[c]
    return ord(c) - ord("X")


def points(opponent, me):
    if opponent == me:
        # Draw
        points = 3
    elif (opponent + 1) % 3 == me:
        # I win
        points = 6
    else:
        # They win
        points = 0
    return points + me + 1


def solve(lines):
    total = 0
    for line in lines:
        opponent, me = line.split()
        total += points(
            translate_first(opponent),
            translate_second(me),
        )
    return total


def main():
    lines = map(str.strip, sys.stdin)
    print("ans1", solve(lines))


if __name__ == "__main__":
    main()
