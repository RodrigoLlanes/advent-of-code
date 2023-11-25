class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

    def __str__(self):
        _next = self.next
        r = str(self.value)
        while _next != self and _next is not None:
            r += str(_next.value)
            _next = _next.next
        return r

    def __contains__(self, key):
        if key == self.value:
            return True
        _next = self.next
        while _next != self and _next is not None:
            if key == _next.value:
                return True
            _next = _next.next
        return False


def extract(node):
    node.prev.next = node.next.next.next
    node.next.next.next.prev = node.prev

    node.prev = None
    node.next.next.next = None
    return node


def insert(node, to_insert):
    to_insert.next.next.next = node.next
    node.next.prev = to_insert.next.next

    node.next = to_insert
    to_insert.prev = node


def is_min(node, out):
    if node.value > 4:
        return False
    for v in range(node.value-1, 0, -1):
        if v not in out:
            return False
    return True


def get_max_value(out):
    if 1000000 not in out:
        return 1000000
    if 999999 not in out:
        return 999999
    if 999998 not in out:
        return 999998
    return 999997


_inp = [int(x) for x in "925176834"] + [x for x in range(10, 1000001)]

inp = {}
prev = None
for i in _inp:
    n = Node(i)
    inp[i] = n
    if prev is not None:
        n.prev = prev
        prev.next = n
    prev = n
inp[_inp[0]].prev = prev
prev.next = inp[_inp[0]]

for step in range(10000000):
    prev = prev.next
    ext = extract(prev.next)

    if is_min(prev, ext):
        dest = inp[get_max_value(ext)]
    else:
        for j in range(prev.value-1, 0, -1):
            if j not in ext:
                dest = inp[j]
                break
    insert(dest, ext)

print(inp[1].next.value * inp[1].next.next.value)
