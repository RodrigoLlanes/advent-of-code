from collections import Counter


def solve(ids):
    two = 0
    three = 0
    for id in ids:
        c = Counter(id)
        two += (2 in c.values())
        three += (3 in c.values())
    return two * three


if __name__ == "__main__":
    ids = [id.strip() for id in open("input.txt", "r").readlines()]
    print(solve(ids))