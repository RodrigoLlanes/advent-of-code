from pycp.all import *


def parse(line: str):
    return list(line)


def f(n, a0, a1, a2):
    a = (a2 - a0) // 2 - (a1 - a0)
    b = a1 - a0 - a
    c = a0

    return a * n * n + b * n + c


def main(lines: list) -> None:
    w = len(lines)
    grid = Grid(lines)
    start = None
    for p, s in grid.items():
        if s == 'S':
            start = p
            grid[start] = '.'

    curr = {start}
    fn = []
    for it in range(3):
        n = (26501365 % w) if it == 0 else w
        for _ in range(n):
            n_curr = set()
            for p in curr:
                for d in DIRECTIONS4:
                    pd = p + d
                    pd.x %= w
                    pd.y %= w
                    if grid[pd] == '.':
                        n_curr.add(p + d)
            curr = n_curr
        fn.append(len(curr))
    print(f(26501365//w, *fn))


if __name__ == '__main__':
    run(main, parse)
