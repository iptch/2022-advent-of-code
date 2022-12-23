from dataclasses import dataclass
from tqdm import tqdm

from common import load_lines


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


def calculate_free_points(sensor_beacon_tuples: list[tuple[Point, Point]], line_idx: int = 2000000) -> set[Point]:
    free_points = set()
    beacon_coordinates = {(tup[1].x, tup[1].y) for tup in sensor_beacon_tuples}

    for sensor, beacon in tqdm(sensor_beacon_tuples):
        distance = manhattan_distance(sensor, beacon)
        for x_pos in range(sensor.x - distance, sensor.x + distance + 1):
            if manhattan_distance(sensor, Point(x_pos, line_idx)) <= distance:
                if (x_pos, line_idx) not in beacon_coordinates:
                    free_points.add(Point(x_pos, line_idx))
    return free_points


def get_n_free_points_in_row(points: set[Point], row_idx: int) -> int:
    return len(list(filter(lambda point: point.y == row_idx, points)))


if __name__ == '__main__':
    ROW_IDX = 2000000

    lines_ = load_lines(day=15, file_name='input.txt', skip_empty_lines=True)
    sensor_beacon_tuples_ = parse_sensor_beacon_tuples(lines_)
    free_points_ = calculate_free_points(sensor_beacon_tuples_)

    print(f'Task 1: In row {ROW_IDX} there are {get_n_free_points_in_row(free_points_, ROW_IDX)} '
          f'positions without a possible beacon.')
