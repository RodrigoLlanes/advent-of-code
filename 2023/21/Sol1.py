from pycp.all import *


def parse(line: str):
    return list(line)


def main(lines: list) -> None:
    grid = Grid(lines)
    start = None
    for p, s in grid.items():
        if s == 'S':
            start = p
            grid[start] = '.'

    par, inp = {start}, set()

    for i in range(1, 64 + 1):
        if i % 2 == 0:
            curr, targ = inp, par
        else:
            curr, targ = par, inp

        for p in curr:
            for d in DIRECTIONS4:
                pd = p + d
                if 0 <= pd.x < len(lines) and 0 <= pd.y < len(lines[0]) and grid[pd] == '.':
                    targ.add(p+d)
    print(len(par))



if __name__ == '__main__':
    run(main, parse)
