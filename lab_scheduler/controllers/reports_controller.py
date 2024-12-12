from tkinter import messagebox
from lab_scheduler.database.models.report_model import ReportModel
from lab_scheduler.views.report_gen_view import ScheduleGenerationView

class ScheduleGenerationController:
    def __init__(self, root, db):
        self.root = root
        self.model = ReportModel(db)
        self.open_schedule_view()

    def open_schedule_view(self):
        try:
            schedule_data = self.model.get_weekly_schedule()
            ScheduleGenerationView(self.root, schedule_data)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar o cronograma: {e}")


