from math import sqrt

from pycp.all import *


def parse(line):
    return Point(*list(map(int, line.split(','))))

def distance(a, b):
    p = a - b
    return sqrt(p.x**2 + p.y**2 + p.z**2)


def main(lines):
    distances = []
    points = defaultdict(list)
    groups_index = {}

    for i, a in enumerate(lines):
        groups_index[a] = i
        for b in lines[i+1:]:
            distances.append(distance(a, b))
            points[distance(a, b)].append((a, b))

    distances = list(sorted(distances))

    for d in distances[:1000]:
        a, b = points[d][0]

        if a in groups_index and b in groups_index and groups_index[a] == groups_index[b]:
            continue

        index = groups_index[b]
        for k, v in groups_index.items():
            if v == index:
                groups_index[k] = groups_index[a]

    circuits = [len([k for k, v in groups_index.items() if v == i]) for i in range(len(lines))]
    s = sorted(circuits)
    print(prod(s[-3:]))


if __name__ == '__main__':
    run(main, parse)
