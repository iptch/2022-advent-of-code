#!/usr/bin/env python
import click


def parse(file_path: str, n: int):
    with open(file_path) as fp:
        values = []

        current_val = 0
        lines = fp.readlines()
        lines.append('')

        for line in lines:
            line = line.strip()
            if len(line) == 0:
                values.append(current_val)
                current_val = 0
            else:
                current_val += int(line)

        values = sorted(values, reverse=True)
        top_values = values[0:n]
        print(f"top {n} {top_values}")
        print(f"sum top {n} {sum(top_values)}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--top', default=1)
def cli(file, top):
    parse(file, top)


if __name__ == '__main__':
    cli()
