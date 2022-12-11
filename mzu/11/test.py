import unittest

import year2022_day11a as part_a
import year2022_day11b as part_b


class Test(unittest.TestCase):

    def test_parse_monkey(self):
        lines = [
            'Monkey 0:',
            '  Starting items: 79, 98',
            '  Operation: new = old * 19',
            '  Test: divisible by 23',
            '    If true: throw to monkey 2',
            '    If false: throw to monkey 3'''
        ]
        monkey = part_a.parse_monkey(lines)
        self.assertListEqual(monkey.items, [79, 98])
        self.assertEqual(monkey.operation, "old * 19")
        self.assertEqual(monkey.test_divider, 23)
        self.assertEqual(monkey.receiver_passed_test, 2)
        self.assertEqual(monkey.receiver_failed_test, 3)

    def test_part_a_with_example_data(self):
        with open('test-data') as file:
            lines = [line for line in file.readlines()]
            result = part_a.solve(lines)
            self.assertEqual(result, 10605)
            print(result)

    def test_part_b_with_example_data(self):
        with open('test-data') as file:
            lines = [line for line in file.readlines()]
            result = part_b.solve(lines)
            self.assertEqual(result, 2713310158)
            print(result)


if __name__ == '__main__':
    unittest.main()
