from pycp.all import *


def parse(line: str):
    return line.rstrip().split(',')


def hash(x):
    h = 0
    for i in x:
        h += ord(i)
        h *= 17
        h %= 256
    return h


def main(lines: list) -> None:
    print(sum(map(hash, lines[0])))


if __name__ == '__main__':
    run(main, parse)
