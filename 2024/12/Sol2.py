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
        borders = defaultdict(set)
        value = grid[list(group)[0]]
        for point in group:
            for dir in DIRECTIONS4:
                p = point + dir
                if len(lines[0]) > p.x >= 0 and len(lines) > p.y >= 0:
                    if grid[p] != value:
                        borders[dir].add(p)
                else:
                    borders[dir].add(p)

        perimeter = 0
        for dir, border in borders.items():
            diff = Point(0, 1) if dir.x != 0 else Point(1, 0)

            while len(border) > 0:
                point = border.pop()
                perimeter += 1

                for d in (diff, -diff):
                    p = point
                    while p + d in border:
                        p = p + d
                        border.remove(p)

        res += perimeter * len(group)

    print(res)


if __name__ == '__main__':
    run(main, parse)
