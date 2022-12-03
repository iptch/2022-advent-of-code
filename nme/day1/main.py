PATH = 'input.txt'


def load_calories():
    res = []
    with open(PATH) as f:
        elf = []
        for line in f:
            if line == '\n':
                res.append(elf)
                elf = []
            else:
                elf.append(int(line))
        res.append(elf)
    return res


def part1():
    res = max([sum(elf) for elf in load_calories()])
    print(res)


def part2():
    s = sorted([sum(elf) for elf in load_calories()])
    res = s[-1] + s[-2] + s[-3]
    print(res)


if __name__ == '__main__':
    part1()
    part2()
