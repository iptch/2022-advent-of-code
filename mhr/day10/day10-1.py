from dataclasses import dataclass
from common import load_lines


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
    register = list()
    for instruction in instructions:
        last_value = register[-1] if not len(register) == 0 else start_value
        if instruction.type == 'addx':
            register.append(last_value)
            register.append(last_value + instruction.value)
        elif instruction.type == 'noop':
            register.append(last_value)
        else:
            raise RuntimeError('unknown instruction type')
    assert len(register) == total_cycles
    return register


def sum_signal_strengths(register: list[int], at_cycles: list[int]) -> int:
    return sum([cycle * register[cycle - 2] for cycle in at_cycles])


if __name__ == '__main__':
    lines_ = load_lines(day=10, file_name='input.txt')
    instructions_ = parse_instructions(lines_)
    register_ = build_register(instructions_)
    signal_strength_sum_ = sum_signal_strengths(register_, [20, 60, 100, 140, 180, 220])

    print(f'Task 1: {signal_strength_sum_} total signal strength sum')
