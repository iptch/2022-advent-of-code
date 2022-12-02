from aocd import data

DAY = '2'
PART = 'a'

SCORE_PER_SHAPE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

WINNING_OUTCOMES = [
    ('A', 'Y'),
    ('B', 'Z'),
    ('C', 'X')
]

DRAW_OUTCOMES = [
    ('A', 'X'),
    ('B', 'Y'),
    ('C', 'Z')
]


def get_score_for_selected_shape(shape):
    return SCORE_PER_SHAPE[shape]


def outcome_is_a_draw(outcome):
    return outcome in DRAW_OUTCOMES


def outcome_is_a_win(outcome):
    return outcome in WINNING_OUTCOMES


def get_score_for_outcome(game_round):
    if outcome_is_a_win(game_round):
        return 6
    elif outcome_is_a_draw(game_round):
        return 3
    else:
        return 0


def calculate_score(game_round):
    score_selected_shape = get_score_for_selected_shape(game_round[1])
    score_round_outcome = get_score_for_outcome(game_round)
    return score_selected_shape + score_round_outcome


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    # lines = [
    #     'A Y',
    #     'B X',
    #     'C Z'
    # ]

    lines = data.splitlines()

    strategy_guide = [(line.split(' ')[0], line.split(' ')[1]) for line in lines]
    score_per_round = [calculate_score(game_round) for game_round in strategy_guide]

    total_score = sum(score_per_round)
    print(f'My total score would be {str(total_score)}.')


if __name__ == '__main__':
    main()
