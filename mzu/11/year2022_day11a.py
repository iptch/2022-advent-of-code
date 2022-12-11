import re
from dataclasses import dataclass

from aocd import data

DAY = '11'
PART = 'a'


@dataclass
class Monkey:
    items: []
    operation: None
    test_divider: None
    receiver_passed_test: None
    receiver_failed_test: None
    inspection_counter: 0


def parse_monkey(monkey_lines: [str]) -> Monkey:
    items = [int(item) for item in re.findall(r'[0-9]+', monkey_lines[1])]
    operation = monkey_lines[2].removeprefix('  Operation: new = ')
    test_divider = int(re.findall(r'[0-9]+', monkey_lines[3])[0])
    receiver_passed_test = int(re.findall(r'[0-9]+', monkey_lines[4])[0])
    receiver_failed_test = int(re.findall(r'[0-9]+', monkey_lines[5])[0])
    return Monkey(items, operation, test_divider, receiver_passed_test, receiver_failed_test, 0)


def parse_input(lines) -> [Monkey]:
    monkeys = []
    i = 0
    while i < len(lines):
        monkeys.append(parse_monkey(lines[i:i + 6]))
        i += 7
    return monkeys


def play_round(monkeys):
    for monkey in monkeys:
        for _ in range(len(monkey.items)):
            monkey.inspection_counter += 1
            old = monkey.items.pop(0)
            new = eval(monkey.operation)
            new = new // 3
            if new % monkey.test_divider == 0:
                monkeys[monkey.receiver_passed_test].items.append(new)
            else:
                monkeys[monkey.receiver_failed_test].items.append(new)
    return monkeys


def solve(lines):
    monkeys = parse_input(lines)
    for i in range(20):
        monkeys = play_round(monkeys)

    monkey_inspection_counters = sorted([monkey.inspection_counter for monkey in monkeys], reverse=True)
    return monkey_inspection_counters[0] * monkey_inspection_counters[1]


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    result = solve(lines)
    print(f'{str(result)}')


if __name__ == '__main__':
    main()
