from pycp.all import *


def parse(line: str):
    return list(line)


def cycle(lines):
    for _ in range(4):
        for i in range(0, len(lines)):
            for j, s in enumerate(lines[i]):
                ind = i
                while ind > 0 and s == 'O' and lines[ind-1][j] == '.':
                    lines[ind][j] = '.'
                    lines[ind-1][j] = 'O'
                    ind -= 1
        lines = list(map(list, zip(*reversed(lines))))    # Rotate 90 degrees to the right
    return lines


def tup(lines):
    return tuple(tuple(line) for line in lines)


def main(lines: list) -> None:
    N = 1000000000

    hist = []
    lines = cycle(lines)
    while tup(lines) not in hist:
        hist.append(tup(lines))
        lines = cycle(lines)

    index = hist.index(tup(lines))
    n = len(hist) - index
    steps = len(hist) + 1

    steps += ((N - steps) // n) * n
    lines = hist[N - steps + index]

    c = 0
    for i in range(0, len(lines)):
        for j, s in enumerate(lines[i]):
            if s == 'O':
                c += len(lines) - i
    print(c)


if __name__ == '__main__':
    run(main, parse)
