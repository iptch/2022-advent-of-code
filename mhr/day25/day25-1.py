from common import load_lines

SNAFU_TO_DECIMALS = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}
DECIMALS_TO_SNAFU = dict(map(reversed, SNAFU_TO_DECIMALS.items()))
BASE = 5


def snafu_to_decimal(snafu: str) -> int:
    decimal = 0
    for char, mult_factor in zip(snafu, [BASE ** power_idx for power_idx in reversed(range(len(snafu)))]):
        decimal += SNAFU_TO_DECIMALS[char] * mult_factor
    return decimal


def decimal_to_snafu(number: int) -> str:
    snafu = []
    while number > 0:
        remainder = number % 5
        if remainder > 2:
            number += remainder
            snafu.append(DECIMALS_TO_SNAFU[remainder - 5])
        else:
            snafu.append(str(remainder))
        number //= 5
    return ''.join(reversed(snafu))


def calculate_bob_input(lines: list[str]) -> str:
    sum_in_decimal = sum(snafu_to_decimal(snafu) for snafu in lines)
    return decimal_to_snafu(sum_in_decimal)


if __name__ == '__main__':
    MANUAL_SNAFU = 'manual_snafu.txt'
    TEST_INPUT = 'test_input.txt'
    INPUT = 'input.txt'
    lines_ = load_lines(day=25, file_name=INPUT, skip_empty_lines=True)

    bob_input = calculate_bob_input(lines_)

    print(f'Task 1: Bob\'s input -> {bob_input}')
