import inspect
import os
from pathlib import Path


def get_importing_file():
    stack = inspect.stack()
    for frame in stack:
        if frame.filename != __file__:
            return frame.filename


def get_input(day: int) -> str:
    file = get_importing_file()
    year = Path(file).parts[-3]
    os.makedirs(os.path.join(os.path.dirname(file), "../inputs"), exist_ok=True)
    path = os.path.join(os.path.dirname(file), f"../inputs/day {day}.txt")

    if not os.path.exists(path):
        import requests

        with open(os.path.join(os.path.dirname(file), "../../cookie.txt")) as f:
            cookies = {"session": f.read().strip()}
        response = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies
        )
        if not response.ok:
            raise RuntimeError("not ok")
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()
