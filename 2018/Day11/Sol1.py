
def power_level(x, y, serial):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = power // 100
    power = power % 10
    power -= 5
    return power


def grid_power(x, y, p):
    return sum([p[y + dy - 1][x + dx - 1] if (x + dx <= 300) and (y + dy <= 300) else 0 for dx in range(3) for dy in range(3)])


if __name__ == "__main__":
    sn = 7689

    power = [[power_level(x, y, sn) for x in range(1, 301)] for y in range(1, 301)]

    m = max([(x, y) for x in range(1, 301) for y in range(1, 301)], key= lambda p: grid_power(p[0], p[1], power))

    print(f"{m[0]},{m[1]}")




