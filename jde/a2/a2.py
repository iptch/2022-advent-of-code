score = 0
inp = []
with open("input.in") as f: 
    temp = 0
    for line in f:
        inp.append(line.rstrip().split(" "))

for a, b in inp:
    if b == 'X':
        score += 0
        if a == 'A':
            score += 3
        if a == 'B':
            score += 1
        if a == 'C':
            score += 2
    if b == 'Y':
        score += 3

        if a == 'A':
            score += 1
        if a == 'B':
            score += 2
        if a == 'C':
            score += 3
    if b == 'Z':
        score += 6
        if a == 'A':
            score += 2
        if a == 'B':
            score += 3
        if a == 'C':
            score += 1


print(score)