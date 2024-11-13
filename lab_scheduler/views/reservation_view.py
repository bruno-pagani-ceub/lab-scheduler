from lab_scheduler.views.templates.form_popup_template import FormPopup

class ReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Reservas")

    def create_widgets(self):
        pass

class LabReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Registrar Reserva")

    def create_widgets(self):
        pass

class UpdateReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Atualizar Reserva")

    def create_widgets(self):
        pass