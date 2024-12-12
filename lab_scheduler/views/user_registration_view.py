from lab_scheduler.views.templates.form_popup_template import FormPopup
import tkinter as tk
from tkinter import messagebox

from lab_scheduler.views.templates.form_popup_template import FormPopup


class UserView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Usuário")

    def create_widgets(self):
        user_registration_section = self.add_section(
            self, "Cadastro de Usuários"
        )

        self.add_button(
            parent=user_registration_section,
            text="Cadastar Usuário",
            command=self.open_user_registration,
            row=1,
            column=0,
            columnspan=4,
        )

        user_management_section = self.add_section(self, "Gerenciamento dos Usuários")

        self.user_name = tk.StringVar(value=str(""))
        field_name = "Nome do usuário"
        self.add_entry(
            parent=user_management_section,
            label_text=field_name,
            variable=self.user_name,
            row=2,
            column=1,
        )

        self.add_button(
            parent=user_management_section,
            text="Carregar Usuários",
            command=self.load_users,
            row=3,
            column=0,
            columnspan=4,
        )

        columns_map = {
            "Id": "id",
            "Nome": "nm_usuario",
            "Posição": "id_tipo_usuario",
            "Documento de Identificação": "ds_identificacao"
        }
        columns_configs = [
            {"column": col, "text": desc, "width": 100, "anchor": "center"}
            for desc, col in columns_map.items()
        ]
        self.tree = self.add_treeview(
            parent=user_management_section,
            columns_configs=columns_configs,
            row=4,
            column=0,
            columnspan=4,
        )

        self.add_button(
            parent=user_management_section,
            text="Atualizar Usuário",
            command=self.update_user,
            row=5,
            column=0,
            columnspan=2,
        )

        self.add_button(
            parent=user_management_section,
            text="Excluir Usuário",
            command=self.delete_user,
            row=5,
            column=2,
            columnspan=2,
        )

        self.add_button(
            parent=user_management_section,
            text="Fechar",
            command=self.destroy,
            row=6,
            column=0,
            columnspan=4,
        )

    def load_users(self):

        user_name = self.user_name.get()
        try:
            users = self.controller.load_users(
                user_name
            )

            table_data = users
            self.display_users(table_data)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar usuários: {e}")

    def display_users(self, table_data):
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
            nm_usuario_index = list(self.tree["columns"]).index("nm_usuario")
            id_tipo_usuario_index = list(self.tree["columns"]).index("id_tipo_usuario")
            ds_identificacao_index = list(self.tree["columns"]).index("ds_identificacao")

            id_value = values[id_index]
            nm_usuario = values[nm_usuario_index]
            id_tipo_usuario = values[id_tipo_usuario_index]
            ds_identificacao = values[ds_identificacao_index]

            return id_value, nm_usuario, id_tipo_usuario, ds_identificacao
        except (ValueError, IndexError):
            return None

    def update_user(self):
        row_data = self.get_selected_row_data()
        if row_data:
            id_value, nm_usuario, id_tipo_usuario, ds_identificacao = row_data

            self.controller.update_users(
                id_value, nm_usuario, id_tipo_usuario, ds_identificacao
            )
        else:
            print("Linha não selecionada")

    def delete_user(self):
        usr_id = self.get_selected_id()
        if usr_id is None:
            return
        confirm = messagebox.askyesno(
            "Confirmação", "Tem certeza de que deseja excluir o usuário selecionado?"
        )
        if confirm:
            try:
                self.controller.delete_user(usr_id)
                messagebox.showinfo("Sucesso", "Usuário excluído com sucesso.")
                self.load_users()
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao excluir usuário: {e}")

    def open_user_registration(self):
        self.controller.register_user()


class UpdateUserView(FormPopup):
    def __init__(self, parent, controller, usr_id, nm_usuario, id_tipo_usuario, ds_identificacao):
        self.controller = controller
        self.full_name_var = tk.StringVar(value=nm_usuario)
        self.position_var = tk.StringVar(value=id_tipo_usuario)
        self.id_doc_var = tk.StringVar(value=ds_identificacao)
        self.usr_id = tk.StringVar(value=usr_id)

        super().__init__(parent, title="Cadastrar Usuário")

    def create_widgets(self):
        self.add_label(self, "Cadastro de Usuário", row=0, column=0, columnspan=2)

        full_name_entry = self.add_entry(
            self,
            label_text="Nome Completo",
            variable=self.full_name_var,
            row=1,
            required=True
        )
        full_name_entry.focus()

        self.add_entry(
            self,
            label_text="Posição",
            variable=self.position_var,
            row=2,
            required=True
        )

        self.add_entry(
            self,
            label_text="Documento de Identificação",
            variable=self.id_doc_var,
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

        usr_id = self.usr_id.get().strip()
        full_name = self.full_name_var.get().strip()
        role = self.position_var.get().strip()
        doc = self.id_doc_var.get().strip()

        try:
            self.controller.update_user(usr_id, full_name, role, doc)
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao registrar usuário: {e}")


class UserRegistrationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Cadastrar Usuário")

    def create_widgets(self):
        self.add_label(self, "Cadastro de Usuário", row=0, column=0, columnspan=2)

        self.full_name_var = tk.StringVar()
        full_name_entry = self.add_entry(
            self,
            label_text="Nome Completo",
            variable=self.full_name_var,
            row=1,
            required=True
        )
        full_name_entry.focus()

        self.position_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Posição",
            variable=self.position_var,
            row=2,
            required=True
        )

        self.id_doc_var = tk.StringVar()
        self.add_entry(
            self,
            label_text="Documento de Identificação",
            variable=self.id_doc_var,
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

        full_name = self.full_name_var.get().strip()
        role = self.position_var.get().strip()  # TODO: Aqui deve ser uma ComboBox
        doc = self.id_doc_var.get().strip()  # TODO: Aqui pode ter validação de documento

        try:
            self.controller.create_user(full_name, role, doc)
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao registrar usuário: {e}")
