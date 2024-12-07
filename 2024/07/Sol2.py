from pycp.all import run


def parse(line: str):
    a, b = line.split(':')
    return int(a), list(map(int, b.split()))


def combinations(ops, i, target):
    if i == 0:
        yield ops[i]
        return
    prevs = list(combinations(ops, i-1, target))
    for prev in prevs:
        if prev * ops[i] <= target:
            yield prev * ops[i]
        if prev + ops[i] <= target:
            yield prev + ops[i]
        if int(str(prev) + str(ops[i])) <= target:
            yield int(str(prev) + str(ops[i]))


def main(lines: list[list[int]]):
    res = 0
    print(max(len(b) for a, b in lines))
    for target, ops in lines:
        if any(target == comb for comb in combinations(ops, len(ops)-1, target)):
            res += target
        
    print(res)


if __name__ == '__main__':
    run(main, parse)

