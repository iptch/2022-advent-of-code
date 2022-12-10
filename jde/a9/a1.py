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

    xT, yT = 0, 0
    x = 0
    y = 0
    h = set()
    h.add((0,0))
    print(h)
    for m, s in moves:
        if m == 'U':
            for _ in range(s):
                y += 1
                if notTouching(x, y, xT, yT):
                    xT = x
                    yT = y - 1
                    h.add((xT, yT))
        if m == 'D':
            for i in range(s):
                y -= 1
                if notTouching(x, y, xT, yT):
                    xT = x
                    yT = y + 1
                    h.add((xT, yT))
        if m == 'L':
            for i in range(s):
                x -= 1
                if notTouching(x, y, xT, yT):
                    yT = y
                    xT = x + 1
                    h.add((xT, yT))
        if m == 'R':
            for i in range(s):
                x += 1
                if notTouching(x, y, xT, yT):
                    yT = y
                    xT = x - 1
                    h.add((xT, yT))

        print(x, y, xT, yT)

    print(h)
    print(len(h))



