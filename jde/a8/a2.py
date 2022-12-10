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

vert2 = list(zip(*hor[::-1]))
vert = [list(reversed(a)) for a in vert2]
print(list(range(100)[:5]))
print(hor)
print(vert)
def scoreForPos(x, y, lenx, leny):
    res = 1
    height = hor[y][x][1]
    height2 = vert[x][y][1]
    if height2 != height:
        raise Exception
    print('h:', height)
    count = 0
    for a in hor[y][x+1:]:
        count += 1
        if a[1] >= height:
            break
    res *= count
    print(count)
    count = 0
    for a in list(reversed(hor[y][:max(0,x)])):
        count += 1
        if a[1] >= height:
            break
    res *=  count
    print(count)
    count = 0
    for a in vert[x][y+1:]:
        count += 1
        if a[1] >= height:
            break
    res *= count
    print(count)
    count = 0
    #nach unten
    for a in list(reversed(vert[x][:max(0,y)])):
        count += 1
        if a[1] >= height:
            break
    res *= count
    print(count)
    return res

score = 0
for y in range(len(hor)):
    for x in range(len(hor[0])):
        score = max(score, scoreForPos(x, y, 0, 0))
print(score)