from pycp.all import *


directions = {
    'U': Point(0, -1),
    'D': Point(0, 1),
    'R': Point(1, 0),
    'L': Point(-1, 0)
}


codes = 'R, D, L, U'.split(', ')


def parse(line: str):
    d, l, c = line.split()
    return codes[int(c[-2])], int(c[2:-2], 16)


# There was a formula, for the next time see Shoelace's formula
def main(lines: list) -> None:
    is_corner = defaultdict(lambda: False)

    edges = []
    curr = Point(0, 0)
    for index, (d, l) in enumerate(lines):
        if d in ('L', 'R'):
            s, end = curr, curr + directions[d] * l
            s, end = (s, end) if s.x < end.x else (end, s)
            if lines[(index-1)%len(lines)][0] != lines[(index+1)%len(lines)][0]:
                is_corner[(s, end)] = True
            edges.append((s, end))
        else:
            s, end = curr, curr + directions[d] * l
            s, end = (s, end) if s.y < end.y else (end, s)
            s, end = s + Point(0, 1), end + Point(0, -1)
            edges.append((s, end))
        curr = curr + directions[d] * l

    i = 0
    while i < len(edges):
        selected = edges[i]
        j = 0
        new_edges = []
        popped = 0
        while j < len(edges):
            other = edges[j]
            if other == selected:
                j += 1
                continue

            if other[0].y < selected[0].y and other[1].y > selected[1].y:
                x = other[0].x
                other = edges.pop(j)
                new_edges.append((other[0], Point(x, selected[0].y-1)))
                new_edges.append((Point(x, selected[0].y), Point(x, selected[1].y)))
                new_edges.append((Point(x, selected[1].y+1), other[1]))
                popped += 1
            elif other[0].y < selected[0].y <= other[1].y:
                x = other[0].x
                other = edges.pop(j)
                new_edges.append((other[0], Point(x, selected[0].y-1)))
                new_edges.append((Point(x, selected[0].y), other[1]))
                popped += 1
            elif other[1].y > selected[1].y >= other[0].y:
                x = other[0].x
                other = edges.pop(j)
                new_edges.append((other[0], Point(x, selected[1].y)))
                new_edges.append((Point(x, selected[1].y+1), other[1]))
                popped += 1
            else:
                j += 1
        edges += new_edges
        i += 1 - popped

    edges = list(sorted(edges, key=lambda e: (e[0].y, e[1].y, e[0].x)))

    c = 0
    i = 0
    while i < len(edges):
        e0 = edges[i]
        i += 1
        if is_corner[e0]:
            c += e0[1].x - e0[0].x + 1
            continue

        e1 = edges[i]
        i += 1
        while is_corner[e1]:
            e1 = edges[i]
            i += 1

        dy = e0[1].y - e0[0].y + 1
        dx = e1[1].x - e0[0].x + 1
        c += dy * dx
    print(c)


if __name__ == '__main__':
    run(main, parse)
