import re

def puzzle_1():
    result = ""
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    stacks = []

    for i in range(9):
        stacks.append([])

    initial_stack = lines[:8]
    initial_stack.reverse()
    for line in initial_stack:
        for i in range(9):
            craft = line[1 + 4 * i]
            if craft.isalpha():
                stacks[i].append(craft)

    for line in lines[10:]:
        groups = [int(group) for group in re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()]
        for i in range(groups[0]):
            stacks[groups[2]-1].append(stacks[groups[1]-1].pop())

    for i in range(9):
        result += stacks[i].pop()

    return result


def puzzle_2():
    result = ""
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    stacks = []

    for i in range(9):
        stacks.append([])

    initial_stack = lines[:8]
    initial_stack.reverse()
    for line in initial_stack:
        for i in range(9):
            craft = line[1 + 4 * i]
            if craft.isalpha():
                stacks[i].append(craft)

    for line in lines[10:]:
        groups = [int(group) for group in re.match(r"move (\d+) from (\d+) to (\d+)", line).groups()]
        for i in range(groups[0]):
            stacks[groups[2]-1].append(stacks[groups[1]-1].pop(i-groups[0]))

    for i in range(9):
        result += stacks[i].pop()

    return result


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")

