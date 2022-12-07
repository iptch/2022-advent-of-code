def mapToVal(a):
    return a

score = 0
inp = []
with open("input.in") as f: 
    for line in f:
        inp.append(line.rstrip())



x = [a for a in inp]
r = [[len(a)] for a in x]
