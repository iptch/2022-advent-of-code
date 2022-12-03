with open('data.txt') as f:
    lines = f.read().splitlines()

print(len(lines))

result = 0
for i in range(0, 300, 3):
    e1 = set(lines[i])
    e2 = set(lines[i + 1])
    e3 = set(lines[i + 2])
    badge = list(e1.intersection(e2).intersection(e3))[0]
    if badge in 'abcdefghijklmnopqrstuvwxyz':
        val = ord(badge) - 96
    else:
        val = ord(badge) - 38
    result += val

print(result)
