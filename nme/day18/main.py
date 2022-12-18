PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            x, y, z = line.split(',')
            res.append((int(x), int(y), int(z)))
    return res


def diff(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])


def surface(points):
    visible_sides = {}
    for p in points:
        visible_sides[p] = 12

    for p in points:
        for q in points:
            if diff(p, q) == 1:
                visible_sides[p] -= 1
                visible_sides[q] -= 1

    return sum(visible_sides.values()) // 2


def part1():
    points = load()
    print(surface(points))


def part2():
    points = load()
    xs, ys, zs = [x for x, _, _ in points], [y for _, y, _ in points], [z for _, _, z in points]
    x_min, x_max, y_min, y_max, z_min, z_max = min(xs) - 1, max(xs) + 1, min(ys) - 1, max(ys) + 1, min(zs) - 1, max(
        zs) + 1

    points_set = set(points)
    outer_hull = set()
    outer_hull.add((0, 0, 0))
    q = [(0, 0, 0)]

    while q:
        x, y, z = q.pop()
        for neigh in [(x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)]:
            a, b, c = neigh
            if x_min <= a <= x_max and y_min <= b <= y_max and z_min <= c <= z_max and neigh not in outer_hull and neigh not in points_set:
                outer_hull.add(neigh)
                q.append(neigh)

    inner_points = set()
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            for z in range(z_min, z_max + 1):
                p = (x, y, z)
                if p not in outer_hull and p not in points_set:
                    inner_points.add(p)

    print(surface(points) - surface(inner_points))


if __name__ == '__main__':
    part1()
    part2()
