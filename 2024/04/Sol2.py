from pycp.all import run, Grid
import re


def parse(line: str):
    return line 

def main(lines: list[list[int]]):
    res = 0

    width = len(lines[0])
    height = len(lines)

    for row, line in enumerate(lines):
        for col, item in enumerate(line):
            if item in ('M', 'S'):
                if row <= height - 3 and col <= width -3:
                    if lines[row+1][col+1] != 'A':
                        continue
                    if lines[row+2][col+2] not in ('M', 'S') or lines[row+2][col+2] == lines[row][col]:
                        continue
                    if lines[row+2][col] not in ('M', 'S') or lines[row][col+2] not in ('M', 'S') or lines[row+2][col] == lines[row][col+2]:
                        continue
                    res += 1
    print(res)


if __name__ == '__main__':
    run(main, parse)

