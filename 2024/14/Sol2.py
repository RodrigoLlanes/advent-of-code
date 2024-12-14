from pycp.all import run, Point, DIRECTIONS8
import re



def parse(line: str):
    return map(int, re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)[0])


def draw(positions):
    grid = [['.' for _ in range(101)] for _ in range(103)]
    for p, _ in positions:
        grid[p.y][p.x] = '#'
    print('\n'.join(map(''.join, grid)))


def main(lines: list[list[int]]):
    size = Point(101, 103)
    positions = []
    for x, y, vx, vy in lines:
        positions.append((Point(x, y), Point(vx, vy)))

    t = 0
    while True:
        t += 1
        current = set()
        new_pos = []
        for p, d in positions:
            p = p + d
            p = Point(p.x % size.x, p.y % size.y)
            new_pos.append((p, d))
            current.add(p)
        positions = new_pos
        
        count = 0
        for p in current:
            c = 0
            for dir in DIRECTIONS8:
                if p + dir in current:
                    c += 1
            count +=  (c >= 2)

        if count >= len(current) // 2:
            print(t)
            draw(positions)
            break


if __name__ == '__main__':
    run(main, parse)

