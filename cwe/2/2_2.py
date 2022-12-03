with open('data.txt') as f:
    lines = f.readlines()

print(len(lines))

rules = {'A': {'X': 3, 'Y': 6, 'Z': 0},
         'B': {'X': 0, 'Y': 3, 'Z': 6},
         'C': {'X': 6, 'Y': 0, 'Z': 3}}
my_tactics = {'X': 1, 'Y': 2, 'Z': 3}
secret_tactics = {'X': 0, 'Y': 3, 'Z': 6}
# res = {'0': []}
res = []
entries = []
win_points = 0
tactics_points = 0
i = 0
for l in lines:
    try:
        l = l[:-1]
        opponent, secret_tactic = l.split(' ')
        win_point = secret_tactics[secret_tactic]
        win_points += win_point
        # my_move = [k for k, v in rules[opponent].items() if v == win_point]
        my_move = list(rules[opponent].keys())[list(rules[opponent].values()).index(win_point)]
        tactics_points += my_tactics[my_move]
    except Exception as ex:
        print(ex)
    i += 1
print(win_points)
print(tactics_points)

print(win_points + tactics_points)
