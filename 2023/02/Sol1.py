from pycp.aoc import data


def main(lines: list[str]) -> None:
    possible = 0
    sets = {'red': 12, 'green': 13, 'blue': 14}
    for line in lines:
        game, subsets = line.split(': ')
        for subset in subsets.split('; '):
            curr = {}
            for s in subset.split(', '):
                n, color = s.strip().split()
                curr[color] = int(n)
            if any(sets[c] < v for c, v in curr.items()):
                break
        else:
            possible += int(game.split()[1])
    print(possible)


if __name__ == '__main__':
    main(data())
