inp = [line.rstrip() for line in open("input.txt")]

trees = 0
x, y = 0, 0
while y < len(inp) - 1:
    x = (x + 3) % len(inp[0])
    y += 1
    if inp[y][x] == "#":
        trees += 1
print(trees)
