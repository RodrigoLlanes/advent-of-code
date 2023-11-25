from collections import defaultdict
import re


class Node:
    def __init__(self, sons, metadata):
        self.sons = sons
        self.meta = metadata

    def value(self):
        if len(self.sons) == 0:
            return sum(self.meta)
        else:
            return sum([self.sons[i-1].value() for i in self.meta if 0 < i <= len(self.sons)])


def build_tree(data):
    n_sons = data.pop(0)
    n_meta = data.pop(0)
    sons = [build_tree(data) for _ in range(n_sons)]
    meta = [data.pop(0) for _ in range(n_meta)]
    return Node(sons, meta)


if __name__ == "__main__":
    data = [int(n) for n in open("input.txt").readlines()[0].rstrip().split()]
    tree = build_tree(data)
    print(tree.value())



