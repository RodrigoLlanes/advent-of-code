from copy import deepcopy
from collections import defaultdict
from test import test_is_affected

class IntcodeMachine:
    def __init__(self, inp):
        self.inp = inp
        self.rb = 0

    def checkMemory(self, n, m):
        if(m == "1"):
            if(n >= len(self.inp)):
                self.inp += ["0" for j in range((n + 1) - len(self.inp))]
            return(n)
        elif(m == "0"):
            self.checkMemory(n, "1")
            return self.checkMemory(int(self.inp[n]), "1")
        elif(m == "2"):
            self.checkMemory(n, "1")
            return self.checkMemory(self.rb + int(self.inp[n]), "1")
        else:
            print("error> Invalid memory acces code (" + str(m) + ")")

    def set(self, n, v, m):
        index = self.checkMemory(n, m)
        self.inp[index] = v

    def get(self, n, m):
        index = self.checkMemory(n, m)
        return self.inp[index]

    def run(self, inputs=[]):
        i=0
        while True:
            opCode = '{:0>2}'.format(self.inp[i])
            opCode = opCode[len(opCode) - 2:len(opCode)]
            if (opCode == "01"):
                aux = '{:0>5}'.format(self.inp[i])
                a = self.get(i + 1, aux[2])
                b = self.get(i + 2, aux[1])
                self.set(i + 3, str(int(a) + int(b)), aux[0])
                i+=4
            elif (opCode == "02"):
                aux = '{:0>5}'.format(self.inp[i])
                a = self.get(i + 1, aux[2])
                b = self.get(i + 2, aux[1])
                self.set(i + 3, str(int(a) * int(b)), aux[0])
                i+=4
            elif (opCode == "03"):
                aux = '{:0>3}'.format(self.inp[i])
                if len(inputs) > 0:
                    inputData = inputs.pop(0) # .pop() DEFAULT INDEX IS -1
                else:
                    inputData = str(input(">>"))
                self.set(i + 1, inputData, aux[0])
                i+=2
            elif (opCode == "04"):
                aux = '{:0>3}'.format(self.inp[i])
                outputData = self.get(i + 1, aux[0])
                #print("out> " + outputData)
                return outputData
                i+=2
            elif (opCode == "05"):
                aux = '{:0>4}'.format(self.inp[i])
                a = self.get(i + 1, aux[1])
                addres = self.get(i + 2, aux[0])
                if(a != "0"): i = int(addres)
                else: i = i+3
            elif (opCode == "06"):
                aux = '{:0>4}'.format(self.inp[i])
                a = self.get(i + 1, aux[1])
                addres = self.get(i + 2, aux[0])
                if(a == "0"): i = int(addres)
                else: i = i+3
            elif (opCode == "07"):
                aux = '{:0>5}'.format(self.inp[i])
                a = self.get(i + 1, aux[2])
                b = self.get(i + 2, aux[1])
                if(int(a) < int(b)): self.set(i + 3, "1", aux[0])
                else: self.set(i + 3, "0", aux[0])
                i += 4
            elif (opCode == "08"):
                aux = '{:0>5}'.format(self.inp[i])
                a = self.get(i + 1, aux[2])
                b = self.get(i + 2, aux[1])
                if(int(a) == int(b)): self.set(i + 3, "1", aux[0])
                else: self.set(i + 3, "0", aux[0])
                i += 4
            elif (opCode == "09"):
                aux = '{:0>3}'.format(self.inp[i])
                self.rb += int(self.get(i + 1, aux[0]))
                i+=2
            elif(opCode == "99"):
                return -1
            else:
                print("error> " + self.inp[i])
                return -1


def memoize(f):
    mem = {}
    def func(inp, x, y):
        if (x, y) not in mem:
            mem[(x, y)] = f(inp, x, y)
        return mem[(x, y)]
    return func


@memoize
def is_affected(inp, x, y):
    #return test_is_affected(x, y)
    return int(IntcodeMachine(deepcopy(inp)).run([x, y]))


def left(inp, x, y):
    while True:
        if is_affected(inp, x, y):
            break
        else:
            x += 1
    return x


def solve(inp, size):
    d = size - 1
    x, y = 0, d
    while True:
        x = left(inp, x, y)
        
        if is_affected(inp, x, y-d) and is_affected(inp, x+d, y-d):
            return x, y-d
        y += 1


if __name__ == "__main__":
    f = open("input.txt", "r").read()
    inp = list(map(str, f.split(",")))
    x, y = solve(inp, 100)
    print(x * 10000 + y)
