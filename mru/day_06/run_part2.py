#!/usr/bin/env python
import click


def parse(file_path: str):
    with open(file_path) as fp:
        lines = fp.readlines()

        stream = lines[0].strip()

        window_start = 0
        window_end = 14
        for i, _ in enumerate(stream):
            if window_end > len(stream):
                break
            marker = stream[window_start:window_end]
            unique = set([m for m in marker])
            print(window_start, window_end, marker, unique)
            if len(unique) == 14:
                break

            window_start += 1
            window_end += 1

       
@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
