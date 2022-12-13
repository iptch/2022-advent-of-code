import re


def puzzle_1():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    hightmap = [list(line) for line in lines]
    start = (0, 20)
    end = (58, 20)
    nexts = [start]
    steps = []

    for i in range(len(hightmap)):
        x = [100000000 for j in hightmap[i]]
        steps.append(x)
    steps[start[1]][start[0]] = 0

    while len(nexts) > 0:
        this = nexts.pop(0)

        up = (this[0], this[1]-1)
        if 0 <= up[1] < len(hightmap) and \
                0 <= up[0] < len(hightmap[up[1]]) and \
                steps[up[1]][up[0]] > steps[this[1]][this[0]] + 1 and \
                (ord(hightmap[this[1]][this[0]]) - ord(hightmap[up[1]][up[0]])) >= -1:
            nexts.append(up)
            steps[up[1]][up[0]] = steps[this[1]][this[0]] + 1

        down = (this[0], this[1]+1)
        if 0 <= down[1] < len(hightmap) and \
                0 <= down[0] < len(hightmap[down[1]]) and \
                steps[down[1]][down[0]] > steps[this[1]][this[0]] + 1 and \
                (ord(hightmap[this[1]][this[0]]) - ord(hightmap[down[1]][down[0]])) >= -1:
            nexts.append(down)
            steps[down[1]][down[0]] = steps[this[1]][this[0]] + 1

        left = (this[0]+1, this[1])
        if 0 <= left[1] < len(hightmap) and \
                0 <= left[0] < len(hightmap[left[1]]) and \
                steps[left[1]][left[0]] > steps[this[1]][this[0]] + 1 and \
                (ord(hightmap[this[1]][this[0]]) - ord(hightmap[left[1]][left[0]])) >= -1:
            nexts.append(left)
            steps[left[1]][left[0]] = steps[this[1]][this[0]] + 1

        right = (this[0]-1, this[1])
        if 0 <= right[1] < len(hightmap) and \
                0 <= right[0] < len(hightmap[right[1]]) and \
                steps[right[1]][right[0]] > steps[this[1]][this[0]] + 1 and \
                (ord(hightmap[this[1]][this[0]]) - ord(hightmap[right[1]][right[0]])) >= -1:
            nexts.append(right)
            steps[right[1]][right[0]] = steps[this[1]][this[0]] + 1

        if this == end:
            break


    return steps[end[1]][end[0]]


def puzzle_2():
    result = []
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    hightmap = [list(line) for line in lines]
    end = (58, 20)

    for start_y in range(len(hightmap)):
        for start_x in range(len(hightmap[start_y])):
            if hightmap[start_y][start_x] != "a":
                continue
            start = (start_x, start_y)
            nexts = [start]
            steps = []

            for i in range(len(hightmap)):
                x = [100000000 for j in hightmap[i]]
                steps.append(x)
            steps[start[1]][start[0]] = 0

            while len(nexts) > 0:
                this = nexts.pop(0)

                up = (this[0], this[1]-1)
                if 0 <= up[1] < len(hightmap) and \
                        0 <= up[0] < len(hightmap[up[1]]) and \
                        steps[up[1]][up[0]] > steps[this[1]][this[0]] + 1 and \
                        (ord(hightmap[this[1]][this[0]]) - ord(hightmap[up[1]][up[0]])) >= -1:
                    nexts.append(up)
                    steps[up[1]][up[0]] = steps[this[1]][this[0]] + 1

                down = (this[0], this[1]+1)
                if 0 <= down[1] < len(hightmap) and \
                        0 <= down[0] < len(hightmap[down[1]]) and \
                        steps[down[1]][down[0]] > steps[this[1]][this[0]] + 1 and \
                        (ord(hightmap[this[1]][this[0]]) - ord(hightmap[down[1]][down[0]])) >= -1:
                    nexts.append(down)
                    steps[down[1]][down[0]] = steps[this[1]][this[0]] + 1

                left = (this[0]+1, this[1])
                if 0 <= left[1] < len(hightmap) and \
                        0 <= left[0] < len(hightmap[left[1]]) and \
                        steps[left[1]][left[0]] > steps[this[1]][this[0]] + 1 and \
                        (ord(hightmap[this[1]][this[0]]) - ord(hightmap[left[1]][left[0]])) >= -1:
                    nexts.append(left)
                    steps[left[1]][left[0]] = steps[this[1]][this[0]] + 1

                right = (this[0]-1, this[1])
                if 0 <= right[1] < len(hightmap) and \
                        0 <= right[0] < len(hightmap[right[1]]) and \
                        steps[right[1]][right[0]] > steps[this[1]][this[0]] + 1 and \
                        (ord(hightmap[this[1]][this[0]]) - ord(hightmap[right[1]][right[0]])) >= -1:
                    nexts.append(right)
                    steps[right[1]][right[0]] = steps[this[1]][this[0]] + 1

                if this == end:
                    break

            result.append(steps[end[1]][end[0]])

    result.sort()
    return result.pop(0)


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
