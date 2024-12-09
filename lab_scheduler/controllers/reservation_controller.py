from lab_scheduler.views import ReservationView, LabReservationView
from lab_scheduler.database.models import ReservationModel, LabReservationModel
from datetime import datetime
from lab_scheduler import static


class ReservationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = ReservationView(root, self)
        self.model = ReservationModel(db=db)

    def manage_reservations(self):
        pass

    def reserve_lab(self):
        pass

class LabReservationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = LabReservationView(root, self)
        self.model = LabReservationModel(db=db)
    

    def get_user_data(self, user_id):
        result = LabReservationModel(db=self.db).get_user(user_id)
        if result:
            return result
        else:
            return ""
    
    def retrieve_lab(self):
        lab_list = LabReservationModel(db=self.db).get_lab_list()
        return lab_list
    
    def convert(self, timeslots):
        for key, value in list(timeslots.items())[1:]:
            total_seconds = value.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            timeslots[key] = f"{hours:02}:{minutes:02}"
        return timeslots

    def get_available_timeslots(self, date, lab):
        datetime_date = datetime.strptime(date, "%d/%m/%Y")
        adjusted_date = datetime_date.strftime("%Y-%m-%d")
        available_timeslots = LabReservationModel(db=self.db).get_available_timeslots(adjusted_date, lab)
        return available_timeslots

    def get_timeslots_weekday(self, weekday, semester, year):
        start_date = LabReservationModel(db=self.db).get_base_date(weekday, semester, year)
        timeslots = LabReservationModel(db=self.db).get_available_timeslots_weekday(start_date['base_date'])
        return timeslots

    def submit_single_reservation(self, selected_items):
        user, text, lab, time = selected_items["user"], selected_items["type"], selected_items["lab"], selected_items["timeslot"]
        self.model.make_single_reservation(user, text, lab, time)

    def submit_recurrent_reservation(self, selected_items):
        user, text, lab, weekday, timeslot, semester, year= selected_items["user"], selected_items["type"], selected_items["lab"], selected_items["weekday"], selected_items["timeslot"], selected_items["semester"], selected_items["year"]
        self.model.make_recurrent_reservation(user, text, lab, weekday, timeslot, semester, year)
