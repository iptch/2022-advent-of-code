PATH = 'input.txt'


def load():
    res = []
    with open(PATH) as f:
        for line in f:
            res.append(int(line))
    return res


def make_circular_linked_list(numbers):
    start = {'n': numbers[0], 'prev': None, 'next': None}
    queue = [start]
    current = start
    for n in numbers[1:]:
        node = {'n': n, 'prev': current, 'next': None}
        current['next'] = node
        current = node
        queue.append(node)
    current['next'] = start
    start['prev'] = current
    return start, queue


def pretty_print(d_linked_list, big=False):
    start = d_linked_list
    queue = [start['n']]
    if big:
        print(f"{start['n']}, prev: {start['prev']['n']}, next: {start['next']['n']}")
    curr = start['next']
    while curr != start:
        if big:
            print(f"{curr['n']}, prev: {curr['prev']['n']}, next: {curr['next']['n']}")
        queue.append(curr['n'])
        curr = curr['next']
    print(queue)


def part1():
    numbers = load()
    d_linked_list, queue = make_circular_linked_list(numbers)
    zero = None
    for node in queue:
        curr, val = node, node['n']
        if val == 0:
            zero = node
        else:
            node['prev']['next'] = node['next']
            node['next']['prev'] = node['prev']

            if val < 0:
                for _ in range(-val):
                    curr = curr['prev']
                curr = curr['prev']
            else:
                for _ in range(val):
                    curr = curr['next']
            node['prev'] = curr
            node['next'] = curr['next']
            curr['next']['prev'] = node
            curr['next'] = node

    curr = zero
    res = 0
    for i in range(1, 3001):
        curr = curr['next']
        if i % 1000 == 0:
            res += curr['n']
    print(res)


def find_idx(numbers, idx):
    next_index = 0
    for _ in numbers:
        if numbers[next_index][1] == idx:
            return next_index
        next_index += 1
    return -1


def mix(numbers):
    n = len(numbers)
    for i in range(n):
        next_index = find_idx(numbers, i)
        numbers.insert((numbers[next_index][0] + next_index) % (n - 1), numbers.pop(next_index))
    return numbers


def part2():
    actual_numbers = [(811589153 * n, i) for i, n in enumerate(load())]
    for _ in range(10):
        actual_numbers = mix(actual_numbers)

    nums = [n for n, _ in actual_numbers]
    idx, n, res = nums.index(0), len(nums), 0
    for i in range(1, 3001):
        actual_index = (idx + i) % n
        if i % 1000 == 0:
            res += nums[actual_index]
    print(res)


if __name__ == '__main__':
    part1()
    part2()
