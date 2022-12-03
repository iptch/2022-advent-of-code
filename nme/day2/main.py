PATH = 'input.txt'

SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}
RESULTS = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3,
}
CHOICE = {
    'AX': 'Z',
    'AY': 'X',
    'AZ': 'Y',
    'BX': 'X',
    'BY': 'Y',
    'BZ': 'Z',
    'CX': 'Y',
    'CY': 'Z',
    'CZ': 'X',
}


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            res.append([line[0], line[2]])
    return res


def part1():
    rounds = load()
    score = 0
    for o, m in rounds:
        score += SCORES[m] + RESULTS[o + m]
    print(score)


def part2():
    rounds = load()
    score = 0
    for o, m in rounds:
        take = CHOICE[o + m]
        score += SCORES[take] + RESULTS[o + take]
    print(score)


if __name__ == '__main__':
    part1()
    part2()
