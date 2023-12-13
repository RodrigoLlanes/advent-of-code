from pycp.all import *


def score(g):
    for y in range(1, len(g)):
        if all(a == b for a, b in zip(reversed(g[0:y]), g[y:])):
            return y * 100

    g = list(zip(*g))
    for y in range(1, len(g)):
        if all(a == b for a, b in zip(reversed(g[0:y]), g[y:])):
            return y


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
