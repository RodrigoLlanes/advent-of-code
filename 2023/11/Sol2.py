from pycp.all import *


def parse(line: str):
    return list(line)


def main(lines: list) -> None:
    x_exp = set()
    for i, line in enumerate(lines):
        if all(e == '.' for e in line):
            x_exp.add(i)

    y_exp = set()
    for i, line in enumerate(zip(*lines)):
        if all(e == '.' for e in line):
            y_exp.add(i)

    galaxies = set(p for p, e in Grid(lines).items() if e == '#')
    d = 0
    for p0 in galaxies:
        for p1 in galaxies:
            if p0 != p1:
                d += p0.manhattan(p1)
                for x in range(min(p0.x, p1.x), max(p0.x, p1.x)+1):
                    if x in x_exp:
                        d += 1000000-1
                for y in range(min(p0.y, p1.y), max(p0.y, p1.y)+1):
                    if y in y_exp:
                        d += 1000000-1
    print(d//2)


if __name__ == '__main__':
    run(main, parse)
