PATH = 'input.txt'


def load():
    sensors, beacons = [], set()
    with open(PATH) as f:
        for line in f:
            s, b = line.split(': closest beacon is at ')
            sx, sy = s[12:].split(', y=')
            bx, by = b[2:].split(', y=')
            sensors.append(((int(sx), int(sy)), (int(bx), int(by))))
            beacons.add((int(bx), int(by)))
    return sensors, beacons


def manhattan_distance(px, py, sx, sy):
    return abs(px - sx) + abs(py - sy)


def part1():
    sensors, beacons = load()
    interesting_line = 2000000
    res = set()
    for (sx, sy), (bx, by) in sensors:
        dist = manhattan_distance(sx, sy, bx, by)
        dist_to_line = abs(interesting_line - sy)
        width_on_both_sides = max(0, dist - dist_to_line)
        a, b = sx - width_on_both_sides, sx + width_on_both_sides + 1
        for i in range(a, b):
            res.add(i)
    for bx, by in beacons:
        if by == interesting_line and bx in res:
            res.remove(bx)
    print(len(res))


def merge(intervals):
    res = sorted(intervals)
    changed = True
    while changed:
        new_res = []
        changed = False
        i = 0
        while i < len(res) - 1:
            if res[i][1] + 1 >= res[i + 1][0]:
                new_res.append((min(res[i][0], res[i + 1][0]), max(res[i][1], res[i + 1][1])))
                i += 2
                changed = True
            else:
                new_res.append(res[i])
                new_res.append(res[i + 1])
                i += 2
        if i != 0 and i == len(res) - 1:
            new_res.append(res[i])
            changed = True
        if changed:
            res = new_res
    return res


def part2():
    sensors, beacons = load()
    # search_area = 20
    search_area = 4000000
    intervals = [[] for _ in range(search_area + 1)]
    for (sx, sy), (bx, by) in sensors:
        dist = manhattan_distance(sx, sy, bx, by)
        for x in range(max(0, sy - dist), min(sy + dist + 1, search_area + 1)):
            dist_to_line = abs(x - sy)
            width_on_both_sides = max(0, dist - dist_to_line)
            a, b = max(0, sx - width_on_both_sides), min(search_area + 1, sx + width_on_both_sides)
            if a <= b:
                intervals[x].append((a, b))
    for i, interval in enumerate(intervals):
        merged = merge(interval)
        if len(merged) > 1:
            print((merged[0][1] + 1) * 4000000 + i)


if __name__ == '__main__':
    part1()
    part2()
