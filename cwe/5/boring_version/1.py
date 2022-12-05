import re

description_lines = 10
with open('../data.txt') as f:
    lines = f.read().splitlines()

# Reading tower description
number_of_towers = 9
towers = {f'{t + 1}': [] for t in range(number_of_towers)}
for l in lines[:description_lines - 2]:
    for t in range(number_of_towers):
        c = l[4 * t + 1]
        if c != ' ':
            towers[f'{t + 1}'].append(c)

# Inverse list so that "top container" is last in list
for t_key in towers.keys():
    towers[t_key].reverse()


def move(tower_from, tower_to, towers):
    element = towers[tower_from].pop()
    towers[tower_to].append(element)


# Reading reshuffling plan
regex = r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$"
for l in lines[description_lines:]:
    matches = re.match(regex, l)
    moves = int(matches[1])
    tower_from = matches[2]
    tower_to = matches[3]
    for x in range(moves):
        move(tower_from, tower_to, towers)

top_elements = [val[-1] for val in towers.values()]
result = ''.join(top_elements)
print(result)
