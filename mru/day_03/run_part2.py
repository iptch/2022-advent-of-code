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

        total_priorities = []
        group_rucksack = []

        for i, line in enumerate(lines):
            line = line.strip()
            group_rucksack.append(line)
            if i % 3 == 2:
                common_item = set(group_rucksack[0]).intersection(set(group_rucksack[1])).intersection(
                    set(group_rucksack[2])).pop()
                priority = PRIOMAPPING[common_item]
                total_priorities.append(priority)
                group_rucksack = []

                print(f"from={i - 2}, to={i + 1}, common item = {common_item}, priority = {priority}")

        print(f"sum priorities = {sum(total_priorities)}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
