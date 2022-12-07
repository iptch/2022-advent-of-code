



def mapToVal(a):
    if a.islower():
        return ord(a) - 97 + 1
    else:
        return ord(a) - 65 + 27

score = 0
inp = []
with open("input.in") as f: 
    temp = 0
    for line in f:
        inp.append([line[0:(int(len(line)/2))], line[int(len(line)/2):].rstrip()])

x = [set(a).intersection(set(b)) for a, b in inp]
r = [[len(a), len(b)] for a, b in inp]
print(r)
for i in x:
    print(i)
    score += sum([mapToVal(y) for y in i])
print(score)

        
print(ord('a'))
print(ord('A'))
