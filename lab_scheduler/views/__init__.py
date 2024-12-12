from lab_scheduler.views.main_view import MainView
from lab_scheduler.views.user_registration_view import UserView, UserRegistrationView, UpdateUserView
from lab_scheduler.views.timeslots_view import TimeSlotsView, TimeSlotsRegistrationView, UpdateTimeSlotView
from lab_scheduler.views.lab_view import LabView, LabRegistrationView, UpdateLabView
from lab_scheduler.views.reservation_view import ReservationView, LabReservationView, ViewReservationView
from lab_scheduler.views.report_gen_view import ScheduleGenerationView

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
    "ViewReservationView",
    "ScheduleGenerationView",
]