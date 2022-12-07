from common import load_lines
from enum import Enum

TOTAL_DISK_SPACE_AVAILABLE = 70000000
SPACE_NEEDED = 30000000


class LineType(Enum):
    CD = 1,
    LS = 2,
    DIR = 3,
    FILE = 4


class NodeKind(Enum):
    DIR = 1,
    FILE = 2


class Node:
    """Data structure representing a tree. The root Node represents the whole tree while children are subtrees."""

    def __init__(self, name, kind: NodeKind, size: int = None, children: list['Node'] = None, parent: 'Node' = None):
        self.name = name
        self.kind = kind
        self.size = size
        self.children = children
        self.parent = parent

    def add_child(self, node) -> 'Node':
        if self.children is None:
            self.children = [node]
        else:
            for child in self.children:
                if node.name == child.name and node.kind == child.kind:
                    return child  # prevent duplicates
            self.children.append(node)
            return node


def build_dir_tree(lines: list[str]) -> Node:
    """Builds up a tree with directories and files as nodes. File and directory sizes are not set yet."""
    tree = Node(name='/', kind=NodeKind.DIR)

    current_node = tree
    for line in lines[1:]:  # first is /
        if parse_line_type(line) == LineType.FILE:
            file_name, file_size = get_file_data(line)
            current_node.add_child(Node(name=file_name, size=file_size, kind=NodeKind.FILE, parent=current_node))
        elif parse_line_type(line) == LineType.DIR:
            current_node.add_child(Node(name=get_dir_name(line), kind=NodeKind.DIR, parent=current_node))
        elif parse_line_type(line) == LineType.CD:
            if is_move_up(line):
                current_node = current_node.parent
            else:
                dir_node = Node(name=get_cd_dir_name(line), kind=NodeKind.DIR, parent=current_node)
                new_node = current_node.add_child(dir_node)
                current_node = new_node
    return tree


def build_dir_sizes(tree: Node) -> int:
    """"Sets the appropriate file and directory sizes for all the nodes in the tree."""
    if tree.kind == NodeKind.FILE:
        return tree.size
    else:
        if tree.children is None:
            return 0
        else:
            tree.size = sum([build_dir_sizes(child) for child in tree.children])
            return tree.size


def parse_line_type(line: str) -> LineType:
    split = line.split(' ')
    if line.startswith('$'):
        if split[1] == 'cd':
            return LineType.CD
        elif split[1] == 'ls':
            return LineType.LS
    else:
        if line.startswith('dir'):
            return LineType.DIR
        elif split[0].isnumeric():
            return LineType.FILE


def get_file_data(line: str) -> tuple[str, int]:
    """"For a line representing a file."""
    file_size, file_name = line.split(' ')
    return file_name, int(file_size)


def get_dir_name(line: str) -> int:
    """"For a line representing a directory."""
    _, dir_name = line.split(' ')
    return dir_name


def get_cd_dir_name(line: str) -> int:
    """"For a line representing a directory change."""
    _, _, dir_name = line.split(' ')
    return dir_name


def is_move_up(line: str) -> bool:
    """"For a line representing a directory change one step up the tree."""
    _, _, dir_name = line.split(' ')
    return dir_name == '..'


def print_tree(tree: Node) -> None:
    """"Recursively traverse the tree and print out the nodes."""
    print(f'Node ({tree.kind}): {tree.name} {tree.size if tree.size is not None else ""}')

    if tree.children is not None:
        for child in tree.children:
            print_tree(child)


def yield_dirs(tree: Node, size_up_to: int = None):
    """Yield directory nodes within the tree, possibly with a size limit."""
    if tree.kind == NodeKind.DIR:
        if size_up_to is not None:
            if tree.size <= size_up_to:
                yield tree
        else:
            yield tree

        if tree.children is not None:
            for child in tree.children:
                yield from yield_dirs(child, size_up_to)


def task1_compute_large_directories_sum(tree: Node) -> int:
    return sum([node.size for node in yield_dirs(tree, size_up_to=100000)])


def task2_find_smallest_dir_which_frees_enough_space(tree: Node) -> Node:
    unused_space = TOTAL_DISK_SPACE_AVAILABLE - tree.size
    space_increase_needed = SPACE_NEEDED - unused_space

    dir_nodes = sorted(list(yield_dirs(tree)), key=lambda node: node.size)

    for dir_node in dir_nodes:
        if dir_node.size >= space_increase_needed:
            return dir_node


if __name__ == '__main__':
    lines = load_lines(day=7, file_name='input.txt')
    tree_ = build_dir_tree(lines)
    build_dir_sizes(tree_)
    directories_sum = task1_compute_large_directories_sum(tree_)
    print(f'Task 1: {directories_sum}')
    dir_node_ = task2_find_smallest_dir_which_frees_enough_space(tree_)
    print(f'Task 2: {dir_node_.size}')
