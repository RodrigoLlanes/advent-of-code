from pycp.all import run, Grid
import re


def parse(line: str):
    return line 

def main(lines: list[list[int]]):
    res = 0

    width = len(lines[0])
    height = len(lines)

    for line in lines:
        matchs = re.findall(r'XMAS', line)
        res += len(matchs)
        matchs = re.findall(r'SAMX', line)
        res += len(matchs)
    
    for line in zip(*lines):
        line = ''.join(line)
        matchs = re.findall(r'XMAS', line)
        res += len(matchs)
        matchs = re.findall(r'SAMX', line)
        res += len(matchs)

    for row, line in enumerate(lines):
        for col in range(len(line)):
            if row <= height - 4 and col <= width -4:
                for i in range(4):
                    if lines[row+i][col+i] != 'XMAS'[i]:
                        break
                else:
                    res += 1
            
            if row <= height - 4 and col <= width -4:
                for i in range(4):
                    if lines[row+i][col+i] != 'SAMX'[i]:
                        break
                else:
                    res += 1
            
            if row <= height-4 and col >= 3:
                for i in range(4):
                    if lines[row+i][col-i] != 'XMAS'[i]:
                        break
                else:
                    res += 1
            
            if row <= height-4 and col >= 3:
                for i in range(4):
                    if lines[row+i][col-i] != 'SAMX'[i]:
                        break
                else:
                    res += 1

    print(res)


if __name__ == '__main__':
    run(main, parse)

