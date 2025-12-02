from collections import Counter

from pycp.all import run


def parse(line: str):
    return map(lambda x: map(int, x.split('-')), line.split(','))


def main(lines):
    ids = set()
    for a, b in lines[0]:
        for v in range(a, b+1):
            s = str(v)
            for i in range(1, len(s)//2+1):
                m = len(s)//i
                if s[:i]*m == s:
                    ids.add(v)
    print(sum(ids))


if __name__ == '__main__':
    run(main, parse)
