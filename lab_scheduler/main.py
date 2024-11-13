import os
import tkinter as tk

from controllers import MainController
from database.setup import ensure_tables
from database.sql import SQL


def main():
    root = tk.Tk()
    root.title("Lab Scheduler")
    root.geometry("300x500")

    # Initialize connection
    db = SQL(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        password=os.environ.get("MYSQL_PASSWORD", "senha123"),
        database=os.environ.get("MYSQL_DATABASE", "lab_scheduler"),
    )
    ensure_tables(db=db)

    # Initialize the controller
    _ = MainController(root, db)

    root.mainloop()


if __name__ == "__main__":
    main()
