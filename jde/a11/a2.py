
monkeys = []
startitems = []
op = []
test = []
denominators = []
nextTrue = []
nextFalse = []

with open("input.in") as f:
    for idx, line in enumerate(f):
        l = line.rstrip()
        if l == '':
            monkeys.append((startitems, op, test, nextTrue, nextFalse))
        elif "Monkey" in l:
            continue
        elif "Starting" in l:
            startitems = list(map(int, l.split(': ')[1].split(', ')))
        elif "Operation" in l:
            if '*' in l:
                el = l.split(' * ')[1]
                if el == 'old':
                    op = lambda x: x * x
                else:
                    s = "lambda x: x * " + el
                    op = eval(s)
            if '+' in l:
                el = l.split(' + ')[1]
                if el == 'old':
                    op = lambda x: x + x
                else:
                    s = "lambda x: x + " + el
                    op = eval(s)
        elif "Test" in l:
            div = l.split(' ')[-1]
            s = "lambda x: x % " + div + " == 0"
            test = eval(s)
            denominators.append(int(div))
        elif "true" in l:
            nextTrue = int(l.split(' ')[-1])
        elif "false" in l:
            nextFalse = int(l.split(' ')[-1])
monkeys.append((startitems, op, test, nextTrue, nextFalse))
print(monkeys)

inspections = [0 for m in monkeys]

commonDenom = 1
for d in denominators:
    commonDenom *= d

for r in range(10000):
    for m in range(len(monkeys)):
        mk = monkeys[m]
        n = len(mk[0])
        for i in range(n):
            wrl = mk[0].pop(0)
            inspections[m] += 1
            newval = mk[1](wrl)
            newval = newval % commonDenom
            if mk[2](newval):
                monkeys[mk[3]][0].append(newval)
            else:
                monkeys[mk[4]][0].append(newval)
print([l[0] for l in monkeys])


inspections = sorted(inspections)
print(inspections)
print(inspections[-1] * inspections[-2])



