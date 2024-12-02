from pycp.all import run
from itertools import pairwise


def parse(line: str):
    return list(map(int, line.split()))


def main(lines: list[list[int]]):
    res = 0
    for line in lines:
        for i in range(len(line)):
            entry = line.copy()
            entry.pop(i)
            if entry == list(sorted(entry)) or entry == list(reversed(sorted(entry))):
                if all(3 >= abs(a - b) >= 1 for a, b in pairwise(entry)):
                    res += 1
                    break
    print(res)


if __name__ == '__main__':
    run(main, parse)

