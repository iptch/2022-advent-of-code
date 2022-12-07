with open('data.txt') as f:
    buffer = f.read()
marker_size = 14
for i in range(len(buffer)-marker_size):
    if len(set(buffer[i:i+marker_size])) == marker_size:
        print(f'Result: {i+marker_size}')
        break

print('end')