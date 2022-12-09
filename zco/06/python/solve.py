import sys


def _get_ord(char):
    return ord(char) - ord("a")


class CharCounter:
    def __init__(self, iterable) -> None:
        self._counts = [0 for _ in range(26)]
        self._num_nonzero = 0
        for char in iterable:
            self.inc(char)

    @property
    def num_nonzero(self):
        return self._num_nonzero

    def inc(self, char):
        idx = _get_ord(char)
        if self._counts[idx] == 0:
            self._num_nonzero += 1
        self._counts[idx] += 1

    def dec(self, char):
        idx = _get_ord(char)
        self._counts[idx] -= 1
        if self._counts[idx] == 0:
            self._num_nonzero -= 1


def solve(line, count):
    i = count - 1
    seen = CharCounter(line[:i])
    while i < len(line):
        seen.inc(line[i])
        if seen.num_nonzero == count:
            return i + 1
        seen.dec(line[i - count + 1])
        i += 1


def main():
    (count,) = sys.argv[1:]
    print(solve(sys.stdin.readline().rstrip("\n"), int(count)))


if __name__ == "__main__":
    main()
