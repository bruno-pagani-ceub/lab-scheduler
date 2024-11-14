import tkinter as tk
from tkinter import ttk, messagebox


class FormPopup(tk.Toplevel):
    def __init__(self, parent, title="Form"):
        super().__init__(parent)
        self.title(title)
        self.grab_set()  # Make the popup modal
        self.resizable(False, False)
        self.padx = 10
        self.pady = 10

        # List to hold required fields for validation
        self.required_fields = []

        # Initialize the form widgets
        self.create_widgets()

    def create_widgets(self):
        raise NotImplementedError("Subclasses must implement create_widgets method.")

    def add_label(self, parent, text, row, column=0, columnspan=1, **kwargs):
        label = ttk.Label(parent, text=text)
        label.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=self.padx,
            pady=self.pady,
            **kwargs,
        )
        return label

    def add_section(self, parent, title):
        frame = ttk.LabelFrame(parent, text=title)
        frame.pack(fill="x", padx=self.padx, pady=self.pady)
        return frame

    def add_entry(
        self, parent, label_text, variable, row, column=0, required=False, sticky="E", **kwargs
    ):
        label = ttk.Label(parent, text=f"{label_text}:")
        label.grid(row=row, column=column, sticky=sticky, padx=self.padx, pady=self.pady)
        entry = ttk.Entry(parent, textvariable=variable, **kwargs)
        entry.grid(row=row, column=column + 1, padx=self.padx, pady=self.pady)
        if required:
            self.required_fields.append((label_text, variable))
        return entry

    def add_combobox(
        self,
        parent,
        label_text,
        variable,
        values,
        row,
        column=0,
        required=False,
        **kwargs,
    ):
        label = ttk.Label(parent, text=f"{label_text}:")
        label.grid(row=row, column=column, sticky="E", padx=self.padx, pady=self.pady)
        combobox = ttk.Combobox(parent, textvariable=variable, values=values, **kwargs)
        combobox.grid(row=row, column=column + 1, padx=self.padx, pady=self.pady)
        if required:
            self.required_fields.append((label_text, variable))
        return combobox

    def add_checkbuttons(self, parent, label_text, options, row, column=0, disabled=[], **kwargs):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=column, sticky="NE", padx=self.padx, pady=self.pady)
        frame = ttk.Frame(self)
        frame.grid(
            row=row, column=column + 1, sticky="W", padx=self.padx, pady=self.pady
        )
        variables = {}
        for idx, option in enumerate(options):
            var = tk.BooleanVar()
            state = "disabled" if option in disabled else "normal"
            chk = ttk.Checkbutton(frame, text=option, variable=var, state=state)
            chk.grid(row=idx // 4, column=idx % 4, sticky="W")
            variables[option] = var
        return variables

    def add_listbox(
        self, parent, label_text, row, column=0, height=5, width=30, **kwargs
    ):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=column, sticky="N", padx=self.padx, pady=self.pady)
        listbox = tk.Listbox(self, height=height, width=width, **kwargs)
        listbox.grid(
            row=row, column=column + 1, padx=self.padx, pady=self.pady, sticky="N"
        )
        return listbox

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

    def add_treeview(
        self,
        parent,
        columns_configs: dict,
        row,
        column=0,
        columnspan=1,
        show: str = "headings",
        **kwargs,
    ):
        tree = ttk.Treeview(
            parent, columns=([config["column"] for config in columns_configs]), show=show
        )
        for config in columns_configs:
            tree.heading(config["column"], text=config["text"])
        for config in columns_configs:
            tree.column(config["column"], width=config["width"], anchor=config.get("anchor"))
        for config in columns_configs:
            tree.column(config["column"], width=config["width"])
        tree.grid(
            row=row,
            column=column,
            columnspan=columnspan,
            padx=self.padx,
            pady=self.pady,
            **kwargs,
        )

        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=row, column=len(columns_configs) + 1, sticky="ns")
        return tree

    def check_required_fields(self):
        for field_name, variable in self.required_fields:
            value = variable.get()
            if isinstance(variable, tk.BooleanVar):
                if not value:
                    messagebox.showerror(
                        "Error", f"The field '{field_name}' is required."
                    )
                    return False
            elif not value.strip():
                messagebox.showerror("Error", f"The field '{field_name}' is required.")
                return False
        return True

    def submit(self):
        raise NotImplementedError("Subclasses must implement submit method.")
