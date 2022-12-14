import numpy as np


def draw_cave(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    cave = np.zeros((1000, 1000))
    for line in lines:
        rock_parts = line.split(' -> ')
        for idx in range(len(rock_parts) - 1):
            start = rock_parts[idx].split(',')
            end = rock_parts[idx + 1].split(',')
            start_col = int(start[0])
            start_row = int(start[1])
            end_col = int(end[0])
            end_row = int(end[1])
            if start_col == end_col:
                # vertical line
                if start_row < end_row:
                    for i in range(start_row, end_row + 1):
                        cave[i, start_col] = 6
                else:

                    for i in range(end_row, start_row + 1):
                        cave[i, start_col] = 6
            else:
                # horizontal
                if start_col < end_col:
                    for i in range(start_col, end_col + 1):
                        cave[start_row, i] = 6
                else:
                    for i in range(end_col, start_col + 1):
                        cave[start_row, i] = 6
    # drop entry rows to check when abyss begins
    rows_to_drop = np.argmax(np.flip(cave.sum(axis=1)) > 0)
    cave = np.delete(cave, np.s_[-rows_to_drop:], 0)
    return cave


def simulate_sand(cave):
    elements = 0
    try:
        while True:
            sand = (0, 500)
            moving = True
            while moving:
                if cave[sand[0] + 1, sand[1]] == 0:
                    # down straight
                    sand = (sand[0] + 1, sand[1])
                elif cave[sand[0] + 1, sand[1] - 1] == 0:
                    # down left
                    sand = (sand[0] + 1, sand[1] - 1)
                elif cave[sand[0] + 1, sand[1] + 1] == 0:
                    # down right
                    sand = (sand[0] + 1, sand[1] + 1)
                else:
                    # resting
                    cave[sand[0], sand[1]] = 1
                    moving = False
            elements += 1
    except IndexError:
        print(f'Entered abyss after {elements} elements')
    print('end')

# simulate_sand(draw_cave('data_test.txt'))
simulate_sand(draw_cave('data_prod.txt'))
