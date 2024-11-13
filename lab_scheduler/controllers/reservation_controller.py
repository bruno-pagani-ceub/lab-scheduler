from lab_scheduler.views import ReservationView, LabReservationView
from lab_scheduler.database.models import ReservationModel


class ReservationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = ReservationView(root, self)
        self.model = ReservationModel(db=db)

class LabReservationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = LabReservationView(root, self)
        
    