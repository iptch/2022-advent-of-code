def mapToVal(a):
    return a

stck1 = []
stck1.append('W');
stck1.append('D');
stck1.append('G');
stck1.append('B');
stck1.append('H');
stck1.append('R');
stck1.append('V');
stck2 = list('WDGBHRV')
stck2 = list('JNGCRF')
stck3 = list('LSFHDNJ')
stck4 = list('JDSV')
stck5 = list('SHDRQWNV')
stck6 = list('PGHCM')
stck7 = list('FJBGLZHC')
stck8 = list('SJR')
stck9 = list('LGSRBNVM')
stacks = [[],stck1, stck2, stck3, stck4, stck5, stck6, stck7, stck8, stck9]
score = 0
stck = []
inp = []
with open("input.in") as f:         
    for line in f:
        inp.append(line.rstrip().split(' '))

conv = [[int(b), int(d), int(f)] for a, b, c, d, e, f in inp[10:]]
print(conv)
for a, b, c in conv:
    temp = []
    for i in range(a):
        v = stacks[b].pop()
        temp.append(v)
    for i in range(a):
        v = temp.pop()
        stacks[c].append(v)
print([list(s).pop() for s in stacks[1:]])
print(''.join([list(s).pop() for s in stacks[1:]]))
