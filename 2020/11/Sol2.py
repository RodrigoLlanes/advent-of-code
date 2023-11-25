from copy import deepcopy

inp = [list(line.rstrip()) for line in open("input.txt")]


def get_adjacent(_x, _y, _map):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if j == 0 == i:
                continue
            ix = i
            iy = j
            while 0 <= _x + ix < len(_map[0]) and 0 <= _y + iy < len(_map):
                if _map[_y + iy][_x + ix] != ".":
                    yield _x + ix, _y + iy
                    break
                else:
                    ix += i
                    iy += j


def get_new_state(_x, _y, _map):
    c = sum([1 for i in get_adjacent(_x, _y, _map) if _map[i[1]][i[0]] == "#"])
    if _map[_y][_x] == "L":
        if c == 0:
            return "#"
        else:
            return "L"
    if _map[_y][_x] == "#":
        if c >= 5:
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
