PATH = 'input.txt'


def operate(val, op):
    b = op[1]
    if op[1] == 'old':
        b = val
    if op[0] == '+':
        return val + b
    return val * b


def load():
    monkeys = []
    with open(PATH) as f:
        line_num = 0
        monkey = None
        for line in f:
            op = line_num % 7
            if op == 0:
                monkey = {'inspections': 0}
            if op == 1:
                monkey['items'] = [int(n) for n in line[18:].split(', ')]
            if op == 2:
                operand = line[25:-1]
                if operand != 'old':
                    operand = int(operand)
                monkey['operation'] = ((line[23]), operand)
            if op == 3:
                monkey['modulo'] = int(line[21:])
            if op == 4:
                monkey['condition_true'] = int(line[29:])
            if op == 5:
                monkey['condition_false'] = int(line[30])
            if op == 6:
                monkeys.append(monkey)
            line_num += 1
        monkeys.append(monkey)
    return monkeys


def part1():
    monkeys = load()

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['inspections'] += 1
                new_value = operate(item, monkey['operation']) // 3
                if new_value % monkey['modulo']:
                    monkeys[monkey['condition_false']]['items'].append(new_value)
                else:
                    monkeys[monkey['condition_true']]['items'].append(new_value)
            monkey['items'] = []

    inspections = sorted([monkey['inspections'] for monkey in monkeys])
    print(inspections[-2] * inspections[-1])


def part2():
    monkeys = load()
    modulos = [monkey['modulo'] for monkey in monkeys]
    big_mod = 1
    for m in modulos:
        big_mod *= m

    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey['inspections'] += 1
                new_value = operate(item, monkey['operation']) % big_mod
                if new_value % monkey['modulo']:
                    monkeys[monkey['condition_false']]['items'].append(new_value)
                else:
                    monkeys[monkey['condition_true']]['items'].append(new_value)
            monkey['items'] = []

    inspections = sorted([monkey['inspections'] for monkey in monkeys])
    print(inspections[-2] * inspections[-1])


if __name__ == '__main__':
    part1()
    part2()
