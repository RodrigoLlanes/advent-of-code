from pycp.all import *


def main(lines):
    ranges = []
    i = 0
    while len(lines[i].strip()) > 0:
        a, b = map(int, lines[i].split('-'))
        ranges.append([int(a), int(b)])
        i += 1
    i_start = i+1

    ranges = list(sorted(ranges))

    prev_size = None
    while prev_size != len(ranges):
        prev_size = len(ranges)
        i = 1
        while i < len(ranges):
            if ranges[i-1][0] <= ranges[i][0] <= ranges[i-1][1]:
                ranges[i-1][1] = max(ranges[i][1], ranges[i-1][1])
                ranges.pop(i)
            else:
                i += 1

    c = 0
    for n in map(int, lines[i_start:]):
        for a, b in ranges:
            if a <= n <= b:
                c += 1
                break
    print(c)



if __name__ == '__main__':
    run(main)
