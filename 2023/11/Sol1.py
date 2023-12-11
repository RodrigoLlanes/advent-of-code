from pycp.all import *


def parse(line: str):
    return list(line)


def main(lines: list) -> None:
    i = 0
    while i < len(lines):
        if all(e == '.' for e in lines[i]):
            lines.insert(i, lines[i].copy())
            i += 1
        i += 1

    lines = list(map(list, zip(*lines)))
    i = 0
    while i < len(lines):
        if all(e == '.' for e in lines[i]):
            lines.insert(i, lines[i].copy())
            i += 1
        i += 1
    lines = list(map(list, zip(*lines)))

    galaxies = set(p for p, e in Grid(lines).items() if e == '#')
    d = 0
    for p0 in galaxies:
        for p1 in galaxies:
            if p0 != p1:
                d += p0.manhattan(p1)
    print(d//2)


if __name__ == '__main__':
    run(main, parse)
