from collections import defaultdict

inp = [line.rstrip().split(" bags contain ") for line in open("input.txt")]
inp = [[line[0], line[1].replace("bag.", "bags.")[:-6]] for line in inp]
inp = [[line[0], line[1].replace("bag,", "bags,").split(" bags, ")] for line in inp]

guide = defaultdict(lambda: set())
for bag, content in inp:
    for _bag in content:
        color = " ".join(_bag.split(" ")[1:])
        guide[color].add(bag)

c = list(guide["shiny gold"])
res = set()
while len(c) > 0:
    actual = c.pop()
    res.add(actual)
    c += guide[actual]

print(len(res))
