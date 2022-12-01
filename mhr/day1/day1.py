import numpy as np


def load_input() -> list[str]:
    with open('input.txt') as infile:
        return infile.readlines()


def find_calories_of_top_n_elves(input_data: list[str], top_n: int = 1) -> int:
    calories_per_elve = []

    calorie_counter = 0
    for idx, entry in enumerate(input_data):
        if entry != '\n':
            calorie_counter += int(entry)
        else:
            calories_per_elve.append(calorie_counter)
            calorie_counter = 0

        if idx == len(input_data) - 1:
            calories_per_elve.append(calorie_counter)

    indices_of_top_carrying_elves = np.array(calories_per_elve).argsort()[-top_n:][::-1]

    return sum([calories_per_elve[idx] for idx in indices_of_top_carrying_elves])


if __name__ == "__main__":
    print(find_calories_of_top_n_elves(load_input(), top_n=3))
