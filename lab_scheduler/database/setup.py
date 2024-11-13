from .sql import SQL

def create_usuario(db:SQL):
    '''Creates user table if it doesn't exist'''
    pass

def create_horario(db:SQL):
    '''Creates time slots table if it doesn't exist'''
    pass

def create_laboratorio(db:SQL):
    '''Creates lab table if it doesn't exist'''
    pass

def create_horario_laboratorio(db:SQL):
    '''Creates time slots, lab associative table if it doesn't exist'''
    pass

def create_reserva(db:SQL):
    '''Creates reservation table if it doesn't exist'''
    pass

def ensure_tables(db:SQL):
    create_usuario(db=db)
    create_horario(db=db)
    create_laboratorio(db=db)
    create_horario_laboratorio(db=db)
    create_reserva(db=db)