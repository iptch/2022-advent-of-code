#!/usr/bin/env python

import math

import click


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))


def get_neighbours(point, target, world):
    y_max = len(world)
    x_max = len(world[0])
    # print("get_neighbours", point)
    candidates = []

    p = world[point[1]][point[0]]
    for ops in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        n_pos = point[0] + ops[0], point[1] + ops[1]

        # print(0 <= n_pos[0] < x_max, n_pos)
        # print(0 <= n_pos[1] < y_max, n_pos)

        alphabet = ['S', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                    't', 'u', 'v', 'w', 'x', 'y', 'z', 'E']

        if 0 <= n_pos[0] < x_max and 0 <= n_pos[1] < y_max:
            n = world[n_pos[1]][n_pos[0]]
            # print(n, p)

            n_index = alphabet.index(n)
            p_index = alphabet.index(p)
            # if abs(n_index - p_index) <= 1:
            if n_index - p_index <= 1:
                # if n_index - p_index == 1 or n_index - p_index == 0:
                candidates.append(n_pos)

    # candidates = sorted(candidates, key=lambda x: distance(x, target), reverse=False)
    return candidates


def print_world(world):
    for row in world:
        out = ""
        for column in row:
            out += str(column)
        print(out)


def bfs(root, target, world):
    # bfs_traversal = list()
    queue = list()
    visited = set()

    parent = dict()
    parent[root] = None

    # push the root node to the queue and mark it as visited
    queue.append(root)
    visited.add(root)

    # loop until the queue is empty
    path_found = False
    while queue:
        # pop the front node of the queue and add it to bfs_traversal
        current_node = queue.pop(0)
        # bfs_traversal.append(current_node)

        if current_node == target:
            path_found = True
            print("found", current_node)
            break

        # check all the neighbour nodes of the current node
        # print("get_neighbours bfs", current_node)
        for next_node in get_neighbours(current_node, target, world):

            # if the neighbour nodes are not already visited,
            # push them to the queue and mark them as visited

            if next_node not in visited:
                # print(f"visiting {next_node}, {world[next_node[1]][next_node[0]]}")
                visited.add(next_node)
                parent[next_node] = current_node
                queue.append(next_node)

    path = []
    if path_found:
        path.append(target)
        while parent[target] is not None:
            path.append(parent[target])
            target = parent[target]
        path.reverse()

    return path, parent


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]

        start_char = "S"
        start_pos = None
        end_char = "E"
        end_pos = None

        world = []

        for h, row in enumerate(lines):
            column = []
            for v, char in enumerate(row):
                if char == start_char:
                    column.append(char)
                    start_pos = (v, h)
                elif char == end_char:
                    column.append(char)
                    end_pos = (v, h)
                else:
                    column.append(char)
            world.append(column)

        print(f"got world {len(world) - 1} x {len(world[0]) - 1}")

        A = []
        for y, row in enumerate(world):
            for x, column in enumerate(row):
                if column == 'a':
                    A.append((x, y))
        found = []
        for a in A:
            path, nodes = bfs(a, end_pos, world)
            print("found", len(path) - 1)
            if len(path) != 0:
                found.append(len(path) - 1)

        found = sorted(found, reverse=False)

        print(found[:10])


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
