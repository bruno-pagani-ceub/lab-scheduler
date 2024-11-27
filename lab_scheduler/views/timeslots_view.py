import tkinter as tk
from datetime import datetime
from itertools import product
from tkinter import messagebox

from lab_scheduler.utils import helper, validate
from lab_scheduler import static
from lab_scheduler.views.templates.form_popup_template import FormPopup


class TimeSlotsView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Horários do Semestre")

    def create_widgets(self):
        registration_section = self.add_section(
            self, "Cadastro de Horários para o Semestre"
        )

        self.add_button(
            parent=registration_section,
            text="Cadastar Horários",
            command=self.open_time_slot_registration,
            row=1,
            column=0,
            columnspan=4,
        )

        management_section = self.add_section(self, "Gerenciamento dos Horários")

        self.semester_var = tk.StringVar()
        field_name = "Semestre"
        self.required_fields.append((field_name, self.semester_var))
        self.add_combobox(
            parent=management_section,
            label_text=field_name,
            variable=self.semester_var,
            values=list(static.SEMESTERS_INFO.keys()),
            row=2,
            column=0,
            required=True,
            state="readonly",
        )

        current_year = datetime.now().year
        self.year_var = tk.StringVar(value=str(current_year))
        field_name = "Ano"
        self.required_fields.append((field_name, self.year_var))
        self.add_entry(
            parent=management_section,
            label_text=field_name,
            variable=self.year_var,
            row=2,
            column=2,
            required=True,
        )

        self.add_button(
            parent=management_section,
            text="Carregar Horários",
            command=self.load_time_slots,
            row=3,
            column=0,
            columnspan=4,
        )

        columns = ["Horários"] + static.WEEKDAYS
        columns_configs = [
            {"column": col, "text": col, "width": 100, "anchor": "center"}
            for col in columns
        ]
        self.tree = self.add_treeview(
            parent=management_section,
            columns_configs=columns_configs,
            row=4,
            column=0,
            columnspan=4,
        )

        self.add_button(
            parent=management_section,
            text="Modificar/Remover Horário",
            command=self.update_time_slot,
            row=5,
            column=0,
            columnspan=2,
        )

        self.add_button(
            parent=management_section,
            text="Fechar",
            command=self.destroy,
            row=5,
            column=2,
            columnspan=2,
        )

    def load_time_slots(self):
        """Load time slots for the selected semester and year."""
        if not self.check_required_fields():
            return

        self.selected_semester = self.semester_var.get()
        self.selected_year = self.year_var.get()

        if not validate.validade_timeslot_year(self.selected_year):
            messagebox.showerror("Erro", "Ano inválido.")
            return

        try:
            time_slots = self.controller.get_time_slots(
                self.selected_semester, self.selected_year
            )
            if not time_slots:
                messagebox.showerror(
                    "Erro", "Não há horários cadastrados para esse semestre"
                )

            table_data = self.format_time_slots_table(time_slots)
            self.display_time_slots(table_data)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar horários: {e}")
            print(e)

    def format_time_slots_table(self, data):
        time_slots = {}
        for record in data:
            ds_dia_semana = record["ds_dia_semana"]
            hr_ini = record["hr_ini"]
            hr_fim = record["hr_fim"]
            time_slot = f"{hr_ini} - {hr_fim}"

            if time_slot not in time_slots:
                time_slots[time_slot] = set()
            time_slots[time_slot].add(ds_dia_semana)

        output = []
        for time_slot in sorted(time_slots.keys()):
            slot_dict = {"Horários": time_slot}
            days = time_slots[time_slot]
            for day in static.WEEKDAYS:
                slot_dict[day] = "X" if day in days else ""
            output.append(slot_dict)

        return output

    def display_time_slots(self, table_data):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for line in table_data:
            self.tree.insert(
                "",
                "end",
                values=(tuple(col for col in line.values())),
            )

    def get_selected_line(self):
        item_id = self.tree.focus()
        values = self.tree.item(item_id)["values"]
        if not values:
            messagebox.showwarning("Aviso", "Nenhum horário selecionado.")
            return None
        return values

    def get_selected_values_from_line(self, values: list):
        start_time, end_time = values.pop(0).split(" - ")
        weekdays = [day for i, day in enumerate(static.WEEKDAYS) if values[i]]
        return start_time, end_time, weekdays

    def update_time_slot(self):
        selected_time_slot = self.get_selected_line()
        if selected_time_slot is None:
            return
        start_time, end_time, weekdays = self.get_selected_values_from_line(
            selected_time_slot
        )
        self.controller.update_delete_time_slots(
            start_time, end_time, weekdays, self.selected_semester, self.selected_year
        )

    # def delete_time_slot(self):
    #     """Delete the selected time slot."""
    #     ts_id = self.get_selected_line()
    #     if ts_id is None:
    #         return
    #     confirm = messagebox.askyesno(
    #         "Confirmação", "Tem certeza de que deseja excluir o horário selecionado?"
    #     )
    #     if confirm:
    #         try:
    #             self.controller.delete_time_slot(ts_id)
    #             messagebox.showinfo("Sucesso", "Horário excluído com sucesso.")
    #             # Refresh the time slots display
    #             self.load_time_slots()
    #         except Exception as e:
    #             messagebox.showerror("Erro", f"Falha ao excluir horário: {e}")

    def open_time_slot_registration(self):
        self.controller.register_time_slots()


class TimeSlotsRegistrationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Horários do Semestre")

    def create_widgets(self):
        self.add_label(
            self, "Cadastrar Horários do Semestre", row=0, column=0, columnspan=4
        )

        self.semester_var = tk.StringVar()
        self.add_combobox(
            self,
            label_text="Semestre",
            variable=self.semester_var,
            values=list(static.SEMESTERS_INFO.keys()),
            row=1,
            column=0,
            required=True,
            state="readonly",
        )

        current_year = datetime.now().year
        self.year_var = tk.StringVar(value=str(current_year))
        self.add_entry(
            self,
            label_text="Ano",
            variable=self.year_var,
            row=1,
            column=2,
            required=True,
        )

        self.weekday_vars = self.add_checkbuttons(
            self,
            label_text="Dias da Semana",
            options=static.WEEKDAYS,
            row=2,
            column=0,
        )

        self.time_slots_listbox = self.add_listbox(
            self, label_text="Horários", row=3, column=0, height=5, width=30
        )

        self.start_time_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Hora Início (HH:MM)",
            variable=self.start_time_var,
            row=3,
            column=2,
        )

        self.end_time_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Hora Fim (HH:MM)",
            variable=self.end_time_var,
            row=4,
            column=2,
        )

        self.add_button(
            self,
            text="Adicionar Horário",
            command=self.add_time_slot,
            row=5,
            column=3,
            sticky="E",
        )

        self.add_button(
            self,
            text="Remover Horário",
            command=self.remove_time_slot,
            row=5,
            column=1,
            sticky="W",
        )

        self.add_button(
            self, text="Salvar", command=self.submit, row=6, column=0, columnspan=4
        )

    def add_time_slot(self):
        start_time = self.start_time_var.get().strip()
        end_time = self.end_time_var.get().strip()

        start_dt, err = validate.validate_time_format(start_time)
        if err:
            messagebox.showerror("Erro", err)
            return
        end_dt, err = validate.validate_time_format(end_time)
        if err:
            messagebox.showerror("Erro", err)
            return

        if validate.valid_time_slot(start_dt, end_dt):
            messagebox.showerror("Erro", "Hora Fim deve ser após a Hora Início.")
            return

        if validate.new_slot_overlaps(start_dt, end_dt, self.time_slots):
            messagebox.showerror("Erro", "Horário sobreposto com um existente.")
            return

        self.time_slots.append((start_dt, end_dt))
        helper.sort_list_of_tuples_by_first_value(self.time_slots)
        self.update_time_slots_listbox()

        self.start_time_var.set("")
        self.end_time_var.set("")

    def remove_time_slot(self):
        selected_indices = self.time_slots_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Aviso", "Nenhum horário selecionado para remover")
            return
        index = selected_indices[0]
        del self.time_slots[index]
        self.update_time_slots_listbox()

    def update_time_slots_listbox(self):
        self.time_slots_listbox.delete(0, tk.END)
        for slot in self.time_slots:
            slot_str = f"{slot[0].strftime('%H:%M')} - {slot[1].strftime('%H:%M')}"
            self.time_slots_listbox.insert(tk.END, slot_str)

    def submit(self):
        if not self.check_required_fields():
            return

        semester = self.semester_var.get()
        year = self.year_var.get()

        if not validate.validade_timeslot_year:
            messagebox.showerror("Erro", "Ano inválido.")
            return

        if not self.time_slots:
            messagebox.showerror("Erro", "Adicione pelo menos um horário.")
            return

        selected_weekdays = [day for day, var in self.weekday_vars.items() if var.get()]
        if not selected_weekdays:
            messagebox.showerror("Erro", "Selecione pelo menos um dia da semana.")
            return

        time_slots = [
            (slot[0].strftime("%H:%M"), slot[1].strftime("%H:%M"))
            for slot in self.time_slots
        ]
        lines_to_save = [
            (start, end, weekday, semester, year)
            for (start, end), weekday in product(time_slots, selected_weekdays)
        ]
        try:
            self.controller.save_time_slots(lines_to_save)
            messagebox.showinfo("Sucesso", "Horários salvos com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar horários: {e}")
            print(e)


