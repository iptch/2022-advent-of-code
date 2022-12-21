PATH = 'input.txt'


def load():
    nodes = {}
    with open(PATH) as f:
        for line in f:
            line = line.replace('\n', '')
            name = line[:4]
            if name not in nodes:
                nodes[name] = {'name': name}
            if len(line) == 17:
                l, op, r = line[6:10], line[11], line[13:17]
                if l not in nodes:
                    nodes[l] = {'name': l}
                if r not in nodes:
                    nodes[r] = {'name': r}

                node, left_node, right_node = nodes[name], nodes[l], nodes[r]

                node['left'] = left_node
                node['right'] = right_node
                node['op'] = op
            else:
                node = nodes[name]
                node['val'] = int(line[5:])

            nodes[name] = node

    return nodes


def pretty_print(node, ident=0):
    if 'val' in node:
        print(' ' * ident + node['name'] + ': ' + str(node['val']))
        return
    print(' ' * ident + node['name'] + ': ' + node['op'])
    pretty_print(node['left'], ident + 1), node['op'], pretty_print(node['right'], ident + 1)


def compute(node):
    if 'val' in node:
        return node['val']

    l, op, r = compute(node['left']), node['op'], compute(node['right'])
    if op == '+':
        return l + r
    if op == '-':
        return l - r
    if op == '/':
        return l // r
    if op == '*':
        return l * r


def has_human(node):
    if node['name'] == 'humn':
        return True

    if 'val' in node:
        return False

    return has_human(node['left']) or has_human(node['right'])


def part1():
    nodes = load()
    print(compute(nodes['root']))


def solve(val, eq):
    if 'val' in eq:
        return val

    op = eq['op']
    if has_human(eq['left']):
        b, new_eq = compute(eq['right']), eq['left']
        if op == '+':
            new_val = val - b
        if op == '-':
            new_val = val + b
        if op == '*':
            new_val = val // b
        if op == '/':
            new_val = val * b
    else:
        a, new_eq = compute(eq['left']), eq['right']
        if op == '+':
            new_val = val - a
        if op == '-':
            new_val = a - val
        if op == '*':
            new_val = val // a
        if op == '/':
            new_val = a // val

    return solve(new_val, new_eq)


def part2():
    nodes = load()
    if has_human(nodes['root']['left']):
        print(solve(compute(nodes['root']['right']), nodes['root']['left']))
    else:
        print(solve(compute(nodes['root']['left']), nodes['root']['right']))


if __name__ == '__main__':
    part1()
    part2()
