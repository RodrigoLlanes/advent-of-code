from pycp.all import *


def parse(line: str):
    return line


def main(lines: list[str]):
    patterns = set(lines[0].split(', '))
    targets = lines[2:]

    @cache()
    def combinations(target):
        if len(target) == 0:
            return 1

        return sum(combinations(target[len(pattern):]) for pattern in patterns if target.startswith(pattern))

    res = 0
    for i, target in enumerate(targets):
        res += combinations(target)
    print(res)


if __name__ == '__main__':
    run(main, parse)

