import re
from copy import copy

from pycp.all import *


def parse(line):
    i = line.index(']')
    l = [e == '#' for e in line[1:i]]
    i2 = line.index('{')
    b = line[i+1:i2].split()
    b = list(map(lambda x: list(map(int, x[1:-1].split(','))), b))
    return l, b


def main(lines):
    s = 0
    for target, buttons in lines:
        heap = Heap([(0, -1, [False] * len(target))])
        best = float('inf')
        hist = {}
        while len(heap):
            length, last, ind = heap.pop()
            if length > best:
                continue
            if tuple(ind) in hist and hist[tuple(ind)] <= length:
                continue
            if ind == target:
                best = length
                continue
            hist[tuple(ind)] = length
            for i, b in enumerate(buttons):
                if i != last:
                    c = copy(ind)
                    for j in b:
                        c[j] = not c[j]
                    heap.push((length+1, i, c))
        s += best
    print(s)


if __name__ == '__main__':
    run(main, parse)
