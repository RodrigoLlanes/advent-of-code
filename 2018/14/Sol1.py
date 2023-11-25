from sys import stdin


def main(lines: list[str]):
    n = int(lines[0])
    scores = [3, 7]
    i, j = 0, 1

    while len(scores) < n + 10:
        scores += [int(c) for c in str(scores[i] + scores[j])]
        i += scores[i]+1
        j += scores[j]+1
        i %= len(scores)
        j %= len(scores)

    print(*scores[n:n+10], sep='')


if __name__ == '__main__':
    main(stdin.read().splitlines())
