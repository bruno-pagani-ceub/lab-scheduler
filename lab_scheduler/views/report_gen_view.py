import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

from lab_scheduler.views.templates.form_popup_template import FormPopup


class ScheduleGenerationView(FormPopup):

    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Cronograma Semanal")

    def create_widgets(self):
        self.add_label(self, "Cronograma Semanal", row=0, column=0, columnspan=2)
        
        self.labs = self.controller.get_labs()

        self.lab_var = tk.StringVar()
        field_name = "Laboratório"
        self.required_fields.append((field_name, self.lab_var))
        self.add_combobox(
            parent=self,
            label_text=field_name,
            variable=self.lab_var,
            values=list(self.labs.keys()),
            row=1,
            required=True,
        )
        
        self.valid_date_label = ttk.Label(
            self,
            text="",
            background="light grey",
            width=1,
            anchor="center",
        )
        self.valid_date_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.date_var = tk.StringVar()
        self.date_var.trace_add("write", self.validate_date)
        self.date_entry = self.add_entry(
            self,
            label_text="Data da reserva (dd/mm/aaaa)",
            variable=self.date_var,
            row=2,
            required=True,
            sticky="W",
        )
        self.required_fields.append(("Data da reserva", self.date_entry))

        self.add_button(
            self,
            text="Gerar",
            command=self.submit,
            row=3,
        )
        
    def validate_date(self, *args):
        date_value = self.date_var.get()
        if len(date_value) == 10:
            try:
                parsed_date = datetime.strptime(date_value, "%d/%m/%Y")
                self.date_var.set(parsed_date.strftime("%d/%m/%Y"))
                self.valid_date_label.config(text="✓")
            except ValueError:
                pass
            
    def submit(self):
        if not self.check_required_fields():
            return

        date = self.date_var.get()
        lab = self.labs[self.lab_var.get()]

        try:
            fpath = self.controller.generate_schedule(lab, date)
            messagebox.showinfo("Sucesso", f"Cronograma gerado com sucesso e salvo em {fpath}")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao gerar cronograma semanal: {e}")