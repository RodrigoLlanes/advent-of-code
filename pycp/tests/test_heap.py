from pycp.structures import Heap


def test_heap():
    heap = Heap()
    heap.push(0)
    heap.push(1)
    assert heap.pop() == 0
    heap.push(-1)
    assert heap.pop() == -1
    assert heap.pop() == 1
