from typing import Counter
from pycp.all import run, reduce, Point, Grid
from collections import defaultdict
from copy import deepcopy


DIRECTIONS = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]


def parse(line: str):
    return list(line)


def loop(width, height, mapa, pos):
    direction = 0
    path_dirs = defaultdict(set)
    while True:
        dir = DIRECTIONS[direction%len(DIRECTIONS)]
        new_pos = pos + dir
        if not (height > new_pos.x >= 0 and width > new_pos.y >= 0):
            return False
        elif mapa[new_pos] == '#':
            direction += 1
        else:
            if dir in path_dirs[new_pos]:
                return True
            path_dirs[new_pos].add(dir)
            pos = new_pos


def main(lines: list[list[int]]):
    mapa = Grid(lines)
    
    direction = 0
    res = 0
    starting_pos = pos = None
    for row, line in enumerate(lines):
        for col, elem in enumerate(line):
            if elem == '^':
                starting_pos = pos = Point(row, col)

    visited = {pos}
    while True:
        dir = DIRECTIONS[direction%len(DIRECTIONS)]
        new_pos = pos + dir
        if not (len(lines[0]) > new_pos.x >= 0 and len(lines[1]) > new_pos.y >= 0):
            break
        elif mapa[new_pos] == '#':
            direction += 1
        else:
            visited.add(new_pos)
            pos = new_pos

    for p in visited:
        new_map = deepcopy(mapa)
        new_map[p] = '#'
        if loop(len(lines[0]), len(lines), new_map, starting_pos):
            res += 1
    print(res)
 

if __name__ == '__main__':
    run(main, parse)

