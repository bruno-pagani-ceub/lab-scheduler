from lab_scheduler.views import TimeSlotsRegistrationView, TimeSlotsView, UpdateTimeSlotView
from lab_scheduler.database.models import TimeSlotsModel


class TimeSlotsController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = TimeSlotsView(root, self)
        self.model = TimeSlotsModel(db=db)

    def get_time_slots(self, semester, year):
        """Logic for getting concatanated timeslots for a week in a semester in a year"""
        return self.model.get_time_slots(self.db, semester, year)


    def update_time_slots(self, start_time, end_time, weekdays, semester, year):
        UpdateTimeSlotsController(
            self.root, self.db, start_time, end_time, weekdays, semester, year
        )

    def register_time_slots(self):
        TimeSlotsRegistrationController(self.root, self.db)


class TimeSlotsRegistrationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = TimeSlotsRegistrationView(root, self)

    def save_time_slots(self, lines_to_save):
        """Logic for Inserting Time Slots in Database."""
        print(f"Lines to save: {lines_to_save}")
        ## TODO: don't forget to write logic for filling associative table


class UpdateTimeSlotsController:
    def __init__(self, root, db, start_time, end_time, weekdays, semester, year):
        self.root = root
        self.db = db
        self.view = UpdateTimeSlotView(
            root, self, start_time, end_time, weekdays, semester, year
        )

    def update_time_slot(self, lines):
        """Logic for Updating Time Slots in Database."""
        print(f"Lines to update: {lines}")
        ## TODO: don't forget to write logic for updating associative table

    def remove_time_slot(self, lines):
        """Logic for Deleting Time Slots in Database."""
        print(f"Lines to remove: {lines}")
        ## TODO: don't forget to write logic for deleting from associative table
