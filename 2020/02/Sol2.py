inp = [line for line in open("input.txt")]

cont = 0

for line in inp:
    spl = line.split(" ")
    mi, ma = map(int, spl[0].split("-"))
    letter = spl[1][0]
    data = spl[2]
    if (data[mi-1] == letter) != (data[ma-1] == letter):  # xor
        cont += 1
print(cont)
