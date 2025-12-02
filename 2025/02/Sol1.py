from collections import Counter

from pycp.all import run


def parse(line: str):
    return map(lambda x: map(int, x.split('-')), line.split(','))


def main(lines):
    c = 0
    for a, b in lines[0]:
        for v in range(a, b+1):
            s = str(v)
            if len(s) % 2 != 0:
                continue
            if s[0:len(s)//2] == s[len(s)//2:]:
                c += v
    print(c)


if __name__ == '__main__':
    run(main, parse)
