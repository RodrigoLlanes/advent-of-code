from pycp.all import *


def parse(line):
    return list(line)


def step(grid, h, w):
    coords = set()
    for pos, v in grid.items():
        if v != '@':
            continue
        neighbours = 0
        for dir in DIRECTIONS8:
            p = pos + dir
            if p.x < 0 or p.x >= w:
                continue
            if p.y < 0 or p.y >= h:
                continue
            if grid[p] != '@':
                continue
            neighbours += 1
        if neighbours < 4:
            coords.add(pos)
    for coord in coords:
        grid[coord] = '.'

    return grid, len(coords)


def main(lines):
    grid = Grid(lines)
    h, w = len(lines), len(lines[0])
    count = 0
    while True:
        grid, n = step(grid, h, w)
        if n == 0:
            break
        count += n
    print(count)


if __name__ == '__main__':
    run(main, parse)
