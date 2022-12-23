from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib import animation

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

    grid = list([['.' for _ in range(max_x + 2)] for _ in range(max_y + 2)])

    for path in paths:
        for segment in path.segments:
            if segment.is_horizontal:
                for x_idx in range(min(segment.x_start, segment.x_end), max(segment.x_start, segment.x_end) + 1):
                    print(x_idx)
                    grid[segment.y_start][x_idx] = "#"
            else:
                for y_idx in range(min(segment.y_start, segment.y_end), max(segment.y_start, segment.y_end) + 1):
                    grid[y_idx][segment.x_start] = "#"
    return grid


def simulate(grid: list[list[str]]):
    height = len(grid)
    width = len(grid[0])
    grid.append(width * ['|'])  # the big dark black hole

    corns_at_rest = 0

    while True:
        print(corns_at_rest)
        x, y = 500, 0
        corn_done = False
        while not corn_done:
            # for line in grid[:30]:
            #     print(''.join(line[450:]))
            # print('-------------------')

            if grid[y + 1][x] not in {'#', 'o'}:  # down
                y += 1
                if y >= height:
                    return corns_at_rest
                continue
            elif grid[y + 1][x - 1] not in {'#', 'o'}:  # left + down
                y += 1
                x -= 1
                if y >= height:
                    return corns_at_rest
                continue
            elif grid[y + 1][x + 1] not in {'#', 'o'}:  # right + down
                y += 1
                x += 1
                if y >= height:
                    return corns_at_rest
                continue
            else:
                corns_at_rest += 1
                grid[y][x] = 'o'
                corn_done = True  # found rest position


def is_corn_falling(height: int, y_idx: int) -> bool:
    return y_idx >= height


# ================= Visualization Code Below =================

# @dataclass
# class GridDimensions:
#     min_x: int
#     min_y: int
#     max_x: int
#     max_y: int
#     width: int
#     height: int
#
#
# def get_grid_dimensions(paths: list[Path]) -> GridDimensions:
#     max_x = max([segment.x_end for path in paths for segment in path.segments])
#     max_y = max([segment.y_end for path in paths for segment in path.segments])
#     min_x = 450
#     min_y = 0
#     width = (abs(max_x - min_x) + 1)
#     height = (abs(max_y - min_y) + 1)
#     return GridDimensions(min_x, min_y, max_x, max_y, width, height)
#
#
# def frame(grid_time_series: list[list[str]], time_idx: int):
#     grid_dimensions = get_grid_dimensions(paths_)
#     grid = [grid_dimensions.width * [10] for _ in range(grid_dimensions.height)]
#     for knot_idx, pose in enumerate(pose_time_series[time_idx]):
#         grid[pose.y + grid_dimensions.height // 2][pose.x + grid_dimensions.width // 2] = knot_idx
#
#     plt.cla()
#     ax = plt.gca()
#     ax.set_xticks([])
#     ax.set_yticks([])
#     image = plt.imshow(grid, cmap='Reds_r')
#     return image


if __name__ == '__main__':
    paths_data_ = load_lines(day=14, file_name='input.txt', skip_empty_lines=True)
    paths_ = to_paths(paths_data_)
    grid_ = build_occupancy_grid(paths_)
    # for line in grid_:
    #     print(''.join(line)[450:])
    print('---')

    n_sands_at_rest_before_doom_ = simulate(grid_)

    print(f'Task 1: {n_sands_at_rest_before_doom_} corns at rest when first falls into the big dark nothing')

    # # Visualize
    # grid_time_series_ = [grid for grid in simulate(grid_)]
    #
    # fig, ax = plt.subplots()
    # grid_dimensions_ = get_grid_dimensions(paths_)
    # ax.set_xlim(0, grid_dimensions_.width)
    # ax.set_ylim(0, grid_dimensions_.height)
    # ani = animation.FuncAnimation(fig, partial(frame, pose_time_series_), frames=len(pose_time_series_), interval=4)
    # plt.show()
