def calc(exp):
    while "(" in exp:
        i = exp.index("(")
        opened = 1
        for j in range(i + 1, len(exp)):
            if exp[j] == ")":
                opened -= 1
            elif exp[j] == "(":
                opened += 1
            if opened == 0:
                break
        partial_exp = exp[i + 1:j]
        partial_res = calc(partial_exp)
        exp = exp[:i] + str(partial_res) + exp[j + 1:]

    exp_list = exp.split(" ")

    while "+" in exp_list:
        i = exp_list.index("+")
        exp_list = exp_list[:i - 1] + [str(int(exp_list[i - 1]) + int(exp_list[i + 1]))] + exp_list[i + 2:]

    res = int(exp_list[0])
    for elem in exp_list[1:]:
        if elem.isnumeric():
            res *= int(elem)

    return res


inp = [line.rstrip() for line in open("input.txt")]

_sum = 0
for line in inp:
    _sum += calc(line)

print(_sum)
