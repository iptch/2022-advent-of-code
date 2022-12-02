from aocd import data

DAY = '1'
PART = 'a'


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
    max_calory_elve = max(sums_of_calories)

    print(f'The result is: {max_calory_elve}')


if __name__ == '__main__':
    main()
