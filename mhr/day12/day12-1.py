from common import load_lines

import networkx as nx


def to_height_map(lines: list[str]) -> list[list[int]]:
    height_map = []
    for line in lines:
        height_map.append([ord(char) if char not in {'S', 'E'} else char for char in line])
    return height_map


def get_shortest_path(height_map: list[list[int]]) -> int:
    n_rows = len(height_map)
    n_cols = len(height_map[0])

    position_to_node_idx_map = dict()
    node_idx_runner = 0
    start_node_idx = -1
    target_node_idx = -1
    start_row_idx, start_col_idx = -1, -1
    target_row_idx, target_col_idx = -1, 1
    for row in range(n_rows):
        for col in range(n_cols):
            if height_map[row][col] == 'S':
                start_node_idx = node_idx_runner
                start_row_idx, start_col_idx = row, col
            if height_map[row][col] == 'E':
                target_node_idx = node_idx_runner
                target_row_idx, target_col_idx = row, col
            position_to_node_idx_map[(row, col)] = node_idx_runner
            node_idx_runner += 1

    height_map[start_row_idx][start_col_idx] = ord('a')
    height_map[target_row_idx][target_col_idx] = ord('z')

    # ---- PRINT
    print(f'Start node {start_node_idx}: ({start_row_idx}, {start_col_idx})')
    print(f'Target node {target_node_idx}: ({target_row_idx}, {target_col_idx})')
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

    shortest_path = get_shortest_path(height_map_)

    print(f'Task 1: {shortest_path} is the shortest possible path from start to target')
