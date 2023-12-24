from pycp.all import *


def parse(line: str):
    a, b = line.split(' @ ')
    return Point(*map(int, a.split(', '))), Point(*map(int, b.split(', ')))


def main(lines: list) -> None:
    min_x, max_x = 200000000000000, 400000000000000
    #min_x, max_x = 7, 27
    c = 0
    for i, (cp, cv) in enumerate(lines):
        for j, (op, ov) in enumerate(lines[i+1:]):
            if cv.x/cv.y == ov.x/ov.y: # Parallel
                continue
            x1, y1 = cp.x, cp.y
            x2, y2 = cp.x + cv.x, cp.y + cv.y
            x3, y3 = op.x, op.y
            x4, y4 = op.x + ov.x, op.y + ov.y

            px = ((x1*y2 - y1*x2) * (x3-x4) - (x1-x2)*(x3*y4-y3*x4))/ \
                 ((x1-x2) * (y3-y4) - (y1-y2)*(x3-x4))
            py = ((x1*y2 - y1*x2) * (y3-y4) - (y1-y2)*(x3*y4-y3*x4))/ \
                 ((x1-x2) * (y3-y4) - (y1-y2)*(x3-x4))

            if min_x <= px <= max_x and min_x <= py <= max_x:
                if abs(px - x1) > abs(px - x2) and abs(py - y1) > abs(py - y2):
                    if abs(px - x3) > abs(px - x4) and abs(py - y3) > abs(py - y4):
                        #print(cp, op, px, py, min_x <= px <= max_x and min_x <= py <= max_x)
                        c += 1
    print(c)
    input()


if __name__ == '__main__':
    run(main, parse)
