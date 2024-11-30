from pycp.aoc import data


operators = {
    'addr': lambda a, b, reg: reg[a] + reg[b],
    'addi': lambda a, b, reg: reg[a] + b,

    'mulr': lambda a, b, reg: reg[a] * reg[b],
    'muli': lambda a, b, reg: reg[a] * b,

    'banr': lambda a, b, reg: reg[a] & reg[b],
    'bani': lambda a, b, reg: reg[a] & b,

    'borr': lambda a, b, reg: reg[a] | reg[b],
    'bori': lambda a, b, reg: reg[a] | b,

    'setr': lambda a, b, reg: reg[a],
    'seti': lambda a, b, reg: a,

    'gtir': lambda a, b, reg: int(a > reg[b]),
    'gtri': lambda a, b, reg: int(reg[a] > b),
    'gtrr': lambda a, b, reg: int(reg[a] > reg[b]),

    'eqir': lambda a, b, reg: int(a == reg[b]),
    'eqri': lambda a, b, reg: int(reg[a] == b),
    'eqrr': lambda a, b, reg: int(reg[a] == reg[b]),
}


def parse(lines):
    examples, program = '\n'.join(lines).split('\n\n\n\n')
    examples = [(list(map(int, inp[0][len('Before: ['):-1].split(', '))),
                 list(map(int, inp[1].split())),
                 list(map(int, inp[2][len('After:  ['):-1].split(', '))))
                for inp in map(lambda x: x.split('\n'), examples.split('\n\n'))]
    program = [list(map(int, row.split())) for row in program.split('\n')]
    return examples, program


def main(lines: list[str]) -> None:
    examples, program = parse(lines)

    opcodes = [set(operators.keys()) for _ in range(16)]

    def remove(operation, code):
        if operation in opcodes[code]:
            opcodes[code].remove(operation)
            if len(opcodes[code]) == 1:
                for other in range(16):
                    if other != code:
                        remove(list(opcodes[code])[0], other)

    for old, (op, a, b, c), new in examples:
        for label, f in operators.items():
            if f(a, b, old) != new[c]:
                remove(label, op)

    opcodes = [code for (code,) in opcodes]

    reg = [0] * 4
    for op, a, b, c in program:
        reg[c] = operators[opcodes[op]](a, b, reg)

    print(reg[0])


if __name__ == '__main__':
    main(data())
