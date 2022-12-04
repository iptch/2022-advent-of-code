from enum import Enum

from common import load_lines


class Hand(Enum):
    ROCK = 0,
    PAPER = 1,
    SCISSOR = 2


class Goal(Enum):
    LOSS = 1,
    DRAW = 2,
    WIN = 3


def map_input_data_to_hands_interpreted_strategy(input_data: list[str]) -> list[tuple[Hand, Hand]]:
    hands = []
    opponent_map = {'A': Hand.ROCK, 'B': Hand.PAPER, 'C': Hand.SCISSOR}
    hand_map = {'X': Hand.ROCK, 'Y': Hand.PAPER, 'Z': Hand.SCISSOR}

    for line in input_data:
        opponent_code, hand_code = line.split(' ')
        hands.append((opponent_map[opponent_code], hand_map[hand_code]))
    return hands


def map_input_data_to_hands_elf_strategy(input_data: list[str]) -> list[tuple[Hand, Hand]]:
    hands = []
    opponent_map = {'A': Hand.ROCK, 'B': Hand.PAPER, 'C': Hand.SCISSOR}
    goal_map = {'X': Goal.LOSS, 'Y': Goal.DRAW, 'Z': Goal.WIN}

    for line in input_data:
        opponent_code, goal_code = line.split(' ')
        opponent_hand = opponent_map[opponent_code]
        goal = goal_map[goal_code]
        if opponent_hand == Hand.ROCK:
            if goal == Goal.WIN:
                own_hand = Hand.PAPER
            elif goal == Goal.LOSS:
                own_hand = Hand.SCISSOR
            else:
                own_hand = Hand.ROCK
        elif opponent_hand == Hand.PAPER:
            if goal == Goal.WIN:
                own_hand = Hand.SCISSOR
            elif goal == Goal.LOSS:
                own_hand = Hand.ROCK
            else:
                own_hand = Hand.PAPER
        else:  # opponent -> SCISSOR
            if goal == Goal.WIN:
                own_hand = Hand.ROCK
            elif goal == Goal.LOSS:
                own_hand = Hand.PAPER
            else:
                own_hand = Hand.SCISSOR

        hands.append((opponent_hand, own_hand))

    return hands


def get_total_score_for_round(opponent_hand: Hand, own_hand: Hand) -> int:
    score = 0

    # points depending on what own hand is
    hand_score_map = {Hand.ROCK: 1, Hand.PAPER: 2, Hand.SCISSOR: 3}
    score += hand_score_map[own_hand]

    # points depending on loss, draw or win
    if own_hand == opponent_hand:
        score += 3
        return score
    else:
        if own_hand == Hand.ROCK:
            score += 6 if opponent_hand == Hand.SCISSOR else 0
            return score
        if own_hand == Hand.PAPER:
            score += 6 if opponent_hand == Hand.ROCK else 0
            return score
        if own_hand == Hand.SCISSOR:
            score += 6 if opponent_hand == Hand.PAPER else 0
            return score


def get_total_score(hands: list[tuple[Hand, Hand]]) -> int:
    score = 0
    for opponent_hand, own_hand in hands:
        score += get_total_score_for_round(opponent_hand, own_hand)
    return score


if __name__ == "__main__":
    input_data = [line.strip() for line in load_lines(day=2)]
    hands = map_input_data_to_hands_interpreted_strategy(input_data)
    interpreted_total_score = get_total_score(map_input_data_to_hands_interpreted_strategy(input_data))
    print(f'Total score for interpreted strategy: {interpreted_total_score}')
    elf_strategy_total_score = get_total_score(map_input_data_to_hands_elf_strategy(input_data))
    print(f'Total score for actual elf strategy: {elf_strategy_total_score}')
