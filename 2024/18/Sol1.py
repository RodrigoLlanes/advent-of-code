from pycp.all import *


def parse(line: str):
    return Point(*map(int, line.split(',')))


def main(lines: list[list[int]]):
    corrupted = set(lines[:1024])

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

    print(visited[Point(70, 70)])


if __name__ == '__main__':
    run(main, parse)

