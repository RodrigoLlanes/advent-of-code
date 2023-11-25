from sys import stdin
from collections import deque


def main(lines: list[str]):
    n = deque(list(lines[0]))
    counter = 2
    scores = [3, 7]
    numbers = deque(['3', '7'])
    i, j = 0, 1

    while True:
        for c in str(scores[i] + scores[j]):
            scores.append(int(c))
            numbers.append(c)
            counter += 1
            if len(numbers) > len(n):
                numbers.popleft()
                if numbers == n:
                    print(counter - len(n))
                    return
        i += scores[i]+1
        j += scores[j]+1
        i %= len(scores)
        j %= len(scores)

    print(*scores[n:n+10], sep='')


if __name__ == '__main__':
    main(stdin.read().splitlines())
