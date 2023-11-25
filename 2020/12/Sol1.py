class Position:
    def __init__(self, north, east, facing):
        self.north = north
        self.east = east
        self.facing = facing

    def rotate(self, direction, degrees):
        dirs = ["N", "E", "S", "W"]
        if direction == "L":
            dirs = list(reversed(dirs))
        p = dirs.index(self.facing)
        p += degrees / 90
        p %= 4
        self.facing = dirs[int(p)]

    def move(self, direction, steps):
        if direction == "F":
            direction = self.facing

        if direction == "N":
            self.north += steps
        elif direction == "S":
            self.north -= steps
        elif direction == "E":
            self.east += steps
        elif direction == "W":
            self.east -= steps


inp = [line.rstrip() for line in open("input.txt")]

p = Position(0, 0, "E")

for line in inp:
    act = line[0]
    inc = int(line[1:])

    if act in ["R", "L"]:
        p.rotate(act, inc)
    else:
        p.move(act, inc)

print(abs(p.east) + abs(p.north))
