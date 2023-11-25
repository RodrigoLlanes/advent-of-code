from collections import defaultdict
from copy import deepcopy
from pprint import pprint
import sys


def memoize(f):
    mem = {}
    def helper(graph, keys, start):
        dir = (tuple(sorted(keys)), tuple(sorted(start)))
        if dir not in mem:
            mem[dir] = f(graph, keys, start)
        return mem[dir]
    return helper


def get_paths(prev, actual, ignore="+"):
    sym = vault_map[actual[1]][actual[0]]
    if sym == "#":
        return []
    elif sym != "." and sym != ignore:
        return [(sym, 0)]
    else:
        options = [(actual[0] + x, actual[1] + y) for (x, y) in [(0, -1), (0, 1), (1,  0), (-1, 0)] if ((actual[0] + x, actual[1] + y) != prev)]
        res = {}
        for (x, y) in options:
            for (rsym, dist) in get_paths(actual, (x, y)):
                if rsym not in res:
                    res[rsym] = dist + 1
                else:
                    res[rsym] = min(dist + 1, res[rsym])
        return list(res.items())


def get_iterative_path(actual):   
    mem = defaultdict(lambda: [])
    next = [((actual[0] + x, actual[1] + y), actual, 1) for (x, y) in [(0, -1), (0, 1), (1,  0), (-1, 0)]]
    res = {}
    while len(next) > 0:
        (x, y), prev, dist = next.pop()
        sym = vault_map[y][x]
        if sym == "#":
            continue
        elif sym == "+":
            sym_name = cross_pos[(x, y)]
            if sym_name not in res:
                res[sym_name] = dist
            else:
                res[sym_name] = min(dist, res[sym_name])
        elif sym == "@":
            sym_name = bot_pos[(x, y)]
            if sym_name not in res:
                res[sym_name] = dist
            else:
                res[sym_name] = min(dist, res[sym_name])
        elif sym != ".":
            if sym not in res:
                res[sym] = dist
            else:
                res[sym] = min(dist, res[sym])
        else:
            next += [((x + dx, y + dy), (x, y), dist + 1) for (dx, dy) in [(0, -1), (0, 1), (1,  0), (-1, 0)] if (x + dx, y + dy) != prev]
    
    return list(res.items())


def remove_vertex(graph, vertex):
    edges = graph[vertex].items()
    for (a, dist_a) in edges:
        del graph[a][vertex]
        for (b, dist_b) in edges:
            if a != b:
                if b not in graph[a]:
                    graph[a][b] = dist_a + dist_b
                else:
                    graph[a][b] = min(graph[a][b], dist_a + dist_b)
    del graph[vertex]


@memoize
def solve(graph, keys, starters):
    res = []

    graph = deepcopy(graph)
    nkeys = deepcopy(keys)
    
    for start in starters:
        if "@" not in start:
            remove_vertex(graph, start.upper())
            if start in nkeys:
                nkeys.remove(start)
            if len(nkeys) == 0:
                return 0

    for start in starters:
        ngraph = deepcopy(graph)

        edges = deepcopy(list(ngraph[start].items()))
        remove_vertex(ngraph, start)

        for (sym, dist) in edges:
            if sym.islower():
                nstarters = deepcopy(starters)
                nstarters.remove(start)
                nstarters.append(sym)
                r = solve(ngraph, nkeys, nstarters)
                if r >= 0:
                    res.append(dist + r)
    return min(res) if len(res) > 0 else -1


if __name__ == "__main__":
    vault_map = [list(line.strip()) for line in open("input2.txt", "r").readlines()]

    points = {}
    keys = []

    cross_pos = {}
    cross_i = 0

    bot_pos = {}
    bot_i = 0

    for y, line in enumerate(vault_map):
        for x, char in enumerate(line):
            if char == "@":
                points[f"@{bot_i}"] = (x, y)
                bot_pos[(x, y)] = f"@{bot_i}"
                bot_i += 1
            elif char.isalpha():
                points[char] = (x, y)
                if char.islower():
                    keys.append(char)
            elif char == "." and sum([1 for (dx, dy) in [(0, -1), (0, 1), (1,  0), (-1, 0)] if vault_map[y + dy][x + dx] == "."]) > 2:
                vault_map[y][x] = "+"
                points[f"+{cross_i}"] = (x, y)
                cross_pos[(x, y)] = f"+{cross_i}"
                cross_i += 1
    
    graph = defaultdict(lambda: {})
    for (start, pos) in points.items():
        for (end, dist) in get_iterative_path(pos):
            graph[start][end] = dist
    
    for (pos, sym) in cross_pos.items():
        remove_vertex(graph, sym)

    print(solve(graph, keys, [f"@{i}" for i in range(bot_i)]))