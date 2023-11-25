import numpy as np
from copy import deepcopy
from pprint import pprint


def neighbours(image_id, image, pieces):
    count = {}
    sides = [image[0], image[-1], image[:, 0], image[:, -1]]
    for tile, v in pieces.items():
        if image_id == tile:
            continue
        value = deepcopy(v)
        for flip in range(2):
            for rot in range(4):
                edges = [value[0], value[-1], value[:, 0], value[:, -1]]
                for edge in edges:
                    for side in sides:
                        if all(edge == side):
                            count[tuple(map(tuple, side))] = 1
                value = np.rot90(value)
            value = np.flip(value, 0)
    count = len(count.keys())
    return count


inp = [line.rstrip() for line in open("input.txt")]

data = {}
_id = 0
img = []
for line in inp:
    if "Tile " in line:
        _id = int(line[5:-1])
    elif line == "":
        data[_id] = np.asarray(img)
        img = []
    else:
        img.append(list(line))
data[_id] = np.asarray(img)

res = 1
for k, img in data.items():
    if neighbours(k, img, data) == 2:
        print("DING")
        res *= k
print(res)
