from pycp.all import *


def parse(line):
    return list(line)


def main(lines):
    grid = Grid(lines, rev=True)

    splits = 0
    x = lines[0].index('S')
    lifo = [[Point(x, 0), []]]
    visited = set()
    mem = defaultdict(int)
    while len(lifo) > 0:
        p, h = lifo.pop()
        if p in visited:
            for e in h[:-1]:
                mem[e] += mem[p]
            splits += mem[p]
            continue
        visited.add(p)

        if p.y >= len(lines):
            continue

        if grid[p] ==  '^':
            for p2 in h:
                mem[p2] += 1
            splits += 1
            lifo.append([p + Point(1, 0), h + [p + Point(1, 0)]])
            lifo.append([p + Point(-1, 0), h + [p + Point(-1, 0)]])
        else:
            lifo.append([p + Point(0, 1), h + [p + Point(0, 1)]])

    print(splits+1)


if __name__ == '__main__':
    run(main, parse)
