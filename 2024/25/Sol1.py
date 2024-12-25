from pycp.all import *


def parse(line: str):
    return line


def main(lines: list[str]):
    keys = []
    locks = []
    for schema in '\n'.join(lines).split('\n\n'):
        schema = schema.split('\n')
        if schema[0][0] == '#':
            keys.append([column.index('.') for column in zip(*schema)])
        else:
            locks.append([column.index('#') for column in zip(*schema)])
    
    c = 0
    for lock in locks:
        for key in keys:
            if all(k >= l for k, l in zip(lock, key)):
                c += 1
    print(c)


if __name__ == '__main__':
    run(main, parse)
