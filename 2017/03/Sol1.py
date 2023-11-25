from sys import stdin 


def main(lines: list[str]):
    v = int(lines[0])
    pos = [0, 0]
    index = 0
    jump = curr = 1
    jumps = 2
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while v > 1:
        v -= 1
        dir = directions[index]
        pos = [pos[0] + dir[0], pos[1] + dir[1]] 

        jump -= 1
        if jump == 0:
            jump = curr
            index = (index + 1) % 4
            jumps -= 1
        if jumps == 0:
            jumps = 2
            curr += 1 
            jump = curr
    print(abs(pos[0]) + abs(pos[1]))


if __name__ == "__main__":
    main(stdin.read().splitlines())

