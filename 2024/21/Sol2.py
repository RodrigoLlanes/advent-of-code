from pycp.all import *


sign = lambda x: -1 if x < 0 else 1


numeric_keys = {
    '0': Point(1, 3),
    'A': Point(2, 3)
}
for i in range(1, 10):
    numeric_keys[str(i)] = Point((i-1)%3, 2 - (i-1)//3)

LEFT = Point(-1, 0)
RIGHT = Point(1, 0)
UP = Point(0, -1)
DOWN = Point(0, 1)

arrow_keys = {
    UP: Point(1, 0),
    DOWN: Point(1, 1),
    LEFT: Point(0, 1),
    RIGHT: Point(2, 1),
    'A': Point(2, 0)
}


def parse(line: str):
    return line


def press_nums(seq):
    valids = set(numeric_keys.values())
    
    pos = numeric_keys['A']
    paths = []
    heap = Heap()
    heap.push((0, 0, pos, []))
    while len(heap):
        l, index, pos, path = heap.pop()

        if pos == numeric_keys[seq[index]]:
            path.append('A')
            if index == len(seq) - 1:
                paths.append(path)
                continue
            index += 1
        
        target = numeric_keys[seq[index]]
        d = target - pos
        if d.x != 0:
            dir = Point(sign(d.x), 0)
            if pos + dir in valids:
                heap.push((l+1, index, pos+dir, path + [dir]))
        if d.y != 0:
            dir = Point(0, sign(d.y))
            if pos + dir in valids:
                heap.push((l+1, index, pos+dir, path + [dir]))
    return paths


@cache()
def press_move(src, target, depth):
    valids = set(arrow_keys.values())
    
    pos = arrow_keys[src]
    paths = []
    heap = Heap()
    heap.push((0, pos, []))
    while len(heap):
        l, pos, path = heap.pop()

        if pos == arrow_keys[target]:
            path.append('A')
            paths.append(path)
            continue
        
        d = arrow_keys[target] - pos

        if d.x != 0:
            dir = Point(sign(d.x), 0)
            if pos + dir in valids:
                heap.push((l+1, pos+dir, path + [dir]))
        if d.y != 0:
            dir = Point(0, sign(d.y))
            if pos + dir in valids:
                heap.push((l+1, pos+dir, path + [dir]))
    
    if depth == 1:
        return min([len(p) for p in paths])
    
    scores = [0] * len(paths)
    for i, path in enumerate(paths):
        prev = 'A'
        for p in path:
            scores[i] += press_move(prev, p, depth-1)
            prev = p
    return min(scores)


def main(lines: list[str]):
    count = 0
    for line in lines:
        scores = []
        for p in press_nums(line):
            score = 0
            prev = 'A'
            for t in p:
                score += press_move(prev, t, 25)
                prev = t
            scores.append(score)
        m = min(scores)
        
        count += m * int(line[:-1])
    print(count)


if __name__ == '__main__':
    run(main, parse)
