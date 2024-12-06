from pycp.all import run, Point, Grid


DIRECTIONS = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]


def parse(line: str):
    return line


def main(lines: list[list[int]]):
    mapa = Grid(lines)
    direction = 0
    res = 1
    pos = None
    for row, line in enumerate(lines):
        for col, elem in enumerate(line):
            if elem == '^':
                pos = Point(row, col)

    visited = {pos}
    while True:
        new_pos = pos + DIRECTIONS[direction%len(DIRECTIONS)]
        if not (len(lines[0]) > new_pos.x >= 0 and len(lines[1]) > new_pos.y >= 0):
            break
        elif mapa[new_pos] == '#':
            direction += 1
        else:
            visited.add(new_pos)
            pos = new_pos
    print(len(visited))


if __name__ == '__main__':
    run(main, parse)

