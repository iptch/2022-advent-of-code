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
    good_pairs = []
    for idx, pair in enumerate(pairs):
        compare_result = compare_lists(pair[0], pair[1])
        if compare_result or compare_result is None :
            good_pairs.append(idx + 1)
    print(good_pairs)
    print(sum(good_pairs))


def compare_lists(left, right):
    try:
        id = 0
        for idx in range(len(left)):
            id = idx
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
