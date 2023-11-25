inp = sorted([int(line.rstrip()) for line in open("input.txt")])

one = 0
three = 1

prev = 0
while len(inp) > 0:
    _next = inp.pop(0)
    if _next - prev == 1:
        one += 1
    elif _next - prev == 3:
        three += 1
    prev = _next

print(one * three)
