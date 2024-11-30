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
    examples, _ = '\n'.join(lines).split('\n\n\n\n')
    examples = [(list(map(int, inp[0][len('Before: ['):-1].split(', '))),
                 list(map(int, inp[1].split())),
                 list(map(int, inp[2][len('After:  ['):-1].split(', '))))
                for inp in map(lambda x: x.split('\n'), examples.split('\n\n'))]
    return examples


def main(lines: list[str]) -> None:
    examples = parse(lines)

    count = sum(sum(f(a, b, old) == new[c] for f in operators.values()) >= 3
                for old, (op, a, b, c), new
                in examples)

    print(count)


if __name__ == '__main__':
    main(data())
