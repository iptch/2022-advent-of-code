import ast
from common import load_lines


def parse_pairs(lines: list[str]) -> list[tuple]:
    string_repr_pairs = [(lines[idx], lines[idx + 1]) for idx in range(0, len(lines), 2)]
    pairs = []
    for first, second in string_repr_pairs:
        pairs.append((ast.literal_eval(first), ast.literal_eval(second)))
    return pairs


def find_right_order_indices_sum(pairs: list) -> int:
    indices = []

    for idx, (first, second) in enumerate(pairs, start=1):
        print(f'\n ------> Pair {idx}')
        print(f'first: {first}, second: {second}')
        if correct_order(first, second):
            indices.append(idx)
    print(f'indices: {indices}')
    return sum(indices)


def correct_order(first: list | int, second: list | int) -> bool | None:
    # Base case -> compare single items
    if not is_list(first) and not is_list(second):
        if first == second:
            print(f'first is second, continue checking {first} - {second}')
            return None
        else:
            if first < second:
                print(f'left smaller than right {first} < {second} -> ok')
            if first > second:
                print(f'left larger than right {first} > {second} -> NOT ok')
            return first < second

    # Adapt single items to lists for mixed cases
    if is_list(first) and not is_list(second):
        print(f'compare made second list {first} & {[second]}')
        second = [second]
    elif not is_list(first) and is_list(second):
        print(f'compare made first list {[first]} & {second}')
        first = [first]
    else:
        print(f'compare original lists {first} & {second}')

    # Compare all items against each other
    for left, right in zip(first, second):
        check = correct_order(left, right)
        if check is None:  # Numbers are same
            continue
        else:
            return check  # We have a result!

    # We arrive here only when all checks have shown that all the numbers are equal, thus len first has to be smaller
    if len(second) == len(first):
        print(f'first is second -> continue') 
        return None
    else:
        return len(first) < len(second)


def is_list(item: int | list) -> bool:
    return isinstance(item, list)


if __name__ == '__main__':
    lines_ = load_lines(day=13, file_name='test_input.txt', skip_empty_lines=True)
    pairs_ = parse_pairs(lines_)
    indices_sum_ = find_right_order_indices_sum(pairs_)

    print(f'Task 1: {indices_sum_}')
