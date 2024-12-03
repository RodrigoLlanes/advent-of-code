from pycp.all import run
import re


def parse(line: str):
    return re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', line)


def main(lines: list[list[int]]):
    res = 0
    do = True
    for line in lines:
        for inst in line:
            if inst[1] != '':
                do = True
            elif inst[2] != '':
                do = False
            elif do:
                a, b = map(int, re.findall(r'\d+', inst[0]))
                res += a * b
    print(res)


if __name__ == '__main__':
    run(main, parse)

