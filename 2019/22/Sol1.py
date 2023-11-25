
# Deal
def deal(size, pos):
    return (size-1) - pos


# Cut
def cut(size, pos, n):
    return (pos - n) % size


# Deal with increment
def deal_with_increment(size, pos, n):
    return (pos * n) % size


if __name__ == "__main__":
    orders = [line.strip() for line in open("input.txt", "r").readlines()]

    size = 10007
    pos = 2019

    for order in orders:
        if order == "deal into new stack":
            pos = deal(size, pos)
        elif order.startswith("cut"):
            pos = cut(size, pos, int(order.split()[-1]))
        elif order.startswith("deal with increment"):
            pos = deal_with_increment(size, pos, int(order.split()[-1]))

    print(pos)
