from dataclasses import dataclass

N_STACKS = 9  # as given by input file


def load_lines(file_name: str) -> list[str]:
    with open(file_name) as infile:
        return [line.rstrip() for line in infile.readlines()]


def to_crate_stacks(crate_stack_lines: list[str]) -> dict[int, list[str]]:
    """Crate stacks is a dictionary with keys for column indices and values being lists representing the stack."""
    crate_stacks = {idx: [] for idx in range(N_STACKS)}
    for line in crate_stack_lines[::-1][1:]:
        chunk_size = 4
        line_chunked = [line[i:i + chunk_size] for i in range(0, len(line), chunk_size)]
        for col_idx, entry in enumerate(line_chunked):
            if not entry.isspace():
                crate_stacks[col_idx].append(entry.strip()[1:-1])
    return crate_stacks


@dataclass
class MoveOperation:
    amount: int
    destination: int  # as given in the input file, is index + 1
    target: int  # as given in the input file, is index + 1


def to_move_operations(plan_lines: list[str]) -> list[MoveOperation]:
    move_operations = []
    for line in plan_lines:
        split_line = line.split(' ')
        move_operations.append(MoveOperation(int(split_line[1]), int(split_line[3]), int(split_line[5])))
    return move_operations


def apply_move_operations_task1_style(crate_stacks: dict[int, list[str]], move_plan: list[MoveOperation]) -> dict[int, list[str]]:
    for move in move_plan:
        for _ in range(move.amount):
            item = crate_stacks[move.destination - 1].pop()
            crate_stacks[move.target - 1].append(item)
    return crate_stacks


def apply_move_operations_task2_style(crate_stacks: dict[int, list[str]], move_plan: list[MoveOperation]) -> dict[int, list[str]]:
    for move in move_plan:
        items = crate_stacks[move.destination - 1][-move.amount:]
        for _ in range(move.amount):
            crate_stacks[move.destination - 1].pop()
        crate_stacks[move.target - 1] += items
    return crate_stacks


def get_top_items(crate_stacks: dict[int, list[str]]) -> str:
    return ''.join([stack[-1] for stack in crate_stacks.values()])


if __name__ == '__main__':
    crate_stack_lines_ = load_lines('crate_stack.txt')
    plan_lines_ = load_lines('move_plan.txt')

    # Task 1
    print(f'')
    crate_stacks_ = to_crate_stacks(crate_stack_lines_)
    move_operations_ = to_move_operations(plan_lines_)
    final_crate_stacks = apply_move_operations_task1_style(crate_stacks_, move_operations_)
    print(f'Task 1 top items: {get_top_items(final_crate_stacks)}')

    # Task 2
    print(f'')
    crate_stacks_ = to_crate_stacks(crate_stack_lines_)
    move_operations_ = to_move_operations(plan_lines_)
    final_crate_stacks = apply_move_operations_task2_style(crate_stacks_, move_operations_)
    print(f'Task 2 top items: {get_top_items(final_crate_stacks)}')
