from dataclasses import dataclass
from enum import Enum

from aocd import data

DAY = '13'
PART = 'a'


class ComparisonResult(Enum):
    IN_RIGHT_ORDER = 1
    NOT_IN_RIGHT_ORDER = 2
    CANNOT_DECIDE = 3


@dataclass
class Pair:
    left: []
    right: []


def compare(left, right) -> ComparisonResult:
    if left == right:
        return ComparisonResult.CANNOT_DECIDE
    elif type(left) is int and type(right) is int:
        if left < right:
            return ComparisonResult.IN_RIGHT_ORDER
        else:
            return ComparisonResult.NOT_IN_RIGHT_ORDER
    elif type(left) is int:
        return compare([left], right)
    elif type(right) is int:
        return compare(left, [right])
    else:
        for index in range(len(left)):
            try:
                result = compare(left[index], right[index])
                if result != ComparisonResult.CANNOT_DECIDE:
                    return result
            except IndexError:
                return ComparisonResult.NOT_IN_RIGHT_ORDER
        return ComparisonResult.IN_RIGHT_ORDER


def parse_array(line) -> []:
    result = []
    open_brackets = 0
    start_index_of_nested_array = None
    current_number = ''
    for char_idx in range(0, len(line), 1):
        if line[char_idx] == '[':
            if open_brackets == 0:
                start_index_of_nested_array = char_idx
            open_brackets += 1
        elif line[char_idx] == ']':
            open_brackets -= 1
            if open_brackets == 0:
                result.append(parse_array(line[start_index_of_nested_array + 1:char_idx]))
        elif open_brackets == 0 and line[char_idx].isdigit():
            current_number += line[char_idx]
        elif current_number and not line[char_idx].isdigit():
            result.append(int(current_number))
            current_number = ''
    if current_number:
        result.append(int(current_number))
    return result


def parse_pair(lines) -> Pair:
    left = parse_array(lines[0][1:-1])
    right = parse_array(lines[1][1:-1])
    return Pair(left, right)


def solve(lines):
    pairs = []
    for line_idx in range(0, len(lines), 3):
        pairs.append(parse_pair(lines[line_idx: line_idx + 2]))
    pair_indexes_which_are_in_correct_order = []
    for pair_idx in range(len(pairs)):
        if compare(pairs[pair_idx].left, pairs[pair_idx].right) == ComparisonResult.IN_RIGHT_ORDER:
            pair_indexes_which_are_in_correct_order.append(pair_idx + 1)
    return sum(pair_indexes_which_are_in_correct_order)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    result = solve(lines)
    print(f'The sum of the indices of the pairs which are already in the right order is {str(result)}.')


if __name__ == '__main__':
    main()
