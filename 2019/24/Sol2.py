from copy import deepcopy


ADJACENT = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class RecursiveGrid:
    def __init__(self, start):
        self.outer = 0
        self.inner = 0
        self.grids = {0: start}
        self.grow()

    def get(self, x, y, z):
        return self.grids[z][y][x] == "#" if z in self.grids else 0

    def neighbours(self, x, y, z):
        n = 0
        for (dx, dy) in ADJACENT:
            nx, ny = x+dx, y+dy
            if nx < 0:
                n += self.get(1, 2, z + 1)
            elif nx > 4:
                n += self.get(3, 2, z + 1)
            elif ny < 0:
                n += self.get(2, 1, z + 1)
            elif ny > 4:
                n += self.get(2, 3, z + 1)
            elif nx == ny == 2:
                if x == 1:
                    n += sum(self.get(0, i, z-1) for i in range(5))
                elif x == 3:
                    n += sum(self.get(4, i, z-1) for i in range(5))
                elif y == 1:
                    n += sum(self.get(i, 0, z-1) for i in range(5))
                elif y == 3:
                    n += sum(self.get(i, 4, z-1) for i in range(5))
            else:
                n += self.get(nx, ny, z)
        return n

    def grow(self):
        if any(self.grids[self.outer][y][x] == "#" for x in range(5) for y in range(5) if (y == 0) or (x == 0) or (y == 4) or (x == 4)):
            self.outer += 1
            self.grids[self.outer] = [["." for _ in range(5)] for _ in range(5)]
        if any(self.grids[self.inner][2+dy][2+dx] == "#" for (dx, dy) in ADJACENT):
            self.inner -= 1
            self.grids[self.inner] = [["." for _ in range(5)] for _ in range(5)]

    def step(self):
        cp = deepcopy(self.grids)
        for (z, level) in self.grids.items():
            for (y, row) in enumerate(level):
                for (x, cell) in enumerate(row):
                    if x == y == 2:
                        continue
                    n = self.neighbours(x, y, z)
                    if cell == "#" and n != 1:
                        cp[z][y][x] = "."
                    elif cell == "." and 1 <= n <= 2:
                        cp[z][y][x] = "#"
        self.grids = cp
        self.grow()

    def biodiversity(self):
        b = 0
        for (z, level) in self.grids.items():
            for (y, row) in enumerate(level):
                for (x, cell) in enumerate(row):
                    if x == y == 2:
                        continue
                    b += self.get(x, y, z)
        return b


if __name__ == "__main__":
    grid = [list(line.strip()) for line in open("Input.txt", "r").readlines()]
    grid = RecursiveGrid(grid)

    for _ in range(200):
        grid.step()

    print(grid.biodiversity())
