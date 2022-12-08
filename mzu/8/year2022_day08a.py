from aocd import data

DAY = '8'
PART = 'a'


def tree_is_at_edge_of_forest(forest_size_rows, forest_size_cols, row_idx, col_idx):
    return row_idx == 0 or col_idx == 0 or row_idx == forest_size_rows - 1 or col_idx == forest_size_cols - 1


def tree_is_visible_from_left(forest, row_idx, col_idx):
    result = True
    for col_idx_left_of_tree in range(col_idx - 1, -1, -1):
        if forest[row_idx][col_idx_left_of_tree] >= forest[row_idx][col_idx]:
            result = False
            break
    return result


def tree_is_visible_from_right(forest, row_idx, col_idx):
    result = True
    for col_idx_right_of_tree in range(col_idx + 1, len(forest[0]), +1):
        if forest[row_idx][col_idx_right_of_tree] >= forest[row_idx][col_idx]:
            result = False
            break
    return result


def tree_is_visible_from_top(forest, row_idx, col_idx):
    result = True
    for row_idx_above_tree in range(row_idx - 1, -1, -1):
        if forest[row_idx_above_tree][col_idx] >= forest[row_idx][col_idx]:
            result = False
            break
    return result


def tree_is_visible_from_bottom(forest, row_idx, col_idx):
    result = True
    for row_idx_below_tree in range(row_idx + 1, len(forest[0]), +1):
        if forest[row_idx_below_tree][col_idx] >= forest[row_idx][col_idx]:
            result = False
            break
    return result


def check_if_tree_is_visible(forest, row_idx, col_idx):
    return tree_is_visible_from_left(forest, row_idx, col_idx) or tree_is_visible_from_right(forest, row_idx, col_idx) \
           or tree_is_visible_from_top(forest, row_idx, col_idx) or tree_is_visible_from_bottom(forest, row_idx, col_idx)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    forest = [[int(tree_size) for tree_size in row] for row in lines]
    visible_trees = [[0 for _ in row] for row in forest]

    forest_size_rows = len(lines)
    forest_size_cols = len(lines[0])
    for row_idx in range(forest_size_rows):
        for col_idx in range(forest_size_cols):
            if tree_is_at_edge_of_forest(forest_size_rows, forest_size_cols, row_idx, col_idx):
                visible_trees[row_idx][col_idx] = True
            else:
                visible_trees[row_idx][col_idx] = check_if_tree_is_visible(forest, row_idx, col_idx)

    number_of_visible_trees = len([tree for column in visible_trees for tree in column if tree])
    print(f'There are a total of {str(number_of_visible_trees)} visible trees in the forest.')


if __name__ == '__main__':
    main()
