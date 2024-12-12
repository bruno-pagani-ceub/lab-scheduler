from datetime import datetime, timedelta
from lab_scheduler.database.models.report_model import ReportModel
from lab_scheduler.views.report_gen_view import ScheduleGenerationView
from lab_scheduler.services.weekly_report import WeeklySchedule

class ScheduleGenerationController:
    def __init__(self, root, db):
        self.root = root
        self.model = ReportModel(db)
        self.generator = WeeklySchedule()
        ScheduleGenerationView(self.root, self)

    def generate_schedule(self, lab, date):
        start_of_week, end_of_week = self.get_week_range(date)
        data = self.model.get_weekly_schedule(lab, start_of_week, end_of_week)
        doc_name = self.generator.generate_schedule_doc(data, lab, start_of_week)
        return doc_name
    
    def get_labs(self):
        result = self.model.get_labs()
        return {f'{line["ds_bloco"]} - {line["ds_sala"]}' : line["id"] for line in result}
    
    def get_week_range(self, input_date):
        try:
            date = datetime.strptime(input_date, "%d/%m/%Y")
        except:
            raise
        weekday = date.weekday()
        start_of_week = date - timedelta(days=weekday)
        end_of_week = start_of_week + timedelta(days=6)
        
        return start_of_week, end_of_week
        
