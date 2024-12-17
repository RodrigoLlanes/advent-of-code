from pycp.all import *


DIRS = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]


def parse(line: str):
    return line


def main(lines: list[list[int]]):
    program = list(map(int, lines[4][len('Program: '):].split(',')))

    prev = 0
    for printed in reversed(program):
        for i in range(9):
            a = prev * 8 + i

            B = a % 8
            B = B ^ 1
            C = a // (2**B)
            B = B ^ 4
            B = B ^ C
            if B % 8 == printed:
                prev = a
                break
    print(prev)


if __name__ == '__main__':
    run(main, parse)
