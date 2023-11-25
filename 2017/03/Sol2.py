from sys import stdin
from typing import DefaultDict 


def main(lines: list[str]):
    grid = DefaultDict(lambda: 0)
    grid[(0, 0)] = 1
    v = int(lines[0])
    pos = [0, 0]
    index = 0
    jump = curr = 1
    jumps = 2
    diagonals = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while True:
        dir = directions[index]
        pos = [pos[0] + dir[0], pos[1] + dir[1]] 
        result = 0
        for diag in diagonals:
            key = (pos[0] + diag[0], pos[1] + diag[1])
            result += grid[key]
        key = tuple(pos)

        if grid[key] == 0:
            grid[key] = result
        if result > v:
            print(result)
            return

        jump -= 1
        if jump == 0:
            jump = curr
            index = (index + 1) % 4
            jumps -= 1
        if jumps == 0:
            jumps = 2
            curr += 1 
            jump = curr


if __name__ == "__main__":
    main(stdin.read().splitlines())