class UpdateTimeSlotView(FormPopup):
    def __init__(
        self, parent, controller, start_time, end_time, weekdays, semester, year
    ):
        self.controller = controller
        self.start_time = start_time
        self.end_time = end_time
        self.weekdays = weekdays
        self.semester = semester
        self.year = year
        super().__init__(parent, title="Horários do Semestre")

    def create_widgets(self):
        self.add_label(self, "Editar Horário", row=0, column=0, columnspan=4)

        self.semester_var = tk.StringVar(value=self.semester)
        self.add_entry(
            self,
            label_text="Semestre",
            variable=self.semester_var,
            row=1,
            column=1,
            required=True,
            state="readonly",
        )

        self.year_var = tk.StringVar(value=str(self.year))
        self.add_entry(
            self,
            label_text="Ano",
            variable=self.year_var,
            row=1,
            column=3,
            required=True,
            state="readonly",
        )

        self.weekday_vars = self.add_checkbuttons(
            self,
            label_text="Dias da Semana",
            options=static.WEEKDAYS,
            row=2,
            column=1,
            disabled=[day for day in static.WEEKDAYS if day not in self.weekdays],
        )

        self.start_time_var = tk.StringVar()
        self.start_time_var.set(self.start_time)
        self.add_entry(
            self,
            label_text="Hora Início (HH:MM)",
            variable=self.start_time_var,
            row=3,
            column=1,
            sticky="W",
        )

        self.end_time_var = tk.StringVar()
        self.end_time_var.set(self.end_time)
        self.add_entry(
            self,
            label_text="Hora Fim (HH:MM)",
            variable=self.end_time_var,
            row=3,
            column=3,
            sticky="E",
        )

        self.add_button(
            self,
            text="Atualizar Horários",
            command=self.submit_update,
            row=4,
            column=1,
            # sticky="E",
        )

        self.add_button(
            self,
            text="Remover Horário",
            command=self.submit_remove,
            row=4,
            column=2,
            # sticky="W",
        )

    def submit_update(self):
        new_timeslots, err = self.process_selected_values()
        old_timeslots = [
            (self.start_time, self.end_time, weekday, self.semester, self.year)
            for weekday, var in self.weekday_vars.items() if var.get()
        ]
        if err:
            messagebox.showerror("Erro", err)
            return
        try:
            self.controller.update_time_slot(old_timeslots, new_timeslots)
            messagebox.showinfo("Sucesso", "Horário alterado com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao alterar horários: {e}")

    def submit_remove(self):
        lines, err = self.process_selected_values()
        if err:
            messagebox.showerror("Erro", err)
            return
        try:
            self.controller.remove_time_slot(lines)
            messagebox.showinfo("Sucesso", "Horário excluído com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao excluir horários: {e}")

    def process_selected_values(self):
        start_time, end_time, semester, year, weekdays = self.get_selected_vars()

        _, err = validate.validate_time_format(start_time)
        if err:
            return None, err
        _, err = validate.validate_time_format(end_time)
        if err:
            return None, err

        if not weekdays:
            return None, "Selecione pelo menos um dia da semana."

        lines = self.get_time_slot_tuple(start_time, end_time, semester, year, weekdays)
        return lines

    def get_selected_vars(self):
        start_time = self.start_time_var.get()
        end_time = self.end_time_var.get()
        semester = self.semester_var.get()
        year = self.year_var.get()
        selected_weekdays = [day for day, var in self.weekday_vars.items() if var.get()]
        return start_time, end_time, semester, year, selected_weekdays

    def get_time_slot_tuple(self, start_time, end_time, semester, year, weekdays):
        lines = [
            (start_time, end_time, weekday, semester, year) for weekday in weekdays
        ]

        return lines, None
