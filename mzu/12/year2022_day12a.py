import string

from aocd import data
from extended_int import int_inf

DAY = '12'
PART = 'a'


def read_height_map(lines):
    height_code = {string.ascii_lowercase[i]: i + 1 for i in range(len(string.ascii_lowercase))}
    height_code['E'] = 27
    height_code['S'] = 0
    height_map = [[height_code[height] for height in row] for row in lines]
    return height_map


def find_start_position(height_map):
    for row_idx in range(len(height_map)):
        for col_idx in range(len(height_map[0])):
            if height_map[row_idx][col_idx] == 0:
                return row_idx, col_idx


def node_exists(row_idx, col_idx, number_of_rows, number_of_cols):
    return 0 <= row_idx <= number_of_rows - 1 and 0 <= col_idx <= number_of_cols - 1


def ascend_is_not_too_steep(current_height, neighbor_height):
    return neighbor_height - current_height <= 1


def get_valid_neighbors(row_idx, col_idx, height_map):
    neighbors = [(row_idx - 1, col_idx), (row_idx, col_idx - 1), (row_idx, col_idx + 1), (row_idx + 1, col_idx)]
    return [neighbor for neighbor in neighbors if
            node_exists(neighbor[0], neighbor[1], len(height_map), len(height_map[0]))
            and ascend_is_not_too_steep(height_map[row_idx][col_idx], height_map[neighbor[0]][neighbor[1]])]


def find_optimal_path_with_dijkstra(distances, previous_hops, height_map, unvisited_nodes):
    while unvisited_nodes:
        current_row_idx, current_col_idx = None, None
        for (row_idx, col_idx) in unvisited_nodes:
            if current_row_idx is None and current_col_idx is None:
                current_row_idx, current_col_idx = row_idx, col_idx
            elif distances[row_idx][col_idx] < distances[current_row_idx][current_col_idx]:
                current_row_idx, current_col_idx = row_idx, col_idx

        neighbors = get_valid_neighbors(current_row_idx, current_col_idx, height_map)
        for (neighbor_row_idx, neighbor_col_idx) in neighbors:
            new_distance = distances[current_row_idx][current_col_idx] + 1
            if new_distance < distances[neighbor_row_idx][neighbor_col_idx]:
                distances[neighbor_row_idx][neighbor_col_idx] = new_distance
                previous_hops[neighbor_row_idx][neighbor_col_idx] = (current_row_idx, current_col_idx)

        unvisited_nodes.remove((current_row_idx, current_col_idx))


def find_end_position(height_map):
    for row_idx in range(len(height_map)):
        for col_idx in range(len(height_map[0])):
            if height_map[row_idx][col_idx] == 27:
                return row_idx, col_idx


def get_optimal_path(previous_hops, goal_row_idx, goal_col_idx, start_row_idx, start_col_idx):
    optimal_path = [(goal_row_idx, goal_col_idx)]
    next_row_idx, next_col_idx = previous_hops[goal_row_idx][goal_col_idx]
    while next_row_idx != start_row_idx or next_col_idx != start_col_idx:
        optimal_path.append((next_row_idx, next_col_idx))
        next_row_idx, next_col_idx = previous_hops[next_row_idx][next_col_idx]
    optimal_path.append((start_row_idx, start_col_idx))
    return optimal_path


def solve(lines):
    height_map = read_height_map(lines)
    start_row_idx, start_col_idx = find_start_position(height_map)
    current_row_idx, current_col_idx = start_row_idx, start_col_idx
    # distances = shortest distance (= fewest steps) from source_node to any node
    distances = [[int_inf for _ in row] for row in lines]
    distances[current_row_idx][current_col_idx] = 0
    # previous_hops = previous node on shortest path (= path with shortest amount of steps) back to source_node
    previous_hops = [[None for _ in row] for row in lines]
    unvisited_nodes = [(row_idx, col_idx) for row_idx in range(len(height_map)) for col_idx in range(len(height_map[0]))]
    find_optimal_path_with_dijkstra(distances, previous_hops, height_map, unvisited_nodes)
    goal_row_idx, goal_col_idx = find_end_position(height_map)
    optimal_path = get_optimal_path(previous_hops, goal_row_idx, goal_col_idx, start_row_idx, start_col_idx)
    return optimal_path


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    optimal_path = solve(lines)
    print(f'It took {str(len(optimal_path) - 1)} steps to go to the top!')
    print(f'The optimal path is:')
    for (row_idx, col_idx) in optimal_path:
        print(f'({str(row_idx)}, {str(col_idx)})')


if __name__ == '__main__':
    main()
