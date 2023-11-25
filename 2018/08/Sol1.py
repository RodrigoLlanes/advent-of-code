from collections import defaultdict
import re


class Node:
    def __init__(self, sons, metadata):
        self.sons = sons
        self.meta = metadata


def build_tree(data):
    n_sons = data.pop(0)
    n_meta = data.pop(0)
    sons = [build_tree(data) for _ in range(n_sons)]
    meta = [data.pop(0) for _ in range(n_meta)]
    return Node(sons, meta)


def summa(tree):
    return sum(tree.meta) + sum(summa(son) for son in tree.sons)


if __name__ == "__main__":
    data = [int(n) for n in open("input.txt").readlines()[0].rstrip().split()]
    tree = build_tree(data)
    print(summa(tree))



