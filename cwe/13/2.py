def parse_input(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()

    pairs = []
    for idx in range(0, len(lines), 3):
        left = eval(lines[idx])
        right = eval(lines[idx + 1])
        pairs.append((left, right))

    return pairs


def check_order(pairs):
    all_entries = []
    for pair in pairs:
        all_entries.append(pair[0])
        all_entries.append(pair[1])
    all_entries.append([[2]])
    all_entries.append([[6]])
    totally_ordered = False
    while not totally_ordered:
        totally_ordered = True
        for idx in range(len(all_entries) - 1):
            compare_result = compare_lists(all_entries[idx], all_entries[idx + 1])
            if not compare_result:
                higher_entry = all_entries[idx]
                all_entries[idx] = all_entries[idx + 1]
                all_entries[idx + 1] = higher_entry
                totally_ordered = False
    print(all_entries)
    index_2 = all_entries.index([[2]])
    index_6 = all_entries.index([[6]])
    print(index_2 +1)
    print(index_6+1)
    print((index_2 +1) * (index_6 +1))



def compare_lists(left, right):
    try:
        id = 0
        for idx in range(len(left)):
            id += 1
            if isinstance(left[idx], int) and isinstance(right[idx], int):
                if left[idx] > right[idx]:
                    return False
                elif left[idx] < right[idx]:
                    return True
                else:
                    continue
            else:
                if isinstance(left[idx], list) and isinstance(right[idx], list):
                    sub_pair_ok = compare_lists(left[idx], right[idx])
                elif isinstance(left[idx], int):
                    sub_pair_ok = compare_lists([left[idx]], right[idx])
                else:
                    sub_pair_ok = compare_lists(left[idx], [right[idx]])
                if sub_pair_ok is not None:
                    return sub_pair_ok
        if id < len(right):
            return True
    except IndexError:
        return False
    return None


# check_order(parse_input('data_test.txt'))
check_order(parse_input('data_prod.txt'))
