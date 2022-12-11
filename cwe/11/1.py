import data


def play(monkeys):
    actions = [0, 0, 0, 0, 0, 0, 0, 0]
    for _ in range(20):
        # play a round
        for idx, monkey in enumerate(monkeys):
            for item in monkey['items']:
                item = int((monkey['operation'](item)) / 3)
                monkeys[monkey['test'](item)]['items'].append(item)
                actions[idx] += 1
            monkey['items'] = []

    print(sorted(actions)[-1] * sorted(actions)[-2])
    print('end')


# play(data.monkeys_test)
play(data.monkeys_prod)
