import re


def puzzle_1():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    root = {}
    path = []
    for line in lines:
        extract = line.split(" ")
        if extract[0] == "$":
            if extract[1] == "cd":
                if extract[2] == "..":
                    path.pop()
                else:
                    path.append(extract[2])
        else:
            if extract[0] != "dir":
                size = int(extract[0])
                current_dir = root
                for d in path:
                    current_dir = current_dir.setdefault(d, {})
                if "size" in current_dir:
                    current_dir["size"] = current_dir["size"] + size
                else:
                    current_dir["size"] = size
    total, sum_puzzle1 = sum_less_tan_100000(root, 0)
    return sum_puzzle1


def sum_less_tan_100000(dir, sum_puzzle1):
    total = 0
    for key in dir:
        if key != "size":
            sub_total, sum_puzzle1 = sum_less_tan_100000(dir[key], sum_puzzle1)
            total += sub_total
    if "size" in dir:
        total += dir["size"]
    if total < 100000:
        sum_puzzle1 += total
    return total, sum_puzzle1

def puzzle_2():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    root = {}
    path = []
    for line in lines:
        extract = line.split(" ")
        if extract[0] == "$":
            if extract[1] == "cd":
                if extract[2] == "..":
                    path.pop()
                else:
                    path.append(extract[2])
        else:
            if extract[0] != "dir":
                size = int(extract[0])
                current_dir = root
                for d in path:
                    current_dir = current_dir.setdefault(d, {})
                if "size" in current_dir:
                    current_dir["size"] = current_dir["size"] + size
                else:
                    current_dir["size"] = size
    total, sum_puzzle1 = sum_less_tan_100000(root, 0)
    free_space = 70000000 - total
    to_delete = 30000000 - free_space
    print("to_delete: ", to_delete)
    total2, dirs_to_delete = find_dirs_bigger_than_to_delete(root, to_delete)
    dirs_to_delete.sort()
    return dirs_to_delete[0]


def find_dirs_bigger_than_to_delete(dir, to_delete):
    total = 0
    dirs_to_delete = []
    for key in dir:
        if key != "size":
            sub_total, sub_dirs_to_delete = find_dirs_bigger_than_to_delete(dir[key], to_delete)
            total += sub_total
            dirs_to_delete = dirs_to_delete + sub_dirs_to_delete
    if "size" in dir:
        total += dir["size"]
    if total >= to_delete:
        dirs_to_delete.append(total)
    return total, dirs_to_delete


if __name__ == '__main__':
    print(f"Puzzle 1: {puzzle_1()}")
    print(f"Puzzle 2: {puzzle_2()}")
