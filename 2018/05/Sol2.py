from copy import copy


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


def clear_react(polymer):
    units = set(polymer.lower())
    res = len(polymer)
    for unit in units:
        res = min(res, react(list(filter(lambda x: x.lower() != unit, polymer))))
    
    return res


if __name__ == "__main__":
    polymer = open("input.txt", "r").read().strip()
    print(clear_react(polymer))