from pycp.all import run, Grid, Point
from collections import defaultdict


def parse(line: str):
    return list(line)


def main(lines: list[list[int]]):
    grid = Grid(lines)
    positions = defaultdict(list)
    
    width = len(lines)
    height = len(lines[0])

    for pos, elem in grid.items():
        if elem != '.':
            positions[elem].append(pos)
    
    antinodes = set()
    for _, nodes in positions.items():
        for i, a in enumerate(nodes):
            antinodes.add(a)
            for b in nodes[:i] + nodes[i+1:]:
                d = a - b
                p0 = a + d
                p1 = b - d
                while 0 <= p0.x < width and 0 <= p0.y < height:
                    antinodes.add(p0)
                    p0 += d
                while 0 <= p1.x < width and 0 <= p1.y < height:
                    antinodes.add(p1)
                    p1 -= d

    print(len(antinodes))


if __name__ == '__main__':
    run(main, parse)

