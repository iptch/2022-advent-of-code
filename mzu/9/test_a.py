import unittest

import year2022_day09a as part_a


class Test(unittest.TestCase):

    def test_are_neighbors_or_on_top(self):
        self.assertTrue(part_a.are_neighbors_or_on_top((1, 0), (0, 1)))
        self.assertTrue(part_a.are_neighbors_or_on_top((0, 1), (1, 0)))
        self.assertTrue(part_a.are_neighbors_or_on_top((2, 2), (2, 1)))
        self.assertTrue(part_a.are_neighbors_or_on_top((2, 2), (1, 2)))
        self.assertTrue(part_a.are_neighbors_or_on_top((2, 2), (2, 3)))
        self.assertTrue(part_a.are_neighbors_or_on_top((3, 2), (3, 2)))
        self.assertTrue(part_a.are_neighbors_or_on_top((3, 2), (4, 3)))
        self.assertFalse(part_a.are_neighbors_or_on_top((3, 0), (3, 4)))
        self.assertFalse(part_a.are_neighbors_or_on_top((1, 2), (3, 2)))

    def test_tail_catches_up(self):
        new_tail = part_a.tail_catches_up((1, 2), (3, 1))
        self.assertTupleEqual(new_tail, (2, 2))

        new_tail = part_a.tail_catches_up((2, 3), (3, 1))
        self.assertTupleEqual(new_tail, (2, 2))

    def test_move_up(self):
        visited_positions = [['.'] * 6 for i in range(5)]
        head, tail = (4, 4), (4, 3)
        for _ in range(4):
            head, tail, visited_positions = part_a.move(head, tail, 'U', visited_positions)
        self.assertTupleEqual(head, (0, 4))
        self.assertTupleEqual(tail, (1, 4))

    def test_move_down(self):
        visited_positions = [[False] * 6 for i in range(5)]
        head, tail, visited_positions = part_a.move((0, 1), (0, 2), 'D', visited_positions)
        self.assertTupleEqual(head, (1, 1))
        self.assertTupleEqual(tail, (0, 2))

    def test_move_left(self):
        visited_positions = [[False] * 6 for i in range(5)]
        head, tail = (2, 5), (1, 4)
        for _ in range(5):
            head, tail, visited_positions = part_a.move(head, tail, 'L', visited_positions)
        self.assertTupleEqual(head, (2, 0))
        self.assertTupleEqual(tail, (2, 1))

    def test_move_right(self):
        visited_positions = [[False] * 6 for i in range(5)]
        head, tail = (1, 1), (0, 2)
        for _ in range(4):
            head, tail, visited_positions = part_a.move(head, tail, 'R', visited_positions)
        self.assertTupleEqual(head, (1, 5))
        self.assertTupleEqual(tail, (1, 4))

    def test_move(self):
        visited_positions = [[False] * 6 for i in range(5)]
        visited_positions[4][0] = True
        head, tail = (4, 0), (4, 0)
        for _ in range(4):
            head, tail, visited_positions = part_a.move(head, tail, 'R', visited_positions)
        self.assertTupleEqual(head, (4, 4))
        self.assertTupleEqual(tail, (4, 3))
        self.assertTrue(visited_positions[4][1])
        self.assertTrue(visited_positions[4][2])
        self.assertTrue(visited_positions[4][3])
        number_of_visited_positions = len([is_visited for row in visited_positions for is_visited in row if is_visited])
        self.assertEqual(number_of_visited_positions, 4)

    def test_calculate_number_of_visited_tail_positions(self):
        lines = [
            'R 4',
            'U 4',
            'L 3',
            'D 1',
            'R 4',
            'D 1',
            'L 5',
            'R 2'
        ]

        number_of_visited_tail_positions = part_a.calculate_number_of_visited_tail_positions(lines, 6, 5)
        self.assertEqual(number_of_visited_tail_positions, 13)


if __name__ == '__main__':
    unittest.main()
