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
    head = tail = (0, 0)
    visited = set()
    visited.add(tail)
    for line in lines:
        direction, amount = line.split()
        direction = DIRS[direction]
        amount = int(amount)
        for _ in range(amount):
            head = add(head, direction)
            if not inrange(head, tail):
                tail = add(tail, normalize(sub(head, tail)))
                visited.add(tail)
    print(head, tail)
    print(len(visited))


def main():
    with open("../input") as f:
        solve(f)


if __name__ == "__main__":
    main()
