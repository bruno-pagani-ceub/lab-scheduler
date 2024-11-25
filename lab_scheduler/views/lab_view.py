from lab_scheduler.views.templates.form_popup_template import FormPopup

class LabView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Gerenciar Laboratórios")

    def create_widgets(self):
        pass

class LabRegistrationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Cadastar Laboratório")

    def create_widgets(self):
        pass

class UpdateLabView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Alterar um Laboratório")

    def create_widgets(self):
        pass