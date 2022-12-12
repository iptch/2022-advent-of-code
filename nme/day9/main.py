PATH = 'input.txt'

'''
  --
  21012
 2OXXXO
 1X...X
 0X.h.X
-1X...X
-2OXXXO
'''

COMBINATIONS = {(2, -2): (-1, 1), (2, -1): (-1, 1), (2, 0): (-1, 0), (2, 1): (-1, -1), (2, 2): (-1, -1),
    (1, -2): (-1, 1), (1, -1): (0, 0), (1, 0): (0, 0), (1, 1): (0, 0), (1, 2): (-1, -1), (0, -2): (0, 1),
    (0, -1): (0, 0), (0, 0): (0, 0), (0, 1): (0, 0), (0, 2): (0, -1), (-1, -2): (1, 1), (-1, -1): (0, 0),
    (-1, 0): (0, 0), (-1, 1): (0, 0), (-1, 2): (1, -1), (-2, -2): (1, 1), (-2, -1): (1, 1), (-2, 0): (1, 0),
    (-2, 1): (1, -1), (-2, 2): (1, -1)}


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            d, c = line.split(' ')
            res.append([d, int(c)])
    return res


def normalize(h, t):
    return t[0] - h[0], t[1] - h[1]


def part1():
    instructions = load()
    tail, head = (0, 0), (0, 0)
    positions = set()
    positions.add(tail)
    for d, c in instructions:
        for _ in range(c):
            # move head
            if d == 'R':
                head = (head[0], head[1] + 1)
            if d == 'L':
                head = (head[0], head[1] - 1)
            if d == 'U':
                head = (head[0] + 1, head[1])
            if d == 'D':
                head = (head[0] - 1, head[1])

            # normalize
            n_tail = normalize(head, tail)

            # find out how much the tail moves
            tail_move_vector = COMBINATIONS[n_tail]

            # add offset + re-normalize
            tail = (n_tail[0] + head[0] + tail_move_vector[0], n_tail[1] + head[1] + tail_move_vector[1])

            positions.add(tail)

    print(len(positions))


def part2():
    instructions = load()
    knots = [(0, 0) for _ in range(10)]
    positions = set()
    positions.add((0, 0))
    for d, c in instructions:
        for _ in range(c):
            # move head
            if d == 'R':
                knots[0] = (knots[0][0], knots[0][1] + 1)
            if d == 'L':
                knots[0] = (knots[0][0], knots[0][1] - 1)
            if d == 'U':
                knots[0] = (knots[0][0] + 1, knots[0][1])
            if d == 'D':
                knots[0] = (knots[0][0] - 1, knots[0][1])

            # move knots
            for i in range(9):
                knot_tail = knots[i + 1]
                knot_head = knots[i]

                # normalize
                n_knot_tail = normalize(knot_head, knot_tail)

                # find out how much the tail moves
                tail_move_vector = COMBINATIONS[n_knot_tail]

                # add offset + re-normalize
                knot_tail = (n_knot_tail[0] + knot_head[0] + tail_move_vector[0],
                             n_knot_tail[1] + knot_head[1] + tail_move_vector[1])
                knots[i + 1] = knot_tail
            positions.add(knots[-1])

    print(len(positions))


if __name__ == '__main__':
    part1()
    part2()
