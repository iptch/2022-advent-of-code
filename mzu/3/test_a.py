import unittest

import year2022_day03a as part_a


class Test(unittest.TestCase):

    def test_read_rucksacks(self):
        lines = [
            'vJrwpWtwJgWrhcsFMMfFFhFp'
        ]
        rucksacks = part_a.read_rucksacks(lines)
        self.assertListEqual(rucksacks[0].first_compartment_prios[:3], [22, 36, 18])

    def test_calculate_error_prios(self):
        rucksacks = [part_a.Rucksack('vJrwpWtwJgWrhcsFMMfFFhFp')]
        error_prios = part_a.calculate_error_prios(rucksacks)
        self.assertListEqual([16], error_prios)


if __name__ == '__main__':
    unittest.main()
