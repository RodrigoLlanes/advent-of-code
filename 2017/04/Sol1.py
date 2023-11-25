from sys import stdin 


def main(lines: list[str]):
    count = 0
    for line in lines:
        if len(line.split()) == len(set(line.split())):
            count += 1
    print(count)


if __name__ == "__main__":
    main(stdin.read().splitlines())

