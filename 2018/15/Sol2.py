from pycp import Point, Heap
from pycp.point import DIRECTIONS4
from pycp.aoc import data


DIRECTIONS = sorted(DIRECTIONS4)


def parse(lines):
    goblins, elves, ground = {}, {}, set()
    for y, row in enumerate(lines):
        for x, tile in enumerate(row):
            if tile == '#':
                continue

            pos = Point(y, x)    # for sorting is easier if the first component is y
            ground.add(pos)
            if tile == 'G':
                goblins[pos] = 200
            if tile == 'E':
                elves[pos] = 200
    return goblins, elves, ground


def find_path(start, targets, ground, obstacles):
    heap = []
    for step in DIRECTIONS:
        pos = start + step
        if pos in ground and pos not in obstacles:
            heap.append((1, pos, step))

    heap = Heap(heap)
    visited = set()
    best = float('inf')
    solutions = []
    while len(heap):
        d, candidate, step = heap.pop()
        if candidate in visited or d >= best:
            continue
        visited.add(candidate)

        for next_step in DIRECTIONS:
            target = candidate + next_step

            if target in targets:
                # We append candidate instead of target because we want to go to the adjacent tile, not to the enemy
                # position
                if d + 1 < best:
                    best = d + 1
                    solutions = []
                solutions.append((candidate, step))

            if target not in obstacles and target in ground:
                # We append step instead of next_step because we only care of the first character step
                heap.push((d+1, target, step))

    solutions = sorted(solutions, key=lambda s: s[0])    # Is first from top to bottom
    if len(solutions) == 0:
        return Point(0, 0)
    return solutions[0][1]


def test(goblins, elves, ground, attack):
    steps = 0
    while len(elves) > 0 and len(goblins) > 0:
        steps += 1
        positions = sorted(list(goblins.keys()) + list(elves.keys()))  # Is first from top to bottom
        i = 0
        while i < len(positions):
            p = positions[i]
            targets, team, damage = (elves, goblins, 3) if p in goblins else (goblins, elves, attack)
            for d in DIRECTIONS:
                if d + p in targets:
                    break
            else:
                dir = find_path(p, targets, ground, positions)
                pos = p + dir
                positions[i] = pos
                team[pos] = team[p]
                if p != pos:
                    del team[p]
                p = pos

            valid_targets = []
            for d in DIRECTIONS:
                t = d + p
                if t in targets:
                    valid_targets.append((targets[t], t))

            if len(valid_targets) > 0:
                t = sorted(valid_targets)[0][1]
                targets[t] -= damage
                if targets[t] <= 0:
                    if damage == 3:
                        return False
                    del targets[t]
                    j = positions.index(t)
                    positions.pop(j)
                    if j <= i:
                        i -= 1
                if (len(elves) == 0 or len(goblins) == 0) and i < len(positions) - 1:
                    steps -= 1
                    break
            i += 1
    print(steps * (sum(elves.values()) + sum(goblins.values())))
    return True


def main(lines: list[str]) -> None:
    goblins, elves, ground = parse(lines)

    attack = 4
    while not test(goblins.copy(), elves.copy(), ground, attack):
        attack += 1


if __name__ == '__main__':
    main(data())
