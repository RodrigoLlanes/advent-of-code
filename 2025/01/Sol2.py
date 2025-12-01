from collections import Counter

from pycp.all import run


def parse(line: str):
    return int(line[1:]) * (-1 if line[0] == 'L' else 1)


def decompose(rotation: float):
    abs_rotation = abs(rotation)
    decomposition = [99] * (abs_rotation // 99) + ([(abs_rotation % 99)] if abs_rotation % 99 != 0 else [])
    if rotation < 0:
        return [-r for r in decomposition]
    return decomposition


def main(lines: list[list[int]]):
    dial_rotation = 50
    count = 0
    for full_rotation in lines:
        for rotation in decompose(full_rotation):
            original = dial_rotation
            dial_rotation += rotation
            before_mod = dial_rotation
            dial_rotation %= 100
            if before_mod != dial_rotation and original != 0:
                count += 1
            elif dial_rotation == 0:
                count += 1
    print(count)


if __name__ == '__main__':
    run(main, parse)
