from pycp.all import *


directions = {
    'U': Point(0, 1),
    'D': Point(0, -1),
    'R': Point(1, 0),
    'L': Point(-1, 0)
}


def parse(line: str):
    d, l, c = line.split()
    return d, int(l)


# As I learned with hours of suffering in part 2, there was a formula, see Shoelace's formula
def main(lines: list) -> None:
    grid = defaultdict(lambda: '.')
    curr = Point(0, 0)
    grid[curr] = '#'
    for d, l in lines:
        for _ in range(l):
            curr += directions[d]
            grid[curr] = '#'


    tl = Point(0, 0)
    br = Point(0, 0)
    for p in grid.keys():
        tl.x = min(tl.x, p.x)
        tl.y = min(tl.y, p.y)
        br.x = max(br.x, p.x)
        br.y = max(br.y, p.y)

    tl += Point(-1, 0)
    br += Point(1, 0)

    y = tl.y
    while y <= br.y:
        c = 0
        x = tl.x
        while x <= br.x:
            prev = Point(x - 1, y)
            p = Point(x, y)
            n = Point(x + 1, y)
            if grid[prev] != '#' and grid[p] == '#' and grid[n] != '#':
                c += 1
            elif grid[p] == '#':
                o = -1 if grid[Point(x, y-1)] == '#' else 1
                while grid[Point(x+1, y)] == '#':
                    x += 1
                d = -1 if grid[Point(x, y-1)] == '#' else 1
                if d != o:
                    c += 1
            elif c % 2 == 1:
                grid[p] = '+'
            x += 1
        y += 1

    print(sum(1 for k, v in grid.items() if v != '.'))


if __name__ == '__main__':
    run(main, parse)
