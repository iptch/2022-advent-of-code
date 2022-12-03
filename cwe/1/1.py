with open('data.txt') as f:
    lines = f.readlines()

print(len(lines))

# res = {'0': []}
res = []
# i = 0
entries = []
for l in lines:
    # print(l)
    if l != '\n':
        entries.append(int(l[:-1]))
        # res[f'{i}'].append(int(l[:-1]))

    else:
        res.append(sum(entries))
        entries = []
        # i += 1
        # res[f'{i}'] = []

print(max(res))
res.sort(reverse=True)
print(sum(res[0:3]))
print('end')