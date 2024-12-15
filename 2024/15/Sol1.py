from pycp.all import run, Grid, Point


DIRS = {
    '>': Point(0, 1),
    '<': Point(0, -1),
    '^': Point(-1, 0),
    'v': Point(1, 0)
}


def parse(line: str):
    return line


def move(grid, pos, dir):
    if grid[pos+dir] == '.':
        grid[pos+dir] = 'O'
        return True
    elif grid[pos+dir] == '#':
        return False
    elif grid[pos+dir] == 'O':
        return move(grid, pos+dir, dir)


def main(lines: list[list[int]]):
    grid, data = '\n'.join(lines).split('\n\n')
    grid = Grid([list(line) for line in grid.split('\n')])
    movement = ''.join(data.split('\n'))

    for p, elem in grid.items():
        if elem == '@':
            pos = p

    for m in movement:
        dir = DIRS[m]
        if grid[pos+dir] == '.':
            grid[pos] = '.'
            grid[pos+dir] = '@'
            pos = pos+dir
        elif move(grid, pos, dir):
            grid[pos] = '.'
            grid[pos+dir] = '@'
            pos = pos + dir
    
    res = 0
    for p, elem in grid.items():
        if elem == 'O':
            res += p.x * 100 + p.y
    
    #print('\n'.join(map(''.join, grid.grid)))

    print(res)


if __name__ == '__main__':
    run(main, parse)

