from pycp.all import *


def parse(line):
    src, r = line.split(': ')
    return src, r.split()


def find_n_paths(g, src, dst):
    dependencies = defaultdict(set)
    for k, v in g.items():
        for t in v:
            dependencies[t].add(k)

    remaining = ['out']
    paths = defaultdict(int, {dst: 1})
    visited = set()
    while len(remaining):
        last = None
        for i in range(len(remaining)):
            if len(dependencies[remaining[i]] - visited) == 0:
                last = remaining.pop(i)
                break
        assert last is not None
        if last in visited:
            continue
        visited.add(last)

        for target in g[last]:
            paths[target] += paths[last]
            remaining.append(target)
    return paths[src]


def main(lines):
    g = defaultdict(list)
    for src, r in lines:
        for target in r:
            g[target].append(src)

    print(find_n_paths(g, 'svr', 'fft') * find_n_paths(g, 'fft', 'dac') * find_n_paths(g, 'dac', 'out') +
          find_n_paths(g, 'svr', 'dac') * find_n_paths(g, 'dac', 'fft') * find_n_paths(g, 'fft', 'out'))


if __name__ == '__main__':
    run(main, parse)
