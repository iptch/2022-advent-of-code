import string

from aocd import data

DAY = '3'
PART = 'b'

ALL_LETTERS = string.ascii_lowercase + string.ascii_uppercase
PRIORITIES = {ALL_LETTERS[i]: i + 1 for i in range(len(ALL_LETTERS))}


class Rucksack:
    def __init__(self, line):
        self.first_compartment_prios = [PRIORITIES[letter] for letter in line[:int(len(line) / 2)]]
        self.second_compartment_prios = [PRIORITIES[letter] for letter in line[int(len(line) / 2):]]
        self.all_prios = self.first_compartment_prios + self.second_compartment_prios


def read_rucksacks(lines):
    return [Rucksack(line) for line in lines]


def separate_rucksacks_into_groups(rucksacks):
    return [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]


def is_badge(prio, group):
    return all(prio in rucksack.all_prios for rucksack in group)


def calculate_badge_prio_per_group(group: [Rucksack]):
    badge_prio = None
    for i in range(len(group)):
        for prio in group[i].all_prios:
            if is_badge(prio, group):
                badge_prio = prio
    return badge_prio


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    rucksacks = read_rucksacks(lines)
    groups = separate_rucksacks_into_groups(rucksacks)
    badge_prios_per_group = [calculate_badge_prio_per_group(group) for group in groups]
    result = sum(badge_prios_per_group)

    print(f'The result is {(str(result))}')


if __name__ == '__main__':
    main()
