WEEKDAYS = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
]

WEEKDAYS_MAP = {v: k for k, v in enumerate(WEEKDAYS)}

SEMESTERS_INFO = {
    "1":{"start_month": 1, "end_month": 6},
    "2":{"start_month": 7, "end_month": 12},
}

SQL_WEEKDAYS_NUMBER = dict(zip(WEEKDAYS, ["2", "3", "4", "5", "6", "7", "1"]))