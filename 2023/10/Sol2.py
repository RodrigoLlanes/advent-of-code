from pycp.all import *
from pycp.structures.point import DIRECTIONS4


dirs = {
    '|': [Point(0, -1), Point(0, 1)],
    '-': [Point(1, 0), Point(-1, 0)],
    'L': [Point(1, 0), Point(0, -1)],
    'J': [Point(-1, 0), Point(0, -1)],
    '7': [Point(-1, 0), Point(0, 1)],
    'F': [Point(1, 0), Point(0, 1)],
    '.': []
}

inv_dirs = {tuple(v): k for k, v in dirs.items()}


def parse(line: str):
    return list(line)


def main(lines: list) -> None:
    grid = Grid(lines, True)

    s = None
    for p, sym in grid.items():
        if sym == 'S':
            s = p
            break

    points = [s]
    while len(points) == 1 or points[0] != s:
        for dir in DIRECTIONS4:
            p = s + dir
            if len(points) > 1 and p == points[-2]:
                continue
            if p.y >= len(lines) or p.x >= len(lines[0]):
                continue
            if (grid[p] == 'S' or -dir in dirs[grid[p]]) and (grid[s] == 'S' or dir in dirs[grid[s]]):
                points.append(p)
                s = p
                break
    points = set(points)

    k = tuple(d for d in DIRECTIONS4 if -d in dirs[grid[s + d]])
    if k in inv_dirs:
        lines[s.y][s.x] = inv_dirs[k]
    else:
        lines[s.y][s.x] = inv_dirs[tuple(reversed(k))]

    count = 0
    cross = 0
    for p, sym in grid.items():
        if p in points and any(s.y == 1 for s in dirs[sym]):
            cross += 1
        elif p not in points and cross % 2 == 1:
            count += 1
    print(count)


if __name__ == '__main__':
    run(main, parse)
