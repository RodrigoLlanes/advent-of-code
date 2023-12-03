import os
import time
from os import environ, path
from typing import List, Callable
from requests import get
from pathlib import Path
from inspect import stack


def data(day: int = 0, year: int = 0, session: str = None, caller_dir: Path = None) -> List[str]:
    if path is None:
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
        open(input_path, 'w').write(response.text)

    return open(input_path, 'r').read().splitlines()


def run(f: Callable[[List[str]], None]) -> None:
    caller_dir = Path(stack()[1][1]).parent
    tests = [file for file in map(Path, os.listdir(caller_dir)) if file.is_file() and 'test' in file.name]
    for file in tests:
        print(f'{file.name}:')
        t0 = time.time()
        f(open(file, 'r').read().splitlines())
        t1 = time.time()
        print(f'time {t1 - t0}')
        print()

    print(f'input data:')
    t0 = time.time()
    f(data(caller_dir=caller_dir))
    t1 = time.time()
    print(f'time {t1 - t0}')
