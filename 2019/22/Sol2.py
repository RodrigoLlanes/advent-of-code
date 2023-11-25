
# Inverse of deal
def deal(a, b, size):
    return -a, size - 1 - b


# Inverse of cut
def cut(a, b, size, n):
    return a, (b + n) % size


# Inverse of deal with increment
def deal_with_increment(a, b, size, n):
    # https://github.com/metalim/metalim.adventofcode.2019.python/blob/master/22_cards_shuffle.ipynb
    z = pow(n,size-2,size) # == modinv(n,size) 
    return (a * z) % size, (b * z) % size


# https://github.com/metalim/metalim.adventofcode.2019.python/blob/master/22_cards_shuffle.ipynb
def polypow(a,b,m,n):
    if m==0:
        return 1,0
    if m%2==0:
        return polypow(a*a%n, (a*b+b)%n, m//2, n)
    else:
        c,d = polypow(a,b,m-1,n)
        return a*c%n, (a*d+b)%n


if __name__ == "__main__":
    orders = [line.strip() for line in open("input.txt", "r").readlines()]
    orders.reverse()

    size = 119315717514047
    pos = 2020
    times = 101741582076661

    a, b = 1, 0

    for order in orders:
        if order == "deal into new stack":
            a, b = deal(a, b, size)
        elif order.startswith("cut"):
            a, b = cut(a, b, size, int(order.split()[-1]))
        elif order.startswith("deal with increment"):
            a, b = deal_with_increment(a, b, size, int(order.split()[-1]))

    a, b = polypow(a, b, times, size)

    print((pos*a + b) % size)
