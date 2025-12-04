from pycp.all import *


def parse(line):
    return list(line)


def main(lines):
    grid = Grid(lines)
    h, w = len(lines), len(lines[0])
    count = 0
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
            count += 1
    print(count)


if __name__ == '__main__':
    run(main, parse)
