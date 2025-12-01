import aocd
import os
import webbrowser
from datetime import date

today = date.today()
day_num = today.day

# day_num = 1
year_num = 2025


def main():
    directory = os.path.join(f"/Users/anthonyberry/PycharmProjects/advent-of-code-{year_num}/src",
                             f"day{str(day_num).zfill(2)}")
    if not os.path.exists(directory):
        os.mkdir(directory)

    session_cookie = "53616c7465645f5f1458b533cd44d4437091b6146d03d3c82c555cf39878cfa4f9409782478567ab683cf6a669b023fdc9412efeb448bd0795dd0060a03790eb"

    with open(os.path.join(directory, "input.txt"), "w") as file:
        file.write(aocd.get_data(session=session_cookie, day=day_num, year=year_num))

    open(os.path.join(directory, "example.txt"), "a").close()
    open(os.path.join(directory, "p1.py"), "a").close()
    open(os.path.join(directory, "p2.py"), "a").close()

    webbrowser.open(f"https://adventofcode.com/{year_num}/day/{day_num}")
    # webbrowser.open(f"https://adventofcode.com/{year_num}/day/{day_num}/input")


if __name__ == "__main__":
    main()
