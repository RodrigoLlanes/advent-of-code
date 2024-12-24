import itertools
from pycp.all import *
from copy import deepcopy


def parse(line: str):
    return line


def simulate(vals, connections):
    q = list(vals.keys())
    while len(q):
        a = q.pop()
        for b, op, res in connections[a]:
            if res not in vals and b in vals:
                if op == 'AND':
                    vals[res] = vals[a] & vals[b]
                elif op == 'OR':
                    vals[res] = vals[a] | vals[b]
                elif op == 'XOR':
                    vals[res] = vals[a] ^ vals[b]
                q.append(res)
    z = []
    x = []
    y = []
    for k, v in vals.items():
        if k.startswith('z'):
            z.append((k, v))
        elif k.startswith('x'):
            x.append((k, v))
        elif k.startswith('y'):
            y.append((k, v))
    z = ''.join(str(v) for _, v in sorted(z, reverse=True))
    print(int(z, base=2))


def main(lines: list[str]):
    vals, cons_text = '\n'.join(lines).split('\n\n')

    vals = map(lambda x: x.split(': '), vals.split('\n'))
    vals = {a: int(b) for a, b in vals}


    cons = [[a, b, op, res] for a, op, b, _, res in map(lambda x: x.split(), cons_text.split('\n'))]
    
    connections = defaultdict(list)
    for a, b, op, res in cons:
        connections[a].append((b, op, res))
        connections[b].append((a, op, res))
        
    q = list(vals.keys())
    while len(q):
        a = q.pop()
        for b, op, res in connections[a]:
            if res not in vals and b in vals:
                if op == 'AND':
                    vals[res] = vals[a] & vals[b]
                elif op == 'OR':
                    vals[res] = vals[a] | vals[b]
                elif op == 'XOR':
                    vals[res] = vals[a] ^ vals[b]
                q.append(res)
    z = []
    x = []
    y = []
    for k, v in vals.items():
        if k.startswith('z'):
            z.append((k, v))
        elif k.startswith('x'):
            x.append((k, v))
        elif k.startswith('y'):
            y.append((k, v))
    z = ''.join(str(v) for _, v in sorted(z, reverse=True))
    print(int(z, base=2))


if __name__ == '__main__':
    run(main, parse)
