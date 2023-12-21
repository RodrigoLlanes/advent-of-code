from pycp.all import *


def parse(line: str):
    return line


def evaluate(rule, mat):
    x = mat['x']
    m = mat['m']
    a = mat['a']
    s = mat['s']
    for c, t in rule:
        if eval(c):
            return t


def main(lines: list) -> None:
    rules = defaultdict(list)
    for index, line in enumerate(lines):
        if len(line.strip()) == 0:
            break

        s = line.index('{')
        name = line[:s]
        rs = line.strip()[s+1:-1].split(',')
        for r in rs[:-1]:
            rules[name].append(tuple(r.split(':')))
        rules[name].append(('True', rs[-1]))

    c = 0
    for i in range(index+1, len(lines)):
        mat = {}
        for elem in lines[i][1:-1].split(','):
            k, v = elem.split('=')
            mat[k] = int(v)
        cur = 'in'
        while cur not in ('A', 'R'):
            cur = evaluate(rules[cur], mat)
        if cur == 'A':
            c += sum(mat.values())
    print(c)




if __name__ == '__main__':
    run(main, parse)
