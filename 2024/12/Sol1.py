from pycp.all import *


def parse(line: str):
    return list(line)


def main(lines: list[list[int]]):
    res = 0
    grid = Grid(lines)

    visited = set()
    groups = []
    for pos, value in grid.items():
        if pos in visited:
            continue
        group = {pos}
        visited.add(pos)

        def rec(start):
            for dir in DIRECTIONS4:
                p = start + dir
                if p in visited:
                    continue
                if len(lines[0]) > p.x >= 0 and len(lines) > p.y >= 0:
                    if grid[p] == value:
                        visited.add(p)
                        group.add(p)
                        rec(p)

        rec(pos)
        groups.append(group)

    for group in groups:
        perimeter = 0
        value = grid[list(group)[0]]
        for point in group:
            for dir in DIRECTIONS4:
                p = point + dir
                if len(lines[0]) > p.x >= 0 and len(lines) > p.y >= 0:
                    if grid[p] != value:
                        perimeter += 1
                else:
                    perimeter += 1
        res += perimeter * len(group)

    print(res)


if __name__ == '__main__':
    run(main, parse)
