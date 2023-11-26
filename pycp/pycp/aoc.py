from os import environ, path
from typing import List
from requests import get
from pathlib import Path
from inspect import stack


def data(day: int = 0, year: int = 0, session: str = None) -> List[str]:
    caller_path = Path(stack()[1][1])
    input_path = path.join(caller_path.parent, 'input')
    if not path.isfile(input_path):
        if day == 0:
            day = int(caller_path.parent.name)
        if year == 0:
            year = int(caller_path.parent.parent.name)
        if session is None:
            session = environ['aoc_session']

        response = get(f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': session})
        open(input_path, 'w').write(response.text)

    return open(input_path, 'r').read().splitlines()
