from typing import List


class Point:
    def __init__(self, *coords: float) -> None:
        self.coords: List[float] = list(coords)

    def manhattan(self) -> int:
        return sum(self.coords)

    def __hash__(self) -> int:
        return hash(tuple(self.coords))

    def __add__(self, other: 'Point') -> 'Point':
        return Point(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def __mul__(self, other: float):
        return Point(*[coord * other for coord in self.coords])

    def __truediv__(self, other: float):
        return Point(*[coord / other for coord in self.coords])

    def __floordiv__(self, other: float):
        return Point(*[coord // other for coord in self.coords])

    def __mod__(self, other: float):
        return Point(*[coord % other for coord in self.coords])

    def __pow__(self, other: float):
        return Point(*[coord ** other for coord in self.coords])

    def __neg__(self):
        return Point(*[-coord for coord in self.coords])
