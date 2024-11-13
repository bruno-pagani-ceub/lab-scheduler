from views import MainView

from .timeslots_controller import TimeSlotsRegistrationController
from .user_controller import UserController, UserRegistrationController
from .labs_controller import LabController
from .reservation_controller import ReservationController, LabReservationController
from .reports_controller import ScheduleGenerationController

class MainController:
    """Controller for the main application."""

    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = MainView(root, self)
        self.view.pack(fill="both", expand=True)

    def register_user(self):
        UserRegistrationController(self.root, self.db)

    def reserve_lab(self):
        LabReservationController(self.root, self.db)

    def generate_schedule(self):
        ScheduleGenerationController(self.root, self.db)

    def manage_users(self):
        UserController(self.root, self.db)

    def manage_reservations(self):
        ReservationController(self.root, self.db)

    def manage_labs(self):
        LabController(self.root, self.db)

    def manage_time_slots(self):
        TimeSlotsRegistrationController(self.root, self.db)