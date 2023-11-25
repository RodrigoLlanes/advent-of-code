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

possible_allergens = set([j for i in list(data.values()) for j in i])
not_allergens = [j for i in inp for j in i[0] if j not in possible_allergens]
print(len(not_allergens))
