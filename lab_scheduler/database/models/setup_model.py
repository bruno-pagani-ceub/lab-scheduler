from lab_scheduler.database.sql import SQL

class SetupModel:
    def __init__(self, db):
        self.db: SQL = db
    
    def ensure_usuario(self):
        '''Ensures user table exists and has all the correct columns and types'''
        pass

    def ensure_horario(self):
        '''Ensures time slots table exists and has all the correct columns and types'''
        pass

    def ensure_laboratorio(self):
        '''Ensures lab table exists and has all the correct columns and types'''
        pass

    def ensure_horario_laboratorio(self):
        '''Ensures time slots, lab associative table exists and has all the correct columns and types'''
        pass

    def ensure_reserva(self):
        '''Ensures reservation table exists and has all the correct columns and types'''
        pass

    def ensure_tables(self):
        self.ensure_usuario()
        self.ensure_horario()
        self.ensure_laboratorio()
        self.ensure_horario_laboratorio()
        self.ensure_reserva()
    

