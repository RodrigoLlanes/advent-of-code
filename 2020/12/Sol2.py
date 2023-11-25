class Position:
    def __init__(self, north, east):
        self.north = north
        self.east = east

    def rotate(self, direction, degrees):
        p = degrees / 90
        p %= 4
        p = int(p)
        if direction == "R":
            for i in range(p):
                self.east, self.north = self.north, -self.east
        else:
            for i in range(p):
                self.east, self.north = -self.north, self.east

    def move(self, direction, steps):
        if direction == "N":
            self.north += steps
        elif direction == "S":
            self.north -= steps
        elif direction == "E":
            self.east += steps
        elif direction == "W":
            self.east -= steps


inp = [line.rstrip() for line in open("input.txt")]

ship = Position(0, 0)
waypoint = Position(1, 10)

for line in inp:
    act = line[0]
    inc = int(line[1:])

    if act in ["R", "L"]:
        waypoint.rotate(act, inc)
    elif act == "F":
        ship.move("E", inc * waypoint.east)
        ship.move("N", inc * waypoint.north)
    else:
        waypoint.move(act, inc)

print(abs(ship.east) + abs(ship.north))
