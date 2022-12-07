elves = []
with open("input.in") as f: 
    temp = 0
    for line in f:
        if line == "\n" or line == "":
            elves.append(temp)
            temp = 0
        else:
            temp += int(line)
elves.append(temp)
           
elves = sorted(elves)
print(elves)
print(elves[-1], elves[-2], elves[-3])
print(sum([elves[-1], elves[-2], elves[-3]]))