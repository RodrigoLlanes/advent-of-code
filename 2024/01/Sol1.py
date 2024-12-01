from typing import Counter
from pycp.all import run, reduce


def parse(line: str):
    return list(map(int, line.split()))


def main(lines: list[list[int]]):
    left, right = zip(*lines)
    right_count = Counter(right)
    print(sum(abs(a-b) for a, b in zip(sorted(left), sorted(right))))
 

if __name__ == '__main__':
    run(main, parse)

