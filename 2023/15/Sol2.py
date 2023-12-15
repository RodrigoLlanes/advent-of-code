from pycp.all import *


def parse(line: str):
    return line.rstrip().split(',')


def hash(x):
    h = 0
    for i in x:
        h += ord(i)
        h *= 17
        h %= 256
    return h


def main(lines: list) -> None:
    lenses = [[] for _ in range(256)]
    for code in lines[0]:
        op_i = code.index('=') if '=' in code else code.index('-')
        label = code[:op_i]
        box = lenses[hash(label)]
        op = code[op_i]

        if op == '-':
            index = -1
            for i, (l, f) in enumerate(box):
                if l == label:
                    index = i
            if index > -1:
                box.pop(index)
        else:
            focus = int(code[op_i+1:])
            index = -1
            for i, (l, f) in enumerate(box):
                if l == label:
                    index = i
            if index > -1:
                box[index] = (label, focus)
            else:
                box.append((label, focus))

    s = 0
    for i, box in enumerate(lenses):
        for j, (label, foc) in enumerate(box):
            s += (i+1) * (j+1) * foc

    print(s)


if __name__ == '__main__':
    run(main, parse)
