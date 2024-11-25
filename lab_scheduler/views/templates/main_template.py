import tkinter as tk
from tkinter import ttk

class MainTemplate(ttk.Frame):
    def __init__(self, parent, title="LabScheduler"):
        super().__init__(parent)
        self.title = title
        self.padx = 10
        self.pady = 10
        self.pack(fill="both", expand=True, padx=self.padx, pady=self.pady)
        
        self.create_widgets()

    def add_section(self, parent, title):
        frame = ttk.LabelFrame(parent, text=title)
        frame.pack(fill="x", padx=self.padx, pady=self.pady)
        return frame

    def add_button(self, parent, text, command, row, column=0, columnspan=1, **kwargs):
        button = ttk.Button(parent, text=text, command=command)
        button.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=self.padx,
            pady=self.pady,
            **kwargs,
        )
        return button

    def create_widgets(self):
        raise NotImplementedError("Subclasses must implement create_widgets method.")
