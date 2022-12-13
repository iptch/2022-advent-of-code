#!/usr/bin/env python

import click


def calc_score(world, x, y):
    p = int(world[y][x])
    x_max = len(world[0])
    y_max = len(world)
    score_right = 0
    score_left = 0
    score_up = 0
    score_down = 0

    # move right
    if x < x_max:
        i = x + 1
        while i < x_max:
            v = int(world[y][i])
            i = i + 1
            if v < p:
                score_right += 1
            else:
                score_right += 1
                break

    # move left
    if x >= 0:
        i = x - 1
        while i >= 0:
            v = int(world[y][i])
            i = i - 1
            if v < p:
                score_left += 1
            else:
                score_right += 1
                break

    # move down
    if y < y_max:
        i = y + 1
        while i < y_max:
            v = int(world[i][x])
            i = i + 1
            if v < p:
                score_down += 1
            else:
                score_right += 1
                break

    # score up
    if y >= 0:
        i = y - 1

        while i >= 0:
            v = int(world[i][x])
            i = i - 1
            if v < p:
                score_up += 1
            else:
                score_up += 1
                break

    score = max(score_right, 1) * max(score_left, 1) * max(score_down, 1) * max(score_up, 1)

    return score


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]
        x_max = len(lines[0])
        y_max = len(lines)

        scores = []

        print(f"x max: {x_max}, y max: {y_max}")

        for y in range(0, y_max):
            for x in range(0, x_max):
                s = calc_score(lines, x, y)
                print(f"check x={x}, y={y}, s={s}")
                scores.append(s)

        print(f"max score: {max(scores)}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
