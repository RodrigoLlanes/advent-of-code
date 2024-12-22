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
    values = defaultdict(int)
    for number in lines:
        changes = []
        visited = set()
        for _ in range(2000):
            prev = number % 10
            number = update(number)
            changes.append((number%10)-prev)
            if len(changes) >= 4:
                key = tuple(changes[-4:])
                if key not in visited:
                    visited.add(key)
                    values[key] += number % 10
                    
    print(max(values.values()))


if __name__ == '__main__':
    run(main, parse)
