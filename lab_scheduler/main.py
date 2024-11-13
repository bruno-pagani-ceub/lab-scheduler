import os
import tkinter as tk

from lab_scheduler.controllers import MainController
from lab_scheduler.database.sql import SQL


def main():
    # Initialize top level widget
    root = tk.Tk()
    root.title("Lab Scheduler")
    root.geometry("300x500")

    # Initialize database connection
    db = SQL(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        password=os.environ.get("MYSQL_PASSWORD", "senha123"),
        database=os.environ.get("MYSQL_DATABASE", "lab_scheduler"),
    )

    # Initialize the controller
    _ = MainController(root, db)

    root.mainloop()


if __name__ == "__main__":
    main()
