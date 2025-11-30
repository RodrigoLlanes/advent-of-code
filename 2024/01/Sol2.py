from collections import Counter

from pycp.all import run


def parse(line: str):
    return list(map(int, line.split()))


def main(lines: list[list[int]]):
    left, right = zip(*lines)
    right_count = Counter(right)
    print(sum(a * right_count[a] for a, b in zip(sorted(left), sorted(right))))
 

if __name__ == '__main__':
    run(main, parse)
