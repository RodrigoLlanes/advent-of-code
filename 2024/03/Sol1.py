from pycp.all import run
import re


def parse(line: str):
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)


def main(lines: list[list[int]]):
    res = 0
    for line in lines:
        for inst in line:
            a, b = map(int, re.findall(r'\d+', inst))
            res += a * b
    print(res)


if __name__ == '__main__':
    run(main, parse)

