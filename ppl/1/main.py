def puzzle_1():
    f = open("input.txt", "r")
    m = 0
    c = 0
    for l in f:
        if len(l) <= 1:
            if c > m:
                m = c
            c = 0
        else:
            c += int(l)
    return m


def puzzle_2():
    result = [0]
    input_txt = open("input.txt", "r")
    for line in input_txt:
        if len(line) <= 1:
            result.insert(0, 0)
        else:
            result[0] = result[0] + int(line)
    result.sort()

    return result[-1] + result[-2] + result[-3]


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")

