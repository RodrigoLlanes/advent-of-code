from pycp.all import *


sign = lambda x: -1 if x < 0 else 1



def parse(line: str):
    return int(line)


def update(number):
    number ^= (number * 64)
    number %= 16777216

    number ^= number // 32
    number %= 16777216

    number ^= number * 2048
    number %= 16777216
    return number


def main(lines: list[str]):
    res = 0
    for number in lines:
        for _ in range(2000):
            number = update(number)
        res += number
                    
    print(res)


if __name__ == '__main__':
    run(main, parse)
