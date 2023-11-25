from sys import stdin 


def main(lines: list[str]):
    offsets = list(map(int, lines))
    pointer = 0
    steps = 0
    while pointer >= 0 and pointer < len(offsets):
        steps += 1
        jump = offsets[pointer]
        offsets[pointer] += 1 if jump < 3 else -1
        pointer += jump
    print(steps)


if __name__ == "__main__":
    main(stdin.read().splitlines())

