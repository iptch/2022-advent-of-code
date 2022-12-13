#!/usr/bin/env python

from functools import cmp_to_key

import click


def sign(n):
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


def comp(left, right):
    t_left = type(left)
    t_right = type(right)
    if t_left == int and t_right == int:
        return sign(left - right)
    elif t_left == list and t_right == int:
        return comp(left, [right])
    elif t_left == int and t_right == list:
        return comp([left], right)
    else:
        n = min(len(left), len(right))
        for i in range(0, n):
            r = comp(left[i], right[i])
            if r > 0:
                return r
            if r < 0:
                return r
            if r == 0 and len(left) == len(right) and i == n - 1:
                return r

        return sign(len(left) - len(right))


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]
        start_marker = [[2]]
        end_marker = [[6]]
        packets = [start_marker, end_marker]
        for i, line in enumerate(lines):

            action = i % 3
            if action == 0 or action == 1:
                packets.append(eval(line))

        packets = sorted(packets, key=cmp_to_key(comp))
        for p in packets:
            print(p)

        index_start_marker = packets.index(start_marker) + 1
        index_end_marker = packets.index(end_marker) + 1
        print(f"s: {index_start_marker}, e: {index_end_marker},  decoder key: {index_start_marker * index_end_marker}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
