from pycp.all import run


def parse(line: str):
    return list(map(int, line))


def main(lines: list[list[int]]):
    data = lines[0]
    
    index = 0
    id = 0
    free_mem = {}
    groups = {}
    for i, elem in enumerate(data):
        if i % 2 == 0:
            groups[id] = (index, elem)
            id += 1
        elif elem > 0:
            free_mem[index] = elem
        index += elem
    
    for id in reversed(sorted(list(groups.keys()))):
        index, length = groups[id]
        for mem_index in sorted(list(free_mem.keys())):
            mem_length = free_mem[mem_index]
            if mem_length >= length and mem_index < index:
                del groups[id]
                del free_mem[mem_index]

                groups[id] = (mem_index, length)
                if mem_length > length:
                    free_mem[mem_index + length] = mem_length - length
                break

    res = 0
    for id, (index, length) in groups.items():
        for i in range(index, index+length):
            res += i * id
    
    print(res)


if __name__ == '__main__':
    run(main, parse)

