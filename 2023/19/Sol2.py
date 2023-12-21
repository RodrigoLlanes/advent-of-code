from copy import deepcopy

from pycp.all import *


def parse(line: str):
    return line


indexes = {'x': 0, 'm': 1, 'a': 2, 's': 3}


def main(lines: list) -> None:
    rules = defaultdict(list)
    for index, line in enumerate(lines):
        if len(line.strip()) == 0:
            break

        s = line.index('{')
        name = line[:s]
        rs = line.strip()[s+1:-1].split(',')
        for r in rs[:-1]:
            rules[name].append(tuple(r.split(':')))
        rules[name].append(('True', rs[-1]))

    heap = [('in', [[1, 4000], [1, 4000], [1, 4000], [1, 4000]])]
    c = 0
    while len(heap):
        cur, ranges = heap.pop()
        if cur == 'A':
            if all(a <= b for a, b in ranges):
                c += prod(b - a + 1 for a, b in ranges)
        elif cur == 'R':
            continue
        else:
            for cond, target in rules[cur]:
                if '>' in cond:
                    i = cond.index('>')
                    index = indexes[cond[:i]]
                    new_ranges = deepcopy(ranges)
                    new_ranges[index][0] = max(ranges[index][0], int(cond[i + 1:]) + 1)
                    heap.append((target, new_ranges))
                    ranges[index][1] = min(ranges[index][1], int(cond[i + 1:]))
                elif '<' in cond:
                    i = cond.index('<')
                    index = indexes[cond[:i]]
                    new_ranges = deepcopy(ranges)
                    new_ranges[index][1] = min(ranges[index][1], int(cond[i + 1:]) - 1)
                    heap.append((target, new_ranges))
                    ranges[index][0] = max(ranges[index][0], int(cond[i + 1:]))
                elif cond == 'True':
                    new_ranges = deepcopy(ranges)
                    heap.append((target, new_ranges))
    print(c)


if __name__ == '__main__':
    run(main, parse)
