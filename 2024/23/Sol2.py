from pycp.all import *


def parse(line: str):
    return line.split('-')


def main(lines: list[str]):
    connections = defaultdict(set)
    for a, b in lines:
        connections[a].add(b)
        connections[b].add(a)
    
    visited = set()
    
    heap = Heap()
    for t, keys in connections.items():
        keys = keys.copy()
        keys.add(t)
        heap.push((-len(keys), keys))
    
    while len(heap):
        _, keys = heap.pop()

        if all((keys - connections[k]) == {k} for k in keys):
            print(','.join(sorted(keys)))
            return

        for i in keys:
            new_keys = keys.copy()
            new_keys.remove(i)
            hashed = tuple(sorted(new_keys))
            if hashed in visited:
                continue
            visited.add(hashed)
            heap.push((-len(new_keys), new_keys))


if __name__ == '__main__':
    run(main, parse)
