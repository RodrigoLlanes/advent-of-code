from pycp.all import *


def parse(line: str):
    k, v = line.split(': ')
    a, b = map(lambda x: list(map(int, x.split())), v.split(' | '))
    k = int(k.split()[1])
    return k, (a, b)


def main(lines: list) -> None:
    i = 0
    cards = [k for k, _ in lines]
    points = [sum(1 for x in b if x in set(a)) for _, (a, b) in lines]
    while i < len(cards):
        k = cards[i]
        for j in range(points[k-1]):
            cards.append(k+j+1)
        i += 1
    print(len(cards))


if __name__ == '__main__':
    run(main, parse)
