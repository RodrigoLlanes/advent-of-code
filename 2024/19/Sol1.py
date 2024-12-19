from pycp.all import *


def parse(line: str):
    return line


def main(lines: list[str]):
    patterns = set(lines[0].split(', '))
    targets = lines[2:]

    @cache()
    def possible(target):
        if len(target) == 0:
            return True

        return any(possible(target[len(pattern):]) for pattern in patterns if target.startswith(pattern))

    res = 0
    for i, target in enumerate(targets):
        res += possible(target)
    print(res)


if __name__ == '__main__':
    run(main, parse)

