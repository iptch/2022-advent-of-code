from dataclasses import dataclass
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


def simulate(motions: list[Motion]) -> int:
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
    if head == tail or max([abs(dist) for dist in {head.x-tail.x, head.y-tail.y}]):
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


if __name__ == '__main__':
    lines_ = load_lines(day=9, file_name='input.txt')
    motions_ = load_motions(lines_)
    n_visited_ = simulate(motions_)
    print(f'Task 2: Tail visited {n_visited_} positions at least once.')
