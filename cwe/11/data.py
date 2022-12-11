def monkey_selector(worry_level, divisor, if_true, if_false):
    if worry_level % divisor == 0:
        return if_true
    else:
        return if_false


modulos_test = [23, 19, 13, 17]
monkeys_test = [
    {
        'items': [79, 98],
        'operation': lambda x: x * 19,
        'test': lambda x: monkey_selector(x, 23, 2, 3),
    },
    {
        'items': [54, 65, 75, 74],
        'operation': lambda x: x + 6,
        'test': lambda x: monkey_selector(x, 19, 2, 0),
    },
    {
        'items': [79, 60, 97],
        'operation': lambda x: x ** 2,
        'test': lambda x: monkey_selector(x, 13, 1, 3),
    },
    {
        'items': [74],
        'operation': lambda x: x + 3,
        'test': lambda x: monkey_selector(x, 17, 0, 1),
    }
]

modulos_prod = [5, 2, 13, 19, 11, 3, 7, 17]
monkeys_prod = [
    {
        'items': [78, 53, 89, 51, 52, 59, 58, 85],
        'operation': lambda x: x * 3,
        'test': lambda y: monkey_selector(y, 5, 2, 7),
    },
    {
        'items': [64],
        'operation': lambda x: x + 7,
        'test': lambda y: monkey_selector(y, 2, 3, 6),
    },
    {
        'items': [71, 93, 65, 82],
        'operation': lambda x: x + 5,
        'test': lambda y: monkey_selector(y, 13, 5, 4),
    },
    {
        'items': [67, 73, 95, 75, 56, 74],
        'operation': lambda x: x + 8,
        'test': lambda y: monkey_selector(y, 19, 6, 0),
    },
    {
        'items': [85, 91, 90],
        'operation': lambda x: x + 4,
        'test': lambda y: monkey_selector(y, 11, 3, 1),
    },
    {
        'items': [67, 96, 69, 55, 70, 83, 62],
        'operation': lambda x: x * 2,
        'test': lambda y: monkey_selector(y, 3, 4, 1),
    },
    {
        'items': [53, 86, 98, 70, 64],
        'operation': lambda x: x + 6,
        'test': lambda y: monkey_selector(y, 7, 7, 0),
    },
    {
        'items': [88, 64],
        'operation': lambda x: x ** 2,
        'test': lambda y: monkey_selector(y, 17, 2, 5),
    }
]
