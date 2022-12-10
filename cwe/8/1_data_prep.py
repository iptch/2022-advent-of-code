with open('data.txt') as f:
    forest = f.read().splitlines()

for l in forest:
    row = ' '.join(l)
    print(f'🍿{row}🍆')
