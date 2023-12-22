from pycp.all import *


def parse(line: str):
    a, b = line.split('~')
    a = Point(*map(int, a.split(',')))
    b = Point(*map(int, b.split(',')))
    return a, b


def overlaps(s0, s1, o0, o1):
    return max(s0.x, o0.x) <= min(s1.x, o1.x) and max(s0.y, o0.y) <= min(s1.y, o1.y)


def fall_to(s0, s1, z):
    dz = z - s0.z
    s0.z += dz
    s1.z += dz


def main(lines: list) -> None:
    sup = [[] for _ in range(len(lines))]
    sb = [set() for _ in range(len(lines))]
    lines = sorted(lines, key=lambda line: line[0].z)
    for index, (s0, s1) in enumerate(lines):
        coll = sorted(lines[:index], key=lambda line: line[1].z)
        for o0, o1 in reversed(coll):
            if overlaps(s0, s1, o0, o1):
                fall_to(s0, s1, o1.z + 1)
                break
        else:
            fall_to(s0, s1, 1)

    for i, (s0, s1) in enumerate(lines):
        for j, (o0, o1) in enumerate(lines):
            if overlaps(s0, s1, o0, o1) and s0.z - 1 == o1.z and j != i:
                sup[j].append(i)
                sb[i].add(j)

    c = 0
    for i in range(len(lines)):
        fell = {i}
        queue = deque([i])
        while len(queue):
            s = queue.popleft()
            for o in sup[s]:
                if len(sb[o].difference(fell)) == 0:
                    fell.add(o)
                    queue.append(o)
        c += len(fell)-1

    print(c)
# 93292

if __name__ == '__main__':
    run(main, parse)
