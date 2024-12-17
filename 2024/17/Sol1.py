from pycp.all import *


DIRS = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]


def parse(line: str):
    return line


def main(lines: list[list[int]]):
    registers = {
        4: int(lines[0][12:]),
        5: int(lines[1][12:]),
        6: int(lines[2][12:])
    }

    program = list(map(int, lines[4][len('Program: '):].split(',')))

    def combo(op):
        if op not in registers:
            return op
        return registers[op]

    out = []
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        match opcode:
            case 0:
                registers[4] = registers[4] // (2 ** combo(operand))
            case 1:
                registers[5] = registers[5] ^ operand
            case 2:
                registers[5] = combo(operand) % 8
            case 3:
                if registers[4] != 0:
                    i = operand
                    continue
            case 4:
                registers[5] = registers[5] ^ registers[6]
            case 5:
                out.append(str(combo(operand) % 8))
            case 6:
                registers[5] = registers[4] // (2 ** combo(operand))
            case 7:
                registers[6] = registers[4] // (2 ** combo(operand))
        i += 2
    print(','.join(out))


if __name__ == '__main__':
    run(main, parse)
