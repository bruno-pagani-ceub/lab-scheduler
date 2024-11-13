from lab_scheduler.views.templates.form_popup_template import FormPopup
import tkinter as tk
from tkinter import messagebox

class UserView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Usuário")

    def create_widgets(self):
        pass

class UpdateUserView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent, title="Atualizar Usuário")

    def create_widgets(self):
        pass
    

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
        role = self.position_var.get().strip() # TODO: Aqui deve ser uma ComboBox
        doc = self.id_doc_var.get().strip() # TODO: Aqui pode ter validação de documento

        try:
            self.controller.create_user(full_name, role, doc)
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao registrar usuário: {e}")
