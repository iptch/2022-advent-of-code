from aocd import data

DAY = '8'
PART = 'b'


def tree_is_not_at_edge_of_forest(forest_size_rows, forest_size_cols, row_idx, col_idx):
    return not (row_idx == 0 or col_idx == 0 or row_idx == forest_size_rows - 1 or col_idx == forest_size_cols - 1)


def scenic_score_left(forest, row_idx, col_idx):
    score = 0
    for col_idx_left_of_tree in range(col_idx - 1, -1, -1):
        score += 1
        if not forest[row_idx][col_idx_left_of_tree] < forest[row_idx][col_idx]:
            break
    return score


def scenic_score_right(forest, row_idx, col_idx):
    score = 0
    for col_idx_right_of_tree in range(col_idx + 1, len(forest[0]), +1):
        score += 1
        if not forest[row_idx][col_idx_right_of_tree] < forest[row_idx][col_idx]:
            break
    return score


def scenic_score_top(forest, row_idx, col_idx):
    score = 0
    for row_idx_above_tree in range(row_idx - 1, -1, -1):
        score += 1
        if not forest[row_idx_above_tree][col_idx] < forest[row_idx][col_idx]:
            break
    return score


def scenic_score_bottom(forest, row_idx, col_idx):
    score = 0
    for row_idx_below_tree in range(row_idx + 1, len(forest[0]), +1):
        score += 1
        if not forest[row_idx_below_tree][col_idx] < forest[row_idx][col_idx]:
            break
    return score


def calculate_scenic_score_of_tree(forest, row_idx, col_idx):
    return scenic_score_left(forest, row_idx, col_idx) * scenic_score_right(forest, row_idx, col_idx) \
           * scenic_score_top(forest, row_idx, col_idx) * scenic_score_bottom(forest, row_idx, col_idx)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    forest = [[int(tree_size) for tree_size in row] for row in lines]
    scenic_scores = [[0 for _ in row] for row in forest]

    forest_size_rows = len(lines)
    forest_size_cols = len(lines[0])
    for row_idx in range(forest_size_rows):
        for col_idx in range(forest_size_cols):
            if tree_is_not_at_edge_of_forest(forest_size_rows, forest_size_cols, row_idx, col_idx):
                scenic_scores[row_idx][col_idx] = calculate_scenic_score_of_tree(forest, row_idx, col_idx)

    max_scenic_score = max([tree for column in scenic_scores for tree in column if tree])
    print(f'The tree with the best view has a scenic score of {str(max_scenic_score)}.')


if __name__ == '__main__':
    main()
