from .main_view import MainView
from .user_registration_view import UserView, UserRegistrationView, UpdateUserView
from .timeslots_view import TimeSlotsView, TimeSlotsRegistrationView, UpdateTimeSlotView
from .lab_view import LabView, LabRegistrationView, UpdateLabView
from .reservation_view import ReservationView, LabReservationView, UpdateReservationView
from .report_gen_view import ScheduleGenerationView

__all__ = [
    "MainView",
    "UserView",
    "UserRegistrationView",
    "UpdateUserView",
    "LabView",
    "LabRegistrationView",
    "UpdateLabView",
    "TimeSlotsView",
    "TimeSlotsRegistrationView",
    "UpdateTimeSlotView",
    "ReservationView",
    "LabReservationView",
    "UpdateReservationView",
    "ScheduleGenerationView",
]