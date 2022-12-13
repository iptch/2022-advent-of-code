#!/usr/bin/env python

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
        index = 1
        left = None
        right = None
        found = []
        for i, line in enumerate(lines):

            action = i % 3
            if action == 0:
                left = eval(line)
            elif action == 1:
                right = eval(line)
            else:
                c = comp(left, right)
                print(f"i: {index}, l: {left}, r: {right}, c: {c}")
                if c < 0:
                    found.append(index)
                index += 1

        print(f"found index: {len(found)}, sum: {sum(found)}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
