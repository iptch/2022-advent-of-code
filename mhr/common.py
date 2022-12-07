import os

# TODO: use pathlib
PROJECT_ROOT_PATH = os.path.dirname((__file__))


def load_lines(day: int, file_name: str = 'input.txt') -> list[str]:
    with open(f'{PROJECT_ROOT_PATH}/day{day}/{file_name}') as infile:
        return [line.strip() for line in infile.readlines()]
