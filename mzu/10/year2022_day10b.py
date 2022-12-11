from aocd import data

SCREEN_WIDTH = 40

DAY = '10'
PART = 'b'


def draw_sprite(CRT, X, cycles):
    row_index = int(cycles / SCREEN_WIDTH)
    col_index = cycles % SCREEN_WIDTH
    sprite_position = [(row_index, X - 1), (row_index, X), (row_index, X + 1)]
    CRT[row_index][col_index] = '#' if (row_index, col_index) in sprite_position else '.'
    return CRT


def transform_to_readable_string(CRT):
    readable_string = ""
    for line in CRT:
        readable_string += ''.join(line) + '\n'
    return readable_string


def process_cycle(CRT, X, cycles):
    CRT = draw_sprite(CRT, X, cycles)
    cycles += 1
    return CRT, cycles


def solve(lines):
    CRT = [['.'] * SCREEN_WIDTH for i in range(6)]
    X = 1
    cycles = 0
    for line in lines:
        if line == "noop":
            CRT, cycles = process_cycle(CRT, X, cycles)
        else:
            for _ in range(2):
                CRT, cycles = process_cycle(CRT, X, cycles)
            X += int(line.split(' ')[1])
    return transform_to_readable_string(CRT)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    result = solve(lines)
    print(result)


if __name__ == '__main__':
    main()
