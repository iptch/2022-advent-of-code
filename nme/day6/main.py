PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            res = line
    return res


def part1():
    stream = load()
    for i in range(len(stream) - 4):
        if len(set(stream[i:i+4])) == 4:
            print(i+4)
            return


def part2():
    stream = load()
    for i in range(len(stream) - 14):
        if len(set(stream[i:i + 14])) == 14:
            print(i + 14)
            return


if __name__ == '__main__':
    part1()
    part2()
