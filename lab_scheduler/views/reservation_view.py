import tkinter as tk
from tkinter import ttk, messagebox
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
        self.required_recurrent_search = []
        self.required_single_search = []
        super().__init__(parent, title="Registrar Reserva")

    def create_widgets(self):

        self.single_selected_items = {
            "user": "",
            "date": "",
            "lab": "",
            "timeslot": "",
            "type": "",
        }

        self.recurrent_selected_items = {
            "user": "",
            "weekday": "",
            "lab": "",
            "timeslot": "",
            "type": "",
            "semester": "",
            "year": "",
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
        
        self.required_recurrent_search.clear()

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
        self.required_single_search.append(("Data da reserva", self.date_entry))

        self.valid_date_label = ttk.Label(
            self.dynamic_frame,
            text="",
            background="light grey",
            width=1,
            anchor="center",
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
            state="readonly",
        ).grid(sticky="W")
        self.required_recurrent_search.append((field_name, self.weekday_var))

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
            state="readonly",
        ).grid(sticky="W")
        self.required_recurrent_search.append((field_name, self.semester_var))

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
        self.required_recurrent_search.append((field_name, self.year_var))

        self.generate_lab_selection(3, 0, self.recurrent_selected_items)
        self.lab_var.grid(sticky="W")

        self.add_button(
            self.dynamic_frame,
            text="Buscar horários",
            command=self.search_timeslots_weekday,
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
        self.required_recurrent_search.append(("Laboratório", self.lab_var))
        self.required_single_search.append(("Laboratório", self.lab_var))

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
                {"column": 2, "text": "Fim", "width": 100, "anchor": "center"},
            ],
            row=row,
            column=column,
            columnspan=1,
        )
        self.timeslot_var.column(0, stretch=False)
        self.timeslot_var.bind(
            "<<TreeviewSelect>>",
            lambda event: self.update_selected_item(
                event, self.timeslot_var, "timeslot", type
            ),
        )

    def search_timeslots(self, date, lab):
        self.check_required_fields(self.required_single_search)
        for _ in self.timeslot_var.get_children():
            self.timeslot_var.delete(_)
        available_timeslots = self.controller.get_available_timeslots(date, lab)
        converted_times = [
            self.controller.convert(line) for line in available_timeslots
        ]
        self.timeslot_var.delete(*self.timeslot_var.get_children())
        for converted_time in converted_times:
            self.timeslot_var.insert("", "end", values=tuple(converted_time.values()))


    def search_timeslots_weekday(self):
        self.check_required_fields(self.required_recurrent_search)
        weekday = self.recurrent_selected_items["weekday"] = self.weekday_var.get()
        semester = self.recurrent_selected_items["semester"] = self.semester_var.get()
        year = self.recurrent_selected_items["year"] = self.year_var.get()
        # lab = self.lab_var.selection()[0]
        if self.timeslot_var.get_children():
            for i in self.timeslot_var.get_children():
                self.timeslot_var.delete(i)
        weekday_number = static.SQL_WEEKDAYS_NUMBER[weekday]
        lab_id = self.recurrent_selected_items["lab"]
        timeslots = self.controller.get_timeslots_weekday(
            lab_id, weekday_number, semester, year
        )
        converted_timeslots = []
        for i, timeslot in enumerate(timeslots):
            converted_timeslot = {
                "id": i,
                **timeslot,
            }
            converted_timeslots.append(self.controller.convert(converted_timeslot))
                     
        self.timeslot_var.delete(*self.timeslot_var.get_children())
        for converted_time in converted_timeslots:
            self.timeslot_var.insert("", "end", values=tuple(converted_time.values()))

    def update_selected_item(self, event, treeview, target, list):
        selected_item = treeview.selection()
        if not selected_item:
            return
        item_data = treeview.item(selected_item[0], "values")
        list[target] = item_data[0]
        self.recurrent_selected_items[target] = list[target]
        self.single_selected_items[target] = list[target]

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
        required_fields = self.required_single_search \
            + [
                ("Usuário", self.user_var),
                ("Horário", self.timeslot_var),
                ("Título da reserva", self.type_var),
            ]
        self.check_required_fields(required_fields)
        self.single_selected_items["type"] = self.type_var.get()
        for key, value in self.single_selected_items.items():
            if value == "":
                messagebox.showerror("Error", f"The field '{key}' is required.")
                pass
        self.controller.submit_single_reservation(self.single_selected_items)
        messagebox.showinfo("Sucesso", "Reserva registrada com sucesso!")
        for row in self.timeslot_var.get_children():
            self.timeslot_var.delete(row)

    def submit_recurrent_reservation(self):
        required_fields = self.required_recurrent_search \
            + [
                ("Usuário", self.user_var),
                ("Horário", self.timeslot_var),
                ("Título da reserva", self.type_var),
            ]
        self.check_required_fields(required_fields)
        values = [
            self.recurrent_selected_items["user"],
            static.SQL_WEEKDAYS_NUMBER[self.weekday_var.get()],
            self.recurrent_selected_items["lab"],
            self.recurrent_selected_items["timeslot"],
            self.type_var.get(),
            self.recurrent_selected_items["semester"],
            self.year_var.get(),
        ]
        self.recurrent_selected_items = dict(
            zip(self.recurrent_selected_items.keys(), values)
        )
        success_check = self.controller.submit_recurrent_reservation(self.recurrent_selected_items)
        if success_check:
            messagebox.showinfo("Sucesso", "Reserva registrada com sucesso!")
            for row in self.timeslot_var.get_children():
                self.timeslot_var.delete(row)
        else:
            messagebox.showinfo("Erro", "Esse horário já está reservado nesse dia da semana para esse laboratório!")

    def submit_user(self):
        user_ident = self.user_var.get()
        search_result = self.controller.get_user_data(user_ident)
        if search_result == "":
            self.result_label.config(text="Nenhum usuário encontrado!")
        else:
            self.result_label.config(
                text=f"{search_result[0]['nm_usuario']} - {search_result[0]['ds_tipo_usuario']}"
            )
            self.single_selected_items["user"] = search_result[0]["id"]
            self.recurrent_selected_items["user"] = search_result[0]["id"]


class ViewReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Gerenciar Reservas")

    def create_widgets(self):

        self.grid_columnconfigure([0, 1, 2, 3, 4, 5], weight=1)
        self.grid_rowconfigure([0, 1, 2, 3, 4, 5], weight=1)

        self.add_label(
            self, "Buscar por:", row=0, column=0, columnspan=5
        )

        self.reservation_type = tk.StringVar()
        user_radio = ttk.Radiobutton(
            self,
            text="Nome de usuário",
            value="Nome",
            variable=self.reservation_type
        )
        user_radio.grid(row=1, column=0, padx=5, pady=5, sticky="we")

        id_radio = ttk.Radiobutton(
            self,
            text="ID de usuário",
            value="ID",
            variable=self.reservation_type
        )
        id_radio.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        lab_radio = ttk.Radiobutton(
            self,
            text="Sala",
            value="Sala",
            variable=self.reservation_type
        )
        lab_radio.grid(row=1, column=2, padx=5, pady=5, sticky="we")

        block_radio = ttk.Radiobutton(
            self,
            text="Bloco",
            value="Bloco",
            variable=self.reservation_type
        )
        block_radio.grid(row=1, column=3, padx=5, pady=5, sticky="we")

        date_radio = ttk.Radiobutton(
            self,
            text="Data",
            value="Data",
            variable=self.reservation_type
        )
        date_radio.grid(row=1, column=4, padx=5, pady=5, sticky="we")

        self.search_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Termo de busca",
            variable=self.search_var,
            row=2,
            column=0,
            sticky="W"
        )

        self.add_button(
            self,
            text="Buscar",
            command=lambda: self.filter_treeview(self.reservation_type, self.search_var),
            row=3,
            column=1,
        )

        self.add_button(
            self,
            text="Resetar",
            command=lambda: self.populate_tree(),
            row=3,
            column=2,
        )

        self.item_list = self.controller.search_all()
 
        columns_configs = [
            {"column": header, "text": header, "width": 100, "anchor": "center"}
            for header in self.item_list[0].keys()
        ]

        
        self.tree = self.add_treeview(
            parent=self,
            columns_configs=columns_configs,
            row=4,
            column=0,
            columnspan=5,
        )
        self.tree.column("id", width=0, stretch=False)

        self.populate_tree()

    def populate_tree(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for line in self.item_list:
            self.tree.insert("", "end", values=(tuple(col for col in line.values())))
    
    def filter_treeview(self, type, search):
        if search == "":
            pass

        query = self.search_var.get().lower()
        selected_column = self.reservation_type.get()

        filtered_data = [
            item for item in self.item_list if query == str(item[selected_column]).lower()
        ]

        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in filtered_data:
            self.tree.insert("", "end", values=(tuple(col for col in item.values())))