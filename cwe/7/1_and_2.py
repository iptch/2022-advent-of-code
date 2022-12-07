import flatdict
with open('data.txt') as f:
# with open('test_data.txt') as f:
    lines = f.read().splitlines()

command_lines = []
i = 1
file_structure = {'_size': 0}
current_path = []
for line in lines[i:]:
    if line == '$ cd ..':
        current_path.pop()
    elif line.startswith('$ cd '):
        current_path.append(line[5:])
    elif line.startswith('$ ls'):
        pass
    elif line.startswith('dir'):
        current_dir = file_structure
        for y in current_path:
            current_dir = current_dir[y]
        current_dir[line[4:]] = {'_size': 0}
    else:
        file_size = int(line.split()[0])
        current_dir = file_structure
        current_dir['_size'] += file_size
        for y in current_path:
            current_dir = current_dir[y]
            current_dir['_size'] += file_size

    i += 1
print('file structure created')
file_structure_flat = flatdict.FlatDict(file_structure, delimiter='.')
result = 0
for entry in file_structure_flat.values():
    if entry <= 100000:
        result += entry
print(f'Result 1: {result}')
print('end part 1 ')
total_space = 70000000
update_space = 30000000
used_space = file_structure['_size']
space_to_cleanup = -1*(total_space-update_space-used_space)
print(f'Space to cleanup: {space_to_cleanup}')
folder_sizes = file_structure_flat.values()
folder_sizes.sort(reverse=True)
f_i = 0
for f in folder_sizes:
    if f < space_to_cleanup:
        break
    f_i += 1
print(f'folder to delete: {folder_sizes[f_i -1]}')