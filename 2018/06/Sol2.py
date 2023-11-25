def manhatan(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


def score(coords: dict, p):
    return sum(manhatan(coord, p) for coord in coords.keys())


def check(grid):
    for x in range(len(grid[0])):
        if grid[0][x] <= 10000:
            return True
        if grid[-1][x] <= 10000:
            return True
    for y in range(len(grid)):
        if grid[y][0] <= 10000:
            return True
        if grid[y][-1] <= 10000:
            return True
    return False


def solve(coords):
    min_x = min(k[0] for k in coords.keys())
    max_x = max(k[0] for k in coords.keys())
    min_y = min(k[1] for k in coords.keys())
    max_y = max(k[1] for k in coords.keys())

    grid = [[score(coords, (x, y)) for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]

    while check(grid):
        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1
        grid = [[None] + row + [None] for row in grid]
        grid = [[None] * len(grid[0])] + grid + [[None] * len(grid[0])]

        for x in range(0, max_x - min_x+1):
            grid[0][x] = score(coords, (x + min_x, min_y))
            grid[-1][x] = score(coords, (x + min_x, max_y))
        for y in range(0, max_y - min_y+1):
            grid[y][0] = score(coords, (min_x, y + min_y))
            grid[y][-1] = score(coords, (max_x, y + min_y))

    return sum([len([j for j in line if j < 10000]) for line in grid])

# x < 43341

if __name__ == "__main__":
    coords = [coord.strip().split(",") for coord in open("input.txt", "r").readlines()]
    coords = {x: id for id, x in enumerate(map(lambda x: (int(x[0]), int(x[1])), coords))}
    print(solve(coords))
