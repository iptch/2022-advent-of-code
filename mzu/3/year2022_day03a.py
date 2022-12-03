import string

from aocd import data

DAY = '3'
PART = 'a'

ALL_LETTERS = string.ascii_lowercase + string.ascii_uppercase
PRIORITIES = {ALL_LETTERS[i]: i + 1 for i in range(len(ALL_LETTERS))}


class Rucksack:
    def __init__(self, line):
        self.first_compartment_prios = [PRIORITIES[letter] for letter in line[:int(len(line) / 2)]]
        self.second_compartment_prios = [PRIORITIES[letter] for letter in line[int(len(line) / 2):]]


def read_rucksacks(lines):
    return [Rucksack(line) for line in lines]


def calculate_error_prios(rucksacks):
    error_priorities = []
    for rucksack in rucksacks:
        error_prios_of_rucksack = \
            [prio for prio in rucksack.first_compartment_prios if prio in rucksack.second_compartment_prios] + \
            [prio for prio in rucksack.second_compartment_prios if prio in rucksack.first_compartment_prios]
        error_priorities.extend(set(error_prios_of_rucksack))

    return error_priorities


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    rucksacks = read_rucksacks(lines)
    error_priorities = calculate_error_prios(rucksacks)
    result = sum(error_priorities)

    print(f'The result is {(str(result))}')


if __name__ == '__main__':
    main()
