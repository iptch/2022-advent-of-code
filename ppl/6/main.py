import re


def puzzle_1():
    result = 4
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    for line in lines:
        signals = list(line)
        packet = []
        for i in range(4):
            packet.append(signals.pop(0))
        while len(line) > 0:
            if len(set(packet)) == 4:
                return result
            packet.pop(-4)
            packet.append(signals.pop(0))
            result += 1

    return result


def puzzle_2():
    result = 14
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    for line in lines:
        signals = list(line)
        packet = []
        for i in range(14):
            packet.append(signals.pop(0))
        while len(line) > 0:
            if len(set(packet)) == 14:
                return result
            packet.pop(-14)
            packet.append(signals.pop(0))
            result += 1

    return result


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
