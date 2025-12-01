from collections import Counter

from pycp.all import run


def parse(line: str):
    return int(line[1:]) * (-1 if line[0] == 'L' else 1)


def main(lines: list[list[int]]):
    dial_rotation = 50
    count = 0
    for rotation in lines:
        dial_rotation += rotation
        dial_rotation %= 100
        if dial_rotation == 0:
            count += 1
    print(count)


if __name__ == '__main__':
    run(main, parse)
