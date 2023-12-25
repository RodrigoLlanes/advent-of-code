import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pycp.all import *
import networkx as nx



def parse(line: str):
    k, v = line.split(': ')
    v = v.split()
    return k, v


def main(lines: list) -> None:
    G = nx.DiGraph()
    for k, v in lines:
        for o in v:
            G.add_edge(k, o, capacity=1.0)
            G.add_edge(o, k, capacity=1.0)

    n0 = list(G.nodes)[0]
    for n1 in G.nodes:
        if n0 != n1:
            cut_value, (sg0, sg1) = nx.minimum_cut(G, n0, n1)
            if cut_value == 3:
                print(len(sg0) * len(sg1))
                break


if __name__ == '__main__':
    run(main, parse)
