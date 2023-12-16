from pycp.all import *


def parse(line: str):
    return list(line)


split = {Point(0, 1): [Point(1, 0), Point(-1, 0)],
         Point(0, -1): [Point(1, 0), Point(-1, 0)],
         Point(1, 0): [Point(0, 1), Point(0, -1)],
         Point(-1, 0): [Point(0, 1), Point(0, -1)]}


def solve(point, direction, grid):
    start = [(point, direction)]
    visited = set()
    while len(start):
        pos, dir = start.pop()

        if pos.x < 0 or pos.x >= len(grid.grid[0]) or pos.y < 0 or pos.y >= len(grid.grid):
            continue

        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))

        if grid[pos] == '|' and dir.y == 0:
            for d in split[dir]:
                start.append((pos + d, d))
        elif grid[pos] == '-' and dir.x == 0:
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

    return len({a for a, _ in visited})


def main(lines: list) -> None:
    grid = Grid(lines, rev=True)

    m = 0
    for y in range(len(lines)):
        m = max(m, solve(Point(0, y), Point(1, 0), grid))
        m = max(m, solve(Point(len(lines[0]) - 1, y), Point(-1, 0), grid))

    for x in range(len(lines[0])):
        m = max(m, solve(Point(x, 0), Point(0, 1), grid))
        m = max(m, solve(Point(x, len(lines) - 1), Point(0, -1), grid))

    print(m)


if __name__ == '__main__':
    run(main, parse)
