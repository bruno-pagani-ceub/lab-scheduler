from datetime import datetime

def validate_time_format(time:str):
    try: 
        return datetime.strptime(time, "%H:%M"), ""
    except ValueError:
        return None, "Formato de hora inválido. Use HH:MM."
    except Exception as e:
        return None, f"Erro de aplicação: {e}"
    
def valid_time_slot(start_dt:datetime, end_dt:datetime):
    return end_dt <= start_dt

def new_slot_overlaps(start_dt:datetime, end_dt:datetime, time_slots):
    if not time_slots:
        return False
    for slot in time_slots:
        if not (end_dt <= slot[0] or start_dt >= slot[1]):
            return True
    return False

def validade_timeslot_year(year:str):
    return year.isdigit() and (2024 <= int(year) < 2100)

