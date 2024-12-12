from lab_scheduler.controllers.labs_controller import LabController
from lab_scheduler.controllers.reports_controller import ScheduleGenerationController
from lab_scheduler.controllers.reservation_controller import (
    LabReservationController,
    ReservationController,
    ViewReservationController
)
from lab_scheduler.controllers.timeslots_controller import TimeSlotsController
from lab_scheduler.controllers.user_controller import (
    UserController,
    UserRegistrationController,
)
from lab_scheduler.database.models import SetupModel
from lab_scheduler.views import MainView


class MainController:
    """Controller for the main application."""

    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = MainView(root, self)
        self.model = SetupModel(db=db)

        self.view.pack(fill="both", expand=True)
        self.model.ensure_tables()

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
        TimeSlotsController(self.root, self.db)
