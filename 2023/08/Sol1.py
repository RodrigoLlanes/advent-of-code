from pycp.all import *


def main(lines: list) -> None:
    insts = lines[0]
    m = {}
    for line in lines[2:]:
        start, dests = line.split(' = ')
        l, r = dests[1:-1].split(', ')
        m[start] = {'L': l, 'R': r}

    current = 'AAA'
    counter = 0
    while current != 'ZZZ':
        inst = insts[counter % len(insts)]
        current = m[current][inst]
        counter += 1
    print(counter)


if __name__ == '__main__':
    run(main)
