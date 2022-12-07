from dataclasses import dataclass

from aocd import data

DAY = '7'
PART = 'b'


@dataclass
class File:
    name: str
    size: int


@dataclass
class Dir:
    name: str
    parent: None
    children: []
    total_size: int


def read_tree(lines):
    root_dir = Dir('/', None, [], 0)
    current_dir = root_dir
    for line in lines[1:]:
        if line == '$ cd ..':
            current_dir = current_dir.parent
        elif line.startswith('$ cd '):
            dir_name = line.removeprefix('$ cd ')
            current_dir = [node for node in current_dir.children if node.name == dir_name][0]
        elif line == '$ ls':
            continue
        elif line.startswith('dir '):
            current_dir.children.append(Dir(line.removeprefix('dir '), current_dir, [], 0))
        elif line[0] in '0123456789':
            size, name = line.split(' ')
            current_dir.children.append(File(name, int(size)))
    return root_dir


def calculate_size(node):
    if type(node) is File:
        return node.size
    else:
        dir_size = sum(calculate_size(child) for child in node.children)
        node.total_size = dir_size
        return dir_size


def get_list_of_sub_dirs(root_dir: Dir):
    dirs = []
    for node in root_dir.children:
        if type(node) is Dir:
            dirs.append(node)
            dirs.extend(get_list_of_sub_dirs(node))
    return dirs


def find_best_dir_to_delete(dirs, root_dir):
    needed_disk_space = 30000000 - (70000000 - root_dir.total_size)
    best_dir_to_delete = root_dir
    for current_dir in dirs:
        if needed_disk_space <= current_dir.total_size < best_dir_to_delete.total_size:
            best_dir_to_delete = current_dir
    return best_dir_to_delete


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    root_dir = read_tree(lines)
    calculate_size(root_dir)
    dirs = get_list_of_sub_dirs(root_dir)
    best_dir_to_delete = find_best_dir_to_delete(dirs, root_dir)

    print(f'The best directory to clean up just enough disk space has a size of: {str(best_dir_to_delete.total_size)}')


if __name__ == '__main__':
    main()
