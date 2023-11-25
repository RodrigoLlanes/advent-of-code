from sys import stdin 


def main(lines: list[str]):
    line = lines[0]
    
    sum = 0
    half = len(line)//2
    for i in range(len(line)):
        if line[i] == line[(i+half) % len(line)]:
            sum += int(line[i])
    print(sum)


if __name__ == "__main__":
    main(stdin.read().splitlines())

