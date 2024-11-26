import calendar
import datetime
from datetime import datetime as dt

from lab_scheduler.controllers import static
from lab_scheduler.database.models import TimeSlotsModel
from lab_scheduler.views import (
    TimeSlotsRegistrationView,
    TimeSlotsView,
    UpdateTimeSlotView,
)

def get_months(semester):
    start_month = static.SEMESTERS_INFO[semester]["start_month"]
    end_month = static.SEMESTERS_INFO[semester]["end_month"]
    return start_month,end_month

class TimeSlotsController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = TimeSlotsView(root, self)
        self.model = TimeSlotsModel(db=db)

    def get_time_slots(self, semester, year):
        start_month, end_month = get_months(semester)
        
        time_slots = self.model.get_time_slots_summary(start_month, end_month, year)
        print(time_slots)
        for time_slot in time_slots:
            print(time_slot)
            print(time_slot["nr_dia_semana"])
            print(static.WEEKDAYS)
            time_slot["ds_dia_semana"] = static.WEEKDAYS[time_slot["nr_dia_semana"]]
        print(f"time_slots: {time_slots}")
        
        return time_slots


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
        self.model = TimeSlotsModel(db=db)

    def save_time_slots(self, timeslots_to_save):
        _, _, _, semester, year = timeslots_to_save[0]
        start_month, end_month = get_months(semester)
        
        time_slots_saved = self.model.get_time_slots_summary(start_month, end_month, year)
        print(time_slots_saved)
        for time_slot in time_slots_saved:
            time_slot["ds_dia_semana"] = static.WEEKDAYS[time_slot["nr_dia_semana"]]
            
        overlaping_timeslots = self.find_overlapping_timeslots(timeslots_to_save, time_slots_saved)
        if overlaping_timeslots:
            raise ValueError(self.generate_error_message(overlaping_timeslots))
           
        inserts = self.get_inserts(timeslots_to_save)
        
        return self.model.save_time_slots(inserts)
    
    def generate_error_message(self, overlapping_timeslots):
        overlaps_by_day = {}
        for slot in overlapping_timeslots:
            day_name = slot['ds_dia_semana']
            time_range = f"{slot['hr_ini']} - {slot['hr_fim']}"
            overlaps_by_day.setdefault(day_name, []).append(time_range)
        
        message_lines = ["\nOs seguintes horários apresentam conflitos com os horários já existentes."]
        for day_name, times in overlaps_by_day.items():
            message_lines.append(f"\n{day_name}:")
            for time_range in times:
                message_lines.append(f"- {time_range}")
        message_lines.append("\nPor favor, revise esses horários para evitar sobreposições.")
        
        error_message = "\n".join(message_lines)
        return error_message
    
    def find_overlapping_timeslots(self, timeslots_to_save, time_slots_saved):
        timeslots_to_save_by_day = {}
        timeslots_saved_by_day = {}

        for start_time_str, end_time_str, weekday, _, _ in timeslots_to_save:
            start_time = dt.strptime(start_time_str, '%H:%M').time()
            end_time = dt.strptime(end_time_str, '%H:%M').time()
            timeslots_to_save_by_day.setdefault(weekday, []).append((start_time, end_time))

        for slot in time_slots_saved:
            start_time = dt.strptime(slot['hr_ini'], '%H:%M').time()
            end_time = dt.strptime(slot['hr_fim'], '%H:%M').time()
            timeslots_saved_by_day.setdefault(slot['ds_dia_semana'], []).append((start_time, end_time))

        overlapping_timeslots = []
        added_timeslots = set()

        for weekday in timeslots_to_save_by_day:
            if weekday in timeslots_saved_by_day:
                for start_to_save, end_to_save in timeslots_to_save_by_day[weekday]:
                    timeslot_id = (weekday, start_to_save, end_to_save)
                    for start_saved, end_saved in timeslots_saved_by_day[weekday]:
                        slots_overlap = (start_to_save < end_saved) and (start_saved < end_to_save)
                        if slots_overlap:
                            if timeslot_id not in added_timeslots:
                                overlapping_timeslots.append({
                                    'ds_dia_semana': weekday,
                                    'hr_ini': start_to_save.strftime('%H:%M'),
                                    'hr_fim': end_to_save.strftime('%H:%M'),
                                })
                                added_timeslots.add(timeslot_id)
                            break

        return overlapping_timeslots

    
    def get_inserts(self, timeslots_to_save):
        inserts = []
        for timeslot in timeslots_to_save:
            start_time_str, end_time_str, weekday_name, semester_number, year_str = timeslot
            semester_number = str(semester_number)
            year = int(year_str)

            weekday_number = static.WEEKDAYS_MAP[weekday_name]
            semester_info = static.SEMESTERS_INFO[semester_number]
            start_month = semester_info["start_month"]
            end_month = semester_info["end_month"]

            start_date = datetime.date(year, start_month, 1)
            last_day = calendar.monthrange(year, end_month)[1]
            end_date = datetime.date(year, end_month, last_day)

            date = start_date
            delta = datetime.timedelta(days=1)
            while date <= end_date:
                if date.weekday() == weekday_number:
                    insert_record = (
                        date.strftime('%Y-%m-%d'),
                        start_time_str,
                        end_time_str,
                    )
                    inserts.append(insert_record)
                date += delta
        return inserts

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
