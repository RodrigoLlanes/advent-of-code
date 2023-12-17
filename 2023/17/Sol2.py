from pycp.all import *


def parse(line: str):
    return list(map(int, line))


def main(lines: list) -> None:
    grid = Grid(lines, rev=True)
    target = Point(len(lines[0])-1, len(lines)-1)

    heap = Heap([(0, Point(0, 0), dir) for dir in DIRECTIONS4])
    visited = {}
    best = float('inf')
    while len(heap):
        loss, p, dir = heap.pop()

        if loss >= best:
            continue

        key = (p, Point(abs(dir.x), abs(dir.y)))
        if key in visited and visited[key] <= loss:
            continue
        visited[key] = loss

        if p == target:
            best = loss
            continue

        for direction in DIRECTIONS4:
            if direction != dir and direction != -dir:
                for i in range(4, 10+1):
                    pos = p + direction * i
                    if pos.x < 0 or pos.x >= len(lines[0]) or pos.y < 0 or pos.y >= len(lines):
                        continue
                    l = loss + sum(grid[p + direction * j] for j in range(1, i+1))
                    heap.push((l, pos, direction))

    print(best)


if __name__ == '__main__':
    run(main, parse)
