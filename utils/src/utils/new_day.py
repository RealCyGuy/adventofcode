import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "year", type=int, nargs="?", default=2024, help="The year to create the day in"
    )
    parser.add_argument("day", type=int, nargs="?", help="The day to create")
    args = parser.parse_args()

    day = args.day
    year = args.year

    if not os.path.exists(os.path.join(os.path.dirname(__file__), f"../../../{year}")):
        print(f"Folder with year {year} does not exist. Create it first!")
        return
    if day is None:
        for x in range(1, 33):
            path = os.path.join(
                os.path.dirname(__file__), f"../../../{year}/day {x:02d}"
            )
            if not os.path.exists(path):
                day = x
                break
    path = os.path.join(os.path.dirname(__file__), f"../../../{year}/day {day:02d}")
    os.mkdir(path)
    for part in range(1, 3):
        with open(os.path.join(path, f"part {part}.py"), "w") as f:
            f.write(f"from utils.api import get_input\n\ninp = get_input({day})\n")
    print(f"Created day {day}! Good luck.")


if __name__ == "__main__":
    main()
