#!/usr/bin/env python
import click

COMMAND = '$'
COMMAND_CD = COMMAND + ' cd'
COMMAND_LS = COMMAND + ' ls'
DIR = 'dir '
COMMAND_CD_UP = '..'
ROOT = '/'


class Dir:
    parent = None
    name = None
    content = None

    def __str__(self):
        return f"dir: {self.name}, ({len(self.content)})"

    def do_print(self, space=""):
        print(f"{space}- {self.name} (dir, size={self.calc_size()})")

        for c in self.content:
            c.do_print(space + " ")

    def calc_size(self):
        sum = 0
        for c in self.content:
            sum += c.calc_size()
        # print(f"d: {self.name}, {sum}")

        return sum


class File:
    name = None
    size = 0

    def __str__(self):
        return f"file: {self.name}, ({self.size})"

    def do_print(self, space):
        print(f"{space}- {self.name} (file, size={self.size})")

    def calc_size(self):
        return self.size


def parse(file_path: str):
    with open(file_path) as fp:
        root = None
        current_element = None

        lines = fp.readlines()
        total_size = 0
        for l in lines:
            l = l.split()
            try:
                s = int(l[0])
                total_size += s
            except ValueError:
                pass

        print(f" check total {total_size}")

        for i, line in enumerate(lines):
            line = line.strip()
            # print(i, line)
            if COMMAND in line:
                if COMMAND_CD in line:
                    dir_name = line.split(' ')[2].strip()
                    if dir_name == ROOT and current_element is None:
                        new_dir = Dir()
                        new_dir.name = dir_name
                        new_dir.content = []
                        current_element = new_dir
                        root = new_dir

                    elif COMMAND_CD_UP in dir_name:
                        current_element = current_element.parent

                    else:
                        if does_element_exist(current_element, dir_name):
                            current_element = get_content(current_element, dir_name)
                        else:
                            new_dir = Dir()
                            new_dir.name = dir_name
                            new_dir.content = []
                            new_dir.parent = current_element

                            current_element.content.append(new_dir)
                            current_element = new_dir

            elif COMMAND_LS in line:
                pass
            elif DIR in line:
                dir_name = line.split(' ')[1]
                if does_element_exist(current_element, dir_name):
                    pass
                else:
                    new_dir = Dir()
                    new_dir.name = dir_name
                    new_dir.content = []
                    new_dir.parent = current_element
                    current_element.content.append(new_dir)
            else:
                size, file_name = line.split(" ")
                new_file = File()
                new_file.name = file_name
                new_file.size = int(size)
                current_element.content.append(new_file)

        root.do_print()
        # root.calc_size()

        total_space = 70000000
        for_update = 30000000
        max_space = total_space - for_update
        used_space = root.calc_size()
        to_free_up = (total_space - for_update - used_space) * -1

        print(f"total_space {total_space}")
        print(f"for_update {for_update}")
        print(f"used_space {used_space}")
        print(f"to_free_up {to_free_up}")

        found = find(root, to_free_up)
        r = []
        for f in found:
            print(f.name, f.calc_size())
            r.append(f.calc_size())

        r.sort()
        print("min", r[0])


def find(dir, max_size):
    found = []

    if dir.calc_size() >= max_size:
        found.append(dir)

    for c in dir.content:
        if isinstance(c, Dir):
            r = find(c, max_size)
            found.extend(r)

    return found


def does_element_exist(current_element, name):
    # print(f" --> does '{name}' exist in ${current_element}")
    found = False
    for e in current_element.content:
        if e.name == name:
            found = True
            break
    return found


def get_content(current_element, name):
    for e in current_element.content:
        if e.name == name:
            return e


@click.command()
@click.argument('file', type=click.Path(exists=True))
def cli(file):
    parse(file)


if __name__ == '__main__':
    cli()
