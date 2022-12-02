from aocd import data

DAY = '1'
PART = 'b'


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    elves = []

    current_elve = []
    for line in lines:
        if line:
            current_elve.append(int(line))
        else:
            elves.append(current_elve)
            current_elve = []

    sums_of_calories = [sum(elve) for elve in elves]
    sorted_calories = sorted(sums_of_calories, reverse=True)
    sum_of_top_3_calories = sum([sorted_calories[0], sorted_calories[1], sorted_calories[2]])

    print(f'The result is: {sum_of_top_3_calories}')


if __name__ == '__main__':
    main()
