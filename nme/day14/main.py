PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            points = [(int(p.split(',')[0]), int(p.split(',')[1])) for p in line.split(' -> ')]
            res.append(points)
    return res


def generate_all_points(points):
    res = set()
    for line in points:
        for (a, b), (x, y) in zip(line[:-1], line[1:]):
            res.add((a, b))
            res.add((x, y))
            if a == x:
                if b < y:
                    s, t = b, y
                else:
                    s, t = y, b
            else:
                if a < x:
                    s, t = a, x
                else:
                    s, t = x, a
            for i in range(s, t):
                if a == x:
                    res.add((a, i))
                else:
                    res.add((i, b))
    return res


def emit(points, sand):
    xs, ys = [x for x, _ in points], [y for _, y in points]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    offset = 5

    for y in range(min_y - offset, max_y + offset):
        line = ''
        for x in range(min_x - offset, max_x + offset):
            if (x, y) in points:
                line += '#'
            elif x == 500 and y == 0:
                line += '+'
            elif (x, y) in sand:
                line += 'o'
            else:
                line += '.'
        print(line)


def part1():
    points = load()
    all_points = generate_all_points(points)

    sand_min = max([y for _, y in all_points])
    sand = set()
    curr_sand = (500, 0)
    while curr_sand[1] <= sand_min:
        #emit(all_points, sand)
        down = (curr_sand[0], curr_sand[1] + 1)
        down_left = (curr_sand[0] - 1, curr_sand[1] + 1)
        down_right = (curr_sand[0] + 1, curr_sand[1] + 1)
        if down not in all_points and down not in sand:
            curr_sand = down
        elif down_left not in all_points and down_left not in sand:
            curr_sand = down_left
        elif down_right not in all_points and down_right not in sand:
            curr_sand = down_right
        else:
            sand.add(curr_sand)
            curr_sand = (500, 0)
    print(len(sand))


def part2():
    points = load()
    all_points = generate_all_points(points)
    sand_min = max([y for _, y in all_points])
    for i in range(500-sand_min-3, 500+sand_min+4):
        all_points.add((i, sand_min+2))
    sand = set()
    curr_sand = (500, 0)
    while (500, 0) not in sand:
        # emit(all_points, sand)
        down = (curr_sand[0], curr_sand[1] + 1)
        down_left = (curr_sand[0] - 1, curr_sand[1] + 1)
        down_right = (curr_sand[0] + 1, curr_sand[1] + 1)
        if down not in all_points and down not in sand:
            curr_sand = down
        elif down_left not in all_points and down_left not in sand:
            curr_sand = down_left
        elif down_right not in all_points and down_right not in sand:
            curr_sand = down_right
        else:
            sand.add(curr_sand)
            curr_sand = (500, 0)
    print(len(sand))


if __name__ == '__main__':
    part1()
    part2()
