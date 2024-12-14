from pycp.all import run, Point
import re



def parse(line: str):
    return map(int, re.findall(r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)', line)[0])


def main(lines: list[list[int]]):
    size = Point(101, 103)
    positions = []
    for x, y, vx, vy in lines:
        positions.append((Point(x, y), Point(vx, vy)))

    for _ in range(100):
        new_pos = []
        for p, d in positions:
            p = p + d
            p = Point(p.x % size.x, p.y % size.y)
            new_pos.append((p, d))
        positions = new_pos

    tl = tr = bl = br = 0
    for p, _ in positions:
        if p.x < size.x // 2:
            if p.y < size.y // 2:
                tl += 1
            elif p.y > size.y // 2:
                bl += 1
        elif p.x > size.x //2:
            if p.y < size.y // 2:
                tr += 1
            elif p.y > size.y // 2:
                br += 1

    print(tl * tr * bl * br)


if __name__ == '__main__':
    run(main, parse)

