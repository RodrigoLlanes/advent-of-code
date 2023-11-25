from collections import defaultdict
import re


def clear(fabric, intacts, id):
    dx, dy, w, h = intacts[id]
    for y in range(dy, dy+h):
        for x in range(dx, dx+w):
            fabric[(x, y)] = -1
    del intacts[id]


def solve(claims):
    regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
    fabric = defaultdict(int)
    intacts = {}
    for claim in claims:
        intact = True
        id, dx, dy, w, h = [int(param) for param in regex.match(claim).groups()]
        for y in range(dy, dy+h):
            for x in range(dx, dx+w):
                if fabric[(x, y)] != 0:
                    intact = False
                    if fabric[(x, y)] != -1:
                        clear(fabric, intacts, fabric[(x, y)])
                fabric[(x, y)] = id
        
        intacts[id] = (dx, dy, w, h)
        if not intact:
            clear(fabric, intacts, id)
    return list(intacts.keys())[0]


if __name__ == "__main__":
    claims = [claim.strip() for claim in open("input.txt", "r").readlines()]
    print(solve(claims))