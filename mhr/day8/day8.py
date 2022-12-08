from common import load_lines


def load_grid(lines: list[str]) -> list[list[int]]:
    grid = []
    for line in lines:
        grid.append([int(char) for char in line])
    return grid


def build_visibility_grid(tree_grid: list[list[int]]) -> list[list[bool]]:
    visibility_grid = [[False for _ in range(len(tree_grid[0]))] for _ in tree_grid]
    for row_idx, row in enumerate(tree_grid):
        for col_idx, col in enumerate(row):
            if is_edge_tree(row_idx, col_idx, tree_grid):
                visibility_grid[row_idx][col_idx] = True
            elif is_tree_visible(row_idx, col_idx, tree_grid):
                visibility_grid[row_idx][col_idx] = True
    return visibility_grid


def is_edge_tree(row_idx: int, col_idx: int, grid: list[list[int]]) -> bool:
    return row_idx == 0 or col_idx == 0 or row_idx == len(grid) - 1 or col_idx == len(grid[0]) - 1


def is_tree_visible(row_idx: int, col_idx: int, grid: list[list[int]]) -> bool:
    visible_from_left = is_visible_in_line(col_idx, grid[row_idx])
    visible_from_right = is_visible_in_line(len(grid[row_idx]) - col_idx - 1, grid[row_idx][::-1])

    visible_from_top = is_visible_in_line(row_idx, [row[col_idx] for row in grid])
    visible_from_bottom = is_visible_in_line(len(grid) - row_idx - 1, [row[col_idx] for row in grid][::-1])

    return visible_from_left or visible_from_right or visible_from_top or visible_from_bottom


def is_visible_in_line(line_idx: int, line: list[int]) -> bool:
    is_visible = True
    highest_tree = -1
    height = line[line_idx]
    for idx in range(0, line_idx):
        if line[idx] >= highest_tree:
            highest_tree = line[idx]
    if highest_tree >= height:
        is_visible = False
    return is_visible


def count_visible(visibility_grid: list[list[bool]]) -> int:
    return sum([tree_visibility for row in visibility_grid for tree_visibility in row])


def calculate_scenic_score_grid(tree_grid: list[list[int]]) -> list[list[int]]:
    score_grid = [[0 for _ in range(len(tree_grid[0]))] for _ in tree_grid]
    for row_idx, row in enumerate(tree_grid):
        for col_idx, col in enumerate(tree_grid):
            if not is_edge_tree(row_idx, col_idx, tree_grid):
                score_grid[row_idx][col_idx] = calculate_scenic_score(row_idx, col_idx, tree_grid)
    return score_grid


def calculate_scenic_score(row_idx: int, col_idx: int, tree_grid: list[list[int]]) -> int:
    height = tree_grid[row_idx][col_idx]
    left = calculate_view_distance_in_line(tree_grid[row_idx][:col_idx + 1][::-1], height)
    right = calculate_view_distance_in_line(tree_grid[row_idx][col_idx:], height)
    top = calculate_view_distance_in_line([row[col_idx] for row in tree_grid][:row_idx + 1][::-1], height)
    bottom = calculate_view_distance_in_line([row[col_idx] for row in tree_grid][row_idx:], height)
    return left * right * top * bottom


def calculate_view_distance_in_line(line: list[int], height: int) -> int:
    distance = len(line) - 1  # default, when looking over the edge
    for idx, tree in enumerate(line[1:]):
        if tree >= height:
            distance = idx + 1
            break
    return distance


def max_scenic_score(scenic_score_grid: list[list[int]]) -> int:
    return max([score for row in scenic_score_grid for score in row])


if __name__ == '__main__':
    lines_ = load_lines(day=8, file_name='input.txt')
    grid_ = load_grid(lines_)
    visibility_grid_ = build_visibility_grid(grid_)
    n_visible_ = count_visible(visibility_grid_)
    print(f'Task 1: {n_visible_} visible trees from outside.')
    scenic_score_grid_ = calculate_scenic_score_grid(grid_)
    max_scenic_score_ = max_scenic_score(scenic_score_grid_)
    print(f'Task 2: {max_scenic_score_} maximum scenic score.')
