from dataclasses import dataclass
from tqdm import tqdm

from common import load_lines, print_grid


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


def manhattan_distance(first: Point, second: Point) -> int:
    return abs(first.x - second.x) + abs(first.y - second.y)


def parse_sensor_beacon_tuples(lines: list[str]) -> list[tuple[Point, Point]]:
    sensor_beacon_tuples = []
    for line in lines:
        first_part, second_part = line.split(': closest beacon is at ')
        beacon_x_str, beacon_y_str = second_part.split(', ')
        beacon = Point(int(beacon_x_str.split('=')[-1]), int(beacon_y_str.split('=')[-1]))
        sensor_x_str, sensor_y_str = first_part.split(' ')[2:]
        sensor = Point(int(sensor_x_str.split('=')[-1][:-1]), int(sensor_y_str.split('=')[-1]))
        sensor_beacon_tuples.append((sensor, beacon))
    return sensor_beacon_tuples


def get_diamond_border_points(sensor_beacon_tuples: list[tuple[Point, Point]], grid_size: int = 4000001) -> dict:
    boarder_points = {row_idx: [] for row_idx in range(grid_size)}
    for sensor, beacon in tqdm(sensor_beacon_tuples):
        distance = manhattan_distance(sensor, beacon)
        # upper right
        for y_pos, x_pos in zip(range(sensor.y - distance - 1, sensor.y + 1), range(sensor.x, sensor.x + distance + 2)):
            if 0 <= x_pos < grid_size and 0 <= y_pos < grid_size:
                boarder_points[y_pos].append((x_pos, y_pos))
        # lower right
        for y_pos, x_pos in zip(range(sensor.y, sensor.y + distance + 2), list(range(sensor.x, sensor.x + distance + 2))[::-1]):
            if 0 <= x_pos < grid_size and 0 <= y_pos < grid_size:
                boarder_points[y_pos].append((x_pos, y_pos))
        # lower right
        for y_pos, x_pos in zip(range(sensor.y, sensor.y + distance + 2), list(range(sensor.x, sensor.x + distance + 2))[::-1]):
            if 0 <= x_pos < grid_size and 0 <= y_pos < grid_size:
                boarder_points[y_pos].append((x_pos, y_pos))
        # lower left
        for y_pos, x_pos in zip(range(sensor.y - 1, sensor.y + distance + 2)[::-1], list(range(sensor.x - distance, sensor.x + 1)[::-1])):
            if 0 <= x_pos < grid_size and 0 <= y_pos < grid_size:
                boarder_points[y_pos].append((x_pos, y_pos))
        # upper left
        for y_pos, x_pos in zip(range(sensor.y - distance - 1, sensor.y + 1)[::-1], range(sensor.x - distance - 1, sensor.x + 1)):
            if 0 <= x_pos < grid_size and 0 <= y_pos < grid_size:
                boarder_points[y_pos].append((x_pos, y_pos))

    return boarder_points


def calculate_free_points(sensor_beacon_tuples: list[tuple[Point, Point]]) -> set[Point]:
    free_points = {row_idx: list() for row_idx in range(4000001)}
    beacon_coordinates = {(tup[1].x, tup[1].y) for tup in sensor_beacon_tuples}

    for sensor, beacon in tqdm(sensor_beacon_tuples):
        distance = manhattan_distance(sensor, beacon)
        for x_pos in range(clamp(sensor.x - distance), clamp(sensor.x + distance + 1)):
            for y_pos in range(clamp(sensor.y - distance), clamp(sensor.y + distance + 1)):
                if manhattan_distance(sensor, Point(x_pos, y_pos)) <= distance:
                    if (x_pos, y_pos) not in beacon_coordinates:
                        free_points[y_pos].append(x_pos)
    return free_points


def clamp(val, start=0, stop=4000001) -> int:
    return min(max(val, start), stop)



def get_n_free_points_in_row(points: set[Point], row_idx: int) -> int:
    return len(list(filter(lambda point: point.y == row_idx, points)))


def tuning_frequency(x: int, y: int, factor: int = 4000000) -> int:
    return x * factor + y


if __name__ == '__main__':
    lines_ = load_lines(day=15, file_name='input.txt', skip_empty_lines=True)
    sensor_beacon_tuples_ = parse_sensor_beacon_tuples(lines_)
    free_points_ = calculate_free_points(sensor_beacon_tuples_)
    for row_idx, x_indices in free_points_.items():
        print(row_idx, len(x_indices))
    print(len(free_points_))

    #boarder_points = get_diamond_border_points(sensor_beacon_tuples_, grid_size=20)

    # grid_size = 20
    # grid = [grid_size * ['.'] for _ in range(grid_size)]
    #
    #
    # for row_idx, points in boarder_points.items():
    #     grid[]
    #     print(f'{row_idx}: {len(points)}')


    #
    # # ----- Visualization Code Start -----
    # grid_size = 20
    # grid = [grid_size * ['.'] for _ in range(grid_size)]
    #
    # for point in free_points_:
    #     if point.x < grid_size and point.y < grid_size:
    #         grid[point.y][point.x] = '#'
    # for sensor, beacon in sensor_beacon_tuples_:
    #     if sensor.x < grid_size and sensor.y < grid_size:
    #         grid[sensor.y][sensor.x] = 'S'
    #     if beacon.x < grid_size and beacon.x < grid_size:
    #         grid[beacon.y][beacon.x] = 'B'
    #
    # border_points_ = get_diamond_border_points(sensor_beacon_tuples_)
    #
    # for point in border_points_:
    #     if point.x < grid_size and point.y < grid_size and grid[point.y][point.x] not in {'#', 'B', 'S'}:
    #         grid[point.y][point.x] = '-'
    #         print(point)
    #
    # # print_grid(grid)
    # # ----- Visualization Code End -----
    #
    # # for y_idx, line in enumerate(grid):
    # #     for x_idx, char in enumerate(line):
    # #         if char == '.':
    # #             print(x_idx, y_idx)
    # #             print(tuning_frequency(x_idx, y_idx))
    #
    # print(f'Task 1: Tuning frequency of free beacon {get_n_free_points_in_row(free_points_)}')
