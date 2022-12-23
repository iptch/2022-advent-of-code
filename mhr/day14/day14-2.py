from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib import animation
from functools import partial

from common import load_lines


@dataclass
class Segment:
    x_start: int
    x_end: int
    y_start: int
    y_end: int
    is_horizontal: int

    def __init__(self, x_start: int, x_end: int, y_start: int, y_end: int) -> None:
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.is_horizontal = x_start != x_end
        if self.is_horizontal:
            assert self.y_start == self.y_end


@dataclass
class Path:
    segments: list[Segment]


def to_paths(path_data: list[str]) -> list[Path]:
    paths = list()
    for line in path_data:
        points = line.split(' -> ')
        segments = []
        for idx, point in enumerate(points[:-1]):
            x_start, y_start = point.split(',')
            x_end, y_end = points[idx + 1].split(',')
            segments.append(Segment(int(x_start), int(x_end), int(y_start), int(y_end)))
        paths.append(Path(segments))
    return paths


def build_occupancy_grid(paths: list[Path]) -> list[list[str]]:
    max_x = max([segment.x_start for path in paths for segment in path.segments] + [segment.x_end for path in paths for segment in path.segments])
    max_y = max([segment.y_start for path in paths for segment in path.segments] + [segment.y_end for path in paths for segment in path.segments])

    grid = list([['.' for _ in range(max_x * 2)] for _ in range(max_y + 1)])  # make it wide enough for the pyramid

    for path in paths:
        for segment in path.segments:
            if segment.is_horizontal:
                for x_idx in range(min(segment.x_start, segment.x_end), max(segment.x_start, segment.x_end) + 1):
                    grid[segment.y_start][x_idx] = "#"
            else:
                for y_idx in range(min(segment.y_start, segment.y_end), max(segment.y_start, segment.y_end) + 1):
                    grid[y_idx][segment.x_start] = "#"
    return grid


def simulate(grid: list[list[str]], grid_listener: list):
    width = len(grid[0])
    grid.append(width * ['.'])
    grid.append(width * ['#'])  # the almost infinite floor

    corns_at_rest = 0

    while True:
        if corns_at_rest % 50 == 0:
            print(corns_at_rest)
            vis_grid = [[char for char in line[330:730]] for line in grid]
            grid_listener.append(vis_grid)

        x, y = 500, 0
        corn_done = False

        while not corn_done:
            if grid[y + 1][x] not in {'#', 'o'}:  # down
                y += 1
                continue
            elif grid[y + 1][x - 1] not in {'#', 'o'}:  # left + down
                y += 1
                x -= 1
                continue
            elif grid[y + 1][x + 1] not in {'#', 'o'}:  # right + down
                y += 1
                x += 1
                continue
            else:
                corns_at_rest += 1
                grid[y][x] = 'o'
                corn_done = True  # found rest position
                if (x, y) == (500, 0):
                    print(f'Task 2: {corns_at_rest} corns are at rest when all send has come down.')
                    return
                    # for line in grid:
                    #     print(''.join(line[300:750]))


def is_corn_falling(height: int, y_idx: int) -> bool:
    return y_idx >= height


# ================= Visualization Code Below =================

@dataclass
class GridDimensions:
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    width: int
    height: int


def get_grid_dimensions() -> GridDimensions:
    max_x = 400
    max_y = 168
    min_x = 0
    min_y = 0
    width = (abs(max_x - min_x) + 1)
    height = (abs(max_y - min_y) + 1)
    return GridDimensions(min_x, min_y, max_x, max_y, width, height)


def frame(vis_grids: list[list[list[str]]], time_idx: int):
    vis_grid = []
    for line in vis_grids[time_idx]:
        vis_line = []
        for char in line:
            if char == '.':
                vis_line.append(0.0)
            elif char == '#':
                vis_line.append(1.0)
            elif char == 'o':
                vis_line.append(2.0)
        vis_grid.append(vis_line)

    plt.cla()
    ax = plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    image = plt.imshow(vis_grid, cmap='rainbow')
    return image


if __name__ == '__main__':
    paths_data_ = load_lines(day=14, file_name='input.txt', skip_empty_lines=True)
    paths_ = to_paths(paths_data_)
    grid_ = build_occupancy_grid(paths_)

    vis_grids_ = []
    simulate(grid_, vis_grids_)

    # # Visualize
    fig, ax = plt.subplots(figsize=(15, 9))
    grid_dimensions_ = get_grid_dimensions()
    ax.set_xlim(0, grid_dimensions_.width)
    ax.set_ylim(0, grid_dimensions_.height)
    ani = animation.FuncAnimation(fig, partial(frame, vis_grids_), frames=len(vis_grids_), interval=1)
    plt.show()
