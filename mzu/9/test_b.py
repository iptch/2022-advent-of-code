import unittest

import year2022_day09b as part_b


class Test(unittest.TestCase):

    def test_are_neighbors_or_on_top(self):
        self.assertTrue(part_b.are_neighbors_or_on_top((1, 0), (0, 1)))
        self.assertTrue(part_b.are_neighbors_or_on_top((0, 1), (1, 0)))
        self.assertTrue(part_b.are_neighbors_or_on_top((2, 2), (2, 1)))
        self.assertTrue(part_b.are_neighbors_or_on_top((2, 2), (1, 2)))
        self.assertTrue(part_b.are_neighbors_or_on_top((2, 2), (2, 3)))
        self.assertTrue(part_b.are_neighbors_or_on_top((3, 2), (3, 2)))
        self.assertTrue(part_b.are_neighbors_or_on_top((3, 2), (4, 3)))
        self.assertFalse(part_b.are_neighbors_or_on_top((3, 0), (3, 4)))
        self.assertFalse(part_b.are_neighbors_or_on_top((1, 2), (3, 2)))

    def test_knot_catches_up(self):
        new_tail = part_b.knot_catches_up((1, 2), (3, 1))
        self.assertTupleEqual(new_tail, (2, 2))

        new_tail = part_b.knot_catches_up((2, 3), (3, 1))
        self.assertTupleEqual(new_tail, (2, 2))

    def test_move_up(self):
        # start position:
        # ......
        # ......
        # ......
        # ......
        # 4321H. (4 covers 5, 6, 7, 8, 9)
        rope = [(4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (4, 0), (4, 0), (4, 0), (4, 0), (4, 0)]

        # end position:
        # ....H.
        # ....1.
        # ..432.
        # .5....
        # 6.....  (6 covers 7, 8, 9, s)
        expected_rope_after_move = [(0, 4), (1, 4), (2, 4), (2, 3), (2, 2), (3, 1), (4, 0), (4, 0), (4, 0), (4, 0)]

        visited_positions = [[False] * 6 for i in range(5)]
        visited_positions[4][0] = True

        for _ in range(4):
            rope, visited_positions = part_b.move(rope, 'U', visited_positions)
        self.assertListEqual(expected_rope_after_move, rope)
        self.assertEqual(1, len([is_visited for row in visited_positions for is_visited in row if is_visited]))

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

        number_of_visited_tail_positions = part_b.calculate_number_of_visited_tail_positions(lines, 6, 5, 4, 0)
        self.assertEqual(number_of_visited_tail_positions, 1)

    def test_calculate_number_of_visited_tail_positions_large(self):
        lines = [
            'R 5',
            'U 8',
            'L 8',
            'D 3',
            'R 17',
            'D 10',
            'L 25',
            'U 20'
        ]

        number_of_visited_tail_positions = part_b.calculate_number_of_visited_tail_positions(lines, 50, 50, 15, 11)
        self.assertEqual(number_of_visited_tail_positions, 36)


if __name__ == '__main__':
    unittest.main()
