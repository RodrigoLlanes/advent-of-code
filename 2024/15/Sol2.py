from pycp.all import run, Grid, Point


DIRS = {
    '>': Point(0, 1),
    '<': Point(0, -1),
    '^': Point(-1, 0),
    'v': Point(1, 0)
}
LEFT = Point(0, -1)
RIGHT = Point(0, 1)


def parse(line: str):
    return line


def move(grid, pos, dir):
    if dir.x != 0:
        if can_move_v(grid, pos, dir):
            move_v(grid, pos, dir)
            return True
        return False
    else:
        return move_h(grid, pos, dir)


def move_h(grid, pos, dir):
    if grid[pos+dir*2] == '.':
        grid[pos+dir*2] = '[' if dir.y == -1 else ']'
        grid[pos+dir] = ']' if dir.y == -1 else '['
        return True
    elif grid[pos+dir*2] == '#':
        return False
    elif grid[pos+dir*2] in '[]':
        if move_h(grid, pos+dir*2, dir):
            grid[pos+dir*2] = '[' if dir.y == -1 else ']'
            grid[pos+dir] = ']' if dir.y == -1 else '['
            return True
        return False 


def can_move_v(grid, pos, dir):
    if grid[pos] == ']':
        pos += LEFT

    if grid[pos+dir] == '.' and grid[pos+dir+RIGHT] == '.':
        return True
    elif grid[pos+dir] == '#' or grid[pos+dir+RIGHT] == '#':
        return False
    elif grid[pos+dir] == '[':
        return can_move_v(grid, pos+dir, dir)
    
    can = True
    if grid[pos+dir] == ']':
        can = can and can_move_v(grid, pos+dir, dir)
    if grid[pos+dir+RIGHT] == '[':
        can = can and can_move_v(grid, pos+dir+RIGHT, dir)
    return can


def move_v(grid, pos, dir):
    if grid[pos] == ']':
        pos += LEFT

    if grid[pos+dir] == '[':
        move_v(grid, pos+dir, dir)
    
    if grid[pos+dir] == ']':
        move_v(grid, pos+dir, dir)
    if grid[pos+dir+RIGHT] == '[':
        move_v(grid, pos+dir+RIGHT, dir)
    
    grid[pos] = '.'
    grid[pos+RIGHT] = '.'
    grid[pos+dir] = '['
    grid[pos+dir+RIGHT] = ']'


def main(lines: list[list[int]]):
    grid_data, data = '\n'.join(lines).split('\n\n')
    grid = []
    for line in grid_data.split('\n'):
        new_line = ''
        for char in line:
            if char in '#.':
                new_line += char*2
            elif char == '@':
                new_line += '@.'
            elif char == 'O':
                new_line += '[]'
        grid.append(list(new_line))
    grid = Grid(grid)

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
        elif grid[pos+dir] == '#':
            continue
        elif move(grid, pos+dir, dir):
            grid[pos] = '.'
            grid[pos+dir] = '@'
            pos = pos + dir
 
    res = 0   
    for p, elem in grid.items():
        if elem == '[':
            res += p.x * 100 + p.y
    
    #print('\n'.join(map(''.join, grid.grid)))

    print(res)


if __name__ == '__main__':
    run(main, parse)

