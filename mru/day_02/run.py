#!/usr/bin/env python
import click

ROCK = 1
PAPER = 2
SCISSOR = 3

MAPPING = {
    ROCK: 'ROCK',
    PAPER: 'PAPER',
    SCISSOR: 'SCISSOR'
}

COLUMN_1_MAPPING = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSOR
}

COLUMN_2_MAPPING_WIN = {
    ROCK: PAPER,
    PAPER: SCISSOR,
    SCISSOR: ROCK
}

COLUMN_2_MAPPING_LOSE = {
    ROCK: SCISSOR,
    PAPER: ROCK,
    SCISSOR: PAPER
}

COLUMN_2_MAPPING_DRAW = {
    ROCK: ROCK,
    PAPER: PAPER,
    SCISSOR: SCISSOR
}

STRATEGY_RESULT = {
    'X': COLUMN_2_MAPPING_LOSE,
    'Y': COLUMN_2_MAPPING_DRAW,
    'Z': COLUMN_2_MAPPING_WIN
}

STRATEGY_NORMAL = {
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSOR
}


def parse(file_path: str, strategy: str):
    with open(file_path) as fp:
        lines = fp.readlines()
        scores = []

        for line in lines:
            line = line.strip()
            c1, c2 = line.split()
            scores.append(get_score(c1, c2, strategy))

        print(f"total score: {sum(scores)}")


def get_score(column_1: str, column_2: str, strategy: str) -> int:
    c1 = COLUMN_1_MAPPING[column_1]
    if strategy.upper() == 'R':
        c2 = STRATEGY_RESULT[column_2][c1]
    elif strategy.upper() == 'M':
        c2 = STRATEGY_NORMAL[column_2]
    else:
        raise RuntimeError(f"unsupported strategy {strategy}")

    print(f"{column_1} ({c1}, {MAPPING[c1]}), {column_2} ({c2}, {MAPPING[c2]})")
    score_lost = 0
    score_draw = 3
    score_win = 6

    if c1 == c2:
        return c2 + score_draw
    elif c1 == ROCK and c2 == PAPER:
        return c2 + score_win
    elif c1 == ROCK and c2 == SCISSOR:
        return c2 + score_lost
    elif c1 == PAPER and c2 == ROCK:
        return c2 + score_lost
    elif c1 == PAPER and c2 == SCISSOR:
        return c2 + score_win
    elif c1 == SCISSOR and c2 == ROCK:
        return c2 + score_win
    elif c1 == SCISSOR and c2 == PAPER:
        return c2 + score_lost

    raise RuntimeError(f"unsupported draw c1={c1}, c2={c2}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--strategy', default='N')
def cli(file, strategy):
    parse(file, strategy)


if __name__ == '__main__':
    cli()
