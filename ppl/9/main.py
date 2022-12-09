import re


def puzzle_1():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    visited = set()
    xh = 0
    yh = 0
    xt = 0
    yt = 0
    for line in lines:
        groups = line.split()
        direction = groups[0]
        amount = int(groups[1])
        for i in range(amount):
            if direction == "R":
                xh += 1
            if direction == "L":
                xh -= 1
            if direction == "U":
                yh += 1
            if direction == "D":
                yh -= 1
            if (abs(xh-xt) > 1 and abs(yh-yt) > 0) or (abs(xh-xt) > 0 and abs(yh-yt) > 1):
                if xh < xt:
                    xt -= 1
                else:
                    xt += 1
                if yh < yt:
                    yt -= 1
                else:
                    yt += 1
            elif abs(xh-xt) > 1:
                if xh < xt:
                    xt -= 1
                else:
                    xt += 1
            elif abs(yh-yt) > 1:
                if yh < yt:
                    yt -= 1
                else:
                    yt += 1
            visited.add((xt, yt))

    return len(visited)


def puzzle_2():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    visited = set()
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for line in lines:
        groups = line.split()
        direction = groups[0]
        amount = int(groups[1])
        for i in range(amount):
            if direction == "R":
                x[0] += 1
            if direction == "L":
                x[0] -= 1
            if direction == "U":
                y[0] += 1
            if direction == "D":
                y[0] -= 1
            for p in range(1, 10):
                if (abs(x[p-1]-x[p]) > 1 and abs(y[p-1]-y[p]) > 0) or (abs(x[p-1]-x[p]) > 0 and abs(y[p-1]-y[p]) > 1):
                    if x[p-1] < x[p]:
                        x[p] -= 1
                    else:
                        x[p] += 1
                    if y[p-1] < y[p]:
                        y[p] -= 1
                    else:
                        y[p] += 1
                elif abs(x[p-1]-x[p]) > 1:
                    if x[p-1] < x[p]:
                        x[p] -= 1
                    else:
                        x[p] += 1
                elif abs(y[p-1]-y[p]) > 1:
                    if y[p-1] < y[p]:
                        y[p] -= 1
                    else:
                        y[p] += 1
            visited.add((x[9], y[9]))

    return len(visited)


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
