def manhatan(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


def nearest(coords: dict, p):
    first = list(coords.items())[0]
    min_dist = manhatan(first[0], p) +1
    first = None
    for point, id in coords.items():
        dist = manhatan(point, p)
        if dist == min_dist:
            first.append(id)
        elif dist < min_dist:
            first = [id]
            min_dist = dist
    return -1 if len(first) != 1 else first[0]


def check(grid, min_x, max_x, min_y, max_y):
    for x in range(1, max_x - min_x):
        if grid[0][x] != grid[1][x]:
            return True
        if grid[-1][x] != grid[-2][x]:
            return True
    for y in range(1, max_y - min_y):
        if grid[y][0] != grid[y][1]:
            return True
        if grid[y][-1] != grid[y][-2]:
            return True
    return False


def solve(coords):
    min_x = min(k[0] for k in coords.keys())
    max_x = max(k[0] for k in coords.keys())
    min_y = min(k[1] for k in coords.keys())
    max_y = max(k[1] for k in coords.keys())

    grid = [[nearest(coords, (x, y)) for x in range(min_x, max_x+1)] for y in range(min_y, max_y+1)]

    while check(grid, min_x, max_x, min_y, max_y):
        min_x -= 1
        max_x += 1
        min_y -= 1
        max_y += 1
        grid = [[None] + row + [None] for row in grid]
        grid = [[None] * len(grid[0])] + grid + [[None] * len(grid[0])]

        for x in range(0, max_x - min_x+1):
            grid[0][x] = nearest(coords, (x + min_x, min_y))
            grid[-1][x] = nearest(coords, (x + min_x, max_y))
        for y in range(0, max_y - min_y+1):
            grid[y][0] = nearest(coords, (min_x, y + min_y))
            grid[y][-1] = nearest(coords, (max_x, y + min_y))

    areas = {i: sum([len([j for j in line if j == i]) for line in grid]) for ((x, y), i) in coords.items()}
    for x in range(0, max_x - min_x + 1):
        if grid[0][x] in areas:
            del areas[grid[0][x]]
        if grid[-1][x] in areas:
            del areas[grid[-1][x]]
    for y in range(0, max_y - min_y + 1):
        if grid[y][0] in areas:
            del areas[grid[y][0]]
        if grid[y][-1] in areas:
            del areas[grid[y][-1]]

    return max(areas.values())


if __name__ == "__main__":
    coords = [coord.strip().split(",") for coord in open("input.txt", "r").readlines()]
    coords = {x: id for id, x in enumerate(map(lambda x: (int(x[0]), int(x[1])), coords))}
    print(solve(coords))
