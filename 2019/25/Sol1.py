from copy import deepcopy


class Queue:
    def __init__(self, queue=[], default=None):
        self.default_value = default
        self.queue = queue

    def dequeue(self):
        if len(self.queue) == 0:
            self.enqueue_all([str(ord(char)) for char in input(">>")] + ["10"])
        return self.queue.pop(0)

    def enqueue(self, value):
        self.queue.append(value)

    def enqueue_all(self, value):
        for item in value:
            self.enqueue(item)

    def __len__(self):
        return len(self.queue)


class IntcodeMachine:
    def __init__(self, code):
        self.inp = code
        self.ptr = 0
        self.queue = Queue()
        self.out = ""
        self.rb = 0

    def checkMemory(self, n, m):
        if m == "1":
            if n >= len(self.inp):
                self.inp += ["0" for j in range((n + 1) - len(self.inp))]
            return n
        elif m == "0":
            self.checkMemory(n, "1")
            return self.checkMemory(int(self.inp[n]), "1")
        elif m == "2":
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

    def output(self, value):
        if value == "10":
            print(self.out)
            self.out = ""
        else:
            self.out += chr(int(value))

    def step(self):
        op_code = '{:0>2}'.format(self.inp[self.ptr])
        op_code = op_code[len(op_code) - 2:len(op_code)]
        if op_code == "01":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            self.set(self.ptr + 3, str(int(a) + int(b)), aux[0])
            self.ptr += 4
        elif op_code == "02":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            self.set(self.ptr + 3, str(int(a) * int(b)), aux[0])
            self.ptr += 4
        elif op_code == "03":
            aux = '{:0>3}'.format(self.inp[self.ptr])
            input_data = self.queue.dequeue()
            self.set(self.ptr + 1, input_data, aux[0])
            self.ptr += 2
        elif op_code == "04":
            aux = '{:0>3}'.format(self.inp[self.ptr])
            output_data = self.get(self.ptr + 1, aux[0])
            self.output(output_data)
            self.ptr += 2
        elif op_code == "05":
            aux = '{:0>4}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[1])
            address = self.get(self.ptr + 2, aux[0])
            if a != "0": self.ptr = int(address)
            else: self.ptr += 3
        elif op_code == "06":
            aux = '{:0>4}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[1])
            address = self.get(self.ptr + 2, aux[0])
            if a == "0": self.ptr = int(address)
            else: self.ptr += 3
        elif op_code == "07":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            if int(a) < int(b): self.set(self.ptr + 3, "1", aux[0])
            else: self.set(self.ptr + 3, "0", aux[0])
            self.ptr += 4
        elif op_code == "08":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            if int(a) == int(b): self.set(self.ptr + 3, "1", aux[0])
            else: self.set(self.ptr + 3, "0", aux[0])
            self.ptr += 4
        elif op_code == "09":
            aux = '{:0>3}'.format(self.inp[self.ptr])
            self.rb += int(self.get(self.ptr + 1, aux[0]))
            self.ptr += 2
        elif op_code == "99":
            return -1
        else:
            print("error> " + self.inp[self.ptr])
            return -1
        return 0

    def run(self):
        while True:
            if self.step() == -1:
                break


if __name__ == "__main__":
    f = open("input.txt", "r").read()
    code = list(map(str, f.split(",")))
    machine = IntcodeMachine(deepcopy(code))
    machine.run()
