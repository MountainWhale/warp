import os
import sqlite3
import click as click
import termcolor as tc
from functions import get_path, get_shell

path = get_path()
db = sqlite3.connect(os.path.realpath(path))
cursor = db.cursor()
result = cursor.execute("SELECT * FROM warp_points")

warp_points = dict(result.fetchall())


@click.command()
@click.argument("name", default='test')
def warp(name):
    if warp_points.get(name) != None:
        os.chdir(warp_points[name])
        os.system(get_shell())
    else:
        print(tc.colored(name, "red"), tc.colored(
            "warp point does not exist", "red"))
        os.system(get_shell())


if __name__ == "__main__":
    warp()
