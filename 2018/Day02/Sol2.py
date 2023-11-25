from collections import Counter


def solve(ids):
    for id1 in ids:
        for id2 in ids:
            dif = [char1 for (char1, char2) in zip(id1, id2) if char1 == char2]
            if len(dif) == len(id1)-1:
                return "".join(dif)


if __name__ == "__main__":
    ids = [id.strip() for id in open("input.txt", "r").readlines()]
    print(solve(ids))