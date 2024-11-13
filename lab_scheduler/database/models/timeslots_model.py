from lab_scheduler.database.sql import SQL

class TimeSlotsModel:
    def __init__(self, db):
        self.db: SQL = db
    
    def get_time_slots(self, semester, year):
        '''
        Logic for getting timeslots for a week
        in a semester in a year from database.
        
        Example: [
            {"ds_dia_semana": "Segunda-feira", "hr_ini": "07:40", "hr_fim": "09:20"},        
            {"ds_dia_semana": "Segunda-feira", "hr_ini": "09:20", "hr_fim": "11:00"},        
            {"ds_dia_semana": "Terça-feira", "hr_ini": "07:40", "hr_fim": "09:20"},        
            {"ds_dia_semana": "Terça-feira", "hr_ini": "09:20", "hr_fim": "11:00"},        
            {"ds_dia_semana": "Terça-feira", "hr_ini": "11:00", "hr_fim": "12:40"},        
            {"ds_dia_semana": "Quarta-feira", "hr_ini": "09:20", "hr_fim": "11:00"},        
            {"ds_dia_semana": "Quarta-feira", "hr_ini": "11:00", "hr_fim": "12:40"},        
        ]
        '''
        return [
            {"ds_dia_semana": "Segunda-feira", "hr_ini": "07:40", "hr_fim": "09:20"},        
            {"ds_dia_semana": "Segunda-feira", "hr_ini": "09:20", "hr_fim": "11:00"},        
            {"ds_dia_semana": "Terça-feira", "hr_ini": "07:40", "hr_fim": "09:20"},        
            {"ds_dia_semana": "Terça-feira", "hr_ini": "09:20", "hr_fim": "11:00"},        
            {"ds_dia_semana": "Terça-feira", "hr_ini": "11:00", "hr_fim": "12:40"},        
            {"ds_dia_semana": "Quarta-feira", "hr_ini": "09:20", "hr_fim": "11:00"},        
            {"ds_dia_semana": "Quarta-feira", "hr_ini": "11:00", "hr_fim": "12:40"},        
        ] ## TODO: remove, added for testing