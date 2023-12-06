from pycp.all import *


def parse(line: str):
    return int(''.join(line.split(':')[1].strip().split()))


def main(lines: list) -> None:
    t, d = lines
    opts = 0
    for hold in range(t):
        if (t - hold) * hold > d:
            opts += 1
    print(opts)


if __name__ == '__main__':
    run(main, parse)
