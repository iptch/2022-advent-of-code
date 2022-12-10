import re


def puzzle_1():
    result = 0
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    cycles = [20, 60, 100, 140, 180, 220]
    x = 1
    cycle = 1
    for line in lines:
        groups = line.split()
        instruction = groups[0]
        if instruction == "noop":
            if cycle in cycles:
                result += (cycle*x)
            cycle += 1
        if instruction == "addx":
            if cycle in cycles:
                result += (cycle*x)
            cycle += 1
            if cycle in cycles:
                result += (cycle*x)
            cycle += 1
            x += int(groups[1])

    return result


def puzzle_2():
    result = []
    for i in range(240):
        result.append(".")
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    x = 0
    cycle = 0
    for line in lines:
        groups = line.split()
        instruction = groups[0]
        if instruction == "noop":
            if x <= cycle % 40 <= x+2:
                result[cycle] = "#"
            cycle += 1
        if instruction == "addx":
            if x <= cycle % 40 <= x+2:
                result[cycle] = "#"
            cycle += 1
            if x <= cycle % 40 <= x+2:
                result[cycle] = "#"
            cycle += 1
            x += int(groups[1])

    result = "\n" + \
        "".join(result[0:40]) + "\n" + \
        "".join(result[40:80]) + "\n" + \
        "".join(result[80:120]) + "\n" + \
        "".join(result[120:160]) + "\n" + \
        "".join(result[160:200]) + "\n" + \
        "".join(result[200:240]) + "\n"
    return result


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
