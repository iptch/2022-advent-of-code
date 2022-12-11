import data


def calculate_kgv(modulos):
    res = 1
    for i in modulos:
        res *= i
    return res


def play(monkeys, modulos):
    kgv = calculate_kgv(modulos)
    actions = [0, 0, 0, 0, 0, 0, 0, 0]
    for _ in range(10000):
        # play a round
        for idx, monkey in enumerate(monkeys):
            for item in monkey['items']:
                item = int((monkey['operation'](item))) % kgv
                monkeys[monkey['test'](item)]['items'].append(item)
                actions[idx] += 1
            monkey['items'] = []
    print(actions)
    print(sorted(actions)[-1] * sorted(actions)[-2])
    print('end')


# play(data.monkeys_test, data.modulos_test)
play(data.monkeys_prod, data.modulos_prod)
