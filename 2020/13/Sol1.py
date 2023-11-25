inp = [line.rstrip() for line in open("input.txt")]

start = int(inp[0])
delays = [int(t) for t in inp[1].split(",") if t != "x"]

_min = 10e999
_id = 0
for delay in delays:
    t = delay - (start % delay)
    if t < _min:
        _min = t
        _id = delay
print(_id * _min)
