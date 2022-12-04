from day4 import Range


def test_range_fully_contains() -> None:
    first_ranges = [Range(1, 5), Range(5, 7), Range(1, 2)]
    second_ranges = [Range(3, 4), Range(6, 8), Range(1, 1)]
    expected_outputs = [True, False, ]

    for first, second, expected in zip(first_ranges, second_ranges, expected_outputs):
        assert first.fully_contains(second) == expected


def test_range_partially_overlaps() -> None:
    first_ranges = [Range(1, 5), Range(5, 7), Range(1, 2), Range(4, 6)]
    second_ranges = [Range(3, 4), Range(6, 8), Range(1, 1), Range(7, 8)]
    expected_outputs = [True, True, True, False]

    for first, second, expected in zip(first_ranges, second_ranges, expected_outputs):
        assert first.partially_overlaps(second) == expected
