from lab_scheduler.database.models import ReportModel
from lab_scheduler.services.weekly_report import Folder
from lab_scheduler.views import ScheduleGenerationView


class ScheduleGenerationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = ScheduleGenerationView(root, self)
        self.report_generator = Folder()
        self.model = ReportModel(db=db)
        
    def _get_week_schedule_data(self): 
        pass

    def generate_report(self):
        data = self._get_week_schedule_data()
        self.report_generator.generate_report(data)
        pass