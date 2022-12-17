from timeit import default_timer as timer
import re


def puzzle_1():
    y = 2000000
    result = set()
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    for line in lines:
        groups = [int(group) for group in re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()]
        distance = abs(groups[0]-groups[2]) + abs(groups[1]-groups[3])
        for xs in range(groups[0]-distance, groups[0]+distance):
            if abs(xs-groups[0]) + abs(y-groups[1]) <= distance:
                result.add(xs)
    for line in lines:
        groups = [int(group) for group in re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()]
        if groups[3] == y and groups[2] in result:
            result.remove(groups[2])

    return len(result)


def puzzle_2():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()

    sensors = []
    for line in lines:
        groups = [int(group) for group in re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()]
        groups.append(abs(groups[0] - groups[2]) + abs(groups[1] - groups[3]))
        sensors.append(groups)

    for x in range(0, 4000001):
        y_ranges = [(0, 4000000)]
        for sensor in sensors:
            y_distance = sensor[4]-abs(x-sensor[0])
            if y_distance <= 0:
                continue
            y_next_ranges = []
            while len(y_ranges) > 0:
                y_range = y_ranges.pop()
                if y_range[0] <= sensor[1]-y_distance and y_range[1] >= sensor[1]+y_distance:
                    y_next_ranges.append((y_range[0], sensor[1]-y_distance-1))
                    y_next_ranges.append((sensor[1]+y_distance+1, y_range[0]))
                else:
                    if sensor[1]-y_distance <= y_range[0] <= sensor[1]+y_distance:
                        y_range = (sensor[1]+y_distance+1, y_range[1])
                    if sensor[1]-y_distance <= y_range[1] <= sensor[1]+y_distance:
                        y_range = (y_range[0], sensor[1]-y_distance-1)
                    if y_range[0] <= y_range[1]:
                        y_next_ranges.append(y_range)
            y_ranges = y_next_ranges

        if len(y_ranges):
            return (x * 4000000) + y_ranges[0][0]

    return 0


if __name__ == '__main__':
    start1 = timer()
    print(f"Puzzle 1: {puzzle_1()} (in {timer()-start1}sec)")
    start2 = timer()
    print(f"Puzzle 2: {puzzle_2()} (in {timer()-start2}sec)")
