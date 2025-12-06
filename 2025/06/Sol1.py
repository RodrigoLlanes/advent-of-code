from pycp.all import *


def parse(line):
    return line.split()


def calculate(lines):
    op = lines[-1].strip()
    operands = map(int, lines[:-1])

    if op == '+':
        return sum(operands)
    else:
        return prod(operands)


def main(lines):
    lines = zip(*lines)

    r = 0
    for line in lines:
        r += calculate(line)

    print(r)


if __name__ == '__main__':
    run(main, parse)
