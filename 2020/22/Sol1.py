inp = [line.rstrip() for line in open("input.txt")]
player_1 = [int(x) for x in inp[1:inp.index("")]]
player_2 = [int(x) for x in inp[inp.index("")+2:]]

while len(player_1) != 0 and len(player_2) != 0:
    p1 = player_1.pop(0)
    p2 = player_2.pop(0)
    if p1 > p2:
        player_1 += [p1, p2]
    else:
        player_2 += [p2, p1]

winner = player_1 if len(player_1) > 0 else player_2

i = 0
res = 0
for w in reversed(winner):
    i += 1
    res += w * i

print(res)
