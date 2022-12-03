with open('data.txt') as f:
    lines = f.read().splitlines()

print(len(lines))

i = 0
result = 0
for l in lines:
    try:
        middle = int(len(l)/2)
        first = l[0:middle]
        second = l[middle:]
        double = list(set(first).intersection(set(second)))[0]
        if double in 'abcdefghijklmnopqrstuvwxyz':
            val = ord(double)-96
        else:
            val = ord(double)-38
        result += val
    except Exception as ex:
        print(ex)
    i += 1

print(result)