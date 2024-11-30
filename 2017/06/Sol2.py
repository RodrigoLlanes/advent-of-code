from pycp.all import *


def parse(line: str):
    return list(map(int, line.split()))


def main(lines: list[list[int]]):
    banks = lines[0]
    states = list()
    i = 0
    while tuple(banks) not in states:
        states.append(tuple(banks))
        i += 1

        index = banks.index(max(banks))

        n = banks[index]
        banks[index] = 0
        for j in range(n):
            banks[(index+1+j) % len(banks)] += 1
    print(i - states.index(tuple(banks)))


if __name__ == '__main__':
    run(main, parse, env_path='../../.env')
