import re

inp = [line.rstrip().split(" ") for line in open("input.txt")]
i = 0
count = 0

fields = {"byr": lambda x: (len(x) == 4 and 1920 <= int(x) <= 2002),
          "iyr": lambda x: (len(x) == 4 and 2010 <= int(x) <= 2020),
          "eyr": lambda x: (len(x) == 4 and 2020 <= int(x) <= 2030),
          "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
                           (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
          "hcl": lambda x: (len(x) == 7 and x[0] == "#" and
                            bool(re.compile(r'^[a-f0-9]+$').match(x[1:]))),
          "ecl": lambda x: (x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
          "pid": lambda x: (x.isnumeric() and len(v) == 9),
          "cid": lambda x: True}
l = list(fields.keys())

while i <= len(inp):
    if i == len(inp) or inp[i] == [""]:
        if l == [] or l == ["cid"]:
            count += 1
        l = list(fields.keys())
    else:
        for data in inp[i]:
            k = data.split(":")[0]
            v = data.split(":")[1]
            if k in l:
                if fields[k](v):
                    l.remove(data.split(":")[0])
    i += 1
print(count)
