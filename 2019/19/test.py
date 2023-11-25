ray = [list(line.strip()) for line in open("test.txt", "r").readlines()]

def test_is_affected(x, y):
    if x >= len(ray[y]):
        return 0
    return ray[y][x] == "#" or ray[y][x] == "O"