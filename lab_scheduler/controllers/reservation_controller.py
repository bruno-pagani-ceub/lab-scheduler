from lab_scheduler.views import ReservationView, LabReservationView, ViewReservationView
from lab_scheduler.database.models import ReservationModel, ViewReservationModel, LabReservationModel
import datetime
from lab_scheduler import static


class ReservationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.model = ReservationModel(db=db)
        self.view = ReservationView(root, self)

    def manage_reservations(self):
        ViewReservationController(self.root, self.db)

    def reserve_lab(self):
        LabReservationController(self.root, self.db)


class LabReservationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.model = LabReservationModel(db=db)
        self.view = LabReservationView(root, self)

    def get_user_data(self, user_id):
        result = self.model.get_user(user_id)
        if result:
            return result
        else:
            return ""

    def retrieve_lab(self):
        lab_list = self.model.get_lab_list()
        return lab_list

    def convert(self, timeslots):
        for key, value in timeslots.items():
            if key not in ["hr_inicio", "hr_fim"]:
                continue
            total_seconds = value.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            timeslots[key] = f"{hours:02}:{minutes:02}"
        return timeslots

    def get_available_timeslots(self, date, lab):
        datetime_date = datetime.datetime.strptime(date, "%d/%m/%Y")
        adjusted_date = datetime_date.strftime("%Y-%m-%d")
        return self.model.get_available_timeslots(
            adjusted_date, lab
        )

    
    def get_timeslots_weekday(self, lab, weekday, semester, year):
        return self.model.get_available_timeslots_weekday(
            lab, weekday, semester, year
        )

    def submit_single_reservation(self, selected_items):
        self.model.make_single_reservation(selected_items["user"], selected_items["type"],
                                           selected_items["lab"], selected_items["timeslot"])

    def submit_recurrent_reservation(self, selected_items):
        success_check = self.model.make_recurrent_reservation(
            selected_items["user"], selected_items["type"], selected_items["lab"], selected_items["weekday"],
            selected_items["timeslot"], selected_items["semester"], selected_items["year"]
        )
        if success_check:
            return True
        else:
            return False

class ViewReservationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.model = ViewReservationModel(db=db)
        self.view = ViewReservationView(root, self)

    def search_all(self):
        all_list = self.model.search_all()
        return all_list