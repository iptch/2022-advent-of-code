import os

# TODO: use pathlib
PROJECT_ROOT_PATH = os.path.dirname((__file__))

def load_input(day: int) -> list[str]:
    with open(f'{PROJECT_ROOT_PATH}/day{day}/input.txt') as infile:
        return infile.readlines()
