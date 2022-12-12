import copy
from tqdm import tqdm
import networkx as nx

from common import load_lines


def to_height_map(lines: list[str]) -> list[list[int]]:
    height_map = []
    for line in lines:
        height_map.append([ord(char) if char not in {'S', 'E'} else char for char in line])
    return height_map


def find_possible_starting_points(height_map: list[list[int]]) -> list[tuple[int, int]]:
    starting_points = list()
    n_rows = len(height_map)
    n_cols = len(height_map[0])
    for row in range(n_rows):
        for col in range(n_cols):
            if height_map[row][col] == 'S' or height_map[row][col] == ord('a'):
                starting_points.append((row, col))
    return starting_points


def get_shortest_path(height_map: list[list[int]], starting_point: tuple[int, int]) -> int:
    n_rows = len(height_map)
    n_cols = len(height_map[0])

    position_to_node_idx_map = dict()
    target_node_idx = -1
    start_row_idx, start_col_idx = -1, -1
    target_row_idx, target_col_idx = -1, -1

    node_idx_runner = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if height_map[row][col] == 'S':
                # start_node_idx = node_idx_runner
                start_row_idx, start_col_idx = row, col
            if height_map[row][col] == 'E':
                target_node_idx = node_idx_runner
                target_row_idx, target_col_idx = row, col
            position_to_node_idx_map[(row, col)] = node_idx_runner
            node_idx_runner += 1

    height_map[start_row_idx][start_col_idx] = ord('a')
    height_map[target_row_idx][target_col_idx] = ord('z')

    start_node_idx = position_to_node_idx_map[starting_point]
    start_row_idx, start_col_idx = starting_point
    # ---- PRINT
    # print(f'Start node {start_node_idx}: ({start_row_idx}, {start_col_idx})')
    # print(f'Target node {target_node_idx}: ({target_row_idx}, {target_col_idx})')
    # ----

    graph = nx.DiGraph()
    edges = []
    for (row, col), node_idx in position_to_node_idx_map.items():
        graph.add_node(node_idx)

        # up
        if row > 0 and height_map[row - 1][col] - height_map[row][col] <= 1:
            edges.append((node_idx, position_to_node_idx_map[(row - 1, col)]))

        # down
        if row < n_rows - 1 and height_map[row + 1][col] - height_map[row][col] <= 1:
            edges.append((node_idx, position_to_node_idx_map[(row + 1, col)]))

        # left
        if col > 0 and height_map[row][col - 1] - height_map[row][col] <= 1:
            edges.append((node_idx, position_to_node_idx_map[(row, col - 1)]))

        # right
        if col < n_cols - 1 and height_map[row][col + 1] - height_map[row][col] <= 1:
            edges.append((node_idx, position_to_node_idx_map[(row, col + 1)]))

    graph.add_edges_from(edges)
    return len(nx.shortest_path(graph, source=start_node_idx, target=target_node_idx)) - 1


if __name__ == '__main__':
    lines_ = load_lines(day=12, file_name='input.txt', skip_empty_lines=True)
    height_map_ = to_height_map(lines_)
    starting_points_ = find_possible_starting_points(height_map_)

    path_lengths = []
    for starting_point in tqdm(starting_points_):
        try:
            path_lengths.append(get_shortest_path(copy.deepcopy(height_map_), starting_point))
        except nx.NetworkXNoPath:
            pass

    print(f'Task 1: {min(path_lengths)} is the shortest path from start to finish for all possible starting points')
