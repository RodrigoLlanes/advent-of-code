from copy import deepcopy


_inp = [line.rstrip() for line in open("input.txt")]

inp = []
for line in _inp:
    ingredients, allergens = line[:-1].split(" (")
    ingredients = ingredients.split(" ")
    allergens = allergens[9:].split(", ")
    inp.append([ingredients, allergens])

data = {}
for ingredients, allergens in inp:
    for allergen in allergens:
        if allergen not in data:
            data[allergen] = set(ingredients)
        else:
            data[allergen] = data[allergen].intersection(set(ingredients))

possible_allergens = [len(i) for i in list(data.values())]
res = []
while len(data.keys()) > 0:
    for k, v in deepcopy(data).items():
        if len(v) == 1:
            for _k, _v in deepcopy(data).items():
                if _k != k:
                    if list(v)[0] in _v:
                        data[_k].remove(list(v)[0])
            res.append((k, list(v)[0]))
            del data[k]

res = ",".join([x[1] for x in sorted(res, key=lambda x: x[0])])

print(res)
