def char_to_value(char):
    o = ord(char)
    if o > 90:
        return o - 96
    else:
        return o - 38


def puzzle_1():
    result = 0
    input_txt = open("input.txt", "r")
    for line in input_txt:
        first = line[:len(line)//2]
        second = line[len(line)//2:-1]
        common = ''.join(set(first).intersection(second))
        result += char_to_value(common)

    return result


def puzzle_2():
    result = 0
    input_txt = open("input.txt", "r")
    group = []
    for line in input_txt:
        group.append(line[:-1])
        if len(group) == 3:
            common = ''.join(set(group[0]).intersection(group[1]).intersection(group[2]))
            result += char_to_value(common)
            group = []

    return result


if __name__ == '__main__':
    print(char_to_value("a"))
    print(char_to_value("z"))
    print(char_to_value("A"))
    print(char_to_value("Z"))
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")

