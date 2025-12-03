from pycp.all import *


def parse(line: str):
    return list(map(int, line))


def main(lines):
    total_sum = 0
    for line in lines:
        digits = []
        prev_index = -1
        for i in range(1, 13):
            sub_list = line[prev_index+1: len(line) - 12 + i]
            digit = max(sub_list)
            prev_index = sub_list.index(digit) + prev_index + 1
            digits.append(digit)
        total_sum += int(''.join(map(str, digits)))
    print(total_sum)


if __name__ == '__main__':
    run(main, parse)
