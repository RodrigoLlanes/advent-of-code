from pycp.all import *


def parse(line: str):
    return list(line)


def main(lines: list) -> None:
    for i in range(0, len(lines)):
        for j, s in enumerate(lines[i]):
            ind = i
            while ind > 0 and s == 'O' and lines[ind-1][j] == '.':
                lines[ind][j] = '.'
                lines[ind-1][j] = 'O'
                ind -= 1

    c = 0
    for i in range(0, len(lines)):
        for j, s in enumerate(lines[i]):
            if s == 'O':
                c += len(lines) - i

    print(c)


if __name__ == '__main__':
    run(main, parse)
