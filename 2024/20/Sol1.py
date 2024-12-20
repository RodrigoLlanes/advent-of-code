from pycp.all import *


def parse(line: str):
    return list(line)


def main(lines: list[str]):
    grid = Grid(lines)

    for p, elem in grid.items():
        if elem == 'S':
            pos = p
        if elem == 'E':
            end = p
    grid[pos] = grid[end] = '.'

    l = [(pos, [pos])]
    while len(l):
        pos, path = l.pop()

        if pos == end:
            break

        for dir in DIRECTIONS4:
            if grid[pos+dir] == '.' and (len(path) == 1 or pos + dir != path[-2]):
                l.append((pos+dir, path + [pos+dir]))

    res = 0
    for i, p0 in enumerate(path):
        for j in range(i+1, len(path)):
            d = p0 - path[j]
            if d.manhattan() == 2 and abs(i-j) - 2 >= 100:
                res += 1

    print(res)


if __name__ == '__main__':
    run(main, parse)

