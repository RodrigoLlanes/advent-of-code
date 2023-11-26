from heapq import heapify, heappush, heappop
from typing import TypeVar, Generic, List

T = TypeVar("T")


class Heap(Generic[T]):
    def __init__(self, heap: List[T] = None):
        self.heap = heapify(heap) if heap is not None else []

    def push(self, item: T) -> None:
        heappush(self.heap, item)

    def pop(self) -> T:
        return heappop(self.heap)
