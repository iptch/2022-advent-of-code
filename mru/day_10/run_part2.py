#!/usr/bin/env python

import click

OPERATION_ADD_X = "addx"
OPERATION_NOOP = "noop"
LEN_WITH = 40


def get_v_index(pos):
    return pos % LEN_WITH


def get_h_index(pos):
    return int(pos / LEN_WITH)


def create_sprite(i):
    sprite = []
    for _ in range(0, LEN_WITH):
        sprite.append(".")

    if 0 <= i - 1 < LEN_WITH:
        sprite[i - 1] = '#'

    if 0 <= i < LEN_WITH:
        sprite[i] = '#'

    if 0 <= i + 1 < LEN_WITH:
        sprite[i + 1] = '#'

    return sprite


def get_pixel(pos, sprite):
    c = sprite[pos % LEN_WITH]
    if c == '#':
        return '#'
    else:
        return '.'


def parse(file_path: str):
    screen = []
    for _ in range(0, 6):
        pixels = []
        for _ in range(0, 40):
            pixels.append("")
        screen.append(pixels)

    x = 1
    pos = 0

    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]

        for line in lines:

            if OPERATION_NOOP in line:
                sprite = create_sprite(x)
                p = get_pixel(pos, sprite)
                print(sprite)
                print("p:", p)
                print("s:", sprite[pos % LEN_WITH])
                print("x:", x)

                screen[get_h_index(pos)][get_v_index(pos)] = p
                pos += 1

            if OPERATION_ADD_X in line:
                sprite = create_sprite(x)
                p = get_pixel(pos, sprite)
                print(sprite, 0)
                print("p:", p)
                print("s:", sprite[pos % LEN_WITH])
                print("x:", x)
                screen[get_h_index(pos)][get_v_index(pos)] = p
                pos += 1

                p = get_pixel(pos, sprite)
                print(sprite, 1)
                print("p:", p)
                print("s:", sprite[pos % LEN_WITH])
                print("x:", x)
                x += int(line.split(" ")[1])

                screen[get_h_index(pos)][get_v_index(pos)] = p
                pos += 1

        for h in range(0, len(screen)):
            out = ""
            for v in range(0, len(screen[h])):
                out += screen[h][v]
            print(out)

        print(f"screen: h={len(screen)}, v={len(screen[0])}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
