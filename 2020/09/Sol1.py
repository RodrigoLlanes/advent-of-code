inp = [int(line.rstrip()) for line in open("input.txt")]

preamble_len = 25
preamble = []

for i in inp[:preamble_len]:
    preamble.append(i)

for elem in inp[preamble_len:]:
    if (elem < 2 * min(preamble)) or (elem > 2 * max(preamble)):
        print(elem)
        break
    else:
        for i in range(len(preamble)):
            for j in range(len(preamble)):
                if i != j:
                    if preamble[j]+preamble[i] == elem:
                        break
            else:
                continue
            break
        else:
            print(elem)
            break
        preamble.pop(0)
        preamble.append(elem)


