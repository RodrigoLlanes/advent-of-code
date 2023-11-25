import numpy as np
from copy import deepcopy


def key4value(value, d):
    for _k, v in d.items():
        if v == value:
            return _k


def neighbour_positions(x, y, d):
    yield x, y-1, d[1]
    yield x, y+1, d[-1]
    yield x+1, y, d[:, -1]
    yield x-1, y, d[:, 0]


def neighbours(image_id, image, pieces):
    count = {}
    sides = {(-1, 0): image[0], (1, 0): image[-1], (0, -1): image[:, 0], (0, 1): image[:, -1]}
    for tile, v in pieces.items():
        if image_id == tile:
            continue
        value = deepcopy(v)
        for flip in range(2):
            for rot in range(4):
                edges = [value[0], value[-1], value[:, 0], value[:, -1]]
                for edge in edges:
                    for side_name, side in sides.items():
                        if all(edge == side):
                            count[tile] = value
                value = np.rot90(value)
            value = np.flip(value, 0)
    return count


def apply_filter(_img):
    filt = [line.rstrip() for line in open("monster.txt")]
    for _y in range(0, len(_img) - len(filt) - 1):
        for _x in range(0, len(_img[0]) - len(filt[0]) - 1):
            for i in range(len(filt)):
                for j in range(len(filt[i])):
                    if filt[i][j] == "#" and \
                            (_img[_y + i][_x + j] != "#" and
                             _img[_y + i][_x + j] != "X"):
                        break
                else:
                    continue
                break
            else:
                for i in range(len(filt)):
                    for j in range(len(filt[i])):
                        if filt[i][j] == "#":
                            _img[_y + i][_x + j] = "X"


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


image = {}
img_k = {}
img_v = {}
top_left = None
for k, img in data.items():
    image[k] = neighbours(k, img, data)
    if len(image[k]) == 2:
        top_left = k

first, second = list(image[top_left].keys())
queue = {}


def top_left_calc():
    tl_v = deepcopy(data[top_left])
    for _ in range(2):
        for _ in range(4):
            f_v = deepcopy(image[top_left][first])
            for _ in range(2):
                for _ in range(4):
                    s_v = deepcopy(image[top_left][second])
                    for _ in range(2):
                        for _ in range(4):
                            if all(f_v[0] == tl_v[-1]) and all(s_v[:, 0] == tl_v[:, -1]):
                                img_k[(0, 0)] = k
                                img_k[(1, 0)] = first
                                img_k[(0, 1)] = second

                                img_v[(0, 0)] = tl_v
                                img_v[(1, 0)] = f_v
                                img_v[(0, 1)] = s_v

                                queue[first] = image[first]
                                queue[second] = image[second]
                                return
                            elif all(s_v[0] == tl_v[-1]) and all(f_v[:, 0] == tl_v[:, -1]):
                                img_k[(0, 0)] = k
                                img_k[(1, 0)] = second
                                img_k[(0, 1)] = first

                                img_v[(0, 0)] = tl_v
                                img_v[(1, 0)] = s_v
                                img_v[(0, 1)] = f_v

                                queue[first] = image[first]
                                queue[second] = image[second]
                                return
                            s_v = np.rot90(s_v)
                        s_v = np.flip(s_v, 0)
                    f_v = np.rot90(f_v)
                f_v = np.flip(f_v, 0)
            tl_v = np.rot90(tl_v)
        tl_v = np.flip(tl_v, 0)


top_left_calc()

while len(queue.keys()) > 0:
    n_k = list(queue.keys())[0]
    near = list(image[n_k].keys())
    x, y = key4value(n_k, img_k)
    this = img_v[(x, y)]
    for n in deepcopy(near):
        tile = deepcopy(image[n_k][n])
        for _ in range(2):
            for _ in range(4):
                if all(this[:, -1] == tile[:, 0]):
                    img_k[(x, y+1)] = n
                    img_v[(x, y+1)] = tile
                    queue[n] = tile
                    near.remove(n)
                    break
                tile = np.rot90(tile)
            else:
                tile = np.flip(tile, 0)
                continue
            break
        else:
            continue
        break

    for n in deepcopy(near):
        tile = deepcopy(image[n_k][n])
        for _ in range(2):
            for _ in range(4):
                if all(this[-1] == tile[0]):
                    img_k[(x+1, y)] = n
                    img_v[(x+1, y)] = tile
                    queue[n] = tile
                    near.remove(n)
                    break
                tile = np.rot90(tile)
            else:
                tile = np.flip(tile, 0)
                continue
            break
        else:
            continue
        break

    del queue[n_k]


m_x = max([k[1] for k in img_k.keys()])
m_y = max([k[0] for k in img_k.keys()])
res = []
for y in range(m_y + 1):
    for line in range(1, len(img_v[(0, 0)]) - 1):
        res.append("")
        for x in range(m_x + 1):
            res[-1] += "".join(img_v[(y, x)][line][1:-1])

res = np.asarray([list(line) for line in res])

img = deepcopy(res)
for _ in range(2):
    for _ in range(4):
        apply_filter(img)
        img = np.rot90(img)
    img = np.flip(img, 0)

print(sum([sum([1 for c in line if c == "#"]) for line in img]))