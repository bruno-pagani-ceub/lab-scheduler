from lab_scheduler.database.sql import SQL


class TimeSlotsModel:
    def __init__(self, db):
        self.db: SQL = db

    def save_time_slots(self, inserts):
        query = "INSERT INTO tb_horario (dt_dia, hr_inicio, hr_fim) VALUES (%s, %s, %s)"
        return self.db.insert_many(query, inserts)

    def count_days_with_timeslot(self, weekday_number, start_month, end_month, year):
        params = {
            "weekday": weekday_number,
            "start_month": start_month,
            "end_month": end_month,
            "year": year,
        }
        query = """
            SELECT
                COUNT(1)
            FROM
                tb_horario
            WHERE
                WEEKDAY(dt_dia) = @weekday
                AND MONTH(dt_dia) BETWEEN @start_month AND @end_month;
                AND YEAR(dt_dia) = @year;
        """
        return self.db.get_int(query, params)
        
    def get_time_slots_summary(self, start_month, end_month, year):
        query = """
            SELECT DISTINCT
                WEEKDAY(dt_dia) AS nr_dia_semana,
                DATE_FORMAT(hr_inicio, '%H:%i') AS hr_ini,
                DATE_FORMAT(hr_fim, '%H:%i') AS hr_fim
            FROM
                tb_horario
            WHERE
                YEAR(dt_dia) = %s
                AND MONTH(dt_dia) BETWEEN %s AND %s
            ORDER BY 
                nr_dia_semana,
                hr_ini,
                hr_fim;
        """

        return self.db.get_list(query, (year, start_month, end_month))

        # """
        # Logic for getting timeslots for a week
        # in a semester in a year from database.

        # Example: [
        #     {"ds_dia_semana": "Segunda-feira", "hr_ini": "07:40", "hr_fim": "09:20"},
        #     {"ds_dia_semana": "Segunda-feira", "hr_ini": "09:20", "hr_fim": "11:00"},
        #     {"ds_dia_semana": "Terça-feira", "hr_ini": "07:40", "hr_fim": "09:20"},
        #     {"ds_dia_semana": "Terça-feira", "hr_ini": "09:20", "hr_fim": "11:00"},
        #     {"ds_dia_semana": "Terça-feira", "hr_ini": "11:00", "hr_fim": "12:40"},
        #     {"ds_dia_semana": "Quarta-feira", "hr_ini": "09:20", "hr_fim": "11:00"},
        #     {"ds_dia_semana": "Quarta-feira", "hr_ini": "11:00", "hr_fim": "12:40"},
        # ]
        # """
        # return [
        #     {"ds_dia_semana": "Segunda-feira", "hr_ini": "07:40", "hr_fim": "09:20"},
        #     {"ds_dia_semana": "Segunda-feira", "hr_ini": "09:20", "hr_fim": "11:00"},
        #     {"ds_dia_semana": "Terça-feira", "hr_ini": "07:40", "hr_fim": "09:20"},
        #     {"ds_dia_semana": "Terça-feira", "hr_ini": "09:20", "hr_fim": "11:00"},
        #     {"ds_dia_semana": "Terça-feira", "hr_ini": "11:00", "hr_fim": "12:40"},
        #     {"ds_dia_semana": "Quarta-feira", "hr_ini": "09:20", "hr_fim": "11:00"},
        #     {"ds_dia_semana": "Quarta-feira", "hr_ini": "11:00", "hr_fim": "12:40"},
        # ]  ## TODO: remove, added for testing
