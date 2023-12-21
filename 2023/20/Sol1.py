from pycp.all import *


def parse(line: str):
    a, b = line.split(' -> ')
    return a, b.split(', ')


def step(ops, rules, start):
    counter = {0: 1, 1: 0}
    while len(start):
        p, n, s = start.popleft()

        counter[p] += 1

        if n not in ops:
            continue

        if ops[n][0] == '%':
            if p == 1:
                continue
            else:
                ops[n][1] = (ops[n][1] + 1) % 2
                for t in rules[n]:
                    start.append((ops[n][1], t, n))
        elif ops[n][0] == '&':
            ops[n][1][s] = p
            if all(i == 1 for i in ops[n][1].values()):
                for t in rules[n]:
                    start.append((0, t, n))
            else:
                for t in rules[n]:
                    start.append((1, t, n))
    return counter


def main(lines: list) -> None:
    start = None
    rules = {}
    ops = {}
    for a, b in lines:
        if a == 'broadcaster':
            start = deque([(0, t, a) for t in b])
        else:
            op = a[0]
            name = a[1:]
            if op == '%':
                ops[name] = [op, 0]
            else:
                ops[name] = [op, {}]
            rules[name] = b

    for _, t, s in start:
        if t in ops and ops[t][0] == '&':
            ops[t][1][s] = 0
    for s, ts in rules.items():
        for t in ts:
            if t in ops and ops[t][0] == '&':
                ops[t][1][s] = 0

    counter = {0: 0, 1: 0}
    for _ in range(1000):
        for k, v in step(ops, rules, start.copy()).items():
            counter[k] += v
    print(prod(counter.values()))


if __name__ == '__main__':
    run(main, parse)
