#!/usr/bin/env python
import click


def parse(file_path: str):
    with open(file_path) as fp:
        lines = fp.readlines()
        count = 0

        for line in lines:
            line = line.strip()
            part_1, part_2 = line.split(',')
            part_1_from, part_1_to = [int(x) for x in part_1.split('-')]
            part_2_from, part_2_to = [int(x) for x in part_2.split('-')]
            part1_set = set(range(part_1_from, part_1_to + 1))
            part2_set = set(range(part_2_from, part_2_to + 1))

            intersection = part1_set.intersection(part2_set)
            
            print(line, len(intersection) > 0)
            if len(intersection) > 0:
                count += 1

        print(f"found: {count}")


def get_f(x, y, f):
    return f(f(x), f(y))


def get_range(x, y):
    return range(get_f(x, y, min), get_f(x, y, max) + 1)


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
