from pycp.all import *


def parse(line):
    return Point(*list(map(int, line.split(','))))


def area(a, b):
    return (abs(a.x - b.x) + 1) * (abs(a.y - b.y) + 1)


def main(lines):
    areas = []

    for i, a in enumerate(lines):
        for b in lines[i+1:]:
            areas.append(area(a, b))

    areas = list(sorted(areas, reverse=True))
    print(areas[0])


if __name__ == '__main__':
    run(main, parse)
