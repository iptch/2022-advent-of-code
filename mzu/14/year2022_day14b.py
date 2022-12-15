from aocd import data

DAY = '14'
PART = 'b'


def draw_cave(lines):
    cave = [['.'] * 1000 for _ in range(200)]
    max_row_idx = 0
    for line in lines:
        line_coordinates = [(int(coordinate.split(',')[1]), int(coordinate.split(',')[0])) for coordinate in line.split(' -> ')]
        last_point_row_idx, last_point_col_idx = line_coordinates[0]
        for next_point_row_idx, next_point_col_idx in line_coordinates[1:]:
            points_in_line = []
            if last_point_row_idx != next_point_row_idx:
                step = 1 if last_point_row_idx <= next_point_row_idx else -1
                for row_idx in range(last_point_row_idx, next_point_row_idx + step, step):
                    points_in_line.append((row_idx, next_point_col_idx))
            else:
                step = 1 if last_point_col_idx <= next_point_col_idx else -1
                for col_idx in range(last_point_col_idx, next_point_col_idx + step, step):
                    points_in_line.append((next_point_row_idx, col_idx))
            for row_idx, col_idx in points_in_line:
                cave[row_idx][col_idx] = '#'
                if row_idx > max_row_idx:
                    max_row_idx = row_idx
            last_point_row_idx, last_point_col_idx = next_point_row_idx, next_point_col_idx
    for col_idx in range(1000):
        cave[max_row_idx + 2][col_idx] = '#'
    return cave


def pour_sand(cave):
    sand_start_row_idx, sand_start_col_idx = 0, 500
    last_rested_sand_row_idx, last_rested_sand_col_idx = None, None
    while last_rested_sand_row_idx != 0 or last_rested_sand_col_idx != 500:
        sand_current_row_idx, sand_current_col_idx = (sand_start_row_idx, sand_start_col_idx)
        try:
            while True:
                if cave[sand_current_row_idx + 1][sand_current_col_idx] == '.':
                    sand_current_row_idx, sand_current_col_idx = sand_current_row_idx + 1, sand_current_col_idx
                elif cave[sand_current_row_idx + 1][sand_current_col_idx - 1] == '.':
                    sand_current_row_idx, sand_current_col_idx = sand_current_row_idx + 1, sand_current_col_idx - 1
                elif cave[sand_current_row_idx + 1][sand_current_col_idx + 1] == '.':
                    sand_current_row_idx, sand_current_col_idx = sand_current_row_idx + 1, sand_current_col_idx + 1
                else:
                    cave[sand_current_row_idx][sand_current_col_idx] = 'o'
                    last_rested_sand_row_idx, last_rested_sand_col_idx = sand_current_row_idx, sand_current_col_idx
                    break
        except IndexError:
            print(f'Cave drawn to small! Failing coordinate: ({str(sand_current_row_idx)},{str(sand_current_col_idx)})')
            break
    return cave


def solve(lines):
    cave = draw_cave(lines)
    cave = pour_sand(cave)
    return len([value for row in cave for value in row if value == 'o'])


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    result = solve(lines)
    print(f'There are a total of {str(result)} units of sand in the cave.')


if __name__ == '__main__':
    main()
