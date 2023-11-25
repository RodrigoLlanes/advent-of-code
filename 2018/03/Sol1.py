from collections import defaultdict
import re


def solve(claims):
    regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    fabric = defaultdict(int)
    for claim in claims:
        _, dx, dy, w, h = [int(param) for param in regex.match(claim).groups()]
        for y in range(dy, dy+h):
            for x in range(dx, dx+w):
                fabric[(x, y)] += 1
    return sum(value > 1 for value in fabric.values())


if __name__ == "__main__":
    claims = [claim.strip() for claim in open("input.txt", "r").readlines()]
    print(solve(claims))