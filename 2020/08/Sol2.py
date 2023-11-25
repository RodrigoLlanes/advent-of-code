from copy import deepcopy

inp = [line.rstrip().split(" ") for line in open("input.txt")]


def run(code):
    accumulator = 0
    index = 0
    executed = {}
    while index < len(code):
        op = code[index][0]
        arg = int(code[index][1])

        if op == "nop":
            pass
        elif op == "acc":
            accumulator += arg
        elif op == "jmp":
            index += arg - 1

        index += 1
        if index in executed:
            return False, None
        else:
            executed[index] = 1
    return True, accumulator

    index += 1


for i in range(len(inp)):
    if inp[i][0] == "jmp" or inp[i][0] == "nop":
        _inp = deepcopy(inp)
        _inp[i][0] = "nop" if inp[i][0] == "jmp" else "nop"
        not_loop, res = run(_inp)
        if not_loop:
            print(res)
            break
