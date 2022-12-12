import heapq
from collections import defaultdict

PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            row = []
            for c in line:
                if c != '\n':
                    row.append(c)
            res.append(row)
    return res


def height(char):
    res = ord(char) - 97
    if char == 'S':
        res = 0
    if char == 'E':
        res = 25
    return res


def build_graph(heightmap):
    graph = {}
    start, end = None, None
    m, n = len(heightmap), len(heightmap[0])
    for i in range(m):
        for j in range(n):
            graph[(i, j)] = []
            node_val = heightmap[i][j]
            node_height = height(node_val)
            if node_val == 'S':
                start = (i, j)
            if node_val == 'E':
                end = (i, j)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n:
                    neigh_height = height(heightmap[x][y])
                    if neigh_height - node_height < 2:
                        graph[(i, j)].append((x, y))
    return graph, start, end


def shortest_path(graph, start, end):
    visited = set()
    queue = []
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        dist, node = heapq.heappop(queue)
        visited.add(node)

        for neigh in graph[node]:
            if neigh in visited:
                continue

            new_dist = dist + 1
            if distances[neigh] > new_dist:
                distances[neigh] = new_dist
                heapq.heappush(queue, (new_dist, neigh))

    return distances[end]


def part1():
    heightmap = load()
    graph, start, end = build_graph(heightmap)
    sp = shortest_path(graph, start, end)
    print(sp)


def part2():
    heightmap = load()
    graph, start, end = build_graph(heightmap)
    best = shortest_path(graph, start, end)
    m, n = len(heightmap), len(heightmap[0])
    for i in range(m):
        for j in range(n):
            if heightmap[i][j] == 'a':
                sp = shortest_path(graph, (i, j), end)
                best = min(best, sp)
    print(best)


if __name__ == '__main__':
    part1()
    part2()
