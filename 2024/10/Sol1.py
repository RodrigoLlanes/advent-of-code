from typing import Counter
from pycp.all import run, reduce, Grid, Point, DIRECTIONS4


def parse(line: str):
    return list(map(int, line))

def paths(grid, pos, visited):
    res = set()
    for dir in DIRECTIONS4:
        new_pos = dir + pos
         
        if len(grid.grid) <= new_pos.y or new_pos.y < 0 or len(grid.grid[0]) <= new_pos.x or new_pos.x < 0:
            continue

        if grid[new_pos] == grid[pos]+1 and new_pos not in visited:
            visited.add(new_pos)
            if grid[new_pos] == 9:
                res.add(new_pos)
            else:
                res = res.union(paths(grid, new_pos, visited))
                
    return res


def main(lines: list[list[int]]):
    grid = Grid(lines)
    
    res = 0
    for pos, elem in grid.items():
        if elem == 0:
            res += len(paths(grid, pos, set()))

    print(res)
 

if __name__ == '__main__':
    run(main, parse)

