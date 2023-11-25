import math

f = open("Input.txt", "r")
result = 0
for line in f:
    fuel = math.floor((int(line))/3) - 2
    while (fuel > 0):
        result += fuel
        fuel = math.floor(fuel/3) - 2
print(result)
