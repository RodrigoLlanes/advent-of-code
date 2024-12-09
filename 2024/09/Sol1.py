from pycp.all import run


def parse(line: str):
    return list(map(int, line))


def main(lines: list[list[int]]):
    data = lines[0]
    
    mem = [-1 for _ in range(sum(data))]
    
    index = 0
    id = 0
    for i, elem in enumerate(data):
        if i % 2 == 0:
            for _ in range(elem):
                mem[index] = id
                index += 1
            id += 1
        else:
            index += elem
    
    empty = 0
    last = len(mem)-1
    while mem[empty] != -1:
        empty += 1
    while mem[last] == -1:
        mem[last] -= 1

    while empty < last:
        mem[empty] = mem[last]
        mem[last] = -1

        while mem[empty] != -1:
            empty += 1
        while mem[last] == -1:
            last -= 1
    
    print(sum(a * b for a, b in enumerate(mem) if b != -1))


if __name__ == '__main__':
    run(main, parse)

