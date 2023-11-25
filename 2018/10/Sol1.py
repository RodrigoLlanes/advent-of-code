import math
from collections import defaultdict
import re

if __name__ == "__main__":
    pos, vel = [], []
    lines = [line.rstrip().replace(" ", "") for line in open("input.txt").readlines()]
    for line in lines:
        x, y, vx, vy = map(int, re.match(r"position=<(-?\d+),(-?\d+)>velocity=<(-?\d+),(-?\d+)>", line).groups())
        pos.append((x, y))
        vel.append((vx, vy))

    area = math.inf
    prev = None
    while True:
        xs, ys = list(map(lambda p: p[0], pos)), list(map(lambda p: p[1], pos))
        min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
        n_area = (max_x - min_x) * (max_y - min_y)
        if area < n_area:
            break
        area = n_area
        prev = pos
        pos = [(x + vel[i][0], y + vel[i][1]) for i, (x, y) in enumerate(pos)]

    xs, ys = list(map(lambda p: p[0], prev)), list(map(lambda p: p[1], prev))
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    for y in range(min(ys), max(ys) + 1):
        for x in range(min(xs), max(xs) + 1):
            print("#" if (x, y) in prev else ".", end="")
        print()





