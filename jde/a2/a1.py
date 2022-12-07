score = 0
inp = []
with open("input.in") as f: 
    temp = 0
    for line in f:
        inp.append(line.rstrip().split(" "))

for a, b in inp:
    if b == 'X':
        if a == 'A':
            score += 4
        if a == 'B':
            score += 1
        if a == 'C':
            score += 7
    if b == 'Y':
        if a == 'A':
            score += 8
        if a == 'B':
            score += 5
        if a == 'C':
            score += 2
    if b == 'Z':
        if a == 'A':
            score += 3
        if a == 'B':
            score += 9
        if a == 'C':
            score += 6


print(score)