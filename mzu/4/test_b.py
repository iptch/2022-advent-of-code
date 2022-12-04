import unittest

import year2022_day04b as part_b


class Test(unittest.TestCase):

    def test_fully_contains_sections(self):
        self.assertTrue(part_b.has_overlapping_sections([2, 3, 4, 5, 6], [3, 4]))
        self.assertTrue(part_b.has_overlapping_sections([3, 4], [2, 3, 4, 5, 6]))
        self.assertTrue(part_b.has_overlapping_sections([2, 3, 4, 5, 6], [2, 3, 4, 5, 6]))
        self.assertTrue(part_b.has_overlapping_sections([2, 3, 4, 5, 6], [1, 2, 3, 4]))
        self.assertTrue(part_b.has_overlapping_sections([2, 3, 4], [3, 4, 5, 6]))
        self.assertFalse(part_b.has_overlapping_sections([2, 3, 4], [5, 6, 7]))
        self.assertFalse(part_b.has_overlapping_sections([5, 6, 7], [2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
