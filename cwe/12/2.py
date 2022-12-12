import dijkstar.algorithm
from dijkstar import Graph, find_path


def find_path_with_dijkstra(file_path):
    field, starts, end = create_field(file_path)
    graph = create_graph(field)
    shortest_paths = []
    for start in starts:
        try:
            sp = find_path(graph, start, end)
            shortest_paths.append(sp.total_cost)
        except dijkstar.algorithm.NoPathError:
            pass

    print(f'Shortest Path Length {min(shortest_paths)}')


def create_graph(field):
    height = len(field)
    width = len(field[0])
    graph = Graph()
    for row in range(height):
        for col in range(width):
            # check if up is possible
            if row > 0 and field[row - 1][col] - field[row][col] <= 1:
                graph.add_edge((row, col), (row - 1, col), 1)
            # check if dow is possible
            if row < height - 1 and field[row + 1][col] - field[row][col] <= 1:
                graph.add_edge((row, col), (row + 1, col), 1)
            # check if left is possible
            if col > 0 and field[row][col - 1] - field[row][col] <= 1:
                graph.add_edge((row, col), (row, col - 1), 1)
            # check if right is possible
            if col < width - 1 and field[row][col + 1] - field[row][col] <= 1:
                graph.add_edge((row, col), (row, col + 1), 1)
    return graph


def create_field(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    field = []
    starts = []
    end = None
    for idl, line in enumerate(lines):
        row = []
        for idc, column in enumerate(line):
            if column == 'S':
                column = 'a'
            elif column == 'E':
                end = (idl, idc)
                column = 'z'
            if column == 'a':
                starts.append((idl, idc))
            row.append(ord(column) - 97)

        field.append(row)
    return field, starts, end


# find_path_with_dijkstra('data_test.txt')
find_path_with_dijkstra('data_prod.txt')
