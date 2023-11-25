from copy import deepcopy


ADJACENT = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def neighbours(grid, x, y):
    return sum(grid[y+dy][x+dx] == "#" for (dx, dy) in ADJACENT if (0 <= y+dy < len(grid)) and (0 <= x+dx < len(grid[y+dy])))


def step(grid):
    old = deepcopy(grid)
    for (y, line) in enumerate(old):
        for (x, char) in enumerate(old[y]):
            n = neighbours(old, x, y)
            if char == "#" and n != 1:
                grid[y][x] = "."
            elif char == "." and 1 <= n <= 2:
                grid[y][x] = "#"


def biodiversity(grid):
    return sum([2**i for (i, cell) in enumerate(sum(grid, [])) if cell == "#"])


if __name__ == "__main__":
    grid = [list(line.strip()) for line in open("Input.txt", "r").readlines()]

    mem = {}
    while True:
        t = tuple([tuple(row) for row in grid])
        if t in mem:
            break
        else:
            mem[t] = True
        step(grid)

    print(biodiversity(grid))
