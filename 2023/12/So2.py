from pycp.all import *


def parse(line: str):
    a, b = line.split()
    return list('?'.join([a] * 5)), list(map(int, b.split(','))) * 5


mem = {}


def cache(f):
    def w(line, sizes, index, si):
        if (index, si) not in mem:
            mem[index, si] = f(line, sizes, index, si)
        return mem[index, si]

    return w


@cache
def solve(line, sizes, index, si):
    if index >= len(line):
        return 1 if si == len(sizes) else 0
    elif line[index] == '.':
        return solve(line, sizes, index + 1, si)
    elif line[index] == '#':
        if si < len(sizes) and index + sizes[si] - 1 < len(line) and \
                all(s == '#' or s == '?' for s in line[index: index + sizes[si]]) and \
                (index + sizes[si] >= len(line) or line[index + sizes[si]] == '.' or line[index + sizes[si]] == '?'):
            return solve(line, sizes, index + sizes[si] + 1, si + 1)
        return 0
    elif line[index] == '?':
        c = 0
        if si < len(sizes) and index + sizes[si] - 1 < len(line) and \
                all(s == '#' or s == '?' for s in line[index: index + sizes[si]]) and \
                (index + sizes[si] >= len(line) or line[index + sizes[si]] == '.' or line[index + sizes[si]] == '?'):
            c = solve(line, sizes, index + sizes[si] + 1, si + 1)
        return c + solve(line, sizes, index + 1, si)


def main(lines: list) -> None:
    c = 0
    for a, b in lines:
        mem.clear()
        c += solve(a, b, 0, 0)
    print(c)


if __name__ == '__main__':
    run(main, parse)
