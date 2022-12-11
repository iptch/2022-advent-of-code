import os

# TODO: use pathlib
PROJECT_ROOT_PATH = os.path.dirname((__file__))


def load_lines(day: int, file_name: str = 'input.txt', skip_empty_lines: bool = False) -> list[str]:
    with open(f'{PROJECT_ROOT_PATH}/day{day}/{file_name}') as infile:
        lines = [line.strip() for line in infile.readlines()]
        if skip_empty_lines:
            lines = [line for line in lines if line != '']
        return lines
