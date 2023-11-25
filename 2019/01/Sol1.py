from math import floor

f = open("Input.txt", "r")
inp = [int(line) for line in f]

result = 0
for m in inp:
    result += floor(m / 3) - 2
print(result)
