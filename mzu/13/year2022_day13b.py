from dataclasses import dataclass
from enum import Enum

from aocd import data

DAY = '13'
PART = 'b'


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


def sort_list(parsed_lines):
    while True:
        list_is_sorted = True
        for index in range(len(parsed_lines) - 1):
            pair_is_sorted = compare(parsed_lines[index], parsed_lines[index + 1]) == ComparisonResult.IN_RIGHT_ORDER
            if not pair_is_sorted:
                list_is_sorted = False
                temp = parsed_lines[index]
                parsed_lines[index] = parsed_lines[index + 1]
                parsed_lines[index + 1] = temp
        if list_is_sorted:
            return parsed_lines


def solve(lines):
    parsed_lines = []
    for line_idx in range(len(lines)):
        if lines[line_idx]:
            parsed_lines.append(parse_array(lines[line_idx][1:-1]))
    first_divider = [[2]]
    second_divider = [[6]]
    parsed_lines.append(first_divider)
    parsed_lines.append(second_divider)
    parsed_lines = sort_list(parsed_lines)
    index_of_first_divider = None
    index_of_second_divider = None
    for index in range(len(parsed_lines)):
        if parsed_lines[index] == first_divider:
            index_of_first_divider = index + 1
        elif parsed_lines[index] == second_divider:
            index_of_second_divider = index + 1
    return index_of_first_divider * index_of_second_divider


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    result = solve(lines)
    print(f'The decoder key for the stress signal is {str(result)}.')


if __name__ == '__main__':
    main()
