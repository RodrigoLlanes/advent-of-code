from ortools.sat.python import cp_model


from pycp.all import *


def parse(line):
    i = line.index(']')
    i2 = line.index('{')
    b = line[i+1:i2].split()
    b = list(map(lambda x: list(map(int, x[1:-1].split(','))), b))
    jolt = list(map(int, line.rstrip()[i2+1:-1].split(',')))
    return jolt, list(sorted(b, key=len))


def solve_eq(target, buttons):
    model = cp_model.CpModel()

    xs = [model.NewIntVar(0, 10 ** 9, f'x{i}') for i in range(len(buttons))]

    for i in range(len(target)):
        involved = [xs[j] for j in range(len(buttons)) if i in buttons[j]]
        model.Add(sum(involved) == target[i])

    model.Minimize(sum(xs))

    solver = cp_model.CpSolver()

    result = solver.Solve(model)

    if result != cp_model.OPTIMAL and result != cp_model.FEASIBLE:
        assert False

    return sum([solver.Value(x) for x in xs])


def main(lines):
    s = 0
    for i, (target, buttons) in enumerate(lines):
        s += solve_eq(target, buttons)
    print(s)


if __name__ == '__main__':
    run(main, parse)
