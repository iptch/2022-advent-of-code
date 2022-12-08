import re


def puzzle_1():
    result = 0
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    forest = []
    for line in lines:
        trees = [int(tree) for tree in list(line)]
        forest.append(trees)
        pass

    for y in range(len(forest)):
        for x in range(len(forest[y])):
            if is_visible(y, x, forest):
                result += 1

    return result

def is_visible(y, x, forest):
    if y == 0 or x == 0 or y == len(forest)-1 or x == len(forest[y])-1:
        return True
    visible = True
    for left in range(x):
        if forest[y][left] >= forest[y][x]:
            visible = False
            break
    if visible:
        return True
    visible = True
    for right in range(x+1, len(forest[y])):
        if forest[y][right] >= forest[y][x]:
            visible = False
            break
    if visible:
        return True
    visible = True
    for up in range(y):
        if forest[up][x] >= forest[y][x]:
            visible = False
            break
    if visible:
        return True
    visible = True
    for down in range(y+1, len(forest)):
        if forest[down][x] >= forest[y][x]:
            visible = False
            break
    if visible:
        return True

    return False


def puzzle_2():
    result = 0
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    forest = []
    for line in lines:
        trees = [int(tree) for tree in list(line)]
        forest.append(trees)
        pass

    for y in range(len(forest)):
        for x in range(len(forest[y])):
            score = scenic_sore(y, x, forest)
            if score > result:
                result = score

    return result


def scenic_sore(y, x, forest):
    left_count = 0
    for left in reversed(range(x)):
        left_count += 1
        if forest[y][left] >= forest[y][x]:
            break
    right_count = 0
    for right in range(x+1, len(forest[y])):
        right_count += 1
        if forest[y][right] >= forest[y][x]:
            break
    up_count = 0
    for up in reversed(range(y)):
        up_count += 1
        if forest[up][x] >= forest[y][x]:
            break
    down_count = 0
    for down in range(y+1, len(forest)):
        down_count += 1
        if forest[down][x] >= forest[y][x]:
            break

    return left_count*right_count*up_count*down_count


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
