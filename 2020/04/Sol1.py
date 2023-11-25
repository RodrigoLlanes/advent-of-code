inp = [line.rstrip().split(" ") for line in open("input.txt")]
i = 0
count = 0

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
l = fields.copy()

while i <= len(inp):
    if i == len(inp) or inp[i] == [""]:
        if l == [] or l == ["cid"]:
            count += 1
        l = fields.copy()
    else:
        for data in inp[i]:
            k = data.split(":")[0]
            v = data.split(":")[1]
            if k in l:
                l.remove(data.split(":")[0])
    i += 1
print(count)
