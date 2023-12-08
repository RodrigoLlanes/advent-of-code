from pycp.all import *
from math import lcm


def main(lines: list) -> None:
    insts = lines[0]
    m = {}
    currents = []
    for line in lines[2:]:
        start, dests = line.split(' = ')
        if start[-1] == 'A':
            currents.append(start)
        l, r = dests[1:-1].split(', ')
        m[start] = {'L': l, 'R': r}

    counters = [0] * len(currents)
    for i in range(len(currents)):
        while currents[i][-1] != 'Z':
            inst = insts[counters[i] % len(insts)]
            currents[i] = m[currents[i]][inst]
            counters[i] += 1

    print(lcm(*counters))


if __name__ == '__main__':
    run(main)
