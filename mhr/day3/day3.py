from common import load_lines

PRIORITY = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
    'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39,
    'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
}


def find_shared_items(input_data):
    shared_items = []
    for rucksack in input_data:
        rucksack = rucksack.strip()
        first = rucksack[:len(rucksack) // 2]
        second = rucksack[len(rucksack) // 2:]
        for item in first:
            if item in second:
                shared_items.append(item)
                break
    return shared_items


def find_team_badges(input_data):
    badges = []
    chunk_size = 3
    list_chunked = [input_data[i:i + chunk_size] for i in range(0, len(input_data), chunk_size)]

    for chunk in list_chunked:
        pack1, pack2, pack3 = chunk
        for item in set(' '.join(chunk)):
            if item in set(pack1) and item in set(pack2) and item in set(pack3):
                badges.append(item)
                break
    return badges


def calculate_priorities_sum(items):
    return sum([PRIORITY[item] for item in items])


if __name__ == '__main__':
    input_lines = load_lines(day=3)

    # Task 1
    shared_items = find_shared_items(input_lines)
    print(calculate_priorities_sum(shared_items))

    # Task 2
    badges = find_team_badges(input_lines)
    print(calculate_priorities_sum(badges))
