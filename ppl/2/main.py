p1_resolver = {
    "X": {"name": "Rock", "value": 1, "A": 3, "B": 0, "C": 6},
    "Y": {"name": "Paper", "value": 2, "A": 6, "B": 3, "C": 0},
    "Z": {"name": "Scissors", "value": 3, "A": 0, "B": 6, "C": 3}
}


def puzzle_1():
    result = 0
    input_txt = open("input.txt", "r")
    for line in input_txt:
        draw = line.split()
        hand = p1_resolver[draw[1]]
        result += (hand["value"] + hand[draw[0]])

    return result


p2_resolver = {
    "X": {"name": "lose", "value": 0, "A": 3, "B": 1, "C": 2},
    "Y": {"name": "tie", "value": 3, "A": 1, "B": 2, "C": 3},
    "Z": {"name": "win", "value": 6, "A": 2, "B": 3, "C": 1}
}


def puzzle_2():
    result = 0
    input_txt = open("input.txt", "r")
    for line in input_txt:
        draw = line.split()
        hand = p2_resolver[draw[1]]
        result += (hand["value"] + hand[draw[0]])

    return result


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")

