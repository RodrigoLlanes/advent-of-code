from collections import defaultdict
from copy import deepcopy
from pprint import pprint
import sys


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
            sym_name = portals[(x, y)]
            if sym_name not in res:
                res[sym_name] = dist
            else:
                res[sym_name] = min(dist, res[sym_name])
            # TODO
            pass
        elif sym != ".":
            print("ERROR", actual, sym)
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


def neightbours(x, y):
    res = 0
    for (dx, dy) in [(0, -1), (0, 1), (1,  0), (-1, 0)]:
        sym = vault_map[y + dy][x + dx]
        if (sym == ".") or (sym == "+") or (sym == "@"):
            res += 1
    return res


def print_vault():
    for line in vault_map:
        for char in line:
            print(char, end="")
        print("")


if __name__ == "__main__":
    vault_map = [[" "] + list(line.replace("\n", "")) + [" "] for line in open("input.txt", "r").readlines()]

    vault_map = [[" " for _ in range(len(vault_map[0]))]] + vault_map +  [[" " for _ in range(len(vault_map[0]))]]

    points = {}
    keys = []
    cross_pos = {}
    cross_i = 0

    portals = {}

    for y, line in enumerate(vault_map):
        for x, char in enumerate(line):
            if char.isalpha():
                other = None
                other_pos = None
                pos = None
                for (dx, dy) in [(0, -1), (0, 1), (1,  0), (-1, 0)]:
                    if vault_map[y + dy][x + dx].isalpha():
                        other_pos = (x + dx, y + dy)
                        other = vault_map[y + dy][x + dx]
                    elif vault_map[y + dy][x + dx] == ".":
                        pos = (x + dx, y + dy)
                if pos != None:
                    name = other + char
                    if name in points:
                        name = char + other
                    vault_map[pos[1]][pos[0]] = "@"
                    vault_map[y][x] = "#"
                    vault_map[other_pos[1]][other_pos[0]] = " "
                    points[name] = pos
                    portals[pos] = name
            elif char == "." and neightbours(x, y) > 2:
                vault_map[y][x] = "+"
                points[f"+{cross_i}"] = (x, y)
                cross_pos[(x, y)] = f"+{cross_i}"
                cross_i += 1


    graph = defaultdict(lambda: {})
    for (start, pos) in points.items():
        if len(start) == 2 and start[0].isalpha() and start[1].isalpha() and start[0] != start[1]:
            graph[start][start[1] + start[0]] = 1
        for (end, dist) in get_iterative_path(pos):
            graph[start][end] = dist

    for (pos, sym) in cross_pos.items():
        remove_vertex(graph, sym)
    
    for (pos, sym) in portals.items():
        if sym[0] != sym[1]:
            remove_vertex(graph, sym)

    print(graph["AA"]["ZZ"])