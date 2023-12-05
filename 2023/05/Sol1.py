from pycp.all import *


def main(lines: list) -> None:
    seeds = list(map(int, lines.pop(0).split(': ')[1].split()))
    lines.pop(0)
    while len(lines):
        lines.pop(0)
        n = []
        while len(lines) > 0 and len(line := lines.pop(0).strip()) > 0:
            ds, ss, r = map(int, line.split())
            i = 0
            while i < len(seeds):
                if ss <= seeds[i] <= (ss+r-1):
                    s = seeds.pop(i)
                    n.append(s - ss + ds)
                else:
                    i += 1
        n += seeds
        seeds = n
    print(min(seeds))


if __name__ == '__main__':
    run(main)
