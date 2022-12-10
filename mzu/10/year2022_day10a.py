from aocd import data

DAY = '10'
PART = 'a'


def calculate_signal_strength(X, cycles, interesting_cycles):
    if cycles in interesting_cycles:
        return X * cycles
    else:
        return 0


def solve(lines):
    X = 1
    cycles = 0
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0
    for line in lines:
        if line == "noop":
            cycles += 1
            total_signal_strength += calculate_signal_strength(X, cycles, interesting_cycles)
        else:
            cycles += 1
            total_signal_strength += calculate_signal_strength(X, cycles, interesting_cycles)
            cycles += 1
            total_signal_strength += calculate_signal_strength(X, cycles, interesting_cycles)
            X += int(line.split(' ')[1])
    return total_signal_strength


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')

    lines = data.splitlines()
    result = solve(lines)
    
    print(f'The total signal strength is {str(result)}.')


if __name__ == '__main__':
    main()
