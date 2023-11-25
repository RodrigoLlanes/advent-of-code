from collections import defaultdict

moves = {"e": (+1, -1, 0), "w": (-1, +1, 0), "se": (0, -1, +1), "sw": (-1, 0, +1), "nw": (0, +1, -1), "ne": (+1, 0, -1)}


def calc_new_state(_pos, _data):
    c = 0
    for _move in moves.values():
        if _data[(_pos[0] + _move[0], _pos[1] + _move[1], _pos[2] + _move[2])]:
            c += 1
    if _data[_pos]:
        if c == 1 or c == 2:
            return True
        else:
            return False
    else:
        if c == 2:
            return True
        else:
            return False


inp = [line.rstrip() for line in open("input.txt")]

data = defaultdict(lambda: False)

for line in inp:
    cut = line
    pos = (0, 0, 0)
    while len(cut) > 0:
        for k, move in moves.items():
            if cut.startswith(k):
                pos = pos[0] + move[0], pos[1] + move[1], pos[2] + move[2]
                cut = cut[len(k):]
                break
    data[pos] = not data[pos]

for day in range(100):
    new_data = data.copy()
    for pos in data.copy().keys():
        for move in moves.values():
            p = pos[0] + move[0], pos[1] + move[1], pos[2] + move[2]
            if p not in new_data:
                new_data[p] = calc_new_state(p, data)
        new_data[pos] = calc_new_state(pos, data)
    data = new_data

print(sum([1 for k, v in data.items() if v]))
