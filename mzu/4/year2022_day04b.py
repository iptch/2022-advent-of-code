from aocd import data

DAY = '4'
PART = 'b'


def read_cleaning_areas(line):
    range_first_elf, range_second_elf = line.split(',')
    start_first_elf, end_first_elf = [int(section_id) for section_id in range_first_elf.split('-')]
    start_second_elf, end_second_elf = [int(section_id) for section_id in range_second_elf.split('-')]
    cleaning_areas_first_elf = range(start_first_elf, end_first_elf + 1)
    cleaning_areas_second_elf = range(start_second_elf, end_second_elf + 1)
    return cleaning_areas_first_elf, cleaning_areas_second_elf


def has_overlapping_sections(cleaning_areas_first_elf, cleaning_areas_second_elf):
    return any(area in cleaning_areas_second_elf for area in cleaning_areas_first_elf) or \
           any(area in cleaning_areas_first_elf for area in cleaning_areas_second_elf)


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()

    number_of_overlapping_pairs = 0
    for line in lines:
        cleaning_areas_first_elf, cleaning_areas_second_elf = read_cleaning_areas(line)
        if has_overlapping_sections(cleaning_areas_first_elf, cleaning_areas_second_elf):
            number_of_overlapping_pairs += 1

    print(f'There are a total of {str(number_of_overlapping_pairs)} overlapping elf pairs.')


if __name__ == '__main__':
    main()
