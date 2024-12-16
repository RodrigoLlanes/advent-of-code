from pycp.all import *


DIRS = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]


def parse(line: str):
    return list(line)


def main(lines: list[list[int]]):
    grid = Grid(lines)

    for p, elem in grid.items():
        if elem == 'S':
            pos = p
        if elem == 'E':
            end = p
    grid[pos] = grid[end] = '.'

    heap = Heap()
    heap.push((0, 0, pos))
    best = defaultdict(lambda: float('inf'))
    while len(heap):
        score, dir, pos = heap.pop()

        if score > best[pos, dir]:
            continue

        best[pos, dir] = score

        if pos == end:
            continue

        if grid[pos + DIRS[dir]] != '#':
            heap.push((score+1, dir, pos + DIRS[dir]))

        heap.push((score + 1000, (dir+1) % 4, pos))
        heap.push((score + 1000, (dir-1) % 4, pos))

    print(min(best[end, i] for i in range(4)))


if __name__ == '__main__':
    run(main, parse)
