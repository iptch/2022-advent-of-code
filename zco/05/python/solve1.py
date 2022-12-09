from collections import defaultdict
from collections import deque
from pprint import pprint
import re
import sys
from typing import Iterator

INSTR_REGEX = re.compile(r"move (\d+) from (\d+) to (\d+)")


def collect_head(lines: Iterator[str]):
    collected = []
    for line in lines:
        if not line:
            break
        collected.append(line)
    return collected[:-1]  # Remove number line


def parse(lines: Iterator[str]):
    stacks = defaultdict(deque)
    for line in collect_head(lines):
        for i, c in enumerate(line[1::4]):
            if c.isalpha():
                stacks[i].appendleft(c)
    return stacks


def solve(lines: Iterator[str]):
    stacks = parse(lines)
    # pprint(stacks)
    for line in lines:
        m = INSTR_REGEX.fullmatch(line)
        if not m:
            raise ValueError("Could not parse line.")
        amount, from_stack, to_stack = map(int, m.groups())
        for _ in range(amount):
            stacks[to_stack - 1].append(stacks[from_stack - 1].pop())
    # pprint(stacks)
    return "".join(stacks[i][-1] for i in range(len(stacks)))


def main():
    print(solve(map(lambda x: str.rstrip(x, "\n"), sys.stdin)))


if __name__ == "__main__":
    main()
