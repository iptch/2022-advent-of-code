from dataclasses import dataclass
from common import load_lines


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
    tail = Pose(0, 0)
    for motion in motions:
        for step in range(motion.steps):
            update_head(head, motion.direction)
            new_tail = update_tail(head, tail)
            visited.add((new_tail.x, new_tail.y))
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

    diagonal_compensation: str = 'N'
    if hor_dist != 0 and vert_dist != 0:
        if abs(hor_dist) > 1 and abs(vert_dist) > 1:
            raise RuntimeError('unexpected behaviour')
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

    if diagonal_compensation != 'N':
        if diagonal_compensation == 'R':
            tail.x += 1
        if diagonal_compensation == 'L':
            tail.x -= 1
        if diagonal_compensation == 'U':
            tail.y += 1
        if diagonal_compensation == 'D':
            tail.y -= 1

    return tail


if __name__ == '__main__':
    lines_ = load_lines(day=9, file_name='input.txt')
    motions_ = load_motions(lines_)
    n_visited_ = simulate(motions_)
    print(f'Task 1: Tail visited {n_visited_} positions at least once.')

