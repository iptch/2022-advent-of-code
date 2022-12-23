import os

# TODO: use pathlib
PROJECT_ROOT_PATH = os.path.dirname((__file__))


def load_lines(day: int, file_name: str = 'input.txt', skip_empty_lines: bool = False, do_strip: bool = True) -> list[str]:
    with open(f'{PROJECT_ROOT_PATH}/day{day}/{file_name}') as infile:
        lines = infile.readlines()
        if do_strip:
            lines = [line.strip() for line in lines]
        if skip_empty_lines:
            lines = [line for line in lines if line != '']
        return lines


def print_grid(grid: list[list[str]]) -> None:
    for line in grid:
        print(''.join(line))
