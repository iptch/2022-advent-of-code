from timeit import default_timer as timer
import re


def puzzle_1():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    jets = lines[1]
    jet_id = 0
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ]
    chamber = [
       [False for j in range(2022*4)] for i in range(7)
    ]

    max_height = -1
    for i in range(2022):
        rock_id = i % 5
        rock_position = (2, max_height+4)
        rock_falling = True
        while rock_falling:
            if not rock_clashes(rocks[rock_id], (rock_position[0] + 1 if jets[jet_id] == ">" else rock_position[0] - 1, rock_position[1]), chamber):
                rock_position = (rock_position[0] + 1 if jets[jet_id] == ">" else rock_position[0] - 1, rock_position[1])
            jet_id = (jet_id + 1) % len(jets)
            if rock_clashes(rocks[rock_id], (rock_position[0], rock_position[1]-1), chamber):
                rock_falling = False
                max_height = max(max_height, (rock_position[1] + rocks[rock_id][len(rocks[rock_id])-1][1]))
                for rock_part in rocks[rock_id]:
                    rock_part_position = (rock_position[0] + rock_part[0], rock_position[1] + rock_part[1])
                    chamber[rock_part_position[0]][rock_part_position[1]] = True
            else:
                rock_position = (rock_position[0], rock_position[1]-1)

        # for y in reversed(range(0,max_height+1)):
        #     for x in range(0, 7):
        #         print("#" if chamber[x][y] else ".", end='')
        #     print()
        # print()

    return max_height + 1


def rock_clashes(rock, rock_position, chamber):
    for rock_part in rock:
        rock_part_position = (rock_position[0] + rock_part[0], rock_position[1] + rock_part[1])
        if not (0 <= rock_part_position[0] < 7):
            return True
        if not (0 <= rock_part_position[1]):
            return True
        if chamber[rock_part_position[0]][rock_part_position[1]]:
            return True
    return False

def puzzle_2():
    input_txt = open("input.txt", "r")
    lines = input_txt.read().splitlines()
    jets = lines[1]
    jet_id = 0
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ]
    chamber = [
       [False for j in range(100000*4)] for i in range(7)
    ]

    found_pattern = {}
    max_height = -1
    rock_number = 0
    rock_number_pattern_jump = 0
    max_height_pattern_jump = 0
    end = 1000000000000
    while rock_number < end:
        rock_id = rock_number % 5
        rock_position = (2, max_height+4)
        rock_falling = True
        while rock_falling:
            if not rock_clashes(rocks[rock_id], (rock_position[0] + 1 if jets[jet_id] == ">" else rock_position[0] - 1, rock_position[1]), chamber):
                rock_position = (rock_position[0] + 1 if jets[jet_id] == ">" else rock_position[0] - 1, rock_position[1])
            jet_id = (jet_id + 1) % len(jets)
            if rock_clashes(rocks[rock_id], (rock_position[0], rock_position[1]-1), chamber):
                rock_falling = False
                max_height = max(max_height, (rock_position[1] + rocks[rock_id][len(rocks[rock_id])-1][1]))
                for rock_part in rocks[rock_id]:
                    rock_part_position = (rock_position[0] + rock_part[0], rock_position[1] + rock_part[1])
                    chamber[rock_part_position[0]][rock_part_position[1]] = True
            else:
                rock_position = (rock_position[0], rock_position[1]-1)

        pattern = str(rock_id) + ";" + str(jet_id) + ";"
        for x in range(7):
            y = 0
            while max_height-y >= 0 and not chamber[x][max_height-y]:
                y += 1
            pattern += str(y) + ";"

        if pattern in found_pattern:
            rocks_in_pattern = rock_number - found_pattern[pattern][0]
            gain_in_pattern = max_height - found_pattern[pattern][1]
            repeating = (1000000000000 - rock_number) // rocks_in_pattern
            rock_number_pattern_jump = (repeating*rocks_in_pattern)
            max_height_pattern_jump = (repeating*gain_in_pattern)
            end -= rock_number_pattern_jump
            found_pattern = {}
        else:
            found_pattern[pattern] = (rock_number, max_height)
        rock_number += 1


        # for y in reversed(range(0,max_height+1)):
        #     for x in range(0, 7):
        #         print("#" if chamber[x][y] else ".", end='')
        #     print()
        # print()

    return max_height + max_height_pattern_jump + 1


if __name__ == '__main__':
    start1 = timer()
    print(f"Puzzle 1: {puzzle_1()} (in {timer()-start1}sec)")
    start2 = timer()
    print(f"Puzzle 2: {puzzle_2()} (in {timer()-start2}sec)")
