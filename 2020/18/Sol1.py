def calc(exp):
    while "(" in exp:
        i = exp.index("(")
        opened = 1
        for j in range(i+1, len(exp)):
            if exp[j] == ")":
                opened -= 1
            elif exp[j] == "(":
                opened += 1
            if opened == 0:
                break
        partial_exp = exp[i + 1:j]
        partial_res = calc(partial_exp)
        exp = exp[:i] + str(partial_res) + exp[j+1:]

    res = 0
    op = 1
    for elem in exp.split(" "):
        if op == 1:
            res += int(elem)
            op = 0
        elif op == 2:
            res *= int(elem)
            op = 0
        else:
            if elem == "+":
                op = 1
            elif elem == "*":
                op = 2

    return res


inp = [line.rstrip() for line in open("input.txt")]

_sum = 0
for line in inp:
    _sum += calc(line)

print(_sum)
