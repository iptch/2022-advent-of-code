import unittest

import year2022_day10a as part_a
import year2022_day10b as part_b


class Test(unittest.TestCase):

    def test_part_a_with_example_data(self):
        with open('test-data') as file:
            lines = [line.strip() for line in file.readlines()]
            result = part_a.solve(lines)
            self.assertEqual(result, 13140)
            print(result)

    def test_part_b_with_example_data(self):
        with open('test-data') as file:
            lines = [line.strip() for line in file.readlines()]
            result = part_b.solve(lines)
            expected_result = \
                "##..##..##..##..##..##..##..##..##..##..\n" + \
                "###...###...###...###...###...###...###.\n" + \
                "####....####....####....####....####....\n" + \
                "#####.....#####.....#####.....#####.....\n" + \
                "######......######......######......####\n" + \
                "#######.......#######.......#######.....\n"
            self.assertEqual(result, expected_result)
            print(result)


if __name__ == '__main__':
    unittest.main()
