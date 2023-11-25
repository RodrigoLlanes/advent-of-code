from copy import deepcopy
import threading
from collections import defaultdict

print_lock = threading.Lock()


def secure_print(text):
    with print_lock:
        print(text)


class Queue:
    def __init__(self, queue=[], default=-1):
        self.default_value = default
        self.queue = queue

    def dequeue(self):
        if len(self.queue) == 0:
            return self.default_value
        return self.queue.pop(0)

    def enqueue(self, value):
        self.queue.append(value)

    def __len__(self):
        return len(self.queue)


class IntcodeMachine:
    def __init__(self, code, inputs, id, package_size=3):
        self.id = id
        self.package_size = package_size
        self.inp = code
        self.ptr = 0
        self.queue = Queue(inputs)
        self.output_queue = Queue()
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

    def output(self, value):
        self.output_queue.enqueue(value)
        if len(self.output_queue) == self.package_size:
            return [self.output_queue.dequeue() for _ in range(self.package_size)]

    def step(self):
        opCode = '{:0>2}'.format(self.inp[self.ptr])
        opCode = opCode[len(opCode) - 2:len(opCode)]
        out = None
        if opCode == "01":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            self.set(self.ptr + 3, str(int(a) + int(b)), aux[0])
            self.ptr += 4
        elif opCode == "02":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            self.set(self.ptr + 3, str(int(a) * int(b)), aux[0])
            self.ptr += 4
        elif opCode == "03":
            aux = '{:0>3}'.format(self.inp[self.ptr])
            inputData = self.queue.dequeue()
            #secure_print(f"{self.id} << {inputData}")
            self.set(self.ptr + 1, inputData, aux[0])
            self.ptr += 2
        elif opCode == "04":
            aux = '{:0>3}'.format(self.inp[self.ptr])
            outputData = self.get(self.ptr + 1, aux[0])
            out = self.output(outputData)
            #print("out> " + outputData)
            self.ptr += 2
        elif opCode == "05":
            aux = '{:0>4}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[1])
            addres = self.get(self.ptr + 2, aux[0])
            if a != "0": self.ptr = int(addres)
            else: self.ptr += 3
        elif opCode == "06":
            aux = '{:0>4}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[1])
            addres = self.get(self.ptr + 2, aux[0])
            if a == "0": self.ptr = int(addres)
            else: self.ptr += 3
        elif opCode == "07":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            if int(a) < int(b): self.set(self.ptr + 3, "1", aux[0])
            else: self.set(self.ptr + 3, "0", aux[0])
            self.ptr += 4
        elif opCode == "08":
            aux = '{:0>5}'.format(self.inp[self.ptr])
            a = self.get(self.ptr + 1, aux[2])
            b = self.get(self.ptr + 2, aux[1])
            if int(a) == int(b): self.set(self.ptr + 3, "1", aux[0])
            else: self.set(self.ptr + 3, "0", aux[0])
            self.ptr += 4
        elif opCode == "09":
            aux = '{:0>3}'.format(self.inp[self.ptr])
            self.rb += int(self.get(self.ptr + 1, aux[0]))
            self.ptr += 2
        elif opCode == "99":
            return -1, None
        else:
            print("error> " + self.inp[self.ptr])
            return -1, None
        return 0 if out is None else 1, out

    def run(self):
        while True:
            code, out = self.step()
            if code == -1:
                break
            elif code == 1:
                print("out>", out)


def main(code):
    ids = range(50)
    machines = []
    alive = [True for _ in ids]

    def thread_func(id):
        while True:
            if not alive[id]:
                break
            code, out = machines[id].step()
            if code == -1:
                break
            elif code == 1:
                other, x, y = out
                other = int(other)
                secure_print(f"{id} >> {other}: {x} {y}")
                if other == 255:
                    secure_print(f"SOLUTION: {other} {x} {y}")
                    for nid in ids:
                        alive[nid] = False
                    break
                else:
                    machines[other].queue.enqueue(x)
                    machines[other].queue.enqueue(y)
        secure_print(f"Machine {id} dead")


    for id in ids:
        machines.append(IntcodeMachine(deepcopy(code), [id], id))

    threads = list()
    for id in ids:
        x = threading.Thread(target=thread_func, args=(id,))
        threads.append(x)
        x.start()

    for thread in threads:
        thread.join()



if __name__ == "__main__":
    f = open("input.txt", "r").read()
    code = list(map(str, f.split(",")))

    print(main(code))
