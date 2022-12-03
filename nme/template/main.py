PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            processed = line  # process the lines
            res.append(processed)
    return res


def part1():
    pass


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()
