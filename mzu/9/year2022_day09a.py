from aocd import data

DAY = '9'
PART = 'a'

START_COL_INDEX = 0
START_ROW_INDEX = 4


def are_neighbors_or_on_top(head, tail):
    return tail in [head, (head[0] + 1, head[1]), (head[0] - 1, head[1]), (head[0], head[1] - 1), (head[0], head[1] + 1),
                    (head[0] - 1, head[1] - 1), (head[0] + 1, head[1] + 1),
                    (head[0] - 1, head[1] + 1), (head[0] + 1, head[1] - 1)]


def tail_catches_up(head, tail):
    new_tail_row_idx = tail[0]
    new_tail_col_idx = tail[1]

    if head[0] != tail[0]:
        new_tail_row_idx = tail[0] + 1 if tail[0] < head[0] else tail[0] - 1
    if head[1] != tail[1]:
        new_tail_col_idx = tail[1] + 1 if tail[1] < head[1] else tail[1] - 1

    return new_tail_row_idx, new_tail_col_idx


def move_tail_if_needed(head, tail, visited_positions):
    if not are_neighbors_or_on_top(head, tail):
        tail = tail_catches_up(head, tail)
        visited_positions[tail[0]][tail[1]] = True
    return tail, visited_positions


def move_head(direction, head):
    match direction:
        case 'U':
            head = (head[0] - 1, head[1])
        case 'D':
            head = (head[0] + 1, head[1])
        case 'L':
            head = (head[0], head[1] - 1)
        case 'R':
            head = (head[0], head[1] + 1)
    return head


def move(head, tail, direction, visited_positions):
    head = move_head(direction, head)
    tail, visited_positions = move_tail_if_needed(head, tail, visited_positions)
    return head, tail, visited_positions


def calculate_number_of_visited_tail_positions(lines, number_of_cols, number_of_rows):
    visited_positions = [[False] * number_of_cols for _ in range(number_of_rows)]
    head = (START_ROW_INDEX, START_COL_INDEX)
    tail = (START_ROW_INDEX, START_COL_INDEX)
    visited_positions[START_ROW_INDEX][START_COL_INDEX] = True
    for line in lines:
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            head, tail, visited_positions = move(head, tail, direction, visited_positions)
    return len([is_visited for row in visited_positions for is_visited in row if is_visited])


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    number_of_visited_tail_positions = calculate_number_of_visited_tail_positions(lines, 1000, 1000)
    print(f'The tail of the rope visits {(str(number_of_visited_tail_positions))} positions at least once.')


if __name__ == '__main__':
    main()
