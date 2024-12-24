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
    x = ''.join(str(v) for _, v in sorted(x, reverse=True))
    y = ''.join(str(v) for _, v in sorted(y, reverse=True))
    return int(x, base=2) + int(y, base=2) == int(z, base=2)


def main(lines: list[str]):
    vals, cons_text = '\n'.join(lines).split('\n\n')

    vals = map(lambda x: x.split(': '), vals.split('\n'))
    vals = {a: int(b) for a, b in vals}


    cons = [[a, b, op, res] for a, op, b, _, res in map(lambda x: x.split(), cons_text.split('\n'))]
    
    changes = {
        'z09': 'rkf', 'rkf': 'z09',
        'rrs': 'rvc', 'rvc': 'rrs',
        'z20': 'jgb', 'jgb': 'z20',
        'z24': 'vcg', 'vcg': 'z24',
    }

    inverse = defaultdict(list)
    connections = {}
    for a, b, op, res in cons:
        if res in changes:
            res = changes[res]
        inverse[a].append((b, op, res))
        inverse[b].append((a, op, res))
        connections[a, b, op] = res
        connections[b, a, op] = res
    
    for i in range(1, 45):
        x = f'x{i:02}'
        y = f'y{i:02}'
        z = f'z{i:02}'

        carry_and = connections[x, y, 'AND']
        if len(inverse[carry_and]) != 1 or inverse[carry_and][0][1] != 'OR':
            print('CARRY', i, carry_and, inverse[carry_and])
            continue
        
        add_xor = connections[x, y, 'XOR']
        if len(inverse[add_xor]) != 2:
            print('ADD', i, add_xor, inverse[add_xor])
            continue
        res_xor = [v for v in inverse[add_xor] if v[1] == 'XOR'][0]
        if res_xor[2] != z:
            print('RES', i, res_xor)
    
    connections = defaultdict(list)
    for a, b, op, res in cons:
        if res in changes:
            res = changes[res]
        connections[a].append((b, op, res))
        connections[b].append((a, op, res))
    
    if simulate(vals, connections):
        print(','.join(sorted(changes.keys())))
    else:
        print('Wrong solution')


if __name__ == '__main__':
    run(main, parse)
