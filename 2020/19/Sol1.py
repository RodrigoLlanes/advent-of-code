rules = {}


def base_rule(_rule, _line, _i):
    if _i >= len(_line):
        return False, _i
    return _rule == _line[_i], _i + 1


def composite_rule(_rules, _line, _i):
    _continue = True
    new_i = _i
    for _rule in _rules:
        if new_i >= len(_line) or not _continue:
            return False, _i
        _continue, new_i = rules[_rule](_line, new_i)
    return _continue, new_i


def or_rule(_op0, _op1, _line, _i):
    if _i >= len(_line):
        return False, _i

    _continue, new_i = composite_rule(_op0, _line, _i)
    if _continue:
        return True, new_i

    _continue, new_i = composite_rule(_op1, _line, _i)
    return _continue, new_i


inp = [line.rstrip() for line in open("input.txt")]

rules_data = [line.split(": ") for line in inp[:inp.index("")]]
data = inp[inp.index("") + 1:]

for rule_data in rules_data:
    if '"' in rule_data[1]:
        rules[rule_data[0]] = lambda x, i, value=rule_data[1][1]: base_rule(value, x, i)
    elif '|' in rule_data[1]:
        rule = [x.split(" ") for x in rule_data[1].split(" | ")]
        rules[rule_data[0]] = lambda x, i, _rule=rule: or_rule(_rule[0], _rule[1], x, i)
    else:
        rule = rule_data[1].split(" ")
        rules[rule_data[0]] = lambda x, i, _rule=rule: composite_rule(_rule, x, i)

count = 0
for line in data:
    correct, i = rules["0"](line, 0)
    if correct and i == len(line):
        count += 1

print(count)
