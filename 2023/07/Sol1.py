from pycp.all import *
from collections import Counter


ORDER = 'A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2'.split(', ')


def parse(line: str):
    a, b = line.split()
    return list(map(ORDER.index, a)), int(b)


def get_score(a):
    common = Counter(a).most_common()
    if len(common) == 1:
        return 0
    elif len(common) == 2 and common[0][1] == 4:
        return 1
    elif len(common) == 2 and common[0][1] == 3:
        return 2
    elif len(common) == 3 and common[0][1] == 3:
        return 3
    elif len(common) == 3 and common[0][1] == 2 and common[1][1] == 2:
        return 4
    elif len(common) >= 3 and common[0][1] == 2:
        return 5
    elif len(common) == 5:
        return 6


def main(lines: list) -> None:
    elements = [(get_score(a), *a, b) for a, b in lines]
    elements = list(reversed(sorted(elements)))
    print(sum([(i+1) * v[-1] for i, v in enumerate(elements)]))


if __name__ == '__main__':
    run(main, parse)
