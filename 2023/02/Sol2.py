from pycp.aoc import data
from collections import defaultdict
from math import prod


def main(lines: list[str]) -> None:
    possible = 0
    for line in lines:
        _, line = line.split(': ')
        sel = defaultdict(int)
        for combs in line.split('; '):
            for s in combs.split(', '):
                n, color = s.strip().split()
                sel[color] = max(int(n), sel[color])
        possible += prod(sel.values())
    print(possible)


if __name__ == '__main__':
    main(data())
