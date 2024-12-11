from math import log10
from pycp.all import run


def parse(line: str):
    return list(map(int, line.split(' ')))


def main(lines: list[list[int]]):
    state = lines[0]

    for _ in range(25):
        new_state = []
        for state in state:
            n = int(log10(state)) + 1 if state > 0 else None
            if state == 0:
                new_state.append(1)
            elif n % 2 == 0:
                a, b = int(state//10**(n/2)), int(state%10**(n/2))
                new_state += [a, b]
            else:
                new_state.append(state * 2024)
        state = new_state

    print(len(state))


if __name__ == '__main__':
    run(main, parse)

