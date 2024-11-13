# views/base_view.py
import tkinter as tk
from tkinter import ttk

class BaseView(ttk.Frame):
    """Base class for all views, providing standardized components."""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.pack(fill="both", expand=True, padx=10, pady=10)

    def create_section(self, title):
        frame = ttk.LabelFrame(self, text=title)
        frame.pack(fill="x", padx=10, pady=10)
        return frame

    def create_button(self, parent, text, command):
        button = ttk.Button(parent, text=text, command=command)
        button.pack(fill="x", pady=5)
        return button
