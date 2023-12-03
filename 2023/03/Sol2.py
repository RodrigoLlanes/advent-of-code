from pycp.all import *
from pycp.structures.point import DIRECTIONS8


def main(lines: list[str]) -> None:
    res = 0
    for i, line in enumerate(lines):
        for j, sym in enumerate(line):
            if sym == '*':
                p = Point(i, j)
                nums = []
                visited = set()
                for direction in DIRECTIONS8:
                    d = direction + p
                    if tuple(d) in visited or not lines[d.x][d.y].isdigit():
                        continue
                    while d.y > 0 and lines[d.x][d.y-1].isdigit():
                        d.y -= 1
                    n = ''
                    while d.y < len(lines[d.x]) and lines[d.x][d.y].isdigit():
                        visited.add(tuple(d))
                        n += lines[d.x][d.y]
                        d.y += 1
                    nums.append(int(n))
                if len(nums) == 2:
                    res += prod(nums)
    print(res)


if __name__ == '__main__':
    run(main)
