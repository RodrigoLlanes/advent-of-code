from pycp.aoc import data

NUMBERS = {num: str(i + 1) for i, num in enumerate('one, two, three, four, five, six, seven, eight, nine'.split(', '))}


def first(line, numbers):
        index = len(line) + 1
        number = None
        for num, value in numbers.items():
            i = line.find(num)
            if i >= 0 and i < index:
                index = i
                number = value
        for i, s in enumerate(line):
            if s.isdigit():
                if i < index:
                    number = s
                break
        return number


def main(lines: list[str]) -> None:
    su = 0
    for line in lines:
        n = first(line, NUMBERS)
        reversed_nums = {''.join(reversed(k)): v for k, v in NUMBERS.items()}
        n += first(''.join(reversed(line)), reversed_nums)
        su += int(n)
    print(su)


if __name__ == '__main__':
    main(data())
