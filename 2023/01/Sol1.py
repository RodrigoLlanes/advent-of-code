from pycp.aoc import data


def main(lines: list[str]) -> None:
    total = 0
    for line in lines:
        n = ''
        for s in line:
            if s.isdigit():
                n += s
                break
        for s in reversed(line):
            if s.isdigit():
                n += s
                break
        total += int(n)
    print(total)


if __name__ == '__main__':
    main(data())
