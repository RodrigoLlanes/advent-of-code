from sys import stdin 


def check(values: list[int]):
    for i, value in enumerate(values):
        for j, other in enumerate(values):
            if i == j:
                continue
            if value % other == 0:
                return value / other


def main(lines: list[str]):
    s = 0
    for line in lines:
        values = list(map(int, line.split()))
        
        s += check(values)
    print(s)


if __name__ == "__main__":
    main(stdin.read().splitlines())

