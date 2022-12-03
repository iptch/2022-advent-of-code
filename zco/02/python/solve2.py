import sys

ROCK, PAPER, SCISSORS = range(3)


def translate_first(c):
    # return {"A": ROCK, "B": PAPER, "C": SCISSORS}[c]
    return ord(c) - ord("A")


def translate_second(c, opponent):
    # delta = {"X": -1, "Y": 0, "Z": 1}[c]
    delta = ord(c) - ord("Y")
    return (opponent + delta) % 3


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
        opponent = translate_first(opponent)
        total += points(
            opponent,
            translate_second(me, opponent),
        )
    return total


def main():
    lines = map(str.strip, sys.stdin)
    print("ans2", solve(lines))


if __name__ == "__main__":
    main()
