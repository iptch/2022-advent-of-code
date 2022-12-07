m = 0
with open("input.in") as f: 
    temp = 0
    for line in f:
        if line == "\n" or line == "":
            m = max(temp, m)
            temp = 0
        else:
            print(line)
            temp += int(line)
print(m)