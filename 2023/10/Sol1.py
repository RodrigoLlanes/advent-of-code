from pycp.all import *
from pycp.structures.point import DIRECTIONS4


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
    s = None
    for y, line in enumerate(lines):
        for x, symb in enumerate(line):
            if symb == 'S':
                s = Point(x, y)
                break

    points = [(0, s)]
    while len(points) == 1 or points[0][1] != s:
        for dir in DIRECTIONS4:
            p = s + dir
            if len(points) > 1 and p == points[-2][1]:
                continue
            if p.y >= len(lines) or p.x >= len(lines[0]):
                continue
            if (lines[p.y][p.x] == 'S' or any(d == -dir for d in dirs[lines[p.y][p.x]])) and \
               (lines[s.y][s.x] == 'S' or any(d == dir for d in dirs[lines[s.y][s.x]])):
                points.append((points[-1][0]+1, p))
                s = p
                break
    print(points[-1][0]/2)


if __name__ == '__main__':
    run(main, parse)
