import os
import sqlite3
import termcolor as tc
from thing import get_path

path = get_path()
db = sqlite3.connect(os.path.realpath(path))
cursor = db.cursor()


def grab():
    cursor.execute("SELECT name, path FROM warp_points")
    for each in sorted(cursor.fetchall()):
        print(tc.colored(each[0], "yellow"), tc.colored("-->", "cyan"),
              tc.colored(each[1][1::], "blue"))


if __name__ == "__main__":
    grab()
