from dataclasses import dataclass

from common import load_lines


@dataclass
class Range:
    start: int
    end: int

    def fully_contains(self, other: "Range") -> bool:
        """"Checks if the 'other' Range is fully included within this Range."""
        return self.start <= other.start and self.end >= other.end

    def partially_overlaps(self, other: "Range") -> bool:
        """Checks if the 'other' Range is partially included within this Range. Caution: Not both ways!"""
        return self.start <= other.start <= self.end or self.start <= other.end <= self.end


@dataclass
class RangePair:
    first: Range
    second: Range


def to_range_pairs(lines: list[str]) -> list[RangePair]:
    range_pairs = []
    for line in lines:
        first, second = line.split(',')
        first_start, first_end = first.split('-')
        second_start, second_end = second.split('-')
        range_pairs.append(RangePair(Range(int(first_start), int(first_end)),
                                     Range(int(second_start), int(second_end))))
    return range_pairs


def find_number_of_fully_contained_pairs(range_pairs: list[RangePair]):
    """Task 1."""
    counter = 0
    for range_pair in range_pairs:
        if range_pair.first.fully_contains(range_pair.second) or range_pair.second.fully_contains(range_pair.first):
            counter += 1
    return counter


def find_number_of_partially_overlapping_pairs(range_pairs: list[RangePair]):
    """Task 2."""
    counter = 0
    for range_pair in range_pairs:
        if range_pair.first.partially_overlaps(range_pair.second) or range_pair.second.partially_overlaps(range_pair.first):
            counter += 1
    return counter


if __name__ == '__main__':
    input_lines = load_lines(day=4)

    # Task 1
    n_fully_contained_ranges = find_number_of_fully_contained_pairs(to_range_pairs(input_lines))
    print(f'Task 1: Found {n_fully_contained_ranges} fully contained ranges.')

    # Task 2
    n_partially_overlapping_ranges = find_number_of_partially_overlapping_pairs(to_range_pairs(input_lines))
    print(f'Task 1: Found {n_partially_overlapping_ranges} partially overlapping ranges.')
