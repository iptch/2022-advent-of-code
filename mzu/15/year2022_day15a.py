import re
from dataclasses import dataclass

from aocd import data

DAY = '15'
PART = 'a'


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


def read_beacons(lines):
    beacons = []
    for line in lines:
        raw_coordinates = re.findall(r'\-?[0-9]+', line)
        beacons.append(Beacon(int(raw_coordinates[1]), int(raw_coordinates[0]), int(raw_coordinates[3]), int(raw_coordinates[2])))
    return beacons


def solve(lines, measured_row, min_idx, max_idx):
    beacons = read_beacons(lines)
    beacons_in_measured_row = [beacon.beacon_col_idx for beacon in beacons if beacon.beacon_row_idx == measured_row]
    number_of_positions_without_beacon = 0
    for col_idx in range(min_idx, max_idx, 1):
        for beacon in beacons:
            if beacon.point_is_covered(measured_row, col_idx) and col_idx not in beacons_in_measured_row:
                number_of_positions_without_beacon += 1
                break
    return number_of_positions_without_beacon


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    measured_row = 2000000
    result = solve(lines, 2000000, -2000000, 7000000)
    print(f'There are {str(result)} positions in row {str(measured_row)} where there cannot be a beacon.')


if __name__ == '__main__':
    main()
