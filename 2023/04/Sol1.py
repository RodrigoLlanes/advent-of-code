from pycp.all import *


def parse(line: str):
    return list(map(lambda x: list(map(int, x.split())), line.split(': ')[1].split(' | ')))


def main(lines: list) -> None:
    res = 0
    for a, b in lines:
        points = sum(1 for x in b if x in set(a))
        if points >= 1:
            points = 2 ** (points-1)
        res += points
    print(res)


if __name__ == '__main__':
    run(main, parse)
