from pycp.all import *


def parse(line):
    return list(line)

def main(lines):
    grid = Grid(lines, rev=True)

    splits = 0
    x = lines[0].index('S')
    lifo = [Point(x, 0)]
    visited = set()
    while len(lifo) > 0:
        p = lifo.pop()
        if p in visited:
            continue
        visited.add(p)
        if p.y >= len(lines):
            continue
        if grid[p] ==  '^':
            splits += 1
            lifo.append(p + Point(1, 0))
            lifo.append(p + Point(-1, 0))
        else:
            lifo.append(p + Point(0, 1))

    print(splits)


if __name__ == '__main__':
    run(main, parse)
