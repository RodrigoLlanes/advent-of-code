from pycp.all import run, Grid, DIRECTIONS4


def parse(line: str):
    return list(map(int, line))

def paths(grid, path, pos, visited):
    res = set()
    for dir in DIRECTIONS4:
        new_pos = dir + pos

        if len(grid.grid) <= new_pos.y or new_pos.y < 0 or len(grid.grid[0]) <= new_pos.x or new_pos.x < 0:
            continue

        if grid[new_pos] == grid[pos]+1 and new_pos not in visited:
            visited.add(new_pos)
            new_path = path + [new_pos]
            if grid[new_pos] == 9:
                res.add(tuple(new_path))
            else:
                res = res.union(paths(grid, new_path, new_pos, visited.copy())) 
    return res


def main(lines: list[list[int]]):
    grid = Grid(lines)
    
    res = 0
    for pos, elem in grid.items():
        if elem == 0:
            res += len(paths(grid, [pos], pos, set()))

    print(res)
 

if __name__ == '__main__':
    run(main, parse)

