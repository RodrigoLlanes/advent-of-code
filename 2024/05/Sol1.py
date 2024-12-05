from pycp.all import run, Grid
import re
from collections import defaultdict


def parse(line: str):
    return line 

def main(lines: list[list[int]]):
    a, b = '\n'.join(lines).split('\n\n')
    rules = defaultdict(lambda: [set(),set()])
    for line in a.split('\n'):
        first, second = map(int, line.split('|'))
        rules[first][1].add(second)
        rules[second][0].add(first)

    res = 0
    for line in b.split('\n'):
        order = list(map(int, line.split(',')))
        for i in range(len(order)):
            if any(elem in rules[order[i]][1] for elem in order[:i]):
                break
            if any(elem in rules[order[i]][0] for elem in order[i+1:]):
                break
        else:
            res += order[len(order)//2]

    print(res)


if __name__ == '__main__':
    run(main, parse)

