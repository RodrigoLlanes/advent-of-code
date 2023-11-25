from copy import deepcopy

inp = [list(line.rstrip()) for line in open("input.txt")]


def get_adjacent(_x, _y):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == 0 == i:
                continue
            yield _x + i, _y + j


def get_new_state(_x, _y, _map):
    if _map[_y][_x] == "L":
        c = sum([1 for i in get_adjacent(_x, _y) if
                 0 <= i[0] < len(_map[0]) and 0 <= i[1] < len(_map) and _map[i[1]][i[0]] == "#"])
        if c == 0:
            return "#"
        else:
            return "L"
    if _map[_y][_x] == "#":
        c = sum([1 for i in get_adjacent(_x, _y) if
                 0 <= i[0] < len(_map[0]) and 0 <= i[1] < len(_map) and _map[i[1]][i[0]] == "#"])
        if c >= 4:
            return "L"
        else:
            return "#"
    else:
        return "."


prev = [["!" for i in range(len(inp[0]))] for j in range(len(inp))]

while prev != inp:
    new = deepcopy(inp)
    for y in range(len(inp)):
        for x in range(len(inp[y])):
            new_value = get_new_state(x, y, new)
            inp[y][x] = new_value
    prev = new

print(sum([sum([1 for char in line if char == "#"]) for line in inp]))

