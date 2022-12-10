moves = []
with open("input.in") as f:
    for idx, line in enumerate(f):
        l = []
        move, step = line.rstrip().split(' ')
        moves.append([move, int(step)])

    def notTouching(x, y, xT, yT):
        res = not (abs(x - xT) <= 1 and abs(y - yT) <= 1)
        #print(res)
        return res

    def moveMode(x, y, xT, yT):
        if abs(y - yT) == abs(x - xT) and abs(x - xT) != 2:
            print("Problem: amount: ", abs(x - xT))
        if abs(y - yT) == abs(x - xT):
            ret = 'X'
            if x > xT:
                ret += 'R'
            if x < xT:
                ret += 'L'
            if y > yT:
                ret += 'U'
            if y < yT:
                ret += 'D'
            #print(ret)
            return ret, abs(x - xT)
        if abs(x - xT) > abs(y - yT):
            if x > xT:
                return 'R', 0
            if x < xT:
                return 'L', 0
        else:
            if y > yT:
                return 'U', 0
            if y < yT:
                return 'D', 0

    def corrFormovemode(x, y, xx, yy, tail=False):
        m, amt = moveMode(x, y, xx, yy)
        xT = xx
        yT = yy
        if m == 'U':
            xT = x
            yT = yT + 1
        elif m == 'D':
            xT = x
            yT = yT - 1
        elif m == 'L':
            xT = xT -1
            yT = y
        elif m == 'R':
            xT = xT + 1
            yT = y
        if m == 'XRD':
            xT = xT + 1
            yT = yT - 1
        if m == 'XRU':
            xT = xT + 1
            yT = yT + 1
        if m == 'XLD':
            xT = xT - 1
            yT = yT - 1
        if m == 'XLU':
            xT = xT - 1
            yT = yT + 1
        return xT, yT

    print(list(range(9)))
    xTail, yTail = 0, 0
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    h = set()
    h.add((0, 0))
    for m, s in moves:
        for _ in range(s):
            if m == 'U':
                y[0] += 1
            if m == 'D':
                y[0] -= 1
            if m == 'L':
                x[0] -= 1
            if m == 'R':
                x[0] += 1
            for i in range(1, 9):
                while notTouching(x[i-1], y[i-1], x[i], y[i]):
                    x[i], y[i] = corrFormovemode(x[i-1], y[i-1], x[i], y[i], False)
            while notTouching(x[-1], y[-1], xTail, yTail):
                #print(x[-1], y[-1], xTail, yTail)
                xTail, yTail = corrFormovemode(x[i-1], y[i-1], xTail, yTail, True)
                h.add((xTail, yTail))
    print(x, y)
    print(sorted(h))
    print(len(h))




