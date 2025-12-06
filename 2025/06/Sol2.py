from pycp.all import *


def calculate(sublines):
    if all(len(line.strip()) == 0 for line in sublines):
        return 0

    sublines = list(map(str.rstrip, sublines))
    l = max(map(len, sublines))
    sublines = [line + ' ' * (l - len(line)) for line in sublines]
    op = sublines[-1].strip()
    operands = list(zip(*sublines[:-1]))

    if op == '+':
        return sum(int(''.join(v)) for v in operands)
    else:
        return prod(int(''.join(v)) for v in operands)


def main(lines):
    r = 0
    prev = 0
    i = max(line.find(' ', 0) for line in lines)
    while i > 0:
        sublines = [line[prev: i+1] for line in lines]
        r += calculate(sublines)
        prev = i+1
        i = max(line.find(' ', i+1) for line in lines)

    sublines = [line[prev:] for line in lines]
    r += calculate(sublines)

    print(r)


if __name__ == '__main__':
    run(main)
