from aocd import data

DAY = '8'
PART = 'a'


def tree_is_at_edge_of_forest(forest_size_x, forest_size_y, x, y):
    return x == 0 or y == 0 or x == forest_size_x - 1 or y == forest_size_y - 1


def tree_is_visible_from_left(forest, x, y):
    result = True
    for y_left in range(y - 1, -1, -1):
        if forest[x][y_left] >= forest[x][y]:
            result = False
            break
    return result


def tree_is_visible_from_right(forest, x, y):
    result = True
    for y_right in range(y + 1, len(forest[0]), +1):
        if forest[x][y_right] >= forest[x][y]:
            result = False
            break
    return result


def tree_is_visible_from_top(forest, x, y):
    result = True
    for x_top in range(x - 1, -1, -1):
        if forest[x_top][y] >= forest[x][y]:
            result = False
            break
    return result


def tree_is_visible_from_bottom(forest, x, y):
    result = True
    for x_bottom in range(x + 1, len(forest[0]), +1):
        if forest[x_bottom][y] >= forest[x][y]:
            result = False
            break
    return result


def check_if_tree_is_visible(forest, x, y):
    return tree_is_visible_from_left(forest, x, y) or tree_is_visible_from_right(forest, x, y) \
           or tree_is_visible_from_top(forest, x, y) or tree_is_visible_from_bottom(forest, x, y)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    forest = [[int(tree_size) for tree_size in row] for row in lines]
    visible_trees = [[0 for _ in row] for row in forest]

    forest_size_x = len(lines)
    forest_size_y = len(lines[0])
    for x in range(forest_size_x):
        for y in range(forest_size_y):
            if tree_is_at_edge_of_forest(forest_size_x, forest_size_y, x, y):
                visible_trees[x][y] = True
            else:
                visible_trees[x][y] = check_if_tree_is_visible(forest, x, y)

    number_of_visible_trees = len([tree for column in visible_trees for tree in column if tree])
    print(f'There are a total of {str(number_of_visible_trees)} visible trees in the forest.')


if __name__ == '__main__':
    main()
