from collections import defaultdict
import re


def react(polymer):
    i = 0
    while i < len(polymer) - 1:
        if (polymer[i] != polymer[i+1]) and (polymer[i].lower() == polymer[i+1].lower()):
            polymer.pop(i)
            polymer.pop(i)
            if i > 0:
                i -= 1
        else:
            i += 1
    return len(polymer)


if __name__ == "__main__":
    polymer = list(open("input.txt", "r").read().strip())
    print(react(polymer))