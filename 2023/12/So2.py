from pycp.all import *


def parse(line: str):
    a, b = line.split()
    return list('?'.join([a] * 5)), list(map(int, b.split(','))) * 5


def cache(f):
    mem = {}

    def w(line, sizes, index, si, fun):
        if (index, si) not in mem:
            mem[index, si] = f(line, sizes, index, si, fun)
        return mem[index, si]

    return w


def solve(line, sizes, index, si, rec):
    if index >= len(line):
        return 1 if si == len(sizes) else 0
    elif line[index] == '.':
        return rec(line, sizes, index + 1, si, rec)
    elif line[index] == '#':
        if si < len(sizes) and index + sizes[si] - 1 < len(line) and \
                all(s == '#' or s == '?' for s in line[index: index + sizes[si]]) and \
                (index + sizes[si] >= len(line) or line[index + sizes[si]] == '.' or line[index + sizes[si]] == '?'):
            return rec(line, sizes, index + sizes[si] + 1, si + 1, rec)
        return 0
    elif line[index] == '?':
        c = 0
        if si < len(sizes) and index + sizes[si] - 1 < len(line) and \
                all(s == '#' or s == '?' for s in line[index: index + sizes[si]]) and \
                (index + sizes[si] >= len(line) or line[index + sizes[si]] == '.' or line[index + sizes[si]] == '?'):
            c = rec(line, sizes, index + sizes[si] + 1, si + 1, rec)
        return c + rec(line, sizes, index + 1, si, rec)


def main(lines: list) -> None:
    c = 0
    for a, b in lines:
        sol = cache(solve)
        c += sol(a, b, 0, 0, sol)
    print(c)


if __name__ == '__main__':
    run(main, parse)
