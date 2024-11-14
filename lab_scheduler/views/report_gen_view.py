from lab_scheduler.views.templates.form_popup_template import FormPopup

class ScheduleGenerationView(FormPopup):
    def __init__(self, parent, controller):
        self.controller = controller
        self.time_slots = []
        super().__init__(parent, title="Gerar cronograma semanal")

    def create_widgets(self):
        pass