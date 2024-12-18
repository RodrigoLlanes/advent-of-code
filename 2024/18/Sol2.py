from pycp.all import *


def parse(line: str):
    return Point(*map(int, line.split(',')))


def is_locked(corrupted):
    visited = defaultdict(lambda: float('inf'))
    heap = Heap()
    heap.push((0, Point(0, 0), []))
    while len(heap):
        length, pos, path = heap.pop()

        if length >= visited[pos]:
            continue
        visited[pos] = length

        if pos == Point(70, 70):
            break

        for dir in DIRECTIONS4:
            new_pos = pos + dir
            if new_pos not in corrupted and new_pos not in path:
                if 0 <= new_pos.x <= 70 and 0 <= new_pos.y <= 70:
                    heap.push((length+1, new_pos, path + [new_pos]))

    return visited[Point(70, 70)] == float('inf')


def main(lines: list[list[int]]):
    bounds = (0, len(lines))
    while True:
        if bounds[1] - bounds[0] == 1:
            print(','.join(map(str, lines[bounds[0]])))
            break

        i = (bounds[1] - bounds[0]) // 2
        i += bounds[0]
        if is_locked(set(lines[:i])):
            bounds = (bounds[0], i)
        else:
            bounds = (i, bounds[1])


if __name__ == '__main__':
    run(main, parse)

