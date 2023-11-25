if __name__ == "__main__":
    changes = [int(frec) for frec in open("input.txt", "r").readlines()]
    print(sum(changes))