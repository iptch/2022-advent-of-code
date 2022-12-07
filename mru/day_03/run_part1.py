#!/usr/bin/env python
import click

PRIOMAPPING = {}

for prio, char in enumerate("abcdefghijklmnopqrstuvwxyz"):
    PRIOMAPPING[char] = prio + 1
    PRIOMAPPING[char.upper()] = prio + 27


def parse(file_path: str):
    print(f"priority mapping = {PRIOMAPPING}")

    with open(file_path) as fp:
        lines = fp.readlines()

        found_priorities = []

        for line in lines:
            line = line.strip()
            n = int(len(line) / 2)
            part_1 = line[:n]
            part_2 = line[n:]
            common_item = set(part_1).intersection(part_2).pop()
            priority = PRIOMAPPING[common_item]
            found_priorities.append(priority)
            print(f"{line}, part1={part_1}, part2={part_2}, common={common_item}, priority={priority}")

        print(f"sum priorities: {sum(found_priorities)}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
