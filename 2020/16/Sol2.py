def check_rules(number, rules):
    for rule in rules:
        for _range in rule:
            if _range[0] <= number <= _range[1]:
                return True
    return False


def check_rules_(number, rules, valids):
    res = []
    for key in valids:
        rule = rules[key]
        for _range in rule:
            if _range[0] <= number <= _range[1]:
                res.append(key)
                break

    return res


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

valid_tickets = []
for ticket in nearby_tickets + [my_ticket]:
    for n in ticket:
        if not check_rules(n, rules.values()):
            break
    else:
        valid_tickets.append(ticket)

possibilities = [list(rules.keys()) for i in range(len(my_ticket))]
for ticket in valid_tickets:
    for i in range(len(ticket)):
        possibilities[i] = check_rules_(ticket[i], rules, possibilities[i])

fields = [None for i in range(len(my_ticket))]
while None in fields:
    for i in range(len(possibilities)):
        if len(possibilities[i]) == 1:
            fields[i] = possibilities[i][0]
            possibilities[i] = []
            for j in range(len(possibilities)):
                if fields[i] in possibilities[j]:
                    possibilities[j].remove(fields[i])

res = 1
for i in range(len(fields)):
    if "departure" in fields[i]:
        res *= my_ticket[i]
print(res)