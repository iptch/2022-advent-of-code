from dataclasses import dataclass
from typing import Callable
from operator import add, mul
import math

from common import load_lines


N_ROUNDS = 10000


@dataclass
class Monkey:
    idx: int
    items: list[int]
    update_op: Callable
    test_divisor: int
    true_target: int
    false_target: int
    n_inspections: int


def parse_monkeys(lines: list[str]) -> list[Monkey]:
    monkey_sub_lists = [lines[start_idx:start_idx + 6] for start_idx in range(0, len(lines), 6)]

    monkeys: list[Monkey] = list()
    for monkey_notes in monkey_sub_lists:
        idx_str, items_str, update_op_str, test_op_str, true_target_str, false_target_str = monkey_notes
        monkeys.append(Monkey(
            int(idx_str.split(' ')[-1][:-1]),
            [int(char) for char in items_str.split(': ')[-1].split(', ')],
            parse_update_op(update_op_str),
            int(test_op_str.split(' ')[-1]),
            int(true_target_str.split(' ')[-1]),
            int(false_target_str.split(' ')[-1]),
            n_inspections=0
        ))

    return monkeys


def play(monkeys: list[Monkey]) -> list[Monkey]:
    mod = math.prod([monkey.test_divisor for monkey in monkeys])
    for round_idx in range(N_ROUNDS):
        for monkey_idx, monkey in enumerate(monkeys):
            for item in monkey.items:
                monkey.n_inspections += 1
                item = monkey.update_op(item)
                item = item % mod
                new_monkey = monkey.true_target if item % monkey.test_divisor == 0 else monkey.false_target
                monkey.items = monkey.items[1:]
                monkeys[new_monkey].items.append(item)
    return monkeys


def parse_update_op(update_op_str: str) -> Callable:
    operator, factor = update_op_str.split('= ')[-1].split(' ')[1:]
    assert operator in {'+', '*'}, 'unexpected operator'
    op_func = add if operator == '+' else mul
    return lambda old: op_func(old, old if factor == 'old' else (int(factor)))


def compute_activity_product(monkeys: list[Monkey]) -> int:
    two_most_active_monkey_inspections = sorted([monkey.n_inspections for monkey in monkeys], reverse=True)[:2]
    return mul(*two_most_active_monkey_inspections)


if __name__ == '__main__':
    lines_ = load_lines(day=11, file_name='input.txt', skip_empty_lines=True)
    monkeys_ = parse_monkeys(lines_)
    final_state_monkeys_ = play(monkeys_)
    final_score = compute_activity_product(final_state_monkeys_)

    print(f'Task 1: {final_score} activity product')
