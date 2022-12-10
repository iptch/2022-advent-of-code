#!/usr/bin/env python

import click

COMMAND_RIGHT = "R"
COMMAND_LEFT = "L"
COMMAND_UP = "U"
COMMAND_DOWN = "D"

NEXT_STEPS = {
    (0, 2): (0, 1),
    (1, 2): (1, 1),
    (2, 1): (1, 1),
    (2, 0): (1, 0),
    (2, -1): (1, -1),
    (1, -2): (1, -1),
    (0, -2): (0, -1),
    (-1, -2): (-1, -1),
    (-2, -1): (-1, -1),
    (-2, 0): (-1, 0),
    (-2, 1): (-1, 1),
    (-1, 2): (-1, 1)

}


class Head:
    loc_x = 0
    loc_y = 0
    history = []

    def update(self, x=None, y=None):
        # print(f"move: x={x}, y={y}")
        if x is not None:
            self.loc_x = x

        if y is not None:
            self.loc_y = y

        self.history.append((self.loc_x, self.loc_y))

    def move_right(self):
        self.update(x=self.loc_x + 1)

    def move_left(self):
        self.update(x=self.loc_x - 1)

    def move_up(self):
        self.update(y=self.loc_y + 1)

    def move_down(self):
        self.update(y=self.loc_y - 1)

    def __str__(self):
        return f"x: {self.loc_x}, y: {self.loc_y}"


class Tail:
    loc_x = 0
    loc_y = 0
    history = []

    def __int__(self, head: Head):
        self.loc_x = head.loc_x
        self.loc_y = head.loc_y
        self.history = [(self.loc_x, self.loc_y)]

    def calc_distance(self, head: Head):
        d_x = head.loc_x - self.loc_x
        d_y = head.loc_y - self.loc_y

        return d_x, d_y

    def update(self, head: Head):
        distance = self.calc_distance(head)

        # print(distance, distance in NEXT_STEPS)
        if distance in NEXT_STEPS:
            x, y = NEXT_STEPS[distance]
            self.history.append((self.loc_x, self.loc_y))
            self.loc_x += x
            self.loc_y += y

    def __str__(self):
        return f"x: {self.loc_x}, y: {self.loc_y}"


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]

        head = Head()
        tail = Tail()
        tail.update(head)
        print(f"head: {head}")
        print(f"tail: {tail}")

        for line in lines:
            steps = int(line.split(" ")[1])

            print(line)

            if COMMAND_RIGHT in line:
                for i in range(0, steps):
                    head.move_right()
                    tail.update(head)
                    print(f"head: {head}")
                    print(f"tail: {tail}")
            elif COMMAND_LEFT in line:
                for i in range(0, steps):
                    head.move_left()
                    tail.update(head)
                    print(f"head: {head}")
                    print(f"tail: {tail}")
            elif COMMAND_UP in line:
                for i in range(0, steps):
                    head.move_up()
                    tail.update(head)
                    print(f"head: {head}")
                    print(f"tail: {tail}")
            elif COMMAND_DOWN in line:
                for i in range(0, steps):
                    head.move_down()
                    tail.update(head)
                    print(f"head: {head}")
                    print(f"tail: {tail}")
            else:
                print(f"unknown command {line}")
                exit(-1)

        unique_locations = set(tail.history)
        last_pos = tail.loc_x, tail.loc_y
        unique_locations.add(last_pos)
        print(f"visited at least once: {len(unique_locations)}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
