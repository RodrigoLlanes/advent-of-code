def check_rules(number, rules):
    for rule in rules:
        for _range in rule:
            if _range[0] <= number <= _range[1]:
                return True
    return False


inp = [line.rstrip() for line in open("input.txt")]

_rules = inp[:inp.index("")]
rules = {}
for i in range(len(_rules)):
    field = _rules[i].split(":")[0]
    ranges = [[int(n) for n in r.split("-")] for r in _rules[i].split(":")[1].split(" or ")]
    rules[field] = ranges

inp = inp[inp.index("")+2:]
my_ticket = [int(n) for n in inp[:inp.index("")][0].split(",")]
nearby_tickets = [[int(n) for n in line.split(",")] for line in inp[inp.index("")+2:]]

error = 0
for ticket in nearby_tickets:
    for n in ticket:
        if not check_rules(n, rules.values()):
            error += n
print(error)