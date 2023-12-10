from typing import TypeVar, Union, List, Generic, Iterator, Generator, Tuple

from .point import Point

T = TypeVar("T")
grid_type = Union[T, List['grid_type']]


def _items(elements: List[grid_type]) -> Generator[Tuple[List[int], T], None, None]:
    for index, item in enumerate(elements):
        if isinstance(item, list):
            for p, i in _items(item):
                yield [index] + p, i
        else:
            yield [index], item


class Grid(Generic[T]):
    def __init__(self, grid: List[grid_type], rev: bool = False):
        self.grid = grid
        self.rev = rev

    def coord(self, p: Point) -> List[int]:
        if self.rev:
            return list(reversed(list(p)))
        return list(p)

    def __getitem__(self, key: Point) -> T:
        item = self.grid
        key = self.coord(key)
        for i in key:
            item = item[i]
        return item

    def __setitem__(self, key: Point, value: T) -> None:
        item = self.grid
        key = self.coord(key)
        for i in key[:-1]:
            item = item[i]
        item[key[-1]] = value

    def items(self):
        for p, item in _items(self.grid):
            yield Point(*(reversed(p) if self.rev else p)), item
