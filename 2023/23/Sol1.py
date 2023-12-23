from pycp.all import *


def parse(line: str):
    return list(line)


DIRECTIONS = {
    '>': Point(1, 0),
    '<': Point(-1, 0),
    '^': Point(0, -1),
    'v': Point(0, 1)
}


def main(lines: list) -> None:
    grid = Grid(lines, rev=True)
    w, h = len(lines[0]), len(lines)
    start, end = Point(1, 0), Point(w-2, h-1)
    queue = deque([(start, 0, set())])
    best = 0
    while len(queue):
        cur, d, visited = queue.popleft()

        if cur in visited:
            continue

        if cur == end:
            best = max(best, d)

        for dir in DIRECTIONS4:
            next = cur + dir
            if 0 <= next.x < w and 0 <= next.y < h and grid[next] != '#':
                if grid[next] == '.':
                    queue.append((next, d+1, visited.union({cur})))
                else:
                    nex = next + DIRECTIONS[grid[next]]
                    queue.append((nex, d + 2, visited.union({cur, next})))

    print(best)



if __name__ == '__main__':
    run(main, parse)
