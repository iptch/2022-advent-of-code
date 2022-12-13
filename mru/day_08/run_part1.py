#!/usr/bin/env python

import click


def is_edge(x, y, x_max, y_max):
    if x == 0 or x == x_max - 1 or y == 0 or y == y_max - 1:
        return True
    else:
        return False


def values_left(world, x, y):
    values = set()
    i = x - 1
    while i >= 0:
        v = int(world[y][i])
        values.add(v)
        i = i - 1

    return values


def values_right(world, x, y, x_max):
    values = set()
    i = x + 1
    while i < x_max:
        v = int(world[y][i])
        values.add(v)
        i = i + 1

    return values


def values_top(world, x, y):
    values = set()
    i = y - 1
    while i >= 0:
        v = int(world[i][x])
        values.add(v)
        i = i - 1

    return values


def values_bottom(world, x, y, y_max):
    values = set()
    i = y + 1
    while i < y_max:
        v = int(world[i][x])
        values.add(v)
        i = i + 1

    return values


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]
        x_max = len(lines[0])
        y_max = len(lines)
        y_min = 0
        x_min = 0

        count = 0

        print(f"x min: {x_min}, x max: {x_max}")
        print(f"y min: {y_min}, y max: {y_max}")

        for y in range(0, y_max):
            for x in range(0, x_max):

                p = int(lines[y][x])
                print(f"checking x={x}, y={y}, p={p}")
                if is_edge(x, y, x_max, y_max):
                    count += 1
                else:
                    v_r = values_right(lines, x, y, x_max)
                    if max(v_r) < p:
                        count += 1
                        continue

                    v_l = values_left(lines, x, y)
                    if max(v_l) < p:
                        count += 1
                        continue

                    v_t = values_top(lines, x, y)
                    if max(v_t) < p:
                        print(x, y, 'T')
                        count += 1
                        continue

                    v_b = values_bottom(lines, x, y, y_max)
                    if max(v_b) < p:
                        print(x, y, 'B')
                        count += 1
                        continue

        print(f"total count: {count}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
