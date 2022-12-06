from aocd import data

MARKER_SIZE = 14

DAY = '6'
PART = 'b'


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    all_chars = lines[0]
    for i in range(len(all_chars)):
        index_after_last_read_char = i + 1
        start_index = index_after_last_read_char - MARKER_SIZE
        if start_index < 0:
            start_index = 0
        current_chars = all_chars[start_index:index_after_last_read_char]
        if len(set(current_chars)) == MARKER_SIZE:
            print(f'First marker found! It is {str(index_after_last_read_char)}')
            break


if __name__ == '__main__':
    main()
