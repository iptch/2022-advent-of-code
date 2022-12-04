import re

a_from = 0
a_to = 1
b_from = 2
b_to = 3


def puzzle_1():
    result = 0
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    for line in lines:
        g = [int(i) for i in re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()]
        if (g[a_from] <= g[b_from] and g[a_to] >= g[b_to]) or \
                (g[b_from] <= g[a_from] and g[b_to] >= g[a_to]):
            result += 1

    return result


def puzzle_2():
    result = 0
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    for line in lines:
        g = [int(i) for i in re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line).groups()]
        if (g[a_from] <= g[b_from] <= g[a_to]) or \
                (g[a_from] <= g[b_to] <= g[a_to]) or \
                (g[b_from] <= g[a_from] <= g[b_to]) or \
                (g[b_from] <= g[a_to] <= g[b_to]):
            result += 1

    return result


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")

