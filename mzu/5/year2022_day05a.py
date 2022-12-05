import re
from dataclasses import dataclass

from aocd import data

DAY = '5'
PART = 'a'


@dataclass
class Move:
    number_of_crates: int
    from_stack_index: int
    to_stack_index: int


def find_stack_bottom_index(lines):
    stack_bottom_index = None
    for i in range(len(lines)):
        if lines[i].startswith(' 1'):
            stack_bottom_index = i
    return stack_bottom_index


def divide_line_into_stacks(line):
    for i in range(0, len(line), 4):
        yield line[i:i + 4]


def read_stacks(lines):
    bottom_index = find_stack_bottom_index(lines)
    number_of_stacks = len(re.findall(r'[0-9]', lines[bottom_index]))
    stacks = []
    for i in range(number_of_stacks):
        stacks.append([])

    for i in range(bottom_index - 1, -1, -1):
        letters = list(divide_line_into_stacks(lines[i]))
        for stack_index in range(len(letters)):
            letter_in_line = re.findall(r'[A-Z]', letters[stack_index])
            if letter_in_line:
                stacks[stack_index].append(letter_in_line[0])

    return stacks


def read_moves(lines):
    moves = []
    for line in lines:
        if not line.startswith('move'):
            continue
        numbers = re.findall(r'[0-9]+', line)
        moves.append(Move(int(numbers[0]), int(numbers[1]) - 1, int(numbers[2]) - 1))
    return moves


def move_crates(stacks: [], moves: [Move]):
    for move in moves:
        for i in range(move.number_of_crates):
            crate = stacks[move.from_stack_index].pop()
            stacks[move.to_stack_index].append(crate)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    stacks = read_stacks(lines)
    moves = read_moves(lines)
    move_crates(stacks, moves)

    top_crates = [stack.pop() for stack in stacks]

    print(f'The final message is: {"".join(top_crates)}.')


if __name__ == '__main__':
    main()
