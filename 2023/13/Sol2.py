from pycp.all import *


def score(g):
    for y in range(1, len(g)):
        zipped = list(zip(reversed(g[0:y]), g[y:]))
        if sum(1 for a, b in zipped if a == b) == len(zipped)-1:
            r = zipped[[i for i, (a, b) in enumerate(zipped) if a != b][0]]
            if sum(1 for a, b in zip(*r) if a == b) == len(r[0])-1:
                return y * 100

    g = list(zip(*g))
    for x in range(1, len(g)):
        zipped = list(zip(reversed(g[0:x]), g[x:]))
        if sum(1 for a, b in zipped if a == b) == len(zipped)-1:
            r = zipped[[i for i, (a, b) in enumerate(zipped) if a != b][0]]
            if sum(1 for a, b in zip(*r) if a == b) == len(r[0])-1:
                return x


def main(lines: list) -> None:
    grids = [[]]
    for line in lines:
        if len(line) == 0:
            grids.append([])
        else:
            grids[-1].append(line)

    print(sum(score(g) for g in grids))


if __name__ == '__main__':
    run(main, list)
