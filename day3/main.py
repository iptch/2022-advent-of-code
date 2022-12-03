PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            length = len(line)
            res.append([set(line[0:length // 2]), set(line[length // 2:-1])])
    return res


def priorities(l):
    return [ord(e) - (96 if e.islower() else 38) for e in l]


def part1():
    diff = [a.intersection(b).pop() for a, b in load()]
    values = priorities(diff)
    print(sum(values))


def part2():
    backpacks = [a.union(b) for a, b in load()]
    badges = [backpacks[i].intersection(backpacks[i + 1].intersection(backpacks[i + 2])).pop() for i in
              range(0, len(backpacks), 3)]
    print(sum(priorities(badges)))


if __name__ == '__main__':
    part1()
    part2()
