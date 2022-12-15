#!/usr/bin/env python

import click


def get_f(world, f):
    x = f([x for x, _ in world])
    y = f([y for _, y in world])
    return x, y


def get_point(x, y, y_max, world):
    if (x, y) not in world and y <= y_max + 1:
        return x, y
    else:
        return None


def print_world(world):
    x_max, y_max = get_f(world, max)
    x_min, y_min = get_f(world, min)
    print(f"x max: {x_max} y_max: {y_max}")
    print(f"x min: {x_min} y_min: {y_min}")
    for y in range(y_min, y_max + 1):
        out = ""
        for x in range(x_min, x_max + 1):
            if (x, y) in world:
                out += world[(x, y)]
            else:
                out += '.'
        print(out)


def parse(file_path: str):
    with open(file_path) as fp:
        world = {}
        start_xy = (500, 0)
        # world[start_xy] = '+'

        lines = [i.strip().split(" -> ") for i in fp.readlines()]
        for line in lines:
            xy = [(int(p.split(',')[0]), int(p.split(',')[1])) for p in line]
            for (x1, y1), (x2, y2) in zip(xy, xy[1:]):
                # print(x1, x2, y1, y2)
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        world[(x, y)] = '#'
        # print(world)
        print_world(world)

        cycles = 0

        x_max, y_max = get_f(world, max)

        while True:

            x, y = start_xy
            print(f"cycle: {cycles}")

            while True:
                # print('x, y', x, y)
                ops = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
                move_down = get_point(*ops[0], y_max, world)
                move_left = get_point(*ops[1], y_max, world)
                move_right = get_point(*ops[2], y_max, world)
                # print(move_left, move_down, move_right)
                # print_world(world)

                if move_down:
                    x, y = move_down
                    # print('move_down', x, y)
                    continue

                if move_left:
                    x, y = move_left
                    # print('move_left', x, y)
                    continue

                if move_right:
                    x, y = move_right
                    # print('move_right', x, y)
                    continue

                break

            if (x, y) == (500, 0):
                cycles += 1
                break

            world[(x, y)] = 'o'
            cycles += 1

        print_world(world)
        print(f"cycle: {cycles}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
