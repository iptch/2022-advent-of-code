from dataclasses import dataclass
from common import load_lines

SCREEN_WIDTH = 40
SCREEN_HEIGHT = 6


@dataclass
class Instruction:
    type: str
    value: int | None  # None for noop


def parse_instructions(lines: list[str]) -> list[Instruction]:
    instructions = list()
    for line in lines:
        if 'noop' in line:
            instructions.append(Instruction(type='noop', value=None))
        else:
            assert 'addx' in line, 'no addx in line: unexpected behaviour'
            instructions.append(Instruction(type='addx', value=int(line.split(' ')[1])))
    return instructions


def build_register(instructions: list[Instruction]) -> list[int]:
    noop_cycles = sum(1 for instruction in instructions if instruction.type == 'noop')
    addx_cycles = sum(2 for instruction in instructions if instruction.type == 'addx')
    total_cycles: int = noop_cycles + addx_cycles

    start_value = 1
    register = [start_value]
    for instruction in instructions:
        last_value = register[-1]
        if instruction.type == 'addx':
            register.append(last_value)
            register.append(last_value + instruction.value)
        elif instruction.type == 'noop':
            register.append(last_value)
        else:
            raise RuntimeError('unknown instruction type')
    assert len(register) - 1 == total_cycles, print(f'register length {len(register)} is not {total_cycles}')
    return register


def render_screen(register: list[int]) -> list[list[str]]:
    screen = [SCREEN_WIDTH * ['.'] for _ in range(SCREEN_HEIGHT)]
    row_indices = [val for sublist in [SCREEN_WIDTH * [row_idx] for row_idx in range(SCREEN_HEIGHT)] for val in sublist]
    cycle_indices = [idx for sublist in [list(range(SCREEN_WIDTH)) for _ in range(SCREEN_HEIGHT)] for idx in sublist]
    for cycle_idx, sprite_idx, row_idx in zip(cycle_indices, register, row_indices):
        sprite_indices = [sprite_idx - 1, sprite_idx, sprite_idx + 1]
        if cycle_idx in sprite_indices:
            screen[row_idx][cycle_idx] = '#'
    return screen


def print_screen(screen: list[list[str]]) -> None:
    for line in screen:
        print(' '.join(line))


if __name__ == '__main__':
    lines_ = load_lines(day=10, file_name='input.txt')
    instructions_ = parse_instructions(lines_)
    register_ = build_register(instructions_)
    screen_ = render_screen(register_)
    print_screen(screen_)


