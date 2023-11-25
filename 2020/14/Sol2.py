inp = [line.rstrip() for line in open("input.txt")]


def apply_mask(_mask, _data):
    res = [""]
    for mask_bit, bit in zip(_mask, _data):
        if mask_bit == "0":
            res = [x + bit for x in res]
        elif mask_bit == "X":
            res = [x + "0" for x in res] + [x + "1" for x in res]
        else:
            res = [x + "1" for x in res]
    return [int(r, 2) for r in res]


mask = "X" * 32
data = {}
for line in inp:
    l = line.split(" ")
    if l[0] == "mask":
        mask = l[2]
    else:
        bin_k = "{0:b}".format(int(l[0][4:-1])).zfill(36)
        keys = apply_mask(mask, bin_k)
        value = int(l[2])
        for k in keys:
            data[k] = value

print(sum([x for x in data.values()]))
