from textwrap import wrap

with open('data.txt') as f:
    lines = f.read().splitlines()


def parse_pixel(cycle, x):
    curser_start = cycle % 40
    if 3 > curser_start - x >= 0:
        return '#'
    else:
        return '.'

def calculate_cycles():
    pixel_line = ''
    cycle = 0
    x = 1
    for line in lines:
        if line.startswith('noop'):
            cycle += 1
            pixel_line += parse_pixel(cycle, x)

        elif line.startswith('addx'):
            cycle += 1
            pixel_line += parse_pixel(cycle, x)

            cycle += 1
            pixel_line += parse_pixel(cycle, x)

            x += int(line.split(' ')[1])
    return pixel_line


wrapped = wrap(calculate_cycles(), 40)
for w in wrapped:
    print(w)
