from pycp.all import *


def parse(line: str):
    return list(line)


split = {Point(0, 1): [Point(1, 0), Point(-1, 0)],
         Point(0, -1): [Point(1, 0), Point(-1, 0)],
         Point(1, 0): [Point(0, 1), Point(0, -1)],
         Point(-1, 0): [Point(0, 1), Point(0, -1)]}


def main(lines: list) -> None:
    grid = Grid(lines, rev=True)
    start = [(Point(0, 0), Point(1, 0))]
    visited = set()
    while len(start):
        pos, dir = start.pop()

        if pos.x < 0 or pos.x >= len(lines[0]) or pos.y < 0 or pos.y >= len(lines):
            continue

        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))

        if (grid[pos] == '|' and dir.y == 0) or (grid[pos] == '-' and dir.x == 0):
            for d in split[dir]:
                start.append((pos + d, d))
        elif grid[pos] == '\\':
            d = Point(dir.y, dir.x)
            start.append((pos + d, d))
        elif grid[pos] == '/':
            d = Point(-dir.y, -dir.x)
            start.append((pos + d, d))
        else:
            start.append((pos + dir, dir))

    print(len({a for a, _ in visited}))


if __name__ == '__main__':
    run(main, parse)
