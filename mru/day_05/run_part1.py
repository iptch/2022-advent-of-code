#!/usr/bin/env python
import click

MAX_LINE_TO_PARSE = 7
INSTRUCTION = 'move'

EMPTY = ' '

SHIFT = 4
POS_1 = 1
POS_2 = POS_1 + SHIFT
POS_3 = POS_2 + SHIFT
POS_4 = POS_3 + SHIFT
POS_5 = POS_4 + SHIFT
POS_6 = POS_5 + SHIFT
POS_7 = POS_6 + SHIFT
POS_8 = POS_7 + SHIFT
POS_9 = POS_8 + SHIFT

STACK_1 = []
STACK_2 = []
STACK_3 = []
STACK_4 = []
STACK_5 = []
STACK_6 = []
STACK_7 = []
STACK_8 = []
STACK_9 = []

STACKS = {
    1: STACK_1,
    2: STACK_2,
    3: STACK_3,
    4: STACK_4,
    5: STACK_5,
    6: STACK_6,
    7: STACK_7,
    8: STACK_8,
    9: STACK_9
}


def parse(file_path: str):
    with open(file_path) as fp:
        lines = fp.readlines()

        for i, line in enumerate(lines):
            line = line.strip()

            if i > MAX_LINE_TO_PARSE:
                # instructions

                print("***")
                for s in range(1, 10):
                    print(STACKS[s])
                print("***")

                if INSTRUCTION in line:
                    _, n, _, move_from, _, move_to = line.split(' ')
                    n = int(n)
                    move_from = int(move_from)
                    move_to = int(move_to)
                    print('instruction', n, move_from, move_to)
                    for _ in range(0, n):
                        e = STACKS[move_from].pop()
                        STACKS[move_to].append(e)
                        print(' copy', e)

            else:
                if line[POS_1] != EMPTY:
                    STACK_1.insert(0, line[POS_1])
                if line[POS_2] != EMPTY:
                    STACK_2.insert(0, line[POS_2])
                if line[POS_3] != EMPTY:
                    STACK_3.insert(0, line[POS_3])
                if line[POS_4] != EMPTY:
                    STACK_4.insert(0, line[POS_4])
                if line[POS_5] != EMPTY:
                    STACK_5.insert(0, line[POS_5])
                if line[POS_6] != EMPTY:
                    STACK_6.insert(0, line[POS_6])
                if line[POS_7] != EMPTY:
                    STACK_7.insert(0, line[POS_7])
                if line[POS_8] != EMPTY:
                    STACK_8.insert(0, line[POS_8])
                if line[POS_9] != EMPTY:
                    STACK_9.insert(0, line[POS_9])

        # parse input

    print(STACK_1)
    print(STACK_2)
    print(STACK_3)
    print(STACK_4)
    print(STACK_5)
    print(STACK_6)
    print(STACK_7)
    print(STACK_8)
    print(STACK_9)

    print(
        f"{STACK_1.pop()}{STACK_2.pop()}{STACK_3.pop()}{STACK_4.pop()}{STACK_5.pop()}{STACK_6.pop()}{STACK_7.pop()}{STACK_8.pop()}{STACK_9.pop()}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
