from pycp.all import *


def parse(line: str):
    return list(line)


DIRECTIONS = {
    '>': Point(1, 0),
    '<': Point(-1, 0),
    '^': Point(0, -1),
    'v': Point(0, 1)
}


def path(grid, p, pdir, nodes):
    cur = p + pdir
    d = 1
    while cur not in nodes:
        for dir in DIRECTIONS4:
            if pdir != -dir and grid[cur + dir] != '#':
                pdir = dir
                cur += dir
                d += 1
                break
    return cur, d


def neighbours(grid, p, nodes):
    neigh = {}
    for dir in DIRECTIONS4:
        next = p + dir
        if 0 <= next.x < len(grid.grid[0]) and 0 <= next.y < len(grid.grid) and grid[next] != '#':
            k, v = path(grid, p, dir, nodes)
            neigh[k] = v
    return neigh


def main(lines: list) -> None:
    grid = Grid(lines, rev=True)
    w, h = len(lines[0]), len(lines)
    start, end = Point(1, 0), Point(w-2, h-1)

    nodes = {start, end}
    for p, s in grid.items():
        if s != '#' and sum(1 for d in DIRECTIONS4 if 0 <= (p+d).x < w and 0 <= (p+d).y < h and grid[p+d] != '#') > 2:
            nodes.add(p)

    graph = {}
    for node in nodes:
        graph[node] = neighbours(grid, node, nodes)

    queue = deque([(start, 0, set())])
    best = 0
    while len(queue):
        cur, d, visited = queue.popleft()

        if cur in visited:
            continue

        if cur == end:
            best = max(best, d)

        for neighbour, dist in graph[cur].items():
            queue.append((neighbour, d+dist, visited.union({cur})))

    print(best)


if __name__ == '__main__':
    run(main, parse)    # 8 minutes (I think I should have used dynamic programming)
