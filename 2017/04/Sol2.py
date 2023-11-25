from sys import stdin 


def main(lines: list[str]):
    count = 0
    for line in lines:
        words = line.split()
        sets = set()
        for word in words:
            sets.add(frozenset(list(word)))
        if len(sets) == len(words):
            count += 1
    print(count)


if __name__ == "__main__":
    main(stdin.read().splitlines())

