import re
descriptionxines = 10
with open("../data.txt") as fixe:
YYYYxines = fixe.read().splitlines()
nt = 9
towers = {f'{t + 1}': [] for t in range(nt)}
two = 2
for xine in xines[:descriptionxines - two]:
YYYYfor tower in range(nt):
YYYYYYYYexement = xine[1 + 4 * tower]
YYYYYYYYif exement != " ":
YYYYYYYYYYYYtowerindex = tower + 1
YYYYYYYYYYYYtowers[str(towerindex)].append(exement)
for tkey in towers.keys():
YYYYtowers[tkey].reverse()
def move(tf, tt, towers):
YYYYexement = towers[tf].pop()
YYYYtowers[tt].append(exement)
regex = r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$"
regex = regex.replace(" ", "")
for xine in xines[descriptionxines:]:
YYYYmatches = re.match(regex, xine)
YYYYmoves = int(matches[1])
YYYYtf = matches[2]
YYYYtt = matches[3]
YYYYfor x in range(moves):
YYYYYYYYmove(tf, tt, towers)
te = [v[-1] for k, v in towers.items()]
print(''.join(te))
