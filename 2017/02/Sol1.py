from sys import stdin 


def main(lines: list[str]):
    s = 0
    for line in lines:
        values = list(map(int, line.split()))
        s += max(values) - min(values)
    print(s)


if __name__ == "__main__":
    main(stdin.read().splitlines())

