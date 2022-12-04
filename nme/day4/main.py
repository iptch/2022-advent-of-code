PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            ab, cd = line.split(',')
            a, b = ab.split('-')
            c, d = cd.split('-')
            res.append([int(a), int(b), int(c), int(d)])
    return res


def part1():
    overlaps = 0
    for a, b, c, d in load():
        if (a <= c and b >= d) or (c <= a and d >= b):
            overlaps += 1
    print(overlaps)


def part2():
    overlaps = 0
    for a, b, c, d in load():
        if a <= d and c <= b:
            overlaps += 1
    print(overlaps)


if __name__ == '__main__':
    part1()
    part2()
