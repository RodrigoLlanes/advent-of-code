from typing import List


class Point:
    def __init__(self, *coords: int) -> None:
        self.coords: List[int] = list(coords)

    def manhattan(self) -> int:
        return sum(self.coords)

    @property
    def x(self) -> int:
        return self.coords[0]

    @x.setter
    def x(self, value: int) -> None:
        self.coords[0] = value

    @property
    def y(self) -> int:
        return self.coords[1]

    @y.setter
    def y(self, value: int) -> None:
        self.coords[1] = value

    @property
    def z(self) -> int:
        return self.coords[2]

    @z.setter
    def z(self, value: int) -> None:
        self.coords[2] = value

    def __getitem__(self, item: int) -> int:
        return self.coords[item]

    def __setitem__(self, key: int, value: int) -> None:
        self.coords[key] = value

    def __delitem__(self, key: int) -> None:
        del self.coords[key]

    def __hash__(self) -> int:
        return hash(tuple(self.coords))

    def __add__(self, other: 'Point') -> 'Point':
        return Point(*[self.coords[i] + other.coords[i] for i in range(len(self.coords))])

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(*[self.coords[i] - other.coords[i] for i in range(len(self.coords))])

    def __mul__(self, other: int) -> 'Point':
        return Point(*[coord * other for coord in self.coords])

    def __truediv__(self, other: int) -> 'Point':
        return Point(*[coord / other for coord in self.coords])

    def __floordiv__(self, other: int) -> 'Point':
        return Point(*[coord // other for coord in self.coords])

    def __mod__(self, other: int) -> 'Point':
        return Point(*[coord % other for coord in self.coords])

    def __pow__(self, other: int) -> 'Point':
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
