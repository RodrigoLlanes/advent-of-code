
def power_level(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = power // 100
    power = power % 10
    power -= 5
    return power


def grid_power(x, y, s, p):
    if s == 0:
        return 0
    top = sum([p[y - 1][x + dx - 1] if (x + dx <= 300) and (y <= 300) else 0 for dx in range(s)])
    left = sum([p[y + dy - 1][x - 1] if (x <= 300) and (y + dy <= 300) else 0 for dy in range(s)])
    return top + left + grid_power(x + 1, y + 1, s - 1, p)


# https://www.reddit.com/r/adventofcode/comments/a53r6i/2018_day_11_solutions/
# Based on sophiebits solution

if __name__ == "__main__":
    sn = 7689

    power = [[power_level(x, y, sn) for x in range(1, 301)] for y in range(1, 301)]

    acc = {}
    for y in range(1, 301):
        for x in range(1, 301):
            acc[(x, y)] = acc.get((x - 1, y), 0) + acc.get((x, y - 1), 0) - acc.get((x - 1, y - 1), 0) + power[y-1][x-1]

    scores = {}
    for y in range(1, 301):
        for x in range(1, 301):
            for s in range(1, max(x, y)+1):
                scores[(x, y, s)] = acc[(x, y)] - acc.get((x, y-s), 0) - acc.get((x-s, y), 0) + acc.get((x-s, y-s), 0)

    m = max(scores.items(), key=lambda x: x[1])[0]

    print(f"{m[0]-m[2]+1},{m[1]-m[2]+1},{m[2]}")
