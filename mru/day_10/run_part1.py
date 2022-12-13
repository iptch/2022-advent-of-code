#!/usr/bin/env python

import click

OPERATION_ADD_X = "addx"
OPERATION_NOOP = "noop"


def signal_strength(c, history):
    return c * history[c]


def parse(file_path: str):
    cycle_count = 1
    history = {}
    x = 1
    history[1] = x

    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]

        for line in lines:

            if OPERATION_NOOP in line:
                history[cycle_count + 1] = x
                cycle_count += 1
            if OPERATION_ADD_X in line:
                history[cycle_count + 1] = x
                x += int(line.split(" ")[1])
                history[cycle_count + 2] = x
                cycle_count += 2

        print(f"cycles: {cycle_count}, x={x}")

        c_20 = signal_strength(20, history)
        c_60 = signal_strength(60, history)
        c_100 = signal_strength(100, history)
        c_140 = signal_strength(140, history)
        c_180 = signal_strength(180, history)
        c_220 = signal_strength(220, history)
        sum_signal = c_20 + c_60 + c_100 + c_140 + c_180 + c_220
        print(f"sum: {sum_signal}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
