DIRS = {
    "R": (1, 0),
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
}


def sub(p1, p2):
    return tuple(i1 - i2 for (i1, i2) in zip(p1, p2))


def add(p1, p2):
    return tuple(i1 + i2 for (i1, i2) in zip(p1, p2))


def inrange(p1, p2):
    return all(abs(i) <= 1 for i in sub(p1, p2))


def normalize(v):
    return tuple(-1 if i < 0 else 1 if i > 0 else 0 for i in v)


def solve(lines):
    rope = [(0, 0) for _ in range(10)]
    visited = set()
    visited.add(rope[-1])
    for line in lines:
        direction, amount = line.split()
        direction = DIRS[direction]
        for _ in range(int(amount)):
            rope[0] = add(rope[0], direction)
            for i in range(1, 10):
                if not inrange(rope[i], rope[i - 1]):
                    rope[i] = add(
                        rope[i], normalize(sub(rope[i - 1], rope[i]))
                    )
                else:
                    break
            else:
                # Tail was reached
                visited.add(rope[-1])
    print(len(visited))


def main():
    with open("../input") as f:
        solve(f)


if __name__ == "__main__":
    main()
