from typing import List


class Point:
    def __init__(self, *coords: float) -> None:
        self.coords: List[float] = list(coords)

    def manhattan(self) -> int:
        return sum(self.coords)

    @property
    def x(self) -> float:
        return self.coords[0]

    @x.setter
    def x(self, value: float) -> None:
        self.coords[0] = value

    @property
    def y(self) -> float:
        return self.coords[1]

    @y.setter
    def y(self, value: float) -> None:
        self.coords[1] = value

    @property
    def z(self) -> float:
        return self.coords[2]

    @z.setter
    def z(self, value: float) -> None:
        self.coords[2] = value

    def __hash__(self) -> int:
        return hash(tuple(self.coords))

    def __add__(self, other: 'Point') -> 'Point':
        return Point(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def __mul__(self, other: float) -> 'Point':
        return Point(*[coord * other for coord in self.coords])

    def __truediv__(self, other: float) -> 'Point':
        return Point(*[coord / other for coord in self.coords])

    def __floordiv__(self, other: float) -> 'Point':
        return Point(*[coord // other for coord in self.coords])

    def __mod__(self, other: float) -> 'Point':
        return Point(*[coord % other for coord in self.coords])

    def __pow__(self, other: float) -> 'Point':
        return Point(*[coord ** other for coord in self.coords])

    def __neg__(self) -> 'Point':
        return Point(*[-coord for coord in self.coords])

    def __str__(self) -> str:
        return '(' + ', '.join(map(str, self.coords)) + ')'

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: 'Point') -> bool:
        return self.coords == other.coords

    def __ne__(self, other: 'Point') -> bool:
        return self.coords != other.coords

    def __lt__(self, other: 'Point') -> bool:
        return self.coords < other.coords

    def __iter__(self):
        for coord in self.coords:
            yield coord


DIRECTIONS4 = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]
DIRECTIONS8 = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0),
               Point(1, 1), Point(-1, 1), Point(1, -1), Point(-1, -1)]
