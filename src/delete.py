import os
import sqlite3
import click
import termcolor as tc
from functions import get_path

path = get_path()
db = sqlite3.connect(os.path.realpath(path))
cursor = db.cursor()


@click.command()
@click.argument('name')
def remove(name):
    if name != None:
        cursor.execute(
            "DELETE FROM warp_points WHERE name == ?", (name,))
        db.commit()
        print(tc.colored(
            f"Successfully deleted {name} warp point", "red"))


if __name__ == "__main__":
    remove()
