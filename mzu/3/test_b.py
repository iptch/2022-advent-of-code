import unittest

import year2022_day03b as part_b


class Test(unittest.TestCase):

    def test_read_rucksacks(self):
        lines = [
            'vJrwpWtwJgWrhcsFMMfFFhFp'
        ]
        rucksacks = part_b.read_rucksacks(lines)
        self.assertListEqual([22, 36, 18], rucksacks[0].first_compartment_prios[:3])

    def test_separate_rucksacks_into_groups(self):
        rucksacks = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
        groups = part_b.separate_rucksacks_into_groups(rucksacks)
        self.assertEqual(3, len(groups))
        self.assertListEqual([[1], [2], [3]], groups[0])

    def test_is_badge(self):
        group = [part_b.Rucksack('abcdef'), part_b.Rucksack('afghijk'), part_b.Rucksack('flmnopq')]
        self.assertTrue(part_b.is_badge(6, group))
        self.assertFalse(part_b.is_badge(2, group))
        self.assertFalse(part_b.is_badge(1, group))

    def test_calculate_badge_prio_per_group(self):
        group = [part_b.Rucksack('abcdef'), part_b.Rucksack('afghijk'), part_b.Rucksack('flmnopq')]
        self.assertEqual(6, part_b.calculate_badge_prio_per_group(group))


if __name__ == '__main__':
    unittest.main()
