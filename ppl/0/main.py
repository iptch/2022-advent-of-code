from timeit import default_timer as timer
import re


def puzzle_1():
    result = ""
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    for line in lines:
        groups = [int(group) for group in re.match(r"", line).groups()]
        pass

    return result


def puzzle_2():
    result = ""
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    for line in lines:
        groups = [int(group) for group in re.match(r"", line).groups()]
        pass

    return result


if __name__ == '__main__':
    start1 = timer()
    print(f"Puzzle 1: {puzzle_1()} (in {timer()-start1}sec)")
    start2 = timer()
    print(f"Puzzle 2: {puzzle_2()} (in {timer()-start2}sec)")
