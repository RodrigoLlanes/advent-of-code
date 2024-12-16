from pycp.all import *


def parse(line: str):
    return list(line)


DIRS = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]

def main(lines: list[list[int]]):
    grid = Grid(lines)

    for p, elem in grid.items():
        if elem == 'S':
            pos = p
        if elem == 'E':
            end = p
    grid[pos] = grid[end] = '.'

    heap = Heap()
    heap.push((0, 0, pos, (pos,)))
    best = defaultdict(lambda: float('inf'))
    tiles = set()
    best_end = float('inf')
    while len(heap):
        score, dir, pos, path = heap.pop()
        path = list(path)

        if score > best[pos, dir]:
            continue

        best[pos, dir] = score

        if pos == end:
            if score < best_end:
                tiles = set(path)
                best_end = score
            elif score == best_end:
                tiles = tiles.union(set(path))
            continue

        best[pos, dir] = score

        if grid[pos + DIRS[dir]] != '#':
            heap.push((score+1, dir, pos + DIRS[dir], tuple(path + [pos + DIRS[dir]])))

        heap.push((score + 1000, (dir+1) % 4, pos, tuple(path)))
        heap.push((score+1000, (dir-1) % 4, pos, tuple(path)))

    print(len(tiles))


if __name__ == '__main__':
    run(main, parse)
