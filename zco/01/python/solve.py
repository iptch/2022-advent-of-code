import sys
import heapq


def iter_total_calories(lines):
    current = 0
    for line in lines:
        if line:
            current += int(line)
        else:
            yield current
            current = 0
    yield current


def nlargest(n, iterable):
    heap = [0 for _ in range(n)]
    for calories in iterable:
        heapq.heappushpop(heap, calories)
    return heap


def main():
    lines = map(str.strip, sys.stdin)

    # print("ans1", max(iter_total_calories(lines)))
    print("ans2", sum(nlargest(3, iter_total_calories(lines))))


if __name__ == "__main__":
    main()
