def mapToVal(a):
    return a

score = 0
inp = []
with open("input.in") as f: 
    for line in f:
        inp.append(line.rstrip())

data=[]
print(inp[0].split(','))
for l in inp:
    data.append(l.split(','))

data2 = [[a.split('-'), b.split('-')] for a, b in data]

print(data2)
count = 0 
for a, b in data2:
    # a in b
    if int(a[0]) >= int(b[0]) and int(a[0])<= int(b[1]):
        count += 1
    elif int(b[0]) >= int(a[0]) and int(b[0]) <= int(a[1]):
        count += 1


print(count)
