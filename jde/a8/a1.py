hor = []
vert = []
with open("input.in") as f:
    for idx, line in enumerate(f):
        l = []
        strl = line.rstrip()
        for ixc, c in enumerate(strl):
            # missing zfill was the 1h-delay bug
            l.append([str(idx).zfill(3) + str(ixc).zfill(3), int(c)])
        hor.append(l)

vert = list(zip(*hor[::-1]))
counted = set()

for l in hor:
    lim = -1
    for a in l:
        if a[1] > lim:
            lim = a[1]
            counted.add(a[0])

print(sorted(counted))
for l in hor:
    lim = -1
    for a in reversed(l):
        if a[1] > lim:
            lim = a[1]
            counted.add(a[0])

print(sorted(counted))

for l in vert:
    lim = -1
    for a in l:
        if a[1] > lim:
            lim = a[1]
            counted.add(a[0])

print(sorted(counted))

for l in vert:
    lim = -1
    for a in reversed(l):
        if a[1] > lim:
            lim = a[1]
            counted.add(a[0])

print(sorted(counted))
print(len(counted))
