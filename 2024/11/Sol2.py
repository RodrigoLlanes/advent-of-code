from collections import defaultdict
from math import log10
from typing import Counter
from pycp.all import run, reduce, Grid, Point, DIRECTIONS4, cache


def parse(line: str):
    return list(map(int, line.split(' ')))


@cache()
def evolve(state, iters):
    n = int(log10(state)) + 1 if state > 0 else None
    if state == 0:
        new_states = [1]
    elif n % 2 == 0:
        a, b = int(state//10**(n/2)), int(state%10**(n/2))
        new_states = [a, b]
    else:
        new_states = [state * 2024]

    if iters == 0:
        return len(new_states)
    else:
        return sum(evolve(st, iters-1) for st in new_states)


def main(lines: list[list[int]]):
    state = lines[0]
    print(sum(evolve(st, 74) for st in state))


if __name__ == '__main__':
    run(main, parse)
