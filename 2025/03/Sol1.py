from pycp.all import *


def parse(line: str):
    return list(map(int, line))


def main(lines):
    total_sum = 0
    for line in lines:
        first_digit = max(line[:-1])
        index = line.index(first_digit)
        second_digit = max(line[index+1:])
        total_sum += int(f'{first_digit}{second_digit}')
    print(total_sum)


if __name__ == '__main__':
    run(main, parse)
