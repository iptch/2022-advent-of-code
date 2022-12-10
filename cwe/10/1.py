import flatdict

with open('data.txt') as f:
    lines = f.read().splitlines()

important_cycles = [220, 180, 140, 100, 60, 20]
cycle = 0
x_tot = 1

signal_tot = 0


for line in lines:
    if line.startswith('noop'):
        cycle += 1
        if cycle in important_cycles:
            signal_tot += x_tot * cycle
    elif line.startswith('addx'):
        cycle += 1
        if cycle in important_cycles:
            signal_tot += x_tot * cycle
        cycle += 1
        if cycle in important_cycles:
            signal_tot += x_tot * cycle
        x_tot += int(line.split(' ')[1])

print(signal_tot)