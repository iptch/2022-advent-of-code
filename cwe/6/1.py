with open('data.txt') as f:
    buffer = f.read()

for i in range(len(buffer)-4):
    if len(set(buffer[i:i+4])) == 4:
        print(f'Result: {i+4}')
        break

print('end')