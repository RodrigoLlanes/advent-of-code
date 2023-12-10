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
    s = None
    for y, line in enumerate(lines):
        for x, symb in enumerate(line):
            if symb == 'S':
                s = Point(x, y)
                break

    points = [s]
    while len(points) == 1 or points[0] != s:
        for dir in DIRECTIONS4:
            p = s + dir
            if len(points) > 1 and p == points[-2]:
                continue
            if p.y >= len(lines) or p.x >= len(lines[0]):
                continue
            if (lines[p.y][p.x] == 'S' or any(d == -dir for d in dirs[lines[p.y][p.x]])) and \
               (lines[s.y][s.x] == 'S' or any(d == dir for d in dirs[lines[s.y][s.x]])):
                points.append(p)
                s = p
                break
    points = set(points)

    k = []
    for d in DIRECTIONS4:
        p = s + d
        if s + d in points and any(-d == dir for dir in dirs[lines[p.y][p.x]]):
            k.append(d)
    k = tuple(k)
    if k in inv_dirs:
        lines[s.y][s.x] = inv_dirs[k]
    else:
        lines[s.y][s.x] = inv_dirs[tuple(reversed(k))]


    count = 0
    cross = 0
    for y, line in enumerate(lines):
        for x, symb in enumerate(line):
            p = Point(x, y)
            if p in points and any(s.y == 1 for s in dirs[symb]):
                cross += 1
            elif p not in points and cross % 2 == 1:
                count += 1
    print(count)


if __name__ == '__main__':
    run(main, parse)
