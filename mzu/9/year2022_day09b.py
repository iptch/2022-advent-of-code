from aocd import data

DAY = '9'
PART = 'b'

START_COL_INDEX = 11
START_ROW_INDEX = 15
NUMBER_OF_KNOTS = 10


def are_neighbors_or_on_top(knot1, knot2):
    return knot2 in [knot1, (knot1[0] + 1, knot1[1]), (knot1[0] - 1, knot1[1]), (knot1[0], knot1[1] - 1),
                     (knot1[0], knot1[1] + 1),
                     (knot1[0] - 1, knot1[1] - 1), (knot1[0] + 1, knot1[1] + 1),
                     (knot1[0] - 1, knot1[1] + 1), (knot1[0] + 1, knot1[1] - 1)]


def knot_catches_up(knot1, knot2):
    new_knot_row_ix = knot2[0]
    new_knot_col_idx = knot2[1]

    if knot1[0] != knot2[0]:
        new_knot_row_ix = knot2[0] + 1 if knot2[0] < knot1[0] else knot2[0] - 1
    if knot1[1] != knot2[1]:
        new_knot_col_idx = knot2[1] + 1 if knot2[1] < knot1[1] else knot2[1] - 1

    return new_knot_row_ix, new_knot_col_idx


def move_knot_if_needed(knot1, knot2, is_tail, visited_positions):
    if not are_neighbors_or_on_top(knot1, knot2):
        knot2 = knot_catches_up(knot1, knot2)
        if is_tail:
            visited_positions[knot2[0]][knot2[1]] = True
    return knot2, visited_positions


def move_rest_of_rope(rope, visited_positions):
    for knot_index in range(1, len(rope) - 1):
        rope[knot_index], visited_positions = move_knot_if_needed(rope[knot_index - 1], rope[knot_index], False, visited_positions)
    rope[len(rope) - 1], visited_positions = move_knot_if_needed(rope[len(rope) - 2], rope[len(rope) - 1], True, visited_positions)
    return rope, visited_positions


def move_up(rope, distance, visited_positions):
    for _ in range(distance):
        rope[0] = (rope[0][0] - 1, rope[0][1])
        rope, visited_positions = move_rest_of_rope(rope, visited_positions)
    return rope, visited_positions


def move_down(rope, distance, visited_positions):
    for _ in range(distance):
        rope[0] = (rope[0][0] + 1, rope[0][1])
        rope, visited_positions = move_rest_of_rope(rope, visited_positions)
    return rope, visited_positions


def move_left(rope, distance, visited_positions):
    for _ in range(distance):
        rope[0] = (rope[0][0], rope[0][1] - 1)
        rope, visited_positions = move_rest_of_rope(rope, visited_positions)
    return rope, visited_positions


def move_right(rope, distance, visited_positions):
    for _ in range(distance):
        rope[0] = (rope[0][0], rope[0][1] + 1)
        rope, visited_positions = move_rest_of_rope(rope, visited_positions)
    return rope, visited_positions


def move(rope, direction, distance, visited_positions):
    match direction:
        case 'U':
            rope, visited_positions = move_up(rope, distance, visited_positions)
        case 'D':
            rope, visited_positions = move_down(rope, distance, visited_positions)
        case 'L':
            rope, visited_positions = move_left(rope, distance, visited_positions)
        case 'R':
            rope, visited_positions = move_right(rope, distance, visited_positions)
    return rope, visited_positions


def calculate_number_of_visited_tail_positions(lines, number_of_cols, number_of_rows, start_row_idx, start_col_idx):
    visited_positions = [[False] * number_of_cols for _ in range(number_of_rows)]
    rope = [(start_row_idx, start_col_idx) for i in range(NUMBER_OF_KNOTS)]
    visited_positions[start_row_idx][start_col_idx] = True
    for line in lines:
        direction, distance = line.split(' ')
        rope, visited_positions = move(rope, direction, int(distance), visited_positions)
    return len([is_visited for row in visited_positions for is_visited in row if is_visited])


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    number_of_visited_tail_positions = calculate_number_of_visited_tail_positions(lines, 1000, 1000, 15, 11)
    print(f'The tail of the rope visits {(str(number_of_visited_tail_positions))} positions at least once.')


if __name__ == '__main__':
    main()
