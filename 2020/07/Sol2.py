from collections import defaultdict

inp = [line.rstrip().split(" bags contain ") for line in open("input.txt")]
inp = [[line[0], line[1].replace("bag.", "bags.")[:-6]] for line in inp]
inp = [[line[0], line[1].replace("bag,", "bags,").split(" bags, ")] for line in inp]

guide = defaultdict(lambda: [])
for bag, content in inp:
    for _bag in content:
        if _bag != "no other":
            data = _bag.split(" ")
            color = " ".join(data[1:])
            n = int(data[0])
            guide[bag].append((n, color))


def recursive_search(d):
    if len(guide[d]) == 0:
        return 1
    res = 1
    for c, v in guide[d]:
        res += c * recursive_search(v)
    return res


print(recursive_search("shiny gold") - 1)
