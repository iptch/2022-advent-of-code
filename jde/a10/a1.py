import functools
sig = []
#ind 1: after the first cycle
sig.append(1)
with open("input.in") as f:
    for idx, line in enumerate(f):
        l = line.rstrip()
        if str(l).startswith('noop'):
            sig.append(0)
        else:
            sig.append(0)
            sig.append(int(l.split(' ')[1]))
res = [sig[0]]
for i in range(1, len(sig)):
    res.append(res[i-1] + sig[i])

print(res)
points = [ a * (indx +1) for indx, a in enumerate(res) if (indx + 1) == 20 or (indx + 1 + 20) % 40 == 0 ]
print(points)
print(sum(points))

