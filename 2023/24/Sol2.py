import z3
from pycp.all import *
from z3 import Int, Solver


def parse(line: str):
    a, b = line.split(' @ ')
    return Point(*map(int, a.split(', '))), Point(*map(int, b.split(', ')))


def main(lines: list) -> None:
    solver = Solver()
    dx, dy, dz = Int('dx'), Int('dy'), Int('dz')
    sx, sy, sz = Int('sx'), Int('sy'), Int('sz')

    for i, (p, v) in enumerate(lines):
        t = Int(f't{i}')
        solver.add(t >= 0)
        solver.add(p.x + v.x * t == sx + dx * t)
        solver.add(p.y + v.y * t == sy + dy * t)
        solver.add(p.z + v.z * t == sz + dz * t)

    assert solver.check() == z3.sat
    print(solver.model().eval(sx + sy + sz))


if __name__ == '__main__':
    run(main, parse)
