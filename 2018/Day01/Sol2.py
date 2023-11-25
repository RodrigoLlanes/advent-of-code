def solve(changes):
    frec = 0
    history = {frec: True}
    while True:
        for change in changes:
            frec += change
            if frec in history:
                return frec
            history[frec] = True


if __name__ == "__main__":
    changes = [int(frec) for frec in open("input.txt", "r").readlines()]
    print(solve(changes))