import os
import time
from os import environ, path
from typing import List, Callable, TypeVar, Generic
from requests import get
from pathlib import Path
from inspect import stack

T = TypeVar("T")


def data(day: int = 0, year: int = 0, session: str = None, caller_dir: Path = None) -> List[str]:
    if caller_dir is None:
        caller_dir = Path(stack()[1][1]).parent
    input_path = path.join(caller_dir, 'input')
    if not path.isfile(input_path):
        if day == 0:
            day = int(caller_dir.name)
        if year == 0:
            year = int(caller_dir.parent.name)
        if session is None:
            session = environ['aoc_session']

        response = get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session})
        with open(input_path, 'w') as out:
            out.write(response.text)

    with open(input_path, 'r') as inp:
        lines = open(input_path, 'r').read().splitlines()
    return lines


def timer(lines: List[str], f: Callable[[List[T]], None], parser: Callable[[str], T] = None):
    lines = lines if parser is None else list(map(parser, lines))
    t = time.time()
    f(lines)
    return time.time() - t


def run(f: Callable[[List[str]], None], parser: Callable[[str], T] = None) -> None:
    caller_dir = Path(stack()[1][1]).parent
    tests = [file for file in map(Path, os.listdir(caller_dir)) if file.is_file() and 'test' in file.name]
    for file in tests:
        print(f'{file.name}:')
        t = timer(open(file, 'r').read().splitlines(), f, parser)
        print(f'time {t}')
        print()

    print(f'input data:')
    t = timer(data(caller_dir=caller_dir), f, parser)
    print(f'time {t}')
