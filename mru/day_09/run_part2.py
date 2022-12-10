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
    (-1, 2): (-1, 1),
    (2, 2): (1, 1),
    (2, -2): (1, -1),
    (-2, 2): (-1, 1),
    (-2, -2): (-1, -1)
}


class Knot:
    loc_x = 0
    loc_y = 0
    history = []
    next_knot = None
    name = None

    def __init__(self, x, y, name, knot):
        self.loc_x = x
        self.loc_y = y
        self.history = [(self.loc_x, self.loc_y)]
        self.next_knot = knot
        self.name = name

    def calc_distance(self, knot):
        d_x = self.loc_x - knot.loc_x
        d_y = self.loc_y - knot.loc_y

        return d_x, d_y

    def move(self, x=0, y=0):

        # print(f"move ({self.name}), x={x}, y={y}")
        self.loc_x += x
        self.loc_y += y

        self.history.append((self.loc_x, self.loc_y))

        if self.next_knot is not None:
            distance = self.calc_distance(self.next_knot)
            # print(f"distance from {self.name} to {self.next_knot.name} is {distance}")
            a, b = distance
            if a > 2 or b > 2 or a < -2 or b < -2:
                print(f"distance {distance} from {self.name} to {self.next_knot.name} to long")
                exit(-1)
            if distance in NEXT_STEPS:
                x, y = NEXT_STEPS[distance]
                self.next_knot.move(x=x, y=y)

    def move_right(self):
        self.move(x=1)

    def move_left(self):
        self.move(x=-1)

    def move_up(self):
        self.move(y=1)

    def move_down(self):
        self.move(y=-1)

    def __str__(self):
        return f"x: {self.loc_x}, y: {self.loc_y}"


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]

        knots = []

        n_9 = Knot(0, 0, name="n9", knot=None)
        n_8 = Knot(0, 0, name="n8", knot=n_9)
        n_7 = Knot(0, 0, name="n7", knot=n_8)
        n_6 = Knot(0, 0, name="n6", knot=n_7)
        n_5 = Knot(0, 0, name="n5", knot=n_6)
        n_4 = Knot(0, 0, name="n4", knot=n_5)
        n_3 = Knot(0, 0, name="n3", knot=n_4)
        n_2 = Knot(0, 0, name="n2", knot=n_3)
        n_1 = Knot(0, 0, name="n1", knot=n_2)
        head = Knot(0, 0, name="head", knot=n_1)

        for line in lines:
            steps = int(line.split(" ")[1])

            print(line)

            if COMMAND_RIGHT in line:
                for i in range(0, steps):
                    head.move_right()

            elif COMMAND_LEFT in line:
                for i in range(0, steps):
                    head.move_left()

            elif COMMAND_UP in line:
                for i in range(0, steps):
                    head.move_up()

            elif COMMAND_DOWN in line:
                for i in range(0, steps):
                    head.move_down()

            else:
                print(f"unknown command {line}")
                exit(-1)

            print(f"head: {head}")
            print(f"n_1: {n_1}")
            print(f"n_2: {n_2}")
            print(f"n_3: {n_3}")
            print(f"n_4: {n_4}")
            print(f"n_5: {n_5}")
            print(f"n_6: {n_6}")
            print(f"n_7: {n_7}")
            print(f"n_8: {n_8}")
            print(f"n_9: {n_9}")

        unique_locations = set(n_9.history)
        last_pos = n_9.loc_x, n_9.loc_y
        unique_locations.add(last_pos)
        print(f"visited at least once: {len(unique_locations)}")


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
