PATH = 'input.txt'
NUM_CRATES = 9
MAX_HEIGHT = 8


def load():
    crates = [[] for _ in range(NUM_CRATES)]
    instructions = []
    with open(PATH) as f:
        current_height = 0
        for line in f:
            if current_height < MAX_HEIGHT:
                current_height += 1
                for i in range(NUM_CRATES):
                    idx = 4 * i + 1
                    if idx < len(line) and line[idx] != ' ':
                        crates[i].append(line[idx])
            elif current_height + 1 > MAX_HEIGHT + 2:
                n, s, d = line.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(',')
                instructions.append([int(n), int(s) - 1, int(d) - 1])
            else:
                current_height += 1
        for i in range(NUM_CRATES):
            crates[i] = crates[i][::-1]
    return crates, instructions


def part1():
    crates, instruction = load()
    for n, s, d in instruction:
        for _ in range(n):
            crates[d].append(crates[s].pop())

    print(''.join([crates[i][-1] for i in range(NUM_CRATES)]))


def part2():
    crates, instruction = load()
    for n, s, d in instruction:
        crates[d] += crates[s][-n:]
        for _ in range(n):
            crates[s].pop()

    print(''.join([crates[i][-1] for i in range(NUM_CRATES)]))


if __name__ == '__main__':
    part1()
    part2()
