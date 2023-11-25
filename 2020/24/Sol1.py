from collections import defaultdict

inp = [line.rstrip() for line in open("input.txt")]

data = defaultdict(lambda: False)
moves = {"e": (+1, -1, 0), "w": (-1, +1, 0), "se": (0, -1, +1), "sw": (-1, 0, +1), "nw": (0, +1, -1), "ne": (+1, 0, -1)}

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

print(sum([1 for k, v in data.items() if v]))
