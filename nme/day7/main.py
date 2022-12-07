PATH = 'input.txt'


def load():
    res = {'name': '/', 'files': [], 'dirs': [], 'parent': None}
    curr = res
    with open(PATH) as f:
        for line in f:
            line = line.replace('\n', '')
            if line == '$ cd /':
                continue
            elif line[0] == '$':  # command
                if line[2] == 'c':  # cd
                    if line == '$ cd ..':
                        curr = curr['parent']
                    else:
                        curr = find_dir(curr['dirs'], line[5:])
            else:  # listing files and directories
                if line[0:3] == 'dir':
                    curr['dirs'].append({'name': line[4:], 'files': [], 'dirs': [], 'parent': curr})
                else:
                    s, name = line.split(' ')
                    curr['files'].append((int(s), name))
    return res


def find_dir(dirs, name):
    for d in dirs:
        if d['name'] == name:
            return d


def compute_size(directory):
    file_size = sum([s for s, _ in directory['files']])
    sub_dir_size = 0
    for d in directory['dirs']:
        sub_dir_size += compute_size(d)
    directory['size'] = file_size + sub_dir_size
    return directory['size']


def compute_sum(directory):
    this_sum = directory['size']
    if this_sum > 100000:
        this_sum = 0
    for d in directory['dirs']:
        this_sum += compute_sum(d)
    return this_sum


def part1():
    directories = load()
    compute_size(directories)
    res = compute_sum(directories)
    print(res)


def compute_delete(needed, directory, acc):
    if needed <= directory['size']:
        acc.append((directory['size'] - needed, directory['name']))
        for d in directory['dirs']:
            compute_delete(needed, d, acc)


def part2():
    directories = load()
    compute_size(directories)
    free_space = 70000000 - directories['size']
    needed_space = 30000000 - free_space
    acc = []
    compute_delete(needed_space, directories, acc)
    acc.sort()
    print(acc[0][0] + needed_space)


if __name__ == '__main__':
    part1()
    part2()
