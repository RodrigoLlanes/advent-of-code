from math import ceil

inp = [line.rstrip() for line in open("input.txt")]

_max = 0
for boarding in inp:
    max_row = 127
    min_row = 0
    max_column = 7
    min_column = 0
    for letter in boarding[:7]:
        if letter == "F":
            max_row -= ceil((max_row - min_row)/2)
        else:
            min_row += ceil((max_row - min_row)/2)
    for letter in boarding[7:]:
        if letter == "L":
            max_column -= ceil((max_column - min_column) / 2)
        else:
            min_column += ceil((max_column - min_column) / 2)
    _max = max(max_row*8 + max_column, _max)

print(_max)
