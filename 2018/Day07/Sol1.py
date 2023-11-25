from collections import defaultdict
import re


def solve(data):
    requires = {i: [] for i in set(sum([list(d) for d in data], []))}
    is_required = defaultdict(list)
    for (f, s) in data:
        requires[s].append(f)
        is_required[f].append(s)

    word = ""
    waiting = [k for (k, v) in requires.items() if len(v) == 0]
    while len(waiting) > 0:
        current = min(waiting)
        waiting.remove(current)

        word += current
        for r in is_required[current]:
            requires[r].remove(current)
            if len(requires[r]) == 0:
                waiting.append(r)

    return word


if __name__ == "__main__":
    data = []
    for line in open("input.txt", "r").readlines():
        match = re.match("Step (\w) must be finished before step (\w) can begin\.", line.strip())
        data.append((match.group(1), match.group(2)))
    print(solve(data))



