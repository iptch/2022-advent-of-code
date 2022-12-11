#!/usr/bin/env python

import click

TOKEN_MONKEY = "Monkey"
TOKEN_ITEMS = "Starting items:"
TOKEN_OPERATION = "Operation: new = "
TOKEN_TEST = "Test: divisible by"
TOKEN_TRUE = "If true: throw to monkey"
TOKEN_FALSE = "If false: throw to monkey"


class Monkey:
    inspect_count = 0
    items = []
    operation: None
    test: None
    monkey_true: None
    monkey_false: None
    divider: None
    comp_op = None
    gcd = 1

    monkeys = []

    def inspect(self):
        if len(self.items) > 0:
            self.inspect_count += 1
            old = self.items[0]

            del self.items[0]
            # print(f"Monkey inspects an item with a worry level of {old}.")
            level = eval(self.operation)
            # print(f"Worry level {self.operation} to {level}.")
            # level = level // 3
            level = level % self.gcd

            # print(f"Monkey gets bored with item. Worry level is divided by 3 to {level}.")
            t = None
            if level % self.test == 0:
                # print(f"Current worry level is divisible by {self.test}.")
                t = self.monkey_true, level
            else:
                # print(f"Current worry level is not divisible by {self.test}.")
                t = self.monkey_false, level
            # print(f"Item with worry level {t[1]} is thrown to monkey {t[0]}.")
            return t
        else:
            # print("Monkey does not hold any items")
            return None

    def __str__(self):
        return f"items: {self.items}, operation: {self.operation}, test: {self.test}, true: {self.monkey_true}, false: {self.monkey_false}, gcd: {self.gcd}"


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def parse(file_path: str):
    with open(file_path) as fp:
        lines = [x.strip() for x in fp.readlines()]

        items = []
        operation = None
        test = None
        monkey_true = None
        monkey_false = None

        monkeys = []
        monkey = None
        gcd = 1

        for ln, line in enumerate(lines):

            if TOKEN_MONKEY in line:
                monkey = Monkey()
                items = []
                operation = None
                test = None
                monkey_true = None
                monkey_false = None

            if TOKEN_ITEMS in line:
                items = [int(x) for x in line.strip().replace(TOKEN_ITEMS, '').split(',')]
                # print(items)

            if TOKEN_OPERATION in line:
                operation = line.strip().replace(TOKEN_OPERATION, '')

            if TOKEN_TEST in line:
                test = int(line.strip().replace(TOKEN_TEST, '').split(' ')[1])
                gcd *= test
                print(test)
            if TOKEN_TRUE in line:
                monkey_true = int(line.strip().replace(TOKEN_TRUE, '').split(' ')[1])
                # print(monkey_true)
            if TOKEN_FALSE in line:
                monkey_false = int(line.strip().replace(TOKEN_FALSE, '').split(' ')[1])
                # print(monkey_false)

                monkey.items = items
                monkey.operation = operation
                monkey.test = test
                monkey.monkey_true = monkey_true
                monkey.monkey_false = monkey_false
                monkeys.append(monkey)

        print(f"setting gdc {gcd}")
        for m in monkeys:
            m.gcd = gcd
            print(m)

        max_round = 10000
        round = 1
        while True:
            if round > max_round:
                break
            for i, m in enumerate(monkeys):

                # print(f"--- monkey {i} / (round {round}) ---")
                while True:

                    r = m.inspect()
                    if r is None:
                        break
                    monkey_to, level = r

                    # print(f"Item with worry level {level} is thrown to monkey {monkey_to}.")
                    monkeys[monkey_to].items.append(level)

            if round > max_round:
                break
            round += 1

        total_counts = []
        for i, m in enumerate(monkeys):
            print(f"Monkey {i} inspected items {m.inspect_count} times. ")
            print(f"items: {m.items}")
            # print(f"comp ops: {m.comp_op}")
            total_counts.append(m.inspect_count)

            # print(m)
        top = sorted(total_counts, reverse=True)
        print(top, top[0] * top[1])


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
