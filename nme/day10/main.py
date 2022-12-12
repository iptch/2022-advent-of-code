PATH = 'input.txt'

RELEVANT_CYCLES = [20, 60, 100, 140, 180, 220]


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            if line[0:4] == 'noop':
                res.append(('noop', 0))
            else:
                op, num = line.split(' ')
                res.append((op, int(num)))
    return res


def part1():
    instructions = load()
    clock = 0
    res = 0
    register = 1
    for op, num in instructions:
        if op == 'noop':
            clock += 1
            if clock in RELEVANT_CYCLES:
                res += register * clock
        else:
            clock += 1
            if clock in RELEVANT_CYCLES:
                res += register * clock
            clock += 1
            if clock in RELEVANT_CYCLES:
                res += register * clock
            register += num
    print(res)


def draw(sprite, cycle, screen):
    line = cycle // 40
    col = cycle % 40
    if col - 1 <= sprite <= col + 1:
        screen[line][col] = '#'


def render(screen):
    for line in screen:
        print(''.join(line))


def part2():
    instructions = load()
    clock = 0
    register = 1
    screen = [['.' for _ in range(40)] for _ in range(6)]

    for op, num in instructions:
        if op == 'noop':
            draw(register, clock, screen)
            clock += 1
        else:
            draw(register, clock, screen)
            clock += 1
            draw(register, clock, screen)
            clock += 1
            register += num
    draw(register, clock, screen)
    render(screen)


if __name__ == '__main__':
    part1()
    part2()
