import functools

PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        l1, l2 = None, None
        for line in f:
            if line == '\n':
                res.append((l1, l2))
                l1, l2 = None, None
            elif l1 is None:
                l1 = eval(line.replace('\n', ''))
            else:
                l2 = eval(line.replace('\n', ''))
        res.append((l1, l2))
    return res


def compare(p1, p2):
    """return true if p1 comes before p2. false otherwise"""

    p1_is_list = type(p1) is list
    p2_is_list = type(p2) is list
    if not p1_is_list and not p2_is_list:
        if p1 == p2:
            return None
        else:
            return p1 < p2
    elif p1_is_list and not p2_is_list:
        p2 = [p2]
    elif not p1_is_list and p2_is_list:
        p1 = [p1]

    for a, b in zip(p1, p2):
        res = compare(a, b)
        if res is None:
            continue
        else:
            return res

    if len(p1) == len(p2):
        return None
    else:
        return len(p1) < len(p2)


def part1():
    packets = load()
    res = 0
    for i, (p1, p2) in enumerate(packets):
        if compare(p1, p2):
            res += i + 1
    print(res)


def compare_sort(a, b):
    res = compare(a, b)
    if res is None:
        return 0
    if res:
        return -1
    return 1


def part2():
    packets = load()
    all_packets = [[2], [6]]
    for a, b in packets:
        all_packets.append(a)
        all_packets.append(b)

    all_packets.sort(key=functools.cmp_to_key(compare_sort))
    i1, i2 = all_packets.index([2]), all_packets.index([6])
    print((i1 + 1) * (i2 + 1))


if __name__ == '__main__':
    part1()
    part2()
