import unittest

import year2022_day04a as part_a


class Test(unittest.TestCase):

    def test_read_cleaning_areas(self):
        cleaning_areas_first_elf, cleaning_areas_second_elf = part_a.read_cleaning_areas('2-4,6-8')
        self.assertListEqual([2, 3, 4], [*cleaning_areas_first_elf])
        self.assertListEqual([6, 7, 8], [*cleaning_areas_second_elf])

    def test_fully_contains_sections(self):
        self.assertTrue(part_a.fully_contains_sections([2, 3, 4, 5, 6], [3, 4]))
        self.assertTrue(part_a.fully_contains_sections([3, 4], [2, 3, 4, 5, 6]))
        self.assertTrue(part_a.fully_contains_sections([2, 3, 4, 5, 6], [2, 3, 4, 5, 6]))
        self.assertFalse(part_a.fully_contains_sections([2, 3, 4, 5, 6], [1, 2, 3, 4]))
        self.assertFalse(part_a.fully_contains_sections([2, 3, 4], [3, 4, 5, 6]))
        self.assertFalse(part_a.fully_contains_sections([2, 3, 4], [5, 6, 7]))
        self.assertFalse(part_a.fully_contains_sections([5, 6, 7], [2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
