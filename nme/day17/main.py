PATH = 'input.txt'


ROCKS = [
    [[0, 0, 2, 2, 2, 2, 0]],
    [[0, 0, 0, 2, 0, 0, 0],
     [0, 0, 2, 2, 2, 0, 0],
     [0, 0, 0, 2, 0, 0, 0]],
    [[0, 0, 0, 0, 2, 0, 0],
     [0, 0, 0, 0, 2, 0, 0],
     [0, 0, 2, 2, 2, 0, 0]],
    [[0, 0, 2, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0]],
    [[0, 0, 2, 2, 0, 0, 0],
     [0, 0, 2, 2, 0, 0, 0]],
]


def load():
    res = None
    with open(PATH) as f:
        for line in f:
            res = line
    return res


def pretty_print(board):
    for line in board[::-1]:
        print(''.join(['.' if c == 0 else '@' if c == 2 else '#' for c in line]))
    print('')


def add_rock(rock, board):
    for j in range(3):
        board.append([0, 0, 0, 0, 0, 0, 0])
    for rock_line in rock[::-1]:
        board.append(rock_line[::])


def blow(mi, ma, direction, board):
    if direction == '<':
        for line_index in range(mi, ma):
            if board[line_index][0] == 2:
                return
            for pos in range(1, 7):
                if board[line_index][pos] == 2 and board[line_index][pos-1] == 1:
                    return
        for line_index in range(mi, ma):
            for pos in range(1, 7):
                if board[line_index][pos] == 2:
                    board[line_index][pos-1] = 2
                    board[line_index][pos] = 0
    if direction == '>':
        for line_index in range(mi, ma):
            if board[line_index][6] == 2:
                return
            for pos in range(0, 6):
                if board[line_index][pos] == 2 and board[line_index][pos+1] == 1:
                    return
        for line_index in range(mi, ma):
            for pos in range(5, -1, -1):
                if board[line_index][pos] == 2:
                    board[line_index][pos + 1] = 2
                    board[line_index][pos] = 0


def fall(mi, ma, board):
    for line_index in range(mi-1, ma-1):
        for pos in range(7):
            if board[line_index+1][pos] == 2:
                board[line_index][pos] = 2
                board[line_index+1][pos] = 0
    if board[-1] == [0, 0, 0, 0, 0, 0, 0]:
        board.pop()


def stuck(mi, ma, board):
    for pos in range(0, 7):
        if board[0][pos] == 2:
            return True
    for line_index in range(mi-1, ma-1):
        lower, upper = board[line_index], board[line_index+1]
        for lo, up in zip(lower, upper):
            if lo == 1 and up == 2:
                return True

    return False


def stop(mi, ma, board):
    for line_index in range(mi, ma):
        for pos in range(7):
            if board[line_index][pos] == 2:
                board[line_index][pos] = 1


def part1():
    line = load()
    line_index = 0
    board = []
    for i in range(2022):
        rock = ROCKS[i % 5]
        add_rock(rock, board)

        pos_min, pos_max = len(board) - len(rock), len(board)

        while True:
            blow(pos_min, pos_max, line[line_index % len(line)], board)
            line_index += 1
            if not stuck(pos_min, pos_max, board):
                fall(pos_min, pos_max, board)
                pos_min -= 1
                pos_max -= 1
            else:
                stop(pos_min, pos_max, board)
                break

    pretty_print(board)
    print(len(board))


def part2():
    line = load()
    line_index = 0
    board = []
    diffs = []
    diffs_num_rocks = []
    for i in range(1012 + 1743):
        if line_index > len(line):
            diffs.append(len(board) - sum(diffs))
            diffs_num_rocks.append(i - sum(diffs_num_rocks))
            line_index = line_index % len(line)
        rock = ROCKS[i % 5]
        add_rock(rock, board)

        pos_min, pos_max = len(board) - len(rock), len(board)

        while True:
            blow(pos_min, pos_max, line[line_index % len(line)], board)
            line_index += 1
            if not stuck(pos_min, pos_max, board):
                fall(pos_min, pos_max, board)
                pos_min -= 1
                pos_max -= 1
            else:
                stop(pos_min, pos_max, board)
                break

    print(diffs)
    print(diffs_num_rocks)

    # Explanation: We want to find repeating patterns when rocks fall

    # Step 1: Run for 100'000 falling blocks and observe,
    # everytime you loop around all left/right moves of your input, how many rocks have fallen
    # and how much height your board has gained. For me, it looks a bit like this

    # period number | rocks in period | height gained in period
    # 0             | 1743            | 2728
    # 1             | 1745            | 2738
    # 2             | 1745            | 2738
    # 3             | 1745            | 2738
    # 4             | 1745            | 2738

    # See a pattern? After the first period, we gain the same height (2738) every 1745 rocks
    period_height = 2738
    period_rocks = 1745
    offset_height = 2728
    offset_rocks = 1743
    big_num = 1000000000000

    # Thus, our total height is:
    # height in first period + (height per period for as many periods as necessary) + padding

    # We have everything except the final padding
    # We calculate that after running for offset_rocks and many many periods,
    # we still have 1012 rocks left to drop. We thus calculate how much height we gain in
    # offset_rocks + 1012 and subtract the offset_height from that. voila!

    rocks_left_to_drop = (big_num - offset_rocks) % period_rocks  # 1012 for me
    # Run simulation for rocks_left_to_drop + offset_height steps, gives me 4305
    padding_height = 4305 - offset_height

    print(offset_height + (((big_num - offset_rocks) // period_rocks) * period_height) + padding_height)


if __name__ == '__main__':
    part1()
    part2()
