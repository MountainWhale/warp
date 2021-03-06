import os
import sqlite3
import click
import termcolor as tc
from functions import get_path

path = get_path()
db = sqlite3.connect(os.path.realpath(path))
cursor = db.cursor()


@click.command()
@click.argument('name', default='thing')
def add(name):
    try:
        cursor.execute(
            "INSERT INTO warp_points (name, path) VALUES (?, ?)", (name, os.getcwd()))
        db.commit()
        print(tc.colored(f"Successfully added {name} warp point", "cyan"))
    except:
        print(tc.colored(f"{name} warp point already exists", "red"))


if __name__ == "__main__":
    add()
