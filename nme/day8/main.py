PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            l = []
            for c in line:
                if c != '\n': l.append(int(c))
            res.append(l)
    return res


def part1():
    trees = load()
    visible = set()
    n = len(trees)
    for i in range(n):
        td_max, dt_max, lr_max, rl_max = -1, -1, -1, -1
        for j in range(n):
            if trees[i][j] > td_max:
                visible.add((i, j))
                td_max = trees[i][j]
            if trees[i][n - j - 1] > dt_max:
                visible.add((i, n - j - 1))
                dt_max = trees[i][n - j - 1]
            if trees[j][i] > lr_max:
                visible.add((j, i))
                lr_max = trees[j][i]
            if trees[n - j - 1][i] > rl_max:
                visible.add((n - j - 1, i))
                rl_max = trees[n - j - 1][i]
    print(len(visible))


def part2():
    trees = load()
    n = len(trees)
    max_score = 0
    for i in range(n):
        for j in range(n):
            a, b, c, d = 0, 0, 0, 0
            th = trees[i][j]
            for da in range(i + 1, n):
                a += 1
                if trees[da][j] >= th:
                    break
            for db in range(i - 1, -1, -1):
                b += 1
                if trees[db][j] >= th:
                    break
            for dc in range(j + 1, n):
                c += 1
                if trees[i][dc] >= th:
                    break
            for dd in range(j - 1, -1, -1):
                d += 1
                if trees[i][dd] >= th:
                    break
            max_score = max(max_score, a * b * c * d)
    print(max_score)


if __name__ == '__main__':
    part1()
    part2()
