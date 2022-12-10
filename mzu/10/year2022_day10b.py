from aocd import data

DAY = '10'
PART = 'b'


def get_sprite_position(X, row_index):
    col_index_center = X % 40
    col_index_left = (X - 1) % 40
    col_index_right = (X + 1) % 40
    return [(row_index, col_index_left), (row_index, col_index_center), (row_index, col_index_right)]


def draw_sprite(CRT, X, cycles):
    row_index = int(cycles / 40)
    col_index = cycles % 40
    CRT[row_index][col_index] = '#' if (row_index, col_index) in get_sprite_position(X, row_index) else '.'
    return CRT


def transform_to_readable_string(CRT):
    readable_string = ""
    for line in CRT:
        readable_string += ''.join(line) + '\n'
    return readable_string


def solve(lines):
    CRT = [['.'] * 40 for i in range(6)]
    X = 1
    cycles = 0
    for line in lines:
        if line == "noop":
            CRT = draw_sprite(CRT, X, cycles)
            cycles += 1
        else:
            CRT = draw_sprite(CRT, X, cycles)
            cycles += 1
            CRT = draw_sprite(CRT, X, cycles)
            cycles += 1
            X += int(line.split(' ')[1])
    return transform_to_readable_string(CRT)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    result = solve(lines)
    print(result)


if __name__ == '__main__':
    main()
