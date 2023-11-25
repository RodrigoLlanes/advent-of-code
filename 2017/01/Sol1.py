from sys import stdin 


def main(lines: list[str]):
    line = lines[0] + lines[0][0]
    sum = 0

    for i in range(len(line)-1):
        if line[i] == line[i+1]:
            sum += int(line[i])
    print(sum)


if __name__ == "__main__":
    main(stdin.read().splitlines())

