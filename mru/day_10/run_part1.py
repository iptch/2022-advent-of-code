#!/usr/bin/env python

import click


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]

        for line in lines:
            print(line)


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
