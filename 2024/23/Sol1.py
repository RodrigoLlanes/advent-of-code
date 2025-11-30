from pycp.all import *


def parse(line: str):
    return line.split('-')


def main(lines: list[str]):
    connections = defaultdict(set)
    for a, b in lines:
        connections[a].add(b)
        connections[b].add(a)
    
    res = set()
    for t, con in connections.items():
        if not t.startswith('t'):
            continue
            
        def test(t, con):
            con = list(con)
            subnets = set()
            for i, a in enumerate(con):
                for b in con[i+1:]:
                    if b in connections[a] and a in connections[b]:
                        subnets.add(tuple(sorted([a, b, t])))
            return subnets
        for n in test(t, con):
            res.add(n)
    print(len(res))


if __name__ == '__main__':
    run(main, parse)
