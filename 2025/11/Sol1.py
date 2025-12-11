from pycp.all import *


def parse(line):
    src, r = line.split(': ')
    return src, r.split()


def main(lines):
    g = {}
    for src, r in lines:
        g[src] = r

    c = 0
    heap = Heap([(0, 'you')])
    while len(heap):
        length, last = heap.pop()
        if last == 'out':
            c += 1
            continue

        for i, b in enumerate(g[last]):
            heap.push((length+1, b))
    print(c)


if __name__ == '__main__':
    run(main, parse)
