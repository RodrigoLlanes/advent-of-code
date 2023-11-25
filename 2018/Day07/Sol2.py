from collections import defaultdict
import re


def solve(data, n_workers):
    requires = {i: [] for i in set(sum([list(d) for d in data], []))}
    is_required = defaultdict(list)
    for (f, s) in data:
        requires[s].append(f)
        is_required[f].append(s)

    workers = [[0, None] for _ in range(n_workers)]
    word = ""
    waiting = [k for (k, v) in requires.items() if len(v) == 0]
    t = -1
    while len(waiting) > 0 or any(w[0] > 0 for w in workers):
        for worker in workers:
            if worker[0] > 0:
                worker[0] -= 1
                if worker[0] == 0:
                    word += worker[1]
                    for r in is_required[worker[1]]:
                        requires[r].remove(worker[1])
                        if len(requires[r]) == 0:
                            waiting.append(r)
                    worker[1] = None
            if worker[0] == 0 and len(waiting) > 0:
                current = min(waiting)
                waiting.remove(current)
                worker[0] = 60 + ord(current) - ord("A") + 1
                worker[1] = current
        t += 1

    return t


if __name__ == "__main__":
    data = []
    for line in open("input.txt", "r").readlines():
        match = re.match("Step (\w) must be finished before step (\w) can begin\.", line.strip())
        data.append((match.group(1), match.group(2)))
    print(solve(data, 5))



