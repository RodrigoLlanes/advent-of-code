inp = [line.rstrip() for line in open("input.txt")]

mask = "X" * 32
data = {}
for line in inp:
    l = line.split(" ")
    if l[0] == "mask":
        mask = l[2]
    else:
        key = int(l[0][4:-1])
        bin_value = "{0:b}".format(int(l[2])).zfill(36)
        bin_value = "".join([mask_bit if mask_bit != "X" else bit for mask_bit, bit in zip(mask, bin_value)])
        data[key] = int(bin_value, 2)

print(sum(data.values()))
