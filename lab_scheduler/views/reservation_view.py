import tkinter as tk
from tkinter import NSEW, ttk, messagebox
from datetime import datetime
from lab_scheduler.views.templates.form_popup_template import FormPopup
from lab_scheduler import static


class ReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Reservas")

    def create_widgets(self):
        main_section = self.add_section(self, "Opções")

        self.add_button(
            main_section,
            "Cadastrar reserva  ",
            command=self.controller.reserve_lab,
            row=1,
            sticky="w",
        )
        self.add_button(
            main_section,
            "Visualizar reservas",
            command=self.controller.manage_reservations,
            row=2,
            sticky="w",
        )


class LabReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Registrar Reserva")

    def create_widgets(self):

        self.single_selected_items = {
            "user": "",
            "date": "",
            "lab": "",
            "timeslot": "",
            "type": ""
        }

        self.recurrent_selected_items = {
            "user": "",
            "weekday": "",
            "lab": "",
            "timeslot": "",
            "type": "",
            "semester": "",
            "year": ""
        }

        self.user_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Registro do Usuário",
            variable=self.user_var,
            row=1,
            column=0,
            required=True,
            sticky="W",
        )

        self.add_button(
            self, text="Buscar", command=self.submit_user, row=1, column=2, columnspan=1
        )

        self.result_label = ttk.Label(
            self, text="", background="light grey", width=40, anchor="center"
        )
        self.result_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.type_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Título da reserva",
            variable=self.type_var,
            row=3,
            column=0,
            required=True,
            sticky="W",
        )

        self.reservation_type = tk.StringVar(value="single")
        single_radio = ttk.Radiobutton(
            self,
            text="Reserva única",
            value="single",
            variable=self.reservation_type,
            command=self.update_fields,
        )
        single_radio.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        recurrent_radio = ttk.Radiobutton(
            self,
            text="Reserva recorrente",
            value="recurrent",
            variable=self.reservation_type,
            command=self.update_fields,
        )
        recurrent_radio.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.dynamic_frame = ttk.Frame(self)
        self.dynamic_frame.grid(
            row=5, column=0, columnspan=4, padx=10, pady=10, sticky="W"
        )

        self.update_fields()

    def update_fields(self):
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()

        if self.reservation_type.get() == "single":
            self.load_single_reservation_fields()
        else:
            self.load_recurrent_reservation_fields()

    def load_single_reservation_fields(self):

        self.date = tk.StringVar()
        self.date.trace_add("write", self.validate_date)
        self.date_entry = self.add_entry(
            self.dynamic_frame,
            label_text="Data da reserva (dd/mm/aaaa)",
            variable=self.date,
            row=1,
            column=0,
            required=True,
            sticky="W",
        )
        
        self.valid_date_label = ttk.Label(
            self.dynamic_frame, text="", background="light grey", width=1, anchor="center"
        )
        self.valid_date_label.grid(row=1, column=2, padx=5, pady=5, sticky="w")

        self.generate_lab_selection(2, 0, self.single_selected_items)

        self.add_button(
            self.dynamic_frame,
            text="Buscar horários",
            command=lambda: self.search_timeslots(
                self.date.get(), self.single_selected_items["lab"]
            ),
            row=3,
            column=0,
        )

        self.generate_timeslot_selection(2, 1, self.single_selected_items)

        self.add_button(
            self.dynamic_frame,
            text="Confirmar reserva",
            command=self.submit_single_reservation,
            row=5,
            column=1,
        )

    def load_recurrent_reservation_fields(self):

        self.weekday_var = tk.StringVar()
        field_name = "Dia da semana"
        self.required_fields.append((field_name, self.weekday_var))
        self.add_combobox(
            parent=self.dynamic_frame,
            label_text=field_name,
            variable=self.weekday_var,
            values=list(static.WEEKDAYS),
            row=0,
            column=0,
            required=True,
            state="readonly"
        ).grid(sticky="W")

        self.semester_var = tk.StringVar()
        field_name = "Semestre"
        self.add_combobox(
            parent=self.dynamic_frame,
            label_text=field_name,
            variable=self.semester_var,
            values=list(static.SEMESTERS_INFO.keys()),
            row=1,
            column=0,
            required=True,
            state="readonly"
        ).grid(sticky="W")

        current_year = datetime.now().year
        self.year_var = tk.StringVar(value=str(current_year))
        field_name = "Ano"
        self.add_entry(
            parent=self.dynamic_frame,
            label_text=field_name,
            variable=self.year_var,
            row=2,
            column=0,
            required=True,
        )

        self.generate_lab_selection(3, 0, self.recurrent_selected_items)
        self.lab_var.grid(sticky="W")

        self.add_button(
            self.dynamic_frame,
            text="Buscar horários",
            command=lambda: self.search_timeslots_weekday(self.weekday_var.get(), self.semester_var.get(), self.year_var.get()),
            row=4,
            column=0,
        )

        self.generate_timeslot_selection(3, 1, self.recurrent_selected_items)
        self.timeslot_var.grid(sticky="W")

        self.add_button(
            self.dynamic_frame,
            text="Confirmar reserva",
            command=self.submit_recurrent_reservation,
            row=5,
            column=1,
        )

    def generate_lab_selection(self, row, column, type):
        lab_list = self.controller.retrieve_lab()

        columns_configs = [
            {"column": col, "text": att, "width": 70, "anchor": "w"}
            for att, col in lab_list[0].items()
        ]
        
        self.lab_var = self.add_treeview(
            self.dynamic_frame,
            columns_configs=columns_configs,
            row=row,
            column=column,
            columnspan=1,
        )
        self.lab_var.column(0, width=0, stretch=False)

        for line in lab_list:
            self.lab_var.insert("", "end", values=(tuple(col for col in line.values())))

        self.lab_var.bind(
            "<<TreeviewSelect>>",
            lambda event: self.update_selected_item(event, self.lab_var, "lab", type),
        )

    def generate_timeslot_selection(self, row, column, type):
        self.timeslot_var = self.add_treeview(
            parent=self.dynamic_frame,
            columns_configs=[
                {"column": 0, "text": "id", "width": 0, "anchor": "center"},
                {"column": 1, "text": "Início", "width": 100, "anchor": "center"},
                {"column": 2, "text": "Fim", "width": 100, "anchor": "center"}
            ],
            row=row,
            column=column,
            columnspan=1
        )
        self.timeslot_var.column(0, stretch=False)
        self.timeslot_var.bind(
            "<<TreeviewSelect>>",
            lambda event: self.update_selected_item(
                event, self.timeslot_var, "timeslot", type
            ),
        )

    def search_timeslots(self, date, lab):
        available_timeslots = self.controller.get_available_timeslots(date, lab)
        converted_times = [self.controller.convert(line) for line in available_timeslots]
        self.timeslot_var.delete(*self.timeslot_var.get_children())
        for converted_time in converted_times:
            self.timeslot_var.insert("", "end", values=tuple(converted_time.values()))

    def search_timeslots_weekday(self, weekday, semester, year):
        self.recurrent_selected_items["semester"] = self.semester_var.get()
        weekday_number = static.SQL_WEEKDAYS_NUMBER[weekday]
        timeslots = self.controller.get_timeslots_weekday(weekday_number, semester, year)
        converted_timeslots = [self.controller.convert(line) for line in timeslots]
        self.timeslot_var.delete(*self.timeslot_var.get_children())
        for converted_time in converted_timeslots:
            self.timeslot_var.insert("", "end", values=tuple(converted_time.values()))

    def update_selected_item(self, event, treeview, target, list):
        selected_item = treeview.selection()
        if not selected_item:
            return
        item_data = treeview.item(selected_item[0], "values")
        list[target] = item_data[0]
        print(f"Selected {target} updated: {list[target]}")

    def validate_date(self, *args):
        date_value = self.date.get()
        if len(date_value) == 10:
            try:
                parsed_date = datetime.strptime(date_value, "%d/%m/%Y")
                self.date.set(parsed_date.strftime("%d/%m/%Y"))
                self.valid_date_label.config(text="✓")
                self.single_selected_items["date"] = self.date.get()
            except ValueError:
                pass

    def submit_single_reservation(self):
        self.single_selected_items["type"] = self.type_var.get()
        for key, value in self.single_selected_items.items():
            if value == "":
                messagebox.showerror("Error", f"The field '{key}' is required.")
                pass
        self.controller.submit_single_reservation(self.single_selected_items)
        
    def submit_recurrent_reservation(self):
        values = [self.recurrent_selected_items["user"], static.SQL_WEEKDAYS_NUMBER[self.weekday_var.get()], self.recurrent_selected_items["lab"],
                  self.recurrent_selected_items["timeslot"], self.type_var.get(), self.recurrent_selected_items["semester"], self.year_var.get()]
        self.recurrent_selected_items = dict(zip(self.recurrent_selected_items.keys(), values))
        self.controller.submit_recurrent_reservation(self.recurrent_selected_items)

    def submit_user(self):
        user_ident = self.user_var.get()
        search_result = self.controller.get_user_data(user_ident)
        if search_result == "":
            self.result_label.config(text="Nenhum usuário encontrado!")
        else:
            self.result_label.config(
                text=f"{search_result[0]['nm_usuario']} - {search_result[0]['ds_tipo_usuario']}"
            )
            self.single_selected_items["user"] = search_result[0]['id']
            self.recurrent_selected_items["user"] = search_result[0]['id']

class UpdateReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Atualizar Reserva")

    def create_widgets(self):
        pass
