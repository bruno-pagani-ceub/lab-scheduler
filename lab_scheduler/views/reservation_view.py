from lab_scheduler.views.templates.form_popup_template import FormPopup

class ReservationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Reservas")

    def create_widgets(self):
<<<<<<< Updated upstream
        pass
=======
        main_section = self.add_section(self, "Opções")

        self.add_button(
            main_section,
            "Cadastrar reserva",
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

>>>>>>> Stashed changes

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