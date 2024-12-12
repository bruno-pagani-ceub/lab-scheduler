from lab_scheduler.views.templates.form_popup_template import FormPopup
import tkinter as tk
from tkinter import messagebox

class LabView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Gerenciar Laboratórios")

    def create_widgets(self):
        lab_registration_section = self.add_section(
            self, "Cadastro de Laboratórios"
        )

        self.add_button(
            parent=lab_registration_section,
            text="Cadastar Laboratórios",
            command=self.open_lab_registration,
            row=1,
            column=0,
            columnspan=4,
        )

        lab_management_section = self.add_section(self, "Gerenciamento dos Laboratórios")

        self.ds_sala_selected = tk.StringVar(value=str(""))
        field_name = "Sala do laboratório"
        self.add_entry(
            parent=lab_management_section,
            label_text=field_name,
            variable=self.ds_sala_selected,
            row=2,
            column=1,
        )

        self.add_button(
            parent=lab_management_section,
            text="Carregar Laboratórios",
            command=self.load_labs,
            row=3,
            column=0,
            columnspan=4,
        )

        columns_map = {
            "Id": "id",
            "Sala": "ds_sala",
            "Bloco": "ds_bloco",
            "Qtd de computadores": "qtd_pcs"
        }
        columns_configs = [
            {"column": col, "text": desc, "width": 100, "anchor": "center"}
            for desc, col in columns_map.items()
        ]
        self.tree = self.add_treeview(
            parent=lab_management_section,
            columns_configs=columns_configs,
            row=4,
            column=0,
            columnspan=4,
        )

        self.add_button(
            parent=lab_management_section,
            text="Atualizar Laboratório",
            command=self.update_lab,
            row=5,
            column=0,
            columnspan=2,
        )

        self.add_button(
            parent=lab_management_section,
            text="Excluir Laboratório",
            command=self.delete_lab,
            row=5,
            column=2,
            columnspan=2,
        )

        self.add_button(
            parent=lab_management_section,
            text="Fechar",
            command=self.destroy,
            row=6,
            column=0,
            columnspan=4,
        )

    def load_labs(self):

        ds_sala_selected = self.ds_sala_selected.get()
        try:
            labs = self.controller.load_labs(
                ds_sala_selected,
            )

            table_data = labs
            self.display_labs(table_data)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar Laboratórios: {e}")

    def display_labs(self, table_data):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for line in table_data:
            self.tree.insert(
                "",
                "end",
                values=(tuple(col for col in line.values())),
            )

    def get_selected_id(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return None

        item = self.tree.item(selected_item[0])
        values = item.get("values", [])

        try:
            id_index = list(self.tree["columns"]).index("id")
            return values[id_index]
        except (ValueError, IndexError):
            return None

    def get_selected_row_data(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return None

        item = self.tree.item(selected_item[0])
        values = item.get("values", [])

        if not values:
            return None

        try:
            id_index = list(self.tree["columns"]).index("id")
            ds_bloco_index = list(self.tree["columns"]).index("ds_bloco")
            ds_sala_index = list(self.tree["columns"]).index("ds_sala")
            qtd_pcs_index = list(self.tree["columns"]).index("qtd_pcs")

            id_value = values[id_index]
            ds_bloco = values[ds_bloco_index]
            ds_sala = values[ds_sala_index]
            qtd_pcs = values[qtd_pcs_index]

            return id_value, ds_bloco, ds_sala, qtd_pcs
        except (ValueError, IndexError):
            return None

    def update_lab(self):
        row_data = self.get_selected_row_data()
        if row_data:
            id_value, ds_bloco, ds_sala, qtd_pcs = row_data

            self.controller.update_labs(
                id_value, ds_bloco, ds_sala, qtd_pcs
            )
        else:
            print("Linha não selecionada")

    def delete_lab(self):
        lab_id = self.get_selected_id()
        if lab_id is None:
            return
        confirm = messagebox.askyesno(
            "Confirmação", "Tem certeza de que deseja excluir o Laboratório selecionado?"
        )
        if confirm:
            try:
                self.controller.delete_lab(lab_id)
                messagebox.showinfo("Sucesso", "Laboratório excluído com sucesso.")
                self.load_labs()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao excluir Laboratório: {e}")

    def open_lab_registration(self):
        self.controller.register_lab()

class LabRegistrationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Cadastar Laboratório")

    def create_widgets(self):
        self.add_label(self, "Cadastro de Laboratório", row=0, column=0, columnspan=2)

        self.ds_bloco_var = tk.StringVar()
        ds_bloco_entry = self.add_entry(
            self,
            label_text="Bloco",
            variable=self.ds_bloco_var,
            row=1,
            required=True
        )
        ds_bloco_entry.focus()

        self.ds_sala_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Sala",
            variable=self.ds_sala_var,
            row=2,
            required=True
        )

        self.qtd_pcs_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Qtd de computadores",
            variable=self.qtd_pcs_var,
            row=3,
            required=True
        )

        self.add_button(
            self,
            text="Registrar",
            command=self.submit,
            row=4,
            column=0,
            columnspan=2
        )

    def submit(self):
        if not self.check_required_fields():
            return

        ds_bloco = self.ds_bloco_var.get().strip()
        ds_sala = self.ds_sala_var.get().strip()
        qtd_pcs = self.qtd_pcs_var.get().strip()

        try:
            self.controller.create_lab(ds_bloco, ds_sala, qtd_pcs)
            messagebox.showinfo("Sucesso", "Laboratório registrado com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao registrar Laboratório: {e}")

class UpdateLabView(FormPopup):
    def __init__(self, parent, controller,lab_id, ds_bloco, ds_sala, qtd_pcs):
        self.controller = controller
        self.time_slots = []
        self.controller = controller
        self.ds_bloco = tk.StringVar(value=ds_bloco)
        self.ds_sala = tk.StringVar(value=ds_sala)
        self.qtd_pcs = tk.StringVar(value=qtd_pcs)
        self.lab_id = tk.StringVar(value=lab_id)

        super().__init__(parent, title="Alterar um Laboratório")

    def create_widgets(self):
        ds_bloco_entry = self.add_entry(
            self,
            label_text="Bloco",
            variable=self.ds_bloco,
            row=1,
            required=True
        )
        ds_bloco_entry.focus()

        self.add_entry(
            self,
            label_text="Sala",
            variable=self.ds_sala,
            row=2,
            required=True
        )

        self.add_entry(
            self,
            label_text="Qtd de computadores",
            variable=self.qtd_pcs,
            row=3,
            required=True
        )

        self.add_button(
            self,
            text="Atualizar",
            command=self.submit,
            row=4,
            column=0,
            columnspan=2
        )

    def submit(self):
        if not self.check_required_fields():
            return

        lab_id = self.lab_id.get().strip()
        ds_bloco = self.ds_bloco.get().strip()
        ds_sala = self.ds_sala.get().strip()
        qtd_pcs = self.qtd_pcs.get().strip()

        try:
            self.controller.update_lab(lab_id, ds_bloco, ds_sala, qtd_pcs)
            messagebox.showinfo("Sucesso", "Laboratorio atualizado com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao atualizar laboratório: {e}")

