import re
from dataclasses import dataclass

from aocd import data

DAY = '15'
PART = 'b'


@dataclass
class Beacon:
    sensor_row_idx: int
    sensor_col_idx: int
    beacon_row_idx: int
    beacon_col_idx: int

    def get_coverage_manhattan_distance(self):
        return abs(self.beacon_row_idx - self.sensor_row_idx) + abs(self.beacon_col_idx - self.sensor_col_idx)

    def point_is_covered(self, row_idx, col_idx):
        return abs(self.sensor_row_idx - row_idx) + abs(self.sensor_col_idx - col_idx) <= self.get_coverage_manhattan_distance()

    def get_uncovered_border_points_of_row(self, row_idx):
        left_over_coverage = self.get_coverage_manhattan_distance() - abs(self.sensor_row_idx - row_idx)
        return self.sensor_col_idx - left_over_coverage - 1, self.sensor_col_idx + left_over_coverage + 1

    def get_uncovered_border_points(self, min_idx, max_idx):
        uncovered_border_points = []
        for row_idx in range(self.sensor_row_idx - self.get_coverage_manhattan_distance() - 1,
                             self.sensor_row_idx + self.get_coverage_manhattan_distance() + 2, 1):
            first_col_idx, second_col_idx = self.get_uncovered_border_points_of_row(row_idx)
            if all(min_idx <= idx <= max_idx for idx in [row_idx, first_col_idx]):
                uncovered_border_points.append((row_idx, first_col_idx))
            if all(min_idx <= idx <= max_idx for idx in [row_idx, second_col_idx]):
                uncovered_border_points.append((row_idx, second_col_idx))
        return uncovered_border_points


def read_beacons(lines):
    beacons = []
    for line in lines:
        raw_coordinates = re.findall(r'\-?[0-9]+', line)
        beacons.append(Beacon(int(raw_coordinates[1]), int(raw_coordinates[0]), int(raw_coordinates[3]), int(raw_coordinates[2])))
    return beacons


def find_all_uncovered_border_points(beacons, max_idx, min_idx):
    uncovered_border_points = []
    counter = 0
    for beacon in beacons:
        uncovered_border_points.extend(beacon.get_uncovered_border_points(min_idx, max_idx))
        counter += 1
        print(f'Detected uncovered border for beacon {str(counter)}.')
    return uncovered_border_points


def calculate_tuning_frequency_of_uncovered_point(beacons, uncovered_border_points):
    print(f'Now starting to check {str(len(uncovered_border_points))} points.')
    counter = 0
    for row_idx, col_idx in uncovered_border_points:
        counter += 1
        if counter % 500000 == 0:
            print(f'Now evaluating point nr. {str(counter)}...')
        if not any(beacon.point_is_covered(row_idx, col_idx) for beacon in beacons):
            return col_idx * 4000000 + row_idx
    return 0


def solve(lines, min_idx, max_idx):
    beacons = read_beacons(lines)
    uncovered_border_points = find_all_uncovered_border_points(beacons, max_idx, min_idx)
    return calculate_tuning_frequency_of_uncovered_point(beacons, uncovered_border_points)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    result = solve(lines, 0, 4000000)
    print(f'The tuning frequency is {str(result)}.')


if __name__ == '__main__':
    main()
