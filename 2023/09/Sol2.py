from pycp.all import *


def parse(line: str):
    return list(map(int, line.split()))


def main(lines: list) -> None:
    res = 0
    for line in lines:
        h = []
        while any(e != 0 for e in line):
            h.append(line[0])
            line = [line[i + 1] - line[i] for i in range(len(line) - 1)]

        n = 0
        for first in reversed(h):
            n = first - n
        res += n
    print(res)


if __name__ == '__main__':
    run(main, parse)
