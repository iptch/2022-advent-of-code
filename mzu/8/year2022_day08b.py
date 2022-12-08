from aocd import data

DAY = '8'
PART = 'b'


def tree_is_not_at_edge_of_forest(forest_size_x, forest_size_y, x, y):
    return not (x == 0 or y == 0 or x == forest_size_x - 1 or y == forest_size_y - 1)


def scenic_score_left(forest, x, y):
    score = 0
    for y_left in range(y - 1, -1, -1):
        score += 1
        if not forest[x][y_left] < forest[x][y]:
            break
    return score


def scenic_score_right(forest, x, y):
    score = 0
    for y_right in range(y + 1, len(forest[0]), +1):
        score += 1
        if not forest[x][y_right] < forest[x][y]:
            break
    return score


def scenic_score_top(forest, x, y):
    score = 0
    for x_top in range(x - 1, -1, -1):
        score += 1
        if not forest[x_top][y] < forest[x][y]:
            break
    return score


def scenic_score_bottom(forest, x, y):
    score = 0
    for x_bottom in range(x + 1, len(forest[0]), +1):
        score += 1
        if not forest[x_bottom][y] < forest[x][y]:
            break
    return score


def calculate_scenic_score_of_tree(forest, x, y):
    return scenic_score_left(forest, x, y) * scenic_score_right(forest, x, y) \
           * scenic_score_top(forest, x, y) * scenic_score_bottom(forest, x, y)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    forest = [[int(tree_size) for tree_size in row] for row in lines]
    scenic_scores = [[0 for _ in row] for row in forest]

    forest_size_x = len(lines)
    forest_size_y = len(lines[0])
    for x in range(forest_size_x):
        for y in range(forest_size_y):
            if tree_is_not_at_edge_of_forest(forest_size_x, forest_size_y, x, y):
                scenic_scores[x][y] = calculate_scenic_score_of_tree(forest, x, y)

    max_scenic_score = max([tree for column in scenic_scores for tree in column if tree])
    print(f'The tree with the best view has a scenic score of {str(max_scenic_score)}.')


if __name__ == '__main__':
    main()
