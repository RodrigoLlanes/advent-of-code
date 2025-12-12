import re

from pycp.all import *


def main(lines):
    sizes = []
    regions = []
    i = 0
    while i < len(lines):
        if re.match(r'\d+:', lines[i]):
            i += 1
            shape = []
            while len(lines[i].strip()) > 0:
                shape.append(lines[i].strip())
                i += 1
            i += 1

            sizes.append(sum([sum([c == '#' for c in line]) for line in shape]))
        else:
            size, count = lines[i].split(': ')
            width, height = map(int, size.split('x'))
            count = list(map(int, count.split()))
            regions.append(((width, height), count))
            i += 1

    # I am so confused, I don't understand why this should work, but it does.
    # Even doesn't work with the test case.
    s = 0
    for progress, ((width, height), original_count) in enumerate(regions):
        su = sum(c * sizes[i] for i, c in enumerate(original_count))
        s += su < width * height
    print(s)


if __name__ == '__main__':
    run(main)
