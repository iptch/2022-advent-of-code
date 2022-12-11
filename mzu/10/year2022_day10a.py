from aocd import data

DAY = '10'
PART = 'a'


def process_cycle(X, cycles, interesting_cycles, total_signal_strength):
    cycles += 1
    if cycles in interesting_cycles:
        total_signal_strength += X * cycles
    return cycles, total_signal_strength


def solve(lines):
    X = 1
    cycles = 0
    interesting_cycles = [20, 60, 100, 140, 180, 220]
    total_signal_strength = 0
    for line in lines:
        if line == "noop":
            cycles, total_signal_strength = process_cycle(X, cycles, interesting_cycles, total_signal_strength)
        else:
            for _ in range(2):
                cycles, total_signal_strength = process_cycle(X, cycles, interesting_cycles, total_signal_strength)
            X += int(line.split(' ')[1])
    return total_signal_strength


def main():
    print(f'Advent of Code 2022 --- Day {DAY} --- Part {PART}')
    lines = data.splitlines()
    result = solve(lines)
    print(f'The total signal strength is {str(result)}.')


if __name__ == '__main__':
    main()
