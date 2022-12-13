import re


def puzzle_1():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    monkeys = {
        0: [54, 98, 50, 94, 69, 62, 53, 85],
        1: [71, 55, 82],
        2: [77, 73, 86, 72, 87],
        3: [97, 91],
        4: [78, 97, 51, 85, 66, 63, 62],
        5: [88],
        6: [87, 57, 63, 86, 87, 53],
        7: [73, 59, 82, 65]
    }
    inspected = [0, 0, 0, 0, 0, 0, 0, 0]
    for round in range(20):
        while len(monkeys[0]) > 0:
            inspected[0] += 1
            item = (monkeys[0].pop(0) * 13) // 3
            if item % 3 == 0:
                monkeys[2].append(item)
            else:
                monkeys[1].append(item)
        while len(monkeys[1]) > 0:
            inspected[1] += 1
            item = (monkeys[1].pop(0) + 2) // 3
            if item % 13 == 0:
                monkeys[7].append(item)
            else:
                monkeys[2].append(item)
        while len(monkeys[2]) > 0:
            inspected[2] += 1
            item = (monkeys[2].pop(0) + 8) // 3
            if item % 19 == 0:
                monkeys[4].append(item)
            else:
                monkeys[7].append(item)
        while len(monkeys[3]) > 0:
            inspected[3] += 1
            item = (monkeys[3].pop(0) + 1) // 3
            if item % 17 == 0:
                monkeys[6].append(item)
            else:
                monkeys[5].append(item)
        while len(monkeys[4]) > 0:
            inspected[4] += 1
            item = (monkeys[4].pop(0) * 17) // 3
            if item % 5 == 0:
                monkeys[6].append(item)
            else:
                monkeys[3].append(item)
        while len(monkeys[5]) > 0:
            inspected[5] += 1
            item = (monkeys[5].pop(0) + 3) // 3
            if item % 7 == 0:
                monkeys[1].append(item)
            else:
                monkeys[0].append(item)
        while len(monkeys[6]) > 0:
            inspected[6] += 1
            item = (monkeys[6].pop(0) ** 2) // 3
            if item % 11 == 0:
                monkeys[5].append(item)
            else:
                monkeys[0].append(item)
        while len(monkeys[7]) > 0:
            inspected[7] += 1
            item = (monkeys[7].pop(0) + 6) // 3
            if item % 2 == 0:
                monkeys[4].append(item)
            else:
                monkeys[3].append(item)

    inspected.sort()
    inspected.reverse()

    return inspected[0]*inspected[1]



def puzzle_2():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    monkeys = {
        0: [54, 98, 50, 94, 69, 62, 53, 85],
        1: [71, 55, 82],
        2: [77, 73, 86, 72, 87],
        3: [97, 91],
        4: [78, 97, 51, 85, 66, 63, 62],
        5: [88],
        6: [87, 57, 63, 86, 87, 53],
        7: [73, 59, 82, 65]
    }
    inspected = [0, 0, 0, 0, 0, 0, 0, 0]
    for round in range(10000):
        while len(monkeys[0]) > 0:
            inspected[0] += 1
            item = (monkeys[0].pop(0) * 13) % 9699690
            if item % 3 == 0:
                monkeys[2].append(item)
            else:
                monkeys[1].append(item)
        while len(monkeys[1]) > 0:
            inspected[1] += 1
            item = (monkeys[1].pop(0) + 2) % 9699690
            if item % 13 == 0:
                monkeys[7].append(item)
            else:
                monkeys[2].append(item)
        while len(monkeys[2]) > 0:
            inspected[2] += 1
            item = (monkeys[2].pop(0) + 8) % 9699690
            if item % 19 == 0:
                monkeys[4].append(item)
            else:
                monkeys[7].append(item)
        while len(monkeys[3]) > 0:
            inspected[3] += 1
            item = (monkeys[3].pop(0) + 1) % 9699690
            if item % 17 == 0:
                monkeys[6].append(item)
            else:
                monkeys[5].append(item)
        while len(monkeys[4]) > 0:
            inspected[4] += 1
            item = (monkeys[4].pop(0) * 17) % 9699690
            if item % 5 == 0:
                monkeys[6].append(item)
            else:
                monkeys[3].append(item)
        while len(monkeys[5]) > 0:
            inspected[5] += 1
            item = (monkeys[5].pop(0) + 3) % 9699690
            if item % 7 == 0:
                monkeys[1].append(item)
            else:
                monkeys[0].append(item)
        while len(monkeys[6]) > 0:
            inspected[6] += 1
            item = (monkeys[6].pop(0) ** 2) % 9699690
            if item % 11 == 0:
                monkeys[5].append(item)
            else:
                monkeys[0].append(item)
        while len(monkeys[7]) > 0:
            inspected[7] += 1
            item = (monkeys[7].pop(0) + 6) % 9699690
            if item % 2 == 0:
                monkeys[4].append(item)
            else:
                monkeys[3].append(item)

    inspected.sort()
    inspected.reverse()

    return inspected[0]*inspected[1]


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
