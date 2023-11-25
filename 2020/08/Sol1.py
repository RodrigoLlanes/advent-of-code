inp = [line.rstrip().split(" ") for line in open("input.txt")]

accumulator = 0
index = 0
executed = {}
while index < len(inp):
    op = inp[index][0]
    arg = int(inp[index][1])

    if op == "nop":
        pass
    elif op == "acc":
        accumulator += arg
    elif op == "jmp":
        index += arg-1

    index += 1
    if index in executed:
        break
    else:
        executed[index] = 1

print(accumulator)

