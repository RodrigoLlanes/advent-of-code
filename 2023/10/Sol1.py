from pycp.all import *


dirs = {
    '|': [Point(0, 1), Point(0, -1)],
    '-': [Point(1, 0), Point(-1, 0)],
    'L': [Point(1, 0), Point(0, -1)],
    'J': [Point(-1, 0), Point(0, -1)],
    '7': [Point(-1, 0), Point(0, 1)],
    'F': [Point(1, 0), Point(0, 1)],
    '.': []
}


def parse(line: str):
    return list(line)


def main(lines: list) -> None:
    grid = Grid(lines, True)

    s = None
    for p, sym in grid.items():
        if sym == 'S':
            s = p
            break

    points = [(0, s)]
    while len(points) == 1 or points[0][1] != s:
        for dir in DIRECTIONS4:
            p = s + dir
            if len(points) > 1 and p == points[-2][1]:
                continue
            if p.y >= len(lines) or p.x >= len(lines[0]):
                continue
            if (grid[p] == 'S' or -dir in dirs[grid[p]]) and (grid[s] == 'S' or dir in dirs[grid[s]]):
                points.append((points[-1][0]+1, p))
                s = p
                break
    print(int(points[-1][0]/2))


if __name__ == '__main__':
    run(main, parse)
