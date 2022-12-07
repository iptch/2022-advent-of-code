score = 0
dirs = {}
st = []
alreadylisted = set()
shouldlist = True
with open("input.in", 'r') as f: 
    for line in f:
        if line.startswith('dir'):
            continue
        elif line.startswith('$ cd ..'):
            st.pop()
        elif line.startswith('$ cd'):
            newd = line.rstrip().split(' ')[2]
            currd = ''.join(st) + newd
            st.append(currd)
        elif line.startswith('$ ls'):
            if st[-1] in alreadylisted:
                shouldlist = False
            else:
                shouldlist = True
                alreadylisted.add(st[-1])
        else:
            if not shouldlist:
                continue
            num, f = line.rstrip().split(' ')
            currd = ''.join(st) + newd
            num = int(num)
            for d in st:
                if dirs.__contains__(d):
                    dirs[d] += num
                else:
                    dirs[d] = num
            

sums = [b for a, b in dirs.items()]
print(max(sums)) 
needed = 43313415 - 40000000
print(sums)
print(st)
sums = [b for a, b in dirs.items() if b >= needed]
print(min(sums))