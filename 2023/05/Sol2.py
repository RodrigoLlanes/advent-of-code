from pycp.all import *


def main(lines: list) -> None:
    seeds = list(map(int, lines.pop(0).split(': ')[1].split()))
    seeds = [(seeds[i], seeds[i] + seeds[i+1]-1) for i in range(0, len(seeds), 2)]
    lines.pop(0)
    while len(lines):
        lines.pop(0)
        n = []
        while len(lines) > 0 and len(line := lines.pop(0).strip()) > 0:
            ds, ss, r = map(int, line.split())
            i = 0
            while i < len(seeds):
                ts, te = seeds[i]
                if ss <= ts and te <= (ss+r-1):    # Full
                    seeds.pop(i)
                    n.append((ts - ss + ds, te - ss + ds))
                elif ss <= ts <= (ss+r-1):         # Beginning
                    cut = ss+r-1
                    seeds.pop(i)
                    n.append((ts - ss + ds, cut - ss + ds))
                    seeds.append((cut+1, te))
                elif ss <= te <= (ss+r-1):         # End
                    cut = ss
                    seeds.pop(i)
                    n.append((ds, te - ss + ds))
                    seeds.append((ts, cut-1))
                elif ss > ts and te > (ss+r-1):    # Middle
                    seeds.pop(i)
                    n.append((ds, ds + r - 1))
                    seeds.append((ts, ss-1))
                    seeds.append((ss+r, te))
                else:
                    i += 1
        n += seeds
        seeds = n
    print(min(seeds)[0])


if __name__ == '__main__':
    run(main)
