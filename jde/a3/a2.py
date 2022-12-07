



def mapToVal(a):
    if a.islower():
        return ord(a) - 97 + 1
    else:
        return ord(a) - 65 + 27

score = 0
inp = []
with open("input.in") as f: 
    temp = 0
    group = []
    for line in f:
        temp += 1
        group.append(line.rstrip())
        if temp % 3 == 0:
            inp.append(group)
            group = []

x = [set(a).intersection(set(b), set(c)) for a, b, c in inp]
r = [[len(a)] for a in inp]
print(r)
for i in x:
    print(i)
    score += sum([mapToVal(y) for y in i])
print(score)

        
print(ord('a'))
print(ord('A'))
