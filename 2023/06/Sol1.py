from pycp.all import *


def parse(line: str):
    return list(map(int, line.split(':')[1].strip().split()))


def main(lines: list) -> None:
    result = 1
    for t, d in zip(*lines):
        opts = 0
        for hold in range(t):
            if (t - hold) * hold > d:
                opts += 1
        result *= opts
    print(result)


if __name__ == '__main__':
    run(main, parse)
