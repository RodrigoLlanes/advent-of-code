import re

from pycp.all import *
from sympy import symbols, Eq, solve


def parse(line: str):
    return Point(*map(int, re.findall(r'(\d+)', line)))


def main(lines: list[list[int]]):
    res = 0
    for i in range(0, len(lines), 4):
        a, b, p = lines[i:i+3]

        a_coeff, b_coeff = symbols('da db', integer=True)
        solution = solve([
            Eq(a_coeff * a[0] + b_coeff * b[0], p[0] + 10000000000000),
            Eq(a_coeff * a[1] + b_coeff * b[1], p[1] + 10000000000000)
        ], (a_coeff, b_coeff))
        if solution:
            res += solution[a_coeff] * 3 + solution[b_coeff]

    print(res)


if __name__ == '__main__':
    run(main, parse)
