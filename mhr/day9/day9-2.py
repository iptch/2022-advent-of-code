from dataclasses import dataclass

import matplotlib.pyplot as plt
from matplotlib import animation
from functools import partial

from common import load_lines

N_KNOTS = 9  # excluding the head knot


@dataclass
class Motion:
    direction: str
    steps: int


@dataclass
class Pose:
    x: int
    y: int


def load_motions(lines: list[str]) -> list[Motion]:
    motions = list()
    for line in lines:
        direction, steps = line.split(' ')
        motions.append(Motion(direction, int(steps)))
    return motions


def simulate(motions: list[list[Motion]], pose_recorder: list = None) -> int:
    """Returns: How many positions did the tail visited at least once?"""
    visited = {(0, 0)}  # starting point

    head = Pose(0, 0)
    knot_poses = N_KNOTS * [Pose(0, 0)]  # last is tail
    for motion in motions:
        for step in range(motion.steps):
            update_head(head, motion.direction)
            for knot_idx in range(N_KNOTS):
                curr_head = head if knot_idx == 0 else knot_poses[knot_idx - 1]
                knot_poses[knot_idx] = update_tail(Pose(curr_head.x, curr_head.y),
                                                   Pose(knot_poses[knot_idx].x, knot_poses[knot_idx].y))
                visited.add((knot_poses[-1].x, knot_poses[-1].y))
            if pose_recorder is not None:
                pose_recorder.append([curr_head] + knot_poses)
    return len(visited)


def update_head(head: Pose, direction: str) -> None:
    if direction == 'R':
        head.x += 1
    if direction == 'U':
        head.y += 1
    if direction == 'L':
        head.x -= 1
    if direction == 'D':
        head.y -= 1


def update_tail(head: Pose, tail: Pose) -> Pose:
    """Returns tail position in any case to potentially add to places visited at least once."""
    if head == tail or max([abs(dist) for dist in {head.x - tail.x, head.y - tail.y}]):
        pass

    hor_dist = head.x - tail.x
    vert_dist = head.y - tail.y

    diagonal_compensation: str = ''
    if abs(hor_dist) > 1 and abs(vert_dist) > 1:
        diagonal_compensation += 'R' if hor_dist > 0 else 'L'
        diagonal_compensation += 'U' if vert_dist > 0 else 'D'
    else:
        if hor_dist != 0 and vert_dist != 0:
            if abs(hor_dist) > 1 or abs(vert_dist) > 1:
                if abs(hor_dist) < abs(vert_dist):
                    diagonal_compensation = 'R' if hor_dist > 0 else 'L'
                else:
                    diagonal_compensation = 'U' if vert_dist > 0 else 'D'

        if abs(head.x - tail.x) > 1:
            if head.x > tail.x:
                tail.x += 1
            else:
                tail.x -= 1

        if abs(head.y - tail.y) > 1:
            if head.y > tail.y:
                tail.y += 1
            else:
                tail.y -= 1

    if diagonal_compensation != '':
        if 'R' in diagonal_compensation:
            tail.x += 1
        if 'L' in diagonal_compensation:
            tail.x -= 1
        if 'U' in diagonal_compensation:
            tail.y += 1
        if 'D' in diagonal_compensation:
            tail.y -= 1

    return tail


# ----------------------------------------------------------------------------------------------------------------------
# Below is visualization code only
# ----------------------------------------------------------------------------------------------------------------------

@dataclass
class GridDimensions:
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    width: int
    height: int


def generate_pose_time_series(motions: list[list[Motion]]) -> list[list[Pose]]:
    """Time series = list (one per time stamp) for all poses of the knots."""
    time_series = list()
    simulate(motions, pose_recorder=time_series)
    return time_series


def get_grid_dimensions(pose_time_series: list[list[Pose]]) -> GridDimensions:
    x_positions = [pose.x for time in pose_time_series for pose in time]
    y_positions = [pose.y for time in pose_time_series for pose in time]
    min_x = min(x_positions)
    max_x = max(x_positions)
    min_y = min(y_positions)
    max_y = max(y_positions)
    width = (abs(max_x - min_x) + 1) * 2
    height = (abs(max_y - min_y) + 1) * 2
    return GridDimensions(min_x, min_y, max_x, max_y, width, height)


def frame(pose_time_series: list[list[Pose]], time_idx: int):
    grid_dimensions = get_grid_dimensions(pose_time_series)
    grid = [grid_dimensions.width * [10] for _ in range(grid_dimensions.height)]
    for knot_idx, pose in enumerate(pose_time_series[time_idx]):
        grid[pose.y + grid_dimensions.height // 2][pose.x + grid_dimensions.width // 2] = knot_idx

    plt.cla()
    ax = plt.gca()
    ax.set_xticks([])
    ax.set_yticks([])
    image = plt.imshow(grid, cmap='Reds_r')
    return image


if __name__ == '__main__':
    lines_ = load_lines(day=9, file_name='test_input_2.txt')
    motions_ = load_motions(lines_)

    # Solving the task
    n_visited_ = simulate(motions_)
    print(f'Task 2: Tail visited {n_visited_} positions at least once.')

    # Visualize
    pose_time_series_ = generate_pose_time_series(motions_)

    fig, ax = plt.subplots()
    grid_dimensions_ = get_grid_dimensions(pose_time_series_)
    ax.set_xlim(0, grid_dimensions_.width)
    ax.set_ylim(0, grid_dimensions_.height)
    ani = animation.FuncAnimation(fig, partial(frame, pose_time_series_), frames=len(pose_time_series_), interval=4)
    plt.show()
