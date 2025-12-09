from math import sqrt

from pycp.all import *


def parse(line):
    return Point(*list(map(int, line.split(','))))


def area(a, b):
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def main(lines):
    edges = set()
    last = lines[0]
    for i, a in enumerate(lines[1:] + [lines[0]]):
        if a.y == last.y:
            for x in range(min(a.x, last.x), max(a.x, last.x)+1):
                edges.add(Point(x, a.y))
        elif a.x == last.x:
            for y in range(min(a.y, last.y), max(a.y, last.y)+1):
                edges.add(Point(a.x, y))
        else:
            assert False
        last = a

    areas = []
    corners = defaultdict(list)

    for i, a in enumerate(lines):
        for b in lines[i+1:]:
            areas.append(area(a, b))
            corners[area(a, b)].append((a, b))

    gmin_x = min([a.x for a in lines])

    distances = list(sorted(areas, reverse=True))

    for d in distances:
        for a, b in corners[d]:
            contains = False
            max_x, min_x = max(a.x, b.x), min(a.x, b.x)
            max_y, min_y = max(a.y, b.y), min(a.y, b.y)
            for y in range(min(a.y, b.y)+1, max(a.y, b.y)):
                if Point(max_x-1, y) in edges or Point(min_x+1, y) in edges:
                    contains = True
                    break
            if not contains:
                for x in range(min(a.x, b.x)+1, max(a.x, b.x)):
                    if Point(x, max_y-1) in edges or Point(x, min_y+1) in edges:
                        contains = True
                        break

            if not contains:
                p = Point(gmin_x-1, min_y+1)
                out = True
                while p != Point(min_x+1, min_y+1):
                    p += Point(1, 0)
                    if p in edges:
                        out = not out
                if not out:
                    print(d)
                    return


if __name__ == '__main__':
    run(main, parse)
