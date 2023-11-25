rules = {}
cache = {}


def base_rule(_rule, _x):
    return _rule == _x


def composite_rule(_rules, _x):
    k = tuple(_rules + [_x])
    if k in cache:
        return cache[k]

    if len(_rules) == 1:
        cache[k] = rules[_rules[0]](_x)
        return cache[k]
    elif len(_rules) == 2:
        for i in range(1, len(_x)):
            if rules[_rules[0]](_x[:i]) and rules[_rules[1]](_x[i:]):
                cache[k] = True
                return True
    else:
        for i in range(1, len(_x)):
            for j in range(i+1, len(_x)):
                if rules[_rules[0]](_x[:i]) and rules[_rules[1]](_x[i:j]) and rules[_rules[2]](_x[j:]):
                    cache[k] = True
                    return True
    cache[k] = False
    return False


def or_rule(_op0, _op1, _x):
    if composite_rule(_op0, _x):
        return True

    return composite_rule(_op1, _x)


inp = [line.rstrip() for line in open("updated_input.txt")]

rules_data = [line.split(": ") for line in inp[:inp.index("")]]
data = inp[inp.index("") + 1:]

for rule_data in rules_data:
    if '"' in rule_data[1]:
        rules[rule_data[0]] = lambda x, value=rule_data[1][1]: base_rule(value, x)
    elif '|' in rule_data[1]:
        rule = [x.split(" ") for x in rule_data[1].split(" | ")]
        rules[rule_data[0]] = lambda x, _rule=rule: or_rule(_rule[0], _rule[1], x)
    else:
        rule = rule_data[1].split(" ")
        rules[rule_data[0]] = lambda x, _rule=rule: composite_rule(_rule, x)

count = 0
for line in data:
    print(line)
    if rules["0"](line):
        count += 1

print(count)
